---
name: jqte-econometric-methods
description: Use when the empirical core of a 《数量经济技术经济研究》 (JQTE) manuscript is an econometric model — time series, cointegration, mixed-frequency, VAR/SVAR, state-space, or panel / macro-econometrics. Enforces correct model setup, stationarity / unit-root and cointegration diagnostics, and lag/specification justification. Use when the method itself is the contribution rather than a causal identification claim.
---

# 计量方法（jqte-econometric-methods）

## 触发时机

- 实证主体是时间序列 / VAR / 协整 / 混频 / 状态空间 / 宏观面板
- 模型设定、平稳性、滞后阶交代不清，或被质疑"伪回归"
- 方法本身是贡献（把某模型用到中国数据），而非干净因果

## 设定前必查：数据性质决定模型

| 数据性质 | 必做诊断 | 建模含义 |
|----------|----------|----------|
| 单一时间序列 | 单位根（ADF/PP/KPSS）、结构突变（Zivot-Andrews/Bai-Perron） | 非平稳需差分或协整建模 |
| 多变量时间序列 | 单位根 + 协整（Johansen / EG / ARDL 边界） | 协整存在用 VECM，否则差分 VAR |
| 混频数据 | 频率对齐方式 | MIDAS / 桥接模型 / 状态空间 |
| 宏观/动态面板 | 截面相关、面板单位根、面板协整 | 跨截面相关需 CCE/CSDL；动态面板用 GMM 并查工具有效性 |

## 各类模型的规范要点

### 时间序列 / VAR / SVAR

- 平稳性先于建模：单位根检验 + 必要的结构突变检验
- 滞后阶用信息准则（AIC/BIC/HQ）选并报告，不凭经验拍
- SVAR 的识别约束（递归/长期/符号约束）显式列出并论证
- 报告脉冲响应、方差分解，必要时给稳定性（伴随矩阵特征根 < 1）

### 协整 / VECM / ARDL

- 报告协整秩检验（迹/最大特征根）或 ARDL 边界检验
- 误差修正项符号与显著性、调整速度解读
- 长期与短期关系分开汇报

### 动态面板 / GMM

- 差分/系统 GMM 选择有依据；工具变量个数受控（避免工具过多）
- 报告 AR(1)/AR(2) 序列相关检验与 Hansen/Sargan 过度识别检验
- 内生变量、外生变量、工具集划分清楚

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《数量经济技术经济研究》偏计量方法与应用；估计量有效性 + 诊断，必要时附模拟证据。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 自检清单

- [ ] 先验平稳性/单位根，再建模（防伪回归）
- [ ] 滞后阶/协整秩用准则选并报告
- [ ] 识别约束（SVAR）或工具有效性（GMM）显式论证
- [ ] 报告了必要的诊断（残差自相关、稳定性、过度识别）
- [ ] 方法的适用条件与局限有交代

## 反模式

- 直接对非平稳序列跑 OLS/VAR，不验单位根（伪回归）
- 滞后阶凭经验定，不报准则
- 动态面板工具变量爆炸，Hansen 检验 p 值接近 1 仍不警觉
- 报一堆系数却不解读长期/短期关系或脉冲响应

## 本刊审稿期待：方法创新 + 中国应用落地

《数量经济技术经济研究》对计量方法论文的核心期待是"方法创新 + 中国问题落地"双轮驱动：不是把时髦模型搬来跑数，而是说清这个设定在中国数据下为何合适、解决了前人哪个困难。

| 本刊审稿维度 | 达标线 | 常见退稿表现 |
|--------------|--------|--------------|
| 设定与数据匹配 | 平稳性/协整诊断先行，模型族有据 | 对非平稳序列直接 OLS/VAR |
| 方法适用边界 | 交代假设、失效条件、与中国数据契合 | "别人都这么用"式套用 |
| 识别/工具有效性 | SVAR 约束有论证；GMM 工具受控 | 工具爆炸，Hansen p≈1 仍不警觉 |

## 微型走查：混频数据预测工业增加值（示意稿件）

设想《基于 MIDAS 的中国工业增加值混频预测》（数字为示意）：

1. **数据性质判定**：月度工业指标 + 季度工业增加值 → 混频，落 MIDAS / 桥接。
2. **平稳性**：对增加值同比序列做 ADF（示意 t=-3.6，拒绝单位根）、对高频指标做 KPSS，必要时取增长率。
3. **设定**：MIDAS 滞后多项式选 Almon，阶数用 BIC 选（示意 3 阶），交代为何不用无约束 U-MIDAS（参数过多）。
4. **诊断**：残差无自相关（Ljung-Box 示意 p=0.31）；与桥接模型比较拟合。
5. **落地论证**：说明该设定对中国"季度 GDP 核算滞后、月度指标先行"格局的契合——这是本刊看重的"中国问题落地"。

```text
【模型】混频 MIDAS（对照桥接）｜【平稳性】ADF 拒单位根（示意 t=-3.6）□
【设定】Almon 多项式 3 阶（BIC 选），非 U-MIDAS（防参数过多）
【诊断】Ljung-Box p=0.31（示意，无残差自相关）□
【中国落地】季度核算滞后 + 月度先行指标契合
```

## 审稿人追问模式 + 本刊语境修法

- **"你这是不是伪回归？"** → 补单位根 + 协整检验表，协整成立改用 VECM 并报误差修正项与调整速度；明确"先验平稳性再建模"。
- **"机器学习/高维计量像黑箱，凭什么信？"** → 本刊近年强调机器学习的规范应用与可解释性：给变量重要性、偏依赖或与传统模型对照，说明不是纯预测黑箱。
- **"动态面板工具变量太多？"** → 限制工具滞后阶或 collapse，报工具数与样本量之比，附 AR(2) 与 Hansen，p 值不应贴近 1。

## 校准锚点

- 本刊计量方法类已刊论文通常把"模型适用条件 + 中国数据契合"写进方法节开头，而非仅罗列公式；检验报告格式等细节**以编辑部最新《投稿须知》与栏目惯例为准**。

## 输出格式

```
【模型】时间序列 / VAR-SVAR / 协整-VECM / 混频 / 动态面板
【平稳性】单位根 □ 结构突变 □ 协整 □
【设定】滞后阶 <准则> / 识别约束 <…> / 工具有效性 <…>
【诊断】自相关 □ 稳定性 □ 过度识别 □
【适用条件】<已交代 / 待补>
【下一步】jqte-forecasting / jqte-sensitivity
```
