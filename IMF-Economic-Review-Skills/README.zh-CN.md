# IMF Economic Review Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="IMF Economic Review Skills 封面"></p>

[English](README.md) | 简体中文

面向 **IMF Economic Review（IMFER）** 投稿的 12 个 agent skills。本包围绕 international macroeconomics, finance, development, policy, exchange rates, sovereign risk, and IMF-relevant evidence 设计，帮助稿件区别于 Journal of International Economics, JIMF, JMCB, and Economic Policy，并强调 policy-facing international macro evidence with transparent country coverage and model assumptions。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| IMFER 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 international macroeconomics, finance, development, policy, exchange rates, sovereign risk, and IMF-relevant evidence |
| 同门边界 | 说明为什么不是 Journal of International Economics, JIMF, JMCB, and Economic Policy |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 policy-facing international macro evidence with transparent country coverage and model assumptions |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./IMF-Economic-Review-Skills
/plugin install imf-economic-review-skills
```

手动使用：先打开 [`skills/imfer-workflow/SKILL.md`](skills/imfer-workflow/SKILL.md)。

## 默认工作流

```text
imfer-workflow → imfer-topic-selection → imfer-literature-positioning → imfer-identification → imfer-theory-model → imfer-robustness → imfer-tables-figures → imfer-writing-style → imfer-replication-package → imfer-referee-strategy → imfer-submission → imfer-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`imfer-workflow`](skills/imfer-workflow/SKILL.md) | 面向 IMFER 稿件的 Workflow Router |
| 2 | [`imfer-topic-selection`](skills/imfer-topic-selection/SKILL.md) | 面向 IMFER 稿件的 Topic Selection |
| 3 | [`imfer-literature-positioning`](skills/imfer-literature-positioning/SKILL.md) | 面向 IMFER 稿件的 Literature Positioning |
| 4 | [`imfer-identification`](skills/imfer-identification/SKILL.md) | 面向 IMFER 稿件的 Identification Strategy |
| 5 | [`imfer-theory-model`](skills/imfer-theory-model/SKILL.md) | 面向 IMFER 稿件的 Theory and Model Craft |
| 6 | [`imfer-robustness`](skills/imfer-robustness/SKILL.md) | 面向 IMFER 稿件的 Robustness Strategy |
| 7 | [`imfer-tables-figures`](skills/imfer-tables-figures/SKILL.md) | 面向 IMFER 稿件的 Tables and Figures |
| 8 | [`imfer-writing-style`](skills/imfer-writing-style/SKILL.md) | 面向 IMFER 稿件的 Writing Style |
| 9 | [`imfer-replication-package`](skills/imfer-replication-package/SKILL.md) | 面向 IMFER 稿件的 Replication Package |
| 10 | [`imfer-referee-strategy`](skills/imfer-referee-strategy/SKILL.md) | 面向 IMFER 稿件的 Referee Strategy |
| 11 | [`imfer-submission`](skills/imfer-submission/SKILL.md) | 面向 IMFER 稿件的 Submission Preflight |
| 12 | [`imfer-rebuttal`](skills/imfer-rebuttal/SKILL.md) | 面向 IMFER 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
