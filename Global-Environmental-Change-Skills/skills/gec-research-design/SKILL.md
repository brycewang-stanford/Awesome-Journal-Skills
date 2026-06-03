---
name: gec-research-design
description: Use when defending the research design of a Global Environmental Change (GEC) manuscript — quantitative causal inference, qualitative case work and process tracing, experiments and surveys, or mixed-methods integration. GEC welcomes methodological pluralism but judges each tradition on its own terms. Strengthens the design; it does not write code.
---

# Research Design (gec-research-design)

GEC is methodologically pluralist: quantitative, qualitative, and mixed-methods work are all welcome,
provided each is rigorous and connects the **conceptual framework** (`gec-conceptual-framework`) to
evidence about the human dimensions of environmental change. This skill is mode-aware: pick the section
that matches your work and defend it against the strongest alternative explanation.

## When to trigger

- Specifying identification, case selection, sampling, or instrument design
- A reviewer questioned causal claims, case choice, generalization, scale mismatch, or a confound
- Designing a mixed-methods study and needing to justify the integration
- Justifying how the design tests the framework's mechanism

## Quantitative / causal inference
- **Estimand first.** State what you are estimating and the assumptions that license a causal reading
  (ignorability, parallel trends, exclusion, continuity). Defend them, don't assert them.
- **Designs**: panel/DID and event study (use modern staggered-adoption estimators, not naive TWFE),
  IV (first-stage strength, exclusion), RDD, matching/weighting with balance + sensitivity, multilevel
  models for nested social-ecological data.
- **Inference**: cluster at the level of treatment/assignment; address spatial autocorrelation where
  relevant; report sensitivity to unobserved confounding.

## Qualitative / case-based
- **Case selection** justified by design logic (typical, deviant, most/least-likely, paired) — not
  convenience. Say what the case is a case *of* and at what scale.
- **Process tracing** with explicit tests (hoop, smoking-gun, straw-in-the-wind); state what evidence
  would have **disconfirmed** the argument.
- **Source transparency**: interviews, archives, fieldnotes, participatory data — plan how they are
  documented and cited (see `gec-submission`).

## Experiments & surveys
- Preregister design and primary analyses; report power/MDE; pre-specify subgroups.
- For survey / choice experiments: sampling frame, treatment realism, and honest generalization claims.
- Address attention/manipulation checks, attrition, and ethics/IRB and consent.

## Mixed-methods integration
- State the **integration logic** (sequential, concurrent, embedded) and *why* it answers the question
  better than either strand alone — do not staple a few interviews onto a regression.
- Use joint displays / triangulation; say how convergence or divergence is interpreted.

## The scale & adjudication test (GEC-specific)

State the **scale** at which your design operates (local, regional, global) and how it connects to the
multi-scale nature of environmental change. Then, for the **single strongest rival explanation**, write
one sentence: *"If the rival were true rather than my argument, the evidence would look like ___;
instead it looks like ___."*

## Anti-patterns

- Naive TWFE on staggered treatment; clustering at the wrong level; ignoring spatial dependence
- "Causal" language on a design that only supports association
- Convenience case selection dressed up as theory-driven
- Mixed methods where the strands never actually integrate
- A scale mismatch between the claim and the design (local data, global claim)

## Output format

```
【Mode】quant-causal / qualitative / experiment-survey / mixed-methods
【Estimand or claim】what is being identified/shown, at what scale
【Key assumption(s)】and how each is defended
【Rival ruled out】the adjudication sentence
【Integration logic】(mixed methods) why both strands
【Next】gec-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design/identification packages and CAQDAS for qualitative work
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — GEC methodological-pluralism notes
