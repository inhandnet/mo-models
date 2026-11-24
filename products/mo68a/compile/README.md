# Model compilation scripts

Scripts that compile a model for the Mo68A NPU (TI C7x with TIDL) on an x86_64 host.

| Path                         | Purpose                                                                                                                                                                                                                                                                                                           |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `zone-demo/compile_model.py` | Compiles the unchanged TI YOLOX-tiny-lite 8210 ONNX model with calibration frames and writes the artifact bundle used by the tutorial application. Requires `SOC=J721S2`, `TIDL_TOOLS_PATH` pointing at `REL.TIDL.11.02.17.00` and the Python 3.10 host environment that mo-docs "Set up the toolchain" installs. |
| `zone-demo/model.py`         | Model constants, preprocessing and source checks shared with the application side.                                                                                                                                                                                                                                |

The toolchain itself is not vendored: use the TI `edgeai-tidl-tools` tag `11_02_17_00` (commit `d2be7203e5680298d7f54bcbd38e299d1bc22bfd`). Compiled artifacts must stay with the exact firmware, runtime and TIDL version they were built for: each entry in [`../models.json`](../models.json) names the images and the TIDL release it was built against.

The eight catalogue bundles in [`../models.json`](../models.json) were compiled from TI model-zoo source models with that TIDL version, using TI's `edgeai-benchmark` rather than the script here. Their compilation configuration is not published yet.
