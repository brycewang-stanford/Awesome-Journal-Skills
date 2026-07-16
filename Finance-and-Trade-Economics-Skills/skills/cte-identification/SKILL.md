---
name: cte-identification
description: Use when the empirical identification strategy is the bottleneck for a 《财贸经济》 manuscript — fiscal / tax / financial / trade policy shocks and firm- / city- / bank-level quasi-experimental designs (DID, IV, RDD, DML). Stress-tests the design and the policy endogeneity before drafting tables. 本技能服务于《财贸经济》(Finance & Trade Economics, CTE)。
---

# 因果识别策略（cte-identification）

## 触发时机

- 实证主体仅有描述统计 + OLS + 控制变量
- 核心解释变量是**政策 / 制度冲击**（税制改革、财政试点、金融监管、贸易政策），但没处理政策内生与预期
- DID 用了 TWFE 但没回应近年异质性处理批评（Goodman-Bacon, de Chaisemartin, Sun-Abraham, Callaway-Sant'Anna）
- IV 第一阶段 F 弱 / 工具变量排他性疑虑
- 用了机器学习控制高维协变量但没做正交化 / 交叉拟合（DML）

## 设计优先级

《财贸经济》编委对财经实证的偏好排序（强 → 弱）：

1. **财经政策冲击 + DID（含 staggered / continuous treatment）**——如营改增、减税降费、财政试点、金融监管改革、自贸区 / 关税调整的分批推行
2. **断点回归 / 断点**——清晰的政策门槛（如税收优惠资格线、财政转移支付分档线、监管资本门槛、贫困县 / 城市规模分档）
3. **工具变量**——强工具 + 排他性论证（处理政策内生与反向因果的核心武器）
4. **双重机器学习（DML）**——高维协变量 / 非线性混淆下的稳健处理效应估计
5. **合成控制法**——城市 / 省级政策评估（如单一试点城市）
6. OLS + 严密的内生性讨论（仅在有强外生性论证或结构 / 理论实证时可接受）

## 财经数据的内生性专项

财经实证最常见的内生性来源，审稿人必查：

- **政策内生**：政策是否非随机地投向"本就更好 / 更差"的地区 / 企业（如试点先选基础好的城市）？
- **反向因果**：是先有金融风险才有监管，还是监管带来风险变化？
- **预期效应**：市场主体是否在政策正式落地前已提前调整（抢出口、突击减税前投资）？
- **测量与口径**：财税口径 / 会计科目 / 贸易统计的可比性与操纵空间

针对性策略至少给出一条：固定效应 + 准实验冲击 / IV / 断点 / DML；纯 Heckman 或纯 PSM 仅作辅助，不能单独立住识别。

## 分支路径

### 分支 A：DID

- 是否 staggered？→ 必须用 Goodman-Bacon 分解 + Callaway-Sant'Anna 或 Sun-Abraham
- 平行趋势检验：事件研究图必须画，处理时点前系数应不显著
- 安慰剂：随机分配处理组 / 处理时点 500–1000 次
- 连续处理（如税率变动幅度）需回应剂量-反应的异质性偏误

### 分支 B：IV

- 第一阶段 F **必须 ≥ 10**（弱工具 → 用 Anderson-Rubin 或 weak-IV-robust CI）
- 排他性论证至少 3 段：理论 / 制度 / 安慰剂；说明工具只通过处理变量影响结果
- 财经常用工具（地理 / 历史 / 政策外生 / Bartik 份额移动）的内生性也要论证
- 是否报告 reduced form？

### 分支 C：RDD / 断点

- 是否做了 McCrary / 密度检验（防止企业 / 地方在门槛附近操纵，如为享税收优惠调节规模）？
- 带宽：最优带宽（Calonico-Cattaneo-Titiunik）+ 至少 3 个带宽稳健性
- 协变量平滑性检验；模糊断点需报告一阶段跳跃

### 分支 D：DML / 双重机器学习

- 用于高维协变量 / 非线性混淆：交叉拟合（cross-fitting）+ Neyman 正交
- 报告不同 ML 学习器（lasso / random forest / boosting）下估计的稳健性
- 说明可识别性仍依赖 CIA / 无未观测混淆假设，不是"上了机器学习就外生"

### 分支 E：结构估计 / 理论实证

- 市场主体决策模型的微观基础是否清晰？
- 识别假设是否明确列出？
- 是否提供反事实（如税率 / 关税政策模拟）？

## Execution bridge (StatsPAI / Stata MCP)

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《财贸经济》是财经实证刊，政策评估与企业 / 城市 / 银行面板为主；突出识别与政策内生性处理。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）；高维混淆用 DML（交叉拟合 + 多学习器稳健性）。
- **实验 / 多结果：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr` 评估未观测混淆。

正文报告**经济量级**（相当于均值百分比 / 折算金额），完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI / Stata 未连接，改用 `resources/code/` 并标注未验证数字。

## 必查清单

- [ ] 平行趋势 / 平滑性 / 弱工具 / 交叉拟合稳健性 检验都做了
- [ ] 政策内生 / 反向因果 / 预期效应有明确处理（不是一句"我们假设外生"）
- [ ] 安慰剂检验做了（处理时点随机 / 处理组随机）
- [ ] 标准误聚类层次合理（企业 / 城市 / 行业 / 政策推行层级）
- [ ] 是否回应了"政策提前预期"问题（政策落地前的抢跑行为）

## 反模式

- 纯描述性统计 + OLS 就下因果结论
- 政策非随机投放却当外生冲击处理
- TWFE + staggered 但不讨论异质性处理偏误
- IV 用"历史 / 地理变量"但不论证它不通过其他渠道影响当代财经结果
- RDD 用了门槛但不做密度检验（主体可能操纵分组）
- 上了机器学习就宣称"控制了内生性"

## 输出格式

```
【识别策略】DID / IV / RDD / DML / 合成控制 / 结构估计
【政策内生处理】方式：[...]
【已完成检验】[平行趋势, 安慰剂, 弱工具, 交叉拟合, 密度检验, ...]
【缺失检验】[...]
【聚类层次】企业 / 城市 / 行业 / ...
【下一步】cte-mechanism
```
