# 《金融与定量分析期刊》技能包（JFQA Skills）

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Financial and Quantitative Analysis 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JFQA-0f3d5c)](https://jfqa.org/)
[![Field](https://img.shields.io/badge/field-%E5%AE%9E%E8%AF%81%E4%B8%8E%E5%AE%9A%E9%87%8F%E9%87%91%E8%9E%8D-1f6feb)](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向投稿 **《金融与定量分析期刊》（Journal of Financial and Quantitative Analysis, JFQA）** 的 Agent 技能栈。JFQA 是**实证与定量金融经济学**的重要期刊，由 **剑桥大学出版社（Cambridge University Press）** 代表 **华盛顿大学 Michael G. Foster 商学院** 出版。

本仓库是有明确取向的，**不是**通用金融写作工具箱，而是一个**专为 JFQA 定制**的技能栈，围绕该刊真实的研究范围与流程：公司金融、投资与资产定价、资本与证券市场、金融机构，以及与金融相关的定量方法——强调可信的研究设计、符合金融惯例的图表、JFQA 的版式规范，以及强制性的 **JFQA 代码共享政策（JFQA Code Sharing Policy）** 存档要求。

> 易变的具体信息（编辑、费用、退款、版式、代码政策、投稿网址）请以官网为准——它们会变化。凡无法从官方来源确认的事实，均在 [`resources/official-source-map.md`](resources/official-source-map.md) 中标注 **待核实**。

---

## 为什么需要专门的 JFQA 技能栈？

JFQA 的约束与顶级经济学旗刊或方法类期刊存在实质差异：

| 约束维度       | JFQA                                                                 | 含义                                                       |
|----------------|----------------------------------------------------------------------|------------------------------------------------------------|
| 研究范围       | 实证与定量**金融**（公司金融、投资、市场、金融机构）                   | 偏离金融或纯描述性的论文不契合                             |
| 投稿系统       | **Editorial Manager**（需单独账号）                                   | 并非 ScholarOne / Editorial Express                        |
| 投稿费         | **$350**，仅限信用卡；若未送审则退 **$275**                           | 即便被桌拒也要扣 **$75**——需预留预算                       |
| 评审模式       | **双向匿名（double-anonymous）**                                      | 需对正文与 PDF 元数据彻底匿名                              |
| 摘要           | 单段，**不超过 100 词**                                               | 比多数金融/经济旗刊更严——务必精简                         |
| 版式           | 8.5×11、1 英寸页边距、12 号 Times New Roman、双倍行距、可检索 PDF      | 规定严格；版式错误即扣分                                   |
| 录用率         | 每年 1000+ 投稿中**印刷率不足 9%**                                    | 干净、识别可信的稿件才能过初筛                             |
| 重投规则       | 未披露的此前拒稿 → 桌拒**并禁投一年**                                 | 须在投稿信中披露此前 JFQA 拒稿                             |
| 代码/数据政策  | **JFQA 代码共享政策**；哈佛 Dataverse 下的 **JFQA Dataverse**         | 2024 年起新投稿一经录用即强制；并有随机核验                |
| 领导结构       | **七位 Managing Editors**，无单一主编                                 | 每篇稿件指派一位 Managing Editor 处理                      |

通用的“科学写作”或“经济学写作”技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jfqa-skills
/plugin install jfqa-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/jfqa-skills.git
cd jfqa-skills

mkdir -p ~/.claude/skills && cp -R skills/jfqa-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jfqa-* ~/.codex/skills/
```

### 第一条提示

```
用 jfqa-workflow 告诉我，我的 JFQA 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
jfqa-topic-selection            选题契合
        ▼
jfqa-literature-positioning     文献定位
        ▼
jfqa-identification-strategy    识别/研究设计
        ▼
jfqa-data-analysis              实证分析
        ▼
jfqa-contribution-framing       贡献与 ≤100 词摘要
        ▼
jfqa-tables-figures             图表
        ▼
jfqa-writing-style              （润色）
        ▼
jfqa-replication-and-data-policy 代码/数据存档
        ▼
jfqa-review-process             评审流程
        ▼
jfqa-submission                 投稿前检查
        ▼
jfqa-rebuttal                   返修回应
```

`jfqa-workflow` 是路由器——根据你所处阶段，告诉你下一步该用哪个技能。

---

## 技能清单

| 技能                                | 用途                                                                 |
|-------------------------------------|----------------------------------------------------------------------|
| `jfqa-workflow`                     | 路由器——决定下一步调用哪个子技能                                     |
| `jfqa-topic-selection`              | 实证/定量金融的范围契合度与录用门槛                                   |
| `jfqa-literature-positioning`       | 针对金融前沿确立贡献（不做独立综述）                                  |
| `jfqa-identification-strategy`      | 可信的金融研究设计（组合排序/FMB、面板 FE、DID、IV、RDD、事件研究）   |
| `jfqa-data-analysis`                | 金融数据构造、聚类标准误、稳健性、经济意义                           |
| `jfqa-contribution-framing`         | 严格的 ≤100 词摘要与引言中的贡献陈述                                  |
| `jfqa-tables-figures`               | 符合金融惯例、注释自足的图表                                          |
| `jfqa-writing-style`                | 定量金融文风与 JFQA 版式规范                                          |
| `jfqa-replication-and-data-policy`  | JFQA 代码共享政策存档（JFQA Dataverse、原始/伪数据）                  |
| `jfqa-review-process`               | 双向匿名评审、七位 Managing Editors、费用/退款、录用概率             |
| `jfqa-submission`                   | Editorial Manager 投稿前检查 + 稿件模板                              |
| `jfqa-rebuttal`                     | 返修（R&R）回应信策略                                                |

### 资源文件

- [`skills/jfqa-submission/templates/manuscript_template.md`](skills/jfqa-submission/templates/manuscript_template.md) — JFQA 稿件骨架（≤100 词摘要、引言结构、设计、图表）
- [`skills/jfqa-submission/templates/checklist.md`](skills/jfqa-submission/templates/checklist.md) — 8 节投稿前自查清单
- [`resources/external_tools.md`](resources/external_tools.md) — 金融数据源（CRSP / Compustat / TAQ / IBES / WRDS）与 Stata / R / Python 工具包
- [`resources/official-source-map.md`](resources/official-source-map.md) — 每条事实背后的 JFQA 官方网址，并标注 **待核实**

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件。
- 不模拟某位具体 Managing Editor 或审稿人的口味。
- 不把易变信息（现任编辑、确切费用、存档规则）当作永久事实——请以官网为准。
- 不评判你的金融贡献是否真正原创——这是研究者自己的判断。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [JFQA 投稿页（官方）](https://jfqa.org/submissions/) — 费用、版式、重投规则
- [JFQA 代码共享政策（官方）](https://jfqa.org/jfqa-code-sharing-policy/) — 存档要求
- [JFQA on Cambridge Core](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis) — 作者须知、双向匿名评审

---

## 许可证

MIT
