---
name: cogpsych-study-design
description: Use when designing the experiments for a Cognitive Psychology (Elsevier) manuscript so they tightly control confounds, discriminate competing models, and have adequate power across a multi-experiment program. Hardens stimulus construction, counterbalancing, design logic, and sample-size justification; it does not write analysis or modeling code.
---

# Experiment Design (cogpsych-study-design)

Cognitive Psychology expects **tightly controlled cognitive experiments** whose design is engineered to
**discriminate models**, organized as a **multi-experiment program** in which each experiment adds
inference. The craft is in stimulus construction, counterbalancing, confound control, and powering the
*critical contrast* — not just the main effect. Co-design the experiments with the model
(`cogpsych-theory-and-hypotheses`).

## When to trigger

- Designing an experiment or a multi-experiment series
- Constructing stimuli, item sets, and counterbalancing schemes
- A reviewer questioned confounds, power, design logic, or whether the design discriminates the models
- Justifying sample size for the critical contrast (often an interaction)

## Design standards

1. **Design for discrimination.** Build the design so the data produce the **signature that separates
   the models** (e.g., a manipulation that the rival accounts predict to diverge). A design that both
   models predict equally well wastes the experiment.
2. **Control researcher and stimulus degrees of freedom.** Counterbalance condition/item assignment;
   control low-level confounds (frequency, length, familiarity, response mapping); randomize order; use
   attention/manipulation checks. Document the full stimulus pool, not a curated subset.
3. **Power the critical contrast.** Justify N (and trials per cell) for the *discriminating* effect —
   often an interaction or a model parameter — not the easy main effect. State the assumed effect size
   and its source. Trials-per-participant is part of power for within-subjects designs.
4. **Multi-experiment logic.** Say what each experiment adds: rules out a confound, extends scope,
   replicates the critical pattern, or tests a further model prediction. Avoid near-duplicate runs.
5. **Validity.** Argue construct validity (does the task measure the process the model is about) and the
   generality of the claim across the stimulus space and population.

## Powering the critical contrast — worked example (illustrative)

For the recognition-memory program, power the *z-ROC shape* contrast, not just overall accuracy.

```
Critical contrast: the diagnostic difference in z-ROC curvature between
            UVSD and DPSD predictions.
Within-subjects: trials per participant drive ROC precision — target enough
            old/new trials per confidence bin to estimate the slope reliably
            (state the per-bin minimum, not just N).
Sample size: justified by simulation under each model (generate data from
            UVSD and DPSD at plausible parameters; find N + trials at which
            the model-recovery rate exceeds the target).
Across experiments: Exp 1 establishes the pattern; Exp 2 rules out a list-
            composition confound; Exp 3 tests a further divergent prediction.
Stopping rule: fixed N + fixed trials; no optional stopping.
```

Justify sample size by **model/parameter recovery simulation** where the contrast is a model parameter,
not only by a textbook power formula for a mean difference — this is the venue-appropriate move.

## Pre-data lockdown checklist

| Degree of freedom | Lock before data? | Where it lives |
|-------------------|-------------------|----------------|
| Hypotheses + discriminating prediction | yes | preregistration / analysis plan |
| Models to be fit + comparison criteria | yes | analysis plan |
| Full stimulus pool + counterbalancing | yes | materials deposit |
| Trials per cell / per confidence bin | yes | design + power justification |
| Exclusion rules (RT, accuracy, dropout) | yes | preregistration |
| Stopping rule | yes | analysis plan |
| Exploratory analyses / model exploration | allowed, labeled | reported separately |

## Design-stage reviewer pushback and the venue fix

- "Both models predict this design equally" → redesign so a manipulation makes the model predictions
  diverge; the signature must be diagnostic.
- "Possible stimulus confound (frequency/length)" → control or counterbalance it; report the matched
  pools; this objection lands hard here.
- "Underpowered for the interaction / too few trials" → power the critical contrast via simulation;
  report trials per cell, not only N.
- "Three near-identical experiments" → make each add inference (confound control, scope, further
  prediction).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Cognitive Psychology is experimental — within-subject designs and mixed models dominate; report the model, the effect size, and multiple-comparison control.

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

- A design that both rival models predict equally well (non-diagnostic)
- Uncontrolled low-level stimulus confounds or a curated stimulus subset
- Powering the easy main effect while the critical interaction/parameter is underpowered
- Too few trials per condition to estimate the model quantities reliably
- A multi-experiment paper of near-duplicate runs with no added inference

## Output format

```
【Discrimination】does the design produce the model-separating signature? [Y/N]
【Confound control】counterbalancing + low-level controls + checks? [Y/N]
【Power】N + trials/cell justified for the critical contrast (simulation)? [Y/N]
【Degrees of freedom】stimuli, models, exclusions, stopping fixed in advance? [Y/N]
【Multi-experiment logic】what each experiment adds
【Next】cogpsych-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — stimulus tools, power/recovery simulation, preregistration templates
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — design and reporting expectations
