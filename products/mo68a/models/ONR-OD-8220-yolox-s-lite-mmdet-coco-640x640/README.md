# ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640

| Field | Value |
|---|---|
| Task | Object detection (COCO) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 640x640 |
| TI model-zoo ID | `od-8220_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `yolox_s_lite_640x640_20220221_model.onnx` (TI model zoo 11_02_00, 35940748 bytes) |
| Source SHA-256 | `9000aae99d4677d134c120a0eee0e943f3321238aea9f710c150c55f6d59aae6` |
| Source license | [1](https://github.com/TexasInstruments/edgeai-tensorlab/blob/f272548ef0fe96046f1bf2c3833e040a1ecf8e44/edgeai-modelzoo/models/vision/detection/coco/edgeai-mmdet/LICENSE) |
| TI pre-compiled AM68A artifact (upstream reference) | [`ti-artifact-am68a.link`](ti-artifact-am68a.link), 41303732 bytes, not re-tested on Mo68A |
| Compiled artifact | Not shipped in an image yet; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | audited-latency |

Compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo68A.

## Audited latency on Mo68A

| Mean | Median | P95 | Samples |
|---|---|---|---|
| 13.358 ms | 13.236 ms | 13.888 ms | 100 after 5 warm-up calls |

Scope: wall-clock synchronous session.run; excludes pre/post-processing and session creation. ONNX Runtime 1.23.0, kernel 6.12.35-vendor-k3-mo68a. Raw record: [`od-8220-c7x.json`](../../benchmarks/results/mo68a-v105-tidl-11_02_17_00/od-8220-c7x.json). Blank input; this is not accuracy or end-to-end video FPS.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
