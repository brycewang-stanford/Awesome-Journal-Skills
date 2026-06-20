# Journal of Management Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Management Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Management（JOMgmt）** 投稿的 12 个 agent skills。本包围绕 management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods 设计，帮助稿件区别于 Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies，并强调 theory-driven management research with clean construct logic and robust empirical design。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JOMgmt 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 management theory and empirical work across organizational behavior, strategy, HR, entrepreneurship, and research methods |
| 同门边界 | 说明为什么不是 Academy of Management Journal, Strategic Management Journal, Organization Science, and Journal of Management Studies |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 theory-driven management research with clean construct logic and robust empirical design |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Management-Skills
/plugin install journal-of-management-skills
```

手动使用：先打开 [`skills/jmgmt-workflow/SKILL.md`](skills/jmgmt-workflow/SKILL.md)。

## 默认工作流

```text
jmgmt-workflow → jmgmt-topic-selection → jmgmt-theory-development → jmgmt-literature-positioning → jmgmt-methods → jmgmt-data-analysis → jmgmt-contribution-framing → jmgmt-tables-figures → jmgmt-writing-style → jmgmt-submission → jmgmt-review-process → jmgmt-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jmgmt-workflow`](skills/jmgmt-workflow/SKILL.md) | 面向 JOMgmt 稿件的 Workflow Router |
| 2 | [`jmgmt-topic-selection`](skills/jmgmt-topic-selection/SKILL.md) | 面向 JOMgmt 稿件的 Topic Selection |
| 3 | [`jmgmt-theory-development`](skills/jmgmt-theory-development/SKILL.md) | 面向 JOMgmt 稿件的 Theory Development |
| 4 | [`jmgmt-literature-positioning`](skills/jmgmt-literature-positioning/SKILL.md) | 面向 JOMgmt 稿件的 Literature Positioning |
| 5 | [`jmgmt-methods`](skills/jmgmt-methods/SKILL.md) | 面向 JOMgmt 稿件的 Methods |
| 6 | [`jmgmt-data-analysis`](skills/jmgmt-data-analysis/SKILL.md) | 面向 JOMgmt 稿件的 Data Analysis |
| 7 | [`jmgmt-contribution-framing`](skills/jmgmt-contribution-framing/SKILL.md) | 面向 JOMgmt 稿件的 Contribution Framing |
| 8 | [`jmgmt-tables-figures`](skills/jmgmt-tables-figures/SKILL.md) | 面向 JOMgmt 稿件的 Tables and Figures |
| 9 | [`jmgmt-writing-style`](skills/jmgmt-writing-style/SKILL.md) | 面向 JOMgmt 稿件的 Writing Style |
| 10 | [`jmgmt-submission`](skills/jmgmt-submission/SKILL.md) | 面向 JOMgmt 稿件的 Submission Preflight |
| 11 | [`jmgmt-review-process`](skills/jmgmt-review-process/SKILL.md) | 面向 JOMgmt 稿件的 Review Process |
| 12 | [`jmgmt-rebuttal`](skills/jmgmt-rebuttal/SKILL.md) | 面向 JOMgmt 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
