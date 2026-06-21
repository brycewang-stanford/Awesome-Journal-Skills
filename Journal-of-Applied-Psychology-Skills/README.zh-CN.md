# 《应用心理学杂志》（Journal of Applied Psychology）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Applied Psychology 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Applied%20Psychology-23457a)](https://www.apa.org/pubs/journals/apl)
[![Field](https://img.shields.io/badge/field-工业组织心理学-1f6feb)](https://www.apa.org/pubs/journals/apl)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《应用心理学杂志》（Journal of Applied Psychology，JAP）** 投稿的 Agent 技能栈。它是
**美国心理学会（APA）旗下工业-组织（I-O）与应用心理学的旗舰期刊**，创刊于 **1917 年**。JAP 发表关于
工作动机、领导力、人员选拔与测评、团队、工作态度与幸福感、组织公正、培训与离职等主题的研究，具有强烈的
**微观/个体层面与测量** 取向。

本仓库是**有主见的**。它**不是**通用心理学写作工具箱，**也不是**把社会科学包改名套用。它是
**JAP 专属**：一道**双重关卡**——既要有真正的 **I-O 理论贡献**，又要有 **测量/设计的严谨性**
（构念效度、共同方法偏差控制、嵌套/多层数据）；配套的定量工具箱（实验室与现场实验、多波次现场研究、
**SEM**、**HLM**、中介/调节、**元分析**）；**匿名（masked）评审**；**APA 第 7 版**体例；以及该刊的
**TOP** 开放科学框架（数据、材料与代码的可得性；预注册纳入考量）。

---

## 《应用心理学杂志》是什么，为何需要专属技能栈？

它的约束与一般实证心理学刊或管理学刊不同：

| 约束 | Journal of Applied Psychology | 含义 |
|------|------|------|
| 门槛 | **既要 I-O 理论贡献，又要测量/设计严谨** | 仅有严谨、或仅有理论，都是常见拒稿 |
| 证据 | 实验室/现场实验、多波次现场研究、SEM、HLM、元分析 | 横断面单一来源自评通常不够 |
| 测量 | **构念效度、信度、测量等价、CMV 控制** | 先报告测量模型，再谈结构模型 |
| 层次 | 个体/团队/组织；**多层与跨层**模型 | 建模嵌套（ICC/r_wg）；分析层次即理论 |
| 出版方 / 所有者 | **美国心理学会（APA）** | 通过 **Editorial Manager**（`/apl`）投稿；匿名评审 |
| 体例 | **APA 第 7 版**；结构化摘要 | 效应量 + 置信区间、拟合指数、精确 p 值 |
| 开放科学 | **TOP 框架**（自 2021-11-01）：数据/材料/代码 + 声明 | 投稿前规划存储与 DOI；披露数据复用 |
| 预注册 | **纳入**评审考量 | 认真预注册，如实报告 |
| 文章类型 | 特稿 · 研究报告 · 理论建构 · 综述 · 质性 · 元分析 | 投稿前选对类型 |

易变的具体信息（编辑、篇幅上限、摘要字数、确切 TOP 等级/措辞、文章类型）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标 **待核实**。
**请以官方页面为准。**

官方依据核对于 **2026-06**（检索于 2026-06；以官网为准）。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/journal-of-applied-psychology-skills
/plugin install journal-of-applied-psychology-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/journal-of-applied-psychology-skills.git
cd journal-of-applied-psychology-skills

mkdir -p ~/.claude/skills && cp -R skills/joap-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/joap-* ~/.codex/skills/
```

### 第一条提示

```
用 joap-workflow 告诉我，我的 Journal of Applied Psychology 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
joap-topic-selection
        ▼
joap-theory-and-hypotheses     （先锁定机制 + 层次）
        ▼
joap-literature-positioning
        ▼
joap-study-design              （测量、CMV、嵌套；在此预注册）
        ▼
joap-data-analysis             （SEM / HLM / 中介 / 元分析）
        ▼
joap-tables-figures
        ▼
joap-writing-style             （APA 第 7 版；贡献前置）
        ▼
joap-open-science-and-transparency
        ▼
joap-review-process
        ▼
joap-submission
        ▼
joap-rebuttal
```

`joap-workflow` 是路由器。此处理论刻意排在文献定位**之前**——JAP 要求先确定机制与分析层次，再用文献
论证其新意。对于元分析与理论建构文章，主线会前移（提前调用 `data-analysis` 或 `theory-and-hypotheses`）。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `joap-workflow` | 路由器——决定下一步调用哪个子技能 |
| `joap-topic-selection` | 双重关卡契合（I-O 理论 + 严谨）；选定文章类型 |
| `joap-theory-and-hypotheses` | I-O 机制、分析层次、方向性 + 验证性假设 |
| `joap-literature-positioning` | 相对最近文献定位贡献；与同类刊的边界 |
| `joap-study-design` | 构念效度、CMV 对策、多层/嵌套设计、检验力 |
| `joap-data-analysis` | SEM/CFA、HLM、带 bootstrap CI 的中介、元分析、充分披露 |
| `joap-tables-figures` | APA 第 7 版表 1、路径/CFA 图、多层结果表、森林/漏斗图 |
| `joap-writing-style` | APA 第 7 版体例；贡献前置叙事；结构化摘要 |
| `joap-open-science-and-transparency` | TOP 数据/材料/代码、数据可得性声明、DOI、数据复用披露 |
| `joap-review-process` | 匿名评审；双重关卡；责任编辑制；桌拒模式 |
| `joap-submission` | Editorial Manager 投稿前检查（体例、匿名化、透明度、图表） |
| `joap-rebuttal` | 面向多位评审 + 责任编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — SEM/HLM/元分析软件（`lavaan`、Mplus、`lme4`、`metafor`/`psychmeta`）、CMV 与等价性工具、预注册（OSF）、数据仓库（OSF/ICPSR/Dataverse/Zenodo）、`papaja`
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 APA 官方 URL，未核实项标 待核实
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 一个 before→after 的 JAP 引言（虚构教学论文）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 按方法 × 主题整理的、经网络核实的真实 JAP 论文，附同类刊辨析

---

## 与同类期刊的区别

| 期刊 | 重心 | JAP 的差异 |
|------|------|------------|
| **Personnel Psychology** | 人员选拔、测评、效度验证 | JAP 以理论机制开篇，而非验证研究 |
| **Academy of Management Journal（AMJ）** | 宏观/中观管理、组织层面结果 | JAP 聚焦微观/个体 + 测量 |
| **OBHDP** | 判断、决策过程、实验性微观 OB | JAP 强调 I-O 理论 + 现场外推 + 测量 |
| **Journal of Organizational Behavior（JOB）** | 宽泛 OB、主题有重叠 | JAP 的测量/定量严谨门槛更高 |

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑、篇幅上限、确切 TOP 等级）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的理论贡献是否足够新颖——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Journal of Applied Psychology（APA）](https://www.apa.org/pubs/journals/apl) — 范围、投稿指南、开放科学政策
- [APA Editorial Manager（apl）](https://www.editorialmanager.com/apl/) — 投稿门户

---

## 许可

MIT
