# Journal of the Association for Information Systems Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of the Association for Information Systems Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of the Association for Information Systems（JAIS）** 投稿的 12 个 agent skills。本包围绕 information systems theory, digital innovation, sociotechnical systems, methods, and cumulative IS scholarship 设计，帮助稿件区别于 MIS Quarterly, Information Systems Research, JMIS, and Management Science，并强调 theory-forward IS research with method fit and clear community contribution。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JAIS 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 information systems theory, digital innovation, sociotechnical systems, methods, and cumulative IS scholarship |
| 同门边界 | 说明为什么不是 MIS Quarterly, Information Systems Research, JMIS, and Management Science |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 theory-forward IS research with method fit and clear community contribution |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-the-Association-for-Information-Systems-Skills
/plugin install jais-skills
```

手动使用：先打开 [`skills/jais-workflow/SKILL.md`](skills/jais-workflow/SKILL.md)。

## 默认工作流

```text
jais-workflow → jais-topic-selection → jais-theory-development → jais-literature-positioning → jais-methods → jais-data-analysis → jais-contribution-framing → jais-tables-figures → jais-writing-style → jais-submission → jais-review-process → jais-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jais-workflow`](skills/jais-workflow/SKILL.md) | 面向 JAIS 稿件的 Workflow Router |
| 2 | [`jais-topic-selection`](skills/jais-topic-selection/SKILL.md) | 面向 JAIS 稿件的 Topic Selection |
| 3 | [`jais-theory-development`](skills/jais-theory-development/SKILL.md) | 面向 JAIS 稿件的 Theory Development |
| 4 | [`jais-literature-positioning`](skills/jais-literature-positioning/SKILL.md) | 面向 JAIS 稿件的 Literature Positioning |
| 5 | [`jais-methods`](skills/jais-methods/SKILL.md) | 面向 JAIS 稿件的 Methods |
| 6 | [`jais-data-analysis`](skills/jais-data-analysis/SKILL.md) | 面向 JAIS 稿件的 Data Analysis |
| 7 | [`jais-contribution-framing`](skills/jais-contribution-framing/SKILL.md) | 面向 JAIS 稿件的 Contribution Framing |
| 8 | [`jais-tables-figures`](skills/jais-tables-figures/SKILL.md) | 面向 JAIS 稿件的 Tables and Figures |
| 9 | [`jais-writing-style`](skills/jais-writing-style/SKILL.md) | 面向 JAIS 稿件的 Writing Style |
| 10 | [`jais-submission`](skills/jais-submission/SKILL.md) | 面向 JAIS 稿件的 Submission Preflight |
| 11 | [`jais-review-process`](skills/jais-review-process/SKILL.md) | 面向 JAIS 稿件的 Review Process |
| 12 | [`jais-rebuttal`](skills/jais-rebuttal/SKILL.md) | 面向 JAIS 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
