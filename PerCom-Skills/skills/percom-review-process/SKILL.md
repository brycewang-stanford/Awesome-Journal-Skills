---
name: percom-review-process
description: Use when reasoning about how an IEEE PerCom research submission is evaluated, covering double-blind review, the three-TPC-member model, the early-rejection stage, the single-round bounded rebuttal gated by a "weak accept," the accept/reject decision, and how PerCom's process differs from ACM UbiComp/IMWUT's journal revise cycle.
---

# PerCom Review Process

Model the pipeline before interpreting any single review. PerCom's process is a **single annual
review round with a bounded rebuttal and an early-rejection gate** — not a journal-style
revise-and-resubmit, and not a multi-deadline conference. The most consequential mental shift for
authors arriving from ACM UbiComp/IMWUT is that there is **no revise cycle**: the paper is judged
on what it submitted, with one bounded chance to answer questions.

## Process model

- Submission and review run on **HotCRP** with **double-blind** review: authors anonymize in good
  faith and cite their own prior work in the third person.
- Each reviewed paper is read by **three** TPC members, who weigh the significance of the
  pervasive-computing contribution, soundness of the method, quality and honesty of the evaluation
  (real subjects, cross-subject generalization, appropriate metrics), and clarity.
- **Early-rejection gate.** After the initial reviews, papers for which **no reviewer** sees a path
  to publication are **early-rejected** and notified (PerCom 2027: ~20 November 2026), so authors
  can improve and target another venue promptly. There is **no rebuttal** for these papers.
- **Rebuttal (bounded).** Papers with **at least one "weak accept"** (a reviewer sees a path) are
  **invited to submit a rebuttal** (~26 November 2026) addressing explicit reviewer questions. The
  rebuttal resolves misunderstandings and clarifies; **new experiments are not expected.**
- **Final decision** (accept / reject) follows TPC discussion; notification PerCom 2027:
  ~18 December 2026. Accepted papers publish in **IEEE Xplore**.

## Reading a decision against the stages

| Stage / outcome | What it means | Author move |
|---|---|---|
| Early reject | No reviewer saw a path; a structural gap (within-subject only, no baseline, thin contribution) | Reframe or reroute (UbiComp/IMWUT, MobiCom, or rework for next PerCom); do not resubmit unchanged |
| Invited to rebuttal | At least one reviewer is an advocate; repairable doubts remain | Answer explicit questions crisply; correct misreadings; point to existing evidence — no new claims |
| Accept | Contribution and evaluation hold | Camera-ready + dataset release; do not reopen scope |
| Reject after rebuttal | Doubts not resolved, or discussion turned | Use the reviews to rework; the study likely needs stronger cross-subject or deployment evidence |

The strategic reading: because the rebuttal cannot add experiments, **write the initial submission
so its weakest point is a *misreading you can correct* or a *clarification you can give*, not a
missing experiment.** The process rewards papers that arrive complete and only need
disambiguating.

## How PerCom differs from its neighbors

- **vs. ACM UbiComp/IMWUT:** IMWUT is a **journal** with rolling quarterly deadlines and a genuine
  **major/minor revision** cycle — you can add experiments in revision. PerCom has **one deadline,
  one round, one bounded rebuttal, no revision**. Never carry an IMWUT revise-and-resubmit mindset
  into a PerCom rebuttal.
- **vs. MobiCom/SenSys:** those venues center the network or the sensor system; PerCom reviewers
  center the human — a systems paper with no human-in-the-loop story reads as mis-venued here.
- **vs. a plain accept/reject conference:** the **early-rejection gate** is distinctive — many
  papers never reach the rebuttal at all, which is why the initial submission carries almost all
  the weight.

## Who reads you

Expect three ubicomp reviewers. They look for **cross-subject / leave-one-subject-out** evaluation,
check whether an activity-recognition number is F1 on realistic class balance rather than pooled
accuracy, ask whether subjects and deployments are real, and probe deployment realism and
generalization. Because PerCom spans recognition, systems, and human factors, a paper is usually
matched to reviewers from its own subarea — thin evaluations get caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic tags + a complete, cross-subject evaluation   (largest lever)
[Early-rejection gate] nothing to do once here; the initial paper decided it
[Rebuttal]           correct factual misreadings; answer explicit questions; cite existing
                     results the reviewer missed -- NOT promise new experiments
[After reject]       no revise cycle; rework and target next PerCom or a neighbor venue
```

A rebuttal moves borderline papers when it corrects a misreading or points to a number a reviewer
overlooked; it does not move papers when it argues taste or promises work not in the submission.

## Reading a review packet

Weight reviews before answering. A review that cites your sections, tables, and evaluation splits
was read closely and will decide the discussion — its author is your likely advocate if the
rebuttal holds. A review that discusses only novelty has left soundness to the others; answer each
reviewer on the axis they raised. Reviewers usually end with an explicit question list; the
rebuttal is scored on whether each question got a direct, evidenced answer from **material already
in the paper**.

## Misreadings to avoid

- **Treating the rebuttal as a revision** — you cannot add experiments; you can only clarify and
  correct.
- **Assuming every paper gets a rebuttal** — the early-rejection gate ends many papers first.
- **Treating the rebuttal as a debate** — the TPC discussion decides; your text is evidence for an
  advocate, not a closing argument.
- **Projecting an IMWUT revise cycle** — PerCom has one round; budget accordingly.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / early-reject / invited-to-rebuttal / final
[Outcome likelihood] driver criterion (significance | soundness | evaluation | clarity)
[Criterion map] each review point -> significance | soundness | cross-subject evaluation | clarity
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak / promising new experiments in the rebuttal
```
