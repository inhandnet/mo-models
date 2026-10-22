# mo-models

[English](README.md) | 简体中文

InHand Mo 系列单板计算机的 AI 模型清单、模型编译脚本与可复现的基准测试脚本。

相关仓库：[Mo62A](https://github.com/inhandnet/Mo62A)（Mo 62A 板级支持与系统镜像）、[mo-docs](https://github.com/inhandnet/mo-docs)（产品文档）。

## 状态

首版清单已就位：`models.json` 共 12 条（Mo OS V1.1.0 镜像内置的 11 个模型包与教程模型），以及文档已发布的编译脚本、基准脚本和 V1.1.0 兼容基线。参照 TI edgeai-modelzoo 的做法，模型文件一律通过 `.link` 文件（每文件一行 URL）引用，仓库不存模型二进制；源模型与 TI 预编译产物指向 TI 公开模型库。InHand 自编译的模型包尚无下载服务器，状态标记为 `pending-hosting`。在发布版本之前，本仓库内容不用于生产。

## 目录结构

- `models/` — 每个模型一个目录：README、`source-model.link`、`ti-artifact-am62a.link`
- `compile/` — 主机侧编译脚本（TIDL `11_02_17_00`，版本钉定见 mo-tools）
- `benchmarks/` — 板上时延脚本与原始结果记录
- `compat/` — 已验证的板卡 / 镜像 / TIDL / 运行时基线（`compat.json`）
- `scripts/` — 仓库维护脚本（提交信息检查、变更记录生成）
- `.githooks/` — 本地提交信息检查钩子
- `.github/` — Issue 表单、PR 模板与 GitHub Actions 工作流

## 参与贡献

通过 PR 提交到 `master`。提交信息规范、PR 流程与本地钩子启用方法见 [CONTRIBUTING.md](CONTRIBUTING.md)（`git config core.hooksPath .githooks`）。PR 必须通过 `commit-message` 与 `ci` 两项检查后才能合并。产品使用问题请到[社区论坛](https://community.inhand.com)提问。

## 发布与标签

推送形如 `V<major>.<minor>.<patch>` 或 `V<major>.<minor>.<patch>-rc<n>` 的附注标签即触发发布工作流：校验标签、根据双语提交信息生成中英文变更记录、打包源码归档（含 SPDX SBOM 与 SHA-256 校验和）并创建以标签命名的 GitHub Release；`-rc` 标签发布为预发布版本。

## 安全

请勿在公开 Issue 中报告安全漏洞，见 [SECURITY.md](SECURITY.md)。

## 许可证

见 [LICENSE](LICENSE)。
