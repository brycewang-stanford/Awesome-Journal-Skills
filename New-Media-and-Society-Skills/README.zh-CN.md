# New Media & Society 技能包

<p align="center">
  <img src="assets/cover.svg" alt="New Media & Society 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-NM%26S-2a2a6a)](https://journals.sagepub.com/home/nms)
[![Field](https://img.shields.io/badge/field-Digital%20Media%20%26%20Society-1f6feb)](https://journals.sagepub.com/home/nms)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **New Media & Society（NM&S，《新媒体与社会》）** 投稿的智能体技能栈。NM&S 是一份关于数字媒体、
互联网与社会的领先 **跨学科** 期刊，由 **SAGE** 出版，创刊于 **1999 年**。其议题包括：平台与数据化
（datafication）、数字不平等与数字鸿沟、社交媒体与在线社群、日常生活中的算法与人工智能、数字劳动、
隐私与监控，以及新媒体在社会、政治、文化层面的相互塑造。它在方法上 **多元而国际化**：质性访谈与数字
民族志、批判与理论研究、内容与话语分析、计算方法以及混合方法都在其版面之内。

本仓库是 **有立场** 的：它不是泛用的社会科学写作工具箱，也不是把定量传播学技能包改个名字。它是
**NM&S 专属** 技能栈——强调面向数字媒体与社会的 **广泛意义**、强调可迁移的概念而非单一平台报告、按各
自方法论标准为研究设计辩护、重视 **在线与平台数据的研究伦理**、在 **约 8000 词** 的目标内提交 **匿名
化（masked）** 稿件，并通过 **Sage Track**、在 **严格匿名（双向匿名）** 评审下投稿。

---

## NM&S 是什么，为何需要专属技能栈？

NM&S 的约束不同于单一学科期刊或定量传播学期刊：

| 约束       | NM&S                                                                  | 含义                                                       |
|------------|----------------------------------------------------------------------|------------------------------------------------------------|
| 范围       | **数字媒体、互联网与社会——跨学科**                                    | 文章须超越单一平台、单一学科                                |
| 看重       | 可迁移的概念/机制 + 跨学科意义                                        | 没有可迁移想法的平台案例研究不对路                          |
| 方法       | 质性、批判/理论、内容/话语、计算、混合——各按自身标准评判              | 不要把回归模板硬套到阐释性研究上                            |
| 出版方     | **SAGE**（ISSN 1461-4448 / 1461-7315）                                | 经 **Sage Track** 投稿，`mc.manuscriptcentral.com/nms` |
| 评审模式   | **匿名化投稿工作流**——匿名稿件 + 单独标题页                           | 以 SAGE 详细匿名化说明准备文件                              |
| 篇幅       | **约 8000 词目标**——*含正文、注释、参考文献、表格与图表的全部文字*    | 参考文献与表格计入；超出数百词可能不予送审                  |
| 摘要       | **150 词**，非结构化；**关键词 ≥ 4 个**                               | 简明陈述目的、方法与发现                                    |
| 引用体例   | **SAGE Harvard**（著者—出版年）                                       | 特定的稿件引用格式                                          |
| 伦理与数据 | **SAGE/COPE** 伦理 + 数据可得性声明；**在线/平台数据伦理**            | 知情同意、匿名化、抓取与服务条款很重要                      |

> **官方依据核验于 2026-06-20** —— 事实锚定于 SAGE 的 NM&S 作者指南、期刊主页与编辑委员会页面。
> Sage Track 实时提示、主编换届细节和可选开放获取费用会变化，上传或接收后付款前请复核官网。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/new-media-and-society-skills
/plugin install new-media-and-society-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/new-media-and-society-skills.git
cd new-media-and-society-skills

mkdir -p ~/.claude/skills && cp -R skills/newms-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/newms-* ~/.codex/skills/
```

### 第一条提示词

```
使用 newms-workflow 告诉我，针对我的 New Media & Society 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
newms-topic-selection
        ▼
newms-literature-positioning
        ▼
newms-theory-building
        ▼
newms-research-design
        ▼
newms-data-analysis
        ▼
newms-tables-figures
        ▼
newms-writing-style          （打磨）
        ▼
newms-transparency-and-data
        ▼
newms-review-process
        ▼
newms-submission
        ▼
newms-rebuttal
```

`newms-workflow` 是路由器——它根据你所处的阶段告诉你下一步用哪个技能。

---

## 技能清单

| 技能                           | 用途                                                                       |
|--------------------------------|----------------------------------------------------------------------------|
| `newms-workflow`               | 路由器——决定下一步调用哪个子技能                                            |
| `newms-topic-selection`        | 跨学科契合度；要可迁移的概念，而非平台报告                                  |
| `newms-literature-positioning` | 交织两条以上文献；把空白写成一处分歧                                        |
| `newms-theory-building`        | 借助媒介与社会理论，构建可迁移的概念/机制                                   |
| `newms-research-design`        | 为设计辩护——访谈/民族志、内容/话语、计算、混合                              |
| `newms-data-analysis`          | 按方法的推断、信度、验证与分析透明度                                        |
| `newms-tables-figures`         | 清晰、自足、已匿名的图表（计入字数目标）                                    |
| `newms-writing-style`          | 在约 8000 词内触达全学科；SAGE Harvard；前置贡献                            |
| `newms-transparency-and-data`  | 在线/平台数据伦理、知情同意、匿名化、抓取/服务条款、数据共享                |
| `newms-review-process`         | 匿名评审、跨学科审稿人看重什么、决定类别                                    |
| `newms-submission`             | Sage Track 投稿前检查（约 8000 词、匿名化、摘要、关键词、伦理）             |
| `newms-rebuttal`               | 面向相互冲突的跨学科审稿人的修回信策略                                      |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 数字媒体数据源 + R / Python / CAQDAS / 内容分析 / 计算工具（按方法）
- [`resources/official-source-map.md`](resources/official-source-map.md) — 本技能包每条事实背后的官方 SAGE / NM&S 链接与实时复核守则
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 一篇 NM&S 引言的 改前→改后（虚构，房屋风格）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 经网络核实的真实 NM&S 论文，按方法 × 主题排列，并附姊妹刊防混淆提示

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定主编或审稿人的口味（注意 2026 年主编换届）
- 不把易变元数据写死为永久规则；Sage Track 提示、主编变更和可选开放获取费用须以官网为准
- 不替你判断选题是否具有广泛的跨学科意义——这是研究者自己的判断

---

## 与姊妹期刊的区别

| 期刊 | 重心 | 何时改投它 |
|------|------|-----------|
| **New Media & Society** | **广义的跨学科数字媒体与社会**，方法多元 | 概念雄心强、跨多学科 |
| Journal of Communication / Communication Research | 定量的美国传播科学 | 用定量方法估计某传播学效应 |
| Information, Communication & Society | 信息、ICT 与政策机制 | 仅关注 ICT/信息社会机制 |
| Social Media + Society | 特定社交媒体平台的实证研究 | 一项难以超越单一平台的平台研究 |

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [New Media & Society（SAGE）](https://journals.sagepub.com/home/nms) — 出版方主页
- [NM&S 投稿指南](https://journals.sagepub.com/author-instructions/nms) — 作者须知（可能屏蔽自动化抓取）

---

## 许可

MIT
