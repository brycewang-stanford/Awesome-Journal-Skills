---
name: mobicom-workflow
description: Use when planning a MobiCom campaign across the rolling two-deadlines-per-year calendar — deciding which round to target and which edition it feeds, building a backward schedule that leaves room for over-the-air experiments, and sequencing the two-round review, rebuttal, and one-shot revision so a slip does not silently cost an edition.
---

# MobiCom Workflow

MobiCom's calendar is the part authors from single-deadline venues mis-plan most. There are
**two rounds a year**, each feeds a **different edition**, and inside each round the review
runs in **two stages with a rebuttal**. Plan the campaign around those facts, not around a
single "the deadline."

## Which round, which edition

Before scheduling anything, pin two facts on the live CFP / HotCRP `/deadlines` page:

- **Which edition does this round feed?** The summer/fall round opening after MobiCom 2026
  competes for **MobiCom 2027**. Submitting to it is a bet on next year's program, not this
  year's.
- **What is the AoE cutoff in local time?** MobiCom prints an Eastern clock time for an
  AoE deadline; convert once, for every coauthor (`mobicom-submission`).

Picking the round is a research-readiness decision: the earlier round gets your work in
front of reviewers sooner, but only if the over-the-air evaluation is actually done.

## Backward schedule from the paper cutoff

Radio experiments do not compress the way a proof or an ablation does — testbeds break,
channels drift, and volunteers for mobility runs have to be scheduled. Work backward:

| Weeks before paper cutoff | Milestone |
|---|---|
| T-12 | Fit and round locked (`mobicom-topic-selection`); testbed reserved; IRB/site access if human mobility |
| T-8 | Core mechanism frozen; headline over-the-air experiment running, not just designed |
| T-5 | Baselines on tuned hardware; energy and channel measurement complete (`mobicom-experiments`) |
| T-3 | Full draft; provenance ledger closed (`mobicom-reproducibility`) |
| T-2 | Writing-style and related-work passes; supplementary/appendix split |
| T-1 (abstract cutoff) | Abstract registered on HotCRP; author list and conflicts entered |
| T-0 (paper cutoff, AoE) | Submission audit and upload (`mobicom-submission`) |

The rule of thumb from wireless deadline archaeology: **the mobility and failure-condition
experiments are always the ones cut when the schedule slips**, and they are the ones
reviewers value most. Protect them by running them before the final scale sweeps.

## Inside the round: two stages plus rebuttal

```text
Round opens -> submission
  Stage 1 review -> either EARLY REJECT (with reviews) or advance
  Stage 2 review -> reviews released -> REBUTTAL window -> decision
Decision space: accept / one-shot revision / reject
```

- An **early reject after stage 1** returns reviews you can use for the *next* round — treat
  it as data, not just a loss (`mobicom-review-process`).
- The **rebuttal** is short and bounded; plan the coauthor time for it now, because it lands
  on a fixed clock you do not control (`mobicom-author-response`).
- A **one-shot revision** is a months-long commitment to a required-changes list, often with
  the same reviewers — budget the experiments it will demand before accepting the plan.

## Which edition a slip costs

Because rounds feed editions, missing the summer round does not just delay a few weeks — it
pushes the work to the winter round of the *same* edition or, if that slips too, to the next
edition entirely. Map the cost explicitly:

- On track for the summer round → decision months earlier.
- Slip to the winter round → same edition, later PC meeting.
- Slip again → next edition; a full year of program calendar.

State which of these the current plan is really on, in machine-days of remaining testbed
work, so "we'll make summer" is a claim with arithmetic behind it, not optimism.

## During the long review silence

MobiCom reviews take weeks. Do not stall: extend the evaluation you already have (more
mobility traces, a deployment week, an energy sweep) so that whatever the letter says —
rebuttal, revision, or the next round — you are answering from a stronger position than the
submitted version.

## Output format

```text
[Round] which round + which edition it feeds + AoE cutoff (local)
[Readiness] over-the-air evaluation done? y/n — gating experiments named
[Backward schedule] milestones with dates; slip risks flagged
[Slip cost] which edition a miss pushes the work to
[Post-decision plan] rebuttal / revision / next-round readiness
```
