---
name: aerj-tables-figures
description: Use when building tables and figures for an American Educational Research Journal (AERJ) manuscript. Exhibits must be self-contained, accessible, and formatted to APA 7th edition, and they must be anonymized for masked review. Improves exhibits; it does not generate data.
---

# Tables & Figures (aerj-tables-figures)

In AERJ, a reader should grasp each exhibit **without hunting through the text**, and every exhibit must
follow **APA 7th-edition** table/figure conventions. Because review is **masked**, exhibits must carry
no identifying clues (institution names, data-source giveaways in titles).

## When to trigger

- Designing tables/figures or revising them after analysis
- A reviewer found an exhibit unreadable, mislabeled, or non-APA
- Preparing exhibits for a masked submission (no identifying content)
- Deciding what belongs in the body vs an appendix

## Principles

1. **Self-contained.** Title states what the exhibit shows; notes define every abbreviation, the
   sample/N, the units, and significance/probability conventions. A reader should not need the text.
2. **APA 7th-edition format.** Table number + italic title; horizontal rules only (no vertical rules);
   figure number + title; a general note, then specific notes, then probability notes.
3. **Report estimates with uncertainty.** Coefficients with SEs/CIs; for multilevel models, label
   levels and random effects; mark the estimand, not just stars.
4. **Figures earn their place.** Use a figure when it shows something a table cannot (trajectories,
   interactions, distributions, RD/event-study, joint displays for mixed methods). Otherwise use a table.
5. **Accessibility.** Colorblind-safe palettes; legible in grayscale; readable at print size; vector
   output for line art.
6. **Qualitative exhibits.** Coding trees, thematic maps, and evidence tables (theme → exemplar
   quotation) are legitimate exhibits — anonymize participants and sites.
7. **Match the package.** Exhibit numbers/values must match the analysis output and the deposited
   materials (see `aerj-transparency-and-data-policy`).

## Anti-patterns

- Tables readable only with the surrounding paragraph
- Vertical rules, inconsistent decimals, undefined abbreviations (non-APA)
- Stars without effect sizes or intervals; no N or units
- Rainbow palettes that fail in grayscale or for colorblind readers
- Identifying clues in titles/notes that break masking
- Exhibit values that drift from the replication package

## Output format

```
【Exhibit】table / figure — one-line purpose
【Self-contained?】title + notes define N, units, abbreviations, significance [Y/N]
【APA 7th format】[Y/N]
【Uncertainty shown】SE/CI + estimand labeled [Y/N]
【Accessible】colorblind-safe + grayscale-legible [Y/N]
【Masked】no identifying clues [Y/N]
【Next】aerj-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — plotting/exhibit tooling and APA table helpers
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — APA style and masked-review requirements
