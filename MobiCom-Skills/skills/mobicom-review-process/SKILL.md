---
name: mobicom-review-process
description: Use when reasoning about where a MobiCom paper sits in the two-round review process — the early-reject cut after round one, the released reviews and rebuttal window after round two, the accept / one-shot revision / reject outcome space, reviewer continuity across a revision, and how the rolling-deadline structure shapes what to do next.
---

# MobiCom Review Process

Understanding MobiCom's review structure changes what you do at each stage. Unlike a
single-verdict venue, MobiCom runs **two rounds per deadline** with an early-reject cut and
a rebuttal, and then keeps a **one-shot revision** channel on top. Knowing which state you
are in — and what each state affords — is the difference between a wasted rolling deadline
and a converging paper.

## The stages and the outcome space

```text
Submission
  -> Round 1 review
       -> EARLY REJECT (reviews returned)         [use them for the next round]
       -> advance to Round 2
  -> Round 2 review -> reviews RELEASED -> REBUTTAL window -> PC decision
       -> ACCEPT
       -> ONE-SHOT REVISION (required-changes list)
       -> REJECT
```

| State | What it means | What you do |
|---|---|---|
| Early reject | did not clear round 1; full reviews returned | mine reviews, decide next round (`mobicom-workflow`) |
| Advanced | reached round 2; reviews will come with a rebuttal window | prepare to respond fast (`mobicom-author-response`) |
| Accept | in the program | artifacts + camera-ready (`mobicom-camera-ready`) |
| One-shot revision | conditional; a list of required changes | treat as a contract; plan the experiments |
| Reject | terminal for this submission | reframe or re-target; do not resubmit unchanged |

## The early reject is data, not just a loss

A round-1 early reject returns reviews well before the round closes. Because MobiCom's rounds
roll, those reviews are the highest-value input to your *next* submission — of the same work,
improved, or of a re-scoped version. Do not treat it as a dead end; treat it as a free
review cycle that most single-deadline venues do not offer.

## The rebuttal window is short and fixed

After round-2 reviews are released, the rebuttal window opens on a clock you do not control.
Its purpose is narrow: correct factual misunderstandings and answer specific reviewer
questions, not to add a new contribution. Plan coauthor availability for it in advance,
because it lands weeks after submission when attention has moved on
(`mobicom-author-response`). The exact length/format of the rebuttal is 待核实 for the current
cycle — read the instructions live.

## The one-shot revision is a commitment

A one-shot (major) revision is not a soft accept. It is a **contract** against a specific
list of required changes, usually re-reviewed by the same reviewers where possible. Before
accepting the plan, cost the experiments it demands in testbed-weeks (`mobicom-workflow`); a
revision that dodges an item on the list, or that re-runs without the requested condition, is
the fastest way to convert a revision into a reject.

## Reviewer continuity shapes strategy

Because the same reviewers tend to carry a paper across the rebuttal and a revision:

- A rebuttal that concedes a real weakness credibly is worth more than one that argues every
  point; the same reviewer reads the revision.
- Promises made in a rebuttal become the revision's checklist — do not promise what you
  cannot measure by the revision deadline.
- Consistency across rebuttal → revision → camera-ready matters; contradicting your own
  earlier response is a memorable red flag.

## Confidentiality and conduct

Reviews and PC discussion are confidential; do not quote reviewers publicly or attempt to
deanonymize them. Reviewer identity is protected the same way author identity is. If you
believe a review breaches policy, the chairs are the channel, not social media.

## Output format

```text
[State] early-reject / advanced / accept / revision / reject
[Reviews] key issues extracted, sorted by severity
[If advanced] rebuttal plan: factual corrections vs question answers
[If revision] required-changes list -> experiment cost in testbed-weeks
[If early reject] which next round + what to fix first
[Continuity] promises that will become the revision checklist
```
