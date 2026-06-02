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
