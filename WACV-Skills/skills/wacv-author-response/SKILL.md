---
name: wacv-author-response
description: Use when responding to WACV reviews, covering the optional one-page Round 1 rebuttal and, separately, the Revise-and-Resubmit change summary that carries a revised paper into the no-rebuttal Round 2, including how to triage three reviews for the area chair, what a rebuttal can and cannot claim, and keeping every response double-blind.
---

# WACV Author Response

WACV gives you **two different response instruments**, and confusing them wastes the one
that matters. Use this after Round 1 reviews arrive. Facts are the WACV 2026/2027 cycles as
read on 2026-07-09; reopen the current Author Guidelines for the rebuttal template and rules
before drafting.

## Know which instrument you are writing

| Situation | Instrument | Constraint |
|---|---|---|
| R1 reviews arrived, decision not yet set | **One-page rebuttal** (optional) | Single-page PDF, author-kit template, no external links, no new unrequested contributions |
| R1 decision = Revise and Resubmit | **Revised paper + change summary** | The revision *is* the argument; there is no R2 rebuttal |
| New Round 2 submission | *(none)* | Round 2 has no author-response step |

The strategic point: at WACV the **change summary that accompanies a Revise-and-Resubmit
carries more weight than any rebuttal**, because Round 2 has no rebuttal to fall back on. If
you must choose where to spend effort, spend it on executing and documenting the revision.

## The one-page Round 1 rebuttal

Treat it as a single skimmable page written for the **area chair**, who must reconcile three
reviews. Order it by decision impact, not by reviewer number:

1. **Factual corrections first.** If a reviewer's objection rests on a misread ("no
   ablation of component X" when Table 3 is exactly that), correct it in one line with the
   pointer. Factual kills move a recommendation fastest.
2. **The single biggest shared concern next**, answered with a mini-result the page can
   hold — one small table or one number, not a promise.
3. **Calibrated concessions.** Concede what is true and scope the claim; a rebuttal that
   disputes everything reads as defensive to the AC.

A rebuttal **cannot** add a new contribution, link to external material, or exceed the page.
It can correct errors, clarify scope, and present a small confirmatory result that already
exists.

```text
[AC summary line] The core objection (R2/R3): "X under condition C" — addressed in point 1.
1. FACTUAL: R2 says no matched-baseline comparison. See Tab. 3 (same budget). Not missing.
2. CORE: R1/R3 doubt robustness under C. New small table: metric held within m over 3 seeds.
3. CONCEDE: R3 is right that claim was too broad; we scope it to setting S (one sentence).
```

## The Revise-and-Resubmit change summary

This is where WACV papers are actually won. Read the R1 reviews as a **revision
specification**, then:

- Enumerate each reviewer-requested change and map it to a concrete edit (new experiment,
  rewritten claim, added baseline, clarified assumption).
- Make exactly those changes in the paper, and keep the **artifact and supplement in sync**
  with the revised claims (see `wacv-artifact-evaluation`, `wacv-supplementary`).
- Write a short, itemized summary of what changed and where, in the reviewers' own terms,
  so the Round 2 reviewers can verify the gap is closed without re-deriving it.

## Anonymity holds throughout

Both instruments are double-blind. Do not de-anonymize in the rebuttal or the change
summary, do not link to author-identifying pages, and do not name your institution or prior
work in first person. A response that leaks identity can undo the review it was meant to win.

## Reverify each cycle

- The Round 1 rebuttal length and template, and that Round 2 still has no rebuttal.
- Whether a structured change summary / response field is required for revised R2 papers.
- Any word or format limit and the no-external-links rule.

## Output format

```text
[Instrument] one-page R1 rebuttal / R&R change summary / none (new R2)
[AC-facing summary] <one line naming the decisive objection>
[Factual corrections] <list with pointers>
[Core concern + existing evidence] <mini-table or number>
[Concessions/scoping] <what you concede>
[If R&R] each requested change → edit made: <mapping>
[Anonymity] clean: yes/no
```
