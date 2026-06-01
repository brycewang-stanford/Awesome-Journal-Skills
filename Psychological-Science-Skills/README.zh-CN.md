# 《心理科学》（Psychological Science）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Psychological Science 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Psychological%20Science-0e7c7b)](https://journals.sagepub.com/home/pss)
[![Field](https://img.shields.io/badge/field-心理学-1f6feb)](https://www.psychologicalscience.org/publications/psychological_science)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《心理科学》（Psychological Science）** 投稿的 Agent 技能栈。它是 **美国心理科学学会（APS）的
旗舰实证期刊**，创刊于 **1990 年**，由 **SAGE** 出版。该刊发表心理学各领域简洁而高影响力的实证研究，
是该领域 **开放科学** 的引领者之一。

本仓库是**有主见的**。它**不是**通用心理学写作工具箱，**也不是**把社会科学包改名套用。它是
**《心理科学》专属**：紧凑的**短报告**格式、**150 词结构化摘要**、**APA 第 7 版**体例且图表嵌入正文、
严格的统计标准（效应量 + 置信区间、样本量论证、充分披露），以及该刊 **2024 年后的开放科学制度**——
强制开放数据与材料，外加一份会被**评分**的 **研究透明度声明（Research Transparency Statement）**。

---

## 《心理科学》是什么，为何需要专属技能栈？

它的约束与长篇幅社科刊截然不同：

| 约束 | Psychological Science | 含义 |
|------|------|------|
| 格式 | **引言 + 讨论 + 脚注 + 致谢 + 附录 ≤ 合计 2,000 词**；方法 + 结果不计入（≤ 约 2,500） | 论证须紧凑；无冗长文献综述 |
| 摘要 | **150 词**，须写明 **样本量、参与者总体、设计的重要局限** | 结构化、含信息量的摘要 |
| 体例 | **APA 第 7 版**；**图表嵌入**正文 | 非置于文末 |
| 出版方 / 所有者 | **SAGE** / **APS** | 通过 **Manuscript Central**（`/psci`）投稿；匿名 |
| 开放科学 | 自 **2024-01-01** 起**强制开放数据 + 材料**（个案豁免） | 投稿前先规划存储与 DOI |
| 透明度 | **研究透明度声明**置于引言与方法之间，并在评审中**评分** | “透明度的限制将是编辑决定的因素” |
| 预注册 | **其质量纳入编辑决定**（徽章已停用） | 认真预注册，如实报告 |
| 统计 | **效应量 + 置信区间**、样本量论证/检验力、充分披露 | 仅报告星号不行 |
| 文章类型 | 研究论文 · Registered Reports（一/二阶段）· 既有数据 RR · 评论（≤1,000） | 投稿前选对类型 |

易变的具体信息（编辑、确切字数格式、开放科学措辞、文章类型）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标 **待核实**。
**请以官方页面为准。**

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/psci-skills
/plugin install psci-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/psci-skills.git
cd psci-skills

mkdir -p ~/.claude/skills && cp -R skills/psci-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/psci-* ~/.codex/skills/
```

### 第一条提示

```
用 psci-workflow 告诉我，我的 Psychological Science 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
psci-topic-selection
        ▼
psci-literature-positioning
        ▼
psci-theory-and-hypotheses
        ▼
psci-study-design          （前瞻性研究在此预注册）
        ▼
psci-data-analysis
        ▼
psci-tables-figures
        ▼
psci-writing-style          （按字数格式润色）
        ▼
psci-open-science-and-transparency
        ▼
psci-review-process
        ▼
psci-submission
        ▼
psci-rebuttal
```

`psci-workflow` 是路由器。若设计为**前瞻性**，尽早走 `psci-study-design` 与 `psci-review-process`
以采用 **Registered Reports**（数据收集前先获一阶段接受）。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `psci-workflow` | 路由器——决定下一步调用哪个子技能 |
| `psci-topic-selection` | 高影响力实证契合；研究论文 vs Registered Report |
| `psci-literature-positioning` | 在有限篇幅内定位广泛、累积性的贡献 |
| `psci-theory-and-hypotheses` | 清晰陈述理论与验证性/探索性假设 |
| `psci-study-design` | 检验力/样本量论证、预注册、混淆控制 |
| `psci-data-analysis` | 效应量 + 置信区间、充分披露、杜绝 p-hacking/HARKing |
| `psci-tables-figures` | APA 第 7 版、嵌入正文的图表 |
| `psci-writing-style` | 2,000 词格式下的 APA 体例；150 词结构化摘要 |
| `psci-open-science-and-transparency` | 强制开放数据/材料、研究透明度声明、DOI |
| `psci-review-process` | 匿名评审；透明度与预注册作为评分因素 |
| `psci-submission` | Manuscript Central 投稿前检查（格式、摘要、匿名化、透明度） |
| `psci-rebuttal` | 面向多位评审 + 编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 预注册（OSF）、数据仓库（OSF/Dataverse/Zenodo）、检验力分析（G*Power/`simr`）、效应量/置信区间工具、`papaja`
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 APS / SAGE 官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑、确切字数格式、开放科学措辞）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的发现是否足够稳健与重要——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Psychological Science（APS）](https://www.psychologicalscience.org/publications/psychological_science) — 所有者、投稿指南、开放科学政策
- [Psychological Science（SAGE）](https://journals.sagepub.com/home/pss) — 出版方主页

---

## 许可

MIT
