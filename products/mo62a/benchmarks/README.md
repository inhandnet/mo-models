# Benchmark scripts

Reproducible on-device latency measurements for catalog models.

| Path | Purpose |
|---|---|
| `benchmark-inference.py` | Measures synchronous ONNX Runtime `session.run` calls with blank input on the board: `--warmup` calls are discarded, then `--runs` samples are recorded with mean, median, P95, min, max, CPU frequency and thermal readings before and after. It is not an accuracy or end-to-end video FPS test. |
| `results/mo62a-v110-tidl-11_02_17_00/` | Raw records from the mo-docs audit of a Mo OS V1.1.0 board: `benchmark-nano.json` (ONR-OD-8200, mean 10.900 ms) and `benchmark-small.json` (ONR-OD-8220, mean 40.402 ms), 100 samples after 5 warm-up calls, ONNX Runtime 1.23.0, kernel 6.12.35, 329/329 nodes offloaded. The `model_sha256` in each record matches the ONNX file of the shipped bundle. |

Run on the board:

```bash
sudo python3 products/mo62a/benchmarks/benchmark-inference.py \
  /opt/model_zoo/ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416 \
  --runs 100 --warmup 5 --output nano.json
```

Results for other models, boards or images are added as new files under `results/<board>-<image>-tidl-<version>/` together with the exact bundle hash; the catalog entry switches from `inventory` to `audited-latency` only when a raw record is published. GTM R-12 cross-board comparisons (FPS per watt, FPS per dollar) are not covered by this script yet.
