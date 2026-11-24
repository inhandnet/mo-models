# Model catalog entries

One directory per model. Each directory holds a `README.md`, a `source-model.link` pointing at the TI model-zoo source file and, for models with a TI pre-compiled AM68A artifact, a `ti-artifact-am68a.link`. The machine-readable index is [`models.json`](../models.json); the directories never contain model binaries.

| Model | Task | Runtime | Input | Verification |
|---|---|---|---|---|
| [`TFL-CL-0000-mobileNetV1-mlperf`](./TFL-CL-0000-mobileNetV1-mlperf/) | Image classification | tflitert | 224x224 (resize 256, centre crop 224) | not yet on Mo68A: calibration needs ImageNet-1k |
| [`ONR-CL-6360-regNetx-200mf`](./ONR-CL-6360-regNetx-200mf/) | Image classification | onnxrt | 224x224 (resize 256, centre crop 224) | not yet on Mo68A: calibration needs ImageNet-1k |
| [`ONR-KD-7060-human-pose-yolox-s-640x640`](./ONR-KD-7060-human-pose-yolox-s-640x640/) | Human pose (keypoint detection) | onnxrt | 640x640 | audited-latency |
| [`TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320`](./TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320/) | Object detection | tflitert | 320x320 | not yet on Mo68A: compiled, no board timing |
| [`ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512`](./ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512/) | Object detection | onnxrt | 512x512 | audited-latency |
| [`ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416`](./ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416/) | Object detection | onnxrt | 416x416 | audited-latency |
| [`ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640`](./ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640/) | Object detection | onnxrt | 640x640 | audited-latency |
| [`ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640`](./ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640/) | Object detection | onnxrt | 640x640 | audited-latency |
| [`ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432`](./ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432/) | Semantic segmentation | onnxrt | 768x432 | audited-latency |
| [`ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512`](./ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512/) | Semantic segmentation | onnxrt | 512x512 | audited-latency |
| [`ONR-SS-8690-fpnlite-aspp-regnetx400mf-ade20k32-384x384`](./ONR-SS-8690-fpnlite-aspp-regnetx400mf-ade20k32-384x384/) | Semantic segmentation | onnxrt | 384x384 | audited-latency |
| [`yolox-tiny-lite-8210-zone-demo`](./yolox-tiny-lite-8210-zone-demo/) | Object detection | onnxrt | 416x416 | tutorial |

Verification values: `audited-latency` = a raw timing record is published under `benchmarks/results/`; `tutorial` = built by the documented tutorial and not shipped in the image.

Three entries are carried over from the Mo62A catalogue and are **not yet part of the Mo68A set**: their fields still hold Mo62A values and will be replaced once the models are compiled and measured on Mo68A. The two classification models need ImageNet-1k for calibration, which is not reachable from the build network; `TFL-OD-2020` is compiled and fully offloaded but the benchmark script reads `.onnx` only, so it has no board timing yet.

The bundles were compiled by InHand with TIDL `11_02_17_00` and measured on a Mo68A running firmware V1.0.5. No InHand download server exists, so every `artifact.status` is `pending-hosting`, and `artifact.hosting` stays `pending` until the V1.0.6 image ships them in `/opt/model_zoo`. The TI pre-compiled artifacts are listed as upstream references and do not load on this TIDL release.
