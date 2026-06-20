# Journal of Environmental Economics and Management Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Environmental Economics and Management Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Environmental Economics and Management（JEEM）** 投稿的 12 个 agent skills。本包围绕 environmental economics, resource economics, climate policy, regulation, valuation, and natural-resource management 设计，帮助稿件区别于 Review of Environmental Economics and Policy, AEJ Economic Policy, Journal of Public Economics, and Nature Climate Change，并强调 economic identification linked to environmental mechanisms and policy welfare。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JEEM 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 environmental economics, resource economics, climate policy, regulation, valuation, and natural-resource management |
| 同门边界 | 说明为什么不是 Review of Environmental Economics and Policy, AEJ Economic Policy, Journal of Public Economics, and Nature Climate Change |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 economic identification linked to environmental mechanisms and policy welfare |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Environmental-Economics-and-Management-Skills
/plugin install jeem-skills
```

手动使用：先打开 [`skills/jeem-workflow/SKILL.md`](skills/jeem-workflow/SKILL.md)。

## 默认工作流

```text
jeem-workflow → jeem-topic-selection → jeem-literature-positioning → jeem-identification → jeem-theory-model → jeem-robustness → jeem-tables-figures → jeem-writing-style → jeem-replication-package → jeem-referee-strategy → jeem-submission → jeem-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jeem-workflow`](skills/jeem-workflow/SKILL.md) | 面向 JEEM 稿件的 Workflow Router |
| 2 | [`jeem-topic-selection`](skills/jeem-topic-selection/SKILL.md) | 面向 JEEM 稿件的 Topic Selection |
| 3 | [`jeem-literature-positioning`](skills/jeem-literature-positioning/SKILL.md) | 面向 JEEM 稿件的 Literature Positioning |
| 4 | [`jeem-identification`](skills/jeem-identification/SKILL.md) | 面向 JEEM 稿件的 Identification Strategy |
| 5 | [`jeem-theory-model`](skills/jeem-theory-model/SKILL.md) | 面向 JEEM 稿件的 Theory and Model Craft |
| 6 | [`jeem-robustness`](skills/jeem-robustness/SKILL.md) | 面向 JEEM 稿件的 Robustness Strategy |
| 7 | [`jeem-tables-figures`](skills/jeem-tables-figures/SKILL.md) | 面向 JEEM 稿件的 Tables and Figures |
| 8 | [`jeem-writing-style`](skills/jeem-writing-style/SKILL.md) | 面向 JEEM 稿件的 Writing Style |
| 9 | [`jeem-replication-package`](skills/jeem-replication-package/SKILL.md) | 面向 JEEM 稿件的 Replication Package |
| 10 | [`jeem-referee-strategy`](skills/jeem-referee-strategy/SKILL.md) | 面向 JEEM 稿件的 Referee Strategy |
| 11 | [`jeem-submission`](skills/jeem-submission/SKILL.md) | 面向 JEEM 稿件的 Submission Preflight |
| 12 | [`jeem-rebuttal`](skills/jeem-rebuttal/SKILL.md) | 面向 JEEM 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
