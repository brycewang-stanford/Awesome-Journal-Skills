# Contemporary Accounting Research (CAR) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Contemporary Accounting Research 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-CAR-7a1f2b)](https://www.caaa.ca/journals-and-research/contemporary-accounting-research-car)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20ABDC%20A*-1f6feb)](https://www.caaa.ca/journals-and-research/contemporary-accounting-research-car)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Contemporary Accounting Research (CAR)** 投稿的 Agent 技能栈 —— CAR 是 **加拿大学术会计学会 (Canadian Academic Accounting Association, CAAA)** 旗下最顶级的会计研究期刊，由 **Wiley** 出版（自 2010 年起的出版合作），季刊（3/6/9/12 月）。

本仓库是有立场的。它**不是**通用的"会计写作"工具箱，而是围绕 CAR 的核心特征打造的 **CAR 专用**技能栈：CAR **刻意不绑定方法**，欢迎"会计学所有主题领域、采用任何合适的方法、植根于任何学科或研究传统的、有趣且严谨的研究"。从已发表论文看，其主体是档案/资本市场研究，但 CAR 同时是最欢迎**实验、解析/建模、田野、问卷与定性**会计研究的顶级期刊之一 —— 因此本技能栈按**研究传统**为你导航，并内置了 CAR 独特的投稿机制（投稿费、盲审稿件 + 独立标题页、强制性的伦理审批核验、Data Integrity & Code Sharing Policy，以及中英对照之外的英/法双语摘要）。

> 仅描述持久规范。主编、版面费、确切页数限制、CAR Style Guide 及 Data Integrity 政策都会变化 —— 请务必以 CAAA/CAR 官方作者指南页面及 Editorial Manager 为准。

---

## 为什么需要单独的 CAR 技能栈？

相比美国本土的会计与管理期刊，CAR 的约束有本质差异：

| 约束维度       | Contemporary Accounting Research (CAR)                          | 含义                                                       |
|----------------|----------------------------------------------------------------|------------------------------------------------------------|
| 范围           | 会计学所有主题领域；**任何合适的方法**                          | 一个技能栈须同时覆盖档案、实验、解析、定性                  |
| 主流方法       | 实践中以档案/资本市场为主，但政策上是"大帐篷"                   | 分析建议必须按研究传统分支，不能默认单一方法                |
| 投稿费         | **CA/US $250（会员）/ $600（非会员）**（Visa/Mastercard）       | 区别于免费投稿的管理期刊；须预算并上传收据                  |
| 篇幅           | **全文 50 页、正文 30 页**；超出部分进在线附录                  | 以页数（非字数）管控                                        |
| 摘要           | **≤ 300 词** + 至多六个关键词；以**英语 + 法语**双语发表        | 行文须便于翻译；CAAA 会翻译每一篇摘要                        |
| 伦理           | 任何涉及人类被试的研究须**REB/IRB 核验**                        | 仅作声明会被拒；必须上传证明文件                            |
| 可复现         | **Data Integrity & Code Sharing Policy**（2020）：仓库链接、代码、保存 6 年 | 从第一天起就规划变量定义与代码共享              |
| 评审与决定     | 双向匿名；**两位审稿人**；学科编辑做处置；**主编批准所有录用**  | 首轮直接录用几乎闻所未闻                                    |
| 流程特色       | CAR 会议致谢脚注；申诉须再交一笔费用；终稿阶段收集作者 X/Twitter 账号 | 美国同行没有的本刊专属规范                          |

通用的"科研写作"或"社科方法"技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/car-skills
/plugin install car-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/car-skills.git
cd car-skills

mkdir -p ~/.claude/skills && cp -R skills/car-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/car-* ~/.codex/skills/
```

### 第一条指令

```
用 car-workflow 告诉我，我这篇 CAR 稿子下一步该用哪个 skill。
```

---

## 默认工作流

```text
car-topic-selection（选题）
        ▼
car-theory-development（理论与预测）
        ▼
car-literature-positioning（文献定位）
        ▼
car-methods（研究设计与识别）
        ▼
car-data-analysis（数据分析与代码共享）
        ▼
car-contribution-framing（会计贡献提炼）
        ▼
car-tables-figures（图表）
        ▼
car-writing-style（文风打磨）
        ▼
car-submission（投稿前自检）
        ▼
car-review-process（理解评审流程）
        ▼
car-rebuttal（R&R 答复）
```

`car-workflow` 是路由器 —— 它根据你当前所处阶段、以及你的论文属于哪种研究传统（档案／实验／解析／定性）告诉你下一步用哪个 skill。

---

## 技能列表

| Skill                        | 用途                                                                  |
|------------------------------|-----------------------------------------------------------------------|
| `car-workflow`               | 路由器 —— 按研究传统决定下一步调用哪个子技能                          |
| `car-topic-selection`        | 会计研究问题 + CAR 契合度；选定问题所需的研究传统                      |
| `car-theory-development`     | 机制／预测／模型，按档案、实验、解析分别适配                           |
| `car-literature-positioning` | 加入会计学术对话；按作者声明披露与自有论文的重叠                       |
| `car-methods`                | 设计与识别策略匹配；强制性伦理审批核验                                 |
| `car-data-analysis`          | 按传统选择估计量、稳健性、Data Integrity & Code Sharing Policy         |
| `car-contribution-framing`   | 明确的会计贡献 + 实务/准则制定含义                                     |
| `car-tables-figures`         | 变量定义附录、结果/单元均值表，符合 CAR Style Guide 体例               |
| `car-writing-style`          | 问题前置、≤300 词摘要、脚注、作者-年份参考文献                         |
| `car-submission`             | Editorial Manager 投稿前自检（盲稿、标题页、费用、伦理、各项声明）     |
| `car-review-process`         | 双向匿名、两位审稿人、主编批准的流程；申诉                             |
| `car-rebuttal`               | R&R 修改方案 + 对两位审稿人与学科编辑的逐条答复                        |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 会计研究数据源（Compustat / CRSP / I/B/E/S / Audit Analytics / WRDS / Qualtrics / Prolific）与分析软件（Stata `reghdfe`/`csdid` / SAS / R `fixest` / PROCESS / Mathematica），并对应 CAR 的代码共享政策
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 本技能包每条已核实事实背后的 CAAA/CAR 官方链接（访问于 2026-06-01）

---

## 与 TAR / JAR / JAE / RAST 的差异

| 维度       | CAR                          | TAR                 | JAR                          | JAE                     |
|------------|------------------------------|---------------------|------------------------------|-------------------------|
| 主办/出版  | CAAA / Wiley（加拿大）       | 美国会计学会        | 芝加哥大学 Booth / Wiley     | Elsevier                |
| 方法立场   | **刻意不绑定方法**           | 宽口径、偏档案       | 宽口径、偏档案/实证          | 档案/经济学导向         |
| 特色规范   | 投稿费；**英/法双语摘要**；CAR 会议；REB 核验 | —  | 注册报告传统                 | 强经济学框架            |
| 最契合     | 任何传统下严谨的会计研究     | 一般性会计研究       | 高影响力的实证会计           | 经济学导向的会计        |

如果你的问题本质是纯金融或纯经济、只是套了会计数据，那么相较一篇"答案能改变我们对**会计本身**理解"的论文，CAR 的契合度更弱。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Academy-of-Management-Journal-Skills](https://github.com/brycewang-stanford) —— AMJ 技能包

---

## 许可证

MIT
