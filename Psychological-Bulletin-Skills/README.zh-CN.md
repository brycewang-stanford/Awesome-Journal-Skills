# 心理学公报（Psychological Bulletin）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Psychological Bulletin 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Psychological%20Bulletin-6a1b4d)](https://www.apa.org/pubs/journals/bul)
[![Field](https://img.shields.io/badge/field-心理学综述-1f6feb)](https://www.apa.org/pubs/journals/bul)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《心理学公报》（Psychological Bulletin）** 投稿的 Agent 技能栈。它是 **美国心理学会（APA）旗下
专门发表整合性研究综述与元分析的旗舰期刊**，创刊于 **1904 年**，是心理学影响因子最高的期刊之一。
Psychological Bulletin **"发表科学心理学的研究综合（syntheses）"**：系统综述、元分析（meta-analysis）、
元综述（meta-review）、元综合（meta-synthesis），以及严谨的定性综述。

本仓库是**有主见的**。它**不是**通用心理学写作工具箱，**也不是**把 Psychological Science 或 JPSP 包
改个名字套用——那些期刊发表**原始实证研究**，而 Psychological Bulletin **不发表**。这里的成果是
**一篇综合，而非一项研究**。因此这是 **综述 / 元分析专属** 技能栈：一个**可元分析**的问题、一次
**系统化 PRISMA 检索**、透明的**纳入标准 + 双人编码**、**随机效应**合并、**调节变量与发表偏倚**诊断、
由综合提炼出的**理论贡献**、**MARS/PRISMA/JARS** 报告规范、**APA 第 7 版**体例、**单向匿名（masked）**
评审，以及一份**预注册**的透明协议。

---

## Psychological Bulletin 是什么，为何需要专属技能栈？

Psychological Bulletin 的约束与原始研究刊截然不同：

| 约束 | Psychological Bulletin | 含义 |
|------|------------------------|------|
| 出版方 / 所有者 | **美国心理学会（APA）** | 通过 APA **Editorial Manager** 投稿 |
| 发表什么 | **研究综合**——系统综述、**元分析**、元综述、元综合、定性综述 | 做的是综合，**不是**原始研究 |
| 不做什么 | **不发表原始实证研究**；原创**理论** → *Psychological Review* | 若贡献是新数据或纯理论则不合适 |
| 核心方法 | **元分析** + 对既有文献的系统综述 | "数据"是既有研究，单位是**效应量** |
| 评审模式 | **单向匿名（masked）**，评审看不到作者身份 | 稿件须匿名化，中性化自引 |
| 摘要 | **≤ 250 词** | 单独成页 |
| 体例 | **APA 出版手册第 7 版** | 作者—年份；APA 标题与表格 |
| 报告规范 | **MARS**（元分析）· **PRISMA**（系统综述）· **JARS**（定量/混合） | 按综合类型选用对应规范 |
| 透明度 | 对包括元分析在内的实证工作要求透明报告（**TOP**，自 2022-02-01 起）；须提供**数据库、编码本、脚本** | 边编码边建材料包 |
| 预注册 | 须说明设计/假设是否预注册及获取途径；**PROSPERO**/OSF | 在筛选**之前**注册协议 |
| 费用 | 未列**投稿费** | 核实接受后的开放获取 APC |

易变的具体信息（现任编辑与任期、确切 TOP 级别、摘要/篇幅措辞、可接受综述类型、费用/APC）会变化——
未直接核实项在 [`resources/official-source-map.md`](resources/official-source-map.md) 中标记
**待核实**。**请以 APA 官方期刊页面为准。**

### 什么样的稿件算 Psychological Bulletin 论文

- **元分析（Meta-analysis）**——跨研究定量合并效应量（随机效应、异质性）。
- **系统综述（Systematic review）**——穷尽式、PRISMA 记录的检索与评价。
- **元综述 / 元综合（Meta-review / meta-synthesis）**——对既有综述或定性发现进行综合。
- **定性 / 叙事综述**——当文献难以合并时的严谨整合性评价。

> 最常见的不合适：投来原始实证研究或纯新理论。它们属于其他 APA 期刊（理论投
> *Psychological Review*）。Bulletin 综合的是**既有**研究。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/psychbull-skills
/plugin install psychbull-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/psychbull-skills.git
cd psychbull-skills

mkdir -p ~/.claude/skills && cp -R skills/psychbull-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/psychbull-* ~/.codex/skills/
```

### 第一条提示

```
用 psychbull-workflow 告诉我，我的 Psychological Bulletin 综述下一步该用哪个技能。
```

---

## 默认工作流

```text
psychbull-topic-selection          （是否值得综述 / 可元分析？）
        ▼
psychbull-literature-search-strategy   （系统检索；PRISMA；数据库）
        ▼
psychbull-inclusion-and-coding     （纳入标准；双人编码；信度）
        ▼
psychbull-meta-analysis-methods    （效应量；随机效应；异质性）
        ▼
psychbull-moderators-and-bias      （元回归；发表偏倚诊断）
        ▼
psychbull-theory-integration       （把综合提炼为贡献）
        ▼
psychbull-tables-figures           （森林图 / 漏斗图；PRISMA 流程图）
        ▼
psychbull-writing-style            （APA 第 7 版；MARS/JARS；摘要 ≤ 250 词）
        ▼
psychbull-open-science-and-transparency
        ▼
psychbull-submission
        ▼
psychbull-rebuttal
```

`psychbull-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。第一个实质决定是：问题是否
**值得综述且可元分析**，以及哪种**综合类型**（元分析 / 系统 / 定性）契合该文献。筛选**之前**先注册
**协议**（PROSPERO/OSF）。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `psychbull-workflow` | 路由器——决定下一步调用哪个子技能 |
| `psychbull-topic-selection` | 检验是否值得综述 / 可元分析；选定综合类型 |
| `psychbull-literature-search-strategy` | 跨数据库系统、可复现检索；PRISMA 记录 |
| `psychbull-inclusion-and-coding` | 纳入标准、双人编码、编码本、评分者间信度 |
| `psychbull-meta-analysis-methods` | 效应量提取、随机效应模型、异质性（I²/τ²） |
| `psychbull-moderators-and-bias` | 元回归、发表偏倚诊断、敏感性/稳健性 |
| `psychbull-theory-integration` | 把综合提炼为理论贡献，而非一张表 |
| `psychbull-tables-figures` | 森林图/漏斗图、PRISMA 流程图、MARS 表格 |
| `psychbull-writing-style` | APA 第 7 版；MARS/PRISMA/JARS 结构；摘要 ≤ 250 词 |
| `psychbull-open-science-and-transparency` | 预注册（PROSPERO/OSF）、TOP、数据库+编码本+脚本 |
| `psychbull-submission` | Editorial Manager 投稿前检查（匿名化、摘要、MARS/PRISMA 清单） |
| `psychbull-rebuttal` | 面向多位评审 + 编辑的 R&R 回应，且不破坏综合 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 检索/筛选（PsycINFO、Covidence、Rayyan）、元分析软件（`metafor`、`robumeta`、Stata `meta`、CMA）、偏倚诊断，以及 MARS/PRISMA/JARS 规范
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 APA / MARS / PRISMA / PROSPERO / TOP 官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的综述，也不替你跑元分析
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑与任期、确切 TOP 级别、摘要/篇幅规则、费用/APC、政策措辞）——请以 APA 官方页面为准；未核实项标 待核实
- 不替你判断问题是否值得综述、文献是否可合并——那是研究者的判断
- 不把一项原始实证研究"改造"成 Bulletin 论文——那是范畴错误；请综合既有工作

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Psychological Bulletin（APA）](https://www.apa.org/pubs/journals/bul) — 所有者、范围、投稿指南
- [APA MARS / JARS](https://apastyle.apa.org/jars) · [PRISMA](http://www.prisma-statement.org/) · [PROSPERO](https://www.crd.york.ac.uk/prospero/) — 报告规范与协议注册

---

## 许可

MIT
