# ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512

| Field | Value |
|---|---|
| Task | Semantic segmentation (ADE20K (32 classes)) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 512x512 |
| TI model-zoo ID | `ss-8610_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `deeplabv3plus_mobilenetv2_edgeailite_512x512_20210308_outby4.onnx` (TI model zoo 11_02_00, 9911946 bytes) |
| Source SHA-256 | `86e60a2b12e2b27603ecd62762f9c850e62ea8f9142d9d674881a1da6748488c` |
| Source license | — |
| TI pre-compiled AM68A artifact (upstream reference) | [`ti-artifact-am68a.link`](ti-artifact-am68a.link), 11937419 bytes, not re-tested on Mo68A |
| Compiled artifact | Not shipped in an image yet; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | audited-latency |

Compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo68A.

## Audited latency on Mo68A

| Mean | Median | P95 | Samples |
|---|---|---|---|
| 10.98 ms | 10.977 ms | 11.038 ms | 100 after 5 warm-up calls |

Scope: wall-clock synchronous session.run; excludes pre/post-processing and session creation. ONNX Runtime 1.23.0, kernel 6.12.35-vendor-k3-mo68a. Raw record: [`ss-8610-c7x.json`](../../benchmarks/results/mo68a-v105-tidl-11_02_17_00/ss-8610-c7x.json). Blank input; this is not accuracy or end-to-end video FPS.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
