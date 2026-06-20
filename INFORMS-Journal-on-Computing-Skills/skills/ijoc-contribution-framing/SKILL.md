---
name: ijoc-contribution-framing
description: Use when the one-sentence computational/methodological claim of an INFORMS Journal on Computing (IJOC) manuscript is not sharp, or the contribution reads as application rather than computing. Sharpens the "what is new and by how much"; it does not run the experiments that back it.
---

# Contribution Framing (ijoc-contribution-framing)

## When to trigger

- You cannot state in one sentence **what is computationally new and by how much**
- The intro frames an *application* win when the contribution should be the *method*
- A coauthor or referee says "interesting but what is the actual contribution?"
- The experiments are solid (`ijoc-data-analysis`) but the paper does not *claim* them crisply

## The IJOC contribution sentence

A strong IJOC contribution sentence names the **method**, the **axis of improvement**, the **magnitude**, and the **evidence regime** — and is falsifiable. Template:

> "We propose [method] for [OR problem]; it [wins on axis] by [magnitude] over [SOTA baseline] on [benchmark set], with [guarantee/property]."

Worked, illustrative: "We propose a Benders-with-lazy-cuts scheme for two-stage stochastic network design that solves instances 6× larger than the best published exact method on standard library instances within the same time limit, with a proof of cut validity and a 31% root-gap reduction." That sentence tells the Area Editor exactly what to verify.

## Types of contribution IJOC rewards

Frame the contribution as one (or a clear combination) of these, and make the *primary* one unambiguous:

| Contribution type | What makes it land at IJOC | Common failure |
|-------------------|---------------------------|----------------|
| New exact method / formulation | larger solvable instances, tighter bounds, with validity proven | "new model" with no computational edge |
| New heuristic/matheuristic | better quality or time, fairly compared, ideally with a bound | win over a strawman baseline |
| ML-for-OR method | beats both OR and prior learning baselines; feasibility safe | a black box with no OR baseline |
| New simulation/estimation method | lower variance/cost at equal accuracy, with theory | "we simulated it" with no methodological news |
| Computational tooling/methodology | enables computations not previously feasible, reproducibly | software existence without a methodological claim |

## Application is the motivation, not the contribution

The most common framing error at IJOC is leading with the application ("we study airline crew scheduling") rather than the computing ("we design a column-generation acceleration that…"). State the application in one or two sentences as motivation, then pivot hard to the methodological news. If you remove the application and the paper still has a contribution, you are framed correctly; if it collapses, the computing is not yet the contribution — return to `ijoc-topic-selection`.

## Calibrating the claim to the evidence

Overclaiming triggers referee distrust; underclaiming wastes a good result. Match the verb to the evidence: "proves," "guarantees" only with proofs; "consistently outperforms" only with a performance profile and a statistical test; "scales to" only with a scaling plot. Scope honestly by regime ("on sparse, large instances") rather than blanket dominance. The claim in the abstract, the intro, and the conclusion must be the *same* claim.

## Checklist

- [ ] One sentence states method + axis + magnitude + baseline + benchmark + property
- [ ] The primary contribution type is unambiguous
- [ ] The claim is computing-first; application is motivation only
- [ ] Verbs match the evidence (prove/guarantee/outperform/scale) and nothing stronger
- [ ] The claim is scoped by regime where a competitor still wins
- [ ] Abstract, intro, and conclusion state the identical claim
- [ ] Removing the application leaves a standing contribution

## Anti-patterns

- Leading with the application domain and burying the method
- "We are faster/better" with no magnitude, baseline, or benchmark named
- A contribution sentence that would fit *Operations Research* (model news) rather than IJOC (computing news)
- Claiming guarantees the theory section does not prove
- Different contribution wording in the abstract vs. the conclusion
- Listing five small contributions with no headline — referees cannot tell what to evaluate

## Output format

```text
【Journal】INFORMS Journal on Computing
【Skill】ijoc-contribution-framing
【Contribution sentence】method + axis + magnitude + baseline + benchmark + property
【Primary type】exact / heuristic / ML-for-OR / simulation / tooling
【Computing-first?】application is motivation only? [Y/N]
【Claim–evidence match】verbs justified by proofs/profiles/scaling? [Y/N]
【Regime scoping】where the claim holds / where a rival wins
【Next skill】ijoc-tables-figures
```
