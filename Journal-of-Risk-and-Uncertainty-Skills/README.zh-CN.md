# Journal of Risk and Uncertainty Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Risk and Uncertainty Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Risk and Uncertainty（JRU）** 投稿的 12 个 agent skills。本包围绕 risk, uncertainty, decision theory, behavioral choice, insurance, and experimental evidence on risky decisions 设计，帮助稿件区别于 Experimental Economics, Journal of Economic Behavior and Organization, Games and Economic Behavior, and Management Science，并强调 decision-theoretic clarity with careful measurement of risk and uncertainty。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JRU 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 risk, uncertainty, decision theory, behavioral choice, insurance, and experimental evidence on risky decisions |
| 同门边界 | 说明为什么不是 Experimental Economics, Journal of Economic Behavior and Organization, Games and Economic Behavior, and Management Science |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 decision-theoretic clarity with careful measurement of risk and uncertainty |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Risk-and-Uncertainty-Skills
/plugin install jru-skills
```

手动使用：先打开 [`skills/jru-workflow/SKILL.md`](skills/jru-workflow/SKILL.md)。

## 默认工作流

```text
jru-workflow → jru-topic-selection → jru-literature-positioning → jru-identification → jru-theory-model → jru-robustness → jru-tables-figures → jru-writing-style → jru-replication-package → jru-referee-strategy → jru-submission → jru-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jru-workflow`](skills/jru-workflow/SKILL.md) | 面向 JRU 稿件的 Workflow Router |
| 2 | [`jru-topic-selection`](skills/jru-topic-selection/SKILL.md) | 面向 JRU 稿件的 Topic Selection |
| 3 | [`jru-literature-positioning`](skills/jru-literature-positioning/SKILL.md) | 面向 JRU 稿件的 Literature Positioning |
| 4 | [`jru-identification`](skills/jru-identification/SKILL.md) | 面向 JRU 稿件的 Identification Strategy |
| 5 | [`jru-theory-model`](skills/jru-theory-model/SKILL.md) | 面向 JRU 稿件的 Theory and Model Craft |
| 6 | [`jru-robustness`](skills/jru-robustness/SKILL.md) | 面向 JRU 稿件的 Robustness Strategy |
| 7 | [`jru-tables-figures`](skills/jru-tables-figures/SKILL.md) | 面向 JRU 稿件的 Tables and Figures |
| 8 | [`jru-writing-style`](skills/jru-writing-style/SKILL.md) | 面向 JRU 稿件的 Writing Style |
| 9 | [`jru-replication-package`](skills/jru-replication-package/SKILL.md) | 面向 JRU 稿件的 Replication Package |
| 10 | [`jru-referee-strategy`](skills/jru-referee-strategy/SKILL.md) | 面向 JRU 稿件的 Referee Strategy |
| 11 | [`jru-submission`](skills/jru-submission/SKILL.md) | 面向 JRU 稿件的 Submission Preflight |
| 12 | [`jru-rebuttal`](skills/jru-rebuttal/SKILL.md) | 面向 JRU 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
