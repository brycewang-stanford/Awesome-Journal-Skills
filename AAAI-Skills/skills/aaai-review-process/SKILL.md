---
name: aaai-review-process
description: Use when explaining or planning around AAAI's two-phase review process, Phase 1 rejection risk, Phase 2 additional reviews, AI-assisted review pilot, author feedback, SPC/AC discussion, and final decisions.
---

# AAAI Review Process

Use this to plan around AAAI review rather than treating it as a generic OpenReview rebuttal.
Reopen the current review-process page and author FAQ before advising on timing or strategy.

## Process model

- AAAI main technical track uses double-blind reviewing.
- AAAI-26 used a two-phase review process. Phase 1 had human reviews and a non-decisional
  AI-generated review. Papers with sufficiently negative reviews could be rejected before author
  feedback.
- Papers continuing to Phase 2 received additional reviews and one author feedback phase.
- Final decisions were made through reviewer discussion and senior program committee oversight,
  not by the AI review.
- Author feedback is short and constrained; it is mainly for correcting misunderstandings, not
  replacing the paper.

## Author strategy

- Reduce Phase 1 reject risk before submission by making contribution, evidence, and checklist
  compliance obvious.
- When reviews arrive, distinguish human-review claims, AI-review errors, and AC/SPC decision
  questions.
- Use rebuttal to resolve the highest-impact factual issue under the character limit.
- Do not attack the AI review. Correct it when it contains consequential false statements.
- Avoid new experiments in rebuttal; use submitted evidence and camera-ready promises sparingly.

## Stage-by-stage decision map

AAAI's pipeline differs from a single-round OpenReview venue, so plan actions per stage rather than
treating every signal as a rebuttal opportunity.

| Stage | What is happening | Author leverage |
| --- | --- | --- |
| Pre-submission | Phase-1 bar is set by clarity and checklist | maximal: fix the paper itself |
| Phase 1 | human reviews plus advisory AI review | none yet; summary reject possible |
| Phase 2 | additional reviews, one feedback round | one short response, no new results |
| Discussion | reviewers and SPC/AC weigh feedback | indirect: a clean correction can swing it |
| Decision | SPC/AC oversight, not the AI review | archive everything for appeal or journal |

## Why papers die in Phase 1

Because the reviewer pool is large and submission volume is high, clearly-below-bar papers are cut
early to protect later effort. Common triggers: an unreadable first page, a contribution a
non-specialist cannot place, a checklist that contradicts the paper, or evidence too thin to trust.
None of these can be repaired after the Phase-1 cut, so they must be eliminated before submission.

## Worked vignette

An NLP paper with strong results buries its contribution under three pages of setup. A Phase-1
reviewer from a planning background cannot find the AI claim and scores it a reject; the paper never
reaches feedback. The fix belongs entirely pre-submission: a first-page contribution statement and a
checklist that matches the experiments, so the broad-AI reviewer can place and trust it fast.

## Output format

```text
[Stage] pre-submission / Phase 1 / Phase 2 / rebuttal / discussion / decision
[Decision risk] summary reject / borderline / likely accept / ethics-policy risk
[Best action] revise before submission / rebut / clarify evidence / escalate
[AI-review handling] ignore / correct / cite submitted evidence
[Rationale] <why this fits AAAI process>
```

