# ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640

| Field | Value |
|---|---|
| Task | Object detection (COCO) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 640x640 |
| TI model-zoo ID | `od-8220_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `yolox_s_lite_640x640_20220221_model.onnx` (TI model zoo 11_02_00, 35941555 bytes) |
| Source SHA-256 | `d7c93e93bc5f3849cf0c5ac6dd6181355072110919a194e5ac063c8d419d69ee` |
| Source license | [1](https://github.com/TexasInstruments/edgeai-tensorlab/blob/f272548ef0fe96046f1bf2c3833e040a1ecf8e44/edgeai-modelzoo/models/vision/detection/coco/edgeai-mmdet/LICENSE) |
| TI pre-compiled AM62A artifact (upstream reference) | [`ti-artifact-am62a.link`](ti-artifact-am62a.link), 41295679 bytes, not re-tested on Mo62A |
| Compiled artifact | Shipped in Mo OS V1.1.0 at `/opt/model_zoo/ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640`; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | audited-latency |

Shipped in the Mo OS V1.1.0 image as a bundle compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo62A.

## Audited latency on Mo62A

| Mean | Median | P95 | Samples |
|---|---|---|---|
| 40.402 ms | 40.406 ms | 40.53 ms | 100 after 5 warm-up calls |

Scope: wall-clock synchronous session.run; excludes pre/post-processing and session creation. ONNX Runtime 1.23.0, kernel 6.12.35. Raw record: [`benchmark-small.json`](../../benchmarks/results/mo62a-v110-tidl-11_02_17_00/benchmark-small.json). Blank input; this is not accuracy or end-to-end video FPS.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
