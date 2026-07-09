---
name: sigmetrics-review-process
description: Use when reasoning about how an ACM SIGMETRICS submission is evaluated, covering the hybrid conference-journal model, double-anonymous review, the three first-round outcomes (Accept-with-shepherding / One-Shot Revision / Reject), the one-shot revision resubmitted to a subsequent rolling deadline, the 12-month resubmission bar, and how SIGMETRICS differs from IMC, SIGCOMM, and NSDI.
---

# SIGMETRICS Review Process

Model the pipeline before interpreting any single review. SIGMETRICS's process is a **hybrid of the
conference and journal models**: papers are POMACS articles, and the first-round decision is one of
**three** outcomes, not a binary accept/reject. The most consequential mental shift for authors
arriving from a plain conference is that **One-Shot Revision** is a real revise-and-resubmit round —
but, unlike an open-ended journal R&R, it is **single-shot** and re-reviewed against an explicit
list of required changes.

## Process model

- Submission and review run on **HotCRP**, one site per rolling deadline, with **double-anonymous**
  review (the Operational Systems Track may reveal the deploying org/system).
- Reviewers weigh the **rigor of the model or measurement**, the **correctness of proofs**, the
  **validity of assumptions**, the fairness and soundness of any empirical/simulation evidence,
  novelty, and reproducibility. SIGMETRICS reviewers check theorems, not just plots.
- **Three first-round outcomes:**
  - **Accept** — every accepted paper is **shepherded**, so reviewer-required changes are
    incorporated into the final POMACS version.
  - **One-Shot Revision** — a major-revision decision: the authors receive a summary of merits and
    a **list of necessary changes**, and may resubmit a revised version to **one of the two
    subsequent SIGMETRICS/Performance deadlines**, where it is re-reviewed (generally by the
    original reviewers).
  - **Reject** — may **not** be resubmitted to any SIGMETRICS deadline within **12 months** of the
    initial submission.
- Accepted papers publish in **POMACS**; summer/fall acceptances appear before the conference.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept (shepherded) | Rigor and evidence hold; shepherd will enforce specific fixes | Execute the shepherd's list precisely; do not reopen scope |
| One-Shot Revision | Repairable gaps: a missing proof case, an unvalidated assumption, a needed experiment | Treat as a single-shot R&R: close **every** listed change, resubmit to a subsequent deadline |
| Reject | Structural: flawed model, wrong metric, unfixable evidence | Reframe or reroute; you cannot resubmit to SIGMETRICS for 12 months |

The strategic reading: write the initial submission so that whatever is weakest is **fixable in one
revision round** (a proof case you can add, a simulation you can run) rather than **structural** (a
model that does not capture the system). The process rewards repairable papers, but the revision is
**one shot** — a second revision is not offered.

## The one-shot-revision mechanics (the distinctive SIGMETRICS move)

- You get **one** resubmission, targeting **one of the next two deadlines** — pick the one that
  gives you enough time to close the list without rushing.
- The revision is judged against the **explicit list of required changes**, not re-opened for new
  objections in principle; unaddressed items are what turn the single shot into a reject.
- **Simultaneous-submission caution:** a paper under one-shot revision is considered under
  submission to SIGMETRICS. Submitting it elsewhere before withdrawing is a dual-submission
  violation.

## How SIGMETRICS differs from its siblings

- **vs. IMC (Internet Measurement Conference):** IMC is a single-annual-deadline, measurement-only
  venue; SIGMETRICS runs three rolling deadlines, publishes in POMACS, and welcomes **theory** and
  **learning** alongside measurement. Do not assume IMC's calendar, scope, or accept/reject binary.
- **vs. SIGCOMM / NSDI:** those are networking-systems conferences with rebuttal-then-decision
  cycles; SIGMETRICS's identity is the **rigorous performance-evaluation** framing (proofs of
  bounds) and the one-shot-revision journal hybrid. A systems-building paper often fits NSDI/OSDI
  better than SIGMETRICS.
- **vs. an open-ended journal (TON, Performance Evaluation):** those allow multiple revision rounds;
  SIGMETRICS gives exactly **one** and ties publication to a conference presentation.

## Who reads you

Expect reviewers who are performance-evaluation specialists: they will read a proof for a missing
case, ask whether the M/G/1 (or other) assumptions match the measured workload, check whether a
baseline is fairly tuned, and open the simulator to see whether the analytic curve really matches.
Vague assumptions and hand-waved proofs get caught, not skimmed.

## Where author leverage actually exists

```text
[Before submission]  track + abstract -> reviewer pool               (largest lever)
[Initial reviews]    factual corrections, a missing proof case, an added assumption-validity check
[One-Shot Revision]  the strongest lever: close every listed change, resubmit to a later deadline,
                     re-read by the same reviewers -- but only once
[After reject]       no appeal; 12-month bar on SIGMETRICS resubmission -> reroute meanwhile
```

## Misreadings to avoid

- **Treating One-Shot Revision as a guaranteed accept** — the re-review is real and single-shot.
- **Assuming you can revise twice** — you cannot; budget the one revision to close everything.
- **Forgetting the 12-month bar** after a reject when planning the calendar.
- **Ignoring the shepherd** on an accept — unincorporated shepherd requests can hold the final
  version.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / one-shot revision / shepherding / accepted
[Decision category] accept / one-shot revision / reject, with the criterion driving it
[Criterion map] each review point -> rigor | proof correctness | assumption validity | evidence | novelty | reproducibility
[Revision plan] which subsequent deadline, and the closed-list of required changes
[Forbidden moves] identity leak / dual-submission while under one-shot revision / unaddressed listed change
```
