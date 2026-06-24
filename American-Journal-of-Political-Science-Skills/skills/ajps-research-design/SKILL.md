---
name: ajps-research-design
description: Use when defending the research design of an American Journal of Political Science (AJPS) manuscript — causal identification for observational work, experimental and survey-experimental design, formal-empirical linkage, or case-based inference. AJPS reviewers are quantitatively demanding, so identification must license the claim being made. Strengthens the design; it does not write code.
---

# Research Design (ajps-research-design)

AJPS publishes many methods but holds identification and inference to a high standard. The design must
credibly connect the argument (`ajps-theory-building`) to evidence and rule out the strongest rival.
This skill is mode-aware: pick the section that matches your work and defend it on its own terms.

## When to trigger

- Specifying identification, sampling, case selection, or experimental design
- A reviewer questioned causal claims, a confound, external validity, or inference
- Preparing a **pre-analysis plan** before collecting/analyzing data
- Justifying why your design adjudicates the rival from `ajps-literature-positioning`

## Quantitative / causal inference
- **Identification first.** State the **estimand** and the assumptions that license a causal reading
  (ignorability, parallel trends, exclusion, continuity). Defend them; do not assert them.
- **Designs**: experiments (incl. survey/conjoint), DID/event study (use modern staggered-adoption
  estimators, not naive TWFE), IV (first-stage strength, exclusion, weak-IV-robust inference), RDD
  (density/manipulation tests, bandwidth robustness), matching/weighting with balance + sensitivity.
- **Inference**: cluster at the level of treatment assignment; randomization inference for
  experiments; small-cluster corrections (wild-cluster bootstrap) when clusters are few.
- **Sensitivity**: how strong must an unobserved confounder be to overturn the result?

## Experiments (lab / survey / field)
- Preregister the design and primary analyses; report power / MDE; pre-specify subgroups.
- Address attention/manipulation checks, attrition, balance, and ethics/IRB and consent (the AJPS
  submission portal asks for human-subjects documentation — see `ajps-submission`).
- For survey experiments: sampling frame, treatment realism, and the limits on generalization.

## Formal-empirical linkage
- Make the **empirical test follow from the model's comparative statics**, not a loose analogy.
- Distinguish predictions unique to your model from those shared with rivals, and test the unique ones.

## Case-based / qualitative & multi-method
- **Case selection** justified by design logic (typical, deviant, most/least-likely, paired) — say what
  the case is a case *of*.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the argument; plan source documentation (see
  `ajps-replication-and-verification`, qualitative path).

## The adjudication test (AJPS-specific)

For the single strongest rival explanation, write: *"If the rival were true rather than my argument,
the data would look like ___; instead they look like ___."* If you cannot, the design does not yet
identify the contribution.

## Design-credibility table (the bar AJPS referees apply by design)

| Design | What the referee demands | Common desk-reject / reject trigger |
|--------|--------------------------|-------------------------------------|
| RDD | Density/manipulation test, bandwidth robustness, no sorting at cutoff | Treating a non-discontinuous threshold as sharp |
| DID / event study | Modern staggered-adoption estimator, pre-trend evidence | Naive TWFE with heterogeneous timing |
| IV | First-stage strength, defended exclusion, weak-IV-robust CIs | "Plausibly exogenous" instrument with no defense of exclusion |
| Matching/weighting | Balance + unobserved-confounder sensitivity bound | Selection-on-observables read as clean causation |

## Worked micro-example (illustrative numbers)

A close-election RD on incumbency states the estimand (local effect of barely winning on next-cycle vote
share at the threshold) and the continuity assumption that licenses it. The density test shows no sorting
(illustrative p = 0.62); the estimate is stable across bandwidths h = 0.08-0.16; a donut-hole spec holds.
The adjudication sentence: *if incumbency advantage were candidate-quality persistence rather than an
officeholding effect, the jump at the bare-win threshold would vanish — instead it is +6 points
(illustrative)*. That sentence converts a quantitatively demanding AJPS referee.

## Referee-pushback patterns and the venue-specific fix

- *"Identification leans on selection-on-observables."* -> Add an Oster-style or sensitivity-bound analysis
  and report how strong an unobserved confounder must be to overturn the result.
- *"Theory and empirics are not tightly linked."* -> Make the test follow from the model's comparative
  statics and target a prediction *unique* to your argument, not one shared with the rival.
- *"The DID uses naive TWFE under staggered adoption."* -> Re-estimate with a heterogeneity-robust
  estimator and show the event-study leads are flat.

Calibration anchor: AJPS spans American, comparative, IR, theory, and methods, but applies a hard premium
on credible identification across all of them; confirm any human-subjects/IRB specifics against the
journal's current submission guidelines.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AJPS prizes credible identification across American / comparative / IR subfields; DiD/IV/RDD for observational claims, randomization inference for experiments.

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

- Naive TWFE on staggered treatment; clustering at the wrong level
- "Causal" language on a design that supports only association
- Convenience case selection dressed up as theory-driven
- Survey/conjoint experiments over-generalized to real-world behavior with no caveat
- A design that cannot distinguish your argument from the leading alternative

## Output format

```
【Mode】quant-causal / experiment / formal-empirical / case-based
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Inference】clustering / RI / small-cluster correction
【Robustness/sensitivity】planned checks
【Next】ajps-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design/identification packages (R/Stata/Python) and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — human-subjects / IRB requirements and submission policy
