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

## Anti-patterns

- Naive TWFE on staggered treatment; clustering at the wrong level
- "Causal" language on a design that only supports association
- Convenience case selection dressed up as theory-driven
- An unvalidated computational measure treated as ground truth
- A design that cannot distinguish your argument from the leading alternative

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
