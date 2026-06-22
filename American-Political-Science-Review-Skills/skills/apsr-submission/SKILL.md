---
name: apsr-submission
description: Use when running the final pre-submission preflight for the American Political Science Review (APSR) via Editorial Manager — track selection, double-anonymous preparation, word/abstract caps, APSA-style formatting, ORCID, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (apsr-submission)

The last check before pressing submit on **Editorial Manager**. APSR is **double-anonymous**, so the
single most common avoidable failure is an under-anonymized manuscript. Verify volatile specifics on
the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming the chosen track's caps are met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** American Political Science Association (APSA) / Cambridge University Press.
- **Portal:** **Editorial Manager** (`editorialmanager.com/apsr`).
- **Review model:** **double-anonymous** — anonymize the manuscript; provide a separate title page.
- **Tracks:** Regular Article (< 11,000 words), Research Note (< 7,000 words — see 待核实 on the exact
  cap), Replications and Reappraisals, Syntheses, Registered Reports.
- **Abstract:** **≤ 150 words.**
- **Word count:** put it on the **front page**; counts **include tables, figures, and printed
  footnotes**, **exclude** the reference list and online appendices.
- **Style:** **APSA Style Manual for Political Science** (author-date).
- **ORCID:** required for the **corresponding author** (submissions after 1 Jan 2019).
- **Fee:** no submission fee and no APSA-membership requirement (verified 2026-06-22). Hybrid Cambridge journal; post-acceptance Gold OA APC is optional — Cambridge 2026 standard **£2,610 / US $3,655** plus tax (re-verify the current rate before submission).

## Preflight checklist

### Track & length
- [ ] Track chosen and its word cap met (Article < 11,000 / Note < 7,000)
- [ ] Word count on the front page (includes tables/figures/footnotes; excludes refs + appendix)
- [ ] Abstract ≤ 150 words, states question + approach + finding

### Anonymity (double-anonymous)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] No obvious self-references ("as we showed in…"); self-citations neutralized
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Anonymized pre-analysis plan / OSF link if preregistration is referenced
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Format & metadata
- [ ] APSA Style Manual formatting; consistent author-date citations
- [ ] Corresponding-author **ORCID** ready
- [ ] Figures/tables self-contained, accessible (see `apsr-tables-figures`)

### Compliance & files
- [ ] Ethics / IRB / human-subjects compliance per APSA principles
- [ ] Original work; preprint status checked against Cambridge preprint policy
- [ ] Reproducibility package staged for the APSR Dataverse at conditional acceptance
      (see `apsr-transparency-and-data-policy`)

## Anti-patterns

- Leaving author identifiers in the text, acknowledgments, or file metadata (breaks anonymity)
- Abstract over 150 words; no word count on the front page
- Sending a long paper to the Research Note track
- Choosing Registered Reports after results exist
- Budgeting for a submission fee that is not charged (none as of 2026-06-22; only optional post-acceptance Gold OA APC)

## Output format

```
【Track】Article / Note / Replication / Synthesis / Registered Report (caps met? Y/N)
【Anonymized】text + self-refs + file metadata clean? [Y/N]
【Abstract】word count (≤150)
【Word count on front page】incl. tables/figures/footnotes? [Y/N]
【APSA style + ORCID】[Y/N]
【Repro package】staged for APSR Dataverse? [Y/N]
【Next】await decision → apsr-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official APSR URLs behind every fact in this pack
