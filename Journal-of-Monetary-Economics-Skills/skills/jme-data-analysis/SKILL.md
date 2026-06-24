---
name: jme-data-analysis
description: Use when building or stress-testing the empirical/quantitative analysis for a Journal of Monetary Economics (JME) manuscript — VAR/SVAR, local projections, DSGE estimation, moment matching, IRFs, and FEVDs — to monetary-economics and macroeconomics norms. Covers estimation choices, inference, and robustness.
---

# Data & Quantitative Analysis (jme-data-analysis)

## When to trigger

- The estimation runs but referees will question the specification or inference
- You must decide between a VAR, a proxy-SVAR, and local projections
- A DSGE is estimated/calibrated and needs convergence and fit diagnostics
- The robustness battery for a macro paper is unclear

## Macro-empirical norms at JME

JME analysis is **aggregate and policy-relevant**, so the workhorses are different from micro-econometrics. The core toolkit:

- **VAR / SVAR / proxy-SVAR** for dynamic responses to identified shocks; report **impulse responses with confidence/credible bands**, lag selection, stability, and **forecast-error variance decompositions (FEVDs)**.
- **Local projections (Jordà)** as a robustness counterpart to VAR IRFs; show both when feasible, since LP trades variance for robustness to misspecification.
- **DSGE / quantitative models** estimated by Bayesian methods (Dynare) or calibrated to micro moments; report **prior/posterior plots, MCMC convergence, identification (Iskrev), and posterior predictive / second-moment fit**.
- **Real-time data** (FRED/ALFRED vintages, Greenbook/Tealbook) where the information set matters — using final-revised data to study a real-time policy decision is a known pitfall.

Inference must match the design: **HAC / Newey–West** or clustered standard errors for time-series regressions and local projections; credible intervals from the posterior for Bayesian DSGE; bootstrap or analytical bands for VAR IRFs. Report units consistently — e.g., responses to a **100-basis-point** or **one-standard-deviation** policy shock.

## Robustness battery (macro)

- Alternative lag lengths, sample splits (e.g., pre/post-1984 Great Moderation, ZLB period), and sub-samples
- Alternative identification (ordering, restriction set, instrument) and LP-vs-VAR comparison
- Real-time vs. revised data; alternative shock series
- For DSGE: prior sensitivity, alternative calibrations, and the mechanism on/off comparison
- Zero-lower-bound / effective-lower-bound treatment where the sample spans it

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JME is monetary macro — SVAR, local projections, high-frequency identification; `local_projections`/`irf` are in StatsPAI, DSGE/calibration is outside this toolchain.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] IRFs reported with bands; FEVDs where informative
- [ ] LP and VAR compared where the question allows
- [ ] Inference matched to the design (HAC/cluster, posterior bands, bootstrap)
- [ ] Real-time vs. revised data considered
- [ ] DSGE convergence / identification / fit diagnostics reported
- [ ] Shock units stated and consistent across exhibits
- [ ] Robustness pushed to the online supplement to respect the 40-page / ≤10-exhibit cap

## Anti-patterns

- Recursive SVAR ordering presented as the only identification with no robustness
- Using final-revised data to model a real-time policy choice
- Reporting a single DSGE point estimate with no convergence or prior-sensitivity evidence
- IRFs without bands, or with inconsistent shock units across figures


## Evidence pass for Journal of Monetary Economics

Treat this skill as an executable review pass, not a prose hint. First lock the main macro object, the identifying variation, and the policy-relevant counterfactual; then judge whether the current manuscript answers the venue's real reader: macro and monetary economists who expect the shock, mechanism, and policy margin to be visible early.

- **Do the pass:** Audit the research design before polishing prose: unit of analysis, comparison set, uncertainty, sensitivity, missingness, and reproducibility must be visible.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JIE for open-economy trade/finance emphasis, RED for dynamic macro theory, AEJ Macro for broader field positioning; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Method】VAR / SVAR / proxy-SVAR / LP / DSGE / mixed
【Inference】HAC / cluster / posterior bands / bootstrap
【IRFs + FEVDs】reported? Y/N
【LP-vs-VAR】reported? Y/N/NA
【Real-time data】used where needed? Y/N
【Robustness done / missing】[...]
【Next step】jme-tables-figures
```
