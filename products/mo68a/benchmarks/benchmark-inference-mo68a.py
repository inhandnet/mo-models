#!/usr/bin/env python3
"""Time one compiled model on Mo 68A (J721S2 / AM68A).

Measures synchronous ONNX Runtime calls with blank input: timing only, not
accuracy, video FPS or power. With --cpu the same graph runs on the Cortex-A72
instead of the C7x-MMA, for an accelerator-versus-CPU comparison.

The model directory is one compiled bundle: the .onnx file in model/, the TIDL
artifacts in artifacts/.
"""
import argparse
import ctypes
import hashlib
import json
import os
import platform
import re
import statistics
import sys
import tempfile
import time
from pathlib import Path

parser = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("model_dir", type=Path,
                    help="compiled bundle: model/<name>.onnx plus artifacts/")
parser.add_argument("--cpu", action="store_true",
                    help="run on the Cortex-A72 instead of the C7x-MMA")
parser.add_argument("--runs", type=int, default=100, metavar="N",
                    help="timed calls (default: %(default)s)")
parser.add_argument("--warmup", type=int, default=5, metavar="N",
                    help="untimed calls first (default: %(default)s)")
parser.add_argument("--threads", type=int, default=2, metavar="N",
                    help="ONNX Runtime threads, --cpu only. J721S2 has two A72 "
                         "cores; more than that is slower, not faster (default: %(default)s)")
parser.add_argument("--output", type=Path, metavar="FILE",
                    help="where to write the record (default: <model>-<target>.json)")
parser.add_argument("--verbose", action="store_true",
                    help="also show the firmware and execution-provider output")
args = parser.parse_args()

# Validate before touching the runtime, and say which input is wrong: these
# messages are the only thing between the user and a 30-line firmware dump.
if args.runs < 2:
    parser.error("--runs must be at least 2")
if args.warmup < 1:
    parser.error("--warmup must be at least 1")
if args.threads != 2 and not args.cpu:
    parser.error("--threads applies to --cpu only")
if not args.model_dir.is_dir():
    parser.error("no such model directory: %s" % args.model_dir)
if not (args.model_dir / "model").is_dir():
    parser.error("%s has no model/ directory; it should hold the .onnx file" % args.model_dir)
models = sorted((args.model_dir / "model").glob("*.onnx"))
if not models:
    parser.error("%s/model holds no .onnx file" % args.model_dir)
if len(models) > 1:
    parser.error("%s/model holds %d .onnx files; it should hold exactly one"
                 % (args.model_dir, len(models)))
if not args.cpu and not (args.model_dir / "artifacts").is_dir():
    parser.error("%s has no artifacts/ directory; compile the model first" % args.model_dir)
if args.output is None:
    args.output = Path("%s-%s.json" % (args.model_dir.name.split("_")[0],
                                       "a72" if args.cpu else "c7x"))

# The execution provider and the vision_apps firmware print from C, straight to
# the file descriptors, so Python-level redirection does not reach them. Take
# over fd 1 and 2 for the rest of the run and keep a duplicate for the result:
# the firmware's teardown lines arrive after the last Python statement, so the
# result would scroll away even if it were printed last. This has to happen
# before onnxruntime is imported, which prints on its own.
_clean, _capture = None, None
if not args.verbose:
    _clean = os.fdopen(os.dup(1), "w")
    _capture = tempfile.NamedTemporaryFile(mode="w+", prefix="benchmark-",
                                           suffix=".log", delete=False)
    os.dup2(_capture.fileno(), 1)
    os.dup2(_capture.fileno(), 2)

import numpy as np
import onnxruntime as ort

if not args.cpu and "TIDLExecutionProvider" not in ort.get_available_providers():
    print("TI ONNX Runtime with TIDLExecutionProvider is required",
          file=_clean or sys.stderr)
    raise SystemExit(2)
