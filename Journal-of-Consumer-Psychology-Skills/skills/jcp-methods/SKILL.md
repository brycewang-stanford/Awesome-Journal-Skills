---
name: jcp-methods
description: Use when designing or stress-testing the experiments for a Journal of Consumer Psychology (JCP) manuscript — manipulations, controls and confounds, manipulation checks, power, the multi-study chain, and pre-registration. Designs the studies that test the process; it does not analyze them (jcp-data-analysis).
---

# Experimental Design & Methods (jcp-methods)

## When to trigger

- You have a mechanism but are unsure which experiments can actually isolate it
- A reviewer questions whether your manipulation moves the construct it claims to
- Mediation rests on a single measured mediator and you need stronger process evidence
- Sample sizes were chosen by convention, not by an a priori power analysis
- You are deciding whether to pre-register, or whether to take the Registered Report route (待核实)

## JCP's design bar: causal isolation of a psychological process

JCP is an **experimental journal**: random assignment, manipulated independent variables, and measured (or manipulated) mediators are the default. The design must do more than show an effect — it must **rule out that the effect is anything other than the proposed process**. Since the rigor reforms of the 2010s, JCP reviewers expect adequately powered cells, clean manipulations with checks, pre-registered confirmatory studies where feasible, and a multi-study package whose studies each test a different link in the causal chain rather than re-running the same demonstration.

## The multi-study chain

A persuasive JCP package walks the mechanism:

1. **Existence** — establish the effect cleanly with a strong manipulation and a behavioral or consequential DV where possible.
2. **Mediation** — show the process carries the effect. A measured mediator is the floor; **manipulating the mediator** (or moderation-of-process) is far stronger and increasingly expected.
3. **Moderation** — a theory-predicted moderator that switches the process on/off; this is the most convincing process evidence.
4. **Boundary / robustness** — generalize across stimuli, populations, and operationalizations so the effect is not stimulus-bound.

Vary the operationalization across studies (different manipulations of the same construct, different DVs, different samples) so a reviewer cannot attribute the result to one idiosyncratic stimulus.

## Manipulations, controls, and confounds

- **Manipulation checks**: include a check that the IV moved the intended construct *and nothing else*. A manipulation that also shifts mood, difficulty, or attention is confounded.
- **Pretest stimuli**: pretest scenarios/images/copy so conditions differ only on the focal dimension.
- **Confound audit**: ask of every manipulation, "what else changed?" — fluency, plausibility, arousal, social desirability, demand. Design controls (yoked conditions, neutral comparisons) before collecting data.
- **Demand and attention**: attention/comprehension checks, funnel debrief for hypothesis guessing, and a design that does not telegraph the prediction.
- **Process-of-mediation**: prefer **causal-chain (experimental-mediation)** or **moderation-of-process** designs over Baron-Kenny on a measured mediator, which reviewers now treat as weak causal evidence.

## Power and samples

- Run an **a priori power analysis** (effect-size assumption justified by pilot or prior literature, not back-solved) and report target N before data collection.
- Pre-specify **exclusion rules** (attention checks, completion, duplicates) in advance; report Ns before and after exclusions.
- For online panels (Prolific/MTurk/CloudResearch), document the platform, screening, and data-quality safeguards.

## Pre-registration and transparency as design choices

- **Pre-register** confirmatory studies (OSF/AsPredicted): hypotheses, design, sample size, analysis plan, exclusions. JCP encourages preregistration with an analysis plan (检索于 2026-06；以官网为准); report deviations transparently.
- Plan the **open data + materials** deposit and the code from the start (see jcp-submission), not at acceptance.
- Consider a **Registered Report** for a strong confirmatory theory test where the result should publish regardless of direction (待核实 whether JCP currently offers this format).

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCP is experimental consumer psychology; randomization inference, mediation done right (`mediate`, not naive controlling-away), and family-wise corrections matter most.

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

- [ ] Each study tests a distinct link: existence → mediation → moderation → boundary
- [ ] At least one strong process design (manipulated mediator or moderation-of-process), not only measured mediation
- [ ] Manipulation checks confirm the IV moved the construct and not a confound
- [ ] Stimuli pretested; conditions differ only on the focal dimension
- [ ] A priori power analysis; target N and exclusion rules pre-specified
- [ ] Confirmatory studies pre-registered; deviations to be reported
- [ ] Materials, data, and code deposit planned now

## Anti-patterns

- **One study, big claim**: a single experiment asked to carry a process contribution
- **Measured-mediation-only**: Baron-Kenny on a self-report mediator presented as causal process
- **Confounded manipulation**: the IV also shifts mood/difficulty/arousal and there is no check
- **Convenience N**: 50/cell because "that's what we usually run," with no power plan
- **Stimulus-bound effect**: one scenario, one product, generalized to "consumers"
- **Post-hoc exclusions**: dropping participants until p < .05 (a rigor-era red flag)

## Output format

```text
【Study chain】existence → mediation → moderation → boundary (map studies)
【Process design】measured mediator / manipulated mediator / moderation-of-process
【Manipulation + check】IV, the construct it moves, the check, the confounds controlled
【Power & samples】a priori N per cell, exclusion rules, platform
【Pre-registration】which studies, registry, what is locked
【Transparency plan】data + materials + code deposit
【Next skill】jcp-data-analysis
```
