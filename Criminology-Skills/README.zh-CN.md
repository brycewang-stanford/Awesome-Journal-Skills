# 《犯罪学》（Criminology）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Criminology 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Criminology-1f3a5f)](https://onlinelibrary.wiley.com/journal/17459125)
[![Field](https://img.shields.io/badge/field-犯罪学-1f6feb)](https://asc41.org/publications/criminology-an-interdisciplinary-journal/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《犯罪学》（Criminology）** 投稿的 Agent 技能栈。《犯罪学》是 **美国犯罪学学会（ASC）的旗舰
跨学科期刊**，创刊于 **1963 年**（最初名为 *Criminologica*，**1970 年** 改为现名），由 **Wiley** 以
**季刊** 形式出版。《犯罪学》发表关于 **犯罪与越轨行为的成因、模式与控制** 的顶尖研究：犯罪学理论、
犯罪生涯与生命历程过程、被害（victimization）、社区与犯罪、威慑与程序正义、刑事法律体系——兼收
社会学、心理学、经济学等学科，定量、定性与混合方法并重。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把政策评估包改个名字套到犯罪研究上。
它是 **《犯罪学》专属** 技能栈：强调**以理论为先**的贡献而非裸的犯罪相关性、严谨的**犯罪测量**
（暗数字；UCR / NIBRS / NCVS / 自我报告）、在生命历程论断中区分**个体内 vs. 个体间**变化、**匿名化**
稿件、**无偏见、以人为本（person-first）** 的语言，以及一条可信的**数据与透明度**路径。

---

## 《犯罪学》是什么，为何需要专属技能栈？

《犯罪学》的约束不同于通用社会学期刊或政策刊：

| 约束 | Criminology | 含义 |
|------|-------------|------|
| 范围 | **犯罪的成因、模式与控制**，跨学科 | 论文须推进犯罪学，而非仅使用犯罪数据 |
| 看重 | **理论贡献** + 明确机制 | 描述性的犯罪相关性不合适 |
| 方法 | 定量/定性/混合——各按其标准评判 | 不要把同一模板硬套到所有论文 |
| 犯罪测量 | 报案（**UCR/NIBRS**）、被害（**NCVS**）、自我报告各异 | 须说明所测构念；处理**暗数字** |
| 生命历程论断 | 必须区分**个体内 vs. 个体间**变化 | 发展性论断用固定效应/混合模型 |
| 出版方 / 所有者 | **Wiley** / **美国犯罪学学会** | 使用 ASC/Wiley 官方页面给出的在线投稿入口 |
| 评审模式 | **双匿名评审** | 匿名正文 + 单独标题页 |
| 体例 | **一种 APA 变体**（其余按 APA 第 6 版）；无偏见、以人为本语言 | 非 Chicago；双倍行距；作者简介 < 100 词 |
| 独占性 | **一次只投一刊**——不允许同时投稿 | 投稿即承诺在《犯罪学》发表 |
| 姊妹刊 | 政策评估应投 **Criminology & Public Policy** | 项目评估请投该刊，而非本刊 |

易变信息仍需以投稿当天的官方页面为准。本包只写入
[`resources/official-source-map.md`](resources/official-source-map.md) 中有来源支撑的当前事实：临时编辑信息、
Wiley ACT 中的评审/OA/ORCID/预印本字段，以及 Research Note 通道。本包**不写死**字数/页数或摘要上限；
上传前请看 Wiley 作者指南。

### 文章类型

- **Articles（论文）**——推进犯罪学理论或测量的完整原创研究；学科主力形式。
- **Research Notes（研究札记）**——聚焦、自洽的贡献；《犯罪学》设有独立的研究札记通道。本包不写死
  数字上限；定稿前请看 Wiley 当前 Research Note 说明。
- **复现 / 再评估研究**——重新检验或再现某一有影响力的已发表发现。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/crim-skills
/plugin install crim-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/crim-skills.git
cd crim-skills

mkdir -p ~/.claude/skills && cp -R skills/crim-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/crim-* ~/.codex/skills/
```

### 第一条提示

```
用 crim-workflow 告诉我，我的《犯罪学》稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
crim-topic-selection
        ▼
crim-literature-positioning
        ▼
crim-theory-building
        ▼
crim-research-design
        ▼
crim-data-analysis
        ▼
crim-tables-figures
        ▼
crim-writing-style          （润色）
        ▼
crim-data-and-transparency
        ▼
crim-review-process
        ▼
crim-submission
        ▼
crim-rebuttal
```

`crim-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。若设计是**前瞻性**的，尽早走
`crim-data-and-transparency` 在看到结果前**预注册**；若是重新评估已发表发现，按**复现/再评估**处理，
重点依靠 `crim-research-design` + `crim-data-and-transparency`。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `crim-workflow` | 路由器——决定下一步调用哪个子技能 |
| `crim-topic-selection` | 犯罪学契合与贡献；Article vs. Research Note；与 *CPP* 区分 |
| `crim-literature-positioning` | 跨学科地回应理论论争 |
| `crim-theory-building` | 构建机制、范围条件与可观测含义 |
| `crim-research-design` | 为设计辩护——因果推断、纵向/生命历程、轨迹模型 |
| `crim-data-analysis` | 计数/轨迹/生存模型、个体内 vs. 个体间、稳健性 |
| `crim-tables-figures` | 年龄—犯罪曲线、轨迹与生存图、犯罪地图——自洽可读 |
| `crim-writing-style` | APA 变体体例；无偏见、以人为本语言；触达整个领域 |
| `crim-data-and-transparency` | 数据可得性、可复现材料包、预注册、受限数据 |
| `crim-review-process` | 匿名评审、编辑初筛、决定类别、专家评审 |
| `crim-submission` | 在线投稿前检查（匿名正文、标题页、APA、单刊投稿） |
| `crim-rebuttal` | 面向多位专家评审 + 编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 犯罪与生命历程数据（UCR / NIBRS / NCVS / NACJD / Add Health / NLSY / PHDCN / Pathways）+ R / Stata / Python（轨迹、生存、空间）与 CAQDAS
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条已写入当前事实背后的 ASC / Wiley 官方 URL

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断官方来源没有给出的易变元数据；投稿当天的 Wiley/ASC 页面决定篇幅上限和入口行为
- 不替你判断你的问题是否构成犯罪学贡献——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Criminology（Wiley Online Library）](https://onlinelibrary.wiley.com/journal/17459125) — 出版方主页
- [ASC 上的 Criminology](https://asc41.org/publications/criminology-an-interdisciplinary-journal/) — 所有者、范围、编辑

---

## 许可

MIT
