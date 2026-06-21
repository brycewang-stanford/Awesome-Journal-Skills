# AER: Insights 技能包

<p align="center"><img src="assets/cover.svg" width="200" alt="American Economic Review: Insights Skills cover"></p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-AER%3A%20Insights-102a54)](https://www.aeaweb.org/journals/aeri)
[![Format](https://img.shields.io/badge/format-short%20%C2%B7%20one%20idea-1f6feb)](resources/official-source-map.md)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://www.aeaweb.org/journals/aeri/submissions)

[English](README.md) | 简体中文

面向 **《美国经济评论：洞见》（American Economic Review: Insights, AER: Insights）** 短篇论文的 12 个智能体技能。
AER: Insights 是美国经济学会（AEA）于 **2019 年** 创办的期刊，发表 **围绕单一重要且执行良好的核心想法、短小自洽的论文**
（实证、理论或方法皆可）。其门槛是 **将 AER 级别的重要性压缩进一篇短文**。本技能包始终围绕两条硬约束设计：
**篇幅上限**（正文无图表时 ≤7,000 词，每个图表扣减 200 词，最多 5 个图表，摘要 ≤100 词）与
**单一洞见纪律**——一切次要内容都放入线上补充附录（Supplemental Appendix）。它同时编码了该刊
**快速而果断的审稿模式**（没有传统的 revise-and-resubmit；首轮决定为"有条件接收"或"拒稿"）以及 AEA 投稿系统、费用、
元数据/分类信息与 AEA 数据与代码可得性政策。

**官方依据核对于 2026-06-20**：AEA / AER: Insights 投稿、编辑政策、编辑名单、格式指南、录用稿指南、JEL 指南，
以及 AEA 数据与代码可得性政策。来源与上传前 live-check 项见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要独立技能包？

| AER: Insights 约束 | 对稿件的强制要求 |
|--------------------|------------------|
| 硬性篇幅上限（≤7,000 词 − 每图表 200 词；≤5 个图表；摘要 ≤100 词） | 超限将被 **不经评审直接退回**；从第一版起就要按上限裁剪 |
| 一篇一个想法 | 单一核心结果支撑全文；次要结果放入附录 |
| 开门见山写作 | 答案（含 SE/CI）出现在第一段，而非第 4 节 |
| 没有传统 R&R | 首轮即"有条件接收"或"拒稿"——投稿 **前** 就要预先化解质疑 |
| 有条件接收（约 8 周，通常不再返回审稿人） | 修改是"收尾"，不是"重新博弈" |
| AEA 排版规范 | **单盲**审稿；标题、作者署名与单位放在首页；不用显著性星号 |
| AEA 数据与代码可得性政策 | openICPSR 存档，**出版前** 由 AEA 数据编辑核验（附录结果同样在核验范围内） |

## 快速开始

**作为 Claude Code 插件** —— 将插件市场指向本目录并启用插件：

```
/plugin marketplace add ./AER-Insights-Skills
/plugin install aer-insights-skills
```

**手动使用** —— 每个技能都是 `skills/` 下自洽的 `SKILL.md`。先打开 `skills/aeri-workflow/SKILL.md`，
它会根据你当前阶段路由到合适的技能。

## 默认工作流

```
aeri-topic-selection → aeri-literature-positioning → aeri-identification → aeri-theory-model
   → aeri-robustness → aeri-tables-figures → aeri-writing-style → aeri-replication-package
   → aeri-referee-strategy → aeri-submission → aeri-rebuttal
                         （aeri-workflow 在以上各技能之间路由）
```

## 技能列表

| # | 技能 | 作用 |
|---|------|------|
| 1 | [`aeri-workflow`](skills/aeri-workflow/SKILL.md) | 路由器——诊断当前瓶颈并路由到相应技能 |
| 2 | [`aeri-topic-selection`](skills/aeri-topic-selection/SKILL.md) | 确认存在一个清晰、重要、识别干净、能独立成文的单一洞见（区分 AER / AEJ） |
| 3 | [`aeri-literature-positioning`](skills/aeri-literature-positioning/SKILL.md) | 用一到两段定位贡献——不写综述 |
| 4 | [`aeri-identification`](skills/aeri-identification/SKILL.md) | 让因果或参数识别干净到足以在短文中守得住 |
| 5 | [`aeri-theory-model`](skills/aeri-theory-model/SKILL.md) | 只保留单一洞见所需的最小模型 |
| 6 | [`aeri-robustness`](skills/aeri-robustness/SKILL.md) | 稳健性分流：正文 ≤2 项，其余进补充附录 |
| 7 | [`aeri-tables-figures`](skills/aeri-tables-figures/SKILL.md) | 控制在 5 个图表预算内，每个一页，不用显著性星号 |
| 8 | [`aeri-writing-style`](skills/aeri-writing-style/SKILL.md) | 开门见山写结果；执行词数上限与 ≤100 词摘要 |
| 9 | [`aeri-replication-package`](skills/aeri-replication-package/SKILL.md) | 为 AEA 数据编辑核验准备 openICPSR 存档 |
| 10 | [`aeri-referee-strategy`](skills/aeri-referee-strategy/SKILL.md) | 理解快速果断的审稿；预先化解短文承受不起的质疑 |
| 11 | [`aeri-submission`](skills/aeri-submission/SKILL.md) | 投稿前最终核查：词数/图表门槛、摘要、作者元数据、费用、声明、数据政策 |
| 12 | [`aeri-rebuttal`](skills/aeri-rebuttal/SKILL.md) | 起草简洁的"有条件接收"回复与修改计划 |

## 资源

- [`resources/README.md`](resources/README.md) —— 能力层索引
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的 AEA / AER: Insights 官方链接
- [`resources/external_tools.md`](resources/external_tools.md) —— 短篇实证/结构/方法研究的数据源、软件与工具包
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— 开门见山呈现单一结果的 AER: Insights 引言改写示例（虚构）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 按方法 × 主题整理、经网络核实的真实 AER: Insights 论文
- [`resources/code/`](resources/code/) —— 可复现的 Stata + Python 因果推断代码骨架（已内置）

## 与 AER / AEJ 的差异

| 期刊 | 定位 | 本技能包的取舍 |
|------|------|----------------|
| **AER: Insights** | **一个** 重要想法、**短**、**快** 审 | 本技能包的目标 |
| **《美国经济评论》（AER）** | 综合性、**多结果**、更长的旗舰刊 | AER: Insights 承接无需 AER 篇幅的单一想法论文 |
| **AEJ 系列（Applied / Micro / Macro / Policy）** | **面向具体领域的完整论文** | AER: Insights 是 **综合性且短**，而非领域内论文 |
| **QJE / JPE / Econometrica** | 长篇、引领议程的领域/综合论文 | AER: Insights 刻意做单一干净洞见的短篇出口 |

## 相关链接

- AER: Insights：https://www.aeaweb.org/journals/aeri
- AER: Insights 投稿指南：https://www.aeaweb.org/journals/aeri/submissions
- AEA 数据与代码可得性政策：https://www.aeaweb.org/journals/policies/data-code

## 许可证

MIT © 2026 Bryce Wang。详见 [LICENSE](LICENSE)。
