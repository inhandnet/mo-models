# mo-models

English | [简体中文](README.zh-CN.md)

AI model catalog, compilation scripts and reproducible benchmark scripts for InHand Mo series single-board computers.

This repository will hold the catalog of AI models validated on Mo boards, the scripts that compile models for the on-board NPU (TI C7x with TIDL), reproducible benchmark scripts, and the compatibility matrix between model, runtime and image versions.

Related repositories:

- [Mo62A](https://github.com/inhandnet/Mo62A) — board support package, OS image build and device-side runtime for the Mo 62A board.
- [mo-docs](https://github.com/inhandnet/mo-docs) — product documentation for the Mo series.

## Status

The first catalog is in place: 12 entries in `models.json` (11 bundles shipped in Mo OS V1.1.0 plus the tutorial model), the compile and benchmark scripts published by the documentation, and the V1.1.0 compatibility baseline. Following the TI edgeai-modelzoo convention, model files are referenced through `.link` files (one URL per file) and never stored here; the source models and TI pre-compiled artifacts link to TI's public model zoo. InHand-compiled bundles have no download server yet, so their status is `pending-hosting`. Catalog publication does not establish new hardware verification or model hosting.

## Repository layout

| Path | Purpose |
| --- | --- |
| `models/` | One directory per model: README, `source-model.link`, `ti-artifact-am62a.link`. |
| `compile/` | Host-side compilation scripts (TIDL `11_02_17_00`, pinned in mo-tools). |
| `benchmarks/` | On-device latency script and raw result records. |
| `compat/` | Tested board / image / TIDL / runtime baselines (`compat.json`). |
| `models.json` | Machine-readable catalog (schema 2); validated by `scripts/validate-catalog.py` in CI. |
| `scripts/` | Repository maintenance scripts (commit message check, changelog generation). |
| `.githooks/` | Git hooks that run the commit message check locally. |
| `.github/` | Issue forms, pull request template and GitHub Actions workflows. |
| `release-notes/` | Changelog baseline used by the release workflow. |

## Contributing

Contributions are welcome through pull requests to `master`. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the commit message convention, the pull request process and how to enable the local Git hooks:

```bash
git config core.hooksPath .githooks
```

Every pull request must pass the `commit-message` and `ci` checks before it can be merged. Use GitHub issues for bugs, reproducible problems and feature requests in this repository.

## Releases and tags

New releases use annotated ordinary `V<major>.<minor>.<patch>` tags on checked `master` commits. Only developer publishes website release candidates. The release workflow validates catalogs, packages source with SPDX SBOM, records the source commit and catalog hashes in `release.json`, writes SHA-256 checksums, then publishes a complete GitHub Release. Historical RCs remain unchanged. Changelog headings are bilingual; entries retain their English commit summaries.

```bash
git switch master
git pull --ff-only
git tag -a V1.0.0 -m "V1.0.0"
git push origin V1.0.0
```

## Security

Do not report security vulnerabilities in public issues. Follow [SECURITY.md](SECURITY.md).

## License

This repository is licensed under the terms in [LICENSE](LICENSE). Third-party content added later keeps its own license, stated next to the content.

## Unified website integration

`models.json` and `compat/compat.json` own model inventory, source references, compatibility and measured evidence. `pending-hosting`, `inventory`, `tutorial` and `audited-latency` remain distinct. Developer reads a pinned source revision, validates the combined data, and renders the website; this repository has no documentation-site frontend or website deployment.

Run `node scripts/check-catalog.mjs` and `node --test tests/*.test.mjs` with Node 22. `validation/` is exported from a committed developer contract and checked by hash; do not edit it locally. For integrated preview, run developer's `npm run preview -- --source mo-models=/path/to/mo-models`.
