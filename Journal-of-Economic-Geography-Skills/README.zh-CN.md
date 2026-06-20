# Journal of Economic Geography Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Economic Geography Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Economic Geography（JEG）** 投稿的 12 个 agent skills。本包围绕 economic geography, spatial economics, regional development, innovation clusters, trade, and place-based policy 设计，帮助稿件区别于 Journal of Urban Economics, Regional Studies, Economic Geography, and Journal of International Economics，并强调 spatial economic argument that combines maps, mechanisms, and regional theory。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JEG 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 economic geography, spatial economics, regional development, innovation clusters, trade, and place-based policy |
| 同门边界 | 说明为什么不是 Journal of Urban Economics, Regional Studies, Economic Geography, and Journal of International Economics |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 spatial economic argument that combines maps, mechanisms, and regional theory |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Economic-Geography-Skills
/plugin install journal-of-economic-geography-skills
```

手动使用：先打开 [`skills/jegeo-workflow/SKILL.md`](skills/jegeo-workflow/SKILL.md)。

## 默认工作流

```text
jegeo-workflow → jegeo-topic-selection → jegeo-literature-positioning → jegeo-identification → jegeo-theory-model → jegeo-robustness → jegeo-tables-figures → jegeo-writing-style → jegeo-replication-package → jegeo-referee-strategy → jegeo-submission → jegeo-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jegeo-workflow`](skills/jegeo-workflow/SKILL.md) | 面向 JEG 稿件的 Workflow Router |
| 2 | [`jegeo-topic-selection`](skills/jegeo-topic-selection/SKILL.md) | 面向 JEG 稿件的 Topic Selection |
| 3 | [`jegeo-literature-positioning`](skills/jegeo-literature-positioning/SKILL.md) | 面向 JEG 稿件的 Literature Positioning |
| 4 | [`jegeo-identification`](skills/jegeo-identification/SKILL.md) | 面向 JEG 稿件的 Identification Strategy |
| 5 | [`jegeo-theory-model`](skills/jegeo-theory-model/SKILL.md) | 面向 JEG 稿件的 Theory and Model Craft |
| 6 | [`jegeo-robustness`](skills/jegeo-robustness/SKILL.md) | 面向 JEG 稿件的 Robustness Strategy |
| 7 | [`jegeo-tables-figures`](skills/jegeo-tables-figures/SKILL.md) | 面向 JEG 稿件的 Tables and Figures |
| 8 | [`jegeo-writing-style`](skills/jegeo-writing-style/SKILL.md) | 面向 JEG 稿件的 Writing Style |
| 9 | [`jegeo-replication-package`](skills/jegeo-replication-package/SKILL.md) | 面向 JEG 稿件的 Replication Package |
| 10 | [`jegeo-referee-strategy`](skills/jegeo-referee-strategy/SKILL.md) | 面向 JEG 稿件的 Referee Strategy |
| 11 | [`jegeo-submission`](skills/jegeo-submission/SKILL.md) | 面向 JEG 稿件的 Submission Preflight |
| 12 | [`jegeo-rebuttal`](skills/jegeo-rebuttal/SKILL.md) | 面向 JEG 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
