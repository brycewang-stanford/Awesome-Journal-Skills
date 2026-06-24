---
name: isr-methods
description: Use when choosing and stress-testing the research design for an Information Systems Research (ISR) manuscript — matching the genre (behavioral empirical, analytical-economic modeling, design-science, or multimethod) to the question, and ensuring the design can actually support the IS contribution. Designs the study; it does not execute the estimation/derivation (isr-data-analysis) or frame the contribution (isr-contribution-framing).
---

# Research Design & Method Fit (isr-methods)

## When to trigger

- You are unsure which genre best supports your IS claim
- The design may not be able to identify the effect (empirical) or may rest on unjustified assumptions (analytical)
- You are combining methods and need the multimethod logic to hold together
- A reviewer says "the method cannot answer the question" or "the artifact is not evaluated"

## Match the genre to the claim

ISR is deliberately pluralistic; no single method is mandated. Choose the genre the **claim** demands:

| Claim / phenomenon                                              | Genre & design                                                         |
|----------------------------------------------------------------|------------------------------------------------------------------------|
| Causal effect of an IT design/policy on behavior or outcomes   | Field/lab experiment, or quasi-experiment with identification          |
| How/why IT use is enacted, appropriated, organized             | Qualitative / interpretive (interviews, ethnography, case)             |
| Equilibrium behavior of platforms, pricing, security, contracts | Analytical economic / game-theoretic model                            |
| A novel IT artifact that solves a class of problems            | Design science — build **and** rigorous evaluation                     |
| Value/impact of IT investment at firm/market level             | Archival econometrics with a credible identification strategy          |
| Mechanism + scope + generalization in one paper                | Multimethod (per ISR 36(2) framework) with an explicit integration logic |

## Genre-specific design discipline

- **Behavioral empirical.** Establish construct validity by design (multi-item validated scales, manipulation/attention checks), separate sources/waves to limit common-method bias, justify the sampling frame, and (for experiments) pre-register and power for interactions, not just main effects.
- **Analytical modeling.** The design *is* the model: state agents, timing, information structure, and equilibrium concept; defend each assumption; plan the comparative statics and the extensions/robustness that show the result is not an artifact of one assumption. Reserve full proofs for the electronic companion.
- **Design science.** Specify the artifact, the design objectives, and an **evaluation** that demonstrates utility (benchmarks, controlled studies, real-world deployment) — a build without evaluation is not a DSR contribution.
- **Archival/causal.** Name the identification strategy (DiD, IV, RDD, matching) and the threat it addresses; a regression without identification is descriptive.

## Sociotechnical level and fit

State the level(s) of analysis and ensure the design observes the level where the mechanism operates (e.g., group-level theory needs group-level variation). Cross-level claims need cross-level data.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ISR is empirical IS with strong econometric and experimental work; identification (DiD / IV) for observational claims, randomization inference for experiments.

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

- [ ] Genre matches the claim; not chosen by habit or data availability
- [ ] Empirical: identification/validity strategy named and adequate
- [ ] Analytical: assumptions justified; comparative statics and robustness planned
- [ ] DSR: artifact + evaluation that demonstrates utility
- [ ] Level(s) of analysis observed where the mechanism operates
- [ ] Multimethod combinations have an explicit integration logic (ISR 36(2))
- [ ] Page budget planned (32-page text cap) with overflow routed to the electronic companion

## Anti-patterns

- **Method by convenience**: using the data you have rather than the design the claim needs.
- **Regression theater**: archival regressions presented as causal without identification.
- **Build-only DSR**: an artifact with no rigorous evaluation.
- **Multimethod garnish**: a second method bolted on without theoretical integration.

## Output format

```
【Claim】[...]
【Genre & design】experiment / qualitative / analytical / DSR / archival / multimethod
【Identification or assumptions】[...]
【Level(s) observed】[...]
【Validity/robustness plan】[...]
【Page/EC budget】[...]
【Next step】isr-data-analysis
```
