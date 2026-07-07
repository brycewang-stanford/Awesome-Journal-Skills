# 复现契约 · 案例 3：工具变量 · Card (1995) 大学距离与教育回报

> 本文件把 [`README.md`](README.md) 中的"实际运行"打包成可复验的最小操作步骤。
> **本案例与案例 5 共用同一数据集，刻意演示「函数形式 vs 内生性」的方法论分界。**

## 元数据

| # | 项 | 值 |
|---|---|---|
| 1 | 复现等级 | **Level 2** — 数据 + 完整 MCP 工具调用清单 |
| 2 | StatsPAI MCP 服务 | 工具：`ivreg`、`iv_diag`、`effective_f_test`、`anderson_rubin_test`、`tF_critical_value`、`robustness_report` |
| 3 | 公开基准数据 | `scunning1975/mixtape` 的 `card.dta`：NLS Young Men 3010 行 |
| 4 | 依赖 skill | `Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md` |
| 5 | 预计用时 | 3–5 分钟 |

## 0. 环境前置

```text
mcp server 'statspai' 已配
Python: pandas / numpy / linearmodels（卡 2SLS 的两种实现，任选其一）
```

## 1. 数据加载

```text
git clone https://github.com/scunning1975/mixtape /tmp/mixtape
pd.read_stata('/tmp/mixtape/card.dta')
→ 列：lwage / educ / exper / expersq / black / south / smsa / nearc4
→ 模型：lwage ~ (educ ~ nearc4) + exper + expersq + black + south + smsa
→ SE: HC1 robust
```

## 2. MCP 工具调用清单

| Step | 工具 (MCP) | 关键参数 | 期望返回主关键值 | 与 `README.md` § 2 / § 3 比对 |
|---|---|---|---|---|
| 1 | `regress`（先做 OLS 对照） | formula=`lwage ~ educ + exper + expersq + black + south + smsa`, robust=`hc1` | educ 系数 ≈ **0.0740**, SE ≈ 0.0036 | ✅ "OLS"行 |
| 2 | `ivreg` | formula=`lwage ~ (educ ~ nearc4) + exper + expersq + black + south + smsa`, robust=`hc1` | educ 系数 ≈ **0.1323**, SE ≈ 0.0483 | ✅ "2SLS"行 |
| 3 | `effective_f_test` | endog=`educ`, instruments=`nearc4`, exog=`exper, expersq, black, south, smsa` | 有效 F ≈ **17.5** | ✅ Olea–Pflueger 段 |
| 4 | `anderson_rubin_test` | endog=`educ`, exog=`exper, expersq, black, south, smsa`, instruments=`nearc4`, h0=0.06 | 拒绝 H0（p ≈ 0.04） | ✅ AR 段 |
| 5 | `tF_critical_value` | first_stage_F=16.7 | tF 校正临界值 ≈ 3.32（比名义 1.96 大）| ✅ tF 段 |
| 6 | `evalue_from_result` | result=ivreg_result, measure=`SMD` | E-value ≈ 1.85（敏感性段）| ✅ E-value 行 |

## 3. 数字对账

- OLS educ = 0.0740、SE = 0.0036 → README 同值
- 2SLS educ = 0.1323、SE = 0.0483 → README 同值
- 首阶段 F ≈ 16.7；Olea–Pflueger 有效 F ≈ 17.5 → README 同值
- AR p ≈ 0.04（拒绝空 6% 假设）→ README 同值
- tF 临界值由 F=16.7 查表得；E-value ≈ 1.85 → README 同值

容差：educ 系数 ±0.005（同一 IV estimator）；F ±1。

## 4. 已知差异 / 工具缺陷

- `anderson_rubin_test` 在某些 seed 下空载荷会回 0 长度——若复现得到 AR 结果 p ≈ 0.04 但
  test 输出为空，对比 `anderson_rubin_ci` 取 CI 上下界交叉判断等效性。
- `tF_critical_value` 当前仅 α=0.05 表（Lee–McCrary–Moreira–Porter 2022）；其他 α 暂未实现。

## 5. 失败模式与提示

| 现象 | 可能原因 | 处理 |
|---|---|---|
| 2SLS educ 系数 ±0.01 偏移 | `nearc4` 不是好工具（弱 F） | 检查首阶段 F；若 <10 报告「弱 IV」并以 AR 为主 |
| AR p 与 README 大幅不同（> 0.20） | HC1 与 HC2 选择 | 锁 `robust=hc1` |
| E-value 报 NaN | measure 选择错 | 用 `measure=SMD` 而非 `RR/OR/HR` |

— 复现契约 3/N 结束。回到 [`README.md`](README.md) 看完整解读。