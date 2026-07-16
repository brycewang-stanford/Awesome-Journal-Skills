---
name: aos-tables-figures
description: Use when building the exhibits of an Accounting, Organizations and Society (AOS) manuscript — data-inventory and evidence tables for qualitative work, cell-means and process-test tables for experiments, and figures that carry theoretical weight — in Elsevier-compatible format. Builds exhibits; it does not run the analysis (aos-data-analysis).
---

# Tables & Figures (aos-tables-figures)

## When to trigger

- A field paper has long quotations but no exhibit showing the evidentiary base
- Experimental results lack a clean cell-means or contrast table
- A figure decorates rather than argues (or a needed process figure is missing)
- Formatting must be reconciled with Elsevier submission requirements

## Exhibits by tradition — what AOS reviewers look for

**Qualitative field / historical papers**

- **Data-inventory table**: interviews (number, roles, duration, period), observations (events, hours), documents (types, spans) — the single exhibit that preempts "how much data is behind this?"
- **Evidence table(s)**: conceptual claim or second-order theme in one column, representative field excerpts in the other, so the interpretive chain is inspectable without bloating the text.
- **Coding-structure exhibit** where the paper's method warrants it: first-order codes → second-order categories → aggregate concepts, showing movement from informant language to theory.
- **Timeline or process figure** for change studies: phases, key events, and where the accounting practice intervened.
- Anonymize consistently — pseudonyms and role labels in exhibits must match the text and betray no site identity.

**Experimental / survey papers**

- Cell-means table: means, SDs, n per condition; the predicted pattern visible at a glance.
- Contrast/ANOVA table plus process results (mediation with bootstrap CIs) as exhibits, not prose asides.
- An interaction figure with error bars when a moderation is the theory's signature; axis units interpretable, no truncated scales that exaggerate effects.
- Survey papers: construct table (items, sources, reliabilities) and a correlation matrix.

**Archival-with-theory papers**

- Descriptives, the main estimation table with clustering and fixed-effects structure stated in the notes, and magnitudes interpreted in institutional terms.

## Self-containment and format

- Every exhibit readable alone: title stating what it shows, sample/period, definitions, and the meaning of any markers in the notes.
- Number tables and figures consecutively; place callouts in the text; Elsevier prefers editable source files for tables and high-resolution figure files at final stages — confirm current artwork specs in the AOS Guide for Authors before submission.
- Keep exhibits inside the double-anonymized envelope: no author names in captions, file names, or embedded metadata.
- Ration exhibits: each one must carry evidence or structure the argument; move genuinely supplementary material to an appendix or online supplement.

## The one-sentence test

For every exhibit, write the sentence it proves ("Table 2 shows the interpretation rests on 74 interviews across four roles over 26 months"; "Figure 3 shows the effect reverses under high accountability"). If no sentence exists, cut the exhibit; if the sentence is central and no exhibit backs it, build one.

## Checklist

- [ ] (Qualitative) data-inventory table present; evidence/coding exhibits trace claims to material
- [ ] (Experimental) cell means, contrasts, process tests, and the key interaction figure present
- [ ] Every exhibit passes the one-sentence test and is self-contained
- [ ] Pseudonyms/labels consistent across text and exhibits; anonymity preserved
- [ ] Numbering, callouts, and artwork specs match the current Guide for Authors
- [ ] No exhibit metadata or file name identifies the authors or the site

## Anti-patterns

- **Quote dumps in tables** — excerpts without the conceptual column that gives them a job.
- **Decorative frameworks**: boxes-and-arrows figures that restate the table of contents.
- **Cell-means tables missing n or SDs**, or interaction plots without uncertainty.
- **Exhibit inflation**: ten tables where three would carry the argument.
- **Anonymity leaks** through logos, letterheads, or document scans reproduced in figures.

## Output format

```
【Exhibit list】each with its one-sentence job ...
【Data inventory (qual)】interviews / observations / documents tabulated? ...
【Process exhibits (exp)】cell means, contrasts, mediation, interaction figure ...
【Self-containment】titles, notes, definitions complete? ...
【Anonymity & format】pseudonyms consistent; Elsevier artwork specs checked ...
【Next step】aos-writing-style
```
