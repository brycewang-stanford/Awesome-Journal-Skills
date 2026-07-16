# 《人文地理学进展》（Progress in Human Geography）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Progress in Human Geography 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Progress%20in%20Human%20Geography-29405c)](https://journals.sagepub.com/home/phg)
[![Field](https://img.shields.io/badge/field-Human%20Geography-1f6feb)](https://journals.sagepub.com/home/phg)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《人文地理学进展》（Progress in Human Geography，简称 PiHG）** 投稿的智能体技能包。该刊是人文地理
学科的**首要综述与理论期刊**，创刊于 **1977 年**（原由 Edward Arnold 出版），现由 **SAGE** 出版。PiHG
**不发表**原创实证研究：它发表**具有议程设定意义的批判性综述文章**、由编辑约稿的**进展报告（Progress
Report）**、年度 **PiHG 讲座（PiHG Lecture）**，以及涵盖经济、政治、社会、文化、城市、女性主义乃至
后人类（more-than-human）地理等方向的短篇论辩。评审采用经 **SAGE Track** 的**双向匿名**方式。

本仓库立场鲜明：它**不是**通用写作工具箱，也**不是**把实证论文包套用到综述期刊。它是**针对 PiHG 的
专用技能栈**，为**综述文章这一体裁**打造：贡献须是**真正的综合**（而非新数据或单一案例）、须**驾驭
庞大且充满争议的文献**、须具备**批判理论的成熟度**、**概念清晰**，并提出一个**面向未来的干预**，为学科
指明下一步方向。如果你的稿件核心是一份数据与一项发现，那么这是错误的期刊——也是错误的技能包。

---

## PiHG 是什么？为何需要专用技能栈？

PiHG 的约束与实证人文地理期刊截然不同：

| 约束维度       | Progress in Human Geography                                                | 含义                                                   |
|----------------|---------------------------------------------------------------------------|--------------------------------------------------------|
| 发表什么       | **批判性综述、理论与议程文章**——而非实证结果                              | “有发现的研究”属于错位投稿；须以论证而非数据开篇       |
| 看重           | **综合且面向未来的贡献**，能重新整理某片文献                              | 仅作总结不够；须论证并作出干预                         |
| 特色体裁       | **综述文章**、约稿的**进展报告**、**PiHG 讲座**                            | 须清楚你在写哪种体裁；进展报告为约稿                   |
| 出版方 / 所有者 | **SAGE**（1977 年起；原为 Edward Arnold）                                  | 经 **SAGE Track**（基于 ScholarOne）投稿              |
| 评审模式       | **双向匿名**同行评审                                                       | 匿名化正文并中和自引                                   |
| 篇幅           | 综述文章 **4,000–8,000 词**，含尾注、**不含参考文献**                     | 论证须紧凑；对综述而言字数上限偏短                     |
| 摘要与关键词   | **非结构化摘要约 100 词**；**至少 5 个关键词**                             | 100 词内须点明干预，而非仅陈述主题                     |
| 文体           | **SAGE Harvard** 作者–年份制引用                                           | 非芝加哥体例；全文保持一致的 Harvard 格式             |
| 图表           | **概念性**表格/图示（类型学、框架图）——极少数据图                        | 图表承担综合工作，而非报告结果                         |
| 伦理           | **COPE** 成员；ORCID；SAGE 科研诚信与 AI 使用政策                          | 按政策披露；必要时声明立场性（positionality）         |

易变信息（现任编辑、确切字数与摘要长度、费用/开放获取选项、政策措辞）会变化——未直接核实的条目在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记为 **待核实**。
**官方信息核对于 2026-07-16。请以官网为准。**

### 核心检验（先于一切）

**PiHG 奖励的是数据无法给出的贡献。** 若读者问“你发现了什么？”，说明你投错了期刊；若读者问“学科此后
该如何思考此问题、下一步该做什么？”，你就来对了地方——本技能栈余下部分帮你把这一论证做扎实。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/phg-skills
/plugin install phg-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/phg-skills.git
cd phg-skills

mkdir -p ~/.claude/skills && cp -R skills/phg-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/phg-* ~/.codex/skills/
```

### 第一条提示词

```
使用 phg-workflow 告诉我，我的 Progress in Human Geography 综述文章下一步该用哪个技能。
```

---

## 默认工作流

```text
phg-topic-selection
        ▼
phg-theory-building
        ▼
phg-literature-positioning
        ▼
phg-argument-synthesis
        ▼
phg-critical-intervention
        ▼
phg-contribution-framing
        ▼
phg-tables-figures
        ▼
phg-writing-style          （打磨）
        ▼
phg-submission
        ▼
phg-review-process
        ▼
phg-rebuttal
```

`phg-workflow` 是路由器——它根据你所处阶段，以及你写的是独立的**综述文章**还是约稿的**进展报告**，
告诉你下一步用哪个技能。多数文章在进入 writing-style 之前会在 理论 ↔ 综合 ↔ 干预 之间往返多次。

---

## 技能清单

| 技能                           | 用途                                                                          |
|--------------------------------|-------------------------------------------------------------------------------|
| `phg-workflow`                 | 路由器——决定下一步调用哪个子技能；选定综述文章 vs. 进展报告                   |
| `phg-topic-selection`          | 主题是否*值得综述*？须是有争议、有分量的活跃文献，而非补缺式研究              |
| `phg-theory-building`          | 构建组织综述并承载论证的概念装置                                              |
| `phg-literature-positioning`   | 梳理并进入庞大且有争议的文献；界定语料及其论辩                                |
| `phg-argument-synthesis`       | 把众多来源汇成一个累积性论证——综合，而非逐条罗列                            |
| `phg-critical-intervention`    | 作出批判性动作：指出学科所缺，并重排论辩格局                                  |
| `phg-contribution-framing`     | 框定可迁移、面向未来的议程——面向学科的“那又如何/下一步”                     |
| `phg-tables-figures`           | 概念性图表：类型学、框架图、综合表（而非数据图）                              |
| `phg-writing-style`            | PiHG 文风；SAGE Harvard；8,000 词含尾注上限；约 100 词摘要；5+ 关键词         |
| `phg-submission`               | SAGE Track 投稿前检查（体裁、匿名化、篇幅、摘要、关键词、ORCID）              |
| `phg-review-process`           | 双向匿名评审；决定类别；综述稿的初审退稿触发点                                |
| `phg-rebuttal`                 | 面向编辑与审稿人的修回回复，强化干预                                          |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 系统综述与文献计量工具（Zotero、Scopus/Web of Science、VOSviewer/CiteSpace、PRISMA、用于定性综合的 CAQDAS）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的 SAGE / PiHG 官方链接，未核实项标 待核实
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 用于对标综述文体的人文地理经典理论家与综述/理论著作，附体裁防混淆清单
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— PiHG 综述文章引言前后对照（示范用）

---

## 与姊妹期刊的区别

| 期刊 | 定位 | 何时改用本技能包 |
|------|------|------------------|
| **Progress in Human Geography** | 学科**综述/理论旗舰**；议程设定文章 | ……你写的是综合、面向未来的综述，而非报告数据 |
| *Annals of the AAG* / *Transactions of the IBG* | 综合**实证**旗舰 | ……你的核心是关于某片文献的论证，而非一项研究 |
| *Environment and Planning A/D* | 重理论的**实证**与概念论文 | ……你在梳理并重排某个领域，而非推进单一案例 |
| *Geoforum* / *Antipode* | 批判性**实证**与理论干预 | ……贡献是带议程的最新研究综述 |
| *Progress in Physical Geography* | 自然地理姊妹综述刊 | ……你的领域是人文地理 |

---

## 本仓库不做什么

- 不替你写出可直接投稿的综述文章
- 不模拟任何特定编辑或审稿人的口味
- 不断言易变元数据（现任编辑、确切字数上限、费用/开放获取、政策措辞）——请以官网为准；未核实项标 待核实
- 不替你判定主题是否值得综述、你的干预是否真正新颖——这是研究者的判断

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Progress in Human Geography（SAGE Journals）](https://journals.sagepub.com/home/phg) —— 期刊主页
- [PiHG 投稿指南](https://journals.sagepub.com/author-instructions/phg) —— 作者须知

---

## 许可证

MIT
