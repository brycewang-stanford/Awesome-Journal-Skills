---
name: acmmm-review-process
description: Use when reasoning about the ACM MM (ACM Multimedia) review pipeline — thematic-area routing to reviewers and area chairs, the OpenReview double-blind process and its single-blind track exceptions, the optional anonymous rebuttal, the meta-review and decision, and the oral/poster and award tiers, and where an author actually has leverage.
---

# ACM MM Review Process

Use this to build an accurate mental model of how an ACM Multimedia paper is judged, so
strategy targets the points where an author can move the outcome and not the points where they
cannot.

## The pipeline

1. **Submission + thematic area.** The paper enters OpenReview under a chosen thematic area,
   which routes it to a matching reviewer pool and area chair.
2. **Assignment.** Reviewers and an AC are assigned; a mismatched thematic area is where papers
   get reviewers who cannot judge the contribution.
3. **Reviews.** Reviewers assess novelty, cross-modal soundness, evidence (including user
   studies where relevant), and reproducibility.
4. **Rebuttal.** An **optional, anonymous** author response addresses reviews; new external
   links are not allowed.
5. **Discussion + meta-review.** Reviewers and the AC discuss; the AC writes a meta-review and
   recommendation.
6. **Decision + tiers.** Accept/reject, with accepted papers sorted into presentation tiers
   (oral vs. poster) and award consideration.

## Where leverage exists

| Stage | Author leverage | Reality |
|---|---|---|
| Thematic-area choice | High | You pick who reviews you — choose the area that can judge the contribution |
| Submission quality | High | The paper is the main lever; the rebuttal only patches |
| Rebuttal | Medium | Fix factual errors and add small confirmatory results; rarely flips a strong reject |
| Discussion | Low/indirect | You cannot see it; a clean rebuttal gives the AC ammunition |
| Decision/tiers | None directly | Set by AC/PC after discussion |

## Reading a review set

- Separate **factual errors** (a reviewer misread a result) from **judgment** (they find the
  delta small); the first is fixable in rebuttal, the second usually is not.
- Weight the **cross-modal** critiques: "the fusion is not shown to matter" is often the
  decisive line, and an ablation is the answer.
- Note the **AC's** implicit questions in the meta-review; that is who the rebuttal is really
  written for.

## Double-blind and its exceptions

The main track and Brave New Ideas are **double-blind**; the Reproducibility, Open Source
Software, and Dataset tracks are **single-blind** because the artifact carries its identity.
Confidentiality runs both ways: reviewers must not deanonymize authors, and authors must not
try to identify or contact reviewers.

## What the rebuttal cannot do

```text
CAN:   correct misreadings, add a promised small experiment/ablation, clarify scope, concede narrowly
CANNOT: add new external links, change the contribution, add pages, argue the reviewer is unqualified
```

## Reading scores and the meta-review

- A spread of scores (one champion, one detractor) is normal; the **rebuttal targets the
  detractor's concrete objection** and gives the champion and AC something to cite.
- A uniform lukewarm set is harder than a split — there is no champion to convert, so the
  rebuttal must move a shared concern, usually the cross-modal-significance one.
- Weight the **AC's meta-review** most: it is the synthesis the decision rests on, and its
  implicit questions are what your response should answer.

## The dates that constrain strategy

The pipeline has a long middle: reviews and rebuttal cluster in late spring, and the decision
lands in early July (2026: rebuttal around June 4, notification early July). The strategic
consequence is that the **confirmatory experiments a reviewer will ask for should be ready before
reviews arrive** — the rebuttal window is too short to start a new user study or a large ablation
from scratch.

## Confidentiality and conduct

- Treat all reviews and discussion as confidential.
- Do not attempt to deanonymize reviewers or lobby ACs outside the system.
- Report suspected violations through the official channel, not by public posting.

## Output format

```text
[Area routing] well-matched / mismatched (off-topic review risk)
[Review split] factual-fixable: <list> | judgment: <list>
[Decisive critique] <usually the cross-modal/evidence line>
[Rebuttal leverage] high / medium / low
[Next action] <what to fix vs. what to accept>
```
