> **Illustrative teaching example — synthetic data, real tool runs.** The dataset is
> **fictional** (a seeded observational study: a binary treatment confounded through a
> *nonlinear* function of a covariate). But every number was produced by an **actual
> StatsPAI MCP call on 2026-06-24** — nothing is hand-typed. Venue-neutral DML companion
> to the DiD / IV / RDD / synthetic-control walkthroughs; shows the
> [`execution-with-mcp`](../execution-with-mcp.md) bridge running Double/Debiased ML.

# Worked Example: Executing Double ML (StatsPAI walkthrough)

**Setup (fictional).** A binary treatment `d`, outcome `y`, and 20 covariates `x1…x20`.
Both treatment selection and the outcome depend on `|x1|` (a **nonlinear** function), so
ordinary **linear** controls cannot remove the confounding. The DGP's true ATE is **2.0**.

> The point is not the coefficient (data are synthetic) — it is that the workflow shows
> **why rich linear controls are not enough** and that ML-based double/debiased estimation
> recovers the effect, with the overlap/sensitivity checks that keep it honest.

---

## The bias ladder (run each — watch the bias fall)

| Estimator | ATE on `d` | 95% CI | vs. true 2.0 |
|---|---|---|---|
| Naive diff-in-means — `regress("y ~ d")` | **3.57** | [3.42, 3.71] | badly biased up |
| **Rich** linear controls — `regress("y ~ d + x1…x20")` | **2.89** | [2.77, 3.01] | **still clearly biased** |
| **Double ML (IRM)** — `dml(model="irm", n_rep=5)` | **2.07** | [1.99, 2.16] | recovers the truth |

The decisive lesson sits in the middle row: throwing **all 20 covariates in linearly**
still leaves a large bias (2.89, CI excludes 2.0), because the confounding runs through
`|x1|`, which a linear term cannot absorb. Double ML — cross-fitted **gradient-boosting**
nuisances for both the outcome and the propensity, combined in a Neyman-orthogonal score —
learns the nonlinearity and lands at **2.07**, CI covering 2.0.

`dml(... model="irm", n_rep=5)` used `GradientBoostingRegressor` (outcome) +
`GradientBoostingClassifier` (propensity), 5 folds × 5 repetitions (median-aggregated for
stability).

## Audit it — DML is not a free lunch

`audit_result(result_id=…)` on the DML fit returns the checks the design still owes:

| Check | Status | Why it matters |
|---|---|---|
| **Overlap** (propensity common support) | missing (high) | without 0 < ê(x) < 1 across arms, the estimate extrapolates → run `overlap_check`, trim/`overlap_weights` if needed |
| **OVB sensitivity** | missing (medium) | unconfoundedness is untestable; quantify how strong a hidden confounder would need to be → `oster` / `sensemakr` / `evalue` |

DML removes bias from *observed* nonlinear confounding; it does **not** rescue you from
poor overlap or unobserved confounders. Reporting overlap + a sensitivity bound is what
makes a DML result credible — the audit names exactly which to run.

---

## What goes where in the manuscript

- **Body:** the bias ladder (naive → rich linear controls → DML), the DML point estimate
  with its CI, the nuisance learners used, and the overlap statement. One sentence on the
  identifying assumption (unconfoundedness given `X`).
- **Appendix:** the overlap/propensity histogram, the OVB sensitivity bound, a
  specification curve over learners (`spec_curve`), and CATE/heterogeneity if relevant.
- **Unconfoundedness** is the assumption DML *cannot* test — argue it from the design and
  bound its failure with sensitivity analysis.

## Reproduce this

1. Generate the data (seeded): 20 covariates; `d` selected via a logit in `|x1|`; outcome
   `y = 2·|x1| + 0.8·x2² + 1.5·x5 + 2·d + ε` (true ATE 2.0). The `|x1|` term is what makes
   linear controls fail and ML nuisances necessary.
2. Run the ladder: `regress("y ~ d")` → `regress("y ~ d + x1…x20")` →
   `dml(model="irm", n_rep=5, as_handle=true)` → `audit_result(result_id=…)` → run the
   overlap + sensitivity functions it names. For a constant effect, `model="plr"` is a
   robustness cross-check. Full map: [`execution-with-mcp`](../execution-with-mcp.md).
3. If StatsPAI is not connected, the empirical-methods `code/` skeleton has the DML chain
   (`06_dml.do`); say which number is unverified rather than reporting one you did not compute.
