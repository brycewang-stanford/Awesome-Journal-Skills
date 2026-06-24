---
name: nbr-survey-sem
description: Use for survey-based structural equation modeling in 《南开管理评论》 (Nankai Business Review) — CFA/SEM fit indices, mediation and moderation, moderated mediation with bootstrap indirect effects and the index of moderated mediation, and multilevel models (HLM) for nested data. Use when testing construct-relationship hypotheses (mediation / moderation / moderated mediation) on questionnaire data.
---

# 问卷-SEM 分析（nbr-survey-sem）

## 触发时机

- 假设是中介 / 调节 / 被调节的中介
- 数据是问卷（个体或企业层级）
- 数据有嵌套结构（员工嵌套于团队/企业）

> 前置：测量须先过 `nbr-measurement`（信效度 + CMV）。模型拟合不能替代测量规范。

## 测量模型与拟合标准（经验门槛，非硬性）

先验证测量模型（CFA），再估结构模型：
- **χ²/df** < 3（宽松 < 5）；**CFI / TLI** > 0.90（宜 > 0.95）
- **RMSEA** < 0.08（宜 < 0.06）；**SRMR** < 0.08
- 用 CFA 区分多构念（如目标模型优于合并模型），佐证区分效度

## 中介 / 调节 / 被调节的中介

- **中介**：报告**Bootstrap**（如 5000 次）间接效应及偏差校正 95% CI，**CI 不含 0** 才成立；优先 Bootstrap 而非 Sobel
- **调节**：自变量与调节变量**中心化/标准化**后建交互项；报告交互项系数，并做**简单斜率（simple slope）**与图示
- **被调节的中介**：报告**moderated mediation 指数**（index of moderated mediation）及其 Bootstrap CI；并给不同调节水平下的**条件间接效应**

## 多层数据（HLM）

- 先看**ICC(1)/ICC(2)** 与 rwg 判断是否需要多层、能否聚合
- 跨层假设用**多层模型（HLM / 多层 SEM）**，区分组内/组间效应
- 跨层中介/调节按 1-1-1、2-1-1 等路径明确层级，必要时组均中心化

## 分析走查：两时点被调节中介

设想 T1 测平台员工感知算法监控与传统性，T2（间隔一个月）测情绪耗竭与离职意愿，假设为被调节的中介（传统性调节前半段）：
1. CFA：四因子目标模型优于备择合并模型（Δχ² 显著），拟合达标后才进结构模型
2. 中介：5000 次 Bootstrap，间接效应 95% CI 不含 0
3. 调节：监控与传统性中心化后建交互项，画高/低传统性（±1SD）简单斜率图
4. 被调节中介：报告 index of moderated mediation 的 Bootstrap CI，并列高/低传统性下的条件间接效应
5. 稳健性：加入标记变量后路径系数无实质变化——与 nbr-measurement 的 CMV 结论互证

## 结果呈现表序（校准锚）

本刊问卷文章的表格序列大体稳定：描述统计与相关矩阵 → 验证性因子分析比较 → 假设检验（回归或 SEM 路径系数）→ Bootstrap 中介 / 条件间接效应表，并配一张简单斜率图。每张表呼应至少一条编号假设；假设检验表宜在行末标注对应假设编号与"支持/不支持"，方便审稿人对照概念模型图核验。具体版式以期刊最新投稿指南与近期刊文为准。

## 统计质疑速答

| 质疑 | 速答路线 |
|------|----------|
| "Y 也可能反向影响 X" | 时滞设计陈述 + 理论排序论证；必要时补反向模型的拟合比较 |
| "为什么不用 HLM？" | 报 ICC(1)：低于经验阈值且假设均在个体层，说明无聚合必要 |
| "中介显著但效应量太小" | 报告效应占比与置信区间，从理论上论证小效应的累积意义 |
| "控制变量取舍随意" | 给出每个控制变量的文献依据，并报告不含控制变量的稳健性结果 |
| "拟合指标是否挑好的报" | CFI/TLI/RMSEA/SRMR 全套同表呈现，不做选择性披露 |

## 执行桥（StatsPAI / Stata MCP）

把稳健性 battery **跑出来**，而不是只罗列。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《南开管理评论》是中国情境实证管理刊；实验用随机化推断 + 多重检验，问卷-SEM 与测量循其规范，定性案例另循其标准。

- **多结果 / 多设定：**`romano_wolf`（逐步 FWER）或 `benjamini_hochberg`，报告校正后阈值。
- **遗漏变量敏感性：**`oster_delta` / `sensemakr`。
- **推断：**少聚类用 `wild_cluster_bootstrap`；视依赖结构用 `twoway_cluster` / `conley`。
- **从一个 handle 复跑：**`audit_result(result_id)` 列出缺失检查及对应 `suggest_function`。
- **出表：**`etable` / `did_summary_to_latex` 直接从 handle 生成，不手抄数字。

正文留决定性检查，详尽 battery 进附录。执行链见 [JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。
## 自检清单

- [ ] 先 CFA 后结构模型，拟合指标齐全（CFI/TLI/RMSEA/SRMR）
- [ ] 中介用 Bootstrap 间接效应 + CI，不只看系数显著
- [ ] 调节做了中心化、交互项、简单斜率与图
- [ ] 被调节的中介报告了 index of moderated mediation
- [ ] 嵌套数据先验证 ICC，再决定是否上 HLM
- [ ] 控制变量、共同方法因子等处理透明可复现

## 反模式

- 直接报结构模型，跳过测量模型拟合
- 中介只用逐步回归（Baron-Kenny）或 Sobel，不做 Bootstrap
- 调节不中心化、不画简单斜率，只贴一个交互项系数
- 嵌套数据当独立样本跑普通 SEM，无视 ICC

## 输出格式

```
【测量模型】χ²/df <…> CFI <…> TLI <…> RMSEA <…> SRMR <…>
【中介】间接效应 <…>，Boot 95% CI [ , ]｜成立□
【调节】交互项 β <…>，简单斜率：高/低 <…>
【被调节中介】index <…>，CI [ , ]｜条件间接效应：<…>
【多层】ICC1/ICC2 <…>｜模型：HLM / 多层SEM
【下一步】nbr-china-context / nbr-discussion-contribution
```
