---
name: jde-identification-strategy
description: Use when the causal identification strategy is the bottleneck for a Journal of Development Economics (JDE) manuscript — RCT/field experiment, DID, IV, RDD in low- and middle-income settings. Stress-tests the design against development-economics empirical norms before tables are drafted.
---

# Identification Strategy (jde-identification-strategy)

## When to trigger

- The empirical core is OLS + controls with an undefended causal claim
- A DID uses two-way fixed effects (TWFE) on staggered timing without modern estimators
- An IV's first stage is weak or the exclusion restriction is unargued
- An RCT lacks a pre-analysis plan, balance, or attrition analysis
- You are unsure your design clears the JDE causal bar

## The JDE identification bar

Development economics has been a leader in the **credibility revolution**, and JDE referees apply a demanding identification standard while respecting that field settings are messy. The implicit credibility ranking (strong → weaker):

1. **RCT / field experiment** with a registered pre-analysis plan, balance, and attrition handling — the modal credible design in modern development micro
2. **Sharp/fuzzy RDD** at a clean program or eligibility threshold (common in targeted transfer and education programs)
3. **DID / event study** off a credibly exogenous policy or shock, using modern estimators
4. **IV** with a strong first stage and a defended, institutionally-grounded exclusion restriction
5. **Selection-on-observables / matching** — acceptable only as a complement, rarely the spine

A **theoretical** paper is judged on the development relevance and rigor of its mechanism, not on a research design. A paper with **novel, hard-to-assemble data** answering a first-order development question can carry reduced-form evidence — but the question and the data discipline must be exceptional.

JDE also runs a permanent **pre-results review / Registered Reports** track: a prospective design (hypotheses, procedures, statistical analysis plan, **power analysis**, pilot data if applicable) can be reviewed and accepted in principle *before* results exist. If your design is prospective, build it to that standard — it both strengthens identification and unlocks that route (see jde-review-process).

## Branch paths

### RCT / field experiment (the development workhorse)
- Pre-registered PAP (AEA RCT Registry / OSF); report deviations honestly.
- **Power / MDE** justified at the level of randomization; clustered designs need cluster-level power.
- Balance table; attrition analysis with **Lee bounds** if differential.
- **Inference at the unit of randomization** (cluster); few clusters → wild-cluster bootstrap or randomization inference.
- Multiple-hypothesis adjustment across outcomes/subgroups (Romano–Wolf / Westfall–Young).
- External validity: what does this population and context teach beyond the site?

### DID / event study
- Staggered adoption → move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); report a Goodman-Bacon decomposition.
- Clean event-study plot with leads; pre-period coefficients near zero.

### IV
- Strong first-stage F; with weak instruments use Anderson–Rubin / weak-IV-robust sets.
- Exclusion argued in three registers: theory, institutional detail, falsification.
- Report reduced form and OLS alongside; discuss the LATE/complier interpretation.

### RDD
- McCrary / Cattaneo–Jansson–Ma density test for manipulation at the cutoff.
- Optimal bandwidth (Calonico–Cattaneo–Titiunik) plus bandwidth robustness; bias-corrected CIs.
- Covariate smoothness and placebo cutoffs.

## Worked micro-example (illustrative)

Hypothetical: a national school-construction program rolled out district-by-district over six years — a quasi-experiment exploiting staggered policy timing to estimate effects on years of schooling.

- **Identifying variation:** within-district changes in program exposure timing, comparing cohorts young enough to benefit against older cohorts at rollout.
- **The trap:** plain TWFE on the staggered rollout reporting one coefficient (e.g., +0.4 years, *illustrative*); with heterogeneous timing, already-treated districts contaminate the comparison group.
- **JDE-shaped fix:** estimate with Callaway–Sant'Anna or de Chaisemartin–D'Haultfœuille, show a Goodman-Bacon decomposition, plot the event study with leads near zero, and cluster at the district (rollout) level.
- **External validity line:** the estimate is a LATE for cohorts near the exposure margin in this institutional setting — say what it teaches about returns to schooling without claiming a universal parameter.

## Credibility pushback and the design-level answer

| Referee concern                                | What clears the JDE bar                                       |
|------------------------------------------------|--------------------------------------------------------------|
| "Staggered TWFE is biased here"                | Modern estimator + Bacon decomposition + event-study plot    |
| "Spillovers leak treatment into controls"      | Spillover/SUTVA test; bound it; defend the controls          |
| "IV exclusion is asserted, not argued"         | Theory + institutions + falsification, all three             |
| "RDD cutoff may be manipulated"                | Density test (McCrary / CJM) + covariate smoothness          |
| "One site — why generalize?"                   | Pin the LATE/population; mechanism evidence that travels      |

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Development economics leans on RCTs and observational designs alike; field experiments demand the many-outcome family-wise correction (`romano_wolf`).

1. `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to list
   the checks the design still owes.
2. **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
   `honest_did_from_result` (the pre-trend test is low-power, Roth 2022).
3. **IV:** `effective_f_test` + an `anderson_rubin_ci` (valid under weak instruments),
   not a 2SLS t-stat alone.
4. **RDD:** `rdrobust` (bias-corrected) + `rddensity` / `mccrary_test` for manipulation.
5. **OVB:** `oster_delta` / `sensemakr` — how strong a confounder would have to be.

Report the economic magnitude; route the full battery to the appendix; keep every
number reproducible. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md). If StatsPAI/Stata are not connected, adapt the
vendored `resources/code/` skeleton and flag any unverified number.
## Anti-patterns

- TWFE on staggered treatment with no discussion of heterogeneity bias
- An RCT with no PAP, no power calculation, and unexamined differential attrition
- Inference not clustered at the randomization level
- Overclaiming a single-site LATE as a universal development parameter

## Output format

```
【Design】RCT / RDD / DID / IV / theory / descriptive
【Identifying variation】one sentence
【Diagnostics done】[PAP, balance, attrition/Lee bounds, density, first-stage F, pre-trends, ...]
【Diagnostics missing】[...]
【Inference】clustering level + few-cluster handling + MHT
【Interpretation】LATE / ATE / external validity note
【Pre-results route?】[Y/N]
【Next step】jde-data-analysis
```
