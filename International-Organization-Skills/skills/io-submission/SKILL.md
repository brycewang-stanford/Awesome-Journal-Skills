---
name: io-submission
description: Use when running the final pre-submission preflight for International Organization (IO) via Editorial Manager — article-type selection, double-blind preparation (third-person self-citation), word caps, separate abstract/word-count/acknowledgments, short author-date footnotes, supplementary material (~20 pages), ORCID, and the Data Availability Statement. Final checks; it does not draft content.
---

# Submission Preflight (io-submission)

The last check before pressing submit on **Editorial Manager**. IO is **double-blind**, so the single
most common avoidable failure is a manuscript that reveals the author through first-person
self-references. Verify volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming the chosen article type's cap is met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** **IO Foundation** / **Cambridge University Press**.
- **Portal:** **Editorial Manager** (confirm the current URL).
- **Review model:** **double-blind** — anonymize the manuscript; provide a separate title page.
- **Article types:** Research Article (**≤ 14,000 words**), Research Note (**≤ 8,000**), Essay
  (**≤ 10,000**). Word limits **include tables, figures, and notes**; **exclude the bibliography**.
- **Abstract / word count / acknowledgments:** submitted **separately** from the manuscript (abstract
  word cap not numerically confirmed — 待核实).
- **Self-citation:** after the title page, **omit identity-revealing self-references**; cite your own
  work in the **third person**.
- **Footnotes / style:** accepted manuscripts use **short author-date footnotes**; consistent style.
- **Supplementary material:** **should rarely exceed twenty pages**, especially at initial submission.
- **ORCID:** required for the **corresponding author**.
- **Data:** **none at initial submission**; requested at **conditional acceptance**; verified by IO
  staff before final acceptance; **Data Availability Statement** before the reference list.
- **Fee:** no submission fee (verified 2026-06-22). Hybrid Cambridge journal; post-acceptance Gold OA is optional — Cambridge 2026 standard APC **£2,610 / US $3,655** plus tax, often covered by institutional agreements or waivers (re-verify the current rate before submission).

## Preflight checklist

### Article type & length
- [ ] Type chosen and its word cap met (Article ≤ 14,000 / Note ≤ 8,000 / Essay ≤ 10,000)
- [ ] Word count **includes tables/figures/notes; excludes bibliography** — recomputed on that basis
- [ ] Abstract, word count, and acknowledgments prepared as **separate** items

### Anonymity (double-blind)
- [ ] No author names, affiliations, or acknowledgments inside the manuscript
- [ ] **Third-person self-citation** after the title page; no "as we showed in…"
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Anonymized pre-analysis plan / OSF link if preregistration is referenced
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Format & metadata
- [ ] Short author-date footnotes; consistent citation style
- [ ] Corresponding-author **ORCID** ready
- [ ] **Data Availability Statement** placed before the reference list
- [ ] Supplementary material within the ~20-page norm; figures/tables self-contained (see `io-tables-figures`)

### Compliance & verification-readiness
- [ ] Ethics / IRB / human-subjects compliance where applicable
- [ ] Original work; preprint status checked against Cambridge preprint policy
- [ ] Reproducibility package + formal-proof appendix **staged** so IO staff can verify after conditional acceptance (see `io-transparency-and-data-policy`)

## Avoidable-rejection triage (catch these before upload)

Some failures are administrative, not intellectual, and IO's double-blind, word-counted process punishes
them disproportionately. Rank your final pass by severity:

| Severity | Failure | Where it bites |
|----------|---------|----------------|
| Fatal | author identity leaks (first-person self-cite, acknowledgments, metadata) | double-blind integrity |
| Fatal | word count omits tables/figures/notes; paper is actually over cap | desk return for length |
| Medium | no Data Availability Statement before the references | transparency-policy gap |

The two fatal rows are the most common avoidable IO rejections; both are caught by a clean-room read of
the anonymized PDF and a recomputed word count.

## Worked preflight vignette (illustrative)

A treaty-compliance study is "ready." The recompute: body 12,400 words, but two dyadic tables and three
figures add ~1,900 word-equivalents and footnotes another ~400, so the true count nears 14,700 — *over*
the 14,000 Research Article cap (figures illustrative; recount on IO's stated basis). The fix is not
prose-trimming alone: move one robustness table and the balance table into supplementary material (within
the ~20-page norm). The clean-room pass then catches "as we showed in Author 2021" — a first-person
self-reference — rewritten in the third person. Only then does it go to Editorial Manager. Confirm every
numeric cap and the current portal against the journal's current submission guidelines before relying on them.

## Anti-patterns

- First-person self-references or author identifiers left in the text/metadata (breaks double-blind)
- Counting words without tables/figures/notes (IO includes them; bibliography is excluded)
- Putting the abstract/acknowledgments inside the manuscript instead of submitting them separately
- Sending a long paper into the Research Note (≤ 8,000) type
- Supplementary material far over ~20 pages at initial submission
- Uploading before a clean-room read of the anonymized PDF (the cheapest catch for the fatal failures)

## Output format

```
【Type】Research Article / Research Note / Essay (cap met? Y/N)
【Anonymized】third-person self-cites + metadata clean? [Y/N]
【Abstract/word-count/acknowledgments separate】[Y/N]
【Word count basis】incl. tables/figures/notes, excl. bibliography? [Y/N]
【Footnotes + ORCID + DAS】[Y/N]
【Repro + proofs staged for verification】[Y/N]
【Next】await decision → io-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official IO URLs behind every fact in this pack
