---
name: cav-review-process
description: Use when reasoning about how a CAV (Computer Aided Verification) submission is evaluated, covering the two-stage reviewing process (two reviews then an early-reject filter, then two more reviews with a rebuttal), the partial double-anonymity by category, the accept/reject outcome, the optional non-conditional artifact evaluation, and how CAV differs from TACAS and FMCAD.
---

# CAV Review Process

Model the pipeline before interpreting any single review. CAV's process is a **two-stage filter**:
a paper must survive the first two reviews before it reaches a rebuttal and the second pair of
reviews. The most consequential mental shift for authors arriving from a single-round rebuttal
conference is that **a paper can be rejected before the rebuttal ever happens** — so the first read
has to stand on its own.

## Process model

- Submission and review run on the CAV portal (EasyChair or HotCRP — **verify the live link**) with
  **partial double-anonymity**: Regular and Application papers are anonymized; Short Tool and
  Industrial Experience papers are not.
- **Stage 1:** each paper receives **two** reviews. Papers with sufficient support proceed; the
  rest are **rejected early** (CAV 2026 tentative first-round outcome ~4 Mar 2026).
- **Stage 2:** surviving papers receive **two additional** reviews and an **author-response
  (rebuttal)** window (CAV 2026: 30 Mar - 2 Apr 2026).
- **Outcome:** accept or reject (CAV 2026 notification 17 Apr 2026). Accepted papers publish open
  access in **Springer LNCS**, and authors may then submit an artifact to the AEC on its own
  deadline.
- Reviewers weigh the **significance** of the verification contribution, the **soundness** of the
  technique and its proofs, the **fairness and reproducibility** of the benchmark evaluation, the
  **novelty/delta** against prior verification work, and **clarity** — and see the artifact-intent
  declaration.

## Reading a decision against the stages

| Signal | What it means | Author move |
|---|---|---|
| Early reject after stage 1 | Two reviewers saw a fatal gap (unsound claim, weak evaluation, thin delta) | No rebuttal exists; reframe or reroute (TACAS/FMCAD/VMCAI) — do not resubmit unchanged |
| Passed to stage 2 | The contribution is plausible; specific concerns remain | Use the rebuttal to fix factual misreadings and supply the missing number/proof detail |
| Accept | Contribution, soundness, and evidence hold | Camera-ready + optional artifact; do not reopen scope |
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
- **Assuming artifact evaluation gates acceptance** — it is optional and non-conditional at CAV.
- **Projecting a sibling's process** — TACAS and FMCAD have their own models; do not carry them over.

## Output format

```text
[Process stage] pre-submission / stage-1 / rebuttal / final / accepted / artifact
[Outcome so far] early-reject / passed to stage 2 / accept / reject, with the driving criterion
[Criterion map] each review point -> significance | soundness/proof | evaluation | novelty | clarity
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak (anonymized categories) / unsupported new claims / unrun promises
```
