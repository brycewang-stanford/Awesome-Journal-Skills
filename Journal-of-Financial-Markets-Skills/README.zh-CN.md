# Journal of Financial Markets Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Financial Markets Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Financial Markets（JFM）** 投稿的 12 个 agent skills。本包围绕 market microstructure, asset pricing, liquidity, trading, and financial-market design 设计，帮助稿件区别于 Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science，并强调 precise institutional detail, clean market data, and careful measurement of frictions。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JFM 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 market microstructure, asset pricing, liquidity, trading, and financial-market design |
| 同门边界 | 说明为什么不是 Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 precise institutional detail, clean market data, and careful measurement of frictions |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Financial-Markets-Skills
/plugin install jfm-skills
```

手动使用：先打开 [`skills/jfm-workflow/SKILL.md`](skills/jfm-workflow/SKILL.md)。

## 默认工作流

```text
jfm-workflow → jfm-topic-selection → jfm-literature-positioning → jfm-identification → jfm-empirical-design → jfm-robustness → jfm-tables-figures → jfm-internet-appendix → jfm-writing-style → jfm-submission → jfm-referee-strategy → jfm-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jfm-workflow`](skills/jfm-workflow/SKILL.md) | 面向 JFM 稿件的 Workflow Router |
| 2 | [`jfm-topic-selection`](skills/jfm-topic-selection/SKILL.md) | 面向 JFM 稿件的 Topic Selection |
| 3 | [`jfm-literature-positioning`](skills/jfm-literature-positioning/SKILL.md) | 面向 JFM 稿件的 Literature Positioning |
| 4 | [`jfm-identification`](skills/jfm-identification/SKILL.md) | 面向 JFM 稿件的 Identification Strategy |
| 5 | [`jfm-empirical-design`](skills/jfm-empirical-design/SKILL.md) | 面向 JFM 稿件的 Empirical Design |
| 6 | [`jfm-robustness`](skills/jfm-robustness/SKILL.md) | 面向 JFM 稿件的 Robustness Strategy |
| 7 | [`jfm-tables-figures`](skills/jfm-tables-figures/SKILL.md) | 面向 JFM 稿件的 Tables and Figures |
| 8 | [`jfm-internet-appendix`](skills/jfm-internet-appendix/SKILL.md) | 面向 JFM 稿件的 Internet Appendix |
| 9 | [`jfm-writing-style`](skills/jfm-writing-style/SKILL.md) | 面向 JFM 稿件的 Writing Style |
| 10 | [`jfm-submission`](skills/jfm-submission/SKILL.md) | 面向 JFM 稿件的 Submission Preflight |
| 11 | [`jfm-referee-strategy`](skills/jfm-referee-strategy/SKILL.md) | 面向 JFM 稿件的 Referee Strategy |
| 12 | [`jfm-rebuttal`](skills/jfm-rebuttal/SKILL.md) | 面向 JFM 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
