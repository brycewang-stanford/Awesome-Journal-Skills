# 美国经济学杂志：宏观经济学 技能包（AEJ: Macroeconomics Skills）

<p align="center">
  <img src="assets/cover.svg" width="200" alt="AEJ: Macroeconomics Skills 封面">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License: MIT">
  <img src="https://img.shields.io/badge/journal-AEJ%3A%20Macro-1f5135" alt="Journal: AEJ: Macro">
  <img src="https://img.shields.io/badge/publisher-AEA-1f5135" alt="Publisher: AEA">
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-blue" alt="Claude Code plugin">
</p>

<p align="center"><a href="README.md">English</a> | 简体中文</p>

面向 **《美国经济学杂志：宏观经济学》（American Economic Journal: Macroeconomics, AEJ: Macro）** 投稿的
十二个智能体技能。AEJ: Macro 是美国经济学会（AEA）旗下季刊、面向广义宏观读者的期刊（创刊于 2009 年，
四本 AEJ 之一）。本技能包紧扣 AEJ: Macro 的核心特征——它**同时**欢迎定量理论研究（DSGE、异质主体/HANK、
结构估计）**与**有识别的实证研究（SVAR、局部投影、叙事识别与高频识别），评判标准是**定量上的严谨性与
政策相关性**。它内化了 AEA 的投稿流程：按会员资格与国家收入分级的投稿费、单盲评审、JEL 代码、≤100 词
摘要、约 40 页的篇幅指引、每位合作者单独的利益披露，以及由 AEA 数据主编在**发表前**完成的可复现性
检查（涵盖模拟与模型求解代码），最终材料存放于 openICPSR 上的 AEA Data and Code Repository。

**官方依据核对于 2026-06：** AEJ: Macro 的投稿指南、编辑政策与编辑名单页；AEA 数据与代码可得性政策及
AEA 数据主编办公室页；AEA 利益披露政策。详见
[`resources/official-source-map.md`](resources/official-source-map.md)。易变事实（费用、版面费、编辑、
篇幅指引、政策生效日期）均标注「检索于 2026-06；以官网为准」——在依赖具体数字前请到 AEA 官网核实。

## 为什么需要单独的技能包？

AEJ: Macro 既非综合性旗舰，也非细分领域刊物，其流程含有通用经济学技能包会忽略的宏观特有陷阱：

| 约束 | AEJ: Macro 的具体要求 | 通用技能包为何失效 |
|---|---|---|
| 方法学广度 | 定量理论（DSGE/HANK）与有识别实证（SVAR/LP/叙事）均在范围内 | 纯实证或纯结构的技能包会错框一半的期刊 |
| 广义读者门槛 | 决策权衡选题广度 + 对 AEJ: Macro 读者的吸引力 | 细分领域式框定会读起来像 JME/RED |
| 摘要长度 | ≤100 词（硬性） | 多数技能包假设 150–250 词 |
| 篇幅指引 | 约 40 页（11pt）/ 45 页（12pt），含图表、参考文献与附录 | 通用技能包忽略版面预算与在线附录分流 |
| 评审模式 | 单盲（作者对审稿人可见） | 假设双盲匿名的技能包会误导 |
| 可复现性 | AEA 数据主编在**发表前**检查；需提供**模拟/求解代码** | 仅打包回归脚本的技能包通不过宏观检查 |
| 利益披露 | **每位合作者**单独声明；1 万美元门槛 | 单一声明的假设会漏掉硬性要求 |

## 快速开始

**作为 Claude Code 插件（推荐）。** 添加市场并安装：

```
/plugin marketplace add brycewang-stanford/aej-macroeconomics-skills
/plugin install aej-macroeconomics-skills
```

随后即可发问，例如「用 aejmac-workflow：我的 HANK 论文收到 R&R，下一步怎么办？」路由技能会指向合适的子技能。

**手动使用。** 将本目录拷入你的项目，让智能体指向 `skills/<名称>/SKILL.md`。请从路由技能
[`skills/aejmac-workflow/SKILL.md`](skills/aejmac-workflow/SKILL.md) 开始。

## 默认工作流

