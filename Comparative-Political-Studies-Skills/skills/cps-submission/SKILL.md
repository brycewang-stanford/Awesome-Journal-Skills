---
name: cps-submission
description: Use when preparing the final Comparative Political Studies (CPS) submission package for SAGE Track (ScholarOne) — anonymization, word count, abstract, ORCID, title page, and data availability statement. Runs the submission preflight; it does not draft the manuscript.
---

# Submission Preflight (cps-submission)

The last gate before SAGE Track. CPS desk-screens on fit and basics, so a clean, correctly anonymized,
within-limit package avoids an avoidable bounce. Run this checklist against the live SAGE author
instructions before you click submit — volatile specifics change.

## When to trigger

- Assembling the final files for SAGE Track (ScholarOne) submission
- Final anonymization and word-count pass
- Writing the data availability statement and confirming ORCID
- A submission was returned for a formatting or anonymity problem

## Submission components

| Component | Requirement (检索于 2026-06；以官网为准) |
|-----------|------|
| Portal | **SAGE Track (ScholarOne)** — reuse an existing account if you have reviewed/authored within the past year |
| Anonymized manuscript | Identifying info removed from the main file (sent to reviewers) |
| Title page (separate) | Authors, affiliations, contact, acknowledgments — kept off the review file |
| Word count | Article **max 11,000 words**; references, tables, figures **excluded** |
| Abstract | **Unstructured, ~150 words** between title and body |
| References | **APA-style author-date** (SAGE house); in-text and list agree |
| ORCID | **Required for the submitting author**; co-authors encouraged to link before acceptance |
| Data availability statement | Required — available where / why not shared |
| Replication materials | Quantitative papers: staged for the **CPS Dataverse** (gates final acceptance) |
| Pre-analysis plan | Optional, anonymized, as supplementary material |
| Supplementary / online appendix | Robustness grids and secondary material |

## Anonymization preflight (CPS is anonymous-reviewed)

- Remove author names, affiliations, acknowledgments, and grant numbers from the main file → title page.
- Neutralize obvious self-references ("in our prior work" → "prior work [Author, year]").
- Strip identifying metadata from the document and from any embedded files/figures.
- Anonymize any linked materials (OSF/pre-analysis plan) used during review.

## Comparative-leverage last check

Before the formatting checklist, ask whether the review file still reads like a CPS paper after
anonymization:

| Gate | Pass condition | Bounce risk |
|------|----------------|-------------|
| Comparative claim | The abstract and introduction state what travels across cases, regions, regimes, or time | A single-country result is submitted with only a broad comparative promise |
| Rival explanation | The design names the strongest comparative rival and shows how the evidence adjudicates it | Robustness appears as generic controls, not a debate-specific test |
| Scope condition | The manuscript says where the argument should and should not generalize | The contribution is framed as universal without leverage |
| Evidence-package fit | Supplemental files and replication materials support the comparative claim | Appendices contain unreferenced analyses or non-anonymized materials |

If any gate fails, route back before submission. A perfectly formatted paper can still be returned or
desk-rejected if the comparative contribution is invisible.

## Final checklist

- [ ] Anonymized manuscript + separate title page prepared
- [ ] Word count ≤ 11,000 (references/tables/figures excluded); count reported as required
- [ ] Unstructured ~150-word abstract present
- [ ] APA-style author-date references; every in-text cite has a list entry
- [ ] ORCID for the submitting author linked in SAGE Track
- [ ] Data availability statement included
- [ ] Replication package staged for the CPS Dataverse (quantitative papers)
- [ ] Figures meet SAGE specs (grayscale-safe, vector/high-res); exhibit numbers consistent
- [ ] All claims verified against the live SAGE author-instructions page

## Anti-patterns

- Submitting to the wrong portal or an outdated URL — CPS uses SAGE Track (ScholarOne)
- Identifying info left in the main file or in document/figure metadata
- Over the word limit, or miscounting (forgetting refs/tables/figures are excluded)
- Missing ORCID for the submitting author, or missing the data availability statement
- Structured abstract or wrong citation style (CPS is APA-style author-date)
- Promising replication materials but not staging them — quant final acceptance is gated on the deposit

## Output format

```
【Portal】SAGE Track (ScholarOne) — account ready? [Y/N]
【Anonymized】main file clean + separate title page? [Y/N]
【Length】words / 11,000 (refs/tables/figures excluded)
【Abstract】unstructured ~150 words? [Y/N]
【Comparative leverage visible?】claim + rival + scope condition stated? [Y/N]
【References】APA author-date, in-text=list? [Y/N]
【ORCID】submitting author linked? [Y/N]
【Data availability statement】present? [Y/N]
【Dataverse package】staged (quant)? [Y/N/NA]
【Next】cps-rebuttal (after a decision)
```

## Templates

- [`templates/checklist.md`](templates/checklist.md) — copy-paste submission preflight checklist

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SAGE Track, length, abstract, ORCID, and data-policy facts
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers and anonymization tooling
