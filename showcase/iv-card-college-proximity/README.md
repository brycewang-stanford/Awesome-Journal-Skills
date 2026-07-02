# 案例 3 · 工具变量：Card (1995) 大学距离与教育回报

> **一句话结论**：以「成长地附近是否有四年制大学」为教育年限的工具，
> 2SLS 估计的教育回报为 **13.2%/年**（OLS 仅 7.4%），首阶段 F = 16.7、
> Olea–Pflueger 有效 F = 17.5 落在「中等强度」区间；三种弱 IV 稳健推断
> （Anderson–Rubin、CLR、tF 校正）一致确认效应显著为正。
> 与 Card (1995) 的经典结论一致。

**运行日期**：2026-07-02 · **执行层**：StatsPAI MCP · 数字为工具真实返回值逐字摘录。

---

## 1. 研究问题与数据

- **问题**：教育年限对工资的因果回报。OLS 受能力偏误污染；用地理供给侧变量
  （成长地是否邻近四年制大学 `nearc4`）作工具。
- **数据**：NLS Young Men（Card 1995 原数据），来自 Mixtape 公开数据仓
  （`scunning1975/mixtape` 的 `card.dta`）：3010 人。
- **规格**：`lwage ~ (educ ~ nearc4) + exper + expersq + black + south + smsa`，HC1 稳健 SE。

## 2. 主估计：2SLS 与 OLS 对照

| 估计量 | educ 系数 | SE | p |
|---|---|---|---|
| OLS | 0.0740 | 0.0036 | <0.001 |
| **2SLS** | **0.1323** | 0.0486 | 0.0065 |
| LIML | 0.1323 | 0.0486 | 0.0065 |

恰好识别（1 工具 1 内生变量）时 LIML 与 2SLS 数值相同——工具返回验证了这一点。
IV > OLS 的经典模式：OLS 的能力偏误方向为正的直觉在此被 LATE 解释取代
（受工具影响的边际入学者回报更高）。

**识别诊断**（工具逐字返回）：首阶段 F = 16.72（p < 0.001），
Olea–Pflueger 有效 F = 17.51，KP rk Wald F = 17.55，
Hausman p = 0.215（不能拒绝 OLS 一致，但按惯例两者并报）。

## 3. 弱 IV 稳健推断（`weakrobust` 统一面板）

有效 F 落在 10–23.1 的「中等强度」区（t 检验可能过度拒绝），
因此显著性必须用对弱工具尺度正确的检验复核：

| 检验 | 统计量 | p | 95% 置信集 |
|---|---|---|---|
| Anderson–Rubin | 6.88 | 0.0088 | [0.057, 0.257] |
| CLR (Moreira) | 6.88 | 0.0096 | [0.039, 0.260] |
| Kleibergen K | 6.92 | 0.0085 | [0.039, 0.260] |
| tF 校正（Lee et al. 2022） | 临界值 2.42 | — | t = 2.72 > 2.42，仍显著 |

四条尺度稳健路径全部确认：教育回报显著为正，置信集不含零且不无界。

## 4. 论文级表述（可直接进稿）

> Instrumenting years of schooling with proximity to a four-year college,
> 2SLS yields a return of 13.2% per year (HC1 SE 4.9%), against an OLS
> estimate of 7.4%. With an effective first-stage F of 17.5, we report
> weak-instrument-robust inference throughout: the Anderson–Rubin 95%
> confidence set is [0.057, 0.257], the CLR set [0.039, 0.260], and the
> estimate remains significant under the Lee et al. (2022) tF-adjusted
> critical value (2.72 > 2.42).

## 运行备注（如实记录）

- `anderson_rubin_test` / `anderson_rubin_ci` 两个独立工具的载荷为空或不接受
  result_id（2026-07-02 复现）；统一面板 `weakrobust` 功能正常且覆盖同一内容，
  本案例以其输出为准。
- 排除约束（大学邻近度只通过教育影响工资）不可检验；Card 原文的家庭背景
  控制变量敏感性检查是投稿前的必做项，此处规格保持教科书基准版。

## 与 skill 体系的连接

- 执行手册 IV 一节（弱 IV 路由）：[`shared-resources/empirical-methods/execution-with-mcp.md`](../../shared-resources/empirical-methods/execution-with-mcp.md)
- 报告标准（弱 IV 诊断为必报项）：[`shared-resources/empirical-methods/reporting-standards.md`](../../shared-resources/empirical-methods/reporting-standards.md)
