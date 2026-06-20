# Economic Policy Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Economic Policy Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Economic Policy（Economic Policy）** 投稿的 12 个 agent skills。本包围绕 policy-relevant economics papers written for an expert but broad policy audience 设计，帮助稿件区别于 AEJ Economic Policy, Journal of Public Economics, IMF Economic Review, and World Bank Economic Review，并强调 policy-first economics that states the decision problem, evidence, and limits plainly。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| Economic Policy 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 policy-relevant economics papers written for an expert but broad policy audience |
| 同门边界 | 说明为什么不是 AEJ Economic Policy, Journal of Public Economics, IMF Economic Review, and World Bank Economic Review |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 policy-first economics that states the decision problem, evidence, and limits plainly |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Economic-Policy-Skills
/plugin install economic-policy-skills
```

手动使用：先打开 [`skills/ecopol-workflow/SKILL.md`](skills/ecopol-workflow/SKILL.md)。

## 默认工作流

```text
ecopol-workflow → ecopol-topic-selection → ecopol-literature-positioning → ecopol-identification → ecopol-theory-model → ecopol-robustness → ecopol-tables-figures → ecopol-writing-style → ecopol-replication-package → ecopol-referee-strategy → ecopol-submission → ecopol-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`ecopol-workflow`](skills/ecopol-workflow/SKILL.md) | 面向 Economic Policy 稿件的 Workflow Router |
| 2 | [`ecopol-topic-selection`](skills/ecopol-topic-selection/SKILL.md) | 面向 Economic Policy 稿件的 Topic Selection |
| 3 | [`ecopol-literature-positioning`](skills/ecopol-literature-positioning/SKILL.md) | 面向 Economic Policy 稿件的 Literature Positioning |
| 4 | [`ecopol-identification`](skills/ecopol-identification/SKILL.md) | 面向 Economic Policy 稿件的 Identification Strategy |
| 5 | [`ecopol-theory-model`](skills/ecopol-theory-model/SKILL.md) | 面向 Economic Policy 稿件的 Theory and Model Craft |
| 6 | [`ecopol-robustness`](skills/ecopol-robustness/SKILL.md) | 面向 Economic Policy 稿件的 Robustness Strategy |
| 7 | [`ecopol-tables-figures`](skills/ecopol-tables-figures/SKILL.md) | 面向 Economic Policy 稿件的 Tables and Figures |
| 8 | [`ecopol-writing-style`](skills/ecopol-writing-style/SKILL.md) | 面向 Economic Policy 稿件的 Writing Style |
| 9 | [`ecopol-replication-package`](skills/ecopol-replication-package/SKILL.md) | 面向 Economic Policy 稿件的 Replication Package |
| 10 | [`ecopol-referee-strategy`](skills/ecopol-referee-strategy/SKILL.md) | 面向 Economic Policy 稿件的 Referee Strategy |
| 11 | [`ecopol-submission`](skills/ecopol-submission/SKILL.md) | 面向 Economic Policy 稿件的 Submission Preflight |
| 12 | [`ecopol-rebuttal`](skills/ecopol-rebuttal/SKILL.md) | 面向 Economic Policy 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
