---
name: jim-tables-figures
description: Use when building or pruning the exhibits of a Journal of International Marketing (JIM) manuscript — the invariance table, per-country descriptives, cross-level model figures, and fitting everything inside the 50-page all-inclusive cap. It shapes exhibits; jim-data-analysis produced the numbers.
---

# Tables, Figures & the Page Budget (jim-tables-figures)

## When to trigger

- Results exist but the exhibit set has not been designed as a set
- The manuscript is over the 50-page all-inclusive limit and something must move or die
- A reviewer says the country comparisons are impossible to follow
- Tables were pasted from software output and still look like it

## The exhibit spine of a multi-country JIM paper

In reading order, the set most JIM empirical papers need:

1. **Conceptual model figure.** Boxes at labeled levels; the country-level moderator drawn at its own level with the cross-level arrow hitting the *path*, not the box. Hypothesis numbers on the arrows. A reader should reconstruct every hypothesis from this figure alone.
2. **Country/sample profile table.** Per country: N, sampling frame, fieldwork window, language version, demographics, and the focal dimension scores that justified selection. This table carries the equivalence argument — do not scatter it through prose.
3. **Measurement table.** Constructs, example items, per-country CR/AVE ranges, and source citations for scales.
4. **Invariance table.** One row per step (configural/metric/scalar, partial releases, alignment summary) with fit indices, Δ-statistics, and the verdict column. This is the exhibit JIM methods reviewers open first; give it a full table, never a footnote.
5. **Per-country descriptives/correlations.** Often Web Appendix; keep pooled-plus-range in the body.
6. **Hypothesis-test table.** Estimates with CIs by country group or with cross-level interactions; a final column mapping each row to H# and verdict (supported / not / partially).
7. **The money exhibit.** One figure showing the cross-national pattern itself — interaction plot of the effect across the country dimension, coefficient-by-country forest plot, or predicted-values map. If a reader sees one exhibit, this is it.

## The 50-page budget is a design constraint, not a formatting chore

JIM's cap — 50 pages including title, 200-word abstract, keywords, text, footnotes, references, tables, figures, and print appendices (12-pt Times New Roman, double-spaced, 1-inch margins) — forces triage. Budget rule of thumb for an empirical paper: exhibits ≤ 12 pages, references ≤ 6, leaving ~30 for text. What stays in the body: the seven spine exhibits above. What goes to the **Web Appendix**: item wordings in all languages, full per-country correlation matrices, invariance sensitivity runs, alternative estimators, and stimulus materials. The Web Appendix must be as anonymous as the manuscript.

## Craft rules that read as house standard

- Every exhibit self-contained: title states what and where ("…across 12 countries, 2023"), notes define abbreviations, samples, and significance conventions.
- Countries ordered by the theoretical dimension, not alphabetically — the ordering *is* an argument.
- Report magnitudes visibly: standardized coefficients with CIs; don't let asterisks do the talking.
- One decimal policy, one variable-naming policy, everywhere; "CET" in Table 2 cannot become "ethnocentrism" in Table 4.
- Figures legible in grayscale print at final size; no chart-junk maps that add geography but no information.
- Number exhibits in order of first mention; every exhibit cited in text; nothing cited that doesn't exist.

## Prune with the claim test

For each exhibit ask: *which sentence in the paper would become unbelievable if this exhibit vanished?* No sentence → Web Appendix or delete. Two exhibits guarding the same sentence → merge. A results table nobody interprets row-by-row → collapse to the rows the hypotheses need and push the rest out.

## Checklist

- [ ] Conceptual figure reconstructs all hypotheses, levels labeled, moderation arrows on paths
- [ ] Country/sample profile table carries the equivalence evidence in one place
- [ ] Invariance table complete: steps, fit, Δ-criteria, verdicts
- [ ] Hypothesis table maps every row to an H# and a verdict
- [ ] One money exhibit shows the cross-national pattern graphically
- [ ] Total manuscript ≤ 50 formatted pages; Web Appendix split executed and anonymized
- [ ] Country ordering, decimals, and construct names consistent across all exhibits

## Anti-patterns

- The invariance evidence buried in a paragraph or a footnote
- Twelve country columns of raw output where a forest plot was needed
- Alphabetical country ordering that hides the theoretical gradient
- Exhibits that survive only because deleting them feels wasteful
- A Web Appendix used as a landfill — unlabeled, uncited, identity-leaking
- Blowing the page cap and "fixing" it with 1.5 spacing or 11-pt font (preflight will catch it)

## Output format

```text
【Spine】model fig / country profile / measurement / invariance / descriptives / H-tests / money exhibit: status each
【Money exhibit】what pattern it shows, in one line
【Page budget】text __ + exhibits __ + refs __ = __ / 50
【Web Appendix】contents list, anonymized: yes/no
【Consistency】ordering, decimals, naming: pass/fix
【Next skill】jim-writing-style
```
