---
name: jhe-identification
description: Use when the identification argument is the bottleneck for a Journal of Health Economics (JHE) manuscript — quasi-experimental health-policy variation, selection into insurance/treatment, eligibility RD, or structural identification of demand/provider parameters. Stress-tests the data-to-estimand mapping to the JHE bar before exhibits are finalized; it does not write prose or build the package.
---

# Identification Strategy (jhe-identification)

## When to trigger

- A causal health-policy claim rests on OLS + controls or TWFE on staggered state adoptions
- An insurance/treatment effect is contaminated by selection that is not modeled
- An eligibility cutoff (income, age-65 Medicare, kink in subsidy schedule) is used without an RD defense
- A structural insurance-demand or provider-response parameter is estimated but it is unclear what identifies it
- You are unsure the design clears JHE's credible-causal-plus-institutional bar

## The JHE identification bar

JHE referees demand **credible causal identification *and* institutional realism**: the mapping from a source of variation to the health-economics estimand must be explicit, falsifiable, and consistent with how the program or market actually works. Two failure modes get punished hardest here: (1) ignoring **selection** — into insurance, into treatment, into the sample — that the health setting makes first-order; and (2) treating a **policy variation as exogenous** when institutional detail (phase-ins, waivers, simultaneous reforms, anticipation) says it is not. State the estimand, name the assumption, show the diagnostic that could have failed, and keep the claim inside what the design supports. Inference clusters at the policy/assignment level (usually state).

## Design paths

### Path A: Quasi-experimental health-policy variation (DiD / event study)
- Medicaid/Medicare expansions, insurance mandates, state reforms: with staggered timing **move beyond TWFE** (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille, Borusyak–Jaravel–Spiess).
- Clean **event-study with leads** for pre-trends; Goodman-Bacon decomposition; Rambachan–Roth honest-DID sensitivity.
- Rule out **concurrent reforms** (other ACA provisions, simultaneous payment changes) and **anticipation/woodwork** effects — the institutional threat referees raise first.

### Path B: Selection into insurance / treatment
- Make the selection model explicit: is identification from random/quasi-random assignment, or from a selection-correction (Heckman, control function, bounds)?
- For coverage effects, separate **take-up, crowd-out, and ex-post moral hazard**; a reduced-form "coverage effect" that blends them is not identified for welfare.
- Where selection is unavoidable, report **bounds** (Lee/Manski) rather than asserting ignorability.

### Path C: Eligibility RD / kink
- Age-65 Medicare, income-threshold subsidies, BMI/clinical cutoffs: **density test** (McCrary / Cattaneo–Jansson–Ma) for manipulation; covariate smoothness; local-linear with data-driven bandwidth and **bias-corrected robust CIs** (rdrobust).
- State the estimand is the **local effect at the cutoff** and resist extrapolation to the whole eligible population.

### Path D: IV / structural identification
- IV (e.g., distance-to-provider, simulated eligibility, judge/examiner leniency): strong first stage (effective F), exclusion argued from institutions + falsification; weak-IV-robust sets (Anderson–Rubin).
- Structural demand/provider models: **name what identifies each parameter** (a price/cost-sharing kink identifies the demand elasticity; a coverage discontinuity identifies the selection parameter), report sensitivity to identifying moments, and Monte Carlo recovery.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JHE is health economics — insurance/program reforms and selection; foreground DiD/IV/RDD and selection corrections.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design chosen; the variation-to-estimand mapping stated in one sentence
- [ ] Estimand named (ITT / LATE / ATT / local-at-cutoff / structural parameter) and matched to the design
- [ ] Selection threat addressed explicitly (modeled, bounded, or argued away with evidence)
- [ ] Institutional confounds ruled out: concurrent reforms, phase-ins, anticipation, woodwork
- [ ] Design-appropriate diagnostic shown (pre-trends+Bacon / density+bandwidth / first-stage+exclusion / moment sensitivity)
- [ ] Modern estimator where TWFE or 2SLS would bias; inference clustered at the policy level
- [ ] The claim never exceeds the design (coverage effect ≠ health-production effect ≠ welfare)

## Anti-patterns

- TWFE on staggered Medicaid/state adoptions with no heterogeneity-bias discussion
- A "coverage effect" read as a health or welfare effect with no take-up/crowd-out/moral-hazard decomposition
- Treating a policy as exogenous while ignoring simultaneous reforms or anticipation
- RD on an eligibility cutoff with no density/manipulation test or a hand-picked bandwidth
- Asserting an instrument is exogenous (distance, simulated eligibility) with no falsification
- Clustering below the policy level so standard errors are understated

## Worked vignette (illustrative)

A paper studies a state Medicaid expansion using TWFE across staggered adoption years; a referee flags negative weighting and a thin parallel-trends story. The JHE fix: re-estimate with Callaway–Sant'Anna by adoption cohort, show flat pre-trend leads, report a Goodman-Bacon decomposition (say 21% of the TWFE estimate came from forbidden already-treated comparisons, illustrative), and add an honest-DID bound. Then decompose the headline "coverage effect" into take-up (4.1pp, s.e. 1.0) and downstream utilization, and rule out the concurrent ACA marketplace launch with a placebo on a non-eligible income band. The referee now sees an identified, institutionally-honest estimate, not a blended reduced form.

## Referee pushback mapped to the identification fix

- *"This is selection, not the causal effect."* → Decompose take-up / crowd-out / moral hazard; report a bound (Lee/Manski/Oster) rather than adding controls.
- *"A concurrent reform drives your result."* → Placebo on an ineligible group or period; rule out the simultaneous policy by timing in the institutional section.
- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna or Sun–Abraham; show flat event-study leads and a Goodman-Bacon decomposition.
- *"Your eligibility cutoff is manipulable."* → Density test (McCrary / CJM); covariate smoothness; bandwidth sensitivity and a donut check.
- *"You read a local/coverage estimate as a population/welfare effect."* → State the estimand precisely and resist extrapolation, or add the model that licenses it (`jhe-theory-model`).

## A note on health-specific identification traps

Three pitfalls recur in health data and sink otherwise clean designs. First, **mortality selection / survivorship**: effects on a surviving population (e.g., spending among those who live) confound treatment with differential survival — bound it or model it. Second, **coding and measurement endogeneity**: a payment reform can change *how* care is coded, so a measured "intensity" change may be relabeling, not real care — validate against an unaffected outcome. Third, **woodwork / anticipation**: coverage expansions pull in already-eligible non-enrollees and providers anticipate phase-ins, contaminating both treatment and control timing — handle with leads and an institutional timeline.

## Output format

```text
【Design】policy-DiD / selection / eligibility-RD / IV / structural
【Variation-to-estimand mapping】one sentence
【Estimand】ITT / LATE / ATT / local-at-cutoff / structural parameter
【Selection + institutional threats handled】[take-up/crowd-out split, concurrent-reform placebo, ...]
【Identification evidence】[pre-trends+Bacon / density+bandwidth / first-stage+exclusion / moment sensitivity]
【Estimator + inference】modern estimator; clustering level; honest-DID/weak-IV sensitivity if any
【What it does NOT identify】[...]
【Next skill】jhe-theory-model (if a model is needed) or jhe-robustness
```

## Handoff boundary

This skill stress-tests the data-to-estimand mapping; it does not build the robustness ledger (`jhe-robustness`) or the model that turns an estimate into welfare (`jhe-theory-model`). Once the design is defensible and the estimand is stated, hand off: to `jhe-theory-model` if interpretation needs structure, otherwise straight to `jhe-robustness` to show the identified estimate is stable. Do not let identification work bleed into exhibit polishing — the design must settle first.
