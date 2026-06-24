---
name: asr-research-design
description: Use when defending the research design of an American Sociological Review (ASR) manuscript — causal/observational inference for quantitative and demographic work, case selection and comparison for comparative-historical work, site and informant logic for ethnography, and network/computational designs. ASR judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (asr-research-design)

ASR welcomes many methods but is exacting about each. The design must credibly link the argument
(`asr-theory-building`) to evidence and rule out the leading alternative. Pick the section matching
your method.

## When to trigger

- Specifying identification, case selection, sampling, or site/informant logic
- A reviewer questioned causal claims, generalization, selection, or a confound
- Justifying why your design adjudicates the rival account from `asr-literature-positioning`

## Quantitative / demographic
- **Be honest about what the design identifies.** Much of sociology is observational; distinguish
  description, association, and causation. If causal, state the assumptions (ignorability, parallel
  trends, exclusion) and defend them.
- **Designs**: panel/fixed-effects, DID/event study (modern staggered estimators, not naive TWFE),
  IV, RDD, matching/weighting with balance and sensitivity; decomposition for inequality; event
  history for timing; age-period-cohort for demographic change.
- **Inference & sampling**: respect complex survey design (weights, clustering, strata); cluster at
  the right level; report uncertainty.
- **Sensitivity**: how strong must an unobserved confounder be to overturn the result?

## Comparative-historical
- **Case selection** by design logic (most/least-likely, paired comparison, deviant) — say what each
  case is a case *of*; justify the comparison and the counterfactual.
- **Evidence**: archives, secondary histories, administrative records; document provenance.
- Specify the causal form (necessary/sufficient conditions, conjuncture, path dependence; QCA where
  apt) and what evidence would have **disconfirmed** the argument.

## Ethnographic / interview
- **Site and informant selection** justified theoretically, not by access alone; state positionality
  and access conditions.
- Plan how depth, saturation, and negative cases are handled; how claims map to observed evidence.
- Ethics/IRB, consent, and confidentiality planned from the start (see `asr-data-and-transparency`).

## Network / computational
- Define boundary specification, missing-ties, and the generative process (e.g., ERGM/SAOM logic).
- For computational text/ML: validate against human-labeled samples; report stability.

## The adjudication test (ASR-specific)

For the **single strongest rival explanation**: *"If the rival were true rather than my argument, the
evidence would look like ___; instead it looks like ___."* If you cannot write it, the design does not
yet identify the contribution.

## What ASR referees demand of each design

ASR judges every tradition rigorously on its own logic — the unifying ASA standard is a design that
connects argument to evidence and rules out the leading rival.

| Design | Referee's first demand | Satisfying move |
|--------|------------------------|------------------|
| Quant / demographic | "What does this identify?" | description vs. causation; defend the assumption + sensitivity |
| Comparative-historical | "Why these cases?" | design-driven selection; say what each is a case *of* |
| Ethnographic | "Why this site and informants?" | theoretical sampling, positionality, negative cases |
| Network / computational | "Principled process?" | boundary spec, missing-tie handling, label validation |

## Worked micro-example (illustrative)

A comparative-historical study argues that labor-incorporation timing shaped later union strength
across four countries.

```
Case logic: paired comparison (early vs. late incorporators), matched on industrialization level
Causal form: path dependence — early settlement locks in conditions C1–C2
Disconfirming evidence sought: a case with early timing but weak unions → would break the claim
Adjudication sentence: "If prior militancy drove this, the deviant case shows strong unions despite
  late timing; instead it shows weak unions, as the timing argument predicts."
```

The selection is design-driven, the rival is named, and the design specifies what evidence would have
falsified the argument.

## Referee pushback → ASR-specific fix

- *"Association dressed as causation."* → Restate what the design identifies and add a sensitivity
  bound or placebo; drop causal verbs you cannot defend.
- *"Your cases look hand-picked."* → Show the selection rule and what each case represents at the
  population level.

## Calibration anchors

- **Method-appropriate rigor, one disciplinary bar.** ASR won't hold ethnography to a regression
  standard or vice versa — but every design must defeat its strongest rival.
- **The adjudication sentence is the test.** If you can't write "if the rival were true the evidence
  would look like ___," the design does not yet earn the contribution.
- **Identification honesty travels.** Stating plainly what observational data can and cannot establish
  reads as strength to a cross-method panel.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ASR is general sociology where observational designs dominate; foreground identification (DiD/IV/RDD), decomposition, and clustered inference.

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

- "Causal" language on a purely observational/associational design
- Naive TWFE on staggered timing; ignoring survey weights/clustering
- Convenience case or site selection dressed up as theory-driven
- Ethnographic claims with no account of negative cases or saturation
- A design that cannot distinguish your mechanism from the leading alternative

## Output format

```
【Method】quant/demographic / comparative-historical / ethnographic / network-computational
【What it identifies】description / association / causation
【Key assumption(s) or selection logic】and how defended
【Rival ruled out】the adjudication sentence
【Robustness / negative cases / sensitivity】planned
【Next】asr-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design/analysis packages and CAQDAS/QCA tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — ASR methodological breadth
