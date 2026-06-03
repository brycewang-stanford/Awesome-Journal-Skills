# 《心智》（Mind）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Mind 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Mind-3a3f6b)](https://academic.oup.com/mind)
[![Field](https://img.shields.io/badge/field-哲学-1f6feb)](https://academic.oup.com/mind/pages/About)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《心智》（Mind）** 投稿的 Agent 技能栈。Mind 是 **分析哲学的顶尖期刊之一**，创刊于 **1876 年**，
由 **牛津大学出版社** 代表 **Mind 学会（Mind Association）** 出版。Mind **以质量为唯一发表标准**，
**不排除任何领域、任何风格、任何学派的哲学**——以 **认识论、形而上学、语言哲学、逻辑哲学、心灵哲学**
的前沿工作著称，同时也欢迎伦理学、哲学史、欧陆哲学与跨学科研究。

本仓库是**有主见的**。它**不是**通用人文写作工具箱，**更不是**把社会科学包改个名字套用到哲学。
**这里没有数据**——没有统计、没有数据集、没有经验意义上的档案。一篇 Mind 论文是一件**论证作品**：
一个**锋利的论点**、一个为之辩护的**有效且可靠的论证**、**预先设想并回应最强反驳**、**概念精确**、
**简约（parsimony）**，以及对广大哲学读者**可读**的文字。本技能栈的存在，就是把这个论证打磨到最好。

---

## Mind 是什么，为何需要专属技能栈？

Mind 的约束不同于经验类期刊，也不同于泛用写作指南：

| 约束 | Mind | 含义 |
|------|------|------|
| 学科 | **分析哲学**（各领域、各学派） | 作品作为**论证**被评判，而非数据分析 |
| 看重 | **有意义的论点 + 可靠的论证** | 综述或裸的直觉还不构成一篇论文 |
| 唯一标准 | **质量**——不排除任何领域、风格、学派 | 题材是否时髦无济于事；论证必须出色 |
| 出版方 / 所有者 | **牛津大学出版社** / **Mind 学会** | 通过 **ScholarOne** 投稿 |
| 评审模式 | **三向匿名（triple-anonymous）** | 编辑与审稿人均不知作者；须按匿名准备 |
| 准备门槛 | **未按匿名评审准备的稿件不会被阅读** | 去除自我指认的引用与致谢 |
| 篇幅 | 论文**约 8,000 词**；摘要**50–200 词**（刊出版） | 一个干净的论点胜过三个半成品 |
| 投稿限制 | **同一通讯作者每 12 个月仅可投一篇论文** | 选你最强的那一篇 |
| 评审稿格式 | **须加行号**；Word 或 PDF + 高清图片 | 上传前加行号（LaTeX `lineno` / Word） |
| 体例 | **MIND house style**（MIND Stylesheet），接受后采用 | 泛用 Chicago/APA 导出并非该体例 |
| 费用 | 未列**投稿费**；接受后有可选开放获取收费 | 不要预算投稿费 |

易变的具体信息（编辑与任期、确切上限、开放获取收费、体例细节、所收稿件类型）会变化——未直接核实项
在 [`resources/official-source-map.md`](resources/official-source-map.md) 中标记 **待核实**。
**请以官方页面为准。**

### Mind 发表的稿件类型

- **Articles（论文）**——原创、独立成立的论证，**约 8,000 词**；主力形式。
- **Discussions（讨论）**——针对某篇已发表论文的简短、精准回应。
- **Book reviews（书评）**——对学科近期著作的评价性综述。
- **Critical notices（评论性述评）**——对某书较长篇幅的回应，并发展作者**自己的**观点。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/mind-skills
/plugin install mind-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/mind-skills.git
cd mind-skills

mkdir -p ~/.claude/skills && cp -R skills/mind-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/mind-* ~/.codex/skills/
```

### 第一条提示

```
用 mind-workflow 告诉我，我的 Mind 论文下一步该用哪个技能。
```

---

## 默认工作流

```text
mind-topic-selection
        ▼
mind-literature-positioning
        ▼
mind-thesis-and-argument
        ▼
mind-objections-and-replies
        ▼
mind-conceptual-analysis-and-method
        ▼
mind-structure-and-exposition
        ▼
mind-writing-style          （润色）
        ▼
mind-citation-and-style
        ▼
mind-review-process
        ▼
mind-submission
        ▼
mind-revision-and-response
```

`mind-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。多数论文会在
**论点 ↔ 反驳 ↔ 概念分析** 之间往返数次，再进入行文：在 Mind，回应最强反驳本身就是贡献的很大一部分，
因此预期会反复打磨论证。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `mind-workflow` | 路由器——决定下一步调用哪个子技能 |
| `mind-topic-selection` | 是否有锋利、重要、可辩护的论点？选定稿件类型 |
| `mind-literature-positioning` | 进入一场活跃论争；针对目标观点的**最强版本** |
| `mind-thesis-and-argument` | 陈述论点；构建有效、可靠的论证（前提 → 结论） |
| `mind-objections-and-replies` | 预设最强反驳；反驳、让步并限定、或承担代价 |
| `mind-conceptual-analysis-and-method` | 精确概念、区分、思想实验、简约、方法选择 |
| `mind-structure-and-exposition` | 在约 8,000 词内编排，使论证清晰展开 |
| `mind-writing-style` | 面向广大读者的清晰文字；对技术内容作非形式化解说 |
| `mind-citation-and-style` | MIND house style / Stylesheet；行号；匿名化引用 |
| `mind-review-process` | 三向匿名评审、质量唯一标准、专家审稿、预期 |
| `mind-submission` | ScholarOne 投稿前检查（匿名化、字数/摘要上限、行号、规则） |
| `mind-revision-and-response` | 回应专家审稿意见而不稀释论点 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 哲学参考工具（SEP / IEP / PhilPapers / JSTOR）、逻辑与论证图工具、LaTeX `lineno`、MIND Stylesheet
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 OUP / Mind 官方 URL，未核实项标 待核实

---

## 本仓库不做什么

- 不替你写出可直接投稿的论文——更不替你做哲学
- 不模拟任何特定编辑或审稿人的口味
- 不把哲学当作经验科学：这里**没有数据、没有统计、没有档案**
- 不臆断易变元数据（现任编辑与任期、确切上限、开放获取收费、体例细节）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的论点是否重要、论证是否可靠——那是哲学家自己的工作

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Oxford Academic 上的 Mind](https://academic.oup.com/mind) — 出版方主页、各期、预印文章
- [Mind General Instructions](https://academic.oup.com/mind/pages/General_Instructions) — 作者指南、投稿、体例
- [Why submit to Mind](https://academic.oup.com/mind/pages/why-submit) — 三向匿名评审、质量唯一标准

---

## 许可

MIT
