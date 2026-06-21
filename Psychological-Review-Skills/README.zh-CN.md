# Psychological Review（《心理学评论》）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Psychological Review 期刊封面" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Psychological%20Review-6a2a2a)](https://www.apa.org/pubs/journals/rev)
[![Index](https://img.shields.io/badge/index-American%20Psychological%20Association-1f6feb)](https://www.apa.org/pubs/journals/rev)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **Psychological Review（《心理学评论》）** 投稿的 Agent 技能栈。它是美国心理学会（APA）旗下专门发表**理论性贡献**的旗舰期刊，刊登新的理论框架、形式化／数学／计算**模型**，以及重大的理论综合，覆盖认知、知觉、学习、发展、社会心理与神经科学。它**不发表原始实证报告**——数据只用于**引出问题**或**约束理论**。

本仓库是高度专门化的，**不是**通用的心理学写作工具箱，也**不是**实证心理学技能栈。它是一套**专属于 Psychological Review 的理论构建**技能栈，覆盖：理论契合度筛查、理论问题的提出、形式化／概念模型的构建、相对竞争模型的定位、预测的推导与对照、范围与边界条件（含可识别性）、模型图与"模型行为模拟"图、贡献差异化、APA 体例，以及通过 Editorial Manager 的盲审。

**官方依据核于 2026-06**（易变信息请以 APA 官网为准；检索于 2026-06；以官网为准）。

---

## 为什么需要单独的 Psychological Review 技能栈？

相比实证心理学期刊（JEP 系列、Psychological Science），Psychological Review 的约束有本质不同：

| 约束                | Psychological Review                                   | 含义                                                |
|---------------------|--------------------------------------------------------|-----------------------------------------------------|
| 交付物              | 新**理论**或**形式化／计算模型**                        | 带数据的实证研究不契合，应投 JEP / Psychological Science |
| 数据                | 仅用于**引出问题或约束理论**                            | 没有作者自己的方法或结果部分                        |
| 核心单元            | 模型**推导出的、可证伪的预测**                          | 不是用新样本检验的假设                              |
| 严谨标准            | 逻辑与形式上的**严密性**                                | 推导／模拟在此处等同于实证期刊里的统计              |
| 定位                | 击败或涵盖**具名的竞争模型**                            | 没有点名竞争模型的主题综述会失败                    |
| 范围                | 明确的边界 + （形式化模型的）**可识别性**               | "能解释一切"会被读作不可证伪                        |
| 图                  | 模型图 + 模型行为模拟图                                 | 没有实验图——每个方框是构念，每条曲线是模拟          |
| 贡献                | 相对前作的差异化"之前 → 之后"                           | 换标签或仅拟合更好都是拒稿信号                      |
| 计算模型            | 共享作者**自己的模型代码**                              | 不是共享的实证分析工具包；没有数据集可存放          |
| 评审                | 盲审、多轮（Editorial Manager）                         | 评审人通常正是竞争模型的作者                        |

通用的"科研写作"或实证心理学技能包都无法处理这些约束。

> 准确性说明：编辑、确切的篇幅／摘要字数限制、投稿门户 URL、费用、APA 版次等会随时间变化。投稿前请到 **Psychological Review / APA 官方作者页面核实所有门户阶段的具体信息**。

---

## 快速开始

### 方式 A —— Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/psychological-review-skills
/plugin install psychological-review-skills
/reload-plugins
```

### 方式 B —— 手动复制

```bash
git clone https://github.com/brycewang-stanford/psychological-review-skills.git
cd psychological-review-skills

mkdir -p ~/.claude/skills && cp -R skills/psychrev-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/psychrev-* ~/.codex/skills/
```

### 第一条提示

```
请用 psychrev-workflow 告诉我，针对我的 Psychological Review 稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
psychrev-topic-selection
        ▼
psychrev-literature-positioning
        ▼
psychrev-theory-construction
        ▼
psychrev-argument-development     （推导预测；对照数据与竞争模型）
        ▼
psychrev-boundary-conditions      （范围、可识别性、不能解释什么）
        ▼
psychrev-conceptual-exhibits      （模型图 + 模拟图）
        ▼
psychrev-contribution-framing
        ▼
psychrev-writing-style            （润色）
        ▼
psychrev-submission
        ▼
psychrev-review-process
        ▼
psychrev-rebuttal
```

`psychrev-workflow` 是路由器——它根据你所处的阶段告诉你下一步该用哪个技能。

---

## 技能清单

| 技能                            | 用途                                                                      |
|---------------------------------|---------------------------------------------------------------------------|
| `psychrev-workflow`             | 路由器——决定下一步调用哪个子技能                                          |
| `psychrev-topic-selection`      | 是否存在真正的理论问题，且属于理论（而非实证）？                          |
| `psychrev-theory-construction`  | 构建假设、机制、形式化结构与推导出的行为                                  |
| `psychrev-literature-positioning`| 点明你拓展的理论与必须击败的竞争模型                                     |
| `psychrev-argument-development` | 推导预测；对照已有数据与竞争模型                                          |
| `psychrev-boundary-conditions`  | 范围、可识别性／参数恢复／模型仿冒、理论不能解释什么                      |
| `psychrev-conceptual-exhibits`  | 模型／架构图 + 模型行为模拟图                                            |
| `psychrev-writing-style`        | APA 体例；以机制为先、用模型词汇的文风（润色）                            |
| `psychrev-contribution-framing` | 相对具名前作的差异化（"之前 → 之后"）                                     |
| `psychrev-review-process`       | 盲审、Theoretical Notes，以及理论期刊特有的质疑                          |
| `psychrev-submission`           | Editorial Manager 投稿前检查 + 清单（格式、盲审、模型代码）              |
| `psychrev-rebuttal`             | 修订 + 回复文档，证明理论本身确实被加强                                  |

### 资源

- [`skills/psychrev-submission/templates/checklist.md`](skills/psychrev-submission/templates/checklist.md) —— 8 节投稿前自查（范围／格式／盲审／摘要／理论／图与代码／参考文献／伦理与门户）
- [`resources/external_tools.md`](resources/external_tools.md) —— 理论／建模工具（建模环境、可识别性／恢复分析、绘图软件、论证逻辑辅助）
- [`resources/official-source-map.md`](resources/official-source-map.md) —— APA Psychological Review 的官方范围、格式与门户事实（附核实日期）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 六篇经网络核实的 Psychological Review 理论／模型论文，按形式分类，附姊妹刊辨别防护
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— 虚构的"之前 → 之后"理论引言示例（house style）

---

## 与姊妹期刊的区别

| 维度          | Psychological Review              | Psychological Bulletin        | BBS                        | JEP 系列 / Psych Science |
|---------------|----------------------------------|-------------------------------|----------------------------|--------------------------|
| 交付物        | 新理论 / 形式化模型              | 综述 / 元分析                 | 标靶文 + 公开评议           | 实证报告                 |
| 数据          | 仅引出／约束                     | 综合的证据                    | 论证                       | 即贡献本身               |
| 核心单元      | 推导出的预测                     | 效应量 / 综合                 | 公开评议                   | 受检验的假设             |
| 严谨标准      | 逻辑／形式严密性                 | 综合的严谨                    | 论辩质量                   | 统计严谨                 |
| 图            | 模型图、模拟图                   | 森林图、汇总                  | （不一）                   | 数据图、结果表           |

如果你的贡献是数据、综合或论辩格式，更合适的是其他期刊——Psychological Review 构建那些文献后续去检验和综述的形式化理论。

---

## 相关链接

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) —— 期刊专属技能包索引
- [Academy-of-Management-Review-Skills](https://github.com/brycewang-stanford/amr-skills) —— 一个姊妹的纯理论深度包

---

## 许可证

MIT
