# 欧洲社会学评论（ESR）技能包

<p align="center">
  <img src="assets/cover.svg" alt="European Sociological Review 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ESR-1f5a66)](https://academic.oup.com/esr)
[![Field](https://img.shields.io/badge/field-定量社会学-1f6feb)](https://ecsrnet.eu/european-sociological-review-esr/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《欧洲社会学评论》（European Sociological Review, ESR）** 投稿的 Agent 技能栈。ESR 是
**欧洲社会学研究联盟（ECSR）的旗舰定量社会学期刊**，由 **牛津大学出版社（OUP）** 出版。它发表严谨的
比较与纵向定量研究：社会分层与流动、教育、劳动力市场、家庭与生命历程、移民与族群、态度，以及跨国欧洲
社会结构——采用多层（multilevel）与结构方程（SEM）模型、面板与事件史设计、比较设计，并在可行处使用因果
推断，数据多为协调化的调查数据（ESS、EU-SILC、SOEP、EVS）。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把美国社会学或经济学包改个名字套用过来。
它是 **ESR 专属** 技能栈：一个具有可迁移机制、且有比较或纵向杠杆的问题；正确的多层/测量建模；一份**完全
匿名**的稿件；通过 **ScholarOne** 投稿；一份必备的**数据可得性声明（DAS）**；以及（对统计/计算类研究）
作为发表条件的**复现包（replication package）**。

**官方依据核于 2026-06**（检索于 2026-06；以官网为准）。易变的具体信息（编辑与任期、确切上限、复现政策
日期、开放获取费用）会变化——未直接核实项在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标 **待核实**。
**请以官方页面为准。**

---

## ESR 是什么，为何需要专属技能栈？

ESR 的约束不同于综合性或美国社会学期刊：

| 约束 | ESR | 含义 |
|------|------|------|
| 范围 | **欧洲定量社会学** | 论文需具备可迁移机制 + 比较/纵向杠杆 |
| 看重 | 用严谨定量设计检验的宏观—微观机制 | 单一国家的描述性结果不合适 |
| 方法 | 多层/SEM、面板与事件史、比较、可行处因果 | 要把层级、聚类与测量等价做对 |
| 出版方 / 所有者 | **牛津大学出版社** / **ECSR** | 通过 **ScholarOne** 投稿，非 Editorial Manager 或 Sage Track |
| 评审模式 | **双盲**——完全匿名稿件 | **可以**自引，只是不能暴露身份 |
| 篇幅 | **论文约 8,000 词**，含尾注+参考文献；更长需说明 | 尾注与参考文献计入目标字数 |
| 摘要 | **≤200 词**，不含身份信息 | 比允许 250 词的期刊更紧 |
| 体例 | 英文；**作者—年份** 引用（如 "(Gans, 1962)"） | OUP/ESR 体例 |
| 透明度 | **数据可得性声明（必备）** + 统计类研究的**复现包**（2025-01-01 起的投稿） | 是发表条件，而非规范 |
| 文章类型 | 研究论文、评论/回应、**数据简报（Data Brief）** | 数据简报展示数据源，而非完整因果论证 |

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/european-sociological-review-skills
/plugin install european-sociological-review-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/european-sociological-review-skills.git
cd european-sociological-review-skills

mkdir -p ~/.claude/skills && cp -R skills/eursr-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/eursr-* ~/.codex/skills/
```

### 第一条提示

```
用 eursr-workflow 告诉我，我的 ESR 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
eursr-topic-selection
        ▼
eursr-literature-positioning
        ▼
eursr-theory-building
        ▼
eursr-research-design
        ▼
eursr-data-analysis
        ▼
eursr-tables-figures
        ▼
eursr-writing-style          （润色）
        ▼
eursr-transparency-and-data
        ▼
eursr-review-process
        ▼
eursr-submission
        ▼
eursr-rebuttal
```

`eursr-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `eursr-workflow` | 路由器——决定下一步调用哪个子技能 |
| `eursr-topic-selection` | 可迁移机制 + 比较杠杆；论文 vs 评论 vs 数据简报 |
| `eursr-literature-positioning` | 把贡献放进活跃的欧洲比较论争中 |
| `eursr-theory-building` | 构建带可检验跨层假设的宏观—微观机制 |
| `eursr-research-design` | 为设计辩护——比较、面板/事件史、多层、因果 |
| `eursr-data-analysis` | 多层/纵向建模、少聚类推断、稳健性 |
| `eursr-tables-figures` | 清晰、自洽的图表（不计入字数） |
| `eursr-writing-style` | OUP 作者—年份体例；在约 8,000 词内触达比较读者 |
| `eursr-transparency-and-data` | 数据可得性声明 + 复现包要求 |
| `eursr-review-process` | 双盲评审、决定、评审人看重什么 |
| `eursr-submission` | ScholarOne 投稿前检查（匿名、约 8,000 词、摘要 ≤200、DAS/包） |
| `eursr-rebuttal` | 面向多位评审 + 编辑的 R&R 回应信策略 |

### 资源

- [`resources/code/`](resources/code/) — 可复现的 Stata + Python 因果推断脚手架（复现包的基础）
- [`resources/external_tools.md`](resources/external_tools.md) — 欧洲数据（ESS / EU-SILC / SOEP / EVS）、ISCED/ISEI/EGP 协调编码、多层 / SEM / 面板软件
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 OUP / ECSR 官方 URL，未核实项标 待核实
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 一篇 ESR 风格引言的 before→after（虚构）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 经网络核实的真实 ESR 论文，按方法 × 主题组织

---

## 与姊妹期刊的区别

| 期刊 | 所有者 / 出版方 | 与 ESR 的定位区别 |
|------|----------------|-------------------|
| **欧洲社会学评论（ESR）** | ECSR / OUP | **本技能包**——欧洲定量社会学旗舰；比较与纵向 |
| 美国社会学评论（ASR） | ASA / SAGE | 美国综合旗舰；含理论与质性的全方法；Sage Track，$25 费 |
| 美国社会学杂志（AJS） | 芝加哥大学 | 美国综合；更偏理论/质性广度 |
| European Societies | ESA / Taylor & Francis | ESA 期刊；范围更广，非 ECSR 的定量旗舰 |
| European Journal of Sociology | 剑桥大学出版社 | 更偏理论/历史；非以定量为主 |
| Sociological Methods & Research | SAGE | 方法刊，非实质性定量文章 |

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不臆断易变元数据（现任编辑与任期、确切上限、政策日期、开放获取费用）——请以官方页面为准；未核实项标 待核实
- 不替你判断你的问题是否具备可迁移的比较机制——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [European Sociological Review（OUP）](https://academic.oup.com/esr) — 出版方主页
- [ECSR 上的 ESR](https://ecsrnet.eu/european-sociological-review-esr/) — 所有者、范围、编辑信息

---

## 许可

MIT
