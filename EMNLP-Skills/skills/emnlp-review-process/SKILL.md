---
name: emnlp-review-process
description: Use when explaining or strategizing around EMNLP's two-stage pipeline — ACL Rolling Review scoring with soundness, excitement, and overall recommendation, area-chair meta-reviews, the commitment step, and conference-side decisions by Senior Area Chairs into Main, Findings, or rejection — including resubmission dynamics and ethics flags.
---

# EMNLP Review Process

Use this to reason about what happens to the paper after upload. EMNLP outsources
reviewing to ACL Rolling Review and keeps only the decision: understanding which body
controls which lever is most of review-stage strategy. Mechanics below are the May 2026
cycle configuration (checked 2026-07-08); ARR revises its own rules midyear, so reconfirm
on `aclrollingreview.org` before relying on any of it.

## Pipeline anatomy

```text
ARR side (owns reviewing)                Conference side (owns deciding)
─────────────────────────                ───────────────────────────────
submit PDF + checklist (May 25)
  → AC assigned, reviewers assigned
  → 3(ish) reviews, scored              commit reviewed paper (by Aug 2)
  → author response + discussion          → SACs rank committed papers
    (Jul 7-13)                             → PCs set boundaries
  → AC meta-review (Jul 30)               → Main / Findings / reject (Aug 20)
  → OR: skip commitment, revise,
       resubmit to a later cycle
```

Nothing on the left is a decision; nothing on the right adds new reviews. A paper is
therefore argued twice — once in front of reviewers, once (silently, via the record) in
front of SACs — and the response you write in July serves both audiences.

## What the scores mean strategically

Since February 2025, ARR reviewers file three scores plus text:

| Score | What it measures | Who consumes it hardest |
|---|---|---|
| Soundness | Is the evidence valid for the claims as scoped? | The Findings bar — sound work is publishable |
| Excitement | Would the community care? | The Main-vs-Findings boundary |
| Overall recommendation | The reviewer's synthesis | SAC triage ordering |

The operational asymmetry: **soundness is repairable in a response; excitement rarely
is.** A soundness objection usually names a missing control, test, or scope edit that
text can address. Low excitement with high soundness signals the likely outcome is
Findings, and the levers are framing and venue choice, not rebuttal volume.

## The meta-review is the product

The AC's meta-review is what SACs actually read at scale. Everything an author does in
the review phase should be optimized to make the meta-review say: *the reviewers'
substantive concerns were addressed or shown mistaken.* Practical consequences:

- Answer the concern the AC is likely to quote, not the reviewer's most annoying
  sentence.
- If reviewers disagree with each other, say so explicitly and give the AC the
  resolution — ACs synthesize, and unresolved contradictions default to caution.
- The discussion window (July 7-13 in 2026) is short and reviewers may engage once;
  front-load your strongest material rather than staging it.

## Resubmission dynamics

Skipping commitment and revising for a later cycle is a first-class outcome, with sharp
edges:

- Resubmissions return to the same AC and reviewers where possible. New reviewers form
  an independent opinion before seeing the old reviews — so a genuinely improved paper
  gets a fresh read, but a cosmetically edited one faces reviewers holding the diff.
- ARR asks for a revision note explaining what changed; write it as an audit trail
  keyed to the previous reviews.
- Cycle arithmetic matters: each ARR cycle aligns to specific conferences. Revising out
  of the May cycle meant targeting whatever the next cycle fed, not EMNLP 2026.

## Ethics and integrity lanes

Reviewers can flag submissions for ethics review, which runs parallel to technical
review and can alter or override outcomes. Separately, the 2026 conference call names
thinly sliced submissions, hallucinated citations, and entirely AI-generated papers as
integrity violations. Neither lane is appealable through a better rebuttal — the defense
is a submission that never trips them: documented data provenance, honest checklist
answers, and verified references.

## Scale effects you should price in

The May 2026 cycle carried 17,087 submissions across a pool of roughly 10,600 reviewers
and 1,400 area chairs. Scale has predictable consequences for any single paper:

- Reviewer expertise is matched statistically, not curated; expect one close expert,
  one adjacent reader, and occasionally one genuine mismatch. Write the paper so the
  adjacent reader can follow the argument — they are the median vote.
- Late, short, or template-flavored reviews happen; the remedy is the discussion
  window and, where a review is substantively deficient, a calm note to the AC — not
  a public quarrel in the thread.
- Meta-review quality varies with AC load. A response that pre-writes the synthesis
  (short summary block, numbered resolutions) is partly self-defense against a rushed
  meta-review.
- Score inflation and compression are real at scale: the difference between "accept"
  and "Findings" often lives in the meta-review's confidence language rather than in
  the numeric scores, which is one more reason the response should target prose, not
  arithmetic.

## Reading a review packet in ten minutes

1. Extract the three scores per reviewer; plot soundness against excitement mentally.
2. Classify each substantive point: factual error by reviewer / missing-but-runnable
   evidence / missing-and-unrunnable evidence / taste.
3. Anything in class two becomes response content; class three drives the
   commit-vs-revise decision; class four gets one polite paragraph, maximum.
4. Draft the sentence you want the meta-review to contain, then write the response
   backward from it.

## Output format

```text
[Stage] under review / response window / meta-review out / committed / decided
[Score read] soundness <low/mid/high> × excitement <low/mid/high> per reviewer
[Likely trajectory] Main / Findings / revise-resubmit / withdraw
[Meta-review target sentence] <what the AC should conclude>
[Ethics or integrity exposure] none / flagged / at-risk items
```
