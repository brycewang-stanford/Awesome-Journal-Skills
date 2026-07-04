---
name: poq-submission
description: Use when running the final pre-submission preflight for Public Opinion Quarterly (POQ) via ScholarOne Manuscripts — submission-type selection, double-blind preparation, word caps, AAPOR-standard Appendix A disclosure, the Data Availability Statement, and the replication package. Final checks; it does not draft content.
---

# Submission Preflight (poq-submission)

The last check before pressing submit on **ScholarOne Manuscripts**. POQ is **double-blind**, so the
single most common avoidable failure is an under-anonymized manuscript — and the second is a missing or
incomplete **Appendix A: Disclosure Elements**. Verify volatile specifics on the official page before
relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming the type's word cap is met and the manuscript is properly anonymized and disclosed

## Process facts (verify volatile items on the official page)

- **Publisher / affiliate:** Oxford University Press / American Association for Public Opinion Research (AAPOR).
- **Portal:** **ScholarOne Manuscripts** (`mc.manuscriptcentral.com/poq`).
- **Review model:** **double-blind** — anonymize the manuscript; provide a separate title page.
- **Submission types & caps (text + notes; exclude figures, tables, references, appendices):**
  Original Article **≤ 6,500**; Research Note **< 3,000**; Polls in Context **≤ 2,500**; Research
  Synthesis **≤ 6,500** (incl. notes); Book Review **~1,200**.
- **AAPOR disclosure:** **Appendix A: Disclosure Elements** for all data reported (funding, exact
  wording, population, sample design, mode + dates, response rate per AAPOR definitions, sample sizes +
  precision, clustering/weighting design effects).
- **Data policy:** replication package to **POQ's Harvard Dataverse**; **Data Availability Statement**
  in the endmatter; materials archived **before typesetting**.
- **Fee:** no submission fee stated (consistent as of 2026-06-22); any open-access APC handled by OUP
  after acceptance — re-verify current charges on the OUP page before submission (待核实).

## Preflight checklist

### Type & length
- [ ] Type chosen and its word cap met (Article ≤ 6,500 / Note < 3,000 / Polls ≤ 2,500 — text + notes)
- [ ] Abstract present and within the current requirement (待核实 on exact cap)
- [ ] Footnotes/endnotes counted toward the cap; long methods moved to appendices (excluded)

### AAPOR disclosure (the POQ-specific gate)
- [ ] **Appendix A: Disclosure Elements** present and complete for every dataset
- [ ] Response rate stated **with AAPOR Standard Definition + calculation**
- [ ] Sample design, mode, dates, sample sizes, precision, weighting/clustering documented

### Anonymity (double-blind)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] No obvious self-references; self-citations neutralized
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Data & files
- [ ] Replication package staged for **POQ's Dataverse** (reproduces every table/figure)
- [ ] **Data Availability Statement** drafted for the endmatter
- [ ] Ethics / IRB / human-subjects compliance addressed
- [ ] Figures/tables self-contained and accessible (see `poq-tables-figures`)

## How the editorial office reads your upload

Think of the ScholarOne package as being screened in this order, and stage files so each check
passes on the first look:

1. **Anonymity sweep** — the anonymized main document is opened first. A name in the running
   header, an "as we showed (Author 2023)" self-citation, or author initials in tracked-changes
   metadata sends the package back before any editor reads the abstract. Export a fresh PDF/DOCX
   and check File → Properties, not just the visible text.
2. **Type-and-cap check** — the declared submission type is compared against the word count you
   enter. Count text + notes yourself before upload; an Article-length manuscript declared as a
   Research Note is returned, not silently retyped.
3. **Disclosure scan** — the office looks for Appendix A by name. Label it exactly "Appendix A:
   Disclosure Elements," one block per dataset, response-rate formula named (e.g., AAPOR RR3), so a
   screener can verify completeness without reading the methods section.
4. **Endmatter** — Data Availability Statement present, Dataverse plan stated, IRB noted. Missing
   endmatter is the most common cause of a revise-before-review email.

A package that survives all four screens goes to the editor with no round-trip — often saving two
weeks of calendar time before first decision.

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-blind)
- A missing or incomplete Appendix A; a response rate with no AAPOR definition
- Sending a long paper to the Research Note or Polls in Context track
- Counting figures/tables against the cap (they are excluded) while ignoring footnotes (they count)
- Budgeting for a submission fee that is not charged (verify)

## Output format

```
【Type】Article / Note / Polls in Context / Synthesis / Book Review (cap met? Y/N)
【Appendix A】complete + AAPOR response rate calculation? [Y/N]
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Word count】within cap (text + notes)?
【Repro package + DAS】staged for POQ Dataverse + DAS drafted? [Y/N]
【Next】await decision → poq-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official POQ URLs behind every fact in this pack
