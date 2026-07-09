---
name: iros-author-response
description: Use when responding to IROS reviews given the traditional no-rebuttal model — pre-answering objections in the paper and video before submission, addressing the meta-review through camera-ready edits, writing RA-L response letters for the journal pathway, and drafting reject-to-ICRA/CoRL/RA-L resubmission memos under double-anonymous rules.
---

# IROS Author Response

Use this after IROS reviews arrive — and, crucially, *before* submission too, because IROS traditionally
offers **no rebuttal**. The reviews come with the decision, so the "response" is spread across three real
channels: pre-answering in the paper, editing the camera-ready, and, if rejected or on the journal route,
a response letter or resubmission memo. Confirm the current cycle's policy before assuming a rebuttal
window does or does not exist.

## Channel 1: pre-answer before you submit

The most effective IROS author response is written before anyone reviews the paper. Anticipate the
standard objections and disarm them in the body and the video:

- "Did it really work?" → shown, uncut trials plus a labeled failure in the video.
- "Is it reliable or cherry-picked?" → trial counts, resets, and a failure taxonomy in the body.
- "Does sim imply real?" → a stated sim-to-real gap, not an implied zero.
- "Is the baseline fair?" → same-platform baseline with comparable tuning.

## Channel 2: the camera-ready revision

When the decision is accept (often with requested changes), the meta-review is your instruction set.
Integrate its asks without inflating the contribution beyond what was reviewed.

| Meta-review ask | Camera-ready move | Trap to avoid |
|---|---|---|
| "Report failure cases" | Add the failure taxonomy table you logged | Do not add new claims the reviewers never saw |
| "Clarify the compute budget" | State measured rate and power on the robot | Do not quietly change the reported system |
| "Compare to system X" | Add the same-platform comparison if you have it | Do not fabricate a comparison you did not run |
| "Fix anonymized links" | Replace with the public, licensed release | Do not leave "code coming soon" |

## Channel 3: RA-L response letters and resubmission memos

- If your work is on the **RA-L journal pathway**, that review *does* have response letters: answer each
  point, quote the change, and cite the revised line — a very different discipline from the no-rebuttal
  conference.
- If the IROS paper is **rejected**, write a short internal resubmission memo: which objections were
  evidence gaps (fixable with a run), which were framing, and which venue (next ICRA, CoRL, or RA-L) the
  revised paper best fits.

## Micro-example: turning a rejection into a plan

Reviewers rejected a manipulation paper for "insufficient real-robot evidence." The memo:

1. Name the gap precisely — 20 trials on 3 objects is too thin for the reliability claim.
2. Scope the fix — 120 trials across 15 objects with a logged failure taxonomy.
3. Choose the target — RA-L (for revision cycles) or the next ICRA (for the spring deadline).
4. Decide the video re-cut — add a labeled failure to pre-answer the same objection.

```text
Response draft skeleton (camera-ready or RA-L letter):
  [Point] <reviewer/meta-review concern>
  [Change] <exact edit or added table/figure>
  [Location] <section / table / line in the revised paper>
  [Not added] <new claims deliberately withheld to stay within review scope>
```

## Output format

```text
[Channel] pre-submission / camera-ready / RA-L letter / resubmission memo
[Priority concern] <the objection that most threatens acceptance>
[Response] <IROS-appropriate, scoped, anonymity-safe>
[Evidence anchor] <paper/video/log item>
[Forbidden] <new unsupported claims / identity leaks / fabricated comparison>
```
