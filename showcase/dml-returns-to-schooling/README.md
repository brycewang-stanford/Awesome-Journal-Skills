# 案例 5 · 双重机器学习：教育回报的偏线性 DML 估计

> **一句话结论**：在 Card (1995) 数据上用 DML-PLR（梯度提升学习 nuisance +
> 5 折交叉拟合）估计教育的偏线性效应为 **7.41%/年**（SE 0.37%）——与 OLS
> （7.40%）几乎重合、与 IV（13.2%，见案例 3）明显分离。这是一个刻意保留的
> 方法论教学点：**DML 放松的是函数形式假设，不是无混杂假设**；面对能力偏误，
> 灵活的机器学习不能替代工具变量。

**运行日期**：2026-07-02 · **执行层**：StatsPAI MCP · 数字为工具真实返回值逐字摘录。

---

## 1. 研究问题与设定

- **问题**：同一份 Card 数据（N = 3010，见案例 3），把「控制观测混杂」这件事
  做到机器学习级别的灵活，教育回报还剩多少？
- **模型**：偏线性回归（PLR，Chernozhukov et al. 2018）：
  Y = θ·D + g(X) + ε，D = m(X) + v。nuisance g、m 由 GradientBoosting 学习，
  Neyman 正交矩 + 交叉拟合保证 θ 的 √n 推断。
- **协变量**：exper, expersq, black, south, smsa。

## 2. 主估计

调用：`dml(y=lwage, treat=educ, covariates=[...], model=plr, n_folds=5)`

| 量 | 值 |
|---|---|
| θ（教育回报） | **0.07411** |
| SE | 0.00375 |
| 95% CI | [0.0668, 0.0815] |
| nuisance 学习器 | GradientBoostingRegressor ×2，5 折交叉拟合 |

## 3. 稳健性

| 检验 | 结果 |
|---|---|
| 10 折 × 5 次重复交叉拟合（中位数聚合） | θ = 0.07478（SE 0.00376）——对样本切分不敏感 |
| 与 OLS 对照（案例 3） | OLS 0.0740 vs DML 0.0741：ML 灵活性没有改变结论 → 线性规格在此数据上并未造成实质偏误 |
| 与 IV 对照（案例 3） | 2SLS 0.132：分歧来自**内生性**而非函数形式——DML 的无混杂假设在能力偏误面前不成立 |

## 4. 论文级表述（可直接进稿）

> Double/debiased machine learning (partially linear model, gradient-boosted
> nuisances, 5-fold cross-fitting) estimates a return to schooling of 7.41%
> (SE 0.37%), statistically indistinguishable from OLS and stable under
> repeated cross-fitting (7.48% with 10 folds × 5 repetitions). The gap
> relative to the 2SLS estimate (13.2%) therefore reflects endogeneity of
> schooling rather than functional-form misspecification, and we interpret
> the DML estimate as a flexible-controls benchmark, not a causal return.

## 运行备注（如实记录）

- `dml_sensitivity`（DML-OVB 敏感性）对 result_id 句柄的解析在服务端损坏
  （`'str' object has no attribute 'model_info'`，2026-07-02 复现，与 `aggte`
  同一 bug 家族：带必填 `result` 字符串参数的工具不解析句柄）；敏感性以
  重复交叉拟合稳定性 + OLS/IV 三角对照替代。
- 这是 showcase 里唯一**刻意不下因果结论**的案例：诚实的方法边界本身就是
  「自动实证」应当输出的内容。

## 与 skill 体系的连接

- 执行手册 DML 一节（无混杂 vs 内生性的路由判断）：[`shared-resources/empirical-methods/execution-with-mcp.md`](../../shared-resources/empirical-methods/execution-with-mcp.md)
- 案例 3（同一数据的 IV 处理）：[`../iv-card-college-proximity/`](../iv-card-college-proximity/README.md)
