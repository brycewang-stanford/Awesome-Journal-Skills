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

## Design objections by mode, and the GEC fix

GEC judges each tradition on its own terms, but every mode faces a scale-and-human-dimensions test on top of the usual methodological one. These are the objections that recur and how to disarm them.

| Mode | The objection a referee writes | The fix that holds at GEC |
|------|-------------------------------|---------------------------|
| Quant-causal | "Causal language, associational design" / "naive TWFE on staggered rollout" | State the estimand and license; switch to a modern staggered-adoption estimator; cluster correctly |
| Qualitative | "Convenience case dressed as theory" | Justify case selection by design logic and say what the case is a case *of*, at what scale |
| Experiment / survey | "Treatment realism and generalisation unaddressed" | Preregister, report MDE, and bound the generalisation claim to the sampling frame |
| Mixed methods | "Interviews stapled to a regression" | Give the integration logic and show why neither strand alone answers the question |
| Any mode | "Scale mismatch — local data, global claim" | Match the claim's scale to the design's, or theorise the link across scales explicitly |

## Worked micro-example (illustrative — mixed-methods coastal study)

A team pairs a household survey on adaptation with process-tracing interviews on why a district fund disbursed unevenly.

- **Weak design:** the survey runs a cross-sectional regression labelled "the effect of governance," and a handful of interviews are appended as colour.
- **GEC-defensible design:** the estimand is the *association* between tenure and adaptation uptake at equal exposure (no causal label it cannot support), clustered at the district; the qualitative strand uses smoking-gun tests on the eligibility-rule mechanism. The adjudication sentence: "If exposure rather than tenure drove uptake, low-tenure uptake would track surge depth; instead it tracks tenure at constant depth (0.37 vs 0.62, illustrative)." The integration logic is explanatory-sequential: the interviews explain *why* the survey pattern arises.
- **Payoff:** each strand is rigorous on its own terms and the scale (district, with a stated link to the multi-scale nature of coastal change) matches the claim.

## Calibration anchors (hedged)

- **Adjudication bar:** a GEC design should rule out the single strongest rival in one written sentence; if it cannot, the design is underspecified.
- **Pluralism bar:** quantitative, qualitative, and mixed work are equally welcome — the question is rigour and fit, not method fashion.
- Confirm any human-subjects, ethics, and preregistration expectations against the journal's current author guidelines, since requirements evolve.

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
