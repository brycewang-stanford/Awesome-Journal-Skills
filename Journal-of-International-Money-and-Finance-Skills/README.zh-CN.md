# Journal of International Money and Finance Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of International Money and Finance Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of International Money and Finance（JIMF）** 投稿的 12 个 agent skills。本包围绕 international finance, exchange rates, global banking, capital flows, and open-economy macro-finance 设计，帮助稿件区别于 Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics，并强调 international-finance identification that respects exchange-rate regimes and cross-country comparability。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JIMF 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 international finance, exchange rates, global banking, capital flows, and open-economy macro-finance |
| 同门边界 | 说明为什么不是 Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 international-finance identification that respects exchange-rate regimes and cross-country comparability |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-International-Money-and-Finance-Skills
/plugin install jimf-skills
```

手动使用：先打开 [`skills/jimf-workflow/SKILL.md`](skills/jimf-workflow/SKILL.md)。

## 默认工作流

```text
jimf-workflow → jimf-topic-selection → jimf-literature-positioning → jimf-identification → jimf-empirical-design → jimf-robustness → jimf-tables-figures → jimf-internet-appendix → jimf-writing-style → jimf-submission → jimf-referee-strategy → jimf-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jimf-workflow`](skills/jimf-workflow/SKILL.md) | 面向 JIMF 稿件的 Workflow Router |
| 2 | [`jimf-topic-selection`](skills/jimf-topic-selection/SKILL.md) | 面向 JIMF 稿件的 Topic Selection |
| 3 | [`jimf-literature-positioning`](skills/jimf-literature-positioning/SKILL.md) | 面向 JIMF 稿件的 Literature Positioning |
| 4 | [`jimf-identification`](skills/jimf-identification/SKILL.md) | 面向 JIMF 稿件的 Identification Strategy |
| 5 | [`jimf-empirical-design`](skills/jimf-empirical-design/SKILL.md) | 面向 JIMF 稿件的 Empirical Design |
| 6 | [`jimf-robustness`](skills/jimf-robustness/SKILL.md) | 面向 JIMF 稿件的 Robustness Strategy |
| 7 | [`jimf-tables-figures`](skills/jimf-tables-figures/SKILL.md) | 面向 JIMF 稿件的 Tables and Figures |
| 8 | [`jimf-internet-appendix`](skills/jimf-internet-appendix/SKILL.md) | 面向 JIMF 稿件的 Internet Appendix |
| 9 | [`jimf-writing-style`](skills/jimf-writing-style/SKILL.md) | 面向 JIMF 稿件的 Writing Style |
| 10 | [`jimf-submission`](skills/jimf-submission/SKILL.md) | 面向 JIMF 稿件的 Submission Preflight |
| 11 | [`jimf-referee-strategy`](skills/jimf-referee-strategy/SKILL.md) | 面向 JIMF 稿件的 Referee Strategy |
| 12 | [`jimf-rebuttal`](skills/jimf-rebuttal/SKILL.md) | 面向 JIMF 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
