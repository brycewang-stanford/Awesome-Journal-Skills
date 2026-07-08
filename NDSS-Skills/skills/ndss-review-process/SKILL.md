---
name: ndss-review-process
description: Use when interpreting where an NDSS submission stands — the two-round pipeline inside each cycle, the early reject with Round-1 reviews, rebuttal and interactive discussion, the Accept / Minor Revision / Major Revision decision set, and the Ethics Review Board's role.
---

# NDSS Review Process

Each NDSS cycle is a funnel with one public narrowing: Round 1 reads everything and ejects
the bottom; Round 2 argues about the rest. Knowing which stage you are in — and what each
stage can still change — prevents both wasted effort and missed leverage.

## The pipeline (2027 cycle structure, verified 2026-07-08)

```text
submit ──▶ ROUND 1 (breadth read)
              │
              ├─ early reject ──▶ Round-1 reviews released; cycle over for this paper;
              │                   major-overlap resubmission barred within this
              │                   symposium's other cycle
              │
              └─ continue ──▶ ROUND 2 (depth read, more reviewers/discussion)
                                 │  rebuttal + interactive discussion with reviewers
                                 ▼
                    Accept │ Minor Revision │ Major Revision │ Reject
```

Dates for the fall cycle: early notification September 25, rebuttal and discussion
October 8-10, final decision November 4, 2026. The summer cycle followed the same shape
(June 12 / June 24-28 / July 22).

## What each outcome means

| Outcome | Substance | Author obligation |
| --- | --- | --- |
| Accept | Paper in, Seoul slot earned | Camera-ready by Jan 6, 2027; consider artifact evaluation |
| Minor Revision | Accepted contingent on a bounded fix-up judged satisfactory | Execute exactly the requested changes, promptly |
| Major Revision | Promising but incomplete — new experiments, implementations, or proofs required | Resubmit within the stated window against a written list of **revision tasks**; re-review checks task fulfillment; at most one major revision per paper |
| Early reject / Reject | Out for this edition | Fold reviews in; retarget (see `ndss-workflow`) |

The Major Revision list is the closest thing conference review offers to a contract: the
original reviewers wrote the tasks, and the resubmission is judged against them — not
against fresh whims. Treat each task as a deliverable with evidence; treat silence on a
task as a decline you must justify explicitly.

## Round 1: what the breadth read screens for

Round-1 reviewers triage many papers quickly. They are deciding whether further review is
*worth the PC's time*, which concentrates attention on: an intelligible threat model, a
believable evidence type for the claim category, obvious scope or novelty problems, ethics
red flags, and format/anonymity violations. The writing-style skill's first-page contract
is calibrated to exactly this read. An early reject is not an insult; it is a verdict that
the fast read failed — often fixable, but not this edition.

## Round 2: where papers are actually won

Round 2 adds closer reads and a live element: authors see reviews, respond, and then
interact with reviewers during a discussion phase. Decisions crystallize here through
reviewer-to-reviewer argument. Your rebuttal's real audience is the *undecided* reviewer
and the discussion that follows it (tactics in `ndss-author-response`). Reviews that
misread the paper are, at this stage, evidence about the paper: something on the page let
the misreading happen.

## The Ethics Review Board

Any reviewer can flag a submission as ethically fraught; flagged papers get examined by an
ERB drawn from the TPC. It evaluates harm handling against community norms (the Menlo
Report is the CFP's named reference), and its judgment can override technical enthusiasm.
Papers are not penalized *for* doing dangerous-looking research — they are penalized for
doing it without visible reasoning about harm, consent, and disclosure. The ERB reads the
Ethics Considerations section as your testimony; write it before submission as if the
board were guaranteed to convene.

## Confidentiality and conduct

Reviews, scores, and discussion content are confidential; do not quote them publicly, and
do not attempt out-of-band contact with suspected reviewers — chairs are the only channel.
Public preprints are a separate question (check the current CFP's stance) but engaging
with reviewers about the paper anywhere except HotCRP is a bright line at every security
flagship.

## Reading your reviews diagnostically

- All reviewers stumble at the same section → structural problem there, not reviewer error.
- Scores split wide → the paper supports two readings; the rebuttal must collapse the
  wrong one with pointable evidence.
- "Threat model unrealistic" → either defend the model's real-world instantiation with
  named deployments, or the topic-selection test was failed months ago.
- Every weakness listed is fixable-in-weeks → a Major Revision may be within reach; make
  the fixes look *scoped* in your response.

## Output format

```text
[Stage] round-1 pending / round-2 / decided: <outcome>
[Cycle dates] next milestone + days remaining
[Review diagnosis] convergent objections, split points, misreadings
[ERB exposure] flagged risk areas + where the paper answers them
[Next action] rebuttal / revision-task plan / retarget, with owner
```
