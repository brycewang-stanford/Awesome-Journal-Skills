# The World Bank Economic Review Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="The World Bank Economic Review Skills 封面"></p>

[English](README.md) | 简体中文

面向 **The World Bank Economic Review（WBER）** 投稿的 12 个 agent skills。本包围绕 policy-relevant development economics, impact evaluation, institutions, trade, labor, agriculture, and poverty 设计，帮助稿件区别于 Journal of Development Economics, World Development, Economic Development and Cultural Change, and AEJ Applied，并强调 development-policy evidence with transparent data construction and actionable interpretation。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| WBER 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 policy-relevant development economics, impact evaluation, institutions, trade, labor, agriculture, and poverty |
| 同门边界 | 说明为什么不是 Journal of Development Economics, World Development, Economic Development and Cultural Change, and AEJ Applied |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 development-policy evidence with transparent data construction and actionable interpretation |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./World-Bank-Economic-Review-Skills
/plugin install wber-skills
```

手动使用：先打开 [`skills/wber-workflow/SKILL.md`](skills/wber-workflow/SKILL.md)。

## 默认工作流

```text
wber-workflow → wber-topic-selection → wber-literature-positioning → wber-identification → wber-theory-model → wber-robustness → wber-tables-figures → wber-writing-style → wber-replication-package → wber-referee-strategy → wber-submission → wber-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`wber-workflow`](skills/wber-workflow/SKILL.md) | 面向 WBER 稿件的 Workflow Router |
| 2 | [`wber-topic-selection`](skills/wber-topic-selection/SKILL.md) | 面向 WBER 稿件的 Topic Selection |
| 3 | [`wber-literature-positioning`](skills/wber-literature-positioning/SKILL.md) | 面向 WBER 稿件的 Literature Positioning |
| 4 | [`wber-identification`](skills/wber-identification/SKILL.md) | 面向 WBER 稿件的 Identification Strategy |
| 5 | [`wber-theory-model`](skills/wber-theory-model/SKILL.md) | 面向 WBER 稿件的 Theory and Model Craft |
| 6 | [`wber-robustness`](skills/wber-robustness/SKILL.md) | 面向 WBER 稿件的 Robustness Strategy |
| 7 | [`wber-tables-figures`](skills/wber-tables-figures/SKILL.md) | 面向 WBER 稿件的 Tables and Figures |
| 8 | [`wber-writing-style`](skills/wber-writing-style/SKILL.md) | 面向 WBER 稿件的 Writing Style |
| 9 | [`wber-replication-package`](skills/wber-replication-package/SKILL.md) | 面向 WBER 稿件的 Replication Package |
| 10 | [`wber-referee-strategy`](skills/wber-referee-strategy/SKILL.md) | 面向 WBER 稿件的 Referee Strategy |
| 11 | [`wber-submission`](skills/wber-submission/SKILL.md) | 面向 WBER 稿件的 Submission Preflight |
| 12 | [`wber-rebuttal`](skills/wber-rebuttal/SKILL.md) | 面向 WBER 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
