# ONR-KD-7060-human-pose-yolox-s-640x640

| Field | Value |
|---|---|
| Task | Human pose (keypoint detection) (COCO) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 640x640 |
| TI model-zoo ID | `kd-7060_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `yolox_s_pose_ti_lite_640_20220301_model.onnx` (TI model zoo 11_02_00, 53657122 bytes) |
| Source SHA-256 | `576b23065b6ad0ba74d54b4774c821bb753962ccd8b250992fd84af377d8cc45` |
| Source license | [1](https://github.com/TexasInstruments/edgeai-tensorlab/blob/f272548ef0fe96046f1bf2c3833e040a1ecf8e44/edgeai-modelzoo/models/vision/keypoint/coco/edgeai-yolox/LICENSE) |
| TI pre-compiled AM62A artifact (upstream reference) | [`ti-artifact-am62a.link`](ti-artifact-am62a.link), 46566852 bytes, not re-tested on Mo62A |
| Compiled artifact | Shipped in Mo OS V1.1.0 at `/opt/model_zoo/ONR-KD-7060-human-pose-yolox-s-640x640`; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | inventory |

Shipped in the Mo OS V1.1.0 image as a bundle compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo62A.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
