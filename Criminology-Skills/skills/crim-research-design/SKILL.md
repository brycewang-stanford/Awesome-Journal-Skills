---
name: crim-research-design
description: Use when defending the research design of a Criminology (ASC / Wiley) manuscript — causal identification for quantitative work, longitudinal and life-course designs, criminal-career and trajectory methods, place-based and experimental designs, or case selection and process tracing for qualitative work. Criminology judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (crim-research-design)

*Criminology* accepts many methodologies but is demanding about each. The design must credibly connect
the mechanism (`crim-theory-building`) to crime evidence. This skill is mode-aware: pick the section
that matches your work and defend it against the strongest rival explanation.

## When to trigger

- Specifying identification, a longitudinal design, case selection, or an experiment
- A reviewer questioned causal claims, selection, the dark figure, or a confound
- Choosing between a trajectory model, fixed-effects panel, or survival design
- Justifying why your design adjudicates the rival theory from `crim-literature-positioning`

## Quantitative / causal inference
- **Identification first.** State the estimand and the assumptions that license a causal reading
  (ignorability, parallel trends, exclusion, continuity). Defend them; don't assert them.
- **Designs**: experiments (incl. randomized policing/hot-spot trials), DID/event study (use modern
  staggered-adoption estimators, not naive TWFE), IV (first-stage strength, exclusion), RDD
  (density/manipulation tests, bandwidth robustness), matching/weighting with balance + sensitivity.
- **Inference**: cluster at the level of treatment assignment (often place or agency); randomization
  inference for experiments; few-cluster corrections (wild-cluster bootstrap).
- **Crime-data validity**: state which construct you measure — reported crime (UCR/NIBRS), victimization
  (NCVS), or self-report — and how the **dark figure** and reporting/recording bias affect inference.

## Longitudinal / life-course / criminal careers
- **Within- vs. between-person**: use fixed effects or hybrid models to isolate within-individual change
  when the theory is about turning points or desistance.
- **Trajectory / group-based models (GBTM, growth mixture)**: justify the number of groups (BIC,
  AvePP ≥ 0.7, group shares, classification odds); treat groups as a summary, not literal types.
- **Survival / recidivism**: handle right-censoring and competing risks; distinguish timing from prevalence.
- **Criminal-career parameters**: separate onset, frequency (λ), seriousness, and desistance; do not let
  prevalence masquerade as incidence.

## Place-based & experimental
- Randomized field trials (patrol, deterrence, reentry): report power/MDE, attrition, fidelity, ethics/IRB.
- Spatial designs: address displacement vs. diffusion of benefits; near-repeat and hot-spot logic.

## Qualitative / case-based
- **Case selection** justified by design logic (typical, deviant, most/least-likely, paired comparison),
  not convenience. Say what the case is a case *of*.
- **Process tracing / life-history** with explicit tests; state what evidence would have **disconfirmed**
  the argument. Plan source documentation (see `crim-data-and-transparency`).

## The adjudication test (Criminology-specific)

For the **single strongest rival theory**, write one sentence: *"If the rival mechanism were operating
instead of mine, the crime data would look like ___; instead they look like ___."* If you cannot, the
design does not yet identify the contribution.

## Anti-patterns

- Naive TWFE on staggered policy adoption; clustering below the assignment level
- "Causal" language on a design that only supports association
- Reading trajectory groups as real, fixed offender types
- Ignoring the dark figure / reporting bias when using official counts
- Convenience case selection dressed up as theory-driven

## Output format

```
【Mode】quant-causal / longitudinal-life-course / place-experiment / qualitative
【Estimand or claim】what is being identified/shown (and within- vs. between-person)
【Crime measure】reported / victimization / self-report + dark-figure note
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】crim-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — trajectory/survival/spatial packages and longitudinal datasets
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Criminology scope and methodological breadth
