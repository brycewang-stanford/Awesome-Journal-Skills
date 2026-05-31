# Journal of Finance Skills（JF 技能包）

<p align="center">
  <img src="assets/cover.svg" alt="The Journal of Finance 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Journal%20of%20Finance-0b3d5c)](https://afajof.org/)
[![Index](https://img.shields.io/badge/index-SSCI-1f6feb)](https://afajof.org/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **The Journal of Finance (JF)** 投稿的智能体技能栈 —— JF 是美国金融学会（American Finance Association, AFA）的旗舰**综合性**金融学期刊，由 Wiley 出版。

本仓库是**有立场的**，并非通用的金融写作工具箱，而是一套**JF 专属**技能栈，覆盖：综合性选题、文献定位、（公司/实证方向的）因果识别与（资产定价方向的）实证检验设计、含多重检验纪律的稳健性、期刊托管的 Internet Appendix（在线附录）、易读的行文表达、经 Manuscript Central / ScholarOne 投稿、严苛的多轮审稿流程，以及 R&R 回复信。

> 准确性说明：本技能包描述的是**持久性规范**，而非易变的具体数值。投稿费、AFA 会员规则、编委名单、格式上限等请务必以 JF / AFA 官方作者页面的当前信息为准。

---

## 为什么要为《Journal of Finance》单独建一套技能栈？

JF 的约束与 JFE、RFS 及领域期刊存在实质差异：

| 约束维度            | The Journal of Finance                                  | 含义                                              |
|---------------------|----------------------------------------------------------|---------------------------------------------------|
| 读者群             | 覆盖金融各领域的广泛 AFA 读者                              | 仅面向某一子领域的论文易被筛掉，"综合性"是门槛       |
| 范围               | 资产定价、公司金融、市场微观结构、银行、家庭金融、国际金融 | 纯方法或纯理论论文常更适合 JFE/RFS                  |
| 贡献               | 重要且具广泛兴趣的问题 + 经济显著性                        | 仅有统计显著性无法过关                              |
| 识别（公司/实证）  | 自然实验、可辩护排他性的 IV、现代 DID、断点回归            | OLS + 控制变量却不处理内生性是危险信号              |
| 检验设计（资产定价）| 因子模型、Fama–MacBeth/面板、正确标准误、多重检验          | 从信号搜索中得到的朴素 t > 2 会被视为数据挖掘        |
| 篇幅与风格         | 相对更短、易读；技术深度移入 Internet Appendix             | 冗长、技术堆砌、淹没主结果的论文会招致批评          |
| Internet Appendix  | 期刊托管；证明与额外表格放在线上                            | 正文保持聚焦；附录条目必须被正文引用                |
| 流程               | Manuscript Central / ScholarOne；投稿费 + AFA 会员规范     | 请核实当前费用/会员要求；预期多轮审稿                |

通用的"科学写作"或"经济学写作"技能包无法覆盖上述约束。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jf-skills
/plugin install jf-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/jf-skills.git
cd jf-skills

mkdir -p ~/.claude/skills && cp -R skills/jf-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jf-* ~/.codex/skills/
```

### 第一条提示词

```
用 jf-workflow 告诉我，我的 Journal-of-Finance 稿件下一步应该用哪个技能。
```

---

## 默认工作流

```text
jf-topic-selection
        ▼
jf-literature-positioning
        ▼
jf-identification        （公司 / 实证分支）
   或 jf-empirical-design （资产定价分支）
        ▼
jf-robustness
        ▼
jf-tables-figures
        ▼
jf-internet-appendix
        ▼
jf-writing-style         （润色）
        ▼
jf-submission
        ▼
jf-referee-strategy
        ▼
jf-rebuttal
```

`jf-workflow` 是路由器 —— 它根据你所处阶段告诉你下一步该用哪个技能。`jf-identification` 与 `jf-empirical-design` 是分支兄弟：前者用于公司/实证的因果主张，后者用于资产定价检验。

---

## 技能清单

| 技能                          | 用途                                                              |
|------------------------------|-------------------------------------------------------------------|
| `jf-workflow`                | 路由器 —— 决定下一步调用哪个子技能                                  |
| `jf-topic-selection`         | 综合性契合度 + 经济显著性框定                                       |
| `jf-literature-positioning`  | 相对金融文献的边际贡献定位                                          |
| `jf-identification`          | 因果识别（自然实验 / IV / DID / 断点回归）                          |
| `jf-empirical-design`        | 资产定价检验设计（因子、Fama–MacBeth、标准误校正）                  |
| `jf-robustness`              | 稳健性矩阵 + 多重检验 / 样本外纪律                                  |
| `jf-tables-figures`          | 干净、自洽、可发表级别的图表                                        |
| `jf-internet-appendix`       | 线上 vs. 正文的内容分配；附录结构                                   |
| `jf-writing-style`           | 易读的综合性行文；先讲清经济量级                                    |
| `jf-submission`              | 投稿前 preflight（投稿系统、费用/会员、格式、声明）                 |
| `jf-referee-strategy`        | 预判审稿人异议；推荐/回避审稿人                                     |
| `jf-rebuttal`                | R&R 回复信结构与修订计划                                            |

### 资源

- [`skills/jf-submission/templates/manuscript_template.md`](skills/jf-submission/templates/manuscript_template.md) —— JF 取向的稿件骨架（标题页、正文、Internet Appendix、参考文献）
- [`skills/jf-submission/templates/checklist.md`](skills/jf-submission/templates/checklist.md) —— 8 类投稿前自检清单
- [`resources/external_tools.md`](resources/external_tools.md) —— 实证金融数据源（CRSP / Compustat / TAQ / WRDS / Refinitiv）+ Stata / R / Python 软件包

---

## 与 JFE / RFS 的差异

| 维度        | Journal of Finance              | JFE                              | RFS                               |
|-------------|---------------------------------|----------------------------------|-----------------------------------|
| 侧重        | 综合性、易读                     | 深度、方法分量                    | 理论框定 + 机制                    |
| 篇幅        | 相对更短；深度放线上              | 容忍更长、更技术                  | 常以理论为锚                       |
| 最佳契合    | 广泛感兴趣的发现                 | 专门化、方法导向的论文            | 结构化 / 机制贡献                  |
| 技术细节    | 移入 Internet Appendix          | 更多保留在正文                    | 模型驱动                          |

若你的论文冗长、技术性强或高度专门化，JFE 或 RFS 可能是更合适的归宿。

---

## 相关项目

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属技能包索引
- [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) —— 《经济研究》

---

## 许可证

MIT
