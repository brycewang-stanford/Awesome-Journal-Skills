# Governance 期刊技能包

<p align="center">
  <img src="assets/cover.svg" alt="Governance: An International Journal of Policy, Administration, and Institutions 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Governance-14274e)](https://onlinelibrary.wiley.com/journal/14680491)
[![Field](https://img.shields.io/badge/field-公共行政与政治学-1f6feb)](https://onlinelibrary.wiley.com/journal/14680491)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《Governance：政策、行政与制度国际期刊》（Governance: An International Journal of Policy,
Administration, and Institutions）** 投稿的 Agent 技能栈。该刊由 **Wiley(-Blackwell)** 出版，与
**国际政治学会（IPSA）第 27 研究委员会——政府结构与组织（SOG）** 合作出版，创刊于 **1988 年**，季刊
（ISSN 0952-1895 印刷版 / 1468-0491 在线版）。《Governance》发表关于**行政政治、公共政策、公共行政与
国家组织**的理论与经验研究——比较与国际治理、规制治理、政策制定过程、官僚与制度改革、治理网络、问责，
以及国家本身。它兼收定量、定性与比较历史研究，各按其方法论标准评判。

本仓库是**有主见的**。它**不是**通用公共行政写作工具箱，**也不是**把经济学包改个名字套用到政策研究。
它是 **《Governance》专属** 技能栈：一个对**政策、行政与制度具有比较意义**的问题、一个能**跨案例、跨
系统迁移**的论证、一个能在各自方法论标准下站得住的研究设计、**双盲**的稿件准备（须附**独立标题页**），
以及一份诚实说明复现材料是否存在及如何获取的**数据可获取性声明（Data Availability Statement）**。

> **官方依据核对于 2026-06**——本文事实取自 Wiley Online Library 期刊页面、该刊作者指南，以及
> IPSA SOG/RC27 来源。易变的具体信息（编辑与任期、确切字数/摘要上限、投稿系统、费用/APC、ORCID 与
> 参考体例细节）会变化；未直接核实项在
> [`resources/official-source-map.md`](resources/official-source-map.md) 中标记 **待核实**。
> **依赖任何信息前，请以官方期刊页面为准。**

---

## Governance 是什么，为何需要专属技能栈？

《Governance》的约束不同于实务导向期刊、公共管理理论期刊或政策分析期刊：

| 约束 | Governance | 含义 |
|------|------------|------|
| 范围 | **行政政治、公共政策、公共行政、国家组织** | 论文须面向比较治理，而非仅一国/一机构 |
| 看重 | **清晰、原创的介入**，能跨案例与制度情境迁移 | 纯地方性的行政报告或描述性个案不合适 |
| 方法 | 定量/定性/比较历史——任何能立论的**严谨**方法 | 方法须配问题，不要套同一模板 |
| 出版方 / 所有者 | **Wiley(-Blackwell)** / 与 **IPSA SOG（RC27）** 合作 | 通过 **Wiley 投稿系统** 投稿（检索于 2026-06；以官网为准） |
| 评审模式 | **双盲**；**至少两位审稿人** 匿名评审 | 稿件须匿名化，并附**独立标题页** |
| 硬性范围外 | **公司治理**；通常**不收文献综述/文献计量分析** | 不要把公司治理或纯综述论文投到此处 |
| 篇幅 | **≤ 9,000 词，不含引用/参考文献**（官方）；摘要 **约 150 词** | 标题页须标字数；初稿起即守上限 |
| 透明度 | **必须提交数据可获取性声明**；推荐可 DOI 引用的仓库 | 诚实撰写声明；力所能及处存放复现材料 |
| 预分析计划 | 可作为补充材料**提交匿名化的预分析计划** | 在前瞻性、验证性设计中用以表明立场 |

> 《Governance》**要求**提交数据可获取性声明，但——与 APSR 经验证的可复现关卡不同——这是一项
> **强制性声明**，而非编辑部在发表前**真的去复现**的硬性核验关卡。请诚实对待这一区别：构建干净的
> 复现材料包、并尽量做可 DOI 引用的存放，是因为这是良好实践且为推荐做法，而非因为编辑部会把重跑
> 作为接受条件（检索于 2026-06；以官网为准）。

官方作者指南给出的工作字数上限为**不含引用/参考文献的 ≤ 9,000 词**。某第三方信息源称为远低于此的
**3,000–5,000 词**；请以官方 9,000 为工作上限，关于此差异的 **待核实** 说明见
[`resources/official-source-map.md`](resources/official-source-map.md)。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/governance-journal-skills
/plugin install governance-journal-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/governance-journal-skills.git
cd governance-journal-skills

mkdir -p ~/.claude/skills && cp -R skills/govern-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/govern-* ~/.codex/skills/
```

### 第一条提示

```
用 govern-workflow 告诉我，我的 Governance 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
govern-topic-selection
        ▼
govern-literature-positioning
        ▼
govern-theory-building
        ▼
govern-research-design
        ▼
govern-data-analysis
        ▼
govern-tables-figures
        ▼
govern-writing-style          （润色）
        ▼
govern-transparency-and-data
        ▼
govern-review-process
        ▼
govern-submission
        ▼
govern-rebuttal
```

`govern-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。若设计是**前瞻性、验证性**的，
尽早走 `govern-transparency-and-data`，把**匿名化的预分析计划**作为补充材料起草；若贡献是
**跨案例或跨系统的比较**，先用 `govern-topic-selection` 与 `govern-literature-positioning`
在动笔前把跨案例的意义讲清楚。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `govern-workflow` | 路由器——决定下一步调用哪个子技能 |
| `govern-topic-selection` | 比较治理契合；一个能跨案例迁移的原创介入 |
| `govern-literature-positioning` | 回应 Governance 读者期待的政策/行政/制度文献 |
| `govern-theory-building` | 把关于政策、行政或国家的论证打造成贡献 |
| `govern-research-design` | 为设计辩护——比较案例、因果推断、QCA、混合方法 |
| `govern-data-analysis` | 分析规范、不确定性、稳健性、跨案例与组态三角互证 |
| `govern-tables-figures` | 面向比较治理读者的可读、自洽图表 |
| `govern-writing-style` | 在约 9,000 词上限内触达比较政策/行政读者 |
| `govern-transparency-and-data` | 数据可获取性声明；可 DOI 引用的存放；匿名化预分析计划 |
| `govern-review-process` | 双盲评审、桌面筛查、范围契合、决定类别 |
| `govern-submission` | Wiley 系统投稿前检查（匿名化、独立标题页、字数、摘要） |
| `govern-rebuttal` | 面向多位审稿人 + 编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 比较治理数据源
  （V-Dem / Quality of Government / 世界银行 WGI / OECD / 比较议程 / ParlGov / Manifesto Project /
  SGI）以及 R / Stata / Python、QCA/fsQCA 工具与定性研究的 CAQDAS
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 Wiley /
  IPSA SOG 官方 URL，未核实项标 待核实

---

## 与同类期刊的区别

《Governance》容易与相邻的公共行政与政策期刊混淆。请把它定位为**比较政策 / 行政 / 制度**期刊，
并把不契合的稿件分流到别处。

| 期刊 | 所有者 / 出版方 | 独特定位 |
|------|----------------|----------|
| **Governance** | IPSA SOG（RC27）/ **Wiley** | **比较与国际**视角的行政政治、政策、行政、制度 |
| **Public Administration Review（PAR）** | ASPA / Wiley | 以美国为中心、**面向实务**的公共行政 |
| **JPART** | 牛津大学出版社 | **公共行政理论**与组织行为 |
| **JPAM** | Wiley（为 APPAM） | **政策分析**与项目评估，常为美国政策 |
| **Regulation & Governance** | **Wiley**（同门姊妹刊） | **规制研究**与规制治理，跨学科 |

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑与任期、确切字数/摘要上限、投稿系统、费用/APC、参考体例与 ORCID 细节）
  ——请以官方页面为准；未核实项标 待核实
- 不替你判断你的问题是否具有比较治理意义——那是研究者的判断
- **不会**把公司治理论文或独立文献综述变成契合《Governance》的稿件——它们属于范围之外

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Governance（Wiley Online Library）](https://onlinelibrary.wiley.com/journal/14680491) — 出版方主页、当期、作者指南
- [IPSA SOG（RC27）——政府结构与组织](https://www.ipsa.org/) — 与之合作出版《Governance》的研究委员会

---

## 许可

MIT
