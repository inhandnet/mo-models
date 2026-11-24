# YOLOX-tiny-lite 8210 model compilation

`model.py` is the authoritative shared model contract, including official model
hashes, preprocessing and artifact validation. `compile_model.py` performs the
recorded calibration and TIDL compilation. Host setup belongs to mo-tools;
application logic, prepared clips and runtime examples belong to mo-examples.

mo-examples carries a generated copy of `model.py` for independent use. Its
`dependencies/model-contract.json` records the source commit and SHA-256. To
update that copy, first commit the canonical change here, then run
`node scripts/sync-model-contract.mjs /path/to/mo-models` in mo-examples and
review the generated changes. Website integration rejects a selected model
contract that differs from the copy expected by the application.

The developer website assembles the complete tutorial download from the fixed
composition. This directory retains its existing local license and provenance;
no model binary is republished here and no new accuracy qualification is added.