options = ort.SessionOptions()
options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
# ONNX Runtime 1.23.0 validates that io-tensor dimensions match the original
# model exactly, but TIDL changes them - extra padding, OD post-processing.
# TI's own wrapper disables both checks for this reason; without them a bundle
# whose detection head was offloaded fails at inference with a misleading
# "Missing Input: <n>" on some Add node. See onnxrt_wrapper.py:247.
options.add_session_config_entry("session.disable_input_validation", "1")
options.add_session_config_entry("session.disable_output_validation", "1")
if args.cpu:
    # Same graph, no accelerator. The artifacts are not loaded at all, so this
    # is the plain float/quantised ONNX running on the A72.
    options.intra_op_num_threads = args.threads
    session = ort.InferenceSession(str(models[0]), sess_options=options,
        providers=["CPUExecutionProvider"], provider_options=[{}])
else:
    session = ort.InferenceSession(str(models[0]), sess_options=options,
        providers=["TIDLExecutionProvider", "CPUExecutionProvider"],
        provider_options=[{"artifacts_folder": str(args.model_dir / "artifacts")}, {}])
inputs = {}
shapes = []
for item in session.get_inputs():
    shapes.append("%s %s %s" % (item.name, "x".join(str(n) for n in item.shape),
                                item.type.replace("tensor(", "").rstrip(")")))
    if item.type not in ("tensor(uint8)", "tensor(float)") or not all(isinstance(n, int) and n > 0 for n in item.shape):
        raise ValueError("Only static uint8 and float32 inputs are supported")
    inputs[item.name] = np.zeros(item.shape, dtype=np.uint8 if item.type == "tensor(uint8)" else np.float32)
def release():
    # The artifacts, the runtime and the C7x firmware move as one set, so the
    # image version is part of the measurement, not decoration.
    values = {}
    path = Path("/etc/inhand-release")
    if path.exists():
        for line in path.read_text().splitlines():
            if "=" in line and not line.startswith("#"):
                key, _, value = line.partition("=")
                values[key.strip()] = value.strip()
    return values

