---
name: sigcomm-author-response
description: Use when drafting an ACM SIGCOMM rebuttal or executing a shepherd-run one-shot revision — triaging reviewer issues, writing a decision-focused anonymous rebuttal for the discussion phase, and building the revision packet (point-by-point response, change-marked manuscript, and list of changes) against the required-changes contract.
---

# SIGCOMM Author Response

SIGCOMM has two distinct author-facing replies, and conflating them is a strategic error.
The **rebuttal** is a short argument during the discussion phase; the **one-shot revision** is
a month-long, shepherd-managed contract. Reopen the current CFP to confirm the mechanics
before drafting.

## First, know which reply you are writing

| Signal in the letter | You are in | The move |
|---|---|---|
| Reviews plus an invitation to respond, no verdict | Rebuttal / discussion phase | Answer the decision-critical objection concisely |
| A merits summary and a list of required changes | One-shot revision | Treat the list as a binding contract; resubmit with a packet |
| An early notification of rejection | Early reject | No reply reopens it; redirect the work |

## Writing the rebuttal

- Answer the concern that decides the paper first: evaluation realism, a missing baseline, a
  correctness question, or a generalization doubt. Style complaints wait.
- Anchor every answer in evidence already in the submission — a table, a figure, an appendix
  measurement — rather than promising new experiments the reviewers cannot see.
- Stay anonymous: no institution, deployment name, or private link that breaks double-blind.
- Concede cleanly what cannot be fixed in the window, and scope a camera-ready wording change
  instead of overclaiming a result you cannot produce now.
- One precise, decision-focused reply per reviewer beats an exhaustive point-by-point that
  buries the objection that actually matters to the discussion.

## Executing the one-shot revision

The revised paper can only be accepted or rejected, so the required-changes list is the
grading rubric. Build the packet the CFP expects:

1. **Point-by-point response** mapping each required change to exactly what you did and where.
2. **Change-marked manuscript** so the shepherd and reviewers see the diff without hunting.
3. **List of changes** at a high level, so a reader gets the shape before the detail.

Then work the contract, not the margins:

- Address **every** listed issue explicitly; a revision that improves adjacent things but
  dodges a listed item is the classic one-shot rejection.
- Engage the **shepherd** through HotCRP early — clarify an ambiguous requirement before you
  build the wrong fix, not after.
- Keep results **honest to the new evidence**; if a required experiment weakens a claim,
  rescope the claim rather than hiding the outcome.

## Reviewer pushback patterns and SIGCOMM-ready fixes

| Pushback | What it signals | SIGCOMM-ready fix |
|---|---|---|
| "Evaluated only in simulation" | Evaluation-realism doubt | Point to the testbed/trace result, or commit one in the revision and report it plainly |
| "Baseline is weak" | The strongest alternative was skipped | Add or defend the state-of-the-art comparison at matched conditions |
| "Only mean latency reported" | Tail behavior hidden | Report the relevant percentiles over repeated trials with stated variance |
| "Does it generalize beyond this topology?" | Mechanism looks tuned | Add a topology/parameter sweep, or scope the claim to what was tested |

## Micro-example (revision)

Reviewer requires a comparison against the deployed state-of-the-art at matched throughput.
Packet skeleton: (1) response entry naming the added baseline and the section/table that now
holds it; (2) change-marked Section 5 with the new column; (3) change-list line "Added
state-of-the-art baseline X at matched throughput (Table 2)." No unlisted claims sneak in.

## Output format

```text
[Reply type] rebuttal / one-shot revision / n-a (early reject)
[Priority issue] <the objection that decides the outcome>
[Evidence anchor] <table / figure / appendix / new run>
[Revision packet] response / marked diff / change list — status
[Shepherd touchpoint] <what to confirm before building>
[Forbidden content removed] <identity leaks, unlisted new claims>
```
