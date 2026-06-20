# Journal of Economic Behavior and Organization Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Economic Behavior and Organization Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Economic Behavior and Organization（JEBO）** 投稿的 12 个 agent skills。本包围绕 behavioral economics, organization, institutions, experiments, and decision-making outside frictionless textbook settings 设计，帮助稿件区别于 Experimental Economics, Games and Economic Behavior, Management Science, and Journal of Public Economics，并强调 mechanism-forward behavioral evidence with transparent experimental or institutional design。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JEBO 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 behavioral economics, organization, institutions, experiments, and decision-making outside frictionless textbook settings |
| 同门边界 | 说明为什么不是 Experimental Economics, Games and Economic Behavior, Management Science, and Journal of Public Economics |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 mechanism-forward behavioral evidence with transparent experimental or institutional design |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Economic-Behavior-and-Organization-Skills
/plugin install jebo-skills
```

手动使用：先打开 [`skills/jebo-workflow/SKILL.md`](skills/jebo-workflow/SKILL.md)。

## 默认工作流

```text
jebo-workflow → jebo-topic-selection → jebo-literature-positioning → jebo-identification → jebo-theory-model → jebo-robustness → jebo-tables-figures → jebo-writing-style → jebo-replication-package → jebo-referee-strategy → jebo-submission → jebo-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jebo-workflow`](skills/jebo-workflow/SKILL.md) | 面向 JEBO 稿件的 Workflow Router |
| 2 | [`jebo-topic-selection`](skills/jebo-topic-selection/SKILL.md) | 面向 JEBO 稿件的 Topic Selection |
| 3 | [`jebo-literature-positioning`](skills/jebo-literature-positioning/SKILL.md) | 面向 JEBO 稿件的 Literature Positioning |
| 4 | [`jebo-identification`](skills/jebo-identification/SKILL.md) | 面向 JEBO 稿件的 Identification Strategy |
| 5 | [`jebo-theory-model`](skills/jebo-theory-model/SKILL.md) | 面向 JEBO 稿件的 Theory and Model Craft |
| 6 | [`jebo-robustness`](skills/jebo-robustness/SKILL.md) | 面向 JEBO 稿件的 Robustness Strategy |
| 7 | [`jebo-tables-figures`](skills/jebo-tables-figures/SKILL.md) | 面向 JEBO 稿件的 Tables and Figures |
| 8 | [`jebo-writing-style`](skills/jebo-writing-style/SKILL.md) | 面向 JEBO 稿件的 Writing Style |
| 9 | [`jebo-replication-package`](skills/jebo-replication-package/SKILL.md) | 面向 JEBO 稿件的 Replication Package |
| 10 | [`jebo-referee-strategy`](skills/jebo-referee-strategy/SKILL.md) | 面向 JEBO 稿件的 Referee Strategy |
| 11 | [`jebo-submission`](skills/jebo-submission/SKILL.md) | 面向 JEBO 稿件的 Submission Preflight |
| 12 | [`jebo-rebuttal`](skills/jebo-rebuttal/SKILL.md) | 面向 JEBO 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
