# ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512

| Field | Value |
|---|---|
| Task | Semantic segmentation (ADE20K (32 classes)) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 512x512 |
| TI model-zoo ID | `ss-8610_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `deeplabv3plus_mobilenetv2_edgeailite_512x512_20210308_outby4.onnx` (TI model zoo 11_02_00, 9912397 bytes) |
| Source SHA-256 | `a3c58e4aa0bfc00c998b85cc6160b664926f313982a0a94ed30ce0816b0def38` |
| Source license | see the TI model-zoo repository for the terms of this model family |
| TI pre-compiled AM62A artifact (upstream reference) | [`ti-artifact-am62a.link`](ti-artifact-am62a.link), 11934325 bytes, not re-tested on Mo62A |
| Compiled artifact | Shipped in Mo OS V1.1.0 at `/opt/model_zoo/ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512`; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | inventory |

Shipped in the Mo OS V1.1.0 image as a bundle compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo62A.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
