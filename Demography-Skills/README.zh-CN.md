# Demography（《人口学》）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Demography 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Demography-0b6e4f)](https://read.dukeupress.edu/demography)
[![Field](https://img.shields.io/badge/field-人口科学-1f6feb)](https://www.populationassociation.org/demography/home)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《Demography》（人口学）** 投稿的 Agent 技能栈。Demography 是 **美国人口学会（Population
Association of America, PAA）的旗舰期刊**，创刊于 **1964 年**，自 **2021 年** 起由 **杜克大学出版社
（Duke University Press）** 出版。该刊采用 **Subscribe to Open（S2O，订阅转开放）** 模式，**对读者
完全开放阅读**，发表 **人口科学** 领域最高质量的研究：人口如何变化，以及生育、死亡、迁移的成因与后果——
取材自人类学、生物学、经济学、流行病学、地理学、历史学、心理学、公共卫生、社会学与统计学。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把经济学或社会学包改个名字套用到人口
研究。它是 **Demography 专属** 技能栈：一个对人口学家具有**普遍意义**的真正**人口变化问题**、一个能
**跨人口成分对话**的论证（研究死亡的学者也应在意你关于生育的论文）、一个在**人口学标准**下站得住的研究
设计（选对生命表、分解、事件史或年龄—时期—世代方法）、**双向匿名**的稿件准备，以及一份**数据可得性声明**
加上存入 FAIR 仓库的**可复现代码**。

---

## Demography 是什么，为何需要专属技能栈？

Demography 的约束不同于通用社会科学刊或方法刊：

| 约束 | Demography | 含义 |
|------|------------|------|
| 范围 | **人口科学**——人口如何变化；生育、死亡、迁移 | 论文必须提出真正的人口问题，而非仅使用人口数据 |
| 看重 | **对人口学家的普遍意义** + 清晰贡献 | 仅用人口数据的窄应用结果不合适 |
| 方法 | 生命表、分解、事件史、APC、多状态、微观模拟、预测、因果——各按其标准评判 | 选能回答问题的人口学方法 |
| 出版方 / 所有者 | **杜克大学出版社**（自 2021）/ **PAA** | 通过 **ScholarOne** 投稿，非 Editorial Manager（2024 年迁移） |
| 评审模式 | **双向匿名（double-blind）** | 避免自我指认引用；作者与评审互盲 |
| 获取模式 | **Subscribe to Open（S2O）**——**免费阅读**；**非** APC 期刊 | 那笔 $1,000 费用**不是**开放获取费 |
| 费用 | **$35 投稿费** + 接受时 **$1,000 编辑管理费**（两者皆可豁免） | 预算 $35；$1,000 在接受后且可豁免 |
| 篇幅 | **论文 <= 8,000 词**；**研究札记 <= 4,000**；**评论 <= 2,000**；**摘要 <= 200** | 正文字数不含摘要/关键词/脚注/参考文献 |
| 前置材料 | **3-5 条 highlights**（每条 <= 85 字符）；**<= 5 个关键词**；**宽松 APA** 体例 | highlights 与关键词为必填，须按规格 |
| 透明度 | **数据可得性声明** + 持久标识；鼓励**可复现代码** | Demography 不设自有仓库——须自行存入 FAIR 仓库 |

易变的具体信息（编辑与任期、确切上限、费用金额/豁免、当年哪一卷开放、政策措辞）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记 **待核实**。
**请以官方页面为准。**

### 三种文章类型

- **Research Article（研究论文）**——完整原创人口研究；正文 **<= 8,000 词**。
- **Research Note（研究札记）**——一项聚焦、自洽的贡献；**<= 4,000 词**。
- **Commentary（评论）**——简短回应或受邀评述；**<= 2,000 词**。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/demog-skills
/plugin install demog-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/demog-skills.git
cd demog-skills

mkdir -p ~/.claude/skills && cp -R skills/demog-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/demog-* ~/.codex/skills/
```

### 第一条提示

```
用 demog-workflow 告诉我，我的 Demography 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
demog-topic-selection
        ▼
demog-literature-positioning
        ▼
demog-theory-building
        ▼
demog-research-design
        ▼
demog-data-analysis
        ▼
demog-tables-figures
        ▼
demog-writing-style          （润色）
        ▼
demog-data-and-reproducibility
        ▼
demog-review-process
        ▼
demog-submission
        ▼
demog-rebuttal
```

`demog-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。多数人口学论文会在**理论 ↔ 设计 ↔ 分析**
之间多次循环，在生命表、分解、事件史或年龄—时期—世代等框架中反复抉择，然后再进入写作与数据可得性声明阶段。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `demog-workflow` | 路由器——决定下一步调用哪个子技能 |
| `demog-topic-selection` | 人口问题契合度与普遍意义；选对文章类型 |
| `demog-literature-positioning` | 跨人口成分对话；回应读者期待的人口学文献 |
| `demog-theory-building` | 把机制、恒等式或更精确的估计打造成贡献 |
| `demog-research-design` | 选择并为人口学方法辩护（生命表、分解、事件史、APC） |
| `demog-data-analysis` | 率/暴露构建、不确定性、分解、APC、生存分析严谨性 |
| `demog-tables-figures` | 人口金字塔、Lexis 曲面、生存曲线、年龄模式图 |
| `demog-writing-style` | 体例（宽松 APA）；摘要、highlights、关键词；字数/图表上限 |
| `demog-data-and-reproducibility` | 数据可得性声明、FAIR 仓库存放、可复现代码 |
| `demog-review-process` | 双向匿名评审、预审/桌面筛查、分主题领域副编辑 |
| `demog-submission` | ScholarOne 投稿前检查（匿名化、上限、highlights、$35 费用） |
| `demog-rebuttal` | 面向专家评审 + 综合意见编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 人口数据源（HMD / HFD / IPUMS / DHS / HRS / WPP）+ R / Stata / Python 人口学软件包（生命表、分解、生存、APC、微观模拟）
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 PAA / 杜克官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑与任期、确切上限、费用金额/豁免、当年哪一卷开放、政策措辞）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的问题是否对人口学家具有普遍意义——那是研究者的判断
- 不把 $1,000 编辑管理费当作开放获取费——Demography 在 S2O 下免费阅读

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [杜克大学出版社上的 Demography](https://read.dukeupress.edu/demography) — 出版方主页、当期目录
- [PAA 上的 Demography](https://www.populationassociation.org/demography/home) — 所有者、作者指南、政策
- [Demography 开放获取（Subscribe to Open）FAQ](https://www.dukeupress.edu/open-access/frequently-asked-questions-(faqs)-about-demography) — S2O 资助模式

---

## 许可

MIT
