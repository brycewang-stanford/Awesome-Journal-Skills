# Perspectives on Psychological Science Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Perspectives on Psychological Science Skills 封面"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-PoPS-1f5a66)](https://www.psychologicalscience.org/publications/perspectives)
[![Publisher](https://img.shields.io/badge/APS-SAGE-1f5a66)](https://journals.sagepub.com/home/pps)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.psychologicalscience.org/publications/perspectives/pps-submissions)

[English](README.md) | 简体中文

面向 **Perspectives on Psychological Science（PoPS）** 投稿的 12 个 agent skills。PoPS 由 **SAGE** 与
**美国心理科学学会（APS）** 合作出版，为双月刊，发表覆盖整个心理学的**广义整合性综述、理论与元理论陈述、
方法学与元科学（meta-science）评论，以及大局观的"观点"文章**。该刊历来是重要元科学、可重复性与改革议题的
主阵地，看重的是**重塑领域的综合或论证**，而非单项实证研究。本技能包帮助稿件区别于 *Psychological Science*、
*Psychological Bulletin*、*Annual Review of Psychology* 与 *Current Directions*，并把"典范级的开放科学实践"
作为一等公民式的要求。

**官方依据核验日期：2026-06**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| PoPS 约束 | 对稿件的要求 |
|-----------|--------------|
| 范围 | 必须是**广义、整合性**的贡献——关于领域的超越性（superordinate）信息，而非单项研究或常规元分析 |
| 投稿路径 | **独立稿件**（提案可选）vs. **合作/杂项稿件**（必须先提交提案）；提案获积极反馈不等于录用 |
| 组织性论证 | 必须有真正的**主线**（分类法／统一理论／重新框定），否则会沦为带注释的文献清单 |
| 平衡性 | 跨领域全面覆盖、对各阵营做"最强化"表述、**以证据为本的改革立场** |
| 开放科学 | PoPS 是开放科学先锋；数据存储、可复现的元科学协议与披露是典范要求而非可选项 |
| 同门边界 | 必须说明为什么不是 *Psychological Science*、*Psychological Bulletin*、*Annual Review of Psychology* 或 *Current Directions* |
| 来源纪律 | 当前流程事实须有来源，或明确标记 待核实 |

## 快速开始

```text
/plugin marketplace add ./Perspectives-on-Psychological-Science-Skills
/plugin install perspectives-on-psychological-science-skills
```

手动使用：先打开 [`skills/ppsych-workflow/SKILL.md`](skills/ppsych-workflow/SKILL.md)。

## 默认工作流

```text
ppsych-workflow → ppsych-topic-selection → ppsych-proposal-and-commissioning → ppsych-literature-synthesis →
ppsych-organizing-framework → ppsych-comprehensiveness-and-balance → ppsych-tables-figures → ppsych-writing-style →
ppsych-transparency-and-reproducibility → ppsych-editor-strategy → ppsych-submission → ppsych-revision
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`ppsych-workflow`](skills/ppsych-workflow/SKILL.md) | PoPS 稿件的工作流路由（阶段 + 贡献类型） |
| 2 | [`ppsych-topic-selection`](skills/ppsych-topic-selection/SKILL.md) | 选题是否"PoPS 体量"（广义、整合、超越性） |
| 3 | [`ppsych-proposal-and-commissioning`](skills/ppsych-proposal-and-commissioning/SKILL.md) | 提案路径；合作/杂项稿件必须提交提案 |
| 4 | [`ppsych-literature-synthesis`](skills/ppsych-literature-synthesis/SKILL.md) | 系统性跨领域阅读；元科学协议 |
| 5 | [`ppsych-organizing-framework`](skills/ppsych-organizing-framework/SKILL.md) | 重塑领域的统一论证／主线 |
| 6 | [`ppsych-comprehensiveness-and-balance`](skills/ppsych-comprehensiveness-and-balance/SKILL.md) | 证据评估、覆盖度、平衡性、改革主张的标定 |
| 7 | [`ppsych-tables-figures`](skills/ppsych-tables-figures/SKILL.md) | 框架图、汇总表、元科学图表（APA） |
| 8 | [`ppsych-writing-style`](skills/ppsych-writing-style/SKILL.md) | 广义、有锋芒、可读的 PoPS 文风；摘要 ≤200 词 |
| 9 | [`ppsych-transparency-and-reproducibility`](skills/ppsych-transparency-and-reproducibility/SKILL.md) | 数据存储、预注册协议、典范级披露 |
| 10 | [`ppsych-editor-strategy`](skills/ppsych-editor-strategy/SKILL.md) | 编辑关系、审稿人预判、推荐审稿人 |
| 11 | [`ppsych-submission`](skills/ppsych-submission/SKILL.md) | ScholarOne 投稿前检查、声明、≥5 名客观审稿人 |
| 12 | [`ppsych-revision`](skills/ppsych-revision/SKILL.md) | 对 PoPS 决定信的逐条回复 |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 SAGE/APS 链接与易变项复核
- [`resources/external_tools.md`](resources/external_tools.md) — 检索、预注册、数据存储与元科学工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构的引言改写前后对照（PoPS 文风）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 真实 PoPS 论文（已联网核验）+ 同门期刊护栏

## 与同门期刊的区别

| 期刊 | 定位 | 本包的边界规则 |
|------|------|----------------|
| **Perspectives on Psychological Science** | 广义整合综述 + 理论 + **元科学**旗舰（APS） | 本包目标 |
| **Psychological Science** | 短篇**单项实证**报告（APS 姊妹刊） | 单项研究投这里，而非 PoPS |
| **Psychological Bulletin** | 正式、全面的**元分析** | 常规元分析投这里，除非带超越性信息 |
| **Annual Review of Psychology** | 面向专家的**特邀**穷尽式子领域综述 | 特邀、专家向——非投稿型广义观点 |
| **Current Directions in Psychological Science** | 面向广义读者的短篇**非技术**速写（APS） | 简短、非技术——非完整整合论证 |

## 相关链接

- https://www.psychologicalscience.org/publications/perspectives
- https://www.psychologicalscience.org/publications/perspectives/pps-submissions
- https://journals.sagepub.com/home/pps

## 许可证

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
