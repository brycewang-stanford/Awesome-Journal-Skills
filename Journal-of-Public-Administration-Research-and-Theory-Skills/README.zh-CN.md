# 公共行政研究与理论期刊（JPART）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Public Administration Research and Theory 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JPART-1f5135)](https://academic.oup.com/jpart)
[![Field](https://img.shields.io/badge/field-公共行政-1f6feb)](https://www.pmranet.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《公共行政研究与理论期刊》（Journal of Public Administration Research and Theory, JPART）** 投稿的
Agent 技能栈。JPART 是 **公共行政领域“理论 + 研究”的旗舰期刊**，创刊于 **1991 年**，由 **牛津大学出版社
（OUP）** 代表 **公共管理研究学会（PMRA）** 出版。它发表关于公共部门的最高质量 **理论与经验** 研究：
官僚行为、公共服务动机（PSM）、繁文缛节（red tape）、代表性官僚制、绩效管理、协作与网络治理，以及
行为公共行政。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**政策评估技能包。它是 **JPART 专属**
技能栈：一个对 **公共管理理论** 的贡献、一个被命名的 **机制**、一个越来越以 **实验与因果** 标准辩护的
研究设计、**双向匿名** 的稿件准备，以及作为发表条件的 **数据与代码公开**。

---

## JPART 是什么，为何需要专属技能栈？

JPART 的约束不同于宽口径 PA 刊或政策分析刊：

| 约束 | JPART | 含义 |
|------|------|------|
| 看重 | 对 **公共管理理论** 的贡献 + 严谨经验研究 | 仅有政策性发现不合适 |
| 机制 | 一个被 **命名的机制**，而非仅一个效应 | “在情境 Y 检验 X”还不够 |
| 方法 | 越来越 **实验与因果**；多层次；混合方法 | 正面处理共同方法偏差与自选择 |
| 出版方 / 所有者 | **牛津大学出版社** / **PMRA** | 通过 **Editorial Express** 投稿，而非 ScholarOne/Editorial Manager |
| 评审模式 | **双向匿名**，详尽且具发展性 | 稿件须匿名；身份信息只放封面页 |
| 篇幅 | **约 12,000 词，含摘要、表格与参考文献** | 上限把参考文献也算进去——精简引用 |
| 摘要 | 须写明 **理论取径 → 方法/数据 → 结果 → 对理论的含义** | 以理论取径开篇 |
| 关键词 | **3–5 个**；前三个分别标示 **理论、研究主题、方法** | 不是自由标签 |
| 体例 | **OUP 作者—年份**，附 DOI | 参考文献按字母排序，须带 DOI |
| 透明度 | 作为发表条件 **公开数据与代码**；须有数据可得性声明 | 边做边建；公开是强制的 |

易变的具体信息（编辑与任期、确切上限、费用/APC、政策措辞）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记 **待核实**。
**请以官方页面为准**（检索于 2026-06；以官网为准）。

### 与兄弟期刊的区分

- **Public Administration Review (PAR)** —— 更宽、更整合、更面向实务。
- **JPAM** —— 政策分析与项目评估。
- **Governance** —— 政府的比较制度研究，较少公共管理机制。
- **JPART** —— 以严谨（常为实验/因果）经验研究检验的 **公共管理理论**。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jpart-skills
/plugin install jpart-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/jpart-skills.git
cd jpart-skills

mkdir -p ~/.claude/skills && cp -R skills/jpart-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jpart-* ~/.codex/skills/
```

### 第一条提示

```
用 jpart-workflow 告诉我，我的 JPART 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
jpart-topic-selection
        ▼
jpart-literature-positioning
        ▼
jpart-theory-building
        ▼
jpart-research-design
        ▼
jpart-data-analysis
        ▼
jpart-tables-figures
        ▼
jpart-writing-style          （润色）
        ▼
jpart-transparency-and-data
        ▼
jpart-review-process
        ▼
jpart-submission
        ▼
jpart-rebuttal
```

`jpart-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能，并执行本刊的核心闸门：
**是否有公共管理理论贡献？** 若理论位空缺，它会先把你送回 theory-building 或 topic-selection，再放行后续。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `jpart-workflow` | 路由器——决定下一步调用哪个子技能；执行理论闸门 |
| `jpart-topic-selection` | 公共管理理论契合；在 PAR / JPAM / Governance 之间选对期刊 |
| `jpart-literature-positioning` | 点名你推进的 PA 对话；回应你声称要检验的理论 |
| `jpart-theory-building` | 把论证打造成理论动作（扩展 / 检验 / 界定 / 推翻） |
| `jpart-research-design` | 为设计辩护——实验、因果观察、多层次、混合方法 |
| `jpart-data-analysis` | 分析规范；共同方法偏差与自选择；稳健性；可复现 |
| `jpart-tables-figures` | 自洽、可读、能展示机制与效应量的图表 |
| `jpart-writing-style` | OUP 作者—年份；理论先行的摘要；约 12,000 词上限（含参考文献） |
| `jpart-transparency-and-data` | 数据与代码公开；数据可得性声明；豁免情形 |
| `jpart-review-process` | 双向匿名、发展性评审；桌面筛查；决定类别 |
| `jpart-submission` | Editorial Express 投稿前检查（匿名化、字数、关键词、DOI、DAS） |
| `jpart-rebuttal` | 保护理论贡献的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — PA 数据源（FEVS / FedScope / ICMA / Form 990 / QoG）+ 调查/实验平台 + R / Stata / Python 包
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 OUP / JPART 官方 URL，未核实项标 待核实
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — JPART 风格引言的 before→after（虚构）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 经网络核实的真实 JPART 论文，按 PA 理论 × 方法编排
- [`resources/code/`](resources/code/) — 可复现的 Stata + Python 因果推断骨架

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑与任期、确切上限、费用/APC、政策措辞）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的问题是否构成公共管理理论贡献——那是研究者的判断

---

## 与兄弟期刊的差异

| 期刊 | 所有者 / 出版方 | 定位 | 不要投… |
|------|----------------|------|---------|
| **JPART** | PMRA / OUP | 公共管理 **理论** + 严谨经验研究 | 一个孤立的政策性发现 |
| PAR | ASPA / Wiley | 宽口径、整合、面向实务 | 只面向少数专家的窄理论检验 |
| JPAM | APPAM / Wiley | 政策分析与项目评估 | 纯粹的管理理论机制论文 |
| Governance | Wiley | 政府的比较制度研究 | 几乎无制度理论的美国机构行为机制 |

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Journal of Public Administration Research and Theory（牛津 Academic）](https://academic.oup.com/jpart) — 出版方主页
- [公共管理研究学会（PMRA）](https://www.pmranet.org/) — 所有者学会

---

## 许可

MIT
