---
name: jmf-submission
description: Use when running the final pre-submission preflight for the Journal of Marriage and Family (JMF) — format selection (article vs. brief report), double-blind anonymization, page limit, structured abstract, modified APA, bias-free language, data availability statement, and the Wiley Research Exchange portal (migrated from ScholarOne). Final checks; it does not draft content.
---

# Submission Preflight (jmf-submission)

The last check before pressing submit. JMF is **double-blind**, so the single most common avoidable
failure is an under-anonymized manuscript. JMF is also **mid-migration** between submission systems, so
confirm the current portal before you start. Verify volatile specifics on the official pages (待核实).

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata the portal expects
- Confirming the chosen format's limits are met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** NCFR (National Council on Family Relations) / **Wiley**.
- **Portal:** **Wiley Research Exchange** for new submissions (after 25 Jun 2025); **ScholarOne
  Manuscript Central** for earlier submissions — confirm the current link on NCFR's "Submit" page.
- **Review model:** **double-blind anonymous** — anonymize the manuscript; supply author details
  separately as the system requires.
- **Formats:** **Article** (≤ ~35 pages) and **Brief Report** (≤ ~25 pages), including abstract, text,
  tables, and figures (待核实 on exact inclusions).
- **Abstract:** **structured, ~200–225 words** — Objective / Background / Method / Results /
  Conclusion / Implications — included in the main document.
- **Style:** **modified APA**; Microsoft Word, 12-point font; **bias-free language** per APA.
- **Data:** **data availability statement** per Wiley's data-sharing policy; replication-level detail
  (待核实 on the exact tier).
- **ORCID / fees:** ORCID for the corresponding author is standard at Wiley; a submission fee has been
  reported (待核实 — confirm current fee and any open-access APC).

## Preflight checklist

### Format & length
- [ ] Format chosen and its page limit met (Article ≤ ~35 / Brief Report ≤ ~25, incl. tables/figures)
- [ ] **Structured abstract** ~200–225 words with all labeled sections present
- [ ] Modified-APA formatting; Microsoft Word, 12-pt font (confirm current spec)

### Anonymity (double-blind)
- [ ] No author names, affiliations, contact information, or acknowledgements in the manuscript
- [ ] Self-citations to work under review/forthcoming neutralized
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] No identifiable information about participating couples, children, or families

### Data, ethics & files
- [ ] **Data availability statement** drafted (shared / restricted + access path)
- [ ] Replication materials / code staged (OSF/ICPSR/Dataverse) where data terms allow
- [ ] Ethics / IRB / human-subjects protections documented
- [ ] Corresponding-author **ORCID** ready; fee/OA status checked (待核实)

## Anti-patterns

- Leaving author identifiers in the text, acknowledgements, or file metadata (breaks anonymity)
- An unstructured abstract or one outside the word range
- Sending a full study to the Brief Report format (or vice versa) without meeting its limits
- Submitting to the old portal after migration (or assuming a fee that has changed)
- Bias-laden or imprecise language about family forms or identities

## Output format

```
【Format】Article / Brief Report (page limit met? Y/N)
【Anonymized】text + self-refs + file metadata + no identifiable families? [Y/N]
【Structured abstract】~200-225 words, all sections? [Y/N]
【Modified APA + bias-free + Word/12pt】[Y/N]
【Data availability statement + repro materials】[Y/N]
【Portal】Wiley Research Exchange (current link confirmed?) [Y/N]
【Next】await decision → jmf-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JMF/NCFR/Wiley URLs behind every fact in this pack
