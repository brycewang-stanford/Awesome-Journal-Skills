# Journal of Health Economics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Health Economics Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Health Economics（JHE）** 投稿的 12 个 agent skills。本包围绕 health economics, insurance, provider incentives, medical technology, health policy, and health behavior 设计，帮助稿件区别于 American Journal of Health Economics, Journal of Public Economics, Health Economics, and AEJ Economic Policy，并强调 policy-relevant causal evidence with institutional health-system detail。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JHE 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 health economics, insurance, provider incentives, medical technology, health policy, and health behavior |
| 同门边界 | 说明为什么不是 American Journal of Health Economics, Journal of Public Economics, Health Economics, and AEJ Economic Policy |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 policy-relevant causal evidence with institutional health-system detail |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Health-Economics-Skills
/plugin install jhe-skills
```

手动使用：先打开 [`skills/jhe-workflow/SKILL.md`](skills/jhe-workflow/SKILL.md)。

## 默认工作流

```text
jhe-workflow → jhe-topic-selection → jhe-literature-positioning → jhe-identification → jhe-theory-model → jhe-robustness → jhe-tables-figures → jhe-writing-style → jhe-replication-package → jhe-referee-strategy → jhe-submission → jhe-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jhe-workflow`](skills/jhe-workflow/SKILL.md) | 面向 JHE 稿件的 Workflow Router |
| 2 | [`jhe-topic-selection`](skills/jhe-topic-selection/SKILL.md) | 面向 JHE 稿件的 Topic Selection |
| 3 | [`jhe-literature-positioning`](skills/jhe-literature-positioning/SKILL.md) | 面向 JHE 稿件的 Literature Positioning |
| 4 | [`jhe-identification`](skills/jhe-identification/SKILL.md) | 面向 JHE 稿件的 Identification Strategy |
| 5 | [`jhe-theory-model`](skills/jhe-theory-model/SKILL.md) | 面向 JHE 稿件的 Theory and Model Craft |
| 6 | [`jhe-robustness`](skills/jhe-robustness/SKILL.md) | 面向 JHE 稿件的 Robustness Strategy |
| 7 | [`jhe-tables-figures`](skills/jhe-tables-figures/SKILL.md) | 面向 JHE 稿件的 Tables and Figures |
| 8 | [`jhe-writing-style`](skills/jhe-writing-style/SKILL.md) | 面向 JHE 稿件的 Writing Style |
| 9 | [`jhe-replication-package`](skills/jhe-replication-package/SKILL.md) | 面向 JHE 稿件的 Replication Package |
| 10 | [`jhe-referee-strategy`](skills/jhe-referee-strategy/SKILL.md) | 面向 JHE 稿件的 Referee Strategy |
| 11 | [`jhe-submission`](skills/jhe-submission/SKILL.md) | 面向 JHE 稿件的 Submission Preflight |
| 12 | [`jhe-rebuttal`](skills/jhe-rebuttal/SKILL.md) | 面向 JHE 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
