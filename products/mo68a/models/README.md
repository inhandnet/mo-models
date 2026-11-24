# Model catalog entries

One directory per model. Each directory holds a `README.md`, a `source-model.link` pointing at the TI model-zoo source file and, for models with a TI pre-compiled AM62A artifact, a `ti-artifact-am62a.link`. The machine-readable index is [`models.json`](../models.json) at the repository root; the directories never contain model binaries.

| Model | Task | Runtime | Input | Verification |
|---|---|---|---|---|
| [`TFL-CL-0000-mobileNetV1-mlperf`](./TFL-CL-0000-mobileNetV1-mlperf/) | Image classification | tflitert | 224x224 (resize 256, centre crop 224) | inventory |
| [`ONR-CL-6360-regNetx-200mf`](./ONR-CL-6360-regNetx-200mf/) | Image classification | onnxrt | 224x224 (resize 256, centre crop 224) | inventory |
| [`ONR-KD-7060-human-pose-yolox-s-640x640`](./ONR-KD-7060-human-pose-yolox-s-640x640/) | Human pose (keypoint detection) | onnxrt | 640x640 | inventory |
| [`TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320`](./TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320/) | Object detection | tflitert | 320x320 | inventory |
| [`ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512`](./ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512/) | Object detection | onnxrt | 512x512 | inventory |
| [`ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416`](./ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416/) | Object detection | onnxrt | 416x416 | audited-latency |
| [`ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640`](./ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640/) | Object detection | onnxrt | 640x640 | audited-latency |
| [`ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640`](./ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640/) | Object detection | onnxrt | 640x640 | inventory |
| [`ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432`](./ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432/) | Semantic segmentation | onnxrt | 768x432 | inventory |
| [`ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512`](./ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512/) | Semantic segmentation | onnxrt | 512x512 | inventory |
| [`ONR-SS-8690-fpnlite-aspp-regnetx400mf-ade20k32-384x384`](./ONR-SS-8690-fpnlite-aspp-regnetx400mf-ade20k32-384x384/) | Semantic segmentation | onnxrt | 384x384 | inventory |
| [`yolox-tiny-lite-8210-zone-demo`](./yolox-tiny-lite-8210-zone-demo/) | Object detection | onnxrt | 416x416 | tutorial |

Verification values: `inventory` = present in the Mo OS V1.1.0 image and not re-measured; `audited-latency` = a raw timing record is published under `benchmarks/results/`; `tutorial` = built by the documented tutorial and not shipped in the image.

The compiled bundles in `/opt/model_zoo` of the image were produced by InHand with TIDL `11_02_17_00`. No InHand download server exists yet, so every `artifact.status` is `pending-hosting`; the TI pre-compiled artifacts are listed as upstream references only.
