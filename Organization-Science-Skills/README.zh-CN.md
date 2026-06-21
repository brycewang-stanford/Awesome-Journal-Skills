# Organization Science Skills

<p align="center">
  <img src="assets/cover.svg" alt="Organization Science 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Organization%20Science-10497e)](https://pubsonline.informs.org/journal/orsc)
[![Index](https://img.shields.io/badge/index-INFORMS%20%7C%20FT50-1f6feb)](https://pubsonline.informs.org/journal/orsc)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Organization Science（组织科学）** 投稿的 Agent 技能栈 —— 这是由 **INFORMS（运筹学与管理科学研究协会）** 出版的、跨学科且**以理论驱动**的组织研究期刊，覆盖从**微观（个体/团队）到宏观（组织/场域/种群）** 的各个层次。

本仓库是有立场的。它**不是**通用的"管理学写作"工具箱，而是围绕 Organization Science 核心标准打造的 **专用**技能栈：以**整体贡献胜过新颖性**为准绳（编辑声明明确指出"理论新颖性既非必要也非充分"），并秉持**方法论上的兼容并蓄** —— 在定量、实验、计算/仿真、形式化分析之外，对**定性与归纳式**研究有着标志性的开放与偏好。覆盖范围包括：理论驱动的选题、演绎或归纳式的理论构建、跨学科的文献定位、与问题匹配的研究设计与透明分析、简洁的**投稿信贡献论证**、符合 INFORMS 体例的图表与文风、在"全计入约 50 页"篇幅规范下的 ScholarOne 投稿、去中心化的资深编辑评审流程，以及在期刊明文规定的作者答复规范下撰写 R&R 答复。

> 仅描述有官方来源支撑的规范。投稿前请重新打开 INFORMS submission guidelines、editorial statement、data and methods transparency、editorial board 与 Manuscript Length Policy PDF。

---

## 为什么需要单独的 Organization Science 技能栈？

相比"先看因果识别"的期刊或纯理论期刊，Organization Science 的约束有本质差异：

| 约束维度       | Organization Science                                       | 含义                                                       |
|----------------|------------------------------------------------------------|------------------------------------------------------------|
| 学科           | 跨学科的组织研究，微观 → 宏观                                | 纯单一学科或纯方法论文章不契合                              |
| 核心标准       | **整体贡献** 胜过新颖性                                      | "从未有人研究过"不构成贡献                                  |
| 方法论         | 兼容并蓄；**定性/归纳是标志**                                | 不要求因果识别（"往往不可能"）                              |
| 推断           | 设计 + 理论 + 制度知识 + 机制证据                            | 可信的机制胜过单薄的工具变量                                |
| 贡献论证       | 投稿信由 EIC/SE 可见，评审不可见                              | 清楚说明贡献；保持简洁                                      |
| 篇幅           | **全计入约 50 页** 的规范；编辑有裁量权                      | 繁重材料放入**单独的、匿名化的附录**                        |
| 评审           | 投稿流程要求按**双盲**准备；至少 2 名审稿人                  | 正文须完全匿名；投稿作者需 ORCID                            |
| 编辑模型       | **去中心化的资深编辑**，权力较大；利益冲突级联路由            | 决定你稿件的是资深编辑（SE），而非领域编辑                  |
| 体例           | INFORMS 作者-年份制；不用 Helvetica Narrow；摘要 ≤ 250 词    | 数字编号引用体例在此是错的                                  |

通用的"科研写作"或"先识别"方法技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/orgsci-skills
/plugin install orgsci-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/orgsci-skills.git
cd orgsci-skills

mkdir -p ~/.claude/skills && cp -R skills/orgsci-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/orgsci-* ~/.codex/skills/
```

### 第一条指令

```
用 orgsci-workflow 告诉我，我这篇 Organization Science 稿子下一步该用哪个 skill。
```

---

## 默认工作流

```text
orgsci-topic-selection（选题）
        ▼
orgsci-theory-development（理论构建）
        ▼
orgsci-literature-positioning（文献定位）
        ▼
orgsci-methods（研究设计）
        ▼
orgsci-data-analysis（分析与透明度）
        ▼
orgsci-contribution-framing（贡献陈述）
        ▼
orgsci-tables-figures（图表）
        ▼
orgsci-writing-style（文风打磨）
        ▼
orgsci-submission（投稿前自检）
        ▼
orgsci-review-process（理解评审流程）
        ▼
orgsci-rebuttal（R&R 答复）
```

`orgsci-workflow` 是路由器 —— 它根据你当前所处的阶段告诉你下一步该用哪个 skill。

---

## 技能列表

| Skill                          | 用途                                                                  |
|--------------------------------|-----------------------------------------------------------------------|
| `orgsci-workflow`              | 路由器 —— 决定下一步调用哪个子技能                                     |
| `orgsci-topic-selection`       | 理论驱动的选题 + 契合度判断（对比 ASQ / AMJ / Management Science）     |
| `orgsci-theory-development`    | 演绎式先验机制**或**归纳式扎根模型；微观-宏观跨层桥接                  |
| `orgsci-literature-positioning`| 加入一场组织理论的学术对话；用"问题化"取代"找空白"                     |
| `orgsci-methods`               | 将兼容并蓄的方法与问题匹配；在无法识别时如何做推断                     |
| `orgsci-data-analysis`         | 因法而异的严谨性：可信度、多层/事件史估计、仿真/形式化                 |
| `orgsci-contribution-framing`  | 投稿信贡献论证 + 与之呼应的讨论                                        |
| `orgsci-tables-figures`        | 数据结构/过程模型/嵌套表/敏感性图，符合 INFORMS 体例                   |
| `orgsci-writing-style`         | 面向微观到宏观读者的论点前置；INFORMS 作者-年份体例                    |
| `orgsci-submission`            | ScholarOne 投稿前自检（贡献陈述、匿名化、约 50 页规范、附录）          |
| `orgsci-review-process`        | 去中心化的资深编辑模型，以及如何读懂决定信                             |
| `orgsci-rebuttal`              | 在期刊明文作者答复规范下做 R&R 修改 + 答复信                           |

### 资源

- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条期刊事实背后的 INFORMS 官方 URL 与投稿周 live-check 边界
- [`resources/external_tools.md`](resources/external_tools.md) —— 覆盖期刊兼容并蓄方法的组织研究数据源与软件（NVivo/ATLAS.ti 与 Gioia 模板；NetLogo/Mesa 与形式化建模；igraph/ERGM 网络；lme4/Mplus/Stata 多层与事件史）

---

## 与 ASQ / AMJ / Management Science 的差异

| 维度       | Organization Science                  | ASQ                          | AMJ                          | Management Science                     |
|------------|---------------------------------------|------------------------------|------------------------------|----------------------------------------|
| 出版方     | INFORMS                                | Cornell / SAGE               | 美国管理学会 (AOM)           | INFORMS                                |
| 核心标准   | **整体贡献** 胜过新颖性                | 大胆框架、深度情境           | 实证**加**理论               | 常偏向因果识别                         |
| 方法       | 兼容并蓄；定性/归纳是标志              | 定性与定量                   | SEM / HLM / 面板 / 实验      | 更偏定量 / 分析                        |
| 因果识别   | 重视但"非必要、往往不可能"             | 不要求                       | 档案数据声明通常需要         | 经常被要求                             |
| 路由       | 自主的**资深编辑**；利益冲突级联       | 编辑 + 编委                  | AOM 行动编辑                 | **按部门的领域编辑**                   |
| 数据政策   | 2025 透明度政策：代码/数据共享，可有例外 | 期刊政策                     | AOM 透明度政策               | **强制代码与数据披露**                 |

如果你的文章不需要理论、成败完全取决于一个干净的工具变量，Management Science 可能更合适；如果是大胆而情境深厚的研究，ASQ 更契合；如果需要在页数限制下兼顾实证与理论，AMJ 更对路。Organization Science 奖励的是对组织研究的**整体贡献**，方法与问题匹配即可。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引

---

## 许可证

MIT
