---
name: er-identification
description: Use when the empirical identification strategy is the bottleneck for an Economic-Research manuscript — quasi-experimental designs (DID, IV, RDD, DML, event study). Stress-tests the design against modern (2019-2024) estimators and reporting standards before drafting tables.
---

# 因果识别策略（er-identification）

配套代码：`resources/code/stata/03_did_modern.do`（DID）、`04_iv.do`（IV）、`05_rdd.do`（RDD）、`06_dml.do`（DML）。

## 触发时机

- 实证主体仅有 OLS + 控制变量
- DID 用了 TWFE 但没回应近年异质性处理效应批评
- IV 第一阶段弱 / 工具变量内生性疑虑
- 准备用双重机器学习但不确定怎么报告

## 设计优先级

《经济研究》编委的偏好排序（强 → 弱）：

1. **政策冲击 + DID（含 staggered / continuous treatment）**
2. **断点回归（清晰的政策门槛）**
3. **工具变量（强工具 + 排他性论证）**
4. **倾向得分匹配 + DID**
5. **合成控制法**
6. **双重机器学习 / 因果森林**
7. OLS + 严密内生性讨论（在结构估计 / 理论实证文章中可接受）

> 该刊明确反对"唯定量倾向"：识别策略再漂亮，也要回到理论与中国制度问题。识别是手段，不是卖点。

## 分支 A：交叠（多时点）DID —— ★ 最常见也最易被挑

交叠 DID **不能只报 TWFE**。标准流程四步：

1. **TWFE 基准**——读者熟悉的起点（但交叠下可能有偏）。
2. **Goodman-Bacon (2021) 分解**（`bacondecomp`）——展示"坏比较 / 负权重"问题。
3. **异质性稳健估计量做主结果**（下表任选其一为主，其余作稳健性）：

| 估计量 | 论文 | Stata | R |
|--------|------|-------|---|
| group-time ATT | Callaway & Sant'Anna (2021) | `csdid` | `did::att_gt` |
| 交互加权 IW | Sun & Abraham (2021) | `eventstudyinteract` | `fixest::sunab` |
| 插补（最有效率） | Borusyak, Jaravel & Spiess (2024) | `did_imputation` | `didimputation` |
| 两阶段 | Gardner (2022) | `did2s` | `did2s` |
| 非二值/可逆处理 | de Chaisemartin & D'Haultfœuille (2020/24) | `did_multiplegt_dyn` | `DIDmultiplegtDYN` |

```stata
* Callaway-Sant'Anna：gvar = 首次受处理年份，从不处理者 = 0
csdid Y X, ivar(id) time(year) gvar(gvar) method(dripw)
estat simple        // 总体 ATT
estat event         // 动态效应
```

4. **事件研究图**检验平行趋势与动态效应（处理前一期为基准、95% CI、处理时点垂直虚线）。
5. **安慰剂**：随机指派处理时点/对象 500–1000 次，看真实系数是否落在分布尾部（见 `er-robustness`）。

**避坑**：平行趋势"只看图不检验"；预期效应/提前反应；用 TWFE 事件研究当交叠下的动态主结果（也可能有偏，主结果用 CS / SA）。

## 分支 B：IV —— 报告现代弱工具诊断

不要只报"F>10"。标准报告四要素：

1. **第一阶段 Kleibergen-Paap rk Wald F**（异方差/聚类下有效，取代 Cragg-Donald F）。
2. 对照 **Stock-Yogo (2005)** 临界值。
3. **有效 F**（Montiel Olea & Pflueger 2013，`weakivtest`），单内生变量更稳妥。
4. **弱工具稳健推断**：Anderson-Rubin 检验与置信区间（`weakiv`）；恰好识别时 AR 对弱工具完全稳健。

```stata
ivreg2 Y X (D = Z1 Z2), robust first   // 自动报告 KP rk F、Hansen J
weakivtest                              // 有效 F
weakiv ivreg2 Y X (D = Z1 Z2), robust   // AR / CLR / K 稳健区间
```

**排他性论证至少三段**：理论 / 制度 / 安慰剂；并报告 reduced form。
**范文对标**（确属《经济研究》）：王永钦、董雯《机器人的兴起如何影响中国劳动力市场？》（2020 年第 10 期）——以美国行业机器人渗透趋势构造 Bartik / shift-share 工具变量，论证外生性与排他性。

## 分支 C：RDD

```stata
rdplot     Y X, c(0) p(1) kernel(triangular)
rdrobust   Y X, c(0) p(1) kernel(triangular) bwselect(mserd)  // 报告 Robust 行
rddensity  X, c(0)                                             // CJM 操纵检验
```

- 主估计报告 **稳健偏差校正 CI**（Calonico-Cattaneo-Titiunik 2014 的核心贡献），不要只报常规 CI。
- 操纵检验用 `rddensity`（Cattaneo-Jansson-Ma，已取代 McCrary 2008）。
- 稳健性：协变量连续性、≥3 个带宽、donut RD、安慰剂断点。
- **范文对标**（确属《经济研究》）：刘生龙、周绍杰、胡鞍钢《义务教育法与中国城镇教育回报：基于断点回归设计》（2016 年第 2 期）。

## 分支 D：DML 双重机器学习

报告：模型类型（偏线性 PLR / 交互式）、交叉拟合折数 K（5 或 10）、干扰函数学习器（lasso / 随机森林 / 梯度提升）+ 学习器稳健性对比、Neyman 正交得分标准误（Chernozhukov et al. 2018）。Stata `ddml`+`pystacked`；Python `DoubleML`。

## 分支 E：结构估计 / 理论实证

微观基础是否清晰？识别假设是否明确列出？参数估计是否提供反事实分析？

## 标准误

| 场景 | 做法 | 命令 |
|------|------|------|
| 组内相关 | 聚类稳健 | `reghdfe ..., vce(cluster id)` |
| 两维相关 | 双向聚类 | `vce(cluster firm year)` |
| 聚类数过少（<~40） | wild cluster bootstrap | `boottest`（见 er-robustness） |
| 空间相关 | Conley 空间 HAC | `acreg` |

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《经济研究》是中文经济学顶刊，识别可信度通常是约束；交错 DID、弱工具稳健 IV、RDD 与机制检验。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 必查清单

- [ ] 交叠 DID：Bacon 分解 + 至少一种异质性稳健估计量 + 事件研究图
- [ ] 平行趋势 / 平滑性 / 弱工具 检验都做了（不是只看图）
- [ ] 安慰剂检验（处理时点随机 / 处理对象随机）
- [ ] IV：KP rk F + 有效 F + AR 稳健区间 + reduced form + 排他性三段论证
- [ ] RDD：报告 Robust 行 CI + rddensity 操纵检验 + 多带宽
- [ ] 标准误聚类层次合理；少聚类时 wild bootstrap
- [ ] 回应了"被处理者预期 / 提前反应"问题

## 反模式

- TWFE + staggered 但不讨论异质性处理偏误
- IV 用"外生事件 × 上一期内生变量"——审稿人会问"为何上一期不影响当期"
- "我们认为该政策外生于公司决策"但没给证据
- RDD 用了截断带宽但不汇报带宽敏感性
- 把识别策略当卖点，脱离理论与中国制度问题

## 输出格式

```
【识别策略】交叠DID / IV / RDD / DML / 结构估计 / 其他
【交叠DID 主估计量】TWFE only（需升级）/ CS / SA / BJS / dCDH
【已完成检验】[Bacon分解, 平行趋势, 安慰剂, KP F, 有效F, AR, rddensity, ...]
【缺失检验】[...]
【聚类层次】...
【下一步】er-mechanism
```
