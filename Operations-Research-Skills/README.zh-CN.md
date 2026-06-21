# Operations Research（运筹学，OR）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Operations Research 期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Operations%20Research-1b3a6b)](https://pubsonline.informs.org/journal/opre)
[![Publisher](https://img.shields.io/badge/publisher-INFORMS-1f6feb)](https://www.informs.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向投稿 **Operations Research（OR）** 的智能体技能栈。OR 是 **INFORMS**（运筹学与管理科学协会）的旗舰方法论期刊。

本仓库立场鲜明，**不是**通用的“数学写作”或“数据科学”工具箱，而是**专为 Operations
Research 打造**的技能栈，围绕 OR 的核心标准构建：一项**数学上严谨、原创的 OR/MS 方法论
贡献**——优化、随机/概率模型、仿真或决策分析——并配以**可证明的结果**（定理与证明），同时
日益接纳数据驱动与应用型工作。技能涵盖：OR/MS 选题与领域归属判断、模型构建与结果陈述、文献定位、
证明/算法方法论、可复现的计算实验、强制性的贡献声明、INFORMS 排版风格与“引言不含公式”规范、
经 INFORMS Author Portal/ScholarOne 投稿并选择编辑领域、软双盲的分领域评审流程、
ORJournal GitHub 代码与数据可复现工作流，以及多轮修改回应。

> 仅沉淀长期稳定的规范。主编、领域编辑、费用、确切的页数分档与各项政策都会变化——请务必在
> 官方投稿指南页、Code and Data Disclosure Policy 以及 ORJournal 作者须知上核对最新要求。

---

## 为什么需要独立的 Operations Research 技能栈？

OR 的约束与实证管理类或资本市场会计类期刊存在本质差异：

| 约束维度      | Operations Research                                  | 含义                                              |
|---------------|------------------------------------------------------|---------------------------------------------------|
| 学科          | OR/MS 方法论（优化、随机、仿真、决策分析）            | 纯应用或方法薄弱的论文不匹配                       |
| 核心标准      | 数学上严谨、原创的方法论贡献                          | 没有方法或证明的数字只算技术报告                   |
| 结果          | 定理与证明；紧界、收敛率、可证保证                    | 仅靠数值“展示”的规律不算定理                       |
| 引言          | **不含公式**——以文字陈述问题、结果与意义              | 引言中出现公式即违反规范                           |
| 贡献          | **强制 <500 字贡献声明**（投稿信，2023-06-01 起）     | 不能含糊带过                                       |
| 路由          | 投稿时须选择期刊命名的**编辑领域**                    | 选错领域会被重新路由、拖慢流程                     |
| 评审          | **软双盲**且透明度不对称                              | 你能看到领域编辑姓名；评审人看不到你               |
| 可复现        | **ORJournal GitHub** 拉取请求式代码/数据评审          | “按需提供”不满足该政策                             |
| 排版          | 页数分档（20/20/30/~40）、1.5 倍行距、11 号、作者-年制 | 篇幅充实、排版精确的稿件                           |

通用的“科技写作”或“机器学习方法”技能包无法应对这些约束。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/ors-skills
/plugin install ors-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/ors-skills.git
cd ors-skills

mkdir -p ~/.claude/skills && cp -R skills/ors-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/ors-* ~/.codex/skills/
```

### 第一条提示词

```
用 ors-workflow 告诉我，我的 Operations Research 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
ors-topic-selection
        ▼
ors-theory-development
        ▼
ors-literature-positioning
        ▼
ors-methods
        ▼
ors-data-analysis
        ▼
ors-contribution-framing
        ▼
ors-tables-figures
        ▼
ors-writing-style        （润色）
        ▼
ors-submission
        ▼
ors-review-process
        ▼
ors-rebuttal
```

`ors-workflow` 是路由器——它会根据你所处的阶段告诉你下一步该用哪个技能。

---

## 技能清单

| 技能                          | 用途                                                                        |
|-------------------------------|-----------------------------------------------------------------------------|
| `ors-workflow`                | 路由器——决定下一步调用哪个子技能                                            |
| `ors-topic-selection`         | OR/MS 匹配度测试 + 正确的编辑领域归属（对比 MS / M&SOM / IJOC）             |
| `ors-theory-development`      | 模型构建；以恰当强度陈述定理/命题；假设的论证                               |
| `ors-literature-positioning`  | 相对最接近的前作给出技术差异（假设、界、复杂度）                            |
| `ors-methods`                 | 证明技术、算法保证、仿真/输出分析方法论                                     |
| `ors-data-analysis`           | 可复现的计算实验：基准实例、对照方法、置信区间、ORJournal 存档             |
| `ors-contribution-framing`    | 强制的 <500 字贡献声明 + 对 OR 的意义                                       |
| `ors-tables-figures`          | 定理排版、对比/计算结果表、收敛/规模化曲线                                 |
| `ors-writing-style`           | 不含公式的引言、≤200 字纯文本摘要、INFORMS 作者-年制风格                    |
| `ors-submission`              | Author Portal/ScholarOne 投稿前检查：领域、3 名 AE + 5 名评审、页数分档    |
| `ors-review-process`          | 分领域路由；软双盲；读懂决定信                                              |
| `ors-rebuttal`                | 逐条回应；弥补证明漏洞；ORJournal 可复现评审                               |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — OR/MS 建模语言与求解器（AMPL / JuMP / Pyomo / Gurobi / CPLEX / Mosek / SCIP）、仿真与随机工具（SimPy / SDDP.jl / RSOME / SimOpt）、证明/计算辅助工具，以及 ORJournal 可复现工作流
- [`resources/official-source-map.md`](resources/official-source-map.md) — 本技能包每条已核实事实背后的 INFORMS/OR 官方网址（访问于 2026-06-20）

---

## 与 INFORMS / OR/MS 同类期刊的差异

| 维度        | Operations Research          | Management Science          | M&SOM                       | INFORMS J. on Computing      |
|-------------|------------------------------|-----------------------------|-----------------------------|------------------------------|
| 核心贡献    | 严谨的 OR/MS **方法论**      | 广义管理科学                | 运营/供应链管理             | 计算/算法制品                |
| 标志性产出  | 定理、证明、可证保证         | 跨领域理论 + 实证           | OM 模型 + 管理洞见          | 计算方法、软件               |
| 最佳匹配    | 新模型类 / 可证明结果        | 广义管理科学问题            | 供应链 / 服务运营           | 算法与软件贡献               |

若贡献主要是计算制品，可考虑 *INFORMS Journal on Computing*；若属管理运营，可考虑
*M&SOM* 或 *Management Science*。

---

## 关键 OR 事实（依赖前请核实）

- **出版方 / 主办：** INFORMS。**主编：** Amy R. Ward（芝加哥大学 Booth 商学院），任期自 2024-01-01 起。
- **评审：** 软双盲；作者能看到领域编辑姓名，评审人看不到作者。
- **投稿：** 经 INFORMS Author Portal 进入 ScholarOne；须选择编辑领域；推荐 3 名 Associate Editor 并建议 5 名评审人。
- **贡献声明：** 自 2023-06-01 起强制，<500 字，写在投稿信中。
- **引言：** 不含公式。**摘要：** ≤200 字，纯文本。**关键词：** 最多 3 个。
- **页数分档（不含参考文献）：** Focused Technical 20 / Context-and-Challenge 20 / 常规 30 / 长文约 40 页；e-companion 不得长于正文。
- **格式：** 1.5 倍行距、11 号字、四周 1 英寸页边距；投稿时提交 PDF；提供 LaTeX 模板；作者-年制引用。
- **可复现：** Code and Data Disclosure Policy，经 ORJournal GitHub 拉取请求工作流。
- **费用：** 官方指南未列投稿/处理费；接收后可选 INFORMS Open Option 开放获取费用 3,000 美元。

详见 [`resources/official-source-map.md`](resources/official-source-map.md) 中的来源及标注为 待核实 / re-confirm 的条目。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引

---

## 许可证

MIT
