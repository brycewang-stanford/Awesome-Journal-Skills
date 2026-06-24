---
name: jhr-identification-strategy
description: Use when stress-testing causal identification for a Journal of Human Resources empirical-micro manuscript, including RCT, DID, RDD, IV, event studies, decompositions, policy shocks, and reconciliation with prior estimates.
---

# Identification Strategy (jhr-identification-strategy)

## When to trigger

- The paper makes a causal claim
- Referees could say selection, omitted variables, or policy timing drives the result
- You need a reconciliation and sensitivity plan before submission

## Design checks

- **RCT**: attrition, balance, compliance, spillovers, pre-analysis plan, multiple
  testing, cluster level.
- **DID / event study**: timing, controls, pre-trends, treatment heterogeneity,
  anticipation, modern estimators where needed.
- **RDD**: manipulation, bandwidth, polynomial order, covariate continuity,
  donut/alternative bandwidths.
- **IV**: first stage, exclusion, monotonicity, weak-IV inference, LATE population.
- **Decomposition/descriptive**: what is descriptive, what is causal, and what
  policy lesson follows.

## JHR-specific layer

- Re-estimate or benchmark against close prior work when results differ.
- Report sensitivity tests that explain which sample/specification choices matter.
- Keep the public-policy interpretation tied to identified variation.

## Public-policy validity check

For every causal claim, write the policy interpretation in LATE/ATT/descriptive terms:

- **Who** is affected: treated population, complier group, cohort, locality, or institution.
- **What margin** changes: enrollment, employment, wages, health, fertility, retirement, or another JHR outcome.
- **Which policy lever** is credible: eligibility rule, treatment intensity, price, access, mandate, or program design.
- **What does not travel**: populations, periods, institutions, or equilibrium responses outside the design.

If the policy sentence needs a broader population than the estimand supports, narrow the claim before
submission.

## Reviewer threat matrix

For each causal design, pre-write the most damaging reviewer objection and the table or paragraph that
answers it:

```text
Threat | Why plausible here | Evidence already in paper | Missing evidence | Claim to narrow
```

This matrix prevents overclaiming. If the missing evidence cannot be produced, the correct repair is often
to narrow the estimand or policy interpretation, not to add another robustness table. JHR referees will
usually accept a precise local estimate more readily than a broad policy claim unsupported by the design.

## What JHR referees probe first, by design

| Design | First probe | Evidence that usually settles it |
|---|---|---|
| Staggered DID | Pre-trends and forbidden TWFE comparisons | Event study from a heterogeneity-robust estimator; honest-bounds sensitivity on the pre-period |
| RDD at an eligibility cutoff | Manipulation and sorting at the threshold | Density test at the cutoff, covariate smoothness, donut estimates |
| IV from policy variation | First-stage strength and exclusion stories | Per-instrument first stage with effective F; reduced form shown; weak-IV-robust CI |
| School/charter lottery | Differential attrition and re-application | Attrition by win/loss, balance within lottery strata, bounds for missing outcomes |
| Shift-share / Bartik | Shock vs. share identification | State which component is exogenous; exposure-robust SEs |

The cluster question cuts across all rows: inference must sit at the level where
treatment was assigned, and the paper should say how many effective clusters
remain after fixed effects absorb variation.

## Worked cutoff walkthrough

Illustrative RD: a selective public high school admits applicants scoring at or
above 70 on a composite exam; outcome is college enrollment (numbers invented
to show the decision rules):

1. Manipulation: density test at the cutoff is insignificant (illustrative
   p = 0.42); retake rules documented so referees see why bunching is unlikely.
2. Continuity: baseline GPA and family income are smooth through 70; the one
   jumpy covariate (sibling enrollment) is shown and discussed, not hidden.
3. Sensitivity: effect of 6.5 percentage points is stable across bandwidths
   roughly half to double the MSE-optimal choice and in a donut dropping exact
   70 scorers.
4. Interpretation: a LATE for marginal admits near 70 — the paper does not
   claim effects for clearly inframarginal admits, and says so.

## Failure modes that end JHR reviews early

- Event-study figure that starts at t = 0, hiding the pre-period entirely.
- One pooled first stage covering several instruments with different complier
  populations.
- Parallel-trends defense that relies on a linear state trend doing the work.
- RD without any density or covariate-continuity evidence in the draft.
- Policy conclusion written as if the LATE were a population average effect.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JHR is labor/education economics — program evaluation with selection; DiD/IV/RDD and the selection objection are central.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Claim] causal / descriptive / decomposition
[Design] RCT / DID / RDD / IV / event study / other
[Main threat] ...
[Design defense] ...
[Reconciliation needed] ...
[Next step] jhr-data-analysis
```
