# Journal of the Academy of Marketing Science Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of the Academy of Marketing Science Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of the Academy of Marketing Science（JAMS）** 投稿的 12 个 agent skills。本包围绕 marketing strategy, consumer behavior, channels, branding, innovation, and marketing theory 设计，帮助稿件区别于 Journal of Marketing, Journal of Marketing Research, Marketing Science, and Journal of Consumer Research，并强调 marketing scholarship with clear managerial implications and theory contribution。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JAMS 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 marketing strategy, consumer behavior, channels, branding, innovation, and marketing theory |
| 同门边界 | 说明为什么不是 Journal of Marketing, Journal of Marketing Research, Marketing Science, and Journal of Consumer Research |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 marketing scholarship with clear managerial implications and theory contribution |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-the-Academy-of-Marketing-Science-Skills
/plugin install jams-skills
```

手动使用：先打开 [`skills/jams-workflow/SKILL.md`](skills/jams-workflow/SKILL.md)。

## 默认工作流

```text
jams-workflow → jams-topic-selection → jams-theory-development → jams-literature-positioning → jams-methods → jams-data-analysis → jams-contribution-framing → jams-tables-figures → jams-writing-style → jams-submission → jams-review-process → jams-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jams-workflow`](skills/jams-workflow/SKILL.md) | 面向 JAMS 稿件的 Workflow Router |
| 2 | [`jams-topic-selection`](skills/jams-topic-selection/SKILL.md) | 面向 JAMS 稿件的 Topic Selection |
| 3 | [`jams-theory-development`](skills/jams-theory-development/SKILL.md) | 面向 JAMS 稿件的 Theory Development |
| 4 | [`jams-literature-positioning`](skills/jams-literature-positioning/SKILL.md) | 面向 JAMS 稿件的 Literature Positioning |
| 5 | [`jams-methods`](skills/jams-methods/SKILL.md) | 面向 JAMS 稿件的 Methods |
| 6 | [`jams-data-analysis`](skills/jams-data-analysis/SKILL.md) | 面向 JAMS 稿件的 Data Analysis |
| 7 | [`jams-contribution-framing`](skills/jams-contribution-framing/SKILL.md) | 面向 JAMS 稿件的 Contribution Framing |
| 8 | [`jams-tables-figures`](skills/jams-tables-figures/SKILL.md) | 面向 JAMS 稿件的 Tables and Figures |
| 9 | [`jams-writing-style`](skills/jams-writing-style/SKILL.md) | 面向 JAMS 稿件的 Writing Style |
| 10 | [`jams-submission`](skills/jams-submission/SKILL.md) | 面向 JAMS 稿件的 Submission Preflight |
| 11 | [`jams-review-process`](skills/jams-review-process/SKILL.md) | 面向 JAMS 稿件的 Review Process |
| 12 | [`jams-rebuttal`](skills/jams-rebuttal/SKILL.md) | 面向 JAMS 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
