---
name: podc-review-process
description: Use when reasoning about how an ACM PODC submission is evaluated — covering lightweight double-blind review, a program committee that reads proofs, the accept/reject decision with no journal-style revision round, the Brief Announcements track's lighter bar, and how PODC's process differs from DISC, SPAA, and the sequential-theory venues STOC/FOCS/SODA.
---

# PODC Review Process

Model the pipeline before interpreting any single review. PODC's process is **proofs-first and
single-shot**: a specialized program committee reads your model and your proof, and the decision is
**accept or reject** — there is **no Major Revision, no journal-style R&R**. The most consequential
mental shift for authors arriving from a software-engineering or ML venue is that there is no second
read to fix a gap in; everything that would go into a revision must be in the initial submission.

## Process model

- Submission and review run on **HotCRP** with **lightweight double-blind** anonymity: identities
  are hidden from reviewers (no author names/affiliations/emails in the submission), a change from
  PODC's historically single-blind practice.
- Each paper is read by program-committee members (often with external subreviewers for specific
  subareas) who weigh: the **significance** of the result, the **correctness of the proof**, the
  **precision and honesty of the model/assumptions**, **novelty** against known bounds, and clarity.
- The committee reads the abstract and the **first 10 pages** as guaranteed; deeper proofs are read
  at its discretion — so the merits case must land in those pages (`podc-supplementary`).
- Decisions are **accept / reject**. Accepted regular papers publish in the ACM proceedings (≤10
  pages); Brief Announcements (≤3 pages) are a separate, lighter-bar track.
- There is typically **no revision round**; whether a **rebuttal / author-response** phase runs
  varies by cycle (**待核实** for 2026 — confirm on the call).

## What a PODC reviewer actually checks

| Dimension | The reviewer's question | How to pass it |
|---|---|---|
| Correctness | Does the proof close in the stated model? | Self-contained proofs; no assumption creep |
| Significance | Does this advance a problem the community cares about? | Position against the closest known bounds |
| Model honesty | Are the timing/fault/adversary assumptions declared and consistent? | An explicit model box the proofs never violate |
| Novelty | Is the result / technique new relative to PODC/DISC/journals? | A precise delta, not a topic list |
| Tightness | Is an "optimal" claim backed by a matching lower bound? | Prove or cite the lower bound, or don't claim optimal |

A reviewer who finds a **proof gap** or an **undeclared assumption** will reject on soundness, and
there is no revision to repair it — which is why `podc-experiments` (the assumption audit) and
`podc-reproducibility` (self-contained proofs) are pre-submission, not post-notification, work.

## How PODC differs from its siblings

- **vs. DISC:** DISC is the other distributed-theory flagship (EATCS, LIPIcs proceedings, fall
  cycle) and shares the Dijkstra Prize and Dissertation Award with PODC. The *review culture* is
  close; the differences are calendar, proceedings format, and community center of gravity, not the
  proofs-first bar.
- **vs. SPAA:** SPAA centers **parallel** computation; a message-passing fault-tolerance result is
  native at PODC and a visitor at SPAA (and vice versa for shared-memory throughput/scheduling).
- **vs. STOC/FOCS/SODA:** these judge **sequential** algorithms and complexity; a PODC paper's value
  must live in the *distributed* difficulty (faults, asynchrony, locality, concurrency) or it will
  be read as a mislabeled sequential result.
- **vs. software-engineering / ML venues:** no artifact evaluation, no rebuttal-driven Major
  Revision, no empirical-benchmark culture. The object of review is the **proof**.

## Where author leverage actually exists

```text
[Before submission]  topic tags + a precise abstract -> reviewers who know your model   (largest lever)
[Track choice]       regular vs. Brief Announcement -> match the bar to the result's completeness
[In the submission]  a self-contained proof and an honest model box -> pre-empt the soundness reject
[Rebuttal, if any]   correct a factual misreading or supply a missing lemma/bound (待核实 it exists)
[After reject]       no appeal; revise the proof and reroute to DISC/SPAA/a focused venue or a journal
```

Because there is no revision round, the leverage is almost entirely **pre-submission**. The single
highest-value action is closing every proof and declaring every assumption *before* 16 February.

## Reading a decision

| Outcome | What it means | Author move |
|---|---|---|
| Accept | Result, proof, and model hold | Camera-ready (≤10 pages) + arXiv full version; do not weaken claims |
| Accept as Brief Announcement (if offered) | The idea is valued but not a full regular paper this cycle | Publish the ≤3-page BA; develop the full paper for a later venue |
| Reject — soundness | A proof gap or undeclared assumption | Fix the proof; do not resubmit unchanged |
| Reject — significance/novelty | Known bound, or the delta is too small | Strengthen (a matching lower bound?) or reroute |

## Misreadings to avoid

- **Expecting a revision round** — there is none; the submission is the whole case.
- **Treating a preprint as forbidden** — arXiv posting is allowed; only concurrent *submission*
  elsewhere is the dual-submission problem.
- **Assuming a rebuttal exists** — confirm per cycle (待核实 for 2026).
- **Under- or over-anonymizing** — follow the lightweight double-blind wording, neither leaking
  identity nor stripping citations.

## Output format

```text
[Process stage] pre-submission / under review / (rebuttal if any) / decided
[Anonymity model] lightweight double-blind — submission clean of author identity?
[Reviewer-axis map] each review point -> correctness | significance | model-honesty | novelty | tightness
[Leverage plan] the pre-submission or (rebuttal) action that can actually change the outcome
[Forbidden moves] identity leak / claiming a revision round that does not exist / unsupported optimality
```
