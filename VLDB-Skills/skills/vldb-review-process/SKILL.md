---
name: vldb-review-process
description: Use when reasoning about how PVLDB reviewing actually works, covering the rolling monthly pipeline, the roughly six-week review turnaround, the accept/revise/reject outcome space, the one-shot revision's odds, single-blind dynamics, the volume review board, and how a VLDB decision differs from batch-deadline venues.
---

# VLDB Review Process

Use this to set expectations after (or before) a PVLDB submission. The process
is a journal pipeline wearing a conference badge: a standing review board for
the volume, decisions on a monthly cadence, and a revision outcome with teeth.
Details below were verified 2026-07-08 for Vols 19/20; the live guidelines page
governs.

## The pipeline at a glance

```text
25th: abstract  ->  1st: paper (5PM PT)  ->  ~15th next month: reviews + verdict
                                                    |
                            accept ---------------- 3 outcomes ---------------- reject
                                                    |
                                            revise (one-shot)
                                                    |
                              up to 3 months -> revised paper -> same reviewers
                                                    |
                                             accept or reject
```

Roughly six weeks from deadline to decision is the structural promise of the
rolling model — competitive with any CS venue — and the price is that there is
no rebuttal stage: your first chance to talk back is the revision, if offered.

## What each outcome means here

| Outcome | Practical meaning | Your move |
|---|---|---|
| Accept | Publication in an upcoming monthly issue; conference slot at the matching VLDB | Camera-ready discipline (`vldb-camera-ready`) |
| Revise | Reviewers believe a specific, listed set of fixes could flip them | Requirement ledger + three-month plan (`vldb-author-response`) |
| Reject | The paper as framed did not convince this panel | Rework before any re-entry; check current re-submission rules (待核实 whether an embargo applies) |

A revise verdict is genuinely positive signal — the board spends its future
reviewing time only on papers it considers rescuable.

## Who is reading

- The volume operates with Editors-in-Chief (who double as the conference PC
  chairs — Vol 20: Boehm and Hose per secondary sources) atop a standing
  review board assembled for the volume.
- Expect builder-reviewers: people who wrote storage engines, optimizers, and
  the baselines you measured. Implementation hand-waving and untuned
  competitors are caught by lived experience, not by checklists.
- Review is single-blind: reviewers see your names. Track records cut both
  ways — a known group gets less benefit of the doubt for overclaiming, not
  more.

## Reading reviews on the monthly clock

- The verdict letter's required-changes list is the only text that matters for
  a revise; reviewer musings outside it are advisory.
- For a reject, extract the *decision reason* (novelty vs. evidence vs. fit)
  before touching the draft — rolling venues tempt authors into resubmitting
  cosmetically-edited papers at machine-gun pace, and review boards notice.
- Timing tactics around "easier months" are folklore; the board is standing
  and the bar does not oscillate. Pick the month your evidence is ready.

## Contrast with batch venues

At a batch-deadline conference a rejection costs a year and a rebuttal is a
480-word ritual; at PVLDB a rejection costs a rework cycle, and the revision
is a real second review with new evidence allowed. Optimize accordingly: at
this venue, holding a submission until the weakest experiment is fixed is
cheap, and burning the revision on a preventable flaw is expensive.

## Output format

```text
[Stage] pre-submission / under review / revise / rejected / accepted
[Clock position] <deadline used, expected decision date>
[Outcome analysis] <required-changes list or decision reason>
[Panel model] <likely reviewer profile for this topic>
[Next move] <hold, revise per ledger, rework, or camera-ready>
[Rules to reverify] <re-submission terms, current escalation channel>
```
