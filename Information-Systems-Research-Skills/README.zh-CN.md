# Information Systems Research (ISR) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Information Systems Research 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ISR-1b3a6b)](https://pubsonline.informs.org/journal/isre)
[![Index](https://img.shields.io/badge/index-Basket%20of%20Eight%20%7C%20INFORMS-1f6feb)](https://pubsonline.informs.org/journal/isre)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Information Systems Research (ISR)** 投稿的 Agent 技能栈 —— ISR 是由 **INFORMS**（运筹学与管理科学学会）出版的季刊，立足于技术、组织、经济与社会的交叉地带，是信息系统（IS）领域 **资深学者"八刊篮子"（Senior Scholars' Basket of Eight）** 成员之一。

本仓库是有立场的。它**不是**通用的"信息系统写作"工具箱，而是围绕 ISR 的核心身份打造的 **ISR 专用**技能栈：一份明确的 **社会技术（sociotechnical）** 与 **跨学科内（intradisciplinary）** 使命，在同一本期刊内将 **严谨的行为/实证研究** 与 **解析式经济、计量与设计科学建模** 并列为 **同等地位的一流体裁**。覆盖范围包括：以契合度驱动的选题、行为假设或解析命题的机制构建、**打通 IS 内部各"竖井"** 的文献定位、多方法研究设计与分析、强制性的约 500 词贡献声明、符合 INFORMS 体例的图表与文风、含编辑/审稿人提名的 ScholarOne 投稿、由资深编辑（Senior Editor）主导的评审流程，以及 R&R 答复。

> 先写持久规范。当前页数上限、编辑/审稿人提名数量、评审模式、ORCID 要求与 Open Option 费用已在 2026-06-20 用 INFORMS 官方页面刷新；上传前仍请重新检查 ISR 投稿指南。

---

## 为什么需要单独的 ISR 技能栈？

相比单一范式期刊或通用管理学期刊，ISR 的约束有本质差异：

| 约束维度       | Information Systems Research (ISR)                          | 含义                                                       |
|----------------|------------------------------------------------------------|------------------------------------------------------------|
| 学科           | 立足技术–组织–经济–社会交叉的信息系统                        | "IT 当背景"或通用参照学科的文章不契合                        |
| 核心身份       | **社会技术** 与 **跨学科内**（"打通 IS 竖井"）               | 单一范式贡献弱于打通竖井的贡献                              |
| 体裁           | 行为实证 **与** 解析/经济及设计科学，**同等地位**            | 技能须同等服务于建模与行为研究                              |
| IT 人造物      | 必须承担实质性的理论作用                                     | 若换成任何工具都成立，则尚不构成 IS 贡献                    |
| 篇幅           | 正文 **32 页**、全文 **38 页**；溢出 → 电子伴随材料           | 比许多同行更严；证明/题项放到线上                          |
| 摘要           | 最多 **300 词**                                             | 开门见山讲贡献                                              |
| 评审           | **双向匿名**；由 **资深编辑主导**，并设主编契合度筛查        | 审稿人提供建议，资深编辑做决定                              |
| 投稿信         | **约 500 词贡献声明**（2023-06-01 起）+ **编辑/审稿人提名**   | 套话或缺失的声明会被退回                                    |
| 体例           | 双倍行距、≥11 号字、四边 1 英寸页边距；INFORMS 著者–年份制   | 具体规定请核实                                              |
| 出版方         | **INFORMS**（运筹学/经济学血统），季刊                       | 在行为类期刊中少见的运筹/经济学传承                        |

通用的"科研写作"或"社科方法"技能包无法覆盖这些约束。

---

## 快速上手

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/isr-skills
/plugin install isr-skills
/reload-plugins
```

### 方式 B —— 手动拷贝

```bash
git clone https://github.com/brycewang-stanford/isr-skills.git
cd isr-skills

mkdir -p ~/.claude/skills && cp -R skills/isr-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/isr-* ~/.codex/skills/
```

### 第一条指令

```
用 isr-workflow 告诉我，我的 ISR 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
isr-topic-selection
        ▼
isr-theory-development
        ▼
isr-literature-positioning
        ▼
isr-methods
        ▼
isr-data-analysis
        ▼
isr-contribution-framing
        ▼
isr-tables-figures
        ▼
isr-writing-style        （打磨）
        ▼
isr-submission
        ▼
isr-review-process
        ▼
isr-rebuttal
```

`isr-workflow` 是路由器 —— 它会根据你当前所处的阶段，以及你的论文属于行为、解析、设计科学还是多方法体裁，告诉你下一步该用哪个技能。

---

## 技能一览

| 技能                         | 用途                                                                             |
|------------------------------|----------------------------------------------------------------------------------|
| `isr-workflow`               | 路由器 —— 决定下一步调用哪个子技能；熟悉 ISR 的并列体裁                            |
| `isr-topic-selection`        | 社会技术/跨学科内契合度检验 + 体裁选择（对比 MISQ/JMIS/MS）                       |
| `isr-theory-development`     | 行为假设 **或** 解析命题，始终以 IT 人造物为中心                                  |
| `isr-literature-positioning` | 加入某条 IS 学术对话；打通行为/经济/设计科学竖井                                  |
| `isr-methods`                | 将体裁（行为/解析/设计科学/多方法）与问题匹配                                     |
| `isr-data-analysis`          | 识别与效度（实证）、证明的严谨性（解析）、设计科学评估                            |
| `isr-contribution-framing`   | 明确的 IS 贡献 + 强制性的约 500 词贡献声明                                        |
| `isr-tables-figures`         | INFORMS 体例图表；在页数上限下做正文与电子伴随材料的拆分                          |
| `isr-writing-style`          | 前置贡献、先讲直觉再上代数、INFORMS 著者–年份体例                                 |
| `isr-submission`             | ScholarOne 投稿前检查：匿名化、贡献声明、编辑提名                                 |
| `isr-review-process`         | 主编契合度筛查与资深编辑主导流程；读懂决定信                                      |
| `isr-rebuttal`               | 多轮 R&R 修改与逐条回应资深编辑                                                   |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— IS 数据源（平台/痕迹数据、Compustat/CiTDB、Qualtrics/Prolific）与两类体裁的软件（解析用 Mathematica/MATLAB/Gurobi；实证用 Stata/R/Mplus/SmartPLS；设计科学评估工具）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条已写入当前事实及其 INFORMS/ISR 官方链接，2026-06-20 刷新

---

## 与 MISQ / JMIS / Management Science 的差异

| 维度               | ISR                                          | MISQ                              | JMIS                          | Management Science                 |
|--------------------|----------------------------------------------|-----------------------------------|-------------------------------|------------------------------------|
| 领域               | IS（社会技术、跨学科内）                       | IS                                | IS                            | 广义管理 / 运筹                    |
| 体裁身份           | 行为 **与** 解析/设计科学并列                  | **设计科学** 身份更强             | IS，体例不同                   | 管理/运筹，非 IS 专属              |
| 出版方             | INFORMS                                       | MISRC / 明尼苏达大学              | Taylor & Francis              | INFORMS                            |
| 费用说明           | INFORMS Open Option 接收后 3,000 美元          | —                                 | —                             | 79 美元原始投稿费（2025 年起）     |

若你的贡献是一个力求进入"设计科学体裁主场"的已构建人造物，可考虑 **MISQ**；若 IS 角度只是附带、内核是通用运筹/经济学，可考虑 **Management Science**。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引

---

## 许可证

MIT
