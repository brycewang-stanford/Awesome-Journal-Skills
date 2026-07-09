---
name: edbt-review-process
description: Use when reasoning about how an EDBT research submission is evaluated, covering Microsoft CMT reviewing, the author-feedback phase, the accept / revise / reject decision, the in-cycle revise-and-resubmit second read by the original reviewers, the cycle-to-conference roll, and how EDBT's rolling model differs from SIGMOD/VLDB/ICDE and the co-located ICDT.
---

# EDBT Review Process

Model the pipeline before interpreting any single review. EDBT's process is a **multiple-cycle
rolling model** with a real **in-cycle revise-and-resubmit**: within one cycle, a paper is reviewed,
gets an author-feedback exchange, receives **accept / revise / reject**, and — if *revise* — is
revised and re-read by the same reviewers before a final accept/reject. The most consequential
mental shift for authors arriving from a one-shot conference is that a *revise* is a genuine second
chance inside the same cycle, not a soft rejection.

## Process model

- Reviewing runs in **Microsoft CMT** (Conference Management Toolkit). Confirm the blind policy for
  the cycle — single- vs double-blind is decided per edition (**待核实**; EDBT has historically used
  author-identified single-blind reviewing).
- Each paper is read by multiple program-committee members who weigh the significance of the
  data-management contribution, technical soundness, the fairness and honesty of the evaluation
  (real workloads, tuned baselines, realistic scale), reproducibility, and clarity.
- The cycle includes an **author-feedback phase** on the initial reviews, then a first notification
  of **accept / revise / reject**.
- A **revise** becomes a revised submission plus a change letter, re-read — generally by the
  original reviewers — for a second notification of accept / reject **within the cycle**.
- Accepted papers publish **open access on OpenProceedings.org** (CC-BY-NC-ND). Earlier-cycle
  acceptances present at that year's conference; last-cycle acceptances roll to the next edition.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | Contribution and evaluation hold; minor polish only | Camera-ready + artifact; do not reopen scope |
| Revise | Repairable gaps: a missing baseline, an unconvincing scale, an unclear mechanism | Treat as an in-cycle R&R: make or explicitly decline every request, evidenced |
| Reject | Structural: wrong problem framing, unfair or missing evaluation, thin contribution | Reframe or reroute (SIGMOD/VLDB/ICDE/ICDT or a journal); remember the 12-month EDBT ban |

The strategic reading: write the initial submission so that whatever is weakest is **fixable inside
the in-cycle revision window** (a baseline you can add, a scale you can extend, a mechanism you can
clarify) rather than **structural** (an evaluation you cannot redo in the cycle). The process rewards
repairable papers.

## How EDBT differs from its siblings

- **vs. SIGMOD / ICDE:** those publish in the paywalled ACM DL / IEEE Xplore and run their own cycle
  structures; EDBT's identity is the **OpenProceedings open-access** record and the **three-cycle
  rolling** cadence. Never assume a shared calendar or template.
- **vs. VLDB / PVLDB:** PVLDB is a journal-style monthly pipeline with its own revision mechanics;
  EDBT's revise-and-resubmit is bounded **inside a discrete cycle**, not a rolling monthly journal.
- **vs. ICDT (the co-located sibling):** ICDT reviews **theory** on its own call and PC; sharing a
  conference week and the OpenProceedings platform does not make them one process. An EDBT paper is
  judged by DB-systems reviewers, not theory reviewers.

## Who reads you

Expect several database-systems reviewers. They look for a real data-management problem, a mechanism
described precisely enough to reimplement, an evaluation on real workloads at honest scale against
tuned baselines, and a reproducible artifact. For an **Experiments & Analysis** paper the bar is
higher on the measurement itself: methodology, coverage, and repeatability are the contribution.

## Where author leverage actually exists

```text
[Before submission]  subject-area tags + cycle choice -> reviewer pool + timing   (largest lever)
[Author feedback]    factual corrections, targeted clarifications, misread fixes
[Revise]             the strongest lever: a revised paper + point-by-point change letter,
                     re-read by the same reviewers inside the cycle
[After reject]       no appeal; reroute to a sibling venue or journal, and mind the 12-month ban
```

A response moves borderline papers when it corrects a factual misreading or supplies a measurement a
reviewer said was missing; it does not move papers when it argues taste. In a revise, **silent
omissions** — a requested change neither made nor explicitly declined with a reason — are what turn
the second read into a rejection.

## Reading a review packet

Weight reviews before answering. A review that cites your figures, tables, and configuration was
read closely and will be read closely again in the revision — its author is your likely advocate if
the changes hold. A review that discusses only novelty has left soundness and reproducibility to the
others; answer each reviewer on the axis they raised. Reviewers often end with an explicit request
list; the revision is scored heavily on whether each request got a direct, evidenced answer.

## Misreadings to avoid

- **Treating a revise as a guaranteed accept** — the in-cycle second read is real; budget the
  revision window like a deadline.
- **Treating the author-feedback phase as the whole game** — it is short and decision-focused; the
  revision carries the real argument.
- **Assuming the last cycle presents this year** — it rolls to the next edition.
- **Confusing EDBT and ICDT reviewing** — separate calls, separate PCs, despite the joint week.
- **Projecting last year's cadence** — cycle count and per-cycle timing are decided per edition.

## Output format

```text
[Process stage] pre-submission / author-feedback / revise / final / accepted
[Cycle] which cycle, presents at <edition/year>
[Decision category] accept / revise / reject, with the criterion driving it
[Criterion map] each review point -> significance | soundness | evaluation | reproducibility | clarity
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] unsupported new claims / (if double-blind) identity leak
```
