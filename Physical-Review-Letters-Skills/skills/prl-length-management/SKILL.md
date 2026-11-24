---
name: prl-length-management
description: Use when a Physical Review Letters manuscript exceeds the strict deductible length limit, where figures, tables, and displayed equations count as word equivalents against the 3750-word budget. Triages what to cut, compress, or move to Supplemental Material; does not rewrite content from scratch.
---

# PRL Length Management (prl-length-management)

## When to trigger

- The manuscript is over the length limit (or you suspect it is)
- You need to know how much "room" a figure or equation actually costs
- You must decide what to cut, compress, or push to Supplemental Material
- A reviewer/editor flagged the Letter as too long
- Late stage: content, figures, and SM are stable and now must fit

## How the PRL length limit works (the deductible model)

A Letter is **short** — **3750 words** for the core of the paper (between the abstract and the Acknowledgments), which works out to about four journal pages; up to **two pages of End Matter** (appendixes and specialist detail, printed after the references) do not count against it (APS PRL author page and Length Guide, re-verified 2026-11-24). The key feature is that the limit is a **deductible budget**: it is not just running text. Against the same total budget you must count, per the APS Length Guide:

- The body text (the largest term).
- Figure and table **captions** and any footnotes/endnotes (counted as text).
- **Figures** — single-column: (150 / aspect ratio) + 20 words; double-column: [300 / (0.5 × aspect ratio)] + 40 words. A wide, short double-column figure costs the most.
- **Equations** — displayed math costs 16 words per row single-column, 32 per row double-column.
- **Tables** — 13 words + 6.5 per line single-column; 26 + 13 per line double-column.

Not counted: title, author list, **abstract**, PhySH keywords/DOI, **references**, byline footnotes and **acknowledgments**. A Letter typeset in REVTeX 4.2 with the `prl` option that fits in four pages is likely to conform. Waivers of 1/2 page or more can be requested from the editor (who must see a clear need and a result of extreme importance); waiver decisions are not appealable. The practical consequence: **a beautiful extra figure can cost you a paragraph of text.** Budget figures and text together, not separately.

## Triage order (cut from cheapest loss to most painful)

1. **Move to SM first.** Derivations, extended data, secondary controls, full error budgets → Supplemental Material (see `prl-supplementary`). This is almost always the largest, lowest-pain saving.
2. **Compress figures.** Drop non-essential panels; convert a double-column figure to single-column; merge two figures showing related points. Each reclaims word-equivalents.
3. **Prune equations.** Keep only claim-defining equations inline; move derivation steps to SM; inline short results within a sentence rather than displaying them.
4. **Use End Matter** (up to two pages, not counted) for appendix-style detail that specialists need; it is not a dumping ground for the core argument.
5. **Tighten prose** (apply `prl-writing-style`): remove padding, hedging, and figure-transcribing sentences.
6. **Cut scope** as a last resort: demote a supporting claim entirely.

## Cost-awareness table

| Element                         | Budget cost (verify formula)        | Cheapest fix                          |
|---------------------------------|-------------------------------------|---------------------------------------|
| Body paragraph of padding       | high per word                       | delete                                |
| Double-column figure            | large word-equivalent               | shrink to single column / fewer panels|
| Extra figure                    | full figure word-equivalent         | move to SM                            |
| Displayed equation              | per-line word-equivalent            | inline or move derivation to SM       |
| Specialist appendix detail      | not counted if in End Matter (≤2 pp)| move to End Matter or SM              |
| Long caption                    | counts as text                      | tighten                               |

## Checklist

- [ ] You have run the current APS length formula / length-check, not just a word count
- [ ] Figures and equations are counted against the budget, not ignored
- [ ] Derivations and extended data are in SM, not the body
- [ ] No double-column figure remains unless the data demand it
- [ ] Only claim-defining equations are displayed inline
- [ ] End Matter (if used) stays within two pages; references are not being cut to save words (they do not count)
- [ ] Prose padding/hedging removed (cross-check `prl-writing-style`)
- [ ] The Letter still stands alone after trimming (cross-check `prl-supplementary`)

## Anti-patterns

- Counting only words and being surprised the figures blow the limit
- Trimming load-bearing content (the key control, the headline uncertainty) to fit
- Shrinking fonts in figures to save area (fails legibility instead)
- Padding the SM until the Letter no longer stands alone
- Leaving a decorative double-column figure that costs a paragraph
- Discovering the over-length only at submission, after content is frozen

## Output format

```
【Current length vs. limit】over by ~X (per APS formula, verify)
【Figure/table/equation word equivalents counted】yes / redo with formula
【Moved to SM】list
【Figures compressed】list (double→single, panels dropped, merged)
【Equations pruned】list
【End Matter used】pages (≤2)
【Still stands alone】yes / fix
【Next】prl-cover-letter or prl-submission
```

> The word/page limit, the length formula, and per-element costs are exactly the kind of volatile specifics that change — always verify the current limit and length guide on the official APS / PRL author page.
