---
name: cie-did-identification
description: Use when the identification strategy for a 《中国工业经济》 (China Industrial Economics) manuscript is multi-period / staggered DID or an event study. Mandates parallel-trends event-study plots, placebo tests, and modern heterogeneity-robust estimators (Callaway-Sant'Anna, Sun-Abraham, de Chaisemartin-D'Haultfœuille, Goodman-Bacon decomposition) whenever treatment timing varies.
---

# 识别策略：多期 DID / 事件研究（cie-did-identification）

## 触发时机

- 实证主体是 DID / 多期（交错）DID / event-study
- TWFE 用在交错处理上，但没回应异质性处理偏误
- 平行趋势只口头说"满足"，没画事件研究图
- 用连续型处理强度（continuous/dose DID）但识别假设没说清

## 本刊红线（缺一即高危退修）

1. **平行趋势必须画事件研究图**（动态效应 + 95% CI，处理前各期系数应不显著）
2. **安慰剂检验必做**（随机化处理时点/处理对象 500—1000 次，看真实估计是否落在分布尾部）
3. **交错处理必须用异质性稳健估计**——TWFE 在交错+异质性处理效应下有偏（负权重问题）

## 分支路径

### 分支 A：标准两期 / 单一时点 DID

- 平行趋势：事件研究图 + 处理前系数联合检验
- 安慰剂：随机分配处理组 ≥ 500 次
- 控制组合理性论证（为什么这些是有效对照）

### 分支 B：交错（staggered）DID —— 本刊高频

- **必须**做 Goodman-Bacon 分解，报告"坏比较（已处理作对照）"权重
- **必须**改用异质性稳健估计之一并作为主/稳健结果：
  - Callaway & Sant'Anna（2021）group-time ATT
  - Sun & Abraham（2021）交互加权事件研究
  - de Chaisemartin & D'Haultfœuille（2020）did_multiplegt
  - Borusyak et al. 插补估计 / Gardner two-stage
- 报告 TWFE 与稳健估计的对比，说明结论是否稳定

### 分支 C：事件研究（event-study）

- 基准期选择明确（通常 t=-1），不要遗漏共线性陷阱
- pre-trend 各期不显著；若显著需讨论预期效应/选择性
- 动态效应图标注处理时点垂直虚线（见 `cie-tables-figures`）

### 分支 D：连续/强度型 DID

- 处理强度的外生性论证
- "强度 × 时点"交互的平行趋势：不同强度组趋势一致
- 警惕强度与其他冲击共变

### 分支 E：识别加固（与 PSM-DID 衔接）

- 分配规则非随机 → PSM-DID（先匹配再 DID，转 `cie-robustness`）
- 排除同期竞争性政策（剔除其他试点样本/时间窗）

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《中国工业经济》偏产业/企业实证，常见政策冲击 DID 与 IV；强调识别与稳健性。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 必查清单

- [ ] 事件研究图已画（动态系数 + 95% CI）
- [ ] 安慰剂检验已做（时点/对象随机化）
- [ ] 交错处理：Bacon 分解 + 异质性稳健估计齐全
- [ ] 标准误聚类层次合理（通常聚类到处理层级，如城市/行业）
- [ ] 回应"预期效应 / 提前响应"
- [ ] 剔除同期竞争性政策的干扰

## 反模式

- TWFE + 交错处理却不谈负权重/异质性偏误（本刊会直接退修）
- "平行趋势满足"一句带过，不画图
- 安慰剂只换一次处理组就称稳健
- 聚类到个体却忽视处理在群组层级（低估标准误）
- 连续 DID 不论证处理强度外生

## 本刊识别审稿期待与高频退稿模式

| 审稿期待 | 达标证据 | 常见退稿模式 |
|----------|----------|--------------|
| 平行趋势可视化 | 事件研究图 + 处理前联合检验 | 仅文字"满足"、无图 |
| 交错处理不偏 | Bacon 分解 + CS/SA/dCDH 主结果 | TWFE 跑到底、不提负权重 |
| 安慰剂稳健 | 随机化时点+对象 500—1000 次 | 只换一次处理组就称通过 |
| 聚类合理 | 聚类到分配层级（城市/行业） | 聚类到个体、低估标准误 |
| 竞争政策剔除 | 剔同期试点样本 | 不提同期政策、识别被混淆 |

> 识别类意见是本刊退修的首要触发点；具体口径以编辑部最新外审标准与稿约为准，不臆造拒稿比例。

## 微型走查：智能制造试点对企业 TFP 的交错 DID

示意稿件：分三批的"智能制造试点示范"，TWFE 得 Treat×Post +0.043。按本刊红线走查：诊断为交错处理后做 Goodman-Bacon 分解（示意坏比较权重 18%，不可忽略）；改用 Callaway-Sant'Anna，示意聚合 ATT +0.038（与 TWFE 接近，稳定），并列 Sun-Abraham；画 t=-4…+4 事件研究图，处理前联合检验 p=0.42（示意）；安慰剂伪试点 1000 次真实 +0.038 落尾部；聚类到城市后标准误升至 0.012 仍 1% 显著。结论：主结果可立，进入 `cie-mechanism`。

## 审稿人追问 × 本刊语境修法

- "分批试点还用 TWFE？" → 补 Bacon 分解 + CS/SA 主结果，正文 TWFE 与稳健估计对照。
- "时点是否被企业预期？" → event-study 展示处理前系数不显著，讨论预期性投资，必要时剔处理前 1 期。
- "试点城市本就先进，分配非随机？" → 承接 `cie-institutional-background` 讲遴选规则，预告 PSM-DID。
- "同期两化融合、宽带中国怎么分离？" → 剔同期试点样本或加其虚拟变量对照。

## 校准锚点

- 本刊已刊交错 DID 论文普遍同时报告 TWFE、CS/SA 与事件研究图三件套；具体首选估计量以稿件设计与编辑部最新审稿偏好为准。
- 上述权重、p 值、系数均为示意数字。估计量选择（CS/SA/dCDH/Borusyak 插补）无唯一正解，应结合处理结构说明取舍理由。

## 输出格式

```
【识别策略】两期DID / 交错DID / event-study / 连续DID
【平行趋势】事件研究图 √ / 缺
【安慰剂】时点随机 □ 对象随机 □ / 缺
【交错处理】Bacon分解 □ CS/SA/dCDH 估计 □ / N.A.
【聚类层级】<…>
【缺失检验】<…>
【下一步】cie-mechanism
```
