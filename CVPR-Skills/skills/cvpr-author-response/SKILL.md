---
name: cvpr-author-response
description: Use when planning or drafting the CVPR one-page rebuttal after reviews are released, covering the official rebuttal template, the ban on new contributions and external links, triaging multiple reviews at 16k-submission scale, choosing which numbers fit in one page, and writing for the AC who reads the discussion.
---

# CVPR Author Response

Use this when CVPR reviews land. In the 2026 cycle, reviews reached authors on
January 22 and the rebuttal closed January 29, with reviewer–AC discussion running
January 30 – February 5 and decisions on February 20. One week, one page — the format
is the strategy.

## What the one page legally is

The rebuttal is an **optional, single-page PDF** built on the `rebuttal.tex` template in
the official author kit. Two rules from the Author Guidelines carry teeth:

- Responses **longer than one page are simply not read**, and that includes pages that
  technically fit because margins or fonts were squeezed — altered formatting counts as
  over-length.
- The rebuttal exists to **correct factual errors and supply requested information**. It
  is explicitly *not* for new contributions or unrequested new experiments, reviewers are
  told not to demand significant new experiments, and it must stay anonymous with **no
  links to external material** (no anonymous repos, no video URLs, no project pages).

That last clause surprises people arriving from venues with revision uploads: at CVPR
you cannot attach anything. If a number matters, it goes in the page as a sentence or a
five-row table.

## Triage before typing

With ~16,000 papers in the 2026 pool, your reviewers wrote many reviews and your AC is
tracking dozens of papers. The rebuttal's real reader is the AC during the discussion
window. Triage accordingly:

| Review signal | Rebuttal move | Budget |
|---|---|---|
| Factual error ("no ablation on X" when Table 4 has it) | Quote the reviewer, cite the exact table/line, one sentence | 2–3 lines each |
| Misread contribution / scope | Restate the claim in one crisp sentence, point to where the paper says it | 4–6 lines |
| Requested clarification (protocol, metric, split) | Answer directly; give the number | 3–5 lines |
| Requested small experiment | Run it if it fits the week; report as a mini-table | 6–10 lines |
| Demand for a full new benchmark or method variant | Decline politely; explain why out of scope for a rebuttal | 2–3 lines |
| Subjective "not novel enough" | Delta-list against the 2–3 closest citations, no adjectives | 4–6 lines |

Answer every reviewer, but not every sentence of every reviewer. Ignoring one review
entirely reads as concession in the discussion phase.

## A page layout that ACs can skim

```latex
% rebuttal.tex skeleton — headings are navigation for the AC
\section*{Shared concerns (R1, R3): fairness of the baseline comparison}
% one paragraph + mini-table with matched-backbone numbers
\section*{R1: reported speed}
% cite Sec. 4.2 line refs; give ms/frame on the named GPU from the CRF hardware
\section*{R2: missing citation [Foo 2025]}
% concede, state the delta in one sentence, promise camera-ready citation
\section*{R3: qualitative failures}
% point to supplement Sec. C; summarize the two failure modes in text
```

Group shared objections once instead of three times; name reviewers in headings; lead
with the concern you can kill with a fact, because the first inches of the page set the
AC's prior about who is being careful.

## Tone calibration

- Quote reviewers verbatim before answering; paraphrases invite "that's not what I said."
- Concede real errors fast and specifically — a clean concession buys credibility for
  the contested points.
- No sarcasm, no appeals to arXiv fame, no "as any expert knows." The discussion phase
  happens without you in the room; give allies quotable sentences.
- Numbers over adjectives. "mIoU 54.1 → 55.8 with matched training schedule" survives
  discussion; "significantly better" does not.

## A paragraph, before and after

Draft rebuttal prose tends to argue; shipping rebuttal prose demonstrates. Compare:

> **Before:** "We respectfully disagree with R2's claim that our comparison is unfair.
> As explained in the paper, our method uses standard settings, and it is common
> practice in the field to compare this way. We believe the improvement is clearly
> significant."

> **After:** "R2: 'the baseline uses a weaker backbone.' Both rows of Table 2 use
> ResNet-50 with the schedule from [24] (Sec. 4.1, L412–418). Under R2's suggested
> ViT-B setting, the gap is +1.9 AP (mini-table below), consistent with the paper's
> +2.1."

The rewrite quotes the objection, cites the paper by line, gives a number, and never
characterizes its own results. Every paragraph on the page should survive the same
transformation: objection verbatim → paper location → number.

## First-hours protocol when reviews land

1. Read all reviews once without responding, then close the laptop for a few hours;
   the first-read emotional register writes bad rebuttals.
2. Build a flat list of every distinct objection with reviewer IDs and a
   fixability tag: factual / clarification / small-run / out-of-scope.
3. Check scores against the venue's realities (25% acceptance) before deciding how
   much of the week the paper deserves versus the resubmission draft.
4. Assign the roles from `cvpr-workflow` and set the internal freeze 24 hours before
   the OpenReview deadline.

## What you cannot fix in January

The rebuttal cannot rescue a paper whose evidence is missing, and reviewers are
instructed not to expect new experiments. If every review converges on the same absent
comparison, the plan is the next cycle (or ICCV/ECCV), not one page of protest. Spend
the week where movement is possible: factual corrections, misreadings, and small
requested numbers.

## Reverify each cycle

- Rebuttal existence, length cap, and template — chairs have restructured response
  formats at CVF venues before.
- Exact window dates and whether reviewer–author discussion (beyond one PDF) exists.
- Whether revision uploads or supplement updates are permitted (they were not in 2026).

## Output format

```text
[Rebuttal plan] file / skip (reason)
[Shared concerns] <grouped items with reviewer IDs>
[Factual corrections] <claim → paper location>
[Numbers to include] <experiment → mini-table budget>
[Declined requests] <item → one-line rationale>
[Page budget] <lines allocated per section, total ≤ 1 page>
```
