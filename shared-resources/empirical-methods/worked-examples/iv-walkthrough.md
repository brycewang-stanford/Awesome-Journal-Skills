> **Illustrative teaching example — synthetic data, real tool runs.** The dataset is
> **fictional** (a seeded returns-to-schooling panel where unobserved *ability* confounds
> both education and wages). But every number in the tables was produced by an **actual
> StatsPAI MCP call on that synthetic data on 2026-06-24** — nothing is hand-typed. This
> is the venue-neutral IV companion to the JF DiD walkthrough; it shows the
> [`execution-with-mcp`](../execution-with-mcp.md) bridge running an instrumental-variables
> design end to end.

# Worked Example: Executing an IV / 2SLS Design (StatsPAI walkthrough)

**Setup (fictional).** `logwage` is regressed on years of `educ`. Unobserved ability
raises both schooling and wages, so OLS is upward-biased. An instrument `Z` (think
standardized college proximity) shifts schooling but is independent of ability, so 2SLS
recovers the causal return. The DGP's true return is **0.08 per year**; OLS should
overshoot, 2SLS should land near 0.08.

> The point is not the coefficients (data are synthetic) — it is that the workflow
> *surfaces the bias, fits the corrected estimate, and reports the weak-instrument
> diagnostic that makes the estimate credible*, each with one tool call.

---

## Step 0 — The biased baseline (run it, to show the problem)

`regress(formula="logwage ~ educ")`:

| Estimator | educ coef | SE | 95% CI |
|---|---|---|---|
| OLS | **0.1956** | 0.0059 | [0.184, 0.207] |

A tight, hugely significant 0.196 — and **wrong**: it is the 0.08 causal return plus
the ability bias. Significance is not identification.

## Step 1 — Fit 2SLS with the instrument (and keep the handle)

`iv(formula="logwage ~ (educ ~ Z)", method="2sls", robust="hc1", as_handle=true)`:

| Estimator | educ coef | SE | 95% CI |
|---|---|---|---|
| 2SLS (IV) | **0.0997** | 0.0215 | [0.058, 0.142] |

The instrument purges the ability bias: 0.196 → **0.0997**, within sampling error of the
true 0.08. Returned `result_id` = `r_801f4148` for downstream diagnostics.

## Step 2 — Is the instrument strong? (the diagnostic that licenses the estimate)

From the same `iv` call's diagnostics (all real returns):

| Diagnostic | Value | Reading |
|---|---|---|
| First-stage F (educ) | **252.7** | ≫ 10 (Stock–Yogo) — relevant |
| Olea–Pflueger effective F | **272.2** | ≫ 10 — strong under heteroskedasticity |
| Partial R² (educ) | 0.078 | instrument explains real first-stage variation |
| Kleibergen–Paap rk Wald F | 272.4 | strong-identification confirmed |

With an effective F of 272, the instrument is **far** from weak, so the conventional
2SLS confidence interval is reliable. Weak-instrument-robust inference
(`anderson_rubin_ci` / `anderson_rubin_test`) is the tool to reach for when the effective
F is low (single digits to ~10); here it would essentially coincide with the 2SLS CI, so
it is not load-bearing. *Report the effective F regardless — it is what tells the referee
the CI can be trusted.*

## Step 3 — Was IV even needed? (endogeneity test)

Also from the `iv` diagnostics — the Durbin–Wu–Hausman test:

| Test | Stat | p | Reading |
|---|---|---|---|
| Hausman (OLS vs IV) | F = 22.6 | **< 0.001** | OLS is inconsistent here — IV is warranted |

The test rejects exogeneity of `educ`, confirming the OLS–IV gap is endogeneity, not
noise. (Had it failed to reject, OLS would be consistent and more efficient — report
both and prefer OLS.)

---

## What goes where in the manuscript

- **Body:** the OLS-vs-2SLS comparison (one table), the **first-stage / effective F**,
  and the economic magnitude (a ~10% wage return per year of schooling, here). One
  sentence naming the instrument and its exclusion logic.
- **Appendix:** the first-stage regression, over-identification test if >1 instrument
  (`estat overid`), alternative estimators (LIML/GMM via `iv(method=...)`), and a
  plausibly-exogenous sensitivity (`iv_diag`'s LTZ bound) if the exclusion restriction is
  contestable.
- **Exclusion restriction** cannot be tested with one instrument — argue it in prose and
  falsify the most plausible alternative channel. No tool substitutes for that argument.

## Reproduce this

1. Generate the panel (seeded): `ability`, `Z` ⊥ `ability`; `educ = 12 + 0.35·Z +
   0.6·ability + ε`; `logwage = 1.5 + 0.08·educ + 0.30·ability + ε`.
2. Run: `regress("logwage ~ educ")` → `iv("logwage ~ (educ ~ Z)", as_handle=true)` →
   read `First-stage F` / `Olea–Pflueger effective F` / `Hausman` from the `iv`
   diagnostics. For a low-F design, add `anderson_rubin_ci`. Full map:
   [`execution-with-mcp`](../execution-with-mcp.md).
3. If StatsPAI is not connected, the same chain exists in the empirical-methods
   `code/` skeleton (`04_iv.do`: `ivreg2`/`ivreghdfe` + `weakivtest`); say which number
   is unverified rather than reporting one you did not compute.
