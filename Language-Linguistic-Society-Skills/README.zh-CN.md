# 《Language》（美国语言学会）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Language（LSA）封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Language-4a2545)](https://www.cambridge.org/core/journals/language)
[![Field](https://img.shields.io/badge/field-语言学-1f6feb)](https://www.linguisticsociety.org/publications/language)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《Language》** 投稿的 Agent 技能栈。《Language》是 **美国语言学会（Linguistic Society of America,
LSA）** 的旗舰刊，**1925 年** 起连续出版，并自 **2026 年 1 月** 起由 **剑桥大学出版社（Cambridge
University Press）** 出版（自第 102 卷起 **完全开放获取**）。它是 **综合性** 期刊，覆盖各个分支——音系学、
语音学、句法学、语义学、形态学、历史与类型语言学、社会语言学、心理语言学与计算语言学——按各自传统的标准评审每类
工作，但对所有稿件都提出同一要求：**由严谨、可核查的语言学证据支撑的、有理论根基的论断**，且要让整个学科（而非
某一框架的圈内人）都读得懂。

本仓库是**有主见的**。它**不是**通用语言学写作工具箱，**也不是**把某个分支刊（如 *NLLT*、*Phonology*、
*Journal of Semantics*、*Language Variation and Change*）改名。《Language》的门槛是**读者面广 + 分析深**：
评审来自各分支、采用 **双盲（double-anonymous）** 评审；数据以 **带编号、按莱比锡规则（Leipzig）逐词注释的
例句** 呈现；参考文献遵循 **Language / Unified Style Sheet**（**不是** APA 或 Chicago）；定量论断需建立在
**恰当设定的模型**（R 的混合效应模型）与共享数据之上。

---

## 《Language》是什么，为何需要专属技能栈？

《Language》的约束不同于分支刊，也不同于通用刊：

| 约束 | Language（LSA） | 含义 |
|------|----------------|------|
| 所有者 / 出版方 | **LSA** / **剑桥大学出版社**（2026 年 1 月起；此前为 Project MUSE / JHU Press） | 通过 **CUP ScholarOne** 投稿；提供 Overleaf 模板 |
| 获取方式 | 自第 102 卷（2026）起 **完全开放获取** | 核对 APC / 豁免 / read-and-publish 条款 |
| 看重 | 面向综合读者的 **有理论根基的分析** | 描述性数据堆砌不合适（会被退稿） |
| 框架立场 | **跨框架对话** | 单一形式主义的圈地会被扣分 |
| 覆盖面 | 各分支，各按其标准 | 不要把同一模板硬套所有论文 |
| 评审模式 | **双盲** | 稿件匿名化；改写自引以防暴露身份 |
| 篇幅 | **General Research Article ≤ 18,000 词**（含注释/图表/附录，不含参考文献）；**超过 12,000 词** 从严评审 | 容忍长文但不鼓励；每页都要值得 |
| 例句 | **带编号、莱比锡注释**；**IPA** 用 Unicode 字体 | 注释错位、伪造 IPA 是常见错误 |
| 体例 | **Language / Unified Style Sheet**（作者-年份） | **不是** APA 或 Chicago |
| 数据 | 有文档、可复现；对发音人/社区合乎伦理 | 在合乎伦理的范围内共享；不夸大强制要求 |

易变信息（词数/摘要上限、可接受格式、开放获取条款、现任编辑名单、数据政策）在 2026 年更换出版方后仍在调整。
[`resources/official-source-map.md`](resources/official-source-map.md) 为每条事实标出 LSA、剑桥大学出版社或
体例表的官方来源；投稿前请在浏览器中即时核对这些操作性细节。

### 栏目一览

- **General Research Article**——深入、面向综合读者、推进语言学理论（≤18,000 词）。
- **Research Report**——更小、更聚焦的贡献。
- **Review Article**——领域综述（≤5,000 词）。
- **Discussion Notes**、**书评 / Book Notices**。
- **仅线上栏目（2013 年起）：** **Perspectives**（靶子文章 + 评论 + 作者 Rejoinder）、
  **Phonological Analysis**、**Language and Public Policy**、**Teaching Linguistics**。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/lang-skills
/plugin install lang-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/lang-skills.git
cd lang-skills

mkdir -p ~/.claude/skills && cp -R skills/lang-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/lang-* ~/.codex/skills/
```

### 第一条提示

```
用 lang-workflow 告诉我，我的 Language 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
lang-topic-selection
        ▼
lang-theory-building
        ▼
lang-literature-positioning
        ▼
lang-research-design
        ▼
lang-data-analysis
        ▼
lang-data-and-transparency
        ▼
lang-tables-figures
        ▼
lang-writing-style          （润色）
        ▼
lang-submission
        ▼
lang-review-process
        ▼
lang-rebuttal
```

`lang-workflow` 是路由器——根据你所处阶段，以及稿件属于 **General Research Article**、**Research Report**、
**Review Article**、**Discussion Note** 还是 **Perspectives** 靶子文章，告诉你下一步用哪个技能。
《Language》论文通常在 writing-style 前多次循环 理论 ↔ 数据 ↔ 分析；解释模式的分析往往到后期才清晰。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `lang-workflow` | 路由器——决定下一步调用哪个子技能 |
| `lang-topic-selection` | 契合：跨分支可读、有理论根基的论断，而非描述 |
| `lang-theory-building` | 把模式提升为带明确预测、能裁决框架之争的分析 |
| `lang-literature-positioning` | 把贡献定位到活跃论争；公正地与对立框架对话 |
| `lang-research-design` | 按分支为设计辩护（田野、语料库、语音、类型学、计算） |
| `lang-data-analysis` | 分析规范；混合效应建模；效应量；避免伪重复 |
| `lang-data-and-transparency` | 有文档、可复现的数据；标注来源的例句；发音人/社区伦理 |
| `lang-tables-figures` | 编号例句、莱比锡注释、IPA、树形图/tableau、图 alt text |
| `lang-writing-style` | 面向综合读者的文风；Language / Unified Style Sheet；前置论断 |
| `lang-submission` | ScholarOne 投稿前检查——匿名化、词数、注释、体例、开放获取 |
| `lang-review-process` | 双盲评审；退稿筛查；决定类别 |
| `lang-rebuttal` | R&R 回应信 + Perspectives 作者 Rejoinder |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 语言学工具栈（Praat、ELAN/FLEx、Montreal Forced Aligner、R/`lme4`/`brms`、CHILDES/BNC/Buckeye 等语料库、IPA/莱比锡注释工具、语料档案库、OSF）
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 LSA / CUP / 体例表官方 URL 与 live-check 提示
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 各分支的知名《Language》论文，附姊妹刊防误引提示
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 一篇带批注的《Language》式引言（before → after）

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不在缺少当前官方来源路径时臆断易变元数据（词数/摘要上限、可接受格式、开放获取条款、现任编辑、数据政策）；投稿前请以官方页面即时核对
- 不替你判断你的工作是否对《Language》足够有理论根基——那是语言学家的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Language（LSA）](https://www.linguisticsociety.org/publications/language) — 美国语言学会的旗舰刊
- [Language on Cambridge Core](https://www.cambridge.org/core/journals/language) — 出版方主页、作者说明、当前期号

---

## 许可

MIT
