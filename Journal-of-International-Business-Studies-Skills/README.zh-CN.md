# Journal of International Business Studies (JIBS) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of International Business Studies 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JIBS-1b3a6b)](https://link.springer.com/journal/41267)
[![Index](https://img.shields.io/badge/index-FT50%20%7C%20%231%20IB-1f6feb)](https://www.aib.world/publications/journal-of-international-business-studies/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Journal of International Business Studies (JIBS，国际商务研究期刊)** 投稿的 Agent 技能栈 —— JIBS 是国际商务领域排名第一的旗舰期刊，创刊于 1970 年，由 Palgrave Macmillan（Springer Nature）代表 **国际商务学会（Academy of International Business, AIB）** 出版，是 AIB 的官方会刊。

本仓库是有立场的。它**不是**通用的"管理学写作"工具箱，而是围绕 JIBS 的核心标准打造的 **JIBS 专用**技能栈：稿件必须针对一个真实的**国际商务现象（phenomenon）**，并对**国际商务（IB）理论**做出明确且非增量的贡献，且要把**国家与文化作为分析层次（levels of analysis）**来处理。覆盖范围包括：以现象驱动的选题、跨层次理论构建、在 IB 学术对话中的定位、方法论多元的研究设计、跨国测量等价性与效度、锚定 JIBS "From the Editors" 方法论社论范式的共同方法偏差（CMV）与（动态）内生性的严谨处理、IB 理论贡献的提炼、符合 JIBS Style Guide 的图表与文风、Springer Nature 投稿、双盲评审、DART 数据透明制度，以及多轮 R&R 答复。

> 先写持久规范。当前投稿平台、编辑团队、字数限制、DART 表述与可选 OA APC 已在 2026-06-20 用 Springer/AIB 官方页面刷新；上传前仍请重新检查 JIBS 投稿指南与 Style Guide。

---

## 为什么需要单独的 JIBS 技能栈？

相比通用管理学期刊或单一国家研究，JIBS 的约束有本质差异：

| 约束维度        | Journal of International Business Studies                                  | 含义                                                  |
|-----------------|---------------------------------------------------------------------------|-------------------------------------------------------|
| 学科            | 国际商务（跨国企业、国际化、跨文化管理、国际战略/金融/经济、全球政治经济） | 单一国家的管理学论文不契合                            |
| 核心标准        | 真实的 IB **现象** + 明确、非增量的 **IB 理论**贡献                        | 结果再强、若无 IB 理论推进，仍属不契合                |
| 分析层次        | 国家与文化是**层次**，而非控制变量                                         | 一个国家虚拟变量不等于"国际化"                        |
| 方法            | 范式与方法论**多元**；以严谨度为门槛                                       | 不强制单一方法，但标准极高                            |
| 测量            | **跨国测量等价性**是首要关切                                               | 不做等价性检验就合并多国数据会被惩罚                  |
| 共同方法偏差    | 主动把关 CMV；"补检验后重投"是常规要求                                     | 单一来源同一受访者问卷风险很高                        |
| 内生性          | 针对国际化过程设计点名"**动态内生性**"                                     | 过程型设计须有识别策略                                |
| 方法论社论范式  | 约 28 篇 "From the Editors" 社论构成事实标准                               | 审稿人会直接点名引用                                  |
| 透明度          | **DART** 政策 + 数据可获取性声明（DAS）                                    | 录用时须提供 DAS                                      |
| 体例            | JIBS Style Guide；文章字数目标计入摘要/正文/尾注/参考文献                 | 表、图与在线补充可随后附上                            |
| 流程            | Springer Nature 平台；双盲；按 IB 子领域的领域编辑分流                     | 首轮直接录用几乎闻所未闻                              |

通用的"科研写作"或"社科方法"技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jibs-skills
/plugin install jibs-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/jibs-skills.git
cd jibs-skills

mkdir -p ~/.claude/skills && cp -R skills/jibs-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jibs-* ~/.codex/skills/
```

### 第一条提示词

```
用 jibs-workflow 告诉我，针对我的 JIBS 稿件接下来应该用哪个技能。
```

---

## 默认工作流

```text
jibs-topic-selection
        ▼
jibs-theory-development
        ▼
jibs-literature-positioning
        ▼
jibs-methods
        ▼
jibs-data-analysis
        ▼
jibs-contribution-framing
        ▼
jibs-tables-figures
        ▼
jibs-writing-style        (润色)
        ▼
jibs-submission
        ▼
jibs-review-process
        ▼
jibs-rebuttal
```

`jibs-workflow` 是路由器 —— 它根据你当前所处的阶段，告诉你下一步用哪个技能。

---

## 技能列表

| 技能                          | 用途                                                                  |
|-------------------------------|-----------------------------------------------------------------------|
| `jibs-workflow`               | 路由器 —— 决定下一步调用哪个子技能                                     |
| `jibs-topic-selection`        | 现象驱动的研究问题 + JIBS 契合度检验（国家/文化作为层次）              |
| `jibs-theory-development`     | 跨层次（国家/文化 → 企业/个体）IB 机制与假设构建                       |
| `jibs-literature-positioning` | 加入鲜活的 IB 学术对话；以问题化取代"找空白"                           |
| `jibs-methods`                | 匹配跨国/多层次设计；在设计阶段植入等价性/CMV/内生性                   |
| `jibs-data-analysis`          | 测量等价性、CMV、多层次/动态面板估计、内生性                          |
| `jibs-contribution-framing`   | 明确、非增量的 IB 理论贡献 + 社会影响框定                              |
| `jibs-tables-figures`         | 国家覆盖、等价性汇总、跨层次交互图（符合 Style Guide）                 |
| `jibs-writing-style`          | 现象前置的行文、严谨的跨文化表述、Article/Research Note 字数预算       |
| `jibs-submission`             | Springer Nature 投稿前检查：匿名化、DART/DAS、格式、文件              |
| `jibs-review-process`         | JIBS 桌面初筛/双盲/领域编辑评审如何运作；如何解读决定信                |
| `jibs-rebuttal`               | 多轮 R&R 修改与逐条回复信                                              |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) —— 跨国数据（Hofstede/GLOBE、World Bank/WGI、Orbis、SDC、fDi Markets）与分析/测量等价性软件（Mplus / R lavaan + semTools / Stata / 动态面板 GMM / fsQCA）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条已写入当前事实背后的 JIBS/AIB/Springer 官方 URL，2026-06-20 刷新

---

## 与 AMJ / SMJ / JWB 的区别

| 维度           | JIBS                                   | AMJ                          | SMJ                          | JWB / MIR / IBR              |
|----------------|----------------------------------------|------------------------------|------------------------------|------------------------------|
| 学科           | **国际商务**                           | 通用管理学                   | 战略 / 绩效                  | IB 相邻领域                  |
| 核心贡献       | IB **现象 + IB 理论**                  | 实证 **+** 理论              | 竞争优势                     | 扎实但更窄                   |
| 国家/文化      | 作为**分析层次**                       | 常作控制变量                 | 常作控制变量                 | 不一                        |
| 重点审查       | 测量等价性、CMV、（动态）内生性        | CMB、内生性、效度            | 内生性（档案数据）           | 不一                        |

如果你的研究没有真实的跨境、多国，或国家/文化作为层次的维度，JIBS 很可能不是合适的投稿对象。

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 各期刊专用技能包索引

---

## 许可证

MIT
