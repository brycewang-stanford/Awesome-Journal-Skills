---
name: wber-identification
description: Use when the causal identification argument is the bottleneck for a The World Bank Economic Review (WBER) manuscript — RCT/program evaluation, DiD/event study around a reform, regression discontinuity, or IV in a developing-country setting. Stress-tests the data-to-estimate mapping AND the external-validity/policy-interpretation step to the WBER bar; it does not write prose or build the package.
---

# Identification Strategy (wber-identification)

## When to trigger

- A causal claim rests on OLS + controls, or TWFE on staggered reform timing
- An RCT's estimand, balance, attrition, or spillover handling is not pinned down
- An RD's density, bandwidth, or covariate-smoothness defense is missing
- An IV's first stage is weak or the exclusion restriction is asserted, not argued
- The design is clean but the *policy interpretation* (scale-up, GE, fiscal cost) is missing

## The WBER identification bar

WBER demands the **same identification rigor as a top applied-micro field journal** — and then one more thing that siblings let slide: the **mapping from the local causal estimate to a development-policy lesson** must be argued, not assumed. A pristine ITT from one trial is necessary but not sufficient; the WBER referee asks "what does this imply for a finance ministry deciding whether to scale this?" So state the estimand, name the identifying assumption, show the diagnostic that could have failed, **and** address external validity, general equilibrium, and scaling. Inference must match the design (clustering at the assignment level; few-cluster corrections). Report standard errors and confidence intervals — not significance asterisks.

## Design paths

### Path A: RCT / program evaluation (own or admin data)
- **Estimand stated** (ITT vs. LATE/TOT); randomization unit and stratification described.
- **Pre-registration** where applicable (AEA RCT Registry / OSF); report deviations from the analysis plan.
- **Balance table** on baseline covariates; **attrition** examined and bounded (Lee bounds if differential) — attrition is endemic in field settings.
- **Spillovers / SUTVA**: in dense developing-country settings, treatment can leak to controls; design or test for it.
- **Multiple-hypothesis adjustment** across outcomes/subgroups; explicit external-validity and scale-up discussion.

### Path B: Difference-in-differences / event study around a reform
- With staggered adoption, **move beyond TWFE** — Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille, or Borusyak–Jaravel–Spiess imputation.
- **Clean event-study with leads** for pre-trends; report a Goodman-Bacon decomposition.
- State and defend **parallel trends**; consider Rambachan–Roth honest-DiD sensitivity. Developing-country reforms are often non-random in timing — argue why.

### Path C: Regression discontinuity (eligibility thresholds, geographic borders)
- **Density / manipulation test** (McCrary / Cattaneo–Jansson–Ma); covariate smoothness at the cutoff.
- **Local-linear** with data-driven bandwidth; **bias-corrected robust CIs** (rdrobust); donut and bandwidth-sensitivity checks.
- Many development RDs are **proxy-means-test** or poverty-line cutoffs — guard against score manipulation by enumerators or applicants.

### Path D: IV / shift-share
- **Strong first stage** (effective F); with weak instruments use Anderson–Rubin / weak-IV-robust sets.
- **Exclusion restriction** argued from institutions/theory + falsification. Be wary of tired development instruments (rainfall, distance, colonial-era variables) — argue exogeneity, do not invoke by tradition.

## The external-validity layer (the WBER differentiator)

- **From LATE to policy:** name *whose* effect you estimate and how the complier population differs from the scale-up population.
- **General equilibrium:** a partial-equilibrium treatment effect can vanish or reverse at scale (wages, prices, congestion). Acknowledge and, where possible, bound it.
- **Fiscal cost / cost-effectiveness:** WBER readers weigh effects against budgets — a cost-per-outcome or benefit-cost figure makes the result actionable.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). WBER is development economics — RCTs and observational designs in low/middle-income settings; randomization inference + DiD/IV, magnitude in policy units.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design chosen; variation-to-estimand mapping stated in one sentence
- [ ] Estimand named (ITT/LATE/ATT/local-at-cutoff) and matched to the design
- [ ] Design-appropriate diagnostic shown (balance+attrition+spillovers / pre-trends+Bacon / density+bandwidth / first-stage+exclusion)
- [ ] Modern estimator used where TWFE or 2SLS would bias
- [ ] Inference clustered at the assignment level; few-cluster corrected
- [ ] External validity, GE, and scaling/fiscal cost explicitly addressed
- [ ] SEs and CIs reported (no asterisks); claim never exceeds what the design identifies

## Anti-patterns

- A clean trial with zero discussion of external validity or scale-up — reads as a project report
- TWFE on staggered reform timing with no heterogeneity-bias discussion
- A development RD with no density test at a proxy-means or poverty-line cutoff
- Rainfall/distance/colonial IVs invoked by tradition with no exclusion argument
- Reading a local LATE as the population ATE for a national scale-up
- Asterisks instead of clustered SEs / weak-IV-robust sets

## Referee pushback mapped to the identification fix

- *"Staggered TWFE here is biased."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show flat event-study leads and a Goodman-Bacon decomposition.
- *"Your instrument is rainfall/distance — assert exclusion at your peril."* → Argue the exclusion restriction from institutions and falsify it (reduced form on never-takers, placebo outcomes); if it fails, drop the IV.
- *"This RD eligibility score is manipulable by enumerators."* → Report a density test, covariate smoothness, and a donut estimate; discuss the assignment mechanism.
- *"Differential attrition contaminates the trial."* → Show attrition by arm and Lee bounds; if spillovers are plausible, test or design for them.
- *"A three-district LATE tells me nothing about a national program."* → Characterize the complier population, bound the GE channel, and report a cost-per-outcome at scale.

## Worked vignette (illustrative)

A paper evaluates a fee-elimination reform rolled out across districts in staggered years using TWFE; a referee flags negative weighting. The WBER fix: re-estimate with Callaway–Sant'Anna by adoption cohort, show flat pre-trend leads, report a Goodman-Bacon decomposition (say 15% of the TWFE estimate came from forbidden already-treated comparisons, illustrative). The cohort-robust ATT settles at 4.3pp enrollment (s.e. 1.1). Then the WBER-specific step: the authors note the complier districts were poorer than average, bound the GE wage effect on teachers, and report a cost-per-additional-enrollee, turning a clean ATT into a scale-up-relevant number.

## Output format

```text
【Design】RCT / DiD / RD / IV
【Variation-to-estimand mapping】one sentence
【Estimand】ITT / LATE / ATT / local-at-cutoff
【Identification evidence】[balance+attrition+spillovers / pre-trends+Bacon / density+bandwidth / first-stage+exclusion]
【Estimator + inference】modern estimator; clustering level; weak-IV/honest-DiD sensitivity if any
【External validity】complier vs. scale-up population; GE; cost-effectiveness
【What it does NOT identify】[...]
【Next step】wber-theory-model (if interpretation needs a model) or wber-robustness
```
