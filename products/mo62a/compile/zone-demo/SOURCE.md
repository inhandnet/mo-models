# Source

Copied unchanged from the mo-docs tutorial package `static/downloads/ai/zone-demo/`
(pages "Compile your own model" and "Warehouse zone application", mo-docs V1.0.1).
`compile_model.py` compiles the unchanged TI YOLOX-tiny-lite 8210 ONNX model with
the pinned x86 AM62A toolchain (`REL.TIDL.11.02.17.00`, `SOC=AM62A`); it imports
`model.py`, which is also used by the application side kept in mo-examples.

These two files are licensed under CC BY-SA 4.0 (see `LICENSE` in this directory),
unlike the Apache-2.0 license of the rest of this repository. Host environment
setup (`setup_host.sh`, `activate_host.sh`, `requirements-host.txt`) lives in
mo-tools `toolchain/host-setup/`.
