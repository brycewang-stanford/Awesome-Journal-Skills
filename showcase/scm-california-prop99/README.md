# 案例 1 · 合成控制：加州 Prop 99 禁烟法案的消费效应

> **一句话结论**：1988 年加州通过 Proposition 99（烟草税 + 控烟计划）后，
> 加州人均卷烟消费相对「合成加州」每年平均下降约 **18 包/人**；三个独立估计量
> （经典 SCM、增广 SCM、合成 DiD）给出 −18.19 / −18.08 / −17.90 的高度一致结果，
> 安慰剂检验 p = 0.026。这与 Abadie, Diamond & Hainmueller (2010) 的经典结论方向
> 与量级一致。

**运行日期**：2026-07-01 · **执行层**：StatsPAI MCP（本仓库 skill 所接入的执行桥）
· 本页所有数字均为工具真实返回值的逐字摘录。

---

## 1. 研究问题与数据

- **问题**：州级控烟政策（1989 年生效的加州 Prop 99）对人均卷烟消费的因果效应。
- **数据**：StatsPAI 内置基准数据集 `california_prop99`（Abadie et al. 2010 的
  标准面板）：39 州 × 31 年（1970–2000），1209 行，列
  `state / year / packspercapita / treated`。
- **加载方式**：MCP 工具 `california_prop99` 返回完整面板，写出 CSV 后供估计器读取。

## 2. 主估计：经典合成控制

调用（关键参数）：

```
synth(data_path=california_prop99.csv, outcome=packspercapita,
      unit=state, time=year, treated_unit=California,
      treatment_time=1989, method=classic, inference=placebo)
```

工具返回（逐字）：

| 量 | 值 |
|---|---|
| ATT | **−18.193** 包/人/年 |
| SE | 5.404 |
| p 值（in-space placebo，38 个 donor 排名） | **0.0256** |
| 95% CI | [−28.78, −7.60] |
| 处理前拟合 RMSE | 2.831（MSPE 8.012，19 个 pre 期） |
| donor 数 | 38（有效权重集中在 8 个州，有效 donor 数 5.27） |

**合成加州的权重构成**（前 5）：Ohio 0.241 · Connecticut 0.212 ·
North Dakota 0.199 · Kansas 0.197 · South Carolina 0.074。

**处理前拟合质量**：pre-RMSE 2.83，远小于结果变量的截面波动（处理效应量级的
1/6），treated/placebo MSPE 比 6.67 —— 合成控制在 1970–1988 年紧贴真实加州，
反事实外推可信。

## 3. 稳健性：备择估计量交叉验证

| 估计量 | ATT | SE | p | 95% CI |
|---|---|---|---|---|
| 经典 SCM（placebo 推断） | −18.19 | 5.40 | 0.026 | [−28.78, −7.60] |
| 增广 SCM（ASCM, Ben-Michael et al. 2021） | −18.08 | 3.88 | 0.026 | [−25.68, −10.48] |
| 合成 DiD（SDID, Arkhangelsky et al. 2021） | −17.90 | 2.49 | <0.001 | [−22.78, −13.02] |

三个方法族（纯权重匹配 / 结果模型增广 / 双向加权）互为稳健性检验，
点估计极差 < 0.3 包 —— 结论对估计量选择不敏感。

## 4. 审计清单（reviewer-grade audit）

`audit_result(result_id=...)` 返回 SCM 设计族的标准审查清单，逐项处置：

| 审计项 | 处置 |
|---|---|
| pretreatment_fit（pre-RMSE 相对结果 SD 是否足够小） | ✅ 2.83，见 §2 |
| placebo_inference（donor 安慰剂排名推断） | ✅ 主估计即用 placebo 推断，p=0.026 |
| 备择估计量敏感性 | ✅ §3，三估计量一致 |
| convergence / ESS（贝叶斯项，仅适用 MCMC 变体） | 不适用（本案例为频率派估计） |

## 5. 论文级表述（可直接进稿）

> Using the synthetic control method with 38 donor states and 19 pre-treatment
> years, we estimate that Proposition 99 reduced California's annual per-capita
> cigarette consumption by 18.2 packs (placebo-permutation p = 0.026,
> pre-treatment RMSE 2.83). The estimate is insensitive to estimator choice:
> augmented SCM and synthetic difference-in-differences yield −18.1 (SE 3.9)
> and −17.9 (SE 2.5), respectively.

## 运行备注（如实记录）

- 经典 SCM 使用 outcome-only、V=I 的默认规格（工具文档明确这是 Kaul 式惯例）；
  与 Abadie et al. (2010) 使用 special predictors 的原规格相比点估计略有差异
  （原文约 −19 至 −24 区间），方向与量级一致。需要与 R `Synth` 完全对齐时应传
  `backend='synth'` 并复现原 predictor 配方。
- `synth_time_placebo` / `synth_loo` 两个工具在整数年份列上存在服务端类型强转
  bug（`treatment_time` 被强转为字符串后与 int64 比较报错，2026-07-01 复现两次），
  时间安慰剂检验因此以备择估计量交叉验证替代。已按「不粉饰」纪律记录。

## 与 skill 体系的连接

- 执行手册：[`shared-resources/empirical-methods/execution-with-mcp.md`](../../shared-resources/empirical-methods/execution-with-mcp.md)
- 跨期刊执行入口：[`Research-Toolkit-Skills/skills/rt-execution-bridge`](../../Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md)
- 深度用例：任何 SCM 论文投稿前，用本案例的「估计 → 备择估计量 → 审计清单」
  三段式作为最低验收线。
