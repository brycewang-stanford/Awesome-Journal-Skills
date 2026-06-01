# 《会计评论》(The Accounting Review, TAR) Skills

<p align="center">
  <img src="assets/cover.svg" alt="The Accounting Review 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-TAR-1b3a5b)](https://aaahq.org/Research/Journals/The-Accounting-Review)
[![Publisher](https://img.shields.io/badge/publisher-AAA-1f6feb)](https://aaahq.org)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《会计评论》(The Accounting Review, TAR)** 投稿的 Agent 技能栈 —— TAR 是由**美国会计学会 (American Accounting Association, AAA)** 出版的旗舰期刊，覆盖档案/实证与分析（建模）类会计研究。

本仓库是有立场的。它**不是**通用的"学术写作"工具箱，而是围绕 TAR 的核心标准打造的 **TAR 专用**技能栈：**对会计文献贡献的重要性 (significance of the contribution)** —— 档案研究靠可信的识别策略，分析类靠被证明的模型，实验类靠干净的操纵来确立。覆盖范围包括以贡献为驱动的选题、经济机制/解析模型构建、文献定位、识别与研究设计、大样本档案与分析估计（含 TAR 的数据真实性 / 代码可获取规定）、符合 Chicago 体例的图表与文风、Editorial Manager 投稿（含 AI 披露与 ORCID）、双盲评审流程，以及多轮 R&R 答复。

> 仅描述持久规范。主编、投稿费、确切页数限制及各项政策会变化 —— 请务必以 TAR 官方 Editorial Policy、Guide for Authors 与 AAA Manuscript Preparation Guide 为准。

---

## 为什么需要单独的 TAR 技能栈？

相比管理学或通用社科期刊，TAR 的约束有本质差异：

| 约束维度       | 《会计评论》(TAR)                                            | 含义                                                       |
|----------------|------------------------------------------------------------|------------------------------------------------------------|
| 学科           | 会计学 —— 财务、资本市场、审计、税务、管理会计、会计信息系统 | 纯金融/经济学文章不契合                                    |
| 核心标准       | **对会计文献贡献的重要性**                                   | 方法再干净、若无贡献也不够                                 |
| 实际主流方法   | 大样本**档案/实证**为主，兼具实验与分析（建模）两条支流       | 期待识别，而非仅有相关                                     |
| 识别           | 冲击 / DiD / IV / RDD / 能打破内生性的研究设定               | "我们控制了一切"并不能识别因果效应                         |
| 数据真实性     | 数据描述 **+ 处理代码**（公开/抽取/私有 三类规则）           | 不可复现的样本与缺失代码会被拒                             |
| 体例           | Chicago Manual of Style (16 版)；首轮 55 页上限（含图表附录）| APA 引用格式与超长稿件会被点名                            |
| 摘要           | **≤ 150 词**，其后须紧跟 **AI 披露声明**                     | 含糊/超长摘要与缺失披露都会扣分                            |
| 评审           | **双盲**；编辑 + 至少两名审稿人                              | 任何自我暴露身份都会破坏流程                               |
| 流程           | Editorial Manager；分层 Senior/Lead/Editor/Ad hoc 路由；多轮 R&R | 首轮直接录用几乎闻所未闻                              |
| 投稿限额       | 每位作者 24 个月内 8 篇首轮投稿；署名 ≤ 10 人                | 通用期刊没有的投稿量与署名节流                            |

通用的"科研写作"或"社科方法"技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/tar-skills
/plugin install tar-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/tar-skills.git
cd tar-skills

mkdir -p ~/.claude/skills && cp -R skills/tar-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/tar-* ~/.codex/skills/
```

### 第一条指令

```
用 tar-workflow 告诉我，我这篇 TAR 稿子下一步该用哪个 skill。
```

---

## 默认工作流

```text
tar-topic-selection（选题）
        ▼
tar-theory-development（机制/模型）
        ▼
tar-literature-positioning（文献定位）
        ▼
tar-methods（识别与设计）
        ▼
tar-data-analysis（估计与数据真实性）
        ▼
tar-contribution-framing（贡献提炼）
        ▼
tar-tables-figures（图表）
        ▼
tar-writing-style（文风打磨）
        ▼
tar-submission（投稿前自检）
        ▼
tar-review-process（理解评审流程）
        ▼
tar-rebuttal（R&R 答复）
```

`tar-workflow` 是路由器 —— 它根据你当前所处的阶段告诉你下一步该用哪个 skill。

---

## 技能列表

| Skill                        | 用途                                                                  |
|------------------------------|-----------------------------------------------------------------------|
| `tar-workflow`               | 路由器 —— 决定下一步调用哪个子技能                                     |
| `tar-topic-selection`        | 贡献驱动的选题 + TAR 契合度判断（对比 JAR/JAE/分会期刊）              |
| `tar-theory-development`     | 经济机制 / 解析模型与可检验预测                                        |
| `tar-literature-positioning` | 加入会计学术对话；用"问题化"取代"找空白"                               |
| `tar-methods`                | 识别设计（DiD/IV/RDD/冲击）、实验或解析模型                            |
| `tar-data-analysis`          | 估计量、固定效应、聚类、稳健性、数据真实性代码                         |
| `tar-contribution-framing`   | 明确的会计贡献陈述，主张与证据相匹配                                   |
| `tar-tables-figures`         | 档案标准表组、事件研究/RDD/模型图，符合 Chicago 体例                   |
| `tar-writing-style`          | 结论前置的文风、Chicago 体例、≤150 词摘要                              |
| `tar-submission`             | Editorial Manager 投稿前自检（匿名化、AI 披露、ORCID、代码）           |
| `tar-review-process`         | TAR 双盲评审/决定如何运作；如何读懂决定信                              |
| `tar-rebuttal`               | 多轮 R&R 修改与逐条答复信                                              |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 会计研究数据源（Compustat / CRSP / I·B·E·S / Audit Analytics / EDGAR / PCAOB）与软件（Stata `reghdfe`/`csdid`、R `fixest`、SAS+WRDS、解析类用 Mathematica）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 本技能包每条已核实事实背后的 AAA/TAR 官方链接（访问于 2026-06-01；未核实项标注 待核实）

---

## 与 JAR / JAE 及 AAA 期刊家族的差异

| 维度       | TAR                          | JAR                 | JAE                          | AAA 分会期刊                  |
|------------|------------------------------|---------------------|------------------------------|-------------------------------|
| 主办       | 美国会计学会 (AAA)           | 芝加哥大学 Booth    | Elsevier                     | AAA 各分会                    |
| 范围       | 全会计领域、全方法           | 偏档案、覆盖广      | 经济学基础的档案研究         | 子领域（审计/税务/管理/AIS）  |
| 评审       | **双盲**                     | 自有规范            | 自有规范                     | 各异（JFR 为单盲）            |
| 最契合     | 具有广泛会计意义的研究       | 顶级档案、芝加哥体例 | 经济学驱动的会计研究         | 主要为子领域兴趣              |

如果会计构念只是附带，问题本质上属于金融或经济学，那么 TAR 不是合适的投稿对象。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Academy-of-Management-Journal-Skills](https://github.com/brycewang-stanford) —— AMJ 技能栈（实证管理学）

---

## 许可证

MIT
