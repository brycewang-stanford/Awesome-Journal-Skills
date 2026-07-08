---
name: eccv-writing-style
description: Use when writing or revising an ECCV paper in the Springer LNCS single-column format — spending the 14-page budget (figures and tables included), LNCS-specific layout craft, first-page architecture for a mixed European panel, numbered-citation hygiene, and claims phrased to survive a one-page rebuttal.
---

# ECCV Writing Style

Use this while drafting or compressing an ECCV manuscript. The defining
constraint is the format: **LNCS single-column, 14 pages including figures
and tables**, references-only pages after that. This is a different craft
from the two-column CVF page — more words per page, cheaper full-width
figures, costlier white space — and the template changed after 2024, so
write in the current kit from day one.

## Spending 14 single-column pages

| Budget line | Typical allocation | LNCS-specific note |
|---|---|---|
| Title, abstract, intro | 2.0 pages | Single column makes long intros tempting; cap at 1.25 pages of prose |
| Related work | 1.0 page | Numbered [n] citations pack tightly; group by idea, not by paper |
| Method | 3.5–4.5 pages | Full-width architecture figures are cheap here — use one, not three |
| Experiments | 4.5–5.5 pages | Tables span the full text width; design them wide and few |
| Limitations + conclusion | 0.5–1.0 page | An honest limitations paragraph is expected |
| Figures/tables total | counted inside the 14 | The submission limit *includes* them — every figure displaces prose |

The inclusion of figures in the limit is the discipline lever: each figure
must either carry an argument (teaser, method overview, failure modes) or
compress one (results curves). Decorative variants go to the supplement.

## First-page architecture

An ECCV first page must work for the adjacent-niche reviewer (see
`eccv-review-process`): by the end of page 1 a non-specialist should be able
to say what input becomes what output, why current methods fail at it, and
what single idea fixes it.

- Teaser figure: input → output with one baseline failure alongside, captioned
  so it is understandable without the body text.
- Contribution list: two or three bullets, each falsifiable ("we show X
  improves Y by Z on W"), none of them "extensive experiments".
- Name the setting precisely (supervised? zero-shot? per-scene?) — mixed
  panels misfile vague papers into the wrong baseline universe.

## LNCS mechanics that bite

- Springer's numbered-citation style makes "[23] showed" unreadable; write
  "Author et al. [23] showed" so prose survives the bibliography.
- `\subsubsection` depth is where LNCS headings stop looking like headings;
  restructure rather than nest.
- Single-column tables tolerate more columns than two-column CVF tables —
  merge your ablation grids instead of stacking small tables.
- Keep the references-only rule literal: nothing but bibliography beyond the
  limit — a stray appendix line on page 15 is a compliance failure.

## Claim phrasing sized for the rebuttal

Every headline sentence should be defensible in two rebuttal lines later:

```text
Fragile:  "Our method significantly outperforms all prior work."
Sized:    "On <benchmark vX>, our method improves <metric> by <d> over
           <strongest baseline> under matched <backbone/training data>."
Fragile:  "generalizes to arbitrary scenes"
Sized:    "generalizes across the N categories of <dataset>; unseen
           domains are evaluated in Sec. 5.4 and remain open"
```

Scope every superlative to benchmark + protocol + substrate. In a
foundation-model era, unmatched pretraining data is the first rebuttal
attack surface — declare the substrate in the claim itself.

## Revision passes, in order

1. **Argument pass**: does each section answer the previous one's open question?
2. **Figure pass**: captions self-contained; every figure referenced; each
   earns its page share against the 14-page count.
3. **Claim pass**: apply the sizing patterns above to abstract, intro, and
   conclusion — the three places reviewers quote from.
4. **Anonymity pass**: self-citations in third person, no repo links, no
   acknowledgements.
5. **Template pass**: current-cycle kit, margins untouched, references-only
   overflow.

## Output format

```text
[Style verdict] submit-ready / restructure / compress / re-scope claims
[Page ledger] <section -> pages vs budget, figure share>
[First-page test] <what an adjacent-niche reader retains, or fails to>
[Fragile claims] <sentence -> sized rewrite>
[Pass order] <which of the five passes remain>
```
