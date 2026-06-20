# 公共行政评论（PAR）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Public Administration Review 封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-PAR-5a2a4a)](https://onlinelibrary.wiley.com/journal/15406210)
[![Field](https://img.shields.io/badge/field-公共行政-1f6feb)](https://www.aspanet.org/ASPA/Publications/Public-Administration-Review/Public-Administration-Review.aspx)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《公共行政评论》（Public Administration Review, PAR）** 投稿的 Agent 技能栈。PAR 是
**美国公共行政学会（ASPA）的旗舰期刊**，由 **Wiley** 出版，是公共行政与公共管理领域的首要发表平台，覆盖
**官僚制与治理、公共部门绩效与管理、公共人事/人力资源、公共财政与预算、协作治理、公共服务动机、政策执行**。
PAR 的标志性特征是 **沟通研究与实践**：每篇文章都被期望既面向学者、也面向实务者——通过
**Evidence for Practice（实践要点）**。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把公共政策包改名套用到公共行政。
它是 **PAR 专属** 技能栈：一个对**整个公共行政学科都有普遍意义**的问题、一个可信的**面向实务者的
"so-what"**、一套在其自身方法论标准上站得住脚的研究设计、**双盲**准备，以及一份符合 **TOP 透明度准则**
的材料（Dataverse / QDR）。

官方依据核对于 **2026-06**（检索于 2026-06；以官网为准）。易变信息（主编与任期、确切字数上限、费用/APC、
投稿系统、政策措辞）会变化——未能直接确认的条目在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标记为 **待核实**。**请以官网为准。**

---

## PAR 是什么，为何需要专属技能栈？

PAR 的约束不同于理论导向的 PA 期刊或政策分析期刊：

| 约束             | PAR                                                                  | 含义                                              |
|------------------|----------------------------------------------------------------------|---------------------------------------------------|
| 范围             | **整个公共行政与管理学科**                                            | 论文必须超越细分领域                              |
| 看重             | **学科普遍意义 + 实务相关性**（研究↔实践的桥梁）                       | 纯学术、没有 "so-what" 的发现属于不对口            |
| 方法             | 定量、实验、定性、混合方法——各按其标准评判                            | 不要把单一模板套到每篇论文                        |
| 标志性要求       | **Evidence for Practice**——3–5 条面向实务者的要点                     | 与贡献一起起草，而非最后补上                      |
| 出版方 / 所有方  | **Wiley** / **ASPA**                                                  | Wiley 投稿系统；请确认现行投稿门户                |
| 评审模式         | **双盲**                                                             | 匿名化稿件；以第三人称引用自己的既往工作          |
| 费用             | 未列明 **投稿费**                                                     | 不要预算投稿费（请核实）待核实                    |
| 篇幅             | **≤ 8,000 词**（含摘要/尾注/参考文献）；摘要 **≤ 150 词**             | 表、图、附录不计入字数                            |
| 体例             | **APA 著者—年份制**                                                   | 请确认当前版次                                    |
| 透明度           | **TOP 准则签署方**——Dataverse/QDR、数据可得性声明                     | 边做边准备材料；记录设计/数据处理决策            |
| 文章类型         | Scholarly Take · Conceptualizing PA · Early Career Intel · Practically Speaking | 提前选定类型                          |

### 文章类型

- **Scholarly Takes** —— 投稿的研究型稿件；主要的实证形式。
- **Conceptualizing Public Administration** —— 概念/理论思想性文章与"PA 现状"评述。
- **Early Career Intel** —— 青年学者的研究型稿件；同等严谨、范围更聚焦。
- **Practically Speaking** —— 实务者与学者合著（常源自 PAR Talk / On PAR）。
- **Public Administration in Print** —— 书评（不属于本实证技能栈范围）。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/public-administration-review-skills
/plugin install public-administration-review-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/public-administration-review-skills.git
cd public-administration-review-skills

mkdir -p ~/.claude/skills && cp -R skills/pubar-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/pubar-* ~/.codex/skills/
```

### 第一条提示

```
用 pubar-workflow 告诉我，我的 PAR 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
pubar-topic-selection
        ▼
pubar-literature-positioning
        ▼
pubar-theory-building
        ▼
pubar-research-design
        ▼
pubar-data-analysis
        ▼
pubar-tables-figures
        ▼
pubar-writing-style          （润色 + Evidence for Practice）
        ▼
pubar-transparency-and-data
        ▼
pubar-review-process
        ▼
pubar-submission
        ▼
pubar-rebuttal
```

`pubar-workflow` 是路由器——根据你所处阶段和目标文章类型，告诉你下一步用哪个技能。请将**面向实务者的
"so-what"** 与贡献一起起草，而非最后补上。

---

## 技能一览

| 技能                            | 用途                                                                       |
|---------------------------------|----------------------------------------------------------------------------|
| `pubar-workflow`                | 路由器——决定下一个调用哪个子技能                                            |
| `pubar-topic-selection`         | 学科普遍意义 + 实务对口；选定文章类型                                       |
| `pubar-literature-positioning`  | 介入 PA 核心争论；超越细分领域；防止漂移到 JPART/JPAM                        |
| `pubar-theory-building`         | 构建可迁移的机制并带管理可操作杠杆（双重检验）                              |
| `pubar-research-design`         | 论证设计——改革 DiD、官僚/公民实验、案例、混合方法                           |
| `pubar-data-analysis`           | 分析规范、不确定性、稳健性；让估计能支撑 Evidence for Practice              |
| `pubar-tables-figures`          | 自足、可访问、向管理者展示效应量的图表                                      |
| `pubar-writing-style`           | APA 体例；同时面向学者与实务者；写出诚实的 Evidence for Practice            |
| `pubar-transparency-and-data`   | TOP 透明度；Dataverse/QDR；数据可得性声明；受限数据路径                     |
| `pubar-review-process`          | 双盲评审、初筛、文章类型分流、决定谱系                                      |
| `pubar-submission`              | 提交前检查——匿名化、字数/摘要上限、Evidence for Practice、投稿门户          |
| `pubar-rebuttal`                | R&R 回复信策略，保护贡献与 Evidence for Practice                            |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— PA 数据源（FedScope / FEVS / 政府普查 / WGI / QoG）及 R / Stata / Python 与定性/CAQDAS 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的 Wiley / ASPA 官方网址，未确认项标注 待核实
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— PAR 风格引言的 before→after 范例（虚构）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 按子领域 × 方法整理、经网络核实的真实 PAR 论文
- [`resources/code/`](resources/code/) —— 内置的 Stata + Python 因果推断脚手架

---

## 与兄弟期刊的差异

| 期刊 | 所有方 / 出版方 | 定位 | 与 PAR 的区别 |
|------|------------------|------|----------------|
| **PAR** | ASPA / Wiley | 沟通研究与实践的 PA 旗舰 | 要求可信的实务 "so-what"（Evidence for Practice） |
| **JPART** | Oxford | 理论导向的 PA | 更形式化/理论化；无实务要点要求 |
| **JPAM** | APPAM / Wiley | 政策分析与评估 | 贡献在于*政策选择*，而非*行政管理* |
| **Governance** | Wiley | 比较制度 / 治理 | 视角是政体/制度设计，而非公共管理实践 |
| **ARPA / Public Administration** | Sage / Wiley | 一般 PA 领域期刊 | 不同期刊；勿将 PAR 政策套用其上 |

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或审稿人的口味
- 不断言易变元数据（现任主编与任期、确切上限、费用/APC、投稿门户、政策措辞）——请以官网为准；未确认项标注 待核实
- 不替你判断问题是否具备学科普遍意义、或实务要点是否诚实——这是研究者的责任

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属技能包索引
- [Public Administration Review（Wiley Online Library）](https://onlinelibrary.wiley.com/journal/15406210) —— 出版方主页
- [PAR @ ASPA](https://www.aspanet.org/ASPA/Publications/Public-Administration-Review/Public-Administration-Review.aspx) —— 所有方与期刊信息

---

## 许可证

MIT
