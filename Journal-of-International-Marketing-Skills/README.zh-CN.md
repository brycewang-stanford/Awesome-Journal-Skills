# Journal of International Marketing Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of International Marketing Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of International Marketing（JIM）** 投稿的 12 个 agent skills。JIM 是美国营销学会（AMA）旗下、由 SAGE 出版的国际营销领域顶级专业期刊（季刊）。本包围绕 JIM 的核心门槛设计：**国际维度必须是论文的理论引擎**，而不是样本标签——需要多国数据、完整的**测量不变性**（measurement invariance）证据链，以及跨境经营企业可以执行的管理启示。它帮助稿件区别于 JIBS、Journal of Marketing 与 International Marketing Review，并预先规避 JIM 的典型 desk-reject 模式（单一国家数据贴"国际"标签、用文化事后解释结果、跨文化量表未做不变性检验）。

**官方依据核验日期：2026-07-16**（投稿前请复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JIM 约束 | 对稿件的要求 |
|----------|--------------|
| 国际维度为理论核心 | 跨境必须生成理论预测；"删除国家名"测试必须让选题失效 |
| 等价性门槛 | 多国量表需要翻译规程与 configural→metric→scalar 不变性阶梯，之后才允许跨国比较 |
| 双重贡献 | 对国际营销理论的增量 **加上** 跨境企业可执行的决策规则 |
| 硬性格式上限 | 全文（含图表、参考文献、附录）不超过 50 页；摘要 200 词、第三人称；ScholarOne 双匿名两文件投稿 |
| 来源纪律 | 易变流程事实标注核验日期（2026-07-16）或明确写"以官网为准" |

## 快速开始

```text
/plugin marketplace add ./Journal-of-International-Marketing-Skills
/plugin install jim-skills
```

手动使用：先打开 [`skills/jim-workflow/SKILL.md`](skills/jim-workflow/SKILL.md)。

## 默认工作流

```text
jim-workflow → jim-topic-selection → jim-theory-development → jim-literature-positioning → jim-methods → jim-data-analysis → jim-contribution-framing → jim-tables-figures → jim-writing-style → jim-submission → jim-review-process → jim-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jim-workflow`](skills/jim-workflow/SKILL.md) | 按稿件当前阶段路由到正确的 jim-* 技能 |
| 2 | [`jim-topic-selection`](skills/jim-topic-selection/SKILL.md) | 检验国际维度是否为理论核心（删国名测试 / 两国预测测试 / 管理者测试） |
| 3 | [`jim-theory-development`](skills/jim-theory-development/SKILL.md) | 事前理论化跨国差异——文化/制度视角、分析层次、假设写作 |
| 4 | [`jim-literature-positioning`](skills/jim-literature-positioning/SKILL.md) | 在国际营销经典文献流中定位论文，搭建定位对比表 |
| 5 | [`jim-methods`](skills/jim-methods/SKILL.md) | 多国研究设计——国家选择、等价性、不变性计划、出口面板识别 |
| 6 | [`jim-data-analysis`](skills/jim-data-analysis/SKILL.md) | 执行不变性阶梯、多层/多组模型与正式的国家间差异检验 |
| 7 | [`jim-contribution-framing`](skills/jim-contribution-framing/SKILL.md) | 表述双重贡献，抵御"情境扩展"式否定 |
| 8 | [`jim-tables-figures`](skills/jim-tables-figures/SKILL.md) | 在 50 页上限内搭建图表主干（不变性表、核心图） |
| 9 | [`jim-writing-style`](skills/jim-writing-style/SKILL.md) | 200 词摘要、引言结构与去刻板化的文化表述（AMA 风格） |
| 10 | [`jim-submission`](skills/jim-submission/SKILL.md) | ScholarOne（ama_jim）投稿预检——双匿名两文件包、上限、声明 |
| 11 | [`jim-review-process`](skills/jim-review-process/SKILL.md) | 编辑流程、JIM 特有的 desk-reject 触发点与等待期安排 |
| 12 | [`jim-rebuttal`](skills/jim-rebuttal/SKILL.md) | 审稿意见分诊、是否补国家/补研究的决策与回复信写作 |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 AMA/SAGE 链接与易变事实台账（核验于 2026-07-16）
- [`resources/external_tools.md`](resources/external_tools.md) — 国家层数据、多国样本面板与不变性/多层模型软件
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 12 篇经典文献（标注真实发表期刊）
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — JIM 式引言改写示例（虚构）
- [`resources/code/`](resources/code/) — 实证代码脚手架（Stata + Python）

## 与同类期刊的边界

| 期刊 | 重心 | 何时选 JIM |
|------|------|------------|
| JIBS | 广义国际商务理论 | 机制是营销机制（品牌、顾客、渠道） |
| Journal of Marketing | 广义营销战略 | 跨国差异是理论引擎而非稳健性脚注 |
| International Marketing Review | 较早期的国际营销研究 | 证据达到顶刊标准（不变性、识别、多研究） |
| Journal of World Business | 跨国公司管理/战略 | 因变量是营销结果 |

## 相关链接

- https://www.ama.org/journal-of-international-marketing/
- https://journals.sagepub.com/home/jig
- https://journals.sagepub.com/author-instructions/jig
- https://mc.manuscriptcentral.com/ama_jim

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
