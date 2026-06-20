# 社会心理学季刊（SPQ）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Social Psychology Quarterly 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-SPQ-2b6b6b)](https://journals.sagepub.com/home/spq)
[![Field](https://img.shields.io/badge/field-社会学取向社会心理学-1f6feb)](https://www.asanet.org/publications/journals/social-psychology-quarterly/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《社会心理学季刊》（Social Psychology Quarterly, SPQ）** 投稿的 Agent 技能栈。SPQ 是
**社会学取向社会心理学（sociological social psychology）的旗舰期刊**，由 **美国社会学会（ASA）** 拥有、
**SAGE** 出版。期刊创刊于 **1937 年**（原名 *Sociometry*，1978 年更名 *Social Psychology*，1979 年定为现名），
发表关于 **个体与社会之间联系** 的理论与实证研究——自我与认同、社会结构与人格、群体过程、社会互动、
符号互动、地位与期望状态、情感与情绪。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**不是**把心理学取向社会心理学包
（JPSP / Psychological Science）改名套用，**也不是**把综合性社会学包（ASR / AJS）改名套用。
SPQ 的核心是 **社会结构与个体之间的联系**：一条社会心理学机制、在所属传统的方法论标准下站得住的研究设计、
**匿名（masked）** 的稿件准备，以及通过 **SageTrack** 投稿、缴纳 ASA **$25 处理费**、遵循 ASA 的
**数据共享** 规范——而该规范下共享材料是 **鼓励但非强制**。

---

## SPQ 是什么，为何需要专属技能栈？

SPQ 是 **社会学内部的社会心理学专门刊**——既不同于心理学期刊，也不同于综合性社会学期刊：

| 约束 | 社会心理学季刊（SPQ） | 含义 |
|------|------|------|
| 范围 | **社会学取向社会心理学**——结构与个体的联系 | 非个体认知（JPSP/Psych Sci）；非宏观社会学（ASR/AJS） |
| 看重 | 一条连接结构/过程与自我的**社会心理学机制** | 仅有相关或仅是巧妙实验发现都不合适 |
| 传统 | 符号互动 · 社会结构与人格 · 群体过程 · 认同 · 情感 | 把论文定位在某一传统，并对话其研究纲领 |
| 方法 | **实验、调查/二手数据、观察/民族志**——各按其标准评判 | 不要把同一模板硬套到所有论文 |
| 出版方 / 所有者 | **SAGE** / **ASA** | 通过 **SageTrack / Manuscript Central** 投稿 |
| 评审模式 | **匿名（masked）**——匿名正文 + **单独标题页** | 匿名不充分的稿件会被**临时退回** |
| 费用 | 首次投稿 **$25** 处理费（再投稿与 ASA 学生会员免收） | 除非符合免收条件，否则需预算 |
| 篇幅 | **论文 ≤ 10,000 词**（含各部分、不含补充材料）；**Note ≤ 5,000** | 字数标注在标题页 |
| 摘要 | **约 150 词**，**不含身份信息**，附关键词；摘要页省略作者名 | 简短且匿名的摘要 |
| 体例 | **ASA 体例指南**（作者—年份） | 非 APA；非泛用 Chicago |
| 数据 / 透明度 | 共享数据/代码/材料**鼓励但非强制**；**不影响录用** | 是一种规范，**不是**编辑核验的复现门槛 |

本包中的期刊事实已映射到
[`resources/official-source-map.md`](resources/official-source-map.md) 中的 SAGE / ASA 来源。真正上传前，
仍需现场检查官方页面上的操作信息，例如投稿链接、费用流程、编辑部邮箱、文件处理、开放获取提示与政策措辞。

### 社会学取向社会心理学的传统

- **符号互动**——意义、自我与互动秩序如何被建构与管理。
- **社会结构与人格（SSP）**——结构位置如何塑造自我、福祉与态度。
- **群体过程**——互动中的地位、期望状态、交换、合法性与公正。
- **认同理论**——认同的凸显性、突出性与验证，及其结构前因。
- **情感与情绪**——情感、印象形成与情绪管理（如情感控制理论）。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/spq-skills
/plugin install spq-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/spq-skills.git
cd spq-skills

mkdir -p ~/.claude/skills && cp -R skills/spq-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/spq-* ~/.codex/skills/
```

### 第一条提示

```
用 spq-workflow 告诉我，我的 SPQ 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
spq-topic-selection
        ▼
spq-literature-positioning
        ▼
spq-theory-building
        ▼
spq-research-design
        ▼
spq-data-analysis
        ▼
spq-tables-figures
        ▼
spq-writing-style          （润色）
        ▼
spq-data-and-transparency
        ▼
spq-review-process
        ▼
spq-submission
        ▼
spq-rebuttal
```

`spq-workflow` 是路由器——根据你所处阶段、论文所属**传统**（符号互动 / SSP / 群体过程 / 认同 / 情感）、
以及你写的是完整 **Article** 还是 **Note**，告诉你下一步用哪个技能。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `spq-workflow` | 路由器——决定下一步调用哪个子技能 |
| `spq-topic-selection` | 检验结构—个体契合；定位传统；Article 还是 Note |
| `spq-literature-positioning` | 把论文放进社会学取向社会心理学的研究纲领 |
| `spq-theory-building` | 构建连接社会结构/过程与个体的机制 |
| `spq-research-design` | 为设计辩护——实验、调查/二手数据、观察/民族志 |
| `spq-data-analysis` | 分析规范、测量质量、不确定性、稳健性 |
| `spq-tables-figures` | 自洽、ASA 体例、能展示结构—个体联系的图表 |
| `spq-writing-style` | ASA 体例指南；在约 10,000 词内同时触达社会学与心理学读者 |
| `spq-data-and-transparency` | ASA 数据共享规范；鼓励而非强制；定性研究的保密 |
| `spq-review-process` | 匿名评审、匿名检查、契合筛查、决定模式 |
| `spq-submission` | SageTrack 投稿前检查（匿名、标题页、$25 费、约 150 词摘要） |
| `spq-rebuttal` | 面向跨传统评审 + 编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 社会学取向社会心理学数据源（GSS / ACL / MIDUS / Add Health）+ 实验、调查、SEM、情感控制与 CAQDAS 工具（按传统） |
- [`resources/official-source-map.md`](resources/official-source-map.md) — 本包期刊专属事实背后的 SAGE / ASA 官方 URL

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不替代最终上传前对操作性元数据（投稿链接、费用流程、当前编辑名单、文件处理、政策措辞）的现场检查
- 不把心理学论文或宏观社会学论文变成 SPQ 论文——结构—个体的贡献需要研究者自己做出

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Social Psychology Quarterly（SAGE）](https://journals.sagepub.com/home/spq) — 出版方主页
- [ASA 上的 SPQ](https://www.asanet.org/publications/journals/social-psychology-quarterly/) — 所有者、投稿信息、政策

---

## 许可

MIT
