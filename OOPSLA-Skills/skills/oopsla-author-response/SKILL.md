---
name: oopsla-author-response
description: Use when writing an OOPSLA author response inside the short per-round window — reading reviews through the four-outcome lens (Accept, Minor Revision, Major Revision, Reject), steering borderline papers toward a revision outcome instead of rejection, and committing only to changes deliverable within the round's revision mechanics.
---

# OOPSLA Author Response

Each OOPSLA round gives authors one written response before decisions are
finalized; the 2026 call scheduled it as a four-day Tuesday-to-Friday window
per round (exact 2026 dates 待核实 — read them off the live HotCRP instance).
What makes the OOPSLA response unlike a classic rebuttal is the decision
space: reviewers are not only choosing accept-or-reject, they are choosing
among **Accept, Minor Revision, Major Revision, and Reject** (2026 merged the
old Conditional Accept into Minor Revision). Your response is an argument
about *which bucket the paper's problems belong in*.

## Reframe every objection as a bucket question

| Reviewer concern type | Bucket you argue for | Argument shape |
| --- | --- | --- |
| Factual misreading | Accept | Quote the submitted PDF: section, page, exact sentence |
| Missing experiment, bounded scope | Minor Revision | Show the experiment is runnable in weeks; sketch the protocol |
| Evaluation redesign, new formalism | Major Revision (next round) | Concede scale honestly; state what the revision would contain |
| "Wrong venue" / fit doubts | Accept or MR | Anchor to precedent shapes (see `resources/exemplars/library.md`) |
| Soundness hole in a theorem | Depends — triage first | If repairable, give the repaired statement now, not a promise |

Arguing "Accept" against every concern is the classic failure: it tells the
committee you would not execute a Minor Revision faithfully, which removes
the middle buckets and polarizes the decision toward Reject.

## Composition rules

- **Lead with the decision-relevant paragraph.** State, in five lines, what
  you believe the correct outcome is and the one or two facts that support
  it. Committees skim; the first screen does the work.
- **Answer questions before defending honor.** Direct reviewer questions get
  numbered answers with pointers into the PDF. Tone disputes get silence.
- **Quantify feasibility.** "We will add a user study" is not credible inside
  a Minor Revision; "we will rerun Table 3 with the two requested baselines;
  scripts already exist in the artifact" is.
- **Never introduce results the PDF cannot support.** New numbers in a
  response are unverifiable and reviewers know it; describe *what would be
  measured*, not what you privately measured last night.
- **Reference the revision caps.** Promised additions must fit the 25-page
  revision limit; promising a new 6-page section is self-defeating.

## Triage worksheet

```text
For each review R1..Rn:
  extract: questions (Q), factual errors (E), evidence gaps (G), fit doubts (F)
  map each to bucket argument (table above)
  order: E first (cheap credibility), then Q, then G with feasibility, F last
  budget: total response length per current call rules (待核实 per cycle);
          spend >50% on the two items most likely to move the outcome
```

## If the outcome will be a revision anyway

When reviews clearly point at Major Revision, use the response to *shape the
expectation list*: propose the concrete revision contents yourself. Reviewers
who accept your framing write requirements you have already planned for, and
under the round system the same reviewers meet the resubmission — so what you
promise here is what you will be graded on next round (`oopsla-review-process`).

## Output format

```text
[Predicted bucket] Accept / Minor Revision / Major Revision / Reject
[Target bucket] <the outcome the response argues for>
[Top two levers] <concern + one-line counter, ×2>
[Commitments made] <list, each with feasibility note and page cost>
[Response draft] <numbered, PDF-cited, within length budget>
```
