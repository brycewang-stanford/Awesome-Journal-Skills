---
name: govern-submission
description: Use when running the final pre-submission preflight for a Governance: An International Journal of Policy, Administration, and Institutions manuscript on the Wiley submission system — double-blind anonymization plus separate title page, the ≤ 9,000-word cap, ~150-word abstract, the Data Availability Statement, ORCID, and scope self-check. Final checks; it does not draft content.
---

# Submission Preflight (govern-submission)

The last check before pressing submit on the **Wiley submission system**. *Governance* is **double-blind**,
so the single most common avoidable failure is an under-anonymized manuscript — followed closely by a
scope miss (corporate governance or a literature review) that the desk rejects on sight. Verify the
volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata the Wiley portal expects
- Confirming the cap is met, the manuscript is anonymized, and the scope is in remit

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** **Wiley(-Blackwell)**, in association with **IPSA Research Committee 27 —
  Structure & Organization of Government (SOG)**. Founded 1988; quarterly. ISSN 0952-1895 (print) /
  1468-0491 (online).
- **Editors-in-Chief:** **Paolo Graziano (University of Padova) and Adam Sheingate (Johns Hopkins University)** (verified 2026-06-22; re-verify the masthead before submission).
- **Portal:** **Wiley submission system** ("Wiley Authors" / Research Exchange). Older guidance
  references ScholarOne, but Wiley migrated to its new system — **verify the live portal** (检索于
  2026-06；以官网为准).
- **Review model:** **double-blind** — at least two referees review anonymously; anonymize the
  manuscript and provide a **separate title page**.
- **Length:** **≤ 9,000 words excluding citations/bibliography** as the working cap (a third-party
  listing cites 3,000–5,000; treat the official 9,000 as binding, 待核实).
- **Abstract:** **~150 words.**
- **Data Availability Statement:** **required at submission** (states whether replication materials are
  available and how to access them; DOI-citable repository recommended). It is mandatory as a statement
  but not a verified pre-publication reproduction gate (see `govern-transparency-and-data`).
- **Citation style:** author-date style typical for the field; confirm the exact style on the live Wiley/
  journal guidelines (待核实).
- **ORCID:** per Wiley norms for the corresponding author (待核实).
- **Fee:** no submission fee (verified 2026-06-22). Hybrid Wiley journal; Gold OA via Wiley OnlineOpen is optional post-acceptance — confirm the journal-specific APC on the live Wiley OnlineOpen pricing page before choosing open access.

## Preflight checklist

### Scope & length
- [ ] In scope: executive politics / public policy / PA / organization of the state — **not corporate
      governance**, **not a literature review or bibliometric study**
- [ ] Clear, original comparative/institutional intervention stated by the end of the introduction
- [ ] ≤ 9,000 words excluding citations/bibliography; robustness grids in supplementary material
- [ ] Abstract ~150 words, stating question + comparative approach + finding

### Anonymity (double-blind)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] No obvious self-references ("as we showed in…"); self-citations neutralized
- [ ] Identifying **file metadata stripped** (document properties, comments, tracked changes)
- [ ] Anonymized pre-analysis plan / OSF link if preregistration is referenced
- [ ] Separate (non-anonymous) **title page** prepared as a distinct file

### Transparency & format
- [ ] **Data Availability Statement** included and matched to real materials
- [ ] DOI-citable repository (Dataverse/OSF/Zenodo) identified where data/code are shared
- [ ] Author-date citations consistent per the live guidelines
- [ ] Corresponding-author **ORCID** ready
- [ ] Figures/tables self-contained, accessible, grayscale-legible (see `govern-tables-figures`)

### Files & compliance
- [ ] Anonymized manuscript + separate title page + supplementary material staged for the Wiley portal
- [ ] Ethics / IRB / human-subjects compliance addressed where applicable
- [ ] Original work; preprint status checked against Wiley's preprint policy

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks double-blind)
- Submitting a corporate-governance paper or a bare literature review (desk-rejected on scope)
- Abstract well past ~150 words; manuscript over 9,000 words with material that belongs in the supplement
- Omitting the Data Availability Statement (it is required at submission)
- Trusting older ScholarOne references instead of confirming the live Wiley portal

## Output format

```
【Scope】in remit (exec politics / policy / PA / state)? not corporate gov / lit-review? [Y/N]
【Length】≤ 9,000 words excl. citations/bibliography? abstract ~150? [Y/N]
【Anonymized】text + self-refs + file metadata clean; separate title page? [Y/N]
【Data Availability Statement】included + matched to materials? [Y/N]
【Style + ORCID】author-date consistent; ORCID ready? [Y/N]
【Portal】Wiley submission system confirmed live? [Y/N]
【Next】await decision → govern-rebuttal on R&R
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — the concrete pre-submission checklist for the Wiley portal
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repository tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official *Governance*/Wiley URLs behind every fact in this pack
