# Annual Review of Economics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Annual Review of Economics Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Annual Review of Economics（AREcon）** 投稿的 12 个 agent skills。本包围绕 commissioned review articles synthesizing major areas of economics for specialists and adjacent economists 设计，帮助稿件区别于 Journal of Economic Literature, Journal of Economic Perspectives, Handbook chapters, and Academy of Management Annals，并强调 agenda-setting synthesis that clarifies what the field knows, disputes, and should do next。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| AREcon 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 commissioned review articles synthesizing major areas of economics for specialists and adjacent economists |
| 同门边界 | 说明为什么不是 Journal of Economic Literature, Journal of Economic Perspectives, Handbook chapters, and Academy of Management Annals |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 agenda-setting synthesis that clarifies what the field knows, disputes, and should do next |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Annual-Review-of-Economics-Skills
/plugin install annual-review-of-economics-skills
```

手动使用：先打开 [`skills/arecon-workflow/SKILL.md`](skills/arecon-workflow/SKILL.md)。

## 默认工作流

```text
arecon-workflow → arecon-topic-selection → arecon-proposal-framing → arecon-literature-synthesis → arecon-organizing-framework → arecon-evidence-standards → arecon-tables-figures → arecon-writing-style → arecon-editor-strategy → arecon-submission → arecon-review-process → arecon-revision
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`arecon-workflow`](skills/arecon-workflow/SKILL.md) | 面向 AREcon 稿件的 Workflow Router |
| 2 | [`arecon-topic-selection`](skills/arecon-topic-selection/SKILL.md) | 面向 AREcon 稿件的 Topic Selection |
| 3 | [`arecon-proposal-framing`](skills/arecon-proposal-framing/SKILL.md) | 面向 AREcon 稿件的 Proposal Framing |
| 4 | [`arecon-literature-synthesis`](skills/arecon-literature-synthesis/SKILL.md) | 面向 AREcon 稿件的 Literature Synthesis |
| 5 | [`arecon-organizing-framework`](skills/arecon-organizing-framework/SKILL.md) | 面向 AREcon 稿件的 Organizing Framework |
| 6 | [`arecon-evidence-standards`](skills/arecon-evidence-standards/SKILL.md) | 面向 AREcon 稿件的 Evidence Standards |
| 7 | [`arecon-tables-figures`](skills/arecon-tables-figures/SKILL.md) | 面向 AREcon 稿件的 Tables and Figures |
| 8 | [`arecon-writing-style`](skills/arecon-writing-style/SKILL.md) | 面向 AREcon 稿件的 Writing Style |
| 9 | [`arecon-editor-strategy`](skills/arecon-editor-strategy/SKILL.md) | 面向 AREcon 稿件的 Editor Strategy |
| 10 | [`arecon-submission`](skills/arecon-submission/SKILL.md) | 面向 AREcon 稿件的 Submission Preflight |
| 11 | [`arecon-review-process`](skills/arecon-review-process/SKILL.md) | 面向 AREcon 稿件的 Review Process |
| 12 | [`arecon-revision`](skills/arecon-revision/SKILL.md) | 面向 AREcon 稿件的 Revision Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
