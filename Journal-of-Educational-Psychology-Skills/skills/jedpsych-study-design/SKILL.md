---
name: jedpsych-study-design
description: Use when designing studies for a Journal of Educational Psychology manuscript so they meet the journal's standards for educational settings — nesting (students in classes/schools), cluster-level power, measurement of learning constructs, ecological validity, and preregistration where appropriate. Strengthens the design and pre-analysis plan; it does not write code.
---

# Study Design (jedpsych-study-design)

The Journal of Educational Psychology expects designs that are **adequately powered for their nesting
structure**, **measure learning constructs well**, and have **ecological validity** for real educational
settings. Because JEP studies are usually students nested in classes nested in schools, the single most
consequential design decision is matching the **unit of randomization, power, and analysis** to the level
at which the treatment and mechanism operate. This skill hardens the design before data collection.

## When to trigger

- Planning a classroom/school study, field trial, or longitudinal study
- Writing a preregistration / pre-analysis plan for a prospective trial
- A reviewer questioned nesting, clustering, power, measurement, or ecological validity
- Justifying sample size at the right level

## Design standards

1. **Match the level: randomization, power, analysis.** If you randomize classrooms or schools, the
   experiment's effective N is the number of **clusters**, not students. Power at the cluster level using
   the intraclass correlation (ICC) and number/size of clusters; plan the matching multilevel analysis up
   front (see `jedpsych-data-analysis`).
2. **Cluster-level sample-size justification.** Provide an explicit basis for the number of clusters and
   their size — a **power analysis** for the smallest educationally meaningful effect, given the ICC and a
   pretest covariate that absorbs cluster variance. State the assumed effect size and its source.
3. **Measure learning constructs well.** Use validated outcome measures of the learning/motivation
   construct; justify their reliability and that they capture *transfer/learning*, not just teaching to
   the test. Pre/post designs should plan for measurement at the right grain.
4. **Baseline equivalence and confounds.** With cluster randomization (or quasi-experiments), report
   baseline equivalence on covariates; address selection, attrition, contamination across conditions, and
   teacher/implementation fidelity.
5. **Ecological validity.** Argue that the setting, task, and delivery (teacher- vs researcher-delivered)
   support the educational claim; a stripped lab analog weakens fit at JEP.
6. **Control researcher degrees of freedom.** Decide in advance: conditions, the full measure set,
   exclusion/attrition rules, covariates, and the model. Preregistration is encouraged here.

## Quasi-experimental and longitudinal designs

- For quasi-experiments, plan a credible counterfactual (matching, regression adjustment, difference-in-
  differences, or RD where assignment is on a cutoff) and state the identifying assumption. For
  longitudinal/growth designs, plan the timing, attrition handling, and the growth model in advance.

## Cluster-level sample-size justification — worked example (illustrative)

For a teacher-delivered reading-comprehension trial, justify the *number of classrooms* before recruiting,
tied to the smallest educationally meaningful effect — not a round student count.

```
Smallest meaningful effect: d = 0.20 (a defensible learning gain for a
            classroom literacy intervention).
Nesting:    students nested in classrooms; assumed ICC = 0.15; ~23 students
            per classroom; pretest covariate (r ≈ .6) absorbs cluster variance.
Power:      target 80% power, two-sided alpha .05 → ~48 classrooms
            (24 per arm), ~1,100 students; design effect handled via the ICC,
            not by counting students as independent.
Stopping:   fixed number of clusters; no optional addition of schools.
Covariate:  baseline comprehension at student and classroom level.
```

State the assumed effect size *and its source* (prior trial, meta-analytic estimate, or a smallest-
meaningful-effect argument). Powering on an inflated lab effect, or on student N alone, is the classic JEP
design failure.

## Pre-data lockdown checklist

| Degree of freedom | Lock before data? | Where it lives |
|-------------------|-------------------|----------------|
| Hypotheses + direction (at the right level) | yes | preregistration / analysis plan |
| Unit of randomization + number of clusters | yes | preregistration |
| Full measure list (all outcomes) | yes | preregistration (prevents cherry-picking) |
| Exclusion / attrition rules | yes | preregistration, with expected attrition |
| Covariates + multilevel model form | yes | analysis plan |
| Fidelity / implementation measures | yes | protocol |
| Exploratory analyses | allowed, but labeled | reported separately, post hoc |

## Design-stage reviewer pushback and the venue fix

- "Powered at the student level" → re-power at the cluster level using the ICC; report the number of
  clusters as the effective N.
- "No baseline equivalence" → report covariate balance across arms; adjust for pretest in the model.
- "Outcome measures teaching-to-the-test" → use a transfer/learning measure and justify its validity.
- "Researcher-delivered, so no classroom claim" → move to teacher delivery or scope the claim; argue
  ecological validity.
- "Flexible exclusions / attrition" → preregister rules; report results with and without
  (handoff to `jedpsych-data-analysis`).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEdPsych mixes field/lab experiments and observational school data; multilevel (student-in-class-in-school) inference and many-outcome corrections matter most.

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

- Powering and analyzing as if nested students were independent
- A round student-N target with no cluster-level justification
- Outcome measures that capture test coaching rather than learning
- Ignoring implementation fidelity and contamination across conditions
- A lab-only analog presented as evidence about classrooms

## Output format

```
【Unit】randomization / power / analysis level (matched?) [Y/N]
【Sample size】# clusters + size + ICC + smallest meaningful effect
【Measures】validated learning outcome + reliability + transfer? [Y/N]
【Baseline + confounds】equivalence, attrition, fidelity addressed?
【Ecological validity】setting / delivery supports the educational claim?
【Preregistration】confirmatory core locked? where?
【Next】jedpsych-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `PowerUpR`, `simr`, Optimal Design, multilevel/SEM software, preregistration templates
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JARS reporting standards and preregistration policy