```
aejmac-workflow（路由）
   │
   ▼
topic-selection → literature-positioning → identification ─┐
                                          theory-model ────┤→ robustness → tables-figures
                                                           │
   writing-style → replication-package → referee-strategy → submission → rebuttal
```

> `identification`（实证）与 `theory-model`（定量）是并列关系：实证论文侧重前者，定量论文侧重后者，
> 混合型论文两者皆需。

## 技能清单

| # | 技能 | 何时使用 |
|---|------|----------|
| 1 | [`aejmac-workflow`](skills/aejmac-workflow/SKILL.md) | 从选题契合度到投稿与 R&R 的路由 |
| 2 | [`aejmac-topic-selection`](skills/aejmac-topic-selection/SKILL.md) | 判断该投 AEJ: Macro 还是 AER、JME、RED、AEJ: Applied |
| 3 | [`aejmac-literature-positioning`](skills/aejmac-literature-positioning/SKILL.md) | 相对理论与实证前沿确立边际贡献 |
| 4 | [`aejmac-identification`](skills/aejmac-identification/SKILL.md) | 压力测试 SVAR / LP / 叙事 / 高频识别 |
| 5 | [`aejmac-theory-model`](skills/aejmac-theory-model/SKILL.md) | 规范 DSGE / HANK / 结构模型：校准、识别、数值 |
| 6 | [`aejmac-robustness`](skills/aejmac-robustness/SKILL.md) | 证明核心数字在样本、设定、方法选择下稳健 |
| 7 | [`aejmac-tables-figures`](skills/aejmac-tables-figures/SKILL.md) | 按 AEA 与宏观惯例制作脉冲响应、扇形图、模型拟合图 |
| 8 | [`aejmac-writing-style`](skills/aejmac-writing-style/SKILL.md) | 写好广义读者导言弧线与 ≤100 词摘要 |
| 9 | [`aejmac-replication-package`](skills/aejmac-replication-package/SKILL.md) | 为 AEA 数据主编组装 openICPSR 包（含模拟/求解代码） |
| 10 | [`aejmac-referee-strategy`](skills/aejmac-referee-strategy/SKILL.md) | 预先化解宏观审稿人会提的异议；评估直拒风险 |
| 11 | [`aejmac-submission`](skills/aejmac-submission/SKILL.md) | AEA 系统投稿前终检：费用分级、摘要、JEL、披露 |
| 12 | [`aejmac-rebuttal`](skills/aejmac-rebuttal/SKILL.md) | R&R 之后撰写回复信与修改计划 |

## 资源

- [`resources/README.md`](resources/README.md) —— 能力层索引。
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的 AEA 官方链接。
- [`resources/external_tools.md`](resources/external_tools.md) —— 数据来源与宏观工具链（FRED/ALFRED、Dynare、序列空间雅可比、SVAR/LP 包）。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— 一篇虚构的 AEJ: Macro 导言「修改前→修改后」示例。
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 按方法 × 主题整理的、经网络核实的真实 AEJ: Macro 论文。
- [`resources/code/`](resources/code/) —— 内置的实证方法代码骨架（对宏观仅为*起点*，需自行补充 SVAR/LP/DSGE 代码）。

## 与兄弟期刊的差异

| 期刊 | 定位 | 本技能包的立场 |
|---|---|---|
| **AEJ: Macro** | 广义宏观；定量理论**与**有识别实证；AEA 流程 | 本技能包的目标刊 |
| **AER** | 顶级综合刊；一阶、更长篇幅 | 能重塑领域共识的成果投 AER；AEJ: Macro 高水平但非旗舰 |
| **J. Monetary Economics** | 面向专家的细分宏观深度 | 若广度不足，JME 更合适 |
| **RED** | 面向宏观方法社区的定量动态/方法 | 纯动态一般均衡方法论文更适合 RED |
| **AEJ: Applied** | 微观实证、识别导向 | 触及总量的微观论文更适合 AEJ: Applied |

## 相关链接

- 参考技能包：`../Quantitative-Economics-Skills/`（计量经济学会，结构完全一致）。
- 共享方法中枢：[`../shared-resources/empirical-methods/`](../shared-resources/empirical-methods/)。

## 许可证

MIT © 2026 Bryce Wang。详见 [LICENSE](LICENSE)。
