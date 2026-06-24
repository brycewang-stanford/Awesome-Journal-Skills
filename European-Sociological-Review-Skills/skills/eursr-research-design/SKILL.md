---
name: eursr-research-design
description: Use when defending the research design of a European Sociological Review (ESR) manuscript — comparative cross-national designs, panel/longitudinal and event-history designs, multilevel structures, and causal inference where feasible on harmonized survey or register data. ESR judges whether the design lets the comparison or panel identify the mechanism. Strengthens the design; it does not write code.
---

# Research Design (eursr-research-design)

ESR is a quantitative journal exacting about whether the **comparative or longitudinal design actually
identifies the mechanism** from `eursr-theory-building` and rules out the leading confound. The design
must connect the cross-level hypothesis to evidence that a single cross-section could not provide.

## When to trigger

- Specifying the comparative frame, the panel structure, sampling, or the identification strategy
- A reviewer questioned causal claims, generalization, selection, measurement comparability, or a confound
- Justifying why your design adjudicates the rival account from `eursr-literature-positioning`

## Comparative / cross-national
- **Justify the country set** by design logic (institutional contrast, regime types, most/least-similar),
  not by data availability alone; say what variation each context contributes.
- **Measurement equivalence** is the first reviewer demand: establish that constructs mean the same
  across countries (configural/metric/scalar invariance for latent scales; harmonized coding for
  education via ISCED/CASMIN, occupation via ISCO/ISEI/EGP).
- **Macro N is small.** With ~20-30 countries, country-level effects rest on few degrees of freedom —
  design the macro hypothesis so it does not over-claim from a handful of clusters (see
  `eursr-data-analysis`).

## Panel / longitudinal / event-history
- **State what the panel buys.** Within-person change (fixed effects), duration/timing (event history),
  or growth (latent growth) — match the estimator to the theoretical quantity.
- **Attrition and selection** into and out of the panel must be addressed (weights, IPW, sensitivity).
- For staggered policy exposure, use **heterogeneity-robust DiD** (Callaway-Sant'Anna, Sun-Abraham,
  Borusyak et al.), not naive TWFE.

## Causal inference where feasible
- Much of ESR is observational; **distinguish description, association, and causation honestly**. If
  causal, state the assumptions (ignorability, parallel trends, exclusion) and defend them; report a
  **sensitivity bound** (how strong an unobserved confounder would have to be).

## Multilevel / SEM
- Specify the level structure (individuals in countries/regions/cohorts), the random effects, and why a
  multilevel model is warranted; for measurement, build the latent model before the structural one.

## The adjudication test (ESR-specific)

For the **single strongest rival explanation**: *"If the rival were true rather than my argument, the
cross-national (or over-time) pattern would look like ___; instead it looks like ___."* If you cannot
write it, the comparative/panel design does not yet identify the contribution.

## What ESR referees demand of each design

| Design | Referee's first demand | Satisfying move |
|--------|------------------------|------------------|
| Comparative cross-national | "Are the measures equivalent?" | invariance / harmonized coding; justified country set |
| Panel / fixed-effects | "What does within-person change identify?" | match estimator to the quantity; handle attrition |
| Event history | "Right risk set and time scale?" | defined onset, censoring, time-varying covariates |
| Causal (DiD/IV/RDD) | "Assumption defended?" | state + test the assumption; sensitivity bound |
| Multilevel / SEM | "Enough clusters; measurement first?" | macro df honesty; fit the latent model before structure |

## Worked micro-example (illustrative)

A comparative study argues that vocational specificity smooths the school-to-work transition.

```
Country set: most-different welfare/training regimes (e.g., dual-system vs. general-education systems),
  chosen for institutional contrast, not convenience
Measurement: education harmonized via ISCED; vocational specificity coded from program-level data
Design: cross-national + cohort variation; cross-level interaction (specificity × individual track)
Disconfirming pattern sought: if signaling (not skills) drove it, the advantage would vanish once firms
  learn quality → instead it persists across the early career, as the specificity argument predicts
Macro-N caution: ~24 countries → country-level claim kept modest; SEs / df handled in data-analysis
```

The country set is design-driven, the measures are comparable, and the design specifies what pattern would falsify the argument.

## Referee pushback → ESR-specific fix

- *"Measures aren't comparable across countries."* → Test invariance; report partial invariance and
  what it permits; use harmonized coding schemes.
- *"You infer too much from ~20 countries."* → Re-state the macro claim modestly; use df-appropriate
  inference (see `eursr-data-analysis`).
- *"Association dressed as causation."* → Restate what the design identifies; add a sensitivity bound or
  placebo; drop causal verbs you cannot defend.

## Calibration anchors

- **Measurement equivalence is the comparative gate.** A cross-national claim built on non-equivalent
  scales is the most common fatal design flaw at ESR.
- **The adjudication sentence is the test.** If you can't write "if the rival were true the pattern
  would look like ___," the comparison/panel does not yet earn the contribution.
- **Identification honesty travels.** Stating plainly what observational European data can and cannot
  establish reads as strength to a quantitative panel.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ESR is comparative quantitative sociology; cross-country panels with confounded institutions — foreground fixed effects and clustering.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference, `romano_wolf` for many-outcome
  family-wise control, and `mediate` for mediation (not naive controlling-away).
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the effect size in interpretable units; route the full battery to the
appendix/supplement. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- A country set chosen by data availability and dressed up as theory-driven
- Cross-national latent comparisons with no measurement-invariance check
- Over-claiming country-level effects from a handful of clusters
- Naive TWFE on staggered policy timing; ignoring panel attrition
- A design that cannot distinguish your mechanism from the leading alternative

## Output format

```
【Design】comparative / panel / event-history / causal / multilevel-SEM
【What it identifies】description / association / causation
【Comparability / assumption】invariance or key assumption + how defended
【Rival ruled out】the adjudication sentence
【Macro-N / attrition / sensitivity】planned
【Next】eursr-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — multilevel / SEM / event-history / DiD tooling
- [`../../resources/code/`](../../resources/code/) — reproducible Stata + Python causal-inference skeleton (DiD/IV/RDD/DML)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ESR methodological expectations
