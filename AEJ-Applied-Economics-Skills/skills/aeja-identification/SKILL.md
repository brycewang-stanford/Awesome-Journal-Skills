---
name: aeja-identification
description: Use when the causal identification argument is the bottleneck for an American Economic Journal: Applied Economics (AEJ: Applied) manuscript — RCT, difference-in-differences/event study, regression discontinuity, IV, or shift-share. Stress-tests the data-to-causal-estimate mapping to the AEJ: Applied credibility bar before exhibits are finalized; it does not write the prose or build the package.
---

# Identification Strategy (aeja-identification)

## When to trigger

- A causal claim rests on OLS + controls, or TWFE on staggered timing
- An RCT's estimand, balance, or attrition handling is not pinned down
- An RD's density, bandwidth, or covariate-smoothness defense is missing
- An IV's first stage is weak or the exclusion restriction is asserted, not argued
- You are unsure the design clears AEJ: Applied's credibility bar

## The AEJ: Applied identification bar

AEJ: Applied is **identification-driven applied micro**: the **mapping from a source of variation to the causal estimand must be explicit, defended, and falsifiable**. Editors and referees here are unusually sophisticated about modern design pitfalls — staggered-DID bias, weak IV, RD manipulation, shift-share exogeneity. State the estimand, name the identifying assumption, show the diagnostic that could have failed but didn't, and keep the claim inside what the design supports. Inference must match the design (clustering at the assignment level; few-cluster corrections).

## Design paths

### Path A: RCT / field experiment (own data)
- **Estimand stated** (ITT vs. LATE/TOT); randomization unit and stratification described.
- **Pre-registration** (AEA RCT Registry / AsPredicted / OSF); report deviations from the pre-analysis plan.
- **Balance table** on baseline covariates; **attrition** examined and bounded (Lee bounds if differential).
- **Multiple-hypothesis adjustment** across outcomes/subgroups; explicit external-validity discussion.

### Path B: Difference-in-differences / event study
- With staggered adoption, **move beyond TWFE** — Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille, or Borusyak–Jaravel–Spiess imputation.
- **Clean event-study with leads** for pre-trends; report a Goodman-Bacon decomposition to show which 2×2s drive the estimate.
- State and defend **parallel trends**; consider Rambachan–Roth honest-DID sensitivity to parallel-trend violations.

### Path C: Regression discontinuity
- **Density test** (McCrary / Cattaneo–Jansson–Ma) for manipulation; covariate smoothness at the cutoff.
- **Local-linear** with data-driven bandwidth; **bias-corrected, robust CIs** (rdrobust); donut and bandwidth-sensitivity checks.
- State whether the estimand is the local effect at the cutoff and resist extrapolation.

### Path D: IV / shift-share
- **Strong first stage** (effective F / Montiel-Olea–Pflueger); with weak instruments use Anderson–Rubin / weak-IV-robust sets.
- **Exclusion restriction** argued from institutions/theory + falsification (reduced-form on never-takers, placebo outcomes).
- Shift-share: defend exogeneity of **shares** or **shocks** (Goldsmith-Pinkham–Sorkin–Swift / Borusyak–Hull–Jaravel) and report the implied just-identified weights.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AEJ: Applied is applied microeconomics — labor, health, education, and development field settings where a clean research design is the entry ticket.

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
## Checklist

- [ ] Design chosen; the variation-to-estimand mapping stated in one sentence
- [ ] Estimand named (ITT/LATE/ATT/local effect) and matched to the design
- [ ] Design-appropriate diagnostic shown (balance+attrition / pre-trends+Bacon / density+bandwidth / first-stage+exclusion)
- [ ] Modern estimator used where TWFE or 2SLS would bias
- [ ] Inference clustered at the assignment level; few-cluster issue addressed (wild-cluster bootstrap)
- [ ] The claim never exceeds what the design identifies (no extrapolation beyond the local/ITT object)

## Anti-patterns

- TWFE on staggered treatment with no heterogeneity-bias discussion
- An RCT with no pre-registration, no balance table, or unexamined differential attrition
- RD with no density/manipulation test or with a hand-picked bandwidth
- "The instrument is plausibly exogenous" asserted with no falsification
- Reporting significance with asterisks but no clustered standard errors or weak-IV-robust set
- Reading a local RD or LATE estimate as if it were the population ATE

## Worked vignette (illustrative)

A paper studies a job-training program rolled out across states in staggered years. The first draft uses TWFE and a referee flags negative weighting. The AEJ: Applied fix: re-estimate with Callaway–Sant'Anna by cohort, show flat pre-trend leads, and report a Goodman-Bacon decomposition revealing that 18% of the TWFE estimate came from contaminating already-treated comparisons (illustrative). The heterogeneity-robust ATT settles at 3.1pp (s.e. 0.9), and an honest-DID bound shows the result survives a plausible parallel-trend violation.

## Output format

```
【Design】RCT / DID / RD / IV / shift-share
【Variation-to-estimand mapping】one sentence
【Estimand】ITT / LATE / ATT / local-at-cutoff
【Identification evidence】[balance+attrition / pre-trends+Bacon / density+bandwidth / first-stage+exclusion]
【Estimator + inference】modern estimator; clustering level; weak-IV/honest-DID sensitivity if any
【What it does NOT identify】[...]
【Next step】aeja-theory-model (if interpretation needs a model) or aeja-robustness
```
