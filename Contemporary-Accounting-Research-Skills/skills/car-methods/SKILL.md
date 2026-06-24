---
name: car-methods
description: Use when the research design and identification are the bottleneck for a Contemporary Accounting Research (CAR) manuscript — choosing and defending an archival, experimental, analytical, field, or survey design and, for human-participant work, meeting CAR's mandatory ethics-approval verification. Designs the study; it does not run the estimation (car-data-analysis).
---

# Research Design & Methods (car-methods)

## When to trigger

- The design may not deliver the inference the question needs (identification, internal validity, equilibrium logic)
- An archival causal claim rests on an endogenous regressor with no strategy
- An experiment's manipulation may not isolate the theorized construct
- The study involves human participants and ethics-approval verification is unprepared
- A reviewer says "the design cannot support this claim"

## Match the design to the question (CAR is method-agnostic)

CAR welcomes any appropriate method; the bar is *fit and rigor*, not a preferred method. Pick the design that earns the claim:

| Claim                                              | Design that earns it                                            |
|----------------------------------------------------|-----------------------------------------------------------------|
| Capital-market/contracting effect of reporting      | Panel archival with fixed effects + an identification strategy  |
| Causal effect of an information feature on judgment  | Controlled experiment (lab/online/professional subjects)        |
| Existence/optimality of an equilibrium or contract  | Analytical model: primitives, equilibrium concept, proofs       |
| Mechanism inside firms, audits, or standard-setting  | Field study / interviews with an explicit coding protocol       |
| A new construct's measurement and external validity  | Survey with a validated instrument; or multi-method             |

A two-study design (e.g., an experiment isolating the mechanism behind an archival association) is a recognized CAR strength.

## Design against the threats CAR reviewers probe

- **Identification (archival).** Anticipate omitted variables, reverse causality, and selection; plan a strategy (natural experiment, difference-in-differences with a credible parallel-trends argument, instrument, entropy balancing/matching, firm/year fixed effects) and state the assumptions each requires.
- **Internal validity (experimental).** Design manipulation and attention checks; randomize; pre-specify the predicted mediator; rule out demand effects and confounds; justify the participant pool (student, online, or professional) for the inference.
- **Model discipline (analytical).** Justify each assumption and the equilibrium concept; show which results are robust to relaxing assumptions.

## CAR-specific design requirements

- **Ethics-approval verification (mandatory).** For *any* research involving human participants — experiments, interviews, surveys, including secondary human-participant data — you must obtain and upload institutional REB/IRB clearance, an REB-issued exemption, or a senior-administrator letter where no review board exists. A bare assertion is not accepted, and failure is grounds for withdrawal by the EIC. Plan this *before* data collection.
- **Instrument capture.** Surveys/experiments must submit the full research instrument with the manuscript (Data Integrity policy, item 1).
- **Proprietary/field data.** If you use proprietary organizational data, plan a credible means of verifying the data source/site on editor request and disclose any non-disclosure restrictions (policy item 2).

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). CAR is archival/empirical accounting; the DiD / IV / RDD chain serves its causal designs around reporting and regulation.

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

- [ ] Design can support each prediction (identification / internal validity / equilibrium logic)
- [ ] (Archival) endogeneity strategy specified with its assumptions
- [ ] (Experimental) manipulation/attention checks, randomization, predicted mediator, pool justified
- [ ] (Analytical) assumptions and equilibrium concept justified; robustness mapped
- [ ] Ethics-approval verification secured for any human participants
- [ ] Full instrument prepared; proprietary-data verification/NDA plan in place

## Anti-patterns

- **Cross-sectional causal claims** from one-period archival correlations with no strategy.
- **Confounded manipulations** that move more than the theorized construct.
- **Assumption-driven results** (analytical) never tested for robustness.
- **Treating ethics approval as a formality** — CAR requires documented verification, not a statement.

## Output format

```
【Design】panel-archival / experiment / analytical / field / survey / multi-method
【Inference fit】each prediction supportable? notes ...
【Identification / internal validity / equilibrium】strategy + assumptions ...
【Ethics】REB/IRB clearance, exemption, or senior-admin letter secured?
【Instrument & proprietary data】full instrument; verification/NDA plan ...
【Next step】car-data-analysis
```
