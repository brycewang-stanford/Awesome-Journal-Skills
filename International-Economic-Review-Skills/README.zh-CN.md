# International Economic Review Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="International Economic Review Skills 封面"></p>

[English](README.md) | 简体中文

面向 **International Economic Review（IER）** 投稿的 12 个 agent skills。本包围绕 general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach 设计，帮助稿件区别于 QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review，并强调 formal economics argument with enough intuition for a broad journal audience。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| IER 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach |
| 同门边界 | 说明为什么不是 QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 formal economics argument with enough intuition for a broad journal audience |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./International-Economic-Review-Skills
/plugin install ier-skills
```

手动使用：先打开 [`skills/ier-workflow/SKILL.md`](skills/ier-workflow/SKILL.md)。

## 默认工作流

```text
ier-workflow → ier-topic-selection → ier-literature-positioning → ier-identification → ier-theory-model → ier-robustness → ier-tables-figures → ier-writing-style → ier-replication-package → ier-referee-strategy → ier-submission → ier-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`ier-workflow`](skills/ier-workflow/SKILL.md) | 面向 IER 稿件的 Workflow Router |
| 2 | [`ier-topic-selection`](skills/ier-topic-selection/SKILL.md) | 面向 IER 稿件的 Topic Selection |
| 3 | [`ier-literature-positioning`](skills/ier-literature-positioning/SKILL.md) | 面向 IER 稿件的 Literature Positioning |
| 4 | [`ier-identification`](skills/ier-identification/SKILL.md) | 面向 IER 稿件的 Identification Strategy |
| 5 | [`ier-theory-model`](skills/ier-theory-model/SKILL.md) | 面向 IER 稿件的 Theory and Model Craft |
| 6 | [`ier-robustness`](skills/ier-robustness/SKILL.md) | 面向 IER 稿件的 Robustness Strategy |
| 7 | [`ier-tables-figures`](skills/ier-tables-figures/SKILL.md) | 面向 IER 稿件的 Tables and Figures |
| 8 | [`ier-writing-style`](skills/ier-writing-style/SKILL.md) | 面向 IER 稿件的 Writing Style |
| 9 | [`ier-replication-package`](skills/ier-replication-package/SKILL.md) | 面向 IER 稿件的 Replication Package |
| 10 | [`ier-referee-strategy`](skills/ier-referee-strategy/SKILL.md) | 面向 IER 稿件的 Referee Strategy |
| 11 | [`ier-submission`](skills/ier-submission/SKILL.md) | 面向 IER 稿件的 Submission Preflight |
| 12 | [`ier-rebuttal`](skills/ier-rebuttal/SKILL.md) | 面向 IER 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
