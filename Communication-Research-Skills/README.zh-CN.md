# Communication Research 技能包

<p align="center">
  <img src="assets/cover.svg" alt="Communication Research 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Communication%20Research-23457a)](https://journals.sagepub.com/home/crx)
[![Field](https://img.shields.io/badge/field-Communication%20Science-1f6feb)](https://journals.sagepub.com/home/crx)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Communication Research（CR）** 投稿的智能体技能栈——这是 SAGE 旗下**定量、社会科学取向**的传播学
期刊。CR 以**假设检验型实验与调查**为主，强调严谨测量与明确理论：媒介效果与信息加工、说服与讯息效果、
人际与组织传播、健康与政治传播，以及新媒体使用与效果。

本仓库立场鲜明。它**不是**通用社会科学写作工具箱，也**不是**把《Journal of Communication》（ICA 全
范式旗舰刊）改装而成。它是**CR 专属**技能栈：一个带有**可检验机制**（中介/调节）的传播科学问题、以定量
标准并辅以**有效且可信的测量**来辩护的研究设计、**APA** 统计报告（效应量与标准差）、**双向匿名**准备，
以及在写作过程中同步准备好的**数据可得性声明**与可复现材料。

---

## CR 是什么，为何需要专属技能栈？

CR 的约束与通用刊或质性传播刊不同：

| 约束 | Communication Research | 含义 |
|------|------------------------|------|
| 范围 | **定量、社会科学取向**的传播科学 | 质性/阐释性研究不匹配——改投同类刊 |
| 看重 | **可检验机制**（中介/调节），而非单纯主效应 | 无过程的主效应难以达标 |
| 方法 | 实验、面板调查、带信度的内容分析 | 以有效测量匹配定量设计 |
| 出版方 | **SAGE 出版社**（创刊于 1974；双月刊） | 经 **SAGE Track**（ScholarOne）投稿 |
| 评审模式 | **双向匿名**；进入 Revise/Accept 需**两份独立评审** | 正文与补充材料均需匿名；要说服两位专家 |
| 篇幅 | 稿件**不超过 45 页，双倍行距，含参考文献** | 参考文献计入篇幅；细节移入在线补充材料 |
| 体例/报告 | **APA**；报告**效应量与标准差** | 仅有显著性星号属于 APA 报告失格 |
| 透明度 | **数据可得性声明**；开放材料/数据；预注册 | 写作时同步准备声明与材料 |
| 测量 | 经验证的量表（alpha/omega、CFA）；编码者间信度；CMV 控制 | 评审会审查构念效度，而不止信度 |

易变细节（主编与任期、确切篇幅、费用/APC、数据/ORCID 要求层级）会变动——未直接核实的项目在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标注 **待核实**。请以
**SAGE 官方期刊页面为准**（检索于 2026-06；以官网为准）。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/communication-research-skills
/plugin install communication-research-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/communication-research-skills.git
cd communication-research-skills

mkdir -p ~/.claude/skills && cp -R skills/commres-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/commres-* ~/.codex/skills/
```

### 第一条提示词

```
使用 commres-workflow 告诉我，我的 Communication Research 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
commres-topic-selection
        ▼
commres-literature-positioning
        ▼
commres-theory-building
        ▼
commres-research-design
        ▼
commres-data-analysis
        ▼
commres-tables-figures
        ▼
commres-writing-style          （润色）
        ▼
commres-transparency-and-data
        ▼
commres-review-process
        ▼
commres-submission
        ▼
commres-rebuttal
```

`commres-workflow` 是路由器——根据你所处阶段告诉你下一步该用哪个技能。若你的设计是**前瞻性**的，尽早进入
`commres-transparency-and-data` 以**预注册**；多数 CR 论文在润色前会多次往复于理论 ↔ 设计 ↔ 测量。

---

## 技能一览

| 技能 | 用途 |
|------|------|
| `commres-workflow` | 路由器——决定下一步调用哪个子技能 |
| `commres-topic-selection` | 定量、检验理论的契合度；要可检验机制，而非平台新奇 |
| `commres-literature-positioning` | 针对既有实证检验定位；推进到编号假设 |
| `commres-theory-building` | 构念、机制与编号假设（中介/调节） |
| `commres-research-design` | 以定量标准辩护实验/面板调查/内容分析 |
| `commres-data-analysis` | 方差/回归/SEM、带 bootstrap CI 的中介、APA 报告、稳健性 |
| `commres-tables-figures` | 自足、可达性强的 APA 图表，展示效应量与不确定性 |
| `commres-writing-style` | 累积式社会科学行文；APA；45 页篇幅 |
| `commres-transparency-and-data` | 数据可得性声明；开放材料/数据；预注册；ORCID |
| `commres-review-process` | 双向匿名评审；两份独立评审的要求 |
| `commres-submission` | SAGE Track 投稿前检查（匿名、45 页上限、APA 报告、DAS） |
| `commres-rebuttal` | 面向两位严格定量评审与编辑的修回应答策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 传播学数据源（ANES / CES / Pew / HINTS / GDELT）与 R / SPSS-PROCESS / Mplus / Python，侧重测量/信度/SEM
- [`resources/official-source-map.md`](resources/official-source-map.md) — 支撑每条事实的 SAGE/CR 官方网址，未核实项标注 待核实
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 虚构的 CR 风格引言 + 摘要范例
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 按方法 × 主题整理、经网络核实的真实 CR 论文
- [`resources/code/`](resources/code/) — 内置可复现的 Stata + Python 分析脚手架

---

## 与同类期刊的区别

| 期刊 | 所有者 / 出版方 | 范式 | 本技能包的提醒 |
|------|----------------|------|----------------|
| **Communication Research** | SAGE | **定量、社会科学取向** | 假设检验型传播科学的归属地 |
| Journal of Communication | ICA / Oxford UP | 全范式、覆盖全领域的旗舰刊 | 更宽泛、并非只限定量——通用/阐释性研究应改投 |
| Human Communication Research | ICA / Oxford UP | 人际 / HCR | 更契合 HCR 的人际理论检验工作应改投 |
| New Media & Society | SAGE | 数字媒体，常更偏质性 | 平台导向或质性数字媒体研究应改投 |

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何具体编辑或评审的口味
- 不断言易变元数据（现任主编与任期、确切篇幅、费用/APC、要求层级）——请以官网为准；未核实项标注 待核实
- 不替你判断你的研究是否足够定量与检验理论——这是研究者自己的判断

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Communication Research（SAGE Journals）](https://journals.sagepub.com/home/crx) — 出版方主页
- [CR 投稿指南（SAGE）](https://journals.sagepub.com/author-instructions/crx) — 作者须知

---

## 许可证

MIT
