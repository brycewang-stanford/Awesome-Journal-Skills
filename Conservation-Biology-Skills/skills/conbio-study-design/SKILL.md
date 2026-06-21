---
name: conbio-study-design
description: Use when defending the study design of a Conservation Biology manuscript — ecological sampling and inference (detection, spatial structure, pseudoreplication), comparative/observational and quasi-experimental designs (BACI), modeling and synthesis design, and human-dimensions methods. The journal judges each appropriate method on its own terms. Strengthens the design; it does not write code.
---

# Study Design (conbio-study-design)

*Conservation Biology* accepts many methodologies but is demanding about each. The design must
credibly connect the conservation question (`conbio-topic-selection`) to evidence that supports a
**transferable, decision-relevant** conclusion. This skill is mode-aware: pick the section that matches
your work and defend it against the strongest alternative explanation.

## When to trigger

- Specifying sampling, comparison, or modeling design before fieldwork or analysis
- A reviewer questioned detection, replication, spatial autocorrelation, or causal claims
- Designing an intervention/management evaluation or a synthesis protocol
- Justifying why your design adjudicates the rival account from `conbio-literature-positioning`

## Field & observational ecology
- **Account for detection.** Imperfect detection biases counts — use occupancy, distance sampling, or
  capture-recapture rather than raw indices when detection varies.
- **Replication and scale.** Avoid pseudoreplication; define the independent unit; match the spatial
  and temporal scale of sampling to the inference. State the sampling frame.
- **Spatial structure.** Address spatial autocorrelation and spatial bias (sampling effort, access).

## Comparative / quasi-experimental (intervention evaluation)
- Use **BACI / before-after-control-impact**, control-impact, or matched designs to attribute change
  to a conservation action rather than to background trend.
- **Counterfactual thinking.** What would have happened without the protected area / policy / harvest
  rule? Matching, difference-in-differences, or synthetic controls where appropriate.
- State confounders (accessibility, prior condition) and how the design or analysis handles them.

## Modeling & synthesis
- **SDM / niche / population models:** justify predictors, address sampling bias and collinearity,
  validate out-of-sample; state transferability limits before projecting.
- **Systematic review / meta-analysis:** follow **PRISMA / CEE** protocols; preregister where possible;
  document search, screening, and effect-size extraction.

## Human dimensions / social science
- Match the method (surveys, interviews, choice experiments) to the question; report sampling, ethics,
  consent, and how respondent identity and sensitive data are protected.

## The adjudication test (journal-specific)

For the **single strongest rival explanation**, write one sentence: *"If the rival were true rather
than my conclusion, the data would look like ___; instead they look like ___."* If you cannot, the
design does not yet support a transferable conservation claim.

## Anti-patterns

- Raw counts treated as abundance with no detection model
- Pseudoreplication; inference at a scale the sampling cannot support
- "Effect of the intervention" with no counterfactual or control
- SDM/model projected far outside its training range with no transferability caveat
- A design that cannot distinguish your conclusion from the leading alternative


## Operating pass for Conservation Biology

Treat this skill as an executable review pass, not a prose hint. First lock the species/system threat, conservation decision, and uncertainty relevant to action; then judge whether the current manuscript answers the venue's real reader: conservation-science reviewers who ask whether evidence changes biodiversity, management, or policy action.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Biological Conservation for applied conservation breadth, Global Change Biology for climate/ecosystem process, Ecology Letters for theory-forward ecology; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Submission-ready gate:** do not give final advice until the pack's `resources/official-source-map.md` has been checked for upload-week rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Mode】field-ecology / quasi-experimental / modeling-synthesis / human-dimensions
【Question / estimand】what is being measured or attributed
【Key assumption(s)】detection, scale, counterfactual, transferability — how each is defended
【Rival ruled out】the adjudication sentence
【Robustness/sensitivity】planned checks
【Next】conbio-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — occupancy, capture-recapture, SDM, BACI, and synthesis tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — reviewer expectations and scope
