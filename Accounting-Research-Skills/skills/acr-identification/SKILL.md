---
name: acr-identification
description: Use when the empirical identification strategy is the bottleneck for a 《会计研究》 (Accounting Research) manuscript — exogenous standard / regulatory changes (event study, DID), PSM, Heckman, IV — and you need to stress-test the design before drafting tables. Prefers standard/regulatory shocks as the cleanest accounting identification source.
---

# 因果识别策略（acr-identification）

## 触发时机

- 实证主体仅有 OLS + 控制变量，未处理内生性
- 用了准则/监管变更但没把它做成干净的 DID/事件研究
- DID 用 TWFE 但未回应近年异质性处理批评
- 自选择明显（如自愿披露、聘请大所）却没 PSM/Heckman

## 设计优先级（本刊偏好，强 → 弱）

1. **准则/监管外生变更 + DID 或事件研究**（本刊黄金来源：统一推行、对企业近似外生）
2. **断点回归**（清晰的监管门槛，如某规模/比例阈值触发披露义务）
3. **PSM + DID**（处理自选择 + 时间趋势）
4. **Heckman 两阶段**（自选择，如是否自愿披露、是否聘大所）
5. **工具变量**（强工具 + 排他性论证，会计场景工具较难，慎用）
6. OLS + 严密内生性讨论（描述性/计量基准类文章可接受）

## 分支路径

### 分支 A：准则/监管变更 DID（首选）
- 处理时点对齐准则**实际施行日**（见 `acr-institutional-standards`），非发布日
- 处理组/对照组界定来自适用范围（强制 vs 未覆盖）
- 平行趋势：事件研究图必须画；分批施行优先用 Callaway-Sant'Anna / Sun-Abraham，回应异质性处理偏误
- 安慰剂：随机处理时点 / 随机处理组 500–1000 次
- 预期效应：是否存在抢先反应（提前调整会计政策）

### 分支 B：PSM / PSM+DID
- 报告匹配变量、匹配方法（近邻/卡尺/核）、匹配后平衡性检验
- 共同支撑域、匹配前后差异

### 分支 C：Heckman
- 第一阶段选择方程须有**排他性约束变量**（影响选择不直接影响结果）
- 报告逆米尔斯比率显著性与方向

### 分支 D：RDD / IV
- RDD：McCrary 操纵检验、最优带宽 + 带宽稳健性、协变量平滑
- IV：第一阶段 F ≥ 10，排他性需理论/制度/安慰剂三段论证

## 执行桥（StatsPAI / Stata MCP）

把识别主张**跑出来并审计**,而不是只做论证。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《会计研究》是档案式会计实证——准则/监管变更的 DID、IV 与盈余类设计居多,正合企业因果链。

1. `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出设计尚欠的检查。
2. **交错 DID：**`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
   `honest_did_from_result`（前趋势检验功效低，Roth 2022）。
3. **IV：**`effective_f_test` + `anderson_rubin_ci`（弱工具稳健），不要只看 2SLS 的 t 值。
4. **RDD：**`rdrobust`（偏误校正）+ `rddensity` / `mccrary_test`。
5. **遗漏变量：**`oster_delta` / `sensemakr` 量化“多强的混淆才能推翻结论”。

正文报告**经济量级**，完整诊断 battery 进附录；每个数字都能复现。端到端真跑示例（合成数据、
真实返回）见 [JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/`
骨架并标注未验证的数字。
## 必查清单

- [ ] 处理时点对齐准则施行日，处理/对照组界定有制度依据
- [ ] 平行趋势 / 平滑性 / 选择方程排他变量 已做
- [ ] 安慰剂检验（随机时点 / 随机处理组）
- [ ] staggered DID 回应异质性处理偏误（CS / SA / Bacon 分解）
- [ ] 标准误聚类层次合理（公司 / 公司+年 / 处理层级）
- [ ] 自选择已用 PSM 或 Heckman 处理

## 反模式

- 用"我们认为该准则外生于公司决策"但无制度论证与安慰剂
- TWFE + 分批施行但不讨论异质性处理偏误
- 把发布日当施行日设事件窗口
- 会计场景硬找工具变量，排他性站不住
- Heckman 第一阶段无排他性约束，等同主回归加一项

## 本刊识别策略的审稿期待（决策表）

《会计研究》由中国会计学会主办，是 CSSCI 唯一权威顶级会计学期刊，审稿人把"准则/监管外生变更"视为最干净的会计识别来源。下表对齐审稿期待与退稿模式：

| 审稿期待 | 达标线 | 常见退稿模式 |
|----------|--------|--------------|
| 处理时点对齐施行日 | 用准则实际施行日界定窗口 | 把发布日当施行日 |
| 处理/对照有制度依据 | 来自准则适用范围（强制 vs 未覆盖） | 处理组界定无制度论证 |
| 平行趋势可视 | 事件研究图 + 处理前近零 | 仅文字声称平行趋势 |
| staggered 异质性 | 分批施行用 CS/SA/Bacon 分解 | TWFE + 分批却不回应异质性偏误 |
| 自选择已处理 | 自愿行为用 PSM/Heckman | 自选择明显却只跑 OLS |

## 微型走查：金融工具准则与减值计提（数字示意）

虚构稿《新金融工具准则（预期信用损失模型）对银行减值计提及时性的影响》，处理组为首批执行 I9 的上市银行、对照组为延后执行者（分批施行）。识别走查（示意）：分批 DID 处理时点对齐各家实际首次执行年报期，优先 Callaway-Sant'Anna 回应异质性；事件研究图处理前三期跨零、处理后减值及时性系数升至约 0.09（t≈2.5）；随机处理时点 1000 次真实系数落尾部（伪 p≈0.02）；Bacon 分解负权重占比约 6%，TWFE 偏误有限；标准误聚类到银行层级。

> 上述数字为演示识别流程的示意值，非真实估计。

## 审稿人追问与本刊语境修法

- 问"为什么该准则对样本外生" → 引制度证据（监管统一推行、范围非企业自选）并配安慰剂。
- 问"分批施行的 TWFE 偏误处理了吗" → 报 CS/SA + Bacon 分解，正文交代负权重占比。
- 问"自愿行为的自选择" → 对自愿披露/聘大所类处理补 PSM 或带排他变量的 Heckman。

## 校准锚点

本刊已刊准则类识别多呈"事件研究图 + 分批 DID（CS/SA）+ 安慰剂 + 聚类说明"四件套。是否需提交 Bacon 分解或额外稳健估计，以编辑部最新稿约为准。

## 输出格式

```
【识别策略】准则DID / 事件研究 / PSM / Heckman / RDD / IV
【处理时点】<施行日对齐？> 处理组/对照组依据
【已完成检验】[平行趋势, 安慰剂, 平衡性, 排他变量, ...]
【缺失检验】[...]
【聚类层次】...
【下一步】acr-mechanism
```
