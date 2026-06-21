---
name: devpsych-study-design
description: Use when designing studies for a Developmental Psychology (APA) manuscript so they can actually support a developmental-change claim. Covers age-appropriate experimental and longitudinal designs, age vs. cohort confounds, attrition, measurement invariance across ages, sample-size justification, and ethics with minors and vulnerable populations. Strengthens the design and pre-analysis plan; it does not write code.
---

# Study Design (devpsych-study-design)

A developmental design must support a claim about **change**, not just measure something at different
ages. Developmental Psychology reviewers probe the four threats that are specific to this field: **age
vs. cohort confounds**, **attrition**, **measurement invariance across ages**, and **age-appropriate
ethics and task validity**. This skill hardens the design before data collection.

## When to trigger

- Planning a cross-sectional, longitudinal, accelerated, micro-genetic, or experimental developmental study
- Writing a preregistration / pre-analysis plan for developmental work
- A reviewer questioned age confounds, attrition, invariance, power, or ethics with minors
- Justifying sample size for a growth model or an age interaction

## Developmental design standards

1. **Match the design to the change claim.**
   - *Cross-sectional* age comparison: cheap, but age is confounded with **cohort** and with
     **selection/era**; you can describe age differences, not within-person change.
   - *Longitudinal*: supports within-person change but introduces **attrition** and **retest** effects.
   - *Accelerated longitudinal (cohort-sequential)*: overlapping age cohorts to cover a wide span fast —
     state the convergence assumption.
   - *Micro-genetic*: dense repeated observation to catch the process of change; justify sampling rate.
2. **Address age vs. cohort.** For any age effect, say what could be cohort/era instead, and how the
   design (or covariates, or a sequential design) addresses it. Do not call a cross-sectional age
   difference "development" without this.
3. **Plan for measurement invariance.** The same instrument can mean different things at different ages.
   Pre-specify a **configural → metric → scalar** invariance test across ages/waves; interpret change
   only at the level of invariance you establish (handoff to `devpsych-data-analysis`).
4. **Plan for attrition.** Estimate expected dropout, design retention, pre-specify the missing-data
   model (FIML/MI) and an attrition (MCAR/MAR) analysis comparing completers vs. dropouts.
5. **Justify sample size.** Power for the *change* parameter you care about — a growth slope, an
   age × condition interaction, or a cross-lagged path — not just a group mean difference. State the
   assumed effect size and its source.
6. **Age-appropriate ethics and validity.** Child **assent** plus parental/guardian **consent**;
   age-appropriate measures (a task valid at 4 and at 8); special protections for vulnerable populations.

## Pre-data lockdown checklist (developmental)

| Degree of freedom | Lock before data? | Where it lives |
|-------------------|-------------------|----------------|
| Hypotheses + developmental form (slope/interaction) | yes | preregistration |
| Age bands / waves / spacing | yes | preregistration |
| Measurement-invariance test plan | yes | analysis plan |
| Inclusion/exclusion + attrition handling (FIML/MI) | yes | preregistration |
| Time coding / centering for growth models | yes | analysis plan |
| Covariates (incl. cohort/SES) and model form | yes | analysis plan |
| Exploratory trajectory analyses | allowed, labeled | reported separately |

## Sample-size justification — worked example (illustrative)

For a three-wave latent-growth study (ages 4, 6, 8), justify N for the *slope* and the
scaffolding × time interaction, not a t-test.

```
Target parameter: latent slope variance + scaffolding × time interaction.
Method: Monte Carlo power simulation (lavaan/Mplus) under a plausible
        growth model with 20% per-wave attrition and FIML.
Result: N = 300 at wave 1 gives ~85% power for the interaction at the
        smallest developmentally meaningful slope difference; precision
        goal is a slope-CI half-width small enough to sign the trajectory.
Invariance: configural→metric→scalar tested across waves before growth is
        interpreted; partial scalar invariance plan if a few intercepts differ.
Attrition: MAR assumed; completers-vs-dropouts compared on baseline covariates.
```

## Design-stage reviewer pushback and the venue fix

- "This is a cohort effect, not development" → add a sequential element or model cohort; soften to
  age-difference language if you cannot separate them.
- "Is the construct the same at every age?" → pre-specify and report measurement invariance; interpret
  change only at the invariance level achieved.
- "Attrition could bias the trajectory" → report the attrition analysis and a principled missing-data
  model, not listwise deletion.
- "Task isn't valid across this age range" → justify age-appropriateness or use age-anchored measures.

## Anti-patterns

- Calling a cross-sectional age difference "developmental change"
- Interpreting trajectories without testing measurement invariance
- Listwise deletion / ignoring differential attrition
- Powering for a mean difference when the claim is a growth slope or an age interaction
- Consent without child assent; one task used across ages it is not valid for

## Output format

```
【Design】cross-sectional / longitudinal / accelerated / micro-genetic / experiment
【Change claim supportable】age vs. cohort addressed? [Y/N]
【Invariance plan】configural→metric→scalar across ages/waves? [Y/N]
【Attrition plan】expected dropout + missing-data model + attrition analysis? [Y/N]
【Sample size】N + power for the change parameter (slope/interaction)
【Ethics】consent + child assent + age-appropriate measures? [Y/N]
【Next】devpsych-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Mplus/lavaan, `simr`, power simulation, longitudinal design references
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JARS design/reporting requirements and ethics policy
