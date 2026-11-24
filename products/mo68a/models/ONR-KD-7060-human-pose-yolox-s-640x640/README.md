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
| TI pre-compiled AM68A artifact (upstream reference) | [`ti-artifact-am68a.link`](ti-artifact-am68a.link), 46574392 bytes, not re-tested on Mo68A |
| Compiled artifact | Not shipped in an image yet; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | audited-latency |

Compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo68A.

## Audited latency on Mo68A

| Mean | Median | P95 | Samples |
|---|---|---|---|
| 14.182 ms | 14.099 ms | 14.331 ms | 100 after 5 warm-up calls |

Scope: wall-clock synchronous session.run; excludes pre/post-processing and session creation. ONNX Runtime 1.23.0, kernel 6.12.35-vendor-k3-mo68a. Raw record: [`kd-7060-c7x.json`](../../benchmarks/results/mo68a-v105-tidl-11_02_17_00/kd-7060-c7x.json). Blank input; this is not accuracy or end-to-end video FPS.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
