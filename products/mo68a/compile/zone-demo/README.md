# YOLOX-tiny-lite 8210 model compilation

`model.py` is the authoritative shared model contract, including official model
hashes, preprocessing and artifact validation. `compile_model.py` performs the
recorded calibration and TIDL compilation. Host setup is covered by mo-docs "Set up the toolchain";
application logic, prepared clips and runtime examples belong to mo-examples.

The application side is not published for Mo68A yet, so `model.py` has no
copy to stay in step with. This directory retains its existing local license
and provenance; no model binary is republished here and no new accuracy
qualification is added.
