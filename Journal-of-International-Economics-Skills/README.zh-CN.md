# 《国际经济学杂志》(JIE) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of International Economics 期刊封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JIE-13386b)](https://www.sciencedirect.com/journal/journal-of-international-economics)
[![Field](https://img.shields.io/badge/field-International%20Economics-1f6feb)](https://www.sciencedirect.com/journal/journal-of-international-economics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Journal of International Economics（JIE，《国际经济学杂志》）** 投稿的 Agent Skill 工具栈。JIE 由 **Elsevier（爱思唯尔）** 出版，是同时覆盖**国际贸易**与**国际宏观/金融**两大方向的顶级领域期刊。其范围包括：贸易模式与贸易政策、国际机构、汇率、开放经济宏观、国家/地区增长与发展、国际金融、国际定价、主权债务、国际要素流动、空间经济学，以及国际货币与财政理论与政策。JIE 同时刊发实证与理论研究，但要求论文在**动机或建模结构上具有原创性**。

本仓库刻意**不通用**——它不是泛化的"经济学写作助手"，而是围绕该领域两个半边（引力/结构化贸易，与开放经济宏观/金融）以及 JIE 真实流程打造的方法论沉淀：不可退还的投稿费、加速通道 Prior Review Process（PRP）、150 词摘要上限，以及向期刊安全仓库强制存放复制代码与数据。

---

## 为什么要为 JIE 单独做一套 Skills？

JIE 的约束维度与综合性 top-5 期刊或方法类期刊**显著不同**：

| 维度        | JIE                                                              | 隐含含义                                   |
|-----------|------------------------------------------------------------------|----------------------------------------|
| 读者       | 国际经济学者——贸易**与**国际宏观/金融                                | 论文须清晰对话其中一个半边                    |
| 原创性门槛   | 在**动机或建模结构**上具有原创性                                     | 把已知设计在新数据上重跑会不契合               |
| 投稿系统    | **Editorial Manager**（Elsevier）                                | 非 Editorial Express / ScholarOne，上传流程不同 |
| 投稿费      | **USD 190 / EUR 169.20 / JPY 20,660**（全部作者为博士生时为 USD 95）  | 需预算；相关欧洲作者另加增值税                 |
| 加速通道    | **PRP**：携带 AER/Econometrica/JPE/QJE/REStud 的拒稿决定信与审稿报告  | Article Type 选 'PRP'；不额外收费           |
| 投稿类型    | 常规、**短文（Short Paper，≤6,000 词且 ≤5 个图表）**、或 PRP          | 按贡献选择类型                             |
| 审稿模型    | **单匿名审稿**；适合送审的稿件通常至少交给两名审稿人                    | 投稿前先校准预期                            |
| 摘要       | **≤150 词**，事实性、单段、避免引用                                  | 又长又堆引用的摘要不合体例                    |
| 关键词      | **1-7 个关键词**                                                  | 选利于领域检索的术语                         |
| 参考文献    | Elsevier 在**校样阶段**套用期刊体例——投稿可用任何一致格式             | 须含必备著录要素；鼓励 DOI                   |
| 数据/代码   | **强制存放**程序与数据到 JIE 安全仓库                                | 边做边构建 Mendeley Data 复制包             |
| 编辑匹配    | 建议匹配论文方向的 **Editor 或 Co-Editor**                           | 贸易 vs 宏观/金融的分流很重要                 |

常规投稿录用率历史上约 **10-15%**，desk reject 约 **25%**（据 Editor Costas Arkolakis 个人主页）。本包已在 2026-06-20 刷新官方 Guide for Authors 与 editorial-board 页面；正式上传前仍应到官网复核费用、编辑名单与投稿入口。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jie-skills
/plugin install jie-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/jie-skills.git
cd jie-skills

mkdir -p ~/.claude/skills && cp -R skills/jie-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jie-* ~/.codex/skills/
```

### 第一条 Prompt

```
用 jie-workflow 告诉我这份 JIE 目标稿子下一步该用哪个 skill。
```

---

## 默认工作流

```text
jie-topic-selection
        ▼
jie-literature-positioning
        ▼
jie-identification-strategy
        ▼
jie-data-analysis
        ▼
jie-contribution-framing
        ▼
jie-tables-figures
        ▼
jie-writing-style          （polish）
        ▼
jie-replication-and-data-policy
        ▼
jie-review-process
        ▼
jie-submission
        ▼
jie-rebuttal
```

`jie-workflow` 是路由器，会根据当前阶段告诉你下一个该用哪个 Skill。

---

## Skill 一览

| Skill                              | 用途                                                       |
|------------------------------------|----------------------------------------------------------|
| `jie-workflow`                     | 路由器：判断当前阶段，推荐下一个 skill                         |
| `jie-topic-selection`              | 契合 JIE 贸易 / 宏观-金融范围 + 原创性门槛                     |
| `jie-literature-positioning`       | 对照贸易或开放经济前沿确立贡献                                |
| `jie-identification-strategy`      | 贸易（引力、政策冲击）与开放经济宏观的可信识别                  |
| `jie-data-analysis`                | 实证规范：PPML 引力、面板、结构估计、稳健性                     |
| `jie-contribution-framing`         | 面向 JIE 读者框定"动机或建模结构"的原创性                      |
| `jie-tables-figures`               | 贸易/宏观图表，自洽的图表注释                                 |
| `jie-writing-style`                | JIE 体例；150 词摘要；理论与实证的平衡                         |
| `jie-replication-and-data-policy`  | 向 JIE 安全仓库（Mendeley Data）强制存放代码 + 数据            |
| `jie-review-process`               | JIE 的处理、审稿与 PRP 加速通道如何运作                        |
| `jie-submission`                   | Editorial Manager 投稿前检查：费用、摘要、关键词、类型、编辑匹配 |
| `jie-rebuttal`                     | 面向贸易 / 开放经济审稿人的 R&R 修改回复策略                   |

### 附属资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 贸易数据（Comtrade、BACI、CEPII 引力、WITS）+ 国际宏观/金融数据（IMF IFS/BOP、BIS、EWN、Penn World Table）+ Stata / R / Python / Dynare 工具
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 本包当前流程事实背后的 JIE / Elsevier 官方 URL

---

## 关于这个仓库不做什么

- 不替你写出可以直接投稿的稿件
- 不模拟任何特定 editor 或审稿人的偏好
- 不把易变元数据（现任编辑、确切投稿费、复制材料规则、投稿入口）当成永久事实——正式投稿前请到官网复核
- 不评判你的动机或模型是否真有原创性——这是研究者本人的判断

---

## 相关仓库

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊 Skill 索引
- [Journal of International Economics（官网）](https://www.sciencedirect.com/journal/journal-of-international-economics) —— Elsevier

---

## License

MIT
