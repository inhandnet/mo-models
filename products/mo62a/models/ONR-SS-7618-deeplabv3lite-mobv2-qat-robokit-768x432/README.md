# ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432

| Field | Value |
|---|---|
| Task | Semantic segmentation (TI Robokit) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 768x432 |
| TI model-zoo ID | `ss-7618_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `deeplabv3plus_mnetv2_edgeailite_robokit_768x432_qat-p2.onnx` (TI model zoo 11_02_00, 9901576 bytes) |
| Source SHA-256 | `feef56d45457d498d8ee4773fe67d467d1989a9c926ed53322086d9ea1c13bee` |
| Source license | [1](https://github.com/TexasInstruments/edgeai-tensorlab/blob/f272548ef0fe96046f1bf2c3833e040a1ecf8e44/edgeai-modelzoo/models/vision/segmentation/ti-robokit/edgeai-tv/LICENSE) |
| TI pre-compiled AM62A artifact (upstream reference) | [`ti-artifact-am62a.link`](ti-artifact-am62a.link), 5520582 bytes, not re-tested on Mo62A |
| Compiled artifact | Shipped in Mo OS V1.1.0 at `/opt/model_zoo/ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432`; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | inventory |

Shipped in the Mo OS V1.1.0 image as a bundle compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo62A.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
