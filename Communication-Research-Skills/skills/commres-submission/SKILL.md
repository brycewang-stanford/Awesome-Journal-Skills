---
name: commres-submission
description: Use when running the final pre-submission preflight for Communication Research (CR) via SAGE Track (ScholarOne) — double-anonymized preparation, the 45-page limit, APA reporting, the data-availability statement, ORCID, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (commres-submission)

The last check before pressing submit on **SAGE Track** (ScholarOne). CR is **double-anonymized**, so
the single most common avoidable failure is an under-anonymized main document or supplement. Verify
volatile specifics on the SAGE author page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata SAGE Track expects
- Confirming the page limit, APA reporting, and anonymization are clean

## Process facts (verify volatile items on the official page)

- **Publisher:** SAGE Publishing. Founded **1974**; bimonthly; ISSN **0093-6502** (print) / **1552-3810**
  (online).
- **Portal:** **SAGE Track** (ScholarOne); author guidelines at
  `journals.sagepub.com/author-instructions/crx` (检索于 2026-06；以官网为准).
- **Review model:** **double-anonymized** — anonymize the main document **and** supplemental materials;
  provide a separate title page. An **initial evaluation precedes peer review**; **two independent
  reviews** are required to back a Revise or Accept. Reviewers recommend to the **Co-editors, who make
  the final decision**.
- **Reviewer suggestions:** the **journal assigns reviewers and does not accept author
  recommendations** — do not include a suggested-reviewer list.
- **Length:** manuscript **no more than 45 pages, double-spaced, inclusive of references**;
  **supplementary files do not count toward the page limit**.
- **Abstract:** **unstructured, no more than 150 words**, placed between title and main body;
  clinical-trial registration details (if applicable) go at the **end of the abstract**.
- **Special issues:** CR **does not publish special issues and does not work with guest editors**.
- **Preprints:** accepted as **prior posting** — supply the **DOI at submission**, and add the
  final-version link if accepted.
- **Style & reporting:** **APA**; report statistics in line with APA — standard deviations and **effect
  sizes** where applicable; power analysis, confidence intervals for bootstrapping, and correlation
  matrices (as an online appendix) are encouraged where relevant.
- **Self-citations:** written in the **third person**.
- **Transparency:** **data-availability statement** expected; note any **preregistration** in the cover
  letter; deposit **open-materials/data** if claiming open practices; provide **ORCID** where requested.
- **Fee:** no submission fee for the standard (subscription) route (verified 2026-06-22); an optional
  **open-access APC** applies only if you choose OA after acceptance — SAGE sets the amount on its live
  OA page (confirm before quoting).
- **Editors:** final decisions rest with the **Co-Editors** — **Silvia Knobloch-Westerwick (Ohio State)
  & Jennifer Gibbs (UC Santa Barbara)** (verified 2026-06-22); editor roles rotate, so confirm the
  current masthead on the live SAGE page before naming them.

## Preflight checklist

### Format & length
- [ ] Manuscript ≤ **45 pages**, double-spaced, **inclusive of references**
- [ ] Full specifications, scale items, robustness grids, codebooks moved to the **online supplement**
- [ ] Abstract **unstructured, ≤ 150 words**, between title and main body; states question + design + tested mechanism + finding

### Anonymity (double-anonymized)
- [ ] No author names, affiliations, or acknowledgments in the **main document**
- [ ] **Supplemental materials also anonymized** (no identifying links/paths)
- [ ] **Self-citations in the third person** ("Smith and Lee (2024) showed…", not "as we showed…")
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate (non-anonymous) **title page** with contact info + brief bio prepared as a distinct file

### Reporting & metadata
- [ ] **APA** formatting; statistics reported with SDs and **effect sizes**, CIs, df, exact p
- [ ] Mediation reported with **bootstrap CIs**; moderated mediation with the index
- [ ] Figures/tables self-contained, accessible (see `commres-tables-figures`)
- [ ] **ORCID** provided where requested

### Compliance & files
- [ ] Ethics / IRB / human-subjects compliance stated
- [ ] **Data-availability statement** included; preregistration noted in cover letter if applicable
- [ ] Open-materials/data staged if claiming open practices (see `commres-transparency-and-data`)

## Desk-reject and return-to-author patterns (avoidable before upload)

| Trigger seen at intake | Editor action | Preflight fix |
|------------------------|---------------|---------------|
| Author name in main doc or file properties | returned for anonymity | strip metadata; identity to the title page |
| Manuscript over 45 double-spaced pages (refs counted) | returned for length | move specs/scales/robustness to the supplement |
| Stars-only results, no effect sizes | returned for APA reporting | add d/η²ₚ/β + CIs; report SDs |
| Qualitative/descriptive submission | declined without review | re-route to a generalist/digital sibling, or add a tested mechanism |
| Abstract over 150 words or structured | returned incomplete | trim to ≤ 150 words, unstructured, between title and body |
| No data-availability statement | flagged incomplete | add the statement (repository + identifier, or exemption) |

## Calibration anchor: what "ready" means at CR (hedged)

A CR-ready submission clears three bars at once: a **tested communication mechanism** (not a bare
effect), **valid, reliably measured constructs** an expert referee will trust, and **APA-standard
reporting** with effect sizes and uncertainty. Volatile specifics — exact caps, APC, masthead,
timelines — drift; **confirm against the current SAGE author page (待核实)**.

## Worked micro-example: a 5-minute anonymity sweep (illustrative)

Before upload, a survey-experiment manuscript runs the sweep: (1) search the main doc for the author
surname — two first-person self-cites get rewritten in the third person; (2) an OSF link in the
supplement resolving to a named project is swapped for a view-only anonymized link; (3) clear the
author field in document properties; (4) confirm the scale items and CFA table sit in the supplement,
not the main text, keeping the manuscript under 45 pages. All four would otherwise return the paper.

## Anti-patterns

- Leaving author identifiers in the text, supplements, or file metadata (breaks anonymization)
- First-person self-references ("as we previously found") instead of third-person
- Reporting significance without effect sizes (an APA-reporting failure at CR)
- Manuscript over 45 double-spaced pages because supplements were not used
- Omitting the data-availability statement

## Output format

```
【Anonymized】main doc + supplements + file metadata clean? [Y/N]
【Self-citations third person】[Y/N]
【Length】≤ 45 double-spaced pp incl. references? [Y/N]
【APA reporting】effect sizes + CIs/SDs, mediation bootstrap CIs? [Y/N]
【Title page】separate non-anonymous file with bio + ORCID? [Y/N]
【Data-availability statement】included? [Y/N]
【Next】await decision → commres-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — copy-paste preflight checklist
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official CR/SAGE URLs behind every fact in this pack
