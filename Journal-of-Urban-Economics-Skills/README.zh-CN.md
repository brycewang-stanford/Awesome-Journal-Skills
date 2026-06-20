# Journal of Urban Economics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Urban Economics Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Urban Economics（JUE）** 投稿的 12 个 agent skills。本包围绕 urban economics, spatial equilibrium, housing, transport, local public finance, and neighborhood sorting 设计，帮助稿件区别于 Journal of Public Economics, Journal of Economic Geography, Regional Science and Urban Economics, and AEJ Applied，并强调 spatially grounded evidence with clear maps, mechanisms, and equilibrium caveats。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JUE 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 urban economics, spatial equilibrium, housing, transport, local public finance, and neighborhood sorting |
| 同门边界 | 说明为什么不是 Journal of Public Economics, Journal of Economic Geography, Regional Science and Urban Economics, and AEJ Applied |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 spatially grounded evidence with clear maps, mechanisms, and equilibrium caveats |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Urban-Economics-Skills
/plugin install jue-skills
```

手动使用：先打开 [`skills/jue-workflow/SKILL.md`](skills/jue-workflow/SKILL.md)。

## 默认工作流

```text
jue-workflow → jue-topic-selection → jue-literature-positioning → jue-identification → jue-theory-model → jue-robustness → jue-tables-figures → jue-writing-style → jue-replication-package → jue-referee-strategy → jue-submission → jue-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jue-workflow`](skills/jue-workflow/SKILL.md) | 面向 JUE 稿件的 Workflow Router |
| 2 | [`jue-topic-selection`](skills/jue-topic-selection/SKILL.md) | 面向 JUE 稿件的 Topic Selection |
| 3 | [`jue-literature-positioning`](skills/jue-literature-positioning/SKILL.md) | 面向 JUE 稿件的 Literature Positioning |
| 4 | [`jue-identification`](skills/jue-identification/SKILL.md) | 面向 JUE 稿件的 Identification Strategy |
| 5 | [`jue-theory-model`](skills/jue-theory-model/SKILL.md) | 面向 JUE 稿件的 Theory and Model Craft |
| 6 | [`jue-robustness`](skills/jue-robustness/SKILL.md) | 面向 JUE 稿件的 Robustness Strategy |
| 7 | [`jue-tables-figures`](skills/jue-tables-figures/SKILL.md) | 面向 JUE 稿件的 Tables and Figures |
| 8 | [`jue-writing-style`](skills/jue-writing-style/SKILL.md) | 面向 JUE 稿件的 Writing Style |
| 9 | [`jue-replication-package`](skills/jue-replication-package/SKILL.md) | 面向 JUE 稿件的 Replication Package |
| 10 | [`jue-referee-strategy`](skills/jue-referee-strategy/SKILL.md) | 面向 JUE 稿件的 Referee Strategy |
| 11 | [`jue-submission`](skills/jue-submission/SKILL.md) | 面向 JUE 稿件的 Submission Preflight |
| 12 | [`jue-rebuttal`](skills/jue-rebuttal/SKILL.md) | 面向 JUE 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
