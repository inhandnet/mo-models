# mo-models

English | [简体中文](README.zh-CN.md)

AI model catalog, compilation scripts and reproducible benchmark scripts for InHand Mo series single-board computers.

This repository will hold the catalog of AI models validated on Mo boards, the scripts that compile models for the on-board NPU (TI C7x with TIDL), reproducible benchmark scripts, and the compatibility matrix between model, runtime and image versions.

Related repositories:

- [Mo62A](https://github.com/inhandnet/Mo62A) — board support package, OS image build and device-side runtime for the Mo 62A board.
- [mo-docs](https://github.com/inhandnet/mo-docs) — product documentation for the Mo series.

## Status

The first catalog is in place: 12 entries in `models.json` (11 bundles shipped in Mo OS V1.1.0 plus the tutorial model), the compile and benchmark scripts published by the documentation, and the V1.1.0 compatibility baseline. Following the TI edgeai-modelzoo convention, model files are referenced through `.link` files (one URL per file) and never stored here; the source models and TI pre-compiled artifacts link to TI's public model zoo. InHand-compiled bundles have no download server yet, so their status is `pending-hosting`. Nothing in this repository is ready for production use until a release is published.

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

Every pull request must pass the `commit-message` and `ci` checks before it can be merged. Questions about using Mo boards belong in the [community forum](https://community.inhand.com); use GitHub issues for bugs and feature requests in this repository.

## Releases and tags

Releases are created by pushing an annotated tag that exactly matches `V<major>.<minor>.<patch>` or, for a release candidate, `V<major>.<minor>.<patch>-rc<n>`. The tag must point to a commit on `master`. The [release workflow](.github/workflows/release.yml) validates the tag, generates English and Chinese changelogs from the bilingual commit messages, packages a source archive with an SPDX SBOM and SHA-256 checksums, and publishes a GitHub Release titled with the tag name. A release candidate is published as a prerelease.

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
