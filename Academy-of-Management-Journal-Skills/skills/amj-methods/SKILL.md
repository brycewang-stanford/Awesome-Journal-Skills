---
name: amj-methods
description: Use when the research design and method are the bottleneck for an Academy of Management Journal (AMJ) manuscript — matching design (archival, survey, experiment, multi-method, field) and level of analysis to the theoretical question. Designs the study; it does not run the estimation or validity checks (amj-data-analysis).
---

# Research Design & Methods (amj-methods)

## When to trigger

- The design may not match the theory's level, timing, or causal claim
- Data are single-source, single-wave, and self-reported (common-method bias risk)
- The theory is causal but the design is cross-sectional/correlational
- Constructs lack established, validated measures
- A reviewer says "the design cannot test this hypothesis" or "endogeneity is unaddressed"

## Match the design to the question

AMJ explicitly welcomes **all empirical methods** — qualitative, quantitative, field, laboratory, meta-analytic, and mixed. The bar is *fit and rigor*, not a single preferred method, and qualitative designs are held to an equally demanding standard (the Eisenhardt multiple-case approach and the Gioia methodology for grounded qualitative rigor are the field's reference points).

| Theoretical claim                          | Design that earns it                                     |
|--------------------------------------------|----------------------------------------------------------|
| Causal effect of a manipulable cause       | Experiment (lab/field/online), or natural experiment     |
| Process unfolding over time                | Multi-wave panel; longitudinal/lagged design             |
| Firm/strategy outcomes from archival cause | Panel archival with fixed effects + endogeneity strategy |
| Cross-level mechanism (e.g., team→indiv.)  | Multilevel/nested data with HLM-appropriate structure    |
| Rich, novel, or contested phenomenon       | Qualitative or multi-method (often paired with a study 2)|

A two-study design (e.g., field study for generalizability + experiment for causal mechanism) is a common AMJ strength — it answers both internal and external validity.

## Designing against the threats AMJ cares about

- **Common-method bias (CMB)**: separate sources for predictor and outcome; temporal separation across waves; objective/archival outcomes where possible. Procedural remedies beat statistical fixes (the Podsakoff et al. guidance is the standard reference). Plan this *before* collecting data.
- **Endogeneity (archival)**: anticipate omitted variables, reverse causality, and selection. Plan an identification strategy (instrument, natural experiment, panel fixed effects, difference-in-differences, Heckman/2SLS, propensity matching) and the assumptions each requires.
- **Measurement**: use validated multi-item scales; pilot new measures; plan a CFA. State the level at which each construct is measured and how cross-level data are aggregated (with justification: ICC, r_wg, aggregation theory).
- **Sampling and power**: justify the sampling frame, response rate, and statistical power for the focal and interaction effects (interactions need more power).

## Level-of-analysis discipline

State the level for theory, measurement, and analysis, and keep them aligned. If theory is at the team level but data are individual, justify aggregation; if effects are cross-level, the analysis must model the nesting (do not run OLS on nested data).

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AMJ is empirical management — panel, multilevel, DiD, IV, and field/lab experiments; the chain below serves that lane, while grounded-theory / qualitative work uses its own standards.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design can actually test each hypothesis (causal claims have causal leverage)
- [ ] CMB addressed by procedural design (separate sources/time), not just a post-hoc test
- [ ] Endogeneity strategy specified for archival/observational causal claims
- [ ] Constructs use validated measures; new measures piloted; CFA planned
- [ ] Level of analysis consistent across theory, measurement, and analysis; aggregation justified
- [ ] Sampling frame, response rate, and power (including for interactions) justified
- [ ] Where feasible, a second study triangulates the causal mechanism

## Anti-patterns

- **Cross-sectional causal claims**: "X causes Y" from one-wave correlational data.
- **CMB as afterthought**: relying solely on a Harman single-factor test instead of designed separation.
- **Ignored endogeneity**: archival "effect" with an obviously endogenous regressor and no strategy.
- **Mismatched levels**: theorizing at the team level, testing with disaggregated individual data via OLS.
- **Unvalidated home-grown scales** with no evidence of reliability or construct validity.
- **Underpowered interactions** presented as null "boundary conditions."

## Output format

```
【Design】experiment / panel-archival / multilevel survey / qualitative / multi-method
【Hypothesis-design fit】each H testable? notes ...
【CMB plan】procedural remedies ...
【Endogeneity strategy】(if archival) instrument / NE / FE / DiD / matching ...
【Measures】validated? new (piloted)? CFA planned?
【Levels】theory / measurement / analysis aligned? aggregation justification ...
【Power & sampling】frame, N, power for interactions ...
【Next step】amj-data-analysis
```
