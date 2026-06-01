# 美国政治学评论（APSR）技能包

<p align="center">
  <img src="assets/cover.svg" alt="American Political Science Review 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-APSR-14274e)](https://www.cambridge.org/core/journals/american-political-science-review)
[![Field](https://img.shields.io/badge/field-政治学-1f6feb)](https://apsanet.org/publications/journals/american-political-science-review/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《美国政治学评论》（American Political Science Review, APSR）** 投稿的 Agent 技能栈。APSR 是
**美国政治学会（APSA）的旗舰综合性期刊**，创刊于 **1906 年**，由 **剑桥大学出版社** 出版。它发表
**整个学科** 的顶尖研究：美国政治、比较政治、国际关系、政治理论、公共政策、政治学方法论——定量、定性、
形式化（博弈论）、实验、计算与诠释取向兼收并蓄。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把经济学包改个名字套用到政治学。
它是 **APSR 专属** 技能栈：一个对**整个政治学科都有普遍意义**的问题、一个能**跨越自身子领域**对话的论证、
一个能在各自方法论标准下站得住的研究设计、**双向匿名**的稿件准备，以及一份存入 **Harvard Dataverse 上
APSR Dataverse** 并经编辑部**实际复现验证**的可复现材料包。

---

## APSR 是什么，为何需要专属技能栈？

APSR 的约束不同于领域刊或方法刊：

| 约束 | APSR | 含义 |
|------|------|------|
| 范围 | **整个政治学科** | 论文必须超越自身子领域才有意义 |
| 看重 | **普遍意义** + 清晰的理论贡献 | 仅限子领域的窄结果不合适 |
| 方法 | 定量/定性/形式化/实验/诠释——各按其标准评判 | 不要把同一模板硬套到所有论文 |
| 出版方 / 所有者 | **剑桥大学出版社** / **APSA** | 通过 **Editorial Manager** 投稿 |
| 评审模式 | **双向匿名** | 稿件须匿名化，去除明显自我指认 |
| 费用 | 未列**投稿费**；无会员要求 | 不要预算投稿费 |
| 篇幅 | 多数**论文 < 11,000 词**；**研究札记 < 7,000**；**摘要 ≤ 150 词** | 首页须标字数 |
| 体例 | **APSA 政治学体例手册**（作者—年份） | 非泛用 Chicago；通讯作者须 ORCID |
| 透明度 | **可复现材料包存入 APSR Dataverse**，条件接受时验证 | 边做边建；编辑部会真的去跑 |
| 特色通道 | Registered Reports + 复现与再评估 + 综述（Syntheses） | 投稿前选对通道 |

易变的具体信息（编辑与任期、确切篇幅上限、费用/APC、政策措辞）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记 **待核实**。
**请以官方页面为准。**

### 五种发表通道

- **Regular Articles（常规论文）**——多数 **< 11,000 词**；学科主力研究形式。
- **Research Notes（研究札记）**——聚焦型贡献，**< 7,000 词**（确切上限见 待核实）。
- **Replications and Reappraisals（复现与再评估）**——复现、再现或重新评估既有发现。
- **Syntheses（综述/整合）**——整合某一文献或论争的整合性文章。
- **Registered Reports（注册报告）**——在**得到结果之前**先评审并接受第一阶段设计 + 分析计划。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/apsr-skills
/plugin install apsr-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/apsr-skills.git
cd apsr-skills

mkdir -p ~/.claude/skills && cp -R skills/apsr-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/apsr-* ~/.codex/skills/
```

### 第一条提示

```
用 apsr-workflow 告诉我，我的 APSR 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
apsr-topic-selection
        ▼
apsr-literature-positioning
        ▼
apsr-theory-building
        ▼
apsr-research-design
        ▼
apsr-data-analysis
        ▼
apsr-tables-figures
        ▼
apsr-writing-style          （润色）
        ▼
apsr-transparency-and-data-policy
        ▼
apsr-review-process
        ▼
apsr-submission
        ▼
apsr-rebuttal
```

`apsr-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。若设计是**前瞻性**的，尽早走
`apsr-review-process` 考虑 **Registered Reports** 通道；若是重新评估已发表发现，考虑
**Replications and Reappraisals** 通道。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `apsr-workflow` | 路由器——决定下一步调用哪个子技能 |
| `apsr-topic-selection` | 跨学科的普遍意义契合；选对通道 |
| `apsr-literature-positioning` | 跨越子领域对话；回应 APSR 读者期待的文献 |
| `apsr-theory-building` | 把论证（形式化/诠释/经验）打造成贡献 |
| `apsr-research-design` | 为设计辩护——因果推断、案例选择、实验、形式化 |
| `apsr-data-analysis` | 分析规范、不确定性、稳健性、多方法三角互证 |
| `apsr-tables-figures` | APSA 体例下可读、自洽的图表 |
| `apsr-writing-style` | APSA 体例手册；在字数上限内触达整个学科 |
| `apsr-transparency-and-data-policy` | APSR Dataverse 可复现材料包；定性透明度；豁免情形 |
| `apsr-review-process` | 双向匿名评审、桌面筛查、通道选择、决定类别 |
| `apsr-submission` | Editorial Manager 投稿前检查（匿名化、字数、ORCID、摘要） |
| `apsr-rebuttal` | 面向多位评审 + 编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 政治学数据源（ANES / CCES / V-Dem / CSES / COW / ACLED / Manifesto Project）+ R / Stata / Python 与定性/CAQDAS 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 APSA / 剑桥官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑与任期、确切上限、费用/APC、政策措辞）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的问题是否具有全学科的普遍意义——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [American Political Science Review（剑桥 Core）](https://www.cambridge.org/core/journals/american-political-science-review) — 出版方主页
- [APSA 上的 APSR](https://apsanet.org/publications/journals/american-political-science-review/) — 所有者、投稿指南、政策

---

## 许可

MIT
