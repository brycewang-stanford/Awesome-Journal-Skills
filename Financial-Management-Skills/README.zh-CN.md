# Financial Management Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Financial Management Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Financial Management（FM）** 投稿的 12 个 agent skills。本包围绕 corporate finance, investments, market institutions, and applied financial decision-making 设计，帮助稿件区别于 Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies，并强调 applied finance evidence that ties estimates to managerial or market decisions。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| FM 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 corporate finance, investments, market institutions, and applied financial decision-making |
| 同门边界 | 说明为什么不是 Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 applied finance evidence that ties estimates to managerial or market decisions |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Financial-Management-Skills
/plugin install financial-management-skills
```

手动使用：先打开 [`skills/finman-workflow/SKILL.md`](skills/finman-workflow/SKILL.md)。

## 默认工作流

```text
finman-workflow → finman-topic-selection → finman-literature-positioning → finman-identification → finman-empirical-design → finman-robustness → finman-tables-figures → finman-internet-appendix → finman-writing-style → finman-submission → finman-referee-strategy → finman-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`finman-workflow`](skills/finman-workflow/SKILL.md) | 面向 FM 稿件的 Workflow Router |
| 2 | [`finman-topic-selection`](skills/finman-topic-selection/SKILL.md) | 面向 FM 稿件的 Topic Selection |
| 3 | [`finman-literature-positioning`](skills/finman-literature-positioning/SKILL.md) | 面向 FM 稿件的 Literature Positioning |
| 4 | [`finman-identification`](skills/finman-identification/SKILL.md) | 面向 FM 稿件的 Identification Strategy |
| 5 | [`finman-empirical-design`](skills/finman-empirical-design/SKILL.md) | 面向 FM 稿件的 Empirical Design |
| 6 | [`finman-robustness`](skills/finman-robustness/SKILL.md) | 面向 FM 稿件的 Robustness Strategy |
| 7 | [`finman-tables-figures`](skills/finman-tables-figures/SKILL.md) | 面向 FM 稿件的 Tables and Figures |
| 8 | [`finman-internet-appendix`](skills/finman-internet-appendix/SKILL.md) | 面向 FM 稿件的 Internet Appendix |
| 9 | [`finman-writing-style`](skills/finman-writing-style/SKILL.md) | 面向 FM 稿件的 Writing Style |
| 10 | [`finman-submission`](skills/finman-submission/SKILL.md) | 面向 FM 稿件的 Submission Preflight |
| 11 | [`finman-referee-strategy`](skills/finman-referee-strategy/SKILL.md) | 面向 FM 稿件的 Referee Strategy |
| 12 | [`finman-rebuttal`](skills/finman-rebuttal/SKILL.md) | 面向 FM 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
