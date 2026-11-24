---
name: sigcomm-author-response
description: Use when deciding how an ACM SIGCOMM author can respond to reviewers — in SIGCOMM 2027 there is no rebuttal and no one-shot revision, so the replies are the submission itself, the CCR-acceptance choice, and the shepherd's camera-ready revision; also use the retained SIGCOMM 2026-style rebuttal and one-shot-revision playbook if a later edition restores them.
---

# SIGCOMM Author Response

**SIGCOMM 2027 has no rebuttals and no one-shot revisions** (CFP, re-verified 2026-11-24).
Reviewers discuss each paper "collaboratively" from the start and return **one relatively
short consensus review** after the decision. The author's voice therefore lives in three
places, and this skill covers each; the rebuttal and one-shot sections further down are the
SIGCOMM 2026 mechanics, kept for editions that restore them. Reopen the current CFP before
drafting anything.

## First, know which reply you are writing

| Signal in the letter | You are in | The move |
|---|---|---|
| Nothing yet — paper still being written | Pre-submission (2027) | Pre-empt the objections in the paper: there is no later chance to answer them |
| "Accepted into the SIGCOMM conference" plus a shepherd | Accept (2027) | Map the consensus review to edits and agree them with the shepherd |
| "Accepted into CCR" | CCR offer (2027) | Decide: take the CCR research article, or decline and resubmit elsewhere |
| Rejected from both | Reject (2027) | No reply reopens it; use the consensus review to redirect the work |
| Reviews plus an invitation to respond, no verdict | Rebuttal (2026 model) | Answer the decision-critical objection concisely |
| A merits summary and a list of required changes | One-shot revision (2026 model) | Treat the list as a binding contract; resubmit with a packet |

## SIGCOMM 2027: answer the reviewers before they ask

With no rebuttal, the paper must carry its own answers:

- Put the decision-critical evidence (realistic evaluation, the strongest baseline, the tail
  numbers) in the **12-page body**; reviewers need not read appendices and body claims cannot
  depend on appendix experiments.
- Write for the **general-accessibility** test: a networking generalist must grasp why the
  problem matters and the gist of the approach, or the PC will reject.
- Anticipate the obvious "does it generalize?" and "why not X?" questions with a sentence and a
  pointer each — a consensus review will not ask twice.

## SIGCOMM 2027: the CCR offer

A paper rejected from the conference may instead be **accepted into CCR** as a regular research
article. Authors may decline and resubmit elsewhere. Decide on the merits of the consensus
review: if it names fixable gaps that another venue would weigh differently, declining can be
right; if the work is complete and the gap is fit or breadth, a CCR article is a real
publication. Record the decision and its reason with the coauthors before replying.

## SIGCOMM 2027: shepherd-led revision of accepted papers

Every conference paper gets a **shepherd**. Map each point in the consensus review to a
concrete edit, agree the map with the shepherd early through HotCRP, and expect the shepherd to
judge whether each appendix is necessary. Accepted papers also owe a **video** and an
in-person presenter at a small-scale discussion session (details 待核实).

## Writing the rebuttal (SIGCOMM 2026 model — not offered in 2027)

- Answer the concern that decides the paper first: evaluation realism, a missing baseline, a
  correctness question, or a generalization doubt. Style complaints wait.
- Anchor every answer in evidence already in the submission — a table, a figure, an appendix
  measurement — rather than promising new experiments the reviewers cannot see.
- Stay anonymous: no institution, deployment name, or private link that breaks double-blind.
- Concede cleanly what cannot be fixed in the window, and scope a camera-ready wording change
  instead of overclaiming a result you cannot produce now.
- One precise, decision-focused reply per reviewer beats an exhaustive point-by-point that
  buries the objection that actually matters to the discussion.

## Executing the one-shot revision (SIGCOMM 2026 model — not offered in 2027)

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
[Reply type] pre-submission pre-emption / CCR decision / shepherd revision / n-a (reject) — or, where an edition restores them, rebuttal / one-shot revision
[Priority issue] <the objection that decides the outcome>
[Evidence anchor] <table / figure / appendix / new run>
[Revision packet] response / marked diff / change list — status
[Shepherd touchpoint] <what to confirm before building>
[CCR decision] accept / decline (+ reason) / n-a
[Forbidden content removed] <identity leaks, unlisted new claims>
```
