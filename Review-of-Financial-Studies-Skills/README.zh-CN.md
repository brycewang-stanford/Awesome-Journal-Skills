# RFS Skills

<p align="center">
  <img src="assets/cover.svg" alt="The Review of Financial Studies 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Review%20of%20Financial%20Studies-1b2a4a)](https://academic.oup.com/rfs)
[![Index](https://img.shields.io/badge/index-SSCI%20%7C%20top--3%20finance-1f6feb)](https://academic.oup.com/rfs)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **The Review of Financial Studies（RFS，《金融研究评论》）** 投稿的智能体（Agent）技能栈 —— 该刊由牛津大学出版社（OUP）为金融研究学会（SFS）出版，与 *Journal of Finance*、*Journal of Financial Economics* 并称金融学"三大刊"。

本仓库是高度定制化的，**不是**通用金融写作工具箱，而是一套**针对 RFS** 的技能栈，围绕该刊的核心张力 ——**新颖性 与 严谨性 缺一不可**—— 展开，覆盖：以"新问题"为核心的选题、文献定位、因果与资产定价识别、实证/结构设计、稳健性与多重检验纪律、出版级图表、期刊托管的 Internet Appendix（在线附录）、行文风格、ScholarOne 投稿、审稿人策略，以及多轮修回（rebuttal）。

---

## 为什么需要单独的 RFS 技能栈？

RFS 与 JF/JFE 共享同样高的因果识别门槛，但又有自身的约束：

| 约束维度       | The Review of Financial Studies                              | 含义                                                       |
|----------------|---------------------------------------------------------------|------------------------------------------------------------|
| 学科           | 金融（资产定价、公司金融、家庭金融、金融科技、气候金融）        | 纯非金融或理论欠缺的稿件契合度低                            |
| 核心检验       | **新颖性 与 严谨性 —— 两者同时具备**                          | 干净但"跟风"的稿件契合度弱；只有新颖性同样不够             |
| 对新工作的接纳 | 明显欢迎新问题、新数据、新方法，以及理论+实证的融合           | 真正新颖的框架会被奖励，而非惩罚                            |
| 识别           | 与 JF/JFE 同等的因果识别门槛（自然实验、IV、RDD、现代 DID）   | 对因果主张仅用 OLS+控制变量有被直接拒稿的风险             |
| 资产定价       | 正确/聚类标准误、样本外检验、多重检验纪律                     | 不应对数据挖掘质疑的新预测因子会被拒                        |
| 理论+实证      | 被欢迎，且期望二者融合                                        | 一个模型加一个不相关的回归，读起来像两篇论文               |
| 在线附录       | 期刊托管；与正文一同送审                                      | 稳健性/证明/数据细节应放此处，并在正文交叉引用             |
| 流程           | ScholarOne / Manuscript Central；含投稿费 + SFS 规范；多轮审稿 | 修订要求高；请在 RFS 官网核实当前费用与政策                |

通用的"科研写作"或"金融写作"技能包无法覆盖这些约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/rfs-skills
/plugin install rfs-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/rfs-skills.git
cd rfs-skills

mkdir -p ~/.claude/skills && cp -R skills/rfs-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/rfs-* ~/.codex/skills/
```

### 第一条提示词

```
Use rfs-workflow to tell me which skill I should use next for my RFS manuscript.
```

---

## 默认工作流

```text
rfs-topic-selection
        ▼
rfs-literature-positioning
        ▼
rfs-identification
        ▼
rfs-empirical-design
        ▼
rfs-robustness
        ▼
rfs-tables-figures
        ▼
rfs-internet-appendix
        ▼
rfs-writing-style       （润色）
        ▼
rfs-submission
        ▼
rfs-referee-strategy
        ▼
rfs-rebuttal
```

`rfs-workflow` 是路由器 —— 它根据你当前所处阶段告诉你下一步该用哪个技能。

---

## 技能清单

| 技能                          | 用途                                                                |
|-------------------------------|---------------------------------------------------------------------|
| `rfs-workflow`                | 路由器 —— 决定下一步调用哪个子技能                                   |
| `rfs-topic-selection`         | 新颖性+严谨性契合度检验 + 贡献陈述模板                               |
| `rfs-literature-positioning`  | 相对 JF/JFE/RFS 及既有文献界定精确"增量"                            |
| `rfs-identification`          | 因果与资产定价识别（DID / IV / RDD / 事件研究）                      |
| `rfs-empirical-design`        | 样本构造、估计量、因子/结构设计                                      |
| `rfs-robustness`              | 脆弱性检验体系 + 多重检验 / 样本外纪律                               |
| `rfs-tables-figures`          | 自洽表格、标准误报告、事件研究图                                     |
| `rfs-internet-appendix`       | 哪些放入期刊托管的在线附录、哪些留在正文                             |
| `rfs-writing-style`           | 贡献框定 + 行文润色（让新颖性尽早可见）                              |
| `rfs-submission`              | ScholarOne 投稿前检查 + 投稿信 + 稿件模板                            |
| `rfs-referee-strategy`        | 推荐/排除审稿人 + 反对意见预演（pre-mortem）                         |
| `rfs-rebuttal`                | 多轮 R&R 回复信结构                                                  |

### 资源

- [`skills/rfs-submission/templates/manuscript_template.md`](skills/rfs-submission/templates/manuscript_template.md) —— RFS 风格稿件骨架（摘要、章节、变量表、参考文献、在线附录、投稿信）
- [`skills/rfs-submission/templates/checklist.md`](skills/rfs-submission/templates/checklist.md) —— 投稿前 8 类自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 金融数据资源（CRSP / Compustat / TAQ / WRDS / OptionMetrics）+ Stata / R / Python 包速查

---

## 与 JF / JFE Skills 的差异

| 维度           | Review of Financial Studies            | Journal of Finance / JFE                  |
|----------------|-----------------------------------------|-------------------------------------------|
| 识别门槛       | 三大刊级别的因果识别标准                 | 三大刊级别的因果识别标准                  |
| 对新颖性的接纳 | **尤其开放**于新问题/新数据/新方法       | 同样开放，但 RFS 最明确地奖励之           |
| 理论+实证      | 欢迎融合性的结构/理论工作                 | 同样欢迎（JFE）；JF 亦强                   |
| 风格特点       | 期刊托管的在线附录是核心组成             | 类似；各刊细节不同                         |
| 典型风险       | "严谨但不新颖"的跟风稿                   | 同一族风险                                |

这三本刊高度重叠；本技能栈针对 RFS 的核心抓手——**让新颖性变得可信**——进行了调校。

---

## 相关项目

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专用技能包索引
- [Journal-of-Finance-Skills](https://github.com/brycewang-stanford/journal-of-finance-skills) —— *Journal of Finance*
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) —— 《经济研究》

---

## 许可证

MIT
