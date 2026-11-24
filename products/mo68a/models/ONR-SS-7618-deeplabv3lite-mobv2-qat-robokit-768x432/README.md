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
| TI pre-compiled AM68A artifact (upstream reference) | [`ti-artifact-am68a.link`](ti-artifact-am68a.link), 5519337 bytes, not re-tested on Mo68A |
| Compiled artifact | Not shipped in an image yet; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | audited-latency |

Compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo68A.

## Audited latency on Mo68A

| Mean | Median | P95 | Samples |
|---|---|---|---|
| 17.568 ms | 17.182 ms | 20.067 ms | 100 after 5 warm-up calls |

Scope: wall-clock synchronous session.run; excludes pre/post-processing and session creation. ONNX Runtime 1.23.0, kernel 6.12.35-vendor-k3-mo68a. Raw record: [`ss-7618-c7x.json`](../../benchmarks/results/mo68a-v105-tidl-11_02_17_00/ss-7618-c7x.json). Blank input; this is not accuracy or end-to-end video FPS.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
