---
name: colm-author-response
description: Use when writing a COLM rebuttal in the OpenReview discussion phase — triaging reviews released in late May, running cache-based follow-up experiments inside the roughly two-and-a-half-week window, answering contamination and baseline-fairness objections with evidence, and writing for the area chair who decides in July.
---

# COLM Author Response

In 2026 the COLM rebuttal ran May 22 to June 8: reviews and the response window
opened the same day, giving about eighteen days between first sight of the reviews
and the last word you get before the July 8 decision. A rebuttal in that geometry is
a project with a plan, not a reply-all reflex.

## Budget the eighteen days

```text
days 1-2    read only; draft nothing; log every reviewer claim into the four bins
            (misreading / evidence gap / scope fight / correct hit — colm-review-process)
days 3-9    run the winnable experiments — cache-based analyses first, single-GPU
            or small-API-budget runs second; anything needing full retraining is
            out of scope, say so plainly
days 10-13  draft one response per reviewer + a short common preamble for
            cross-cutting points; every paragraph anchored to a page, table,
            appendix section, or new number
days 14-16  co-author cold read: does each response open with its conclusion?
days 17-18  post with margin; OpenReview deadline-hour uploads are self-harm
```

The highest-yield experiments are the ones your artifact discipline pre-paid for: a
cached-responses archive lets you re-slice results, add a metric, or test a reviewer
hypothesis in hours without touching a model (`colm-artifact-evaluation`).

## The objections COLM reviewers actually raise

These four LM-specific objections dominate borderline cases; each has a right and a
wrong answer shape:

| Objection | Weak answer | Strong answer |
|---|---|---|
| "Benchmark is likely contaminated for these models." | "This benchmark is widely used." | Overlap analysis numbers, or dated-item split showing the effect survives on post-cutoff items |
| "Baselines are under-tuned; better prompting closes the gap." | "We used standard prompts." | The tried-ledger: k prompt variants per system, matched budgets; if the gap narrows, report the narrowed gap |
| "Results are on one model family; is this about LMs or about model X?" | "We expect it generalizes." | One added family inside the window, claim rescoped in the revision either way |
| "API model results won't reproduce." | "We used the public API." | Version strings + query dates already in App. A, plus commitment to release the response cache |

Notice the pattern: every strong answer is either *evidence you can generate this
week* or *a scope concession that makes the paper truer*. Both move ACs; indignation
moves nothing.

## Writing mechanics

- **Conclusion first, then support.** "The gap survives decontamination (new Table
  R1): on items post-dating every model's cutoff, the effect is 7.9 points." Then
  the method sentence.
- **Number new artifacts** R1, R2, ... and reference them consistently; the AC
  skims all responses in one sitting and consistent labels are navigation.
- **Quote the reviewer's own words** for each point you answer — it prevents the
  "they dodged my question" reading — and answer *the words*, not a nastier
  paraphrase.
- **Concede in the open.** A visible "R2 is right; we overclaimed X and have
  rescoped to Y" is the single most credibility-generating sentence a rebuttal can
  contain.
- **Stay anonymous.** The discussion is inside double-blind: no lab names, no
  "in our previous paper," no links that resolve to you.
- **Keep LLM-policy discipline** — if a response experiment used LLM-based
  evaluation, it is disclosable under the same 2026 policy as the paper.

## Handling the difficult cases

- **The low-engagement review** (two lines, generic, possibly LLM-drafted without
  disclosure): respond substantively and briefly, then note factually in a comment
  visible to the AC that the review does not engage the paper's content. Flag, do
  not accuse.
- **The scope-fight reviewer** (wants a different paper): one crisp paragraph on
  why the paper's question is the right size, pointing at the venue's own genre —
  measurement and analysis papers are COLM's award lineage — then stop. Repetition
  reads as anxiety.
- **The correct hit you cannot fix in eighteen days:** say what the fix is, why it
  does not fit the window, and how the revision will scope claims meanwhile. ACs
  reward authors who can tell the difference between a flesh wound and a broken
  spine.

## Per-reviewer response skeleton

One response per reviewer, same skeleton, filled with their words and your numbers:

```text
Thank you for the careful reading. We address each point below.

> "<reviewer's sentence, quoted verbatim>"
<conclusion sentence with the page/table/new-artifact anchor>
<one or two support sentences — method, numbers, or the concession>

> "<next quoted point>"
...

Summary of changes committed for the revision:
 1. <rescoped claim / new table R1 folded into §4 / added limitation>
 2. ...
We believe the remaining disagreement (if any) is <one neutral sentence>,
which we leave to the AC's judgment.
```

Length discipline: reviewers are reading many rebuttals in the same week you are
writing yours. A response that fits on one screen per reviewer, with bolded
conclusions and numbered artifacts, gets read twice; a 2,000-word essay gets
skimmed once. If a point genuinely needs depth, put the depth in a clearly labeled
final section so the main thread stays scannable.

## After June 8

Nothing. The reviewer-AC discussion through the July 8 decision has no author
channel — resist the urge to post updates. Spend the month preparing both branches:
the camera-ready plan (due August 7 if accepted) and the resubmission map
(`colm-review-process`).

## Output format

```text
[Window] days remaining: <n> of ~18
[Per reviewer] R<k>: bins A/B/C/D counts + the one thing they must hear
[Experiment queue] <cache-based first, with owner and finish-by date>
[Concessions] <what gets conceded and the rescoped claim>
[AC preamble] <3-sentence summary of what changed during discussion>
```
