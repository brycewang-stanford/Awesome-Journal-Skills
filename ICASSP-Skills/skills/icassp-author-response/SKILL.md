---
name: icassp-author-response
description: Use when drafting an ICASSP rebuttal or author response to reviews, covering the recently added and short author-response window, the single-blind setting where reviewers already know you, answering signal-processing reviewers from the four-page record without a revised PDF, and writing for the technical-committee decision rather than for tone.
---

# ICASSP Author Response

Use this after ICASSP reviews are released. First confirm whether the current cycle even runs a
rebuttal: ICASSP historically had **no** author-response stage, and a short window is a
comparatively **recent addition** (in the 2026 cycle authors could reply until ~22 December
2025). Reopen the current call before promising reviewers anything.

## What the rebuttal is and is not

- It is a **short, text-based reply** to the reviews, not a chance to upload a revised PDF or new
  experiments. Argue from what you already submitted.
- ICASSP is **single-blind**, so the reviewers know your identity; write professionally and do
  not attempt to re-establish anonymity or drop identifying hints to sway a reviewer.
- The audience is the **area/technical-committee decision**: give whoever aggregates the reviews
  a clean reason to accept, not a point-by-point defense that wins arguments but not the paper.

## Triage before drafting

1. Separate **factual errors in the review** (a metric misread, a missed baseline that is in the
   paper) from **legitimate gaps** (a missing comparison, an unreported condition).
2. Fix the factual errors first with an exact pointer: "Table 2, row 3 already reports this."
3. For real gaps, concede cleanly and scope a **camera-ready** clarification that adds no
   unsupported new claim — the four pages you submitted are the evidence of record.
4. Rank concerns by decision weight; one resolved correctness objection outranks five answered
   style notes.

## Signal-processing reviewer pushback patterns

| Pushback | What it signals | ICASSP-ready fix |
|---|---|---|
| "The baseline is not the current strong method" | Reviewer knows the task's state of the art | Name the specific stronger baseline you did compare, or concede and scope it for camera-ready |
| "Which SNR / condition does this hold at?" | The reported number hides its operating point | Point to the sweep or table cell; if only one condition was tested, say so plainly |
| "Metric is not the one this task uses" | Measurement mismatch (e.g., accuracy where SI-SDR belongs) | Report the field-standard metric if you have it, or explain why yours is defensible |
| "No significance / spread over runs" | One-seed result | Cite the multi-run spread if present; otherwise concede it as a limitation |
| "This is a known result / prior art" | Novelty challenge | Cite the exact delta versus the named prior work in one sentence |

## Drafting pattern

1. Open with the single most decision-critical correction or concession.
2. Anchor each point to an exact location in the submitted paper (table, figure, equation, line).
3. State the signal-processing consequence, not just the fact.
4. Promise only camera-ready wording or clarification fixes that stay within the accepted claim.

## Micro-example

Reviewer objection: the enhancement gain is reported only at one SNR, so the improvement may not
generalize. Reply skeleton:

1. Concede the main table fixes SNR at one value for space.
2. Point to Fig. 3, which already sweeps 0-15 dB and shows the gain persists.
3. Note the trend is monotone, so the single-SNR table is representative, not cherry-picked.
4. Offer one camera-ready sentence stating the operating range explicitly.

## Calibration for a short window

- Reply **early**; ICASSP rebuttal windows are brief and a late, exhaustive reply is worth less
  than a prompt, precise one.
- Do not paste new derivations or fresh result tables the reviewers cannot verify against the
  submitted PDF.
- Keep within any stated length/format cap; if none is stated, be concise anyway — committee
  members read many rebuttals in one sitting.

## Output format

```text
[Rebuttal exists?] yes (dates) / no this cycle / unverified
[Priority issue] <reviewer concern>
[Decision dimension] correctness / novelty / evidence / clarity / metric-fit
[Draft response] <ICASSP-ready text, anchored to submitted paper>
[Evidence anchor] <table/figure/equation/line>
[Camera-ready promise] <scoped fix that adds no new claim>
```

## Currency note

The 2026 rebuttal window (reported open to ~22 December 2025) was checked 2026-07-09 via
official-page renderings (see `../../resources/official-source-map.md`). Whether a rebuttal
recurs, and its dates and length, are cycle-specific — verify on the current call before drafting.
