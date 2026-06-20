# Research Policy Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Research Policy Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Research Policy（Research Policy）** 投稿的 12 个 agent skills。本包围绕 innovation, science policy, technology management, entrepreneurship, R&D, and knowledge production 设计，帮助稿件区别于 Strategic Management Journal, Management Science, Industrial and Corporate Change, and Journal of Business Venturing，并强调 innovation-policy argument linking mechanisms, institutions, and technology evidence。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| Research Policy 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 innovation, science policy, technology management, entrepreneurship, R&D, and knowledge production |
| 同门边界 | 说明为什么不是 Strategic Management Journal, Management Science, Industrial and Corporate Change, and Journal of Business Venturing |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 innovation-policy argument linking mechanisms, institutions, and technology evidence |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Research-Policy-Skills
/plugin install research-policy-skills
```

手动使用：先打开 [`skills/respol-workflow/SKILL.md`](skills/respol-workflow/SKILL.md)。

## 默认工作流

```text
respol-workflow → respol-topic-selection → respol-theory-development → respol-literature-positioning → respol-methods → respol-data-analysis → respol-contribution-framing → respol-tables-figures → respol-writing-style → respol-submission → respol-review-process → respol-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`respol-workflow`](skills/respol-workflow/SKILL.md) | 面向 Research Policy 稿件的 Workflow Router |
| 2 | [`respol-topic-selection`](skills/respol-topic-selection/SKILL.md) | 面向 Research Policy 稿件的 Topic Selection |
| 3 | [`respol-theory-development`](skills/respol-theory-development/SKILL.md) | 面向 Research Policy 稿件的 Theory Development |
| 4 | [`respol-literature-positioning`](skills/respol-literature-positioning/SKILL.md) | 面向 Research Policy 稿件的 Literature Positioning |
| 5 | [`respol-methods`](skills/respol-methods/SKILL.md) | 面向 Research Policy 稿件的 Methods |
| 6 | [`respol-data-analysis`](skills/respol-data-analysis/SKILL.md) | 面向 Research Policy 稿件的 Data Analysis |
| 7 | [`respol-contribution-framing`](skills/respol-contribution-framing/SKILL.md) | 面向 Research Policy 稿件的 Contribution Framing |
| 8 | [`respol-tables-figures`](skills/respol-tables-figures/SKILL.md) | 面向 Research Policy 稿件的 Tables and Figures |
| 9 | [`respol-writing-style`](skills/respol-writing-style/SKILL.md) | 面向 Research Policy 稿件的 Writing Style |
| 10 | [`respol-submission`](skills/respol-submission/SKILL.md) | 面向 Research Policy 稿件的 Submission Preflight |
| 11 | [`respol-review-process`](skills/respol-review-process/SKILL.md) | 面向 Research Policy 稿件的 Review Process |
| 12 | [`respol-rebuttal`](skills/respol-rebuttal/SKILL.md) | 面向 Research Policy 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
