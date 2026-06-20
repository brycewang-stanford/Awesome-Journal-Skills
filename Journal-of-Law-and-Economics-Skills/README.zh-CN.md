# The Journal of Law and Economics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="The Journal of Law and Economics Skills 封面"></p>

[English](README.md) | 简体中文

面向 **The Journal of Law and Economics（JLE）** 投稿的 12 个 agent skills。本包围绕 law and economics, regulation, property rights, contracts, liability, antitrust, and legal institutions 设计，帮助稿件区别于 Journal of Legal Studies, JLEO, American Law and Economics Review, and Journal of Public Economics，并强调 economics-first legal analysis that respects doctrine, timing, and institutional assignment。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JLE 约束 | 对稿件的要求 |
|-------------------|--------------|
| 范围 | 主张必须服务于 law and economics, regulation, property rights, contracts, liability, antitrust, and legal institutions |
| 同门边界 | 说明为什么不是 Journal of Legal Studies, JLEO, American Law and Economics Review, and Journal of Public Economics |
| 证据标准 | 设计、模型、综述或质性证据必须匹配 economics-first legal analysis that respects doctrine, timing, and institutional assignment |
| 来源纪律 | 当前流程事实必须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Law-and-Economics-Skills
/plugin install jle-skills
```

手动使用：先打开 [`skills/jle-workflow/SKILL.md`](skills/jle-workflow/SKILL.md)。

## 默认工作流

```text
jle-workflow → jle-topic-selection → jle-literature-positioning → jle-identification → jle-theory-model → jle-robustness → jle-tables-figures → jle-writing-style → jle-replication-package → jle-referee-strategy → jle-submission → jle-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jle-workflow`](skills/jle-workflow/SKILL.md) | 面向 JLE 稿件的 Workflow Router |
| 2 | [`jle-topic-selection`](skills/jle-topic-selection/SKILL.md) | 面向 JLE 稿件的 Topic Selection |
| 3 | [`jle-literature-positioning`](skills/jle-literature-positioning/SKILL.md) | 面向 JLE 稿件的 Literature Positioning |
| 4 | [`jle-identification`](skills/jle-identification/SKILL.md) | 面向 JLE 稿件的 Identification Strategy |
| 5 | [`jle-theory-model`](skills/jle-theory-model/SKILL.md) | 面向 JLE 稿件的 Theory and Model Craft |
| 6 | [`jle-robustness`](skills/jle-robustness/SKILL.md) | 面向 JLE 稿件的 Robustness Strategy |
| 7 | [`jle-tables-figures`](skills/jle-tables-figures/SKILL.md) | 面向 JLE 稿件的 Tables and Figures |
| 8 | [`jle-writing-style`](skills/jle-writing-style/SKILL.md) | 面向 JLE 稿件的 Writing Style |
| 9 | [`jle-replication-package`](skills/jle-replication-package/SKILL.md) | 面向 JLE 稿件的 Replication Package |
| 10 | [`jle-referee-strategy`](skills/jle-referee-strategy/SKILL.md) | 面向 JLE 稿件的 Referee Strategy |
| 11 | [`jle-submission`](skills/jle-submission/SKILL.md) | 面向 JLE 稿件的 Submission Preflight |
| 12 | [`jle-rebuttal`](skills/jle-rebuttal/SKILL.md) | 面向 JLE 稿件的 Rebuttal Strategy |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息
- [`resources/external_tools.md`](resources/external_tools.md) — 数据库、方法与软件工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构引言改写示例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实论文槽位与来源纪律
- [`resources/code/`](resources/code/) — 适用时使用的实证代码脚手架

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
