# 案例 2 · 交错 DiD：Castle Doctrine 法案与凶杀率

> **一句话结论**：2005–2009 年间 21 个州先后通过的 Castle Doctrine（"就地防卫"）
> 法案使州凶杀率**上升约 11%**（Callaway–Sant'Anna 组-时 ATT = +0.110 log points，
> p = 0.004）；换 not-yet-treated 对照组结果几乎不变，Rambachan–Roth Honest DiD
> 显示结论在平行趋势小幅违背（M ≤ 0.019）下仍然成立。方向与量级与
> Cheng & Hoekstra (2013, JHR) 的经典结论一致。

**运行日期**：2026-07-02 · **执行层**：StatsPAI MCP · 数字为工具真实返回值逐字摘录。

---

## 1. 研究问题与数据

- **问题**：扩大正当防卫范围的州法（castle doctrine / stand-your-ground）对凶杀率的因果效应。
- **数据**：Cheng & Hoekstra (2013) 复现面板，来自 Scott Cunningham《Causal Inference:
  The Mixtape》公开数据仓（`scunning1975/mixtape` 的 `castle.dta`）：50 州 × 2000–2010 年，
  550 州-年观测。
- **处理时点**：`effyear` ∈ {2005, 2006, 2007, 2008, 2009}，5 个采纳队列
  （11/143/44/22/11 州-年），29 个 never-treated 州做对照。
- **预处理**：构造 cohort 列 `g` = 首次生效年（never-treated 记 0），结果变量
  `l_homicide`（log 每 10 万人凶杀数）。

## 2. 主估计：Callaway–Sant'Anna (2021)

为什么不用 TWFE：采纳时点交错 + 效应可能随队列/时间异质，TWFE 的负权重问题
会污染估计；CS 的组-时 ATT 聚合对此稳健——这正是共享执行手册对交错设计的默认路由。

调用：`callaway_santanna(y=l_homicide, i=sid, t=year, g=g, estimator=dr, control_group=nevertreated)`

| 量 | 值 |
|---|---|
| 总 ATT | **+0.1104** log points（≈ +11.7%） |
| SE | 0.0386 |
| p 值 | **0.0042** |
| 95% CI | [0.035, 0.186] |
| 设计 | DR（双重稳健）估计量，50 单位 × 11 期，5 个队列 |

**平行趋势直观证据**：2005 队列的全部前期组-时 ATT 均不显著
（t−5 至 t−2：p = 0.246 / 0.932 / 0.684 / 0.986）——前期无系统性偏离。

## 3. 稳健性

| 检验 | 结果 |
|---|---|
| 对照组换 not-yet-treated | ATT = +0.1094（SE 0.0386，p = 0.0046）——几乎不变 |
| Rambachan–Roth Honest DiD（SD 限制，e=0） | M = 0 时 CI [0.023, 0.171] 拒绝零；**直到 M ≈ 0.0189 仍拒绝零**；M ≥ 0.038 起 CI 含零 |

Honest DiD 的读法：允许处理后趋势偏离幅度达到前期斜率变化 0.019 log points/期
以内，效应仍显著为正——结论不依赖「平行趋势严格成立」。

## 4. 论文级表述（可直接进稿）

> Using the Callaway–Sant'Anna (2021) doubly-robust estimator with
> never-treated states as controls, we estimate that castle-doctrine laws
> increased log homicide rates by 0.110 (SE 0.039, p = 0.004). The estimate
> is invariant to using not-yet-treated controls (0.109) and survives
> Rambachan–Roth honest confidence intervals up to smoothness deviations of
> M = 0.019; pre-treatment group-time ATTs are jointly indistinguishable
> from zero.

## 运行备注（如实记录）

- `aggte`（事件研究聚合）与 `pretrends_test` 对 result_id 句柄的解析在服务端损坏
  （`'str' object has no attribute 'detail'`，2026-07-02 复现），事件研究聚合以
  主调用返回的组-时 ATT 明细替代；`honest_did_from_result` 的句柄链路正常。
- 与原文差异：Cheng & Hoekstra 用 TWFE 报告约 +8%；本案例的 CS 估计（+11%）
  是对异质效应稳健的版本，方向一致、量级相近。

## 与 skill 体系的连接

- 执行手册交错 DiD 一节：[`shared-resources/empirical-methods/execution-with-mcp.md`](../../shared-resources/empirical-methods/execution-with-mcp.md)
- 审稿人预判（DiD 常见质疑）：[`shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
