---
name: jmf-submission
description: Use when running the final pre-submission preflight for the Journal of Marriage and Family (JMF) — format selection (article vs. brief report), double-blind anonymization, page limit, structured abstract, modified APA, bias-free language, data availability statement, and the Wiley Research Exchange portal (migrated from ScholarOne). Final checks; it does not draft content.
---

# Submission Preflight (jmf-submission)

The last check before pressing submit. JMF is **double-blind**, so the single most common avoidable
failure is an under-anonymized manuscript. New JMF manuscripts have used **Wiley Research Exchange**
since the June 25, 2025 NCFR transition; live-check the current portal link and file requirements
before upload.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata the portal expects
- Confirming the chosen format's limits are met and the manuscript is properly anonymized

## Process facts (live-check operational items on the official page)

- **Owner / publisher:** NCFR (National Council on Family Relations) / **Wiley**.
- **Portal:** **Wiley Research Exchange** for new submissions (after 25 Jun 2025); **ScholarOne
  Manuscript Central** for earlier submissions — confirm the current link on NCFR's "Submit" page.
- **Review model:** **double-blind anonymous** — anonymize the manuscript; supply author details
  separately as the system requires.
- **Formats:** **Article** (≤ ~35 pages) and **Brief Report** (≤ ~25 pages), including abstract, text,
  tables, and figures.
- **Abstract:** **structured, ~200–225 words** — Objective / Background / Method / Results /
  Conclusion / Implications — included in the main document.
- **Style:** **modified APA**; Microsoft Word, 12-point font; **bias-free language** per APA.
- **Data:** **data availability statement** per Wiley's data-sharing policy; replication-level detail
  and shared/restricted data access path.
- **ORCID / fees:** ORCID is common in Wiley workflows; live-check the current portal for required
  identifiers, submission charges, and open-access APC options.

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
- [ ] Corresponding-author **ORCID** ready if required; fee/OA status checked in the live portal

## Desk-handling patterns at JMF (avoid before upload)

| Pattern | Why it stalls at the editor's desk | The fix |
|---------|------------------------------------|---------|
| Author identifiable | Breaks the double-blind model NCFR/Wiley operate; editor cannot send it out | Strip names, affiliations, acknowledgements, funding, and document-property metadata; neutralize self-cites |
| "Family" is incidental | Out of scope for the flagship family-science journal | Re-foreground the family/couple/parent-child contribution or re-route (see `jmf-topic-selection`) |
| Wrong format-to-limit | A full study sent as a Brief Report (or padded into an Article) | Match the contribution to Article vs. Brief Report and meet the page limit incl. tables/figures |
| Abstract unstructured | Reviewers are recruited on the structured abstract | Use Objective/Background/Method/Results/Conclusion/Implications, ~200–225 words |
| No data availability statement | Wiley data-sharing policy expects one | Draft shared/restricted status + access path before upload |
| Stale portal/fee assumption | JMF migrated submission systems mid-2025 | Confirm the live portal and any fee on NCFR's Submit page |

These are anonymization, scope, and format gates that an editor can apply *before* peer review; clearing
them is what converts a desk-screen into a sent-for-review decision.

## Worked micro-example (illustrative)

A longitudinal dyadic paper on marital quality and health is ready to upload. Preflight catches, in order:
(1) the Acknowledgements still thank a named grant and lab — removed and held for the title page; (2)
"as we showed in Smith (2023)" self-identifies the author — neutralized to "prior work has shown"; (3) a
couple's verbatim quote names a town small enough to identify the family — generalized; (4) the abstract
is 240 words and unlabeled — cut to 215 and split into the six structured sections; (5) the manuscript is
38 pages, over the ~35 Article limit — two full robustness tables moved to supplementary materials,
bringing it to 34. Word counts and page counts here are illustrative. Only after these does the data
availability statement and the live portal link get confirmed.

## Referee/editor-facing pitfalls and fixes

- *"Could identify the authors."* Anonymization is not just the byline — funding, IRB-protocol numbers,
  named datasets you uniquely collected, and PDF metadata all leak identity in a double-blind venue.
- *"Could identify participating families."* Generalize town names, employers, and rare family
  configurations so no couple or child is re-identifiable.
- *"Format limit exceeded."* The page cap typically *includes* tables and figures; thin the exhibits or
  move detail to supplements rather than shrinking margins or font.

## Calibration anchors (hedged where uncertain)

- Owner/publisher (NCFR/Wiley), the double-blind model, the structured abstract, and the
  Article/Brief-Report split are stable identity features of JMF; live-check the portal URL, file
  requirements, fee/APC information, and any policy wording before upload.
- Treat every numeric limit in this skill as a default to verify, not a guarantee.

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
