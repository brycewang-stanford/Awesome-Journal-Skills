# 英国政治学杂志（BJPS）技能包

<p align="center">
  <img src="assets/cover.svg" alt="British Journal of Political Science 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-BJPS-6a2a2a)](https://www.cambridge.org/core/journals/british-journal-of-political-science)
[![Field](https://img.shields.io/badge/field-Political%20Science-1f6feb)](https://www.cambridge.org/core/journals/british-journal-of-political-science)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向投稿 **《英国政治学杂志》（British Journal of Political Science, BJPS / BJPolS）** 的智能体技能栈。BJPS
创刊于 **1971 年**，由 **剑桥大学出版社（Cambridge University Press）** 出版，是一份**综合性、面向国际**的领先
政治学期刊：其宗旨是覆盖**广泛国家与各专业领域**的研究进展，发表横跨整个学科的成果——比较政治、国际关系、政治
理论、政治行为与民意、政治经济学、政治方法论——并平等对待定量、定性、形式化、实验、计算与诠释性研究，同时欢迎
相关学科（社会学、社会心理学、经济学、哲学）的作品。

本仓库是有立场的。它**不是**通用的社会科学写作工具箱，也**不是**把经济学技能包套用到政治学上。它是一套
**BJPS 专属**技能栈：要求选题具有**广泛的政治学意义**、能超越单一子领域**且**超越单一国家个案，论证可迁移，研究
设计按其自身方法论标准被辩护，采用**双盲**评审准备，并在录用时向 **Harvard Dataverse 上的 BJPolS Dataverse**
提交**复制数据包**。

**官方依据核验于 2026-06**（检索于 2026-06；以官网为准）——每条事实的来源 URL 及对未核实条目的 `待核实` 标记
见 [`resources/official-source-map.md`](resources/official-source-map.md)。

---

## 什么是 BJPS，为何需要专属技能栈？

BJPS 的约束不同于美国旗舰刊、比较政治专刊或方法刊：

| 约束维度        | BJPS                                                              | 含义                                                  |
|-----------------|-------------------------------------------------------------------|-------------------------------------------------------|
| 范围            | **全学科**、**面向国际**                                          | 论文须同时超越单一子领域与单一国家                    |
| 看重            | **广泛意义** + 清晰、可迁移的贡献                                 | 狭窄的、单一个案框架的结果不合适                      |
| 方法            | 定量、定性、形式化、实验、诠释——各按其自身标准评判               | 不要把单一模板强加于所有论文                          |
| 出版方 / 所有方 | **剑桥大学出版社**（与英国学术院相关联）                          | 通过期刊在线系统投稿，而非美国系统                    |
| 评审模式        | **双盲**，通常 ≥ 2 名审稿人                                       | 匿名化稿件；移除资助致谢与自引                        |
| 费用            | 未列明投稿费；**Comments 不收文章处理费（APC）**                  | 不要预算投稿费；任何 OA APC 请核实                    |
| 篇幅            | 研究论文 **约 10,000 词**；Letters **约 4,000**；摘要 **≤ 150**（待核实） | 提前选定正确的稿件类型                          |
| 格式            | **剑桥社内格式——哈佛作者-年份制**                                | 非 Chicago/APSA；接受 MS Word 或 LaTeX               |
| 透明度          | **DA-RT 签署方**；录用时向 **BJPolS Dataverse** 提交数据与代码    | 边做边搭建复制包                                      |
| 特色类型        | 研究论文 + Letters（短文）+ Comments                              | Letter 是完整的短论文，而非删减版长文                |

易变细节（编辑及任期、确切字数上限、费用/APC、门户 URL、政策措辞）会变动——未直接核实的条目在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标为 **待核实**。**请以官网为准。**

### 三种发表类型

- **研究论文（Research Articles）** —— 学科主要研究形式，**约 10,000 词**（待核实）。
- **Letters** —— 聚焦、完整的短篇贡献，**约 4,000 词**（待核实）。
- **Comments** —— 针对某篇已发表 BJPS 论文的批评、更正或再评估（不收 APC）。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/british-journal-of-political-science-skills
/plugin install british-journal-of-political-science-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/british-journal-of-political-science-skills.git
cd british-journal-of-political-science-skills

mkdir -p ~/.claude/skills && cp -R skills/bjps-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/bjps-* ~/.codex/skills/
```

### 第一条提示

```
使用 bjps-workflow 告诉我，我的 BJPS 稿件下一步应该用哪个技能。
```

---

## 默认工作流

```text
bjps-topic-selection
        ▼
bjps-literature-positioning
        ▼
bjps-theory-building
        ▼
bjps-research-design
        ▼
bjps-data-analysis
        ▼
bjps-tables-figures
        ▼
bjps-writing-style          （润色）
        ▼
bjps-transparency-and-data
        ▼
bjps-review-process
        ▼
bjps-submission
        ▼
bjps-rebuttal
```

`bjps-workflow` 是路由器——根据你所处的阶段告诉你下一步用哪个技能。若贡献是聚焦的单一结果，考虑 **Letter**
类型；若是对已发表 BJPS 结论的批评，考虑 **Comment**。

---

## 技能列表

| 技能                           | 用途                                                              |
|--------------------------------|-------------------------------------------------------------------|
| `bjps-workflow`                | 路由器——决定下一步调用哪个子技能                                  |
| `bjps-topic-selection`         | 跨子领域、跨国家的广泛意义契合度；选定正确的稿件类型              |
| `bjps-literature-positioning`  | 参与 BJPS 读者期待的跨子领域、跨国家学术对话                      |
| `bjps-theory-building`         | 将论证（形式化、诠释或经验）打造成可迁移的贡献                    |
| `bjps-research-design`         | 辩护研究设计——因果推断、个案选择、实验、形式化                    |
| `bjps-data-analysis`           | 分析规范、不确定性、稳健性、跨国测量等价性                        |
| `bjps-tables-figures`          | 自洽、可读、符合剑桥尺寸限制的图表                                |
| `bjps-writing-style`           | 剑桥哈佛作者-年份制；在字数上限内触达广泛读者                     |
| `bjps-transparency-and-data`   | BJPolS Dataverse 复制包；DA-RT；定性透明度；豁免路径              |
| `bjps-review-process`          | 双盲评审、初筛、审稿人数、决定类别                                |
| `bjps-submission`              | 投稿前检查（匿名化、字数、ORCID、摘要）                           |
| `bjps-rebuttal`                | 面向多审稿人 + 编辑的 R&R 回复信策略                              |

### 资源

- [`resources/code/`](resources/code/) —— 可复现的 Stata + Python 因果推断骨架（DiD / IV / RDD / DML / 机制 / 稳健性 / 表格），随包自含
- [`resources/external_tools.md`](resources/external_tools.md) —— 政治学数据源（V-Dem / CSES / ESS / WVS / COW / ACLED / Manifesto Project / KOF）+ R / Stata / Python 与定性/CAQDAS 工具
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— BJPS 风格引言的改写前后对照（虚构示例）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 按子领域 × 方法整理的、经核实的真实 BJPS 论文，附姊妹刊防误标清单
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的剑桥 / BJPS 官方 URL，未核实项标 待核实

---

## 与姊妹期刊的区别

| 期刊 | 所有方 / 出版方 | 相对 BJPS 的定位 |
|------|-----------------|------------------|
| **BJPS** | 剑桥大学出版社 | 综合性、**面向国际**的政治学期刊；看重跨国家、跨子领域的广泛意义 |
| **APSR** | APSA / 剑桥大学出版社 | 美国全学科旗舰；双匿名；APSA 格式；APSR Dataverse——美国综合性姊妹刊 |
| **AJPS** | 中西部政治学会 / Wiley | 美国综合性旗舰，经验/定量声誉强；非剑桥社 |
| **比较政治研究（CPS）** | SAGE | 比较政治**专刊**，非全学科综合刊 |
| **World Politics** | 剑桥大学出版社 / 普林斯顿 | 比较政治 + 国际关系专刊，看重理论；范围窄于 BJPS 的全学科定位 |

切勿在这些刊物间误标名篇——见 [`resources/exemplars/library.md`](resources/exemplars/library.md) 中的排除清单。

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或审稿人的口味
- 不断言易变元数据（现任编辑及任期、确切字数上限、费用/APC、门户、政策措辞）——请以官网为准；未核实项标 待核实
- 不替你判断你的问题是否具有广泛学科意义——这是研究者自己的判断

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属技能包索引
- [British Journal of Political Science（Cambridge Core）](https://www.cambridge.org/core/journals/british-journal-of-political-science) —— 出版方主页、投稿指南、政策
- [BJPolS Dataverse（Harvard Dataverse）](https://dataverse.harvard.edu/dataverse/BJPolS) —— 复制材料库

---

## 许可证

MIT
