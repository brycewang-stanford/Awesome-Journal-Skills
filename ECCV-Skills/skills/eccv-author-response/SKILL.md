---
name: eccv-author-response
description: Use when drafting an ECCV rebuttal — the optional one-page, two-column PDF answering three-plus reviews inside a nine-day window (reviews May 2, rebuttal due May 11 in 2026), with references counted inside the page, no venue-forbidden extras, and arguments sized for the area-chair discussion that follows.
---

# ECCV Author Response

Use this when ECCV reviews land. In the 2026 cycle reviews were released
May 2, the rebuttal was due May 11, and reviewers received rebuttals on
May 12 — nine calendar days to answer everything. The rebuttal was optional,
a single-page PDF **including references**, set in a two-column rebuttal
template even though the paper itself is single-column LNCS.

## What the one page is for

The rebuttal's real reader is the area chair running the post-rebuttal
discussion, not the reviewer who wrote the complaint. Write each block so an
AC can lift it directly into a meta-review: objection, answer, pointer into
the submitted PDF.

- Answer misreadings first — they are the cheapest score to recover.
- Answer requests whose evidence already exists in the paper or supplement
  second; cite figure/table/line numbers, never "see above".
- Concede real limitations in one sentence each; a clean concession reads
  better in discussion than a strained defense.
- Skip philosophical disagreements about importance; one page cannot win them.

## Budgeting a page against three reviews

| Block | Share of the page | Content rule |
|---|---|---|
| Header + shared clarification | ~15% | One paragraph fixing the misunderstanding all reviewers share, if any |
| Reviewer 1 (most negative, fixable) | ~35% | Two or three numbered points, each ending in a PDF pointer |
| Reviewer 2 | ~25% | Same pattern, shorter |
| Reviewer 3 (already positive) | ~10% | Thank, confirm, correct one detail |
| References | ~15% | Only citations actually used in the rebuttal — they count against the page |

References counting inside the single page is the ECCV-specific squeeze:
every citation you add deletes a sentence of argument. Cite by number into
the paper's own bibliography where possible instead of restating entries.

## New-experiment judgment

ECCV rebuttal norms on new results vary by cycle and are enforced by ACs, so
check the current author FAQ before pasting fresh numbers (待核实 for any
cycle you are in). The safe pattern regardless of cycle:

1. If a number already exists in the supplement, quote it — that is retrieval,
   not new work.
2. If a small experiment is genuinely decisive and the FAQ permits it, report
   it in one row with its protocol named, no new figure.
3. Never promise a camera-ready experiment you have not already run; ECCV ACs
   read unbacked promises as concessions.

## Nine-day schedule

```text
Day 0-1  (May 2-3):  read all reviews twice; classify every point:
                     misread / evidence-exists / real-gap / opinion
Day 2-3:            draft answers for misread + evidence-exists points
Day 4-5:            run at most ONE decisive check if the cycle allows it
Day 6:              compress to one page in the official rebuttal template
Day 7:              co-author pass — every claim gets a PDF pointer or dies
Day 8  (May 10):    freeze; upload a day before the May 11 cutoff
```

## Tone calibration for a European generalist panel

ECCV panels mix subfields more than a specialist workshop would; the
reviewer who scored you lowest may be adjacent to, not inside, your niche.
Spell out what a neighboring-subfield reader needs (what the benchmark
measures, why the baseline is the right one) instead of assuming shared
folklore. Avoid sarcasm and priority fights — the AC discussion happens in
your absence, and your prose is the only advocate present.

## Output format

```text
[Rebuttal verdict] worth submitting / skip (already sunk or already safe)
[Point map] <review point -> misread / evidence-exists / real-gap / opinion>
[Page budget] <block -> lines allocated>
[PDF pointers] <claim -> figure/table/section in the submission>
[Risks] <new-result rule check, reference overflow, tone flags>
```
