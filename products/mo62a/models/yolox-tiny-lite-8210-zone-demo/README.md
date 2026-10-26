# yolox-tiny-lite-8210-zone-demo

| Field | Value |
|---|---|
| Task | Object detection (COCO) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 416x416 |
| TI model-zoo ID | `od-8210_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `yolox_tiny_lite_416x416_20220217_model.onnx` (TI model zoo 11_02_00) |
| Source SHA-256 | `c9d2a3fdb21bed079a74029441d83235ddd910c82f1e7b9de5a2a5998bc3eeca` |
| Source license | [1](https://github.com/TexasInstruments/edgeai-modelzoo/blob/99f1bd6e434bdde9d26c3b0678ce368e69050ea3/models/vision/detection/coco/edgeai-mmdet/LICENSE) |
| Compiled artifact | Compiled by the mo-docs tutorial on the host; the tutorial package mo62a-zone-demo.tar.gz is published by mo-docs until a model server exists.; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | tutorial |

Mo62A zone-counting tutorial model (mo-docs: Compile your own model / warehouse application). Not part of /opt/model_zoo; the compile scripts live in compile/zone-demo.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
