---
name: jim-data-analysis
description: Use when estimating and reporting results for a Journal of International Marketing (JIM) manuscript — measurement-invariance testing (MGCFA/alignment), multilevel models with country-level predictors, multi-group SEM, and multi-country panels. It executes and reports; jim-methods designed the study.
---

# Cross-National Data Analysis (jim-data-analysis)

## When to trigger

- Multi-country data are in and the invariance battery must be run before anything else
- Country-level moderators need estimating (HLM, multi-group SEM, cross-level interactions)
- Latent means or path coefficients are about to be compared across countries
- A reviewer writes "the cross-national comparisons are not interpretable as reported"

## Invariance first — nothing compares until it passes

Run the MGCFA ladder per construct, in order, and report every rung:

| Step | Constraint added | Licenses you to… |
|------|-----------------|-------------------|
| Configural | same factor structure | claim the construct exists everywhere |
| Metric | equal loadings | compare structural paths / correlations across countries |
| Scalar | equal intercepts | compare latent means across countries |

Decision rules: χ² difference plus practical criteria (ΔCFI ≤ .01; monitor ΔRMSEA). When full invariance fails: release the minimum number of parameters for **partial invariance** (at least two invariant items per construct, per the Steenkamp–Baumgartner protocol) and restate exactly which comparisons remain licensed. With many countries (8+), pairwise MGCFA explodes — use the **alignment method** and report the proportion of non-invariant parameters (≤25% rule of thumb). If scalar invariance dies and cannot be partially rescued, mean-comparison hypotheses are off the table; say so in the paper rather than burying it.

Also run: **response-style controls** (model ARS/ERS factors or covariates as planned in design) and per-country reliability/validity (CR, AVE, discriminant checks reported for *each* country, not pooled).

## Match the estimator to the cross-national structure

| Data structure | Estimator | Reporting keys |
|----------------|-----------|----------------|
| Consumers nested in countries (10+ countries) | Multilevel / HLM with country-level predictors | ICC first; random slopes for moderated effects; group-mean vs. grand-mean centering stated |
| Few countries (2–4) | Multi-group SEM with invariance constraints | path-difference tests across groups, not eyeballed coefficients |
| Cross-level moderation | random-slope HLM or MSEM | the slope variance must be nonzero before a country variable can explain it |
| Firm export panels | FE / DiD (staggered-adoption estimators) / selection models | cluster at firm or country per the variation; pre-trends where causal |
| Country dyads (home–host) | dyadic models with distance variables | control both origin and destination effects |
| Meta-analytic | random-effects + meta-regression on country dimensions | between-study heterogeneity decomposed |

Small-N-countries warning: with fewer than ~10 countries, country-level regression coefficients are unstable — prefer multi-group contrasts, fixed effects, or Bayesian multilevel with informative priors, and never narrate 5 countries as a "test" of a continuous cultural dimension.

## Report so the cross-national claim is auditable

- **Invariance table is mandatory** — steps, fit per step, Δ-statistics, decision. It is the first table JIM methods reviewers look for.
- Per-country descriptives and correlations (or a Web Appendix panel), not pooled-only.
- Standardized effects with CIs; for mediation, bootstrapped indirect effects per group or conditional on the country moderator.
- For every country difference claimed: the formal test of the *difference* (constrained vs. free model; interaction coefficient), never two separate significance verdicts.
- Translate the headline effect into a cross-border managerial magnitude: adaptation lift in market A vs. B, export-revenue elasticity, the country profile where the strategy flips sign.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery end-to-end instead of enumerating it. Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). For JIM's structures: multi-country panels via `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`; staggered policy variation via `callaway_santanna` / `sun_abraham` with `honest_did_from_result`; few-cluster (few-country) inference via `wild_cluster_bootstrap`; many-outcome hypothesis families via `romano_wolf`; OVB sensitivity via `oster_delta` / `sensemakr`; exhibits exported from the result handle (`etable`) so no number is retyped. HLM and measurement-invariance runs (MGCFA ladders, alignment) execute in lavaan/Mplus-lane scripts under [`resources/code/`](../../resources/code/) — keep the per-step fit log as the audit trail; SEM path models follow the same handle-then-audit discipline.

## Checklist

- [ ] Invariance ladder run and tabled per construct; licensed comparisons restated
- [ ] Partial invariance (≥2 invariant items) or alignment used where full invariance failed
- [ ] Response styles controlled; per-country reliability and validity reported
- [ ] Estimator matches nesting; ICC and centering choices stated for multilevel models
- [ ] Every claimed country difference backed by a formal difference test
- [ ] Small-N-countries limits acknowledged; no continuous-dimension claims from 4 countries
- [ ] Headline results carry cross-border managerial magnitudes

## Anti-patterns

- Comparing raw scale means across countries with no scalar-invariance evidence
- "Significant in Germany, not in Brazil" offered as evidence of moderation
- Country dummies interpreted as cultural effects
- HLM with 6 countries and three country-level predictors
- Pooled reliability statistics hiding a collapsed construct in one country
- An invariance failure silently absorbed by dropping the offending country

## Output format

```text
【Invariance】per construct: configural/metric/scalar (full/partial/alignment) + decision rule
【Licensed comparisons】means / paths / neither — per construct
【Estimator】structure-matched model + clustering/centering choices
【Country-difference tests】formal Δ-tests for each claimed difference: done?
【Managerial magnitude】headline effect in cross-border decision units
【Robustness】response styles / small-N limits / identification threat addressed
【Next skill】jim-contribution-framing
```
