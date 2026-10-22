# ONR-CL-6360-regNetx-200mf

| Field | Value |
|---|---|
| Task | Image classification (ImageNet-1k) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 224x224 (resize 256, centre crop 224) |
| TI model-zoo ID | `cl-6360_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `regnetx-200mf.onnx` (TI model zoo 11_02_00, 10851198 bytes) |
| Source SHA-256 | `34467b5aa8b1e65a22fcb4e8cfc8395888442d854b0d98a3bf73e500ff967473` |
| Source license | [1](https://github.com/TexasInstruments/edgeai-tensorlab/blob/f272548ef0fe96046f1bf2c3833e040a1ecf8e44/edgeai-modelzoo/models/vision/classification/imagenet1k/fbr-pycls/LICENSE) |
| TI pre-compiled AM62A artifact (upstream reference) | [`ti-artifact-am62a.link`](ti-artifact-am62a.link), 12696036 bytes, not re-tested on Mo62A |
| Compiled artifact | Shipped in Mo OS V1.1.0 at `/opt/model_zoo/ONR-CL-6360-regNetx-200mf`; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | inventory |

Shipped in the Mo OS V1.1.0 image as a bundle compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo62A.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
