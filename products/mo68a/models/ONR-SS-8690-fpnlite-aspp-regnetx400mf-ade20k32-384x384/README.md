# ONR-SS-8690-fpnlite-aspp-regnetx400mf-ade20k32-384x384

| Field | Value |
|---|---|
| Task | Semantic segmentation (ADE20K (32 classes)) |
| Runtime | onnxrt with TIDL execution provider / delegate |
| Input | 384x384 |
| TI model-zoo ID | `ss-8690_onnxrt` |
| Source model | [`source-model.link`](source-model.link) → `fpn_aspp_regnetx400mf_edgeailite_384x384_20210314_outby4.onnx` (TI model zoo 11_02_00, 24018372 bytes) |
| Source SHA-256 | `f73cab20497d56ccd78df4f328a4f933b5df5d98998f29dd27f02da7410c2a03` |
| Source license | — |
| TI pre-compiled AM68A artifact (upstream reference) | [`ti-artifact-am68a.link`](ti-artifact-am68a.link), 28329163 bytes, not re-tested on Mo68A |
| Compiled artifact | Not shipped in an image yet; compiled by InHand with TIDL `11_02_17_00`; download hosting: pending-hosting |
| Verification | audited-latency |

Compiled by InHand with TIDL 11_02_17_00 from the TI model-zoo source model; the TI pre-compiled artifact link is an upstream reference and was not re-tested on Mo68A.

## Audited latency on Mo68A

| Mean | Median | P95 | Samples |
|---|---|---|---|
| 9.944 ms | 9.652 ms | 11.923 ms | 100 after 5 warm-up calls |

Scope: wall-clock synchronous session.run; excludes pre/post-processing and session creation. ONNX Runtime 1.23.0, kernel 6.12.35-vendor-k3-mo68a. Raw record: [`ss-8690-c7x.json`](../../benchmarks/results/mo68a-v105-tidl-11_02_17_00/ss-8690-c7x.json). Blank input; this is not accuracy or end-to-end video FPS.

The `.link` files follow the TI edgeai-modelzoo convention: one line with the URL of the file. This repository stores no model binaries.
