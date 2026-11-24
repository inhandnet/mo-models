# ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416

| Field | Value |
|---|---|
| Task | Object detection (COCO) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 416x416 |
| TI model-zoo ID | `od-8200_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `yolox_nano_lite_416x416_20220214_model.onnx` (TI model zoo 11_02_00, 9079592 bytes) |
| Source SHA-256 | `319f9e447b63655fc089f25c2d0975d21d9b3b228f5961f95d191e8cb6002da1` |
| Source license | [1](https://github.com/TexasInstruments/edgeai-tensorlab/blob/f272548ef0fe96046f1bf2c3833e040a1ecf8e44/edgeai-modelzoo/models/vision/detection/coco/edgeai-mmdet/LICENSE) |
| TI pre-compiled AM68A artifact (upstream reference) | [`ti-artifact-am68a.link`](ti-artifact-am68a.link), 10641474 bytes, not re-tested on Mo68A |
| Compiled artifact | Not shipped in an image yet; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | audited-latency |

Compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo68A.

## Audited latency on Mo68A

| Mean | Median | P95 | Samples |
|---|---|---|---|
| 5.129 ms | 5.119 ms | 5.212 ms | 100 after 5 warm-up calls |

Scope: wall-clock synchronous session.run; excludes pre/post-processing and session creation. ONNX Runtime 1.23.0, kernel 6.12.35-vendor-k3-mo68a. Raw record: [`od-8200-c7x.json`](../../benchmarks/results/mo68a-v105-tidl-11_02_17_00/od-8200-c7x.json). Blank input; this is not accuracy or end-to-end video FPS.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
