---
name: wacv-review-process
description: Use when reasoning about how WACV decides a paper, covering the two-round model, the Round 1 Accept / Revise-and-Resubmit / Reject recommendations, the optional Round 1 rebuttal, the no-rebuttal Round 2, area-chair consolidation, double-blind confidentiality, and where author leverage actually exists across the two rounds.
---

# WACV Review Process

Use this to model the machine WACV runs your paper through, so effort lands where it moves
a decision. WACV's pipeline is unlike its CVF siblings: it is a **two-round, journal-style
process** with an explicit revision path. Facts below are the WACV 2026/2027 cycles as read
on 2026-07-09; reopen the current Reviewer Guidelines and Dates page before relying on a
date or rule.

## The two-round pipeline

Each Round 1 submission is seen by **at least three reviewers**; the area chair consolidates
the reviews and issues one of three recommendations:

| R1 outcome | What it means | What happens next |
|---|---|---|
| **Accept** | The paper clears the bar as submitted | Proceeds to camera-ready |
| **Revise and Resubmit** | Not accepted, but plausibly fixable within the cycle | Invited into **Round 2** with reviewer-requested revisions |
| **Reject** | Concerns too large for a short-timeframe revision | Out for this cycle |

Round 2 then reviews **two populations together**: the revised R1 (Revise-and-Resubmit)
papers and brand-new Round 2 submissions. Round 2 recommendations are **Accept or Reject**
only. The scale of the middle band is the headline fact: in WACV 2025's Round 1, of 1381
submissions, roughly 12% were accepted outright, ~37% rejected, and **~51% invited to
revise** — most papers live or die in the revision lap, not the first review.

## Where the rebuttal fits (and where it doesn't)

- **Round 1 has an optional one-page rebuttal.** After R1 reviews arrive, authors may file
  a single-page PDF (rebuttal template in the author kit) to correct factual errors and
  answer the reviewers before the recommendation is set.
- **Round 2 has no rebuttal.** For revised R1 papers, your "response" is the *revision plus
  the change summary*, not a rebuttal PDF; for new R2 submissions, there is simply no
  author-response step. Plan accordingly — an R2 paper cannot argue itself out of a weak
  first submission after the fact.

## Confidentiality and conduct

Reviewing is double-blind: authors do not learn reviewer or AC identities, and reviewers
should not be able to infer authorship beyond reasonable doubt. Review content is
confidential; do not seek reviewer identities, post reviews, or contact chairs to
circumvent the process. Treat the AC as the reader who must reconcile three reviews into
one recommendation — clarity aimed at the AC pays off more than point-scoring a single
reviewer.

## Author leverage, by stage

```text
R1 reviews land      → optional one-page rebuttal: fix factual errors, answer the top blocker
R1 = Accept          → move to camera-ready (see wacv-camera-ready)
R1 = Revise&Resubmit → the real work: make the reviewer-requested changes, write the change
                       summary, keep paper and artifact in sync for Round 2
R1 = Reject          → harvest the reviews; re-target (see wacv-topic-selection) or rebuild
R2 (revised paper)   → no rebuttal; the revision *is* the argument
R2 = Accept/Reject   → terminal for the cycle
```

The highest-leverage moment at WACV is **not** the rebuttal — it is executing a clean
Revise-and-Resubmit. A paper that reads its R1 reviews as a concrete revision spec, makes
exactly those changes, and documents them, converts far more often than one that argues.

## Reading a recommendation honestly

- A **Revise and Resubmit** is an invitation, not a soft reject: it means the reviewers
  believe the gap is closable this cycle. Treat every requested change as load-bearing.
- An **Accept** at R1 is rare and clean — do not reopen the paper beyond camera-ready fixes.
- A **Reject** with substantive reviews is still valuable input for a sibling venue or the
  next cycle; separate "reviewers missed it" (rare) from "the paper did not answer the
  obvious question" (common).

## Reverify each cycle

- Whether the two-round model, the three R1 recommendations, and the R2 Accept/Reject set
  still hold.
- The Round 1 rebuttal format and length, and the confirmation that Round 2 has none.
- Reviewer count per paper and any reviewer-side LLM or conduct rules.
- The exact R1/R2 review and decision dates (reported for 2027 — reconfirm).

## Output format

```text
[Stage] R1 reviews / R1 decision / R2 review / R2 decision
[R1 outcome] Accept / Revise&Resubmit / Reject
[Highest-leverage action now] <rebuttal fix | revision spec | re-target>
[If R&R] reviewer-requested changes enumerated: yes/no
[AC-facing clarity] <the one thing the AC must be able to conclude>
```
