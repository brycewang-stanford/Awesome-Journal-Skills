---
name: ase-review-process
description: Use when reasoning about how an ASE (IEEE/ACM Automated Software Engineering) research submission is evaluated, covering double-anonymous review, the early-rejection stage before rebuttal, the Accept / Revision / Reject outcomes, the criteria-bound revision round, and how ASE's process differs from FSE's PACMSE Major Revision, ICSE's cycles, and ISSTA's rounds.
---

# ASE Review Process

Model the pipeline before interpreting any single review. ASE's process has **two distinctive
gates** that authors from a plain accept/reject conference miss: an **early-rejection stage** that
ends the process *before* rebuttal for the weakest papers, and a first-class **Revision** outcome
whose criteria are fixed in advance. Getting both wrong wastes the little leverage authors have.

## Process model

- Submission and review run on **HotCRP** with **double-anonymous** review: identities are hidden
  from reviewers, and authors reference their own prior work in the third person.
- Each paper receives multiple reviews scoring the **significance and soundness of the automation**,
  the quality of the evaluation on real subjects, threats to validity, clarity, and the Data
  Availability / artifact posture.
- **Early-rejection stage:** papers whose initial scores are **uniformly negative are rejected
  before the rebuttal period**. This is a mercy and a filter — it gives those authors a fast answer
  and concentrates rebuttal effort where it can change an outcome. If your paper survives to
  rebuttal, at least one reviewer saw something.
- **Rebuttal**, then a final outcome of **Accept**, **Revision**, or **Reject**.
- **Revision** is criteria-bound: instead of rejecting, reviewers specify **concrete, actionable
  revision criteria** and agree to **accept the paper in principle if those criteria are met**.
  Authors return a revised paper with a **point-by-point summary of changes**, re-checked (often by
  a discussion lead) against the stated criteria.
- Accepted papers appear in the proceedings in **both IEEE Xplore and the ACM Digital Library**;
  camera-ready compliance and artifact follow-through matter after the verdict.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | The automation and its evaluation hold; minor polish only | Camera-ready + artifact; do not reopen scope |
| Revision | Repairable gaps captured as explicit criteria: a missing baseline, an ablation, a clarified construct | Meet **every** stated criterion, or justify why one is infeasible; map each to a change in the summary-of-changes |
| Reject | Structural: the automation is unsound, the evaluation is not on real subjects, the delta is thin | Reframe or reroute (ICSE/FSE/ISSTA or a journal); do not lightly resubmit unchanged |
| Early reject (pre-rebuttal) | Uniformly negative initial scores | No rebuttal opportunity; diagnose honestly and rebuild before any resubmission |

The strategic reading: write the initial submission so its weakest point is **expressible as a
revision criterion** (an ablation you can add, a subject set you can extend) rather than
**structural** (a tool you would have to redesign). The Revision outcome rewards papers that are one
bounded step from done.

## How ASE differs from its siblings

- **vs. ESEC/FSE:** FSE papers are **PACMSE journal articles** with a Major Revision round and heavy
  double-anonymity into the response letter. ASE is a **conference** (dual IEEE/ACM, proceedings in
  IEEE Xplore *and* ACM DL) whose Revision is criteria-bound but lighter-weight, and whose center of
  gravity is *automation* rather than broad empirical SE. Do not assume shared calendars, templates,
  or that ASE's Revision equals PACMSE's Major Revision.
- **vs. ICSE:** ICSE runs its own multi-cycle structure on the IEEE side; ASE's early-rejection +
  Revision model is its own. Never carry ICSE's cadence or page box across.
- **vs. ISSTA:** ISSTA has used multi-round reviewing for *every* paper within a cycle; ASE's
  Revision is **decision-driven** (you revise because you were told to, against fixed criteria), not
  a scheduled second read of the whole pool.

## Who reads you

Expect automated-SE specialists: people who build analyzers, test generators, synthesizers, repair
tools, and code models. They check whether the automation is **sound and general**, whether the
evaluation uses **real subject systems** and **fair tool baselines**, whether claims outrun
evidence, and they frequently open the artifact. A tool described vaguely gets caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  area/topic tags -> reviewer pool               (largest lever)
[Initial reviews]    factual corrections, targeted evidence, clarifying a misread tool/experiment
[Rebuttal]           survive early rejection first; then move the borderline reviewer with numbers
[Revision]           the strongest lever: meet each fixed criterion, mapped in the summary-of-changes
[After reject]       no appeal; reroute to a sibling flagship or a journal
```

A rebuttal moves borderline papers when it corrects a factual misreading or supplies a number a
reviewer said was missing; it does not move papers when it argues taste. In a Revision, a criterion
that is **neither met nor explicitly addressed** is what turns the re-check into a rejection.

## Misreadings to avoid

- **Treating Revision as a guaranteed accept** — the re-check against the criteria is real.
- **Ignoring a stated criterion** — silent omission of even one is the classic Revision failure.
- **Treating the rebuttal as a debate** — the PC discussion decides; your text is evidence for an
  advocate, not a closing argument.
- **Forgetting the early-rejection gate** — a uniformly weak first impression ends the process with
  no rebuttal; the first three pages and the evaluation table must land immediately.
- **Projecting last year's cadence** — deadline count and revision timing are decided per edition.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / rebuttal / revision / final / accepted
[Decision category] accept / revision / reject / early-reject, with the criterion driving it
[Criterion map] each review point (or revision criterion) -> significance | soundness | evaluation | threats | clarity | data-availability
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak (incl. in rebuttal/summary-of-changes) / unsupported new claims / ignoring a stated criterion
```
