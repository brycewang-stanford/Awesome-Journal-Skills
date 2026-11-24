---
name: cav-review-process
description: Use when reasoning about how a CAV (Computer Aided Verification) submission is evaluated, covering the two-stage reviewing process (two reviews then an early-reject filter, then two more reviews with a rebuttal), the per-category anonymity split (only Regular Papers double-blind in CAV 2027), the accept/reject outcome, the artifact evaluation that is mandatory for Tool Papers and optional for other categories, and how CAV differs from TACAS and FMCAD.
---

# CAV Review Process

Model the pipeline before interpreting any single review. CAV's process is a **two-stage filter**:
a paper must survive the first two reviews before it reaches a rebuttal and the second pair of
reviews. The most consequential mental shift for authors arriving from a single-round rebuttal
conference is that **a paper can be rejected before the rebuttal ever happens** — so the first read
has to stand on its own.

## Process model

- Submission and review run on **HotCRP** (CAV 2027; the CFP link was not yet posted on
  2026-11-24 — **verify the live link**) with **partial double-anonymity**: in CAV 2027 only
  Regular Papers are anonymized; Tool Papers and Application/Industrial/Case Study Papers are
  single-blind. (CAV 2026 also anonymized Short Application Papers.)
- **Stage 1:** each paper receives **two** reviews. Papers with sufficient support proceed; the
  rest are **rejected early** (CAV 2027 early rejection notification: 4 Mar 2027).
- **Tool Papers in parallel:** the mandatory tool-paper artifact is registered (8 Mar 2027),
  submitted (11 Mar 2027) and smoke-tested during the review; the paper is accepted only if the
  artifact earns at least the Functional badge.
- **Stage 2:** surviving papers receive **two additional** reviews and an **author-response
  (rebuttal)** window (CAV 2027: 5-8 Apr 2027).
- **Outcome:** accept or reject (CAV 2027 notification 23 Apr 2027). Accepted papers publish in
  **Springer LNCS**, and authors of non-tool papers may then submit an artifact to the AEC on its
  own deadline (26 Apr / 3 May 2027).
- CAV 2027 evaluates Regular Papers on correctness, technical depth, significance, novelty,
  clarity, and transparency. In practice reviewers weigh the **significance** of the verification
  contribution, the **soundness** of the technique and its proofs, the **fairness and reproducibility** of the benchmark evaluation, the
  **novelty/delta** against prior verification work, and **clarity** — and see the artifact-intent
  declaration.

## Reading a decision against the stages

| Signal | What it means | Author move |
|---|---|---|
| Early reject after stage 1 | Two reviewers saw a fatal gap (unsound claim, weak evaluation, thin delta) | No rebuttal exists; reframe or reroute (TACAS/FMCAD/VMCAI) — do not resubmit unchanged |
| Passed to stage 2 | The contribution is plausible; specific concerns remain | Use the rebuttal to fix factual misreadings and supply the missing number/proof detail |
| Accept | Contribution, soundness, and evidence hold (and, for a Tool Paper, the artifact earned at least Functional) | Camera-ready + optional artifact for non-tool papers; do not reopen scope |
| Reject after stage 2 | A concern the rebuttal did not resolve | Address it substantively before any resubmission |

The strategic reading: write the submission so its **soundness and headline benchmark result are
legible in the first two reviews**. A contribution that only convinces after the rebuttal may never
reach the rebuttal.

## How CAV differs from its siblings

- **vs. TACAS:** TACAS (at ETAPS) overlaps heavily in scope and also values tools, but is a distinct
  venue with its own calendar and process; never assume they share a deadline or a review model.
  CAV's identity is the flagship LNCS proceedings and the two-stage filter.
- **vs. FMCAD:** FMCAD centers formal methods in hardware/design; its review culture and page model
  differ. A hardware-methodology paper may be read as more native there.
- **vs. a single-round rebuttal conference:** the early-reject stage is the key difference — plan for
  it (`cav-workflow`).

## Who reads you

Expect verification-literate reviewers matched to your subarea (model checking, SMT, theorem
proving, program analysis, hardware or NN verification). They check whether the **theorem actually
holds**, whether the **baselines and benchmarks are fair and pinned**, whether the claim is scoped
to what was proved and measured, and — for tool papers — whether the **tool is real and usable**.
Vague algorithm descriptions and unpinned benchmarks get caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  category + topic tags -> reviewer pool and page/anonymity rules  (largest lever)
[Stage 1]            nothing to do but wait; the paper must defend itself
[Rebuttal (stage 2)] correct factual misreadings; supply a missing number, proof detail, or
                     benchmark clarification the reviewers can verify
[After reject]       no appeal; reroute to a sibling flagship or a journal (FMSD/JAR)
```

A rebuttal moves borderline papers when it corrects a misreading of a theorem or supplies a
benchmark clarification a reviewer said was missing; it does not move papers when it argues taste or
promises unrun experiments.

## Reading a review packet

Weight reviews before answering. A review that engages your theorem statement, checks your
assumptions, or questions a specific benchmark was read closely and will be read closely again — its
author is your likely advocate if the rebuttal holds. A review that only questions novelty has left
soundness and evaluation to the others; answer each reviewer on the axis they raised. Reviewers
often end with explicit questions; the rebuttal is scored heavily on whether each got a direct,
verifiable answer.

## Misreadings to avoid

- **Treating stage 1 as a formality** — the early-reject filter is real; the first two reviews
  decide whether a rebuttal ever happens.
- **Treating the rebuttal as a debate** — the PC decides; your response is evidence for an advocate,
  not a closing argument.
- **Getting the artifact gate backwards** — in CAV 2027 it gates acceptance for Tool Papers only;
  for every other category it is optional and non-conditional.
- **Projecting a sibling's process** — TACAS and FMCAD have their own models; do not carry them over.

## Output format

```text
[Process stage] pre-submission / stage-1 / rebuttal / final / accepted / artifact
[Outcome so far] early-reject / passed to stage 2 / accept / reject, with the driving criterion
[Criterion map] each review point -> significance | soundness/proof | evaluation | novelty | clarity
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak (Regular Papers) / unsupported new claims / unrun promises
```
