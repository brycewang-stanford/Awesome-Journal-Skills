---
name: oopsla-review-process
description: Use when explaining or strategizing around OOPSLA's two-round review machinery — double-anonymous multi-stage reviewing, the four outcomes (Accept, Minor Revision, Major Revision, Reject), reviewer continuity across rounds, round-hopping a Major Revision, and how acceptance flows into a PACMPL issue and the SPLASH talk.
---

# OOPSLA Review Process

OOPSLA reviews like a journal wearing a conference's clock. Two submission
rounds per volume (2026: October 10, 2025 and March 17, 2026), a Review
Committee whose chairs act as PACMPL Associate Editors (2026: Anders Møller
and Işıl Dillig), multi-stage double-anonymous reviewing, an author-response
window per round, and a four-way decision instead of a binary one. Round 1 of
2026 accepted 75 of 227 submissions into PACMPL Vol. 10, Issue OOPSLA1 —
roughly a third, but treat any single round's rate as one data point, not a
planning constant.

## The four outcomes and what each really means

| Outcome | Mechanics | Author's correct read |
| --- | --- | --- |
| Accept | Into the round's PACMPL issue after camera-ready | Deliver commitments; start the artifact |
| Minor Revision | Fixable concerns resolved **within the same round's** process (2026 folded the old Conditional Accept in here) | A near-accept with homework and a checker |
| Major Revision | Invitation to resubmit to the **next round** against an explicit expectations list, with reviewer continuity to the extent possible | The venue wants the paper — at its price |
| Reject | Out of this volume's pipeline | Diagnose before re-entering the SIGPLAN family |

The revision categories change meaningfully between volumes (the 2025→2026
merge is the proof), so restate the current definitions from the live track
page before advising anyone.

## Round-hopping: the mechanic to teach explicitly

A Major Revision is not a rejection with kind words — it is a reserved slot
with named examiners. The hop works like this:

```text
R1 submission (Oct) --Major Revision--> resubmit in R2 (Mar), same volume
R2 submission (Mar) --Major Revision--> resubmit in next volume's R1 (~Oct)
Either round --Accept/Minor Revision--> that round's issue (OOPSLA1 / OOPSLA2)
```

Consequences worth spelling out:

- An R1 Major Revision handled well still publishes *in the same year's
  volume* (OOPSLA2) — often faster than a fresh submission elsewhere.
- An R2 Major Revision crosses volumes, so the calendar cost is ~7 months;
  factor that into round choice at submission time (`oopsla-workflow`).
- Reviewer continuity cuts both ways: unresolved expectations are checked by
  the people who wrote them. Answer the list item by item in a change log;
  do not silently re-litigate demands you dislike — argue them explicitly or
  satisfy them.

## Inside a round

1. **Triage** — format, anonymity, scope; the firm-deadline and 23-page rules
   bite here (`oopsla-submission`).
2. **Multi-stage reviewing** — the OOPSLA1 2026 front matter describes
   multiple stages of double-anonymous review; expect additional reviews or
   expert consultations on borderline papers between stages.
3. **Author response** — the four-day window where bucket arguments happen
   (`oopsla-author-response`).
4. **Committee resolution** — outcomes assigned; expectation lists drafted
   for revision buckets.
5. **After acceptance** — camera-ready into the PACMPL issue
   (`oopsla-camera-ready`), artifact evaluation with badges
   (`oopsla-artifact-evaluation`), talk at SPLASH.

## Reading a review packet like a strategist

- Count, per review, the demands that are *bounded* (rerun, clarify, add
  baseline) versus *unbounded* (rethink the design, new study population).
  Mostly-bounded packets are Minor-Revision-shaped; argue accordingly.
- A single devastated reviewer among positive ones is a discussion problem,
  not a paper problem — your response should arm the positive reviewers with
  the citations and pointers they need to carry the argument.
- Fit complaints at OOPSLA are weaker than at narrower venues (the published
  scope spans formalisms to empirical studies); rebut them with precedent
  shapes, not indignation.

## Output format

```text
[Stage] triage / in review / response window / decision / revision pending
[Packet read] bounded vs unbounded demands per review
[Likely outcome] one of four + confidence
[Round plan] same-round path or hop target with dates from live pages
[Action] the single highest-leverage next move
```
