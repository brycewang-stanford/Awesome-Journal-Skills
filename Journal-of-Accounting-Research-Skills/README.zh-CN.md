# 《会计研究杂志》(Journal of Accounting Research, JAR) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Accounting Research 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JAR-7a0019)](https://www.chicagobooth.edu/research/chookaszian/journal-of-accounting-research)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20SSCI-1f6feb)](https://www.chicagobooth.edu/research/chookaszian/journal-of-accounting-research)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《会计研究杂志》(Journal of Accounting Research, JAR)** 投稿的 Agent 技能栈 —— JAR 是"会计学三大顶刊"之一，由**芝加哥大学布斯商学院 Chookaszian 会计研究中心**主办、与 Wiley-Blackwell 合作出版。

本仓库是有立场的。它**不是**通用的"会计写作"工具箱，而是围绕 JAR 的核心身份打造的 **JAR 专用**技能栈：以 **Ball-Brown** 传统为根基、严谨的**实证档案式资本市场**研究，以**可信的识别策略 (identification)** 与"会计信息如何被生产、披露、审计与使用"的经济学故事作为评判标准。覆盖范围包括：选题与 JAR 契合度判断、以经济学为基础的理论与有方向的预测、文献定位、以识别为驱动的研究设计、大样本档案数据分析（聚类标准误、内生性、构念测量、稳健性）、贡献提炼、符合 JAR 体例的图表与文风、Wiley Research Exchange 投稿与分级版面费、双盲（double-anonymized）的编委团队评审，以及多轮 R&R 答复。

> 仅描述持久规范。主编、版面费、确切篇幅限制、会议主题及各项政策都会变化 —— 请务必以 Chookaszian 中心的 JAR 官方页面与 Wiley 作者须知为准。

---

## 为什么需要单独的 JAR 技能栈？

相比纯理论期刊或管理学期刊，JAR 的约束有本质差异：

| 约束维度       | 《会计研究杂志》(JAR)                                       | 含义                                                       |
|----------------|------------------------------------------------------------|------------------------------------------------------------|
| 学科           | 实证会计（资本市场、披露、审计、税务）                       | 纯金融或纯方法论文章不契合                                  |
| 核心标准       | 可信的**识别策略**＋经济学故事                               | 没有识别变异的面板回归会被视为相关性，而非因果              |
| 理论           | 以经济学为基础的机制（信息／代理／披露）                     | 心理学式的构念链条不适合                                    |
| 设计           | 档案式自然实验、断点 (RD)、工具变量 (IV)、事件研究（也含实验／解析／田野） | 设计必须真正识别出该效应                          |
| 推断           | 聚类标准误与设计匹配（公司／公司×年度）                       | 在面板数据上用普通稳健标准误会被点名                        |
| 可复现         | **强制**数据与代码共享（公开托管）                           | "代码备索"不被接受；须尽早搭建可复现包                      |
| 投稿门槛       | **分级版面费**（$750/$500/$50），一周内付清                  | 须预留费用；低档需全部作者居住于二／三档国家                |
| 投稿数量上限   | 每位作者**两年内最多四篇新稿**                               | 须筛选投哪些项目                                            |
| 流程           | Senior Editor 编委团队；双盲；多轮 R&R                       | 没有单一主编；首轮直接录用闻所未闻                          |
| 特色通道       | **Ray Ball 年度会议**（六月会议专号）；**Registered Reports** | 有各自规则的额外路径                                       |

通用的"科研写作"或"社科方法"技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jar-skills
/plugin install jar-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/jar-skills.git
cd jar-skills

mkdir -p ~/.claude/skills && cp -R skills/jar-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jar-* ~/.codex/skills/
```

### 第一句提示词

```
使用 jar-workflow 告诉我，我的 JAR 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
jar-topic-selection
        ▼
jar-theory-development
        ▼
jar-literature-positioning
        ▼
jar-methods
        ▼
jar-data-analysis
        ▼
jar-contribution-framing
        ▼
jar-tables-figures
        ▼
jar-writing-style        （润色）
        ▼
jar-submission
        ▼
jar-review-process
        ▼
jar-rebuttal
```

`jar-workflow` 是路由器 —— 它会根据你所处的阶段告诉你下一步用哪个技能。

---

## 技能列表

| 技能                        | 用途                                                                     |
|-----------------------------|--------------------------------------------------------------------------|
| `jar-workflow`              | 路由器 —— 决定下一步调用哪个子技能                                        |
| `jar-topic-selection`       | 会计问题＋可信情境＋JAR 契合度（对比 TAR/JAE/RAST/CAR）                   |
| `jar-theory-development`    | 以经济学为基础的机制；有方向、可证伪的预测                                |
| `jar-literature-positioning`| 加入会计文献对话；明确边际贡献                                            |
| `jar-methods`               | 识别策略（档案自然实验／RD／IV／事件研究／实验）                          |
| `jar-data-analysis`         | 聚类标准误、内生性处理、构念测量、稳健性                                  |
| `jar-contribution-framing`  | 对会计知识的明确贡献＋经济意义上的幅度                                    |
| `jar-tables-figures`        | 符合 JAR 体例的样本／描述统计／结果／识别图表                             |
| `jar-writing-style`         | 设计先行、经济学语感的文风；JAR 作者-年份引用体例                         |
| `jar-submission`            | Research Exchange 投稿前检查：匿名化、分级版面费、数据与代码包            |
| `jar-review-process`        | 编委团队评审、费用／案头门槛、Ray Ball 会议与 Registered Reports 通道     |
| `jar-rebuttal`              | 多轮 R&R 修改与逐条回复信                                                 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 实证会计数据源（Compustat / CRSP / I/B/E/S / Audit Analytics / EDGAR）与分析软件（Stata `reghdfe`/`csdid`/`rdrobust`、R `fixest`、SAS、WRDS）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条已核实事实背后的 JAR / Chookaszian 中心 / Wiley 官方链接（访问于 2026-06-01）；未核实项标注 **待核实**

---

## JAR 的独特之处

- **实证档案式资本市场身份**（Ball-Brown 传统）—— 识别与经济幅度与回归的严谨性同等重要。
- **强制数据与代码共享** —— JAR 真正**要求并托管**数据表/代码，而非像部分顶刊那样仅"鼓励"。
- **分级、按国别的版面费**（$750/$500/$50），须在投稿后一周内付清。
- **Senior Editor 编委团队**（无单一主编）主持双盲评审。
- **Ray Ball JAR 年度会议**，并设有专门的（历史上为六月的）会议专号。
- **Registered Reports** —— 预注册、两阶段、与结果无关的"原则性接收"。

---

## 与 TAR / JAE / RAST / CAR 的差异

| 维度               | JAR                               | TAR                          | JAE                                | RAST / CAR                   |
|--------------------|-----------------------------------|------------------------------|------------------------------------|------------------------------|
| 主办/出版          | 芝加哥布斯（Chookaszian）/ Wiley   | 美国会计学会 (AAA)           | Elsevier                           | Springer / Wiley             |
| 标志性身份         | 实证档案式资本市场                 | 全会计领域、范围宽广          | 实证的契约/披露经济学              | 宽口径实证会计                |
| 数据/代码政策      | **强制并托管**                     | 无等同强制要求               | **鼓励**                           | 各异                          |
| 特色通道           | Ray Ball 会议；Registered Reports  | —                            | —                                  | —                            |

如果你的论文纯属方法论贡献、没有会计问题，或没有识别杠杆，JAR 很可能不是合适的投稿对象。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 各期刊专用技能包索引

---

## 许可证

MIT
