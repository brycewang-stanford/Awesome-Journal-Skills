# Organization Studies Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Organization Studies Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Organization Studies（OS）** 投稿的 12 个 agent skills。本包围绕 organization theory, institutional theory, critical management, qualitative research, and process studies 设计，帮助稿件区别于 Administrative Science Quarterly, Organization Science, Journal of Management Studies, and Academy of Management Review，并强调 organization-theory argument with careful positioning, reflexivity, and evidence-theory fit。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| OS 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 organization theory, institutional theory, critical management, qualitative research, and process studies |
| 同门边界 | 说明为什么不是 Administrative Science Quarterly, Organization Science, Journal of Management Studies, and Academy of Management Review |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 organization-theory argument with careful positioning, reflexivity, and evidence-theory fit |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Organization-Studies-Skills
/plugin install organization-studies-skills
```

手动使用：先打开 [`skills/orgstud-workflow/SKILL.md`](skills/orgstud-workflow/SKILL.md)。

## 默认工作流

```text
orgstud-workflow → orgstud-topic-selection → orgstud-theory-development → orgstud-literature-positioning → orgstud-methods → orgstud-data-analysis → orgstud-contribution-framing → orgstud-tables-figures → orgstud-writing-style → orgstud-submission → orgstud-review-process → orgstud-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`orgstud-workflow`](skills/orgstud-workflow/SKILL.md) | 面向 OS 稿件的 Workflow Router |
| 2 | [`orgstud-topic-selection`](skills/orgstud-topic-selection/SKILL.md) | 面向 OS 稿件的 Topic Selection |
| 3 | [`orgstud-theory-development`](skills/orgstud-theory-development/SKILL.md) | 面向 OS 稿件的 Theory Development |
| 4 | [`orgstud-literature-positioning`](skills/orgstud-literature-positioning/SKILL.md) | 面向 OS 稿件的 Literature Positioning |
| 5 | [`orgstud-methods`](skills/orgstud-methods/SKILL.md) | 面向 OS 稿件的 Methods |
| 6 | [`orgstud-data-analysis`](skills/orgstud-data-analysis/SKILL.md) | 面向 OS 稿件的 Data Analysis |
| 7 | [`orgstud-contribution-framing`](skills/orgstud-contribution-framing/SKILL.md) | 面向 OS 稿件的 Contribution Framing |
| 8 | [`orgstud-tables-figures`](skills/orgstud-tables-figures/SKILL.md) | 面向 OS 稿件的 Tables and Figures |
| 9 | [`orgstud-writing-style`](skills/orgstud-writing-style/SKILL.md) | 面向 OS 稿件的 Writing Style |
| 10 | [`orgstud-submission`](skills/orgstud-submission/SKILL.md) | 面向 OS 稿件的 Submission Preflight |
| 11 | [`orgstud-review-process`](skills/orgstud-review-process/SKILL.md) | 面向 OS 稿件的 Review Process |
| 12 | [`orgstud-rebuttal`](skills/orgstud-rebuttal/SKILL.md) | 面向 OS 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
