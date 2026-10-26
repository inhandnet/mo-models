# Compatibility matrix

[`compat.json`](compat.json) records one tested baseline per board and image: TIDL version, C7x firmware directory, target runtimes, the pinned host toolchain and the TI model-zoo version the source models were taken from. A model artifact is only valid for the baseline it was compiled against; do not mix firmware, runtime libraries and artifacts from different rows.

| Board | Image | TIDL | Firmware dir | TI ONNX Runtime | Host toolchain |
|---|---|---|---|---|---|
| mo-62a | V1.1.0 | 11_02_17_00 | edgeai/11_1 | 1.23.0 | edgeai-tidl-tools `11_02_17_00` (`d2be720`) |

The values come from the mo-docs "Version map" audit of a V1.1.0 development board (2026-10-21). They are not a manifest for every later image; add a new row when a new image or TIDL version is validated, and keep the previous row so older artifacts stay traceable.
