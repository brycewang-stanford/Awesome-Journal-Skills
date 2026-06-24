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

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Criminology is observational — place/person panels where selection is pervasive; foreground DiD/IV/RDD and the selection objection.

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

- Naive TWFE on staggered policy adoption; clustering below the assignment level
- "Causal" language on a design that only supports association
- Reading trajectory groups as real, fixed offender types
- Ignoring the dark figure / reporting bias when using official counts
- Convenience case selection dressed up as theory-driven

## Identification expectations by design (Criminology calibration table)

A defensible *Criminology* design names the threat reviewers are trained to raise and the move that
neutralizes it. Selection into offending and into treatment is the recurring worry.

| Design | Identifying assumption | Threat a referee names | Defensive move |
|--------|------------------------|------------------------|----------------|
| Hot-spot / policing RCT | randomization, no spillover | displacement contaminates controls | measure diffusion vs. displacement |
| Staggered deterrence-policy DID | parallel trends across adopters | bad-comparison TWFE | staggered estimator + pre-trends |
| Life-course turning point | within-person change isolates effect | selection into marriage/work | fixed-effects/hybrid + sensitivity |
| RDD at a sentencing threshold | continuity at the cutoff | manipulation at the line | McCrary density + bandwidth robustness |

## Worked micro-example: a deterrence-policy quasi-experiment (illustrative)

A state raises a sentencing penalty in some counties before others. A naive TWFE gives a 9% drop
(illustrative); a referee flags invalid comparisons among staggered adopters. Refit with a
heterogeneity-robust staggered estimator: flat pre-trends and a credibly identified 4% first-year drop.
Cluster at the county (assignment) level; with 14 treated counties add a wild-cluster bootstrap, and
note a NIBRS transition could inflate pre-period UCR counts.

## Design-stage referee pushback (with the Criminology fix)

- *"Selection into treatment/offending."* Fix: isolate within-person change or use a quasi-experiment with a stated continuity/parallel-trends defense.
- *"Association, not causation."* Fix: write the estimand and the licensing assumption; soften prose if the design only supports correlation.
- *"Official-records bias unaddressed."* Fix: name reported vs. victimization vs. self-report and the dark-figure bias.
- *"Clustering below assignment."* Fix: cluster at place/agency; few-cluster corrections when units are sparse.

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
