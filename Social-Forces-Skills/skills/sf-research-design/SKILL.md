---
name: sf-research-design
description: Use when defending the research design of a Social Forces (SF) manuscript — causal identification for quantitative work, formal demographic design, case selection and process tracing for comparative-historical and ethnographic work, network and computational designs. SF's reputation rests on methodological rigor. Strengthens the design; it does not write code.
---

# Research Design (sf-research-design)

Social Forces is known for **methodological rigor**, and its reviewers are demanding about each
tradition. The design must credibly connect the argument (`sf-theory-building`) to evidence and rule
out the strongest alternative. This skill is mode-aware: pick the section that matches your work and
defend it on its own terms.

## When to trigger

- Specifying identification, demographic design, case selection, or a network/computational pipeline
- A reviewer questioned causal claims, case choice, measurement, or a confound
- Deciding what design buys the cleanest test of your mechanism within a tight word budget
- Justifying why your design adjudicates the rival account from `sf-literature-positioning`

## Quantitative / causal inference
- **Identification first.** State the estimand and the assumptions that license a causal reading
  (ignorability, parallel trends, exclusion, continuity). Defend them, don't assert them.
- **Designs**: panel/fixed effects, DID/event study (use modern staggered-adoption estimators, not
  naive TWFE), IV (first-stage strength, exclusion, weak-IV-robust inference), RDD (density tests,
  bandwidth robustness), matching/weighting with balance + sensitivity.
- **Inference**: cluster at the level of treatment/sampling; account for complex survey designs and
  weights; correct for multiple comparisons when testing many implications.
- **Sensitivity**: how strong must an unobserved confounder be to overturn the result?

## Demographic
- Be explicit about period vs. cohort, exposure, and standardization/decomposition choices.
- Handle censoring and competing risks correctly in event-history work; justify the hazard form.

## Comparative-historical / ethnographic
- **Case selection** justified by design logic (typical, deviant, most/least-likely, paired
  comparison) — not convenience. Say what the case is a case *of*.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the argument.
- **Source transparency**: archives, interviews, fieldnotes — plan how they will be documented and
  cited (see `sf-data-and-transparency`).

## Network / computational
- Justify boundary specification, tie definition, and the null/baseline you compare against.
- Validate any computational measure (e.g., classifier, topic model) against human-labeled samples.

## The adjudication test (SF-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather
than my argument, the data would look like ___; instead they look like ___."* If you cannot, the
design does not yet identify the contribution.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Social Forces is quantitative sociology — survey and administrative panels; emphasize identification, decomposition, and multilevel inference.

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
- "Causal" language on a design that only supports association
- Convenience case selection dressed up as theory-driven
- An unvalidated computational measure treated as ground truth
- A design that cannot distinguish your argument from the leading alternative

## What SF referees probe in the design

Because Social Forces built its standing on methodological rigor across a broad discipline, its referees
read the design for whether the strongest alternative is actually ruled out — not whether the method is
fashionable. A practical gate by mode:

| Design mode | The check an SF referee runs first | Common decline trigger |
|-------------|-----------------------------------|------------------------|
| Quant-causal | Estimand stated and key assumption defended? | "Causal" verbs on an associational design |
| Panel / DID | Modern staggered estimator + parallel-trends evidence? | Naive TWFE on staggered adoption |
| Demographic | Period vs. cohort, exposure, standardization explicit? | Rates compared without standardization |
| Comparative-historical | Case justified as a case *of* something? | Convenience case dressed as theory-driven |
| Network / computational | Boundary, tie definition, validated measure vs. a null? | Classifier output as ground truth |

Calibration (hedged): SF welcomes all these traditions, but the bar is rigor on the tradition's own
terms plus general-sociology significance — less theory-maximalist than AJS/ASR yet far stricter on
identification than a descriptive outlet. Confirm method-specific expectations against current practice.

## Worked vignette (illustrative)

A neighborhoods-and-attainment study uses a sibling comparison: children in one family exposed to
different neighborhood poverty via a mid-childhood move. Movers to lower-poverty tracts show a 0.12 SD
test-score gain (illustrative). SF-grade adjudication: "If the effect were pure selection it should
vanish within families; instead the within-family estimate is 0.09 SD, so selection explains at most a
quarter." Pairing this with an Oster-style sensitivity bound moves an SF referee from skeptic to advocate.

## Referee-pushback patterns and the SF fix

- "Selection threatens the inference" → add a within-unit comparison or sensitivity bound.
- "Mechanism under-specified" → state the observable implication tested and what would have disconfirmed it.
- "Clustering at the wrong level" → cluster at treatment/sampling level; wild-cluster bootstrap if few.

## Output format

```
【Mode】quant-causal / demographic / comparative-historical / ethnographic / network-computational
【Estimand or claim】what is being identified/shown
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】sf-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design/identification packages (R/Stata/Python), demography, networks, CAQDAS/QCA
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SF rigor reputation and scope
