---
name: cjms-workflow
description: Use when deciding which cjms-* sub-skill to invoke next, or when sequencing a 《中国管理科学》 (Chinese Journal of Management Science) manuscript from topic selection through rebuttal. The key fork is 优化建模 vs 数据驱动预测 vs 金融工程实证 — three strands the journal publishes side by side. Routes — does not replace — the specialized skills.
---

# 《中国管理科学》工作流（cjms-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 cjms-* skill**。

默认假设：目标是《中国管理科学》——华罗庚教授 1984 年 12 月创办（原名《优选与管理科学》，1993 年更名、2014 年起为月刊），中国科学院主管，中国优选法统筹法与经济数学研究会与中科院科技战略咨询研究院主办。本刊要的是**应用建模 + 算例/实证**：把真实管理情境刻画成模型，解出来、算出来、检验出来，最后落到可执行的管理启示。基础事实与来源见 `../../resources/official-source-map.md`。

## 关键分叉：三条主线

动笔前先判断稿件属于哪条主线，后续路由随之不同：

- **优化建模型**（规划与优化、生产与经营管理、项目管理栏目）：管理情境 → 模型 → 求解算法 → 数值实验 → 管理启示。
- **数据驱动预测型**（预测与决策栏目）：预测对象 → 方法组合/改进 → 真实数据样本外检验 → 与基准比较 → 决策含义。
- **金融工程实证型**（市场与投资分析栏目）：金融问题 → 度量/组合/风险模型 → 市场数据实证 → 稳健性 → 投资或监管启示。

三条线共享同一底线：**方法要有增量，检验要见真章**——纯文字论述、纯回归找相关、无对比的"新方法"都过不了外审。

## 触发时机

- 用户问"这篇能不能投《中国管理科学》/ 下一步做什么"
- 有模型但没有算法或算例，或有预测方法但没有样本外检验
- 手头是问卷量表或政策评估回归，不确定是否对口
- 收到外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定选题对不对口、投哪个栏目 | `cjms-topic-selection` |
| 综述只堆文献、说不清贡献增量 | `cjms-literature-review` |
| 情境讲了很多，模型要素不全 | `cjms-model-formulation` |
| 模型建好了，不知道怎么解 / 算法没对比 | `cjms-solution-algorithm` |
| 预测/金融类缺真实数据检验或基准比较 | `cjms-empirical-validation` |
| 数值实验单薄、参数拍脑袋 | `cjms-numerical-experiments` |
| 管理启示写成政策口号 | `cjms-managerial-insights` |
| 表不合三线表、公式没用编译器 | `cjms-tables-figures` |
| 摘要/关键词/中图分类号/结语体例不合 | `cjms-writing-style` |
| 准备投稿，需要 12 页红线与系统 checklist | `cjms-submission` |
| 收到外审意见，需要写回复 | `cjms-rebuttal` |

## 默认顺序

1. `cjms-topic-selection` — 判主线与栏目，先排除姊妹刊错配
2. `cjms-literature-review` — 中外双线综述，锚定方法增量
3. `cjms-model-formulation` — 把管理情境刻画成完整模型
4. `cjms-solution-algorithm` — 求解路线与算法交付（优化线重点）
5. `cjms-empirical-validation` — 真实数据检验（预测/金融线重点）
6. `cjms-numerical-experiments` — 算例与敏感性分析
7. `cjms-managerial-insights` — 从结果导出决策规律
8. `cjms-tables-figures` — 三线表、公式、图件统稿
9. `cjms-writing-style` — 摘要、结语、体例合规
10. `cjms-submission` — zgglkx.com 投稿前 preflight
11. `cjms-rebuttal` — 外审后

> 优化建模型稿件可弱化第 5 步；预测/金融实证型稿件第 4 步换成"方法构造"，但第 5 步不可省。两条线在第 6 步汇合。

## 决策口诀

- "只有回归系数没有模型/方法" → `cjms-topic-selection`（多半改投）
- "新方法但没跟基准比" → `cjms-empirical-validation` 或 `cjms-solution-algorithm`
- "算例参数说不出来源" → `cjms-numerical-experiments`
- "启示是'加强、完善、推进'" → `cjms-managerial-insights`

## 与本仓库其它期刊包的差异

- 定理与证明更厚、方法更数理 → **管理科学学报**（journal-of-management-sciences-in-china）
- 系统工程方法论、大型工程应用 → **系统工程理论与实践**（Chinese-SocialScience 广度束内 profile）
- 经验实证 / 案例 / 政策评估 → **管理世界**（journal-of-management-world）
- 资产定价与宏观金融实证 → **金融研究**（journal-of-financial-research）
- 《中国管理科学》居中：**应用建模为体、算例实证为用**，比学报更重应用情境，比管理世界更重方法交付

## 本刊全流程卡点与路由目标

本刊稿件按"情境→模型/方法→求解/检验→算例→启示"骨架推进，每节都有外审卡点。路由器的价值是让稿件不带着未过关的环节走到下一步：

| 全流程卡点 | 症状 | 应调用 |
|------------|------|--------|
| 赛道错配 | 定理厚 / 回归+政策硬投应用建模刊 | `cjms-topic-selection` |
| 情境-模型脱节 | 背景很中国、模型很教科书 | `cjms-model-formulation` |
| 方法不可辩 | 算法无性质分析、无消融基线 | `cjms-solution-algorithm` |
| 检验不硬 | 无样本外、基准全是弱者 | `cjms-empirical-validation` |
| 算例不立 | 单参数点、参数无来源 | `cjms-numerical-experiments` |
| 启示空转 | 口号化、与结果脱钩 | `cjms-managerial-insights` |
| 形式不合 | 超 12 页、公式非编译器排印 | `cjms-tables-figures` / `cjms-writing-style` |

## 微型走查：一份稿件的路由轨迹

虚构稿件《考虑极端行情的碳价组合预测》从初稿到投稿，按路由表逐阶段判断：

```
输入：VMD 分解 + 三个学习器组合，全样本内 RMSE 领先，结论含"助力双碳战略"
1 [topic] 主线=数据驱动预测，栏目=预测与决策；增量待命名 → 有条件通过
2 [literature] 中文线缺本刊近年碳价预测对话 → 补 2 篇并逐篇写差异
3 [model] 组合权重环节 = 新增结构，单独成式 → 增量可命名
4 [algorithm] 无自设计算法，跳过（方法构造已在第 3 步落实）
5 [empirical] 卡点：只有全样本内拟合 → 补滚动样本外 + DM 检验 + 危机子样本
6 [numerical] 分解层数 K 拍脑袋 → 补 K 的敏感性扫描与边界报告
7 [insights] "助力双碳战略"命中口号黑名单 → 改写为配额调节的参数校准建议
8 [style] 摘要 260 字超限 → 压到 180 字、五要素齐
9 [submission] 13 页超红线 → 附加实验表移附录，12 页达标 → 可投
```

轨迹显示：第 5、6、7 步是真实卡点；预测线稿件最常死在"样本外"与"口号启示"两处。

## 反模式

- **不要**跳过 `cjms-topic-selection` 就动笔——本刊与《管理科学学报》《系统工程理论与实践》分工明确，投错赛道是最常见退稿
- **不要**在模型没立住时先去打磨图表与文风
- **不要**把"管理启示"当装饰段落——本刊源自华罗庚"把方法用到国民经济中去"的传统，应用落点是审稿硬指标
- **不要**让 `cjms-rebuttal` 在正文未修订前生成回复
