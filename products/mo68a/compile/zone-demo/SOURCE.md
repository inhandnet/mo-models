# Source

Ported from the Mo62A scripts of the same name: the compile options, the
quantisation settings and the model contract are unchanged, and the only
functional difference is the SoC the toolchain is pinned to.
`compile_model.py` compiles the unchanged TI YOLOX-tiny-lite 8210 ONNX model with
the pinned x86 J721S2 toolchain (`REL.TIDL.11.02.17.00`, `SOC=J721S2`); it imports
`model.py`, which is also used by the application side kept in mo-examples.

These two files are licensed under CC BY-SA 4.0 (see `LICENSE` in this directory),
unlike the Apache-2.0 license of the rest of this repository. Host environment setup is not vendored for Mo68A; mo-docs "Set up the
toolchain" covers it.
