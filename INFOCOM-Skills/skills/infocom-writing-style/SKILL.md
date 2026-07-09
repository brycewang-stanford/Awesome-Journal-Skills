---
name: infocom-writing-style
description: Use when revising an IEEE INFOCOM paper for a networking problem and system model stated up front, theorems or protocol design that pay off, evaluation proportional to the claim, defensive writing that pre-empts objections (because there is no rebuttal), double-blind wording, and disciplined use of the tight IEEEtran two-column page budget.
---

# INFOCOM Writing Style

Use this when revising the main paper. INFOCOM papers are read by a **broad networking TPC** that
spans theory and systems, inside a **nine-page IEEEtran budget** and (traditionally) with **no
rebuttal**. Two constraints follow: the paper must be legible to both an analyst and a systems
reader, and it must **pre-empt the reviewer's objection in the text**, because you will not get to
answer it later.

## Revision rules

- **State the networking problem and the system model first.** By the end of the introduction a
  reader should know the setting (topology, traffic, constraints), the gap, the contribution
  (analysis and/or design), and what improves. Do not open with a technology-trend paragraph.
- **Make the model do work.** If you formulate an optimization or a Markov/queueing model, its
  assumptions must be stated plainly and its results must yield insight or an algorithm — not a
  formalism that the evaluation ignores. Reviewers reward a model whose theorem changes what you
  build or bound.
- **Pair every claim with proportional evidence** — a proof for an analytical claim, a
  simulation/testbed number with the setup named, or a measurement with its methodology — not
  adjectives like "significantly improves."
- **Write defensively.** Name the assumption a theory reviewer will question and justify it; name
  the baseline a systems reviewer will call unfair and tune it; state the regime where your result
  does *not* hold. Because there is no rebuttal, an unaddressed objection becomes a reject.
- **Respect the page budget as a design constraint.** Nine pages of text (appendices included) is
  tight; a proof sketch in the body with the full proof compressed, and a focused evaluation, beat
  an over-scoped paper that only fits by cutting the model.
- **Maintain double-blind wording** in self-citations (third person), tool names, testbed/cluster
  identifiers, acknowledgements, and funding.

## Networking-paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Problem, setting, gap, contribution, what improves — by the first column or two | Leads with a trend, not a networking problem |
| System model | Topology, traffic, constraints, assumptions, notation, stated plainly | Assumptions hidden or introduced only in the evaluation |
| Analysis / design | Theorems + proof sketches, or the protocol/algorithm, reproducibly | A model no result uses; a design too thin to re-implement |
| Evaluation | Each claim answered with proportional evidence, honest baselines | Toy topology; untuned baseline; metric that proxies the claim |
| Discussion / limits | The regime where the result holds; deployment caveats | No limits stated (invites the objection you cannot rebut) |
| Related work | Delta-first positioning against the networking literature | Citation catalog with no contrast |

## Sentence-level rewrites

| Draft pattern | INFOCOM-safe rewrite |
|---|---|
| "Our scheme significantly improves throughput." | "improves median throughput by X% (95% CI ...) over <tuned baseline> in <topology/scale>" |
| "We prove our algorithm is optimal." | "We prove a (1-1/e) approximation under <stated assumptions>; §V bounds the gap empirically" |
| "We evaluate on a large simulation." | "We simulate <N nodes> in <ns-3/custom>, <traffic model>, <M seeds>; setup in §V-A" |
| "The model captures the system." | "Under assumptions A1-A3 (stated and justified in §III), the model yields Theorem 1" |
| "State-of-the-art performance." | Claim scoped to the topology, traffic, and regime actually tested |

## Defensive-writing discipline (no rebuttal)

```text
[Assumption]  which modeling assumption will a theory reviewer challenge? -> justify it in §III
[Baseline]    which comparison will a systems reviewer call unfair? -> tune it, document the budget
[Scale]       does the evaluation reach a realistic size? -> if not, scope the claim and say so
[Regime]      where does the result break? -> state it before a reviewer finds it
-> each objection answered in the PDF, because there is no turn to answer it in a reply
```

## Vignette: compressing an over-scoped analytical paper

A draft with two models, five theorems, and a sprawling evaluation: keep the one model the design
uses, the two theorems that carry the insight (full proofs compressed or sketched), and the two
evaluation figures that test the headline claim; move notation-heavy derivations into a tight
in-budget appendix (remember it counts toward the nine pages); cut the second model to a remark.
The test of a good cut: a reviewer should be able to state your assumptions, your main result, and
why your baseline is fair — from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-modeled / over-claimed / evidence-mismatched / over-scoped
[First-page fix] <new framing leading with the networking problem + system model>
[Claim audit] <claim -> proof or simulation/measurement -> proportional? yes/no>
[Defensive gaps] <assumption/baseline/scale/regime objection -> where to pre-empt it>
[Anonymity edits] <self-citations / tool / testbed names / acks to rewrite>
```
