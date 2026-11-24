# Model compilation scripts

Scripts that compile a model for the Mo board NPU (TI C7x with TIDL) on an x86_64 host.

| Path | Purpose |
|---|---|
| `zone-demo/compile_model.py` | Compiles the unchanged TI YOLOX-tiny-lite 8210 ONNX model with calibration frames and writes the artifact bundle used by the tutorial application. Requires `SOC=AM62A`, `TIDL_TOOLS_PATH` pointing at `REL.TIDL.11.02.17.00` and the host environment from mo-tools `toolchain/host-setup/`. |
| `zone-demo/model.py` | Model constants, preprocessing and source checks shared with the application side. |

The toolchain itself is not vendored: use the TI `edgeai-tidl-tools` tag `11_02_17_00` (commit `d2be7203e5680298d7f54bcbd38e299d1bc22bfd`) as pinned in mo-tools `products/mo62a/toolchain/versions.json`. Compiled artifacts must stay with the exact firmware, runtime and TIDL version they were built for; see [`../compat/`](../compat/).

The 11 bundles shipped in `/opt/model_zoo` of Mo OS V1.1.0 were compiled by InHand with the same TIDL version from the TI model-zoo source models listed in [`../models.json`](../models.json). Their compilation configuration is not yet published here; `/opt/model_zoo/unsupported_models.txt` on the image records the entries that were dropped and why.
