# 人格与社会心理学杂志（JPSP）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Personality and Social Psychology 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JPSP-3b2c6e)](https://www.apa.org/pubs/journals/psp)
[![Field](https://img.shields.io/badge/field-心理学-1f6feb)](https://www.apa.org/pubs/journals/psp)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《人格与社会心理学杂志》（Journal of Personality and Social Psychology, JPSP）** 投稿的 Agent
技能栈。JPSP 是 **美国心理学会（APA）在人格与社会心理学领域的旗舰长文期刊**，创刊于 **1965 年**。
它**不是**短报告期刊：发表 **理论驱动、多研究** 的论文，并分为 **三个独立编辑的 section**，各有
自己的编辑与投稿入口。

本仓库是**有主见的**。它**不是**通用心理学写作工具箱，**也不是**把《心理科学》(Psychological Science)
包改名——两刊在格式上**截然相反**。它是 **JPSP 专属** 技能栈：先选对 **section**，再构建一个连贯的
多研究组合，配合 **JARS** 报告、**APA 第 7 版** 体例、**TOP Level 2** 透明度、**masked** 评审，
以及 **分 section** 的篇幅与研究数约束。

---

## JPSP 是什么，为何需要专属技能栈？

JPSP 的约束与短报告刊截然不同：

| 约束 | JPSP | 含义 |
|------|------|------|
| 出版方 | **美国心理学会（APA）** | 通过 APA **Editorial Manager** **分 section** 投稿 |
| 结构 | **三个 section**，分别编辑 | 一切之前先选 **ASC / IRGP / PPID** |
| 格式 | **长文、多研究** 的理论论文 | 单个小研究通常不合适；要构建组合 |
| 评审模式 | **masked** 评审（双向） | 稿件须匿名化 |
| 摘要 | **≤ 250 词** | 比很多刊的 150 词上限更长 |
| 分 section 篇幅 | ASC 引言+讨论 **≤ 3,500 词**；IRGP **≤ 5,000 词且正文 ≤ 5 个研究**；PPID "尽量精炼" | 各 section 规则不同——核对你的 |
| 体例 / 报告 | **APA 第 7 版** + **JARS**（期刊文章报告标准） | 结构化、标准化报告 |
| 透明度 | **TOP 指南 Level 2**（要求）；数据/代码/材料 + 预注册披露 | 披露并存入可信仓库 |
| Registered Reports | **接受发表**；**不提供** 开放科学徽章 | 用格式，而非徽章 |
| 费用 | 未列 **投稿费** | 核对任何开放获取 APC |

**三个 section**：

- **ASC** — *Attitudes and Social Cognition*（态度与社会认知）
- **IRGP** — *Interpersonal Relations and Group Processes*（人际关系与群体过程）
- **PPID** — *Personality Processes and Individual Differences*（人格过程与个体差异）

每个 section 有自己的编辑与 Editorial Manager 入口。易变信息（section 编辑与任期、确切的分 section
篇幅/研究数规则、费用/APC、政策措辞）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标 **待核实**。
**请以你所投 section 的 APA 官方页面为准。**

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jpsp-skills
/plugin install jpsp-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/jpsp-skills.git
cd jpsp-skills

mkdir -p ~/.claude/skills && cp -R skills/jpsp-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jpsp-* ~/.codex/skills/
```

### 第一条提示

```
用 jpsp-workflow 告诉我，我的 JPSP 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
jpsp-topic-selection          （先选 ASC / IRGP / PPID）
        ▼
jpsp-literature-positioning
        ▼
jpsp-theory-and-hypotheses
        ▼
jpsp-study-design             （多研究组合；功效；预注册）
        ▼
jpsp-data-analysis            （JARS；效应量；internal meta-analysis）
        ▼
jpsp-tables-figures
        ▼
jpsp-writing-style            （长文 APA 第 7 版润色）
        ▼
jpsp-open-science-and-transparency
        ▼
jpsp-review-process
        ▼
jpsp-submission
        ▼
jpsp-rebuttal
```

`jpsp-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。第一个真正的决定是论文属于
**哪个 section**，因为篇幅规则、编辑与评审流程都由它决定。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `jpsp-workflow` | 路由器——决定下一步调用哪个子技能 |
| `jpsp-topic-selection` | 选择 ASC / IRGP / PPID 并判断 JPSP 契合度 |
| `jpsp-literature-positioning` | 在人格/社会心理学文献中定位论文 |
| `jpsp-theory-and-hypotheses` | 构建理论与假设架构 |
| `jpsp-study-design` | 设计连贯的多研究组合（功效、预注册） |
| `jpsp-data-analysis` | 分析各研究、稳健性、internal meta-analysis；JARS 报告 |
| `jpsp-tables-figures` | APA 第 7 版 / JARS 规范的图表 |
| `jpsp-writing-style` | 长文 APA 第 7 版文风；≤ 250 词摘要；分 section 篇幅规则 |
| `jpsp-open-science-and-transparency` | TOP Level 2：仓库、数据/材料、预注册、JARS |
| `jpsp-review-process` | masked、分 section 的评审与决定 |
| `jpsp-submission` | 分 section 的 Editorial Manager 投稿前检查 |
| `jpsp-rebuttal` | 面向多位评审 + section 编辑的 R&R / accept-with-revision 回应 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 心理学研究设计、分析、meta-analysis、预注册、仓库与 APA 体例工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 APA / JARS / TOP 与分 section 官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（section 编辑与任期、确切篇幅/研究数规则、费用/APC、政策措辞）——请以 APA 官方页面为准；未核实项标 待核实
- 不替你判断论文属于哪个 section、或多研究组合是否足够强——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Journal of Personality and Social Psychology（APA）](https://www.apa.org/pubs/journals/psp) — 所有者、section、投稿指南
- [APA JARS](https://apastyle.apa.org/jars) · [TOP 指南](https://www.cos.io/initiatives/top-guidelines) — 报告标准与透明度

---

## 许可

MIT