def snapshot():
    # J721S2 exposes no cpufreq policy: the A72 runs at one fixed frequency, so
    # scaling_cur_freq does not exist. Report it as absent rather than crash.
    frequency = Path("/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
    return {
        "load": os.getloadavg()[0],
        "cpu_khz": frequency.read_text().strip() if frequency.exists() else "no-cpufreq",
        "temperatures_mC": {p.parent.name: int(p.read_text()) for p in Path("/sys/class/thermal").glob("thermal_zone*/temp")},
    }
for _ in range(args.warmup):
    session.run(None, inputs)
before = snapshot()
times = []
for _ in range(args.runs):
    start = time.perf_counter_ns()
    outputs = session.run(None, inputs)
    times.append((time.perf_counter_ns() - start) / 1e6)
after = snapshot()
if not all(np.isfinite(value).all() for value in outputs):
    raise RuntimeError("Non-finite output")
offloaded = total = subgraphs = None
if _capture:
    # The firmware and the execution provider write through the C library, so
    # Python's own flush does not reach their buffers.
    ctypes.CDLL(None).fflush(None)
    with open(_capture.name) as handle:
        text = handle.read()
    nodes = re.search(r"Offloaded Nodes - (\d+), Total Nodes - (\d+)", text)
    count = re.search(r"subgraphs created are : (\d+)", text)
    if nodes:
        offloaded, total = int(nodes.group(1)), int(nodes.group(2))
    if count:
        subgraphs = int(count.group(1))

report = {
    "model": args.model_dir.name, "model_sha256": hashlib.sha256(models[0].read_bytes()).hexdigest(),
    "kernel": platform.release(), "onnxruntime": ort.__version__, "providers": session.get_providers(),
    "backend": "cpu-a72" if args.cpu else "tidl-c7x",
    "cpu_threads": args.threads if args.cpu else None,
    "warmup": args.warmup, "runs": args.runs,
    "mean_ms": statistics.mean(times), "median_ms": statistics.median(times),
    "p95_ms": float(np.percentile(times, 95)), "min_ms": min(times), "max_ms": max(times),
    "nodes_total": total, "nodes_offloaded": 0 if args.cpu else offloaded,
    "subgraphs": None if args.cpu else subgraphs,
    "device": release().get("MODEL_NAME"), "firmware": release().get("FIRMWARE_VERSION"),
    "tidl_tag": release().get("TIDL_TAG"),
    "before": before, "after": after, "samples_ms": times,
}
with args.output.open("w") as handle:
    json.dump(report, handle, indent=2)
out = _clean or sys.stdout

def field(label, value):
    print("    %-15s%s" % (label, value), file=out)

def block(title):
    print("", file=out)
    print("  " + title, file=out)

# Resolve the node total before anything is printed, so the same fields appear
# whichever core ran the graph: with --cpu the runtime prints no counts, so it
# comes from the bundle's own metadata.
meta = args.model_dir / "artifacts" / "onnxrtMetaData.txt"
if total is None and meta.exists():
    found = re.search(r"numGraphNodes=(\d+)", meta.read_text())
    total = int(found.group(1)) if found else None
if args.cpu:
    offloaded, subgraphs = 0, None

catalog = re.match(r"^[a-z]{2}-\d{4}", report["model"])
block("model")
if catalog:
    field("id", catalog.group(0))
field("bundle", report["model"])
for shape in shapes:
    field("input tensor", shape)
field("graph", models[0].name)
# Last, so the total sits directly above the execution table that splits it.
if total is not None:
    field("nodes", total)

block("execution")
if total is None:
    field("nodes", "not reported by the runtime")
else:
    print(("    %-15s%-10s%-10s" % ("", "nodes", "subgraphs")).rstrip(), file=out)
    print(("    %-15s%-10d%-10s" % ("C7x-MMA", offloaded,
          "-" if args.cpu else subgraphs if subgraphs is not None else "?")).rstrip(), file=out)
    print(("    %-15s%-10d%-10s" % ("Cortex-A72", total - offloaded, "-")).rstrip(), file=out)
    if offloaded not in (0, total):
        field("", "not comparable with a fully offloaded figure")

hottest = lambda side: max(report[side]["temperatures_mC"].values()) / 1000.0
block("run")
field("warm-up", "%d calls" % args.warmup)
field("measured", "%d calls" % args.runs)
field("input values", "all zeros")
if args.cpu:
    field("threads", args.threads)
field("hottest zone", "%.1f -> %.1f C" % (hottest("before"), hottest("after")))
field("load average", "%.2f -> %.2f" % (before["load"], after["load"]))

# Homogeneous numbers of one unit read better side by side than as a column
# of labels; the heterogeneous blocks above stay label-per-line.
block("latency (ms)")
print(("    %-15s" % "" + "".join("%-10s" % name for name in
                                  ("mean", "median", "p95", "min", "max"))).rstrip(), file=out)
print(("    %-15s" % ("Cortex-A72" if args.cpu else "C7x-MMA")
       + "".join("%-10.3f" % value for value in
                 (report["mean_ms"], report["median_ms"], report["p95_ms"],
                  report["min_ms"], report["max_ms"]))).rstrip(), file=out)

block("throughput")
# One blocking call at a time, so the rate is 1/mean. Pipelined or batched
# execution is a different measurement.
field("mean", "%.3g inferences/s" % (1000.0 / report["mean_ms"]))

block("environment")
for label, value in (("device", report["device"]), ("firmware", report["firmware"]),
                     ("TIDL", report["tidl_tag"]), ("kernel", report["kernel"]),
                     ("ONNX Runtime", report["onnxruntime"])):
    if value:
        field(label, value)

block("output")
field("record", args.output.resolve())
if _capture:
    field("runtime log", _capture.name)
print("", file=out)
out.flush()
