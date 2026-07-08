---
name: cvpr-review-process
description: Use when reasoning about how CVPR review actually works at 16,000-submission scale, covering the OpenReview pipeline and timeline, reviewer-duty enforcement and desk rejects, the reviewer LLM ban, AC and discussion dynamics, oral/highlight/poster decision tiers, and calibrating expectations to a ~25% acceptance rate.
---

# CVPR Review Process

Use this to model what happens to a CVPR paper between upload and decision, and where
author leverage exists. Every mechanism below is the 2026 cycle as verified 2026-07-08;
scale numbers come from official CVPR program announcements.

## The machine, by the numbers

The 2026 cycle put 16,092 submissions through full review (withdrawals and desk rejects
excluded from that count) and accepted 4,090 — 25.42%. Doing that required roughly
doubling the reviewer pool to 25,149 reviewers across 97 countries, coordinated by 909
area chairs. Two consequences follow for authors:

- Your reviewers are statistically likely to include first-time CVPR reviewers (the
  pool doubled in one year; official training material exists for a reason). Write for
  a competent generalist in vision, not the five people in your subfield.
- No individual paper gets much AC deliberation time by default. Papers that make the
  AC's job easy — clear claims, clean rebuttal, consistent reviews — get the benefit of
  scarce attention.

## Timeline anatomy (2026 cycle)

| Phase | 2026 dates | What authors can do |
|---|---|---|
| Profile/abstract registration | Nov 6, 2025 | Fix profiles, finalize author list |
| Paper + CRF deadline | Nov 13, 2025 | Submit; after this, nothing |
| Supplement deadline | Nov 20, 2025 | Upload depth material |
| Reviewing | Dec – Jan 12, 2026 | Serve your own reviewer duties well |
| Reviews released | Jan 22, 2026 | Read cold, then triage |
| Rebuttal | → Jan 29, 2026 | One page (see `cvpr-author-response`) |
| Reviewer–AC discussion | Jan 30 – Feb 5, 2026 | Nothing — your rebuttal speaks |
| Decisions | Feb 20, 2026 | Plan camera-ready or resubmission |

## Enforcement culture: the distinctive part

CVPR's response to scale is to make authorship and reviewing one social contract, with
teeth that surprised people in recent cycles:

- **Enrollment**: submitting authors are expected to review and are added to the pool
  unless exempted; complete OpenReview profiles are mandatory for everyone.
- **The nuclear clause**: papers authored by a reviewer who fails to deliver assigned
  reviews on time, or delivers highly irresponsible ones, can be desk-rejected — *all*
  of that person's submissions — at PC discretion. A coauthor's negligence in January
  can kill your November submission.
- **Reviewer LLM ban**: reviews and meta-reviews may not be written by LLMs (local or
  API), and sharing substantial paper content with an LLM is prohibited; grammar
  checkers and background research are the carve-outs. As an author, this means a
  suspiciously LLM-flavored review is reportable to the AC, not just annoying.

```text
# Confidential-channel escalation, in order
1. Rebuttal PDF        → factual corrections all reviewers see
2. Confidential comment to AC (where the form allows)
   → reviewer misconduct: LLM-written review, review of the wrong paper,
     demonstrably unread paper. Cite evidence, stay unemotional.
3. Never              → contacting reviewers or ACs outside OpenReview; that
                        is an integrity violation on YOUR side.
```

## What a CVPR review contains

The review form's exact fields shift by cycle (待核实 each year), but the durable
skeleton a CVPR review argues through is: summary of the paper in the reviewer's own
words (misreadings here predict everything downstream), claimed strengths, weaknesses
with the score-driving one usually listed first, and a recommendation with confidence.
Read your reviews against that skeleton: a wrong summary is rebuttal priority one,
because every weakness derived from it inherits the error.

## Decision tiers

Acceptance is not binary. The 2026 program sorted acceptances into poster, **highlight**
(program-flagged posters, 578 papers per program trackers), and **oral** (141 papers in
four parallel tracks), plus 74 award candidates — treat those tier counts as reported,
and the tiering itself as the durable pattern. Tier decisions ride on review scores plus
AC/SAC advocacy, which is one more reason the rebuttal's real audience is the AC.

## After a rejection: mining reviews for signal

Roughly three of four reviewed papers exit here, so treat rejection processing as part
of the process, not an aftermath:

- Separate objections into **evidence gaps** (missing baseline, unmatched backbone —
  fix before any resubmission; CVF reviewer pools overlap and repeat objections
  compound), **communication failures** (a reviewer missed something the paper does
  say — a writing-style problem, see `cvpr-writing-style`), and **taste** (novelty
  judgments that a different draw of three reviewers may not share).
- Score patterns carry information: uniform lukewarm reviews usually mean a framing
  problem; one champion plus one detractor means the discussion phase decided it, and
  the rebuttal is where to look for what failed.
- Do not shop an unchanged paper to the next deadline. The overlap between CVPR,
  ICCV, and ECCV reviewer pools makes "same paper, new lottery ticket" a strategy
  with memory.

## Calibration for authors

- A ~25% rate at 16k submissions means ~12,000 rejections of mostly competent papers.
  Rejection is the modal outcome for good work; plan the ICCV/ECCV/next-CVPR path at
  submission time, not in grief.
- Borderline papers live or die in discussion week. What moves them: a rebuttal that
  kills a factual objection, and one reviewer willing to champion. What doesn't:
  eloquence about importance.
- Reviews disagreeing 2-vs-1 is normal at this scale; the AC weighs arguments, not
  averages, more than authors assume.

## Reverify each cycle

- Whether decisions remain single-round (no conditional-accept revision cycle existed
  in 2026).
- Reviewer-duty enforcement wording, LLM-policy scope, and review-form structure.
- Tier definitions (highlight/oral percentages shift with program capacity).

## Output format

```text
[Stage] pre-submission / in-review / rebuttal / discussion / decided
[Process risks] duty-compliance · profile validity · policy exposure
[Review read] per-reviewer: score-driver + fixability in one line
[AC theory] what the meta-reviewer needs in order to advocate
[Next actions] <dated, owner-assigned>
```
