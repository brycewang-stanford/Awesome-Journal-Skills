---
name: sf-submission
description: Use when running the final pre-submission preflight for Social Forces (SF) via ScholarOne Manuscript Central — double-anonymized preparation with a separate title page, the reference-inclusive 10,000-word cap, the 10 tables-and-figure-panels limit, Chicago 17th author-date, the data availability statement, ORCID, and the $50 processing fee. Final checks; it does not draft content.
---

# Submission Preflight (sf-submission)

The last check before pressing submit on **ScholarOne Manuscript Central** (`mc.manuscriptcentral.com/sf`).
SF is **double-anonymized**, so the most common avoidable failures are an under-anonymized manuscript
and a manuscript that misses the **reference-inclusive 10,000-word cap** or the **10-panel** exhibit
limit. Verify volatile specifics on the official page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata ScholarOne expects
- Confirming length, panel count, anonymization, and the data availability statement are all in order

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** UNC Chapel Hill (Dept. of Sociology) / **Oxford University Press**.
- **Portal:** **ScholarOne Manuscript Central** (`mc.manuscriptcentral.com/sf`); Word or .odt.
- **Review model:** **double-anonymized** — anonymize the manuscript; all identifying info on a
  **separate title page**.
- **Length:** **≤ 10,000 words including text, endnotes, and references** (references count).
- **Exhibits:** **≤ 10 tables and figure panels**; supplementary materials **≤ 10 pages**.
- **Style:** **Chicago Manual of Style, 17th ed.** (author-date) required at final submission.
- **Data availability statement:** **required** for publication (see `sf-data-and-transparency`).
- **ORCID:** encouraged for authors at submission.
- **Fee:** **$50 non-refundable** processing fee (**$20** for manuscripts written solely by students);
  **no page charges** (post-acceptance OA APCs apply only if you choose Creative Commons — 待核实 amounts).
  *(Fee/no-page-charges verified 2026-06-22; re-confirm current OUP amounts before payment.)*

## Preflight checklist

### Length & exhibits
- [ ] **≤ 10,000 words including text, endnotes, AND references** (recount with references)
- [ ] **≤ 10 tables and figure panels** total (count multi-panel figures by panel)
- [ ] Supplementary materials ≤ 10 pages
- [ ] Abstract present, in English, **no references** (length 待核实 — ~150-200 words is safe)

### Anonymity (double-anonymized)
- [ ] No author names, affiliations, acknowledgements, or funding details in the manuscript
- [ ] All identifying info on a **separate title page** file
- [ ] No obvious self-references; self-citations neutralized
- [ ] Identifying **file metadata stripped** (document properties)
- [ ] Funding sources entered in the ScholarOne fields (not the manuscript)

### Format & metadata
- [ ] **Chicago 17th author-date** formatting; one consistent citation style
- [ ] ORCID ready for authors
- [ ] Figures/tables self-contained and accessible (see `sf-tables-figures`)

### Compliance & files
- [ ] **Data availability statement** drafted and included
- [ ] Ethics / IRB / consent (incl. consent to publish data) addressed; data anonymized
- [ ] **$50 processing fee** ready ($20 if student-only) — payable by card

## Anti-patterns

- Counting words **without** references and missing the real 10,000-word cap
- Discovering an 11th panel at upload (count panels, not figures)
- Leaving acknowledgements/funding/self-references in the manuscript (breaks anonymity)
- Formatting to ASA or an in-house style instead of Chicago 17th author-date
- Submitting without the required data availability statement
- Budgeting the wrong fee (it is $50 / $20-student, not ASR's $25 or AJS's $30)

## Desk-reject triage before upload

Most avoidable SF declines at the screening stage are format and anonymity failures, not science
failures. Triage in priority order — the first failure a screener sees ends the submission before review:

| Screening check | Pass condition | Fails the desk if… |
|-----------------|----------------|--------------------|
| Word count | ≤ 10,000 incl. text, endnotes, refs | Counted without references, over the real cap |
| Panels | ≤ 10 tables + figure panels combined | An 11th panel hides in a multi-panel figure |
| Anonymity | No names/affil/acks/funding in text | Self-references or metadata leak identity |
| Title page | Separate file holds identifying info | Identity baked into the manuscript file |
| Data statement | Present and concrete | Missing or "available on request" only |

Calibration (hedged): the fee is reported as roughly $50 ($20 student-only), the portal is ScholarOne,
and the style is Chicago 17th author-date — fees, abstract limits, and OA terms are the volatile items
to confirm against current guidelines.

## Worked vignette (illustrative)

A work-and-occupations manuscript looks "ready" at 9,700 words of text. The preflight catches what a
screener catches first: the reference list adds 1,100 words, pushing the true count to 10,800
(illustrative, over cap); a 3-panel figure plus eight tables makes 11 panels; and an acknowledgements
footnote names a grant. Fix: trim citations under 10,000, fold two tables into one for 10 panels, and
move the acknowledgement to the title page. Now it survives.

Referee fixes: "desk-rejected for length" → recount *with* references and endnotes; "anonymity
compromised" → strip file metadata and neutralize self-citations to "Author (year)".

## Output format

```
【Length】≤ 10,000 words INCLUDING references? [Y/N] (count)
【Exhibits】≤ 10 tables + figure panels? supplement ≤ 10pp? [Y/N]
【Anonymized】text + self-refs + metadata clean; title page separate? [Y/N]
【Chicago 17th + ORCID】[Y/N]
【Data availability statement】included? [Y/N]
【Fee】$50 / $20-student ready? [Y/N]
【Next】await decision → sf-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Social Forces URLs behind every fact in this pack
