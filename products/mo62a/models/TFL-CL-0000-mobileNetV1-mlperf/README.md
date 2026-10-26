# TFL-CL-0000-mobileNetV1-mlperf

| Field | Value |
|---|---|
| Task | Image classification (ImageNet-1k) |
| Runtime | tflitert with TIDL execution provider / delegate |
| Input | 224x224 (resize 256, centre crop 224) |
| TI model-zoo ID | `cl-0000_tflitert` |
| Source model | [`source-model.link`](source-model.link) → `mobilenet_v1_1.0_224.tflite` (TI model zoo 11_02_00, 16901680 bytes) |
| Source SHA-256 | `f0e609e043552f514fd3534a615c612c96e17b2aa65059c9297a09db3d5b7d6a` |
| Source license | [1](https://github.com/TexasInstruments/edgeai-tensorlab/blob/f272548ef0fe96046f1bf2c3833e040a1ecf8e44/edgeai-modelzoo/models/vision/classification/imagenet1k/mlperf/LICENSE.md) |
| TI pre-compiled AM62A artifact (upstream reference) | [`ti-artifact-am62a.link`](ti-artifact-am62a.link), 19589032 bytes, not re-tested on Mo62A |
| Compiled artifact | Shipped in Mo OS V1.1.0 at `/opt/model_zoo/TFL-CL-0000-mobileNetV1-mlperf`; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | inventory |

Shipped in the Mo OS V1.1.0 image as a bundle compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo62A.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
