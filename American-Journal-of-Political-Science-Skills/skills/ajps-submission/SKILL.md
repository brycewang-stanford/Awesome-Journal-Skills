---
name: ajps-submission
description: Use when running the final pre-submission preflight for the American Journal of Political Science (AJPS) via Editorial Manager — submission-type selection, full anonymizing for double-blind review, word/abstract caps, APSA-or-Chicago formatting, the 25-page Supporting Information limit, and human-subjects/IRB documentation. Final checks; it does not draft content.
---

# Submission Preflight (ajps-submission)

The last check before pressing submit on **Editorial Manager** (`editorialmanager.com/ajps`). AJPS is
**double-blind**, so the most common avoidable failure is an under-anonymized manuscript — and AJPS's
anonymizing rules are strict (no acknowledgments, funding lines, or conference mentions, third-person
self-citation). Official AJPS baseline checked 2026-06-20; live-check Editorial Manager prompts before upload.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming the chosen type's cap is met and the manuscript is fully anonymized

## Process facts (official baseline checked 2026-06-20)

- **Owner / publisher:** Midwest Political Science Association (MPSA) / **Wiley**.
- **Portal:** **Editorial Manager** (`http://www.editorialmanager.com/ajps/`).
- **Review model:** **double-blind** — fully anonymize the manuscript.
- **Types:** Article (<= 10,000 words), Research Note (<= 4,000 — methodology/meta-analysis only),
  Correspondence (<= 4,000 — critique of published AJPS work).
- **Abstract:** **<= 150 words** (background, hypotheses, approach, findings, conclusions).
- **Word count:** put it on the **title page** with the abstract; counts **include** main text, notes,
  parenthetical references, print appendices, and **table/figure headers and notes**; **exclude** the
  title page, abstract, reference list, online Supporting Information, and math notation.
- **Style:** **APSA Style Manual** (rev. 2018, updated 2023) **or** **Chicago 18th ed.**; full first +
  last names in references; double-spaced, 12-point, >= one-inch margins.
- **Supporting Information:** **<= 25 pages** for original submissions, uploaded as "Appendix"; anonymized PAPs are separate and do not count against SI pages.
- **Human subjects:** IRB approval/exemption where an author has IRB access, else an appendix answering
  the human-subjects questions; not required when relying on publicly available data approved at
  original collection.
- **Fee:** no submission fee. Wiley OnlineOpen (Gold OA) is optional after acceptance — APC US $4,300 (verified 2026-06-22; re-verify the current rate before submission). Confirm any ORCID, Wiley-license/open-access, or portal-specific prompt during upload/production.

## Preflight checklist

### Type & length
- [ ] Type chosen and its word cap met (Article <= 10,000 / Note or Correspondence <= 4,000)
- [ ] Word count on the **title page** (incl. notes + table/figure headers and notes; excl. refs + SI)
- [ ] Abstract <= 150 words covering background/hypotheses/approach/findings/conclusions

### Anonymity (double-blind)
- [ ] No author names, affiliations, **acknowledgments, funding statements, or conference mentions**
- [ ] **Third-person self-citation** only (no "as we showed...")
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Anonymized response memorandum (for revisions) attached as a PDF to the manuscript

### Files & format
- [ ] One **anonymous manuscript** (PDF / Word / LaTeX)
- [ ] Supporting Information (if any) <= 25 pages, uploaded as "Appendix"; PAP separate if used
- [ ] APSA **or** Chicago 18th style applied consistently; full names in references

### Compliance & reproducibility
- [ ] Human-subjects / IRB documentation ready per the portal's questions
- [ ] Original work; preprint/prior-publication status checked
- [ ] Replication package being staged for the AJPS Dataverse — verified after acceptance
      (see `ajps-replication-and-verification`)

## Desk-reject risk table (avoidable failures at AJPS)

| Trigger | Likely outcome | Preflight fix |
|---------|----------------|---------------|
| Manuscript not anonymized (names, acknowledgments, funding) | Double-blind breach return | Strip identifying text and file metadata |
| Short empirical paper sent as a Research Note | Wrong-type return | Route as an Article; the Note is methodology/meta-analysis only |
| Over the word cap, or SI over 25 pages | Returned to re-fit | Recount with notes/captions; trim SI |

## Worked micro-example (illustrative)

An author readies a survey-experiment Article. Preflight catches a funding acknowledgment in a footnote
(removed), a first-person self-cite "in our 2022 paper" (made third-person), and a word count of 10,250
that omitted exhibit captions — recounted it exceeds 10,000, so one robustness table moves to the SI to land
at ~9,800 *(illustrative)*. The IRB exemption is attached and the replication package staged for the AJPS
Dataverse pending verification.

## Editor-pushback patterns and the venue-specific fix

- *"This reads as a methods Note but is a short empirical paper."* -> Resubmit as an Article; AJPS reserves
  the Note for methodology and meta-analysis.
- *"The manuscript still names the authors."* -> Re-anonymize and strip document properties.

Calibration anchor: AJPS is Wiley-published for the MPSA, uses Editorial Manager, and is double-blind with a
strict anonymizing standard; confirm portal-specific prompts against the live Editorial Manager workflow.

## Anti-patterns

- Leaving acknowledgments, funding lines, conference mentions, or first-person self-cites in the text
- Abstract over 150 words; no word count on the title page
- Sending a short empirical study as a methodology-only Research Note
- Supporting Information over 25 pages on an original submission
- Treating Wiley production/license choices as settled before acceptance

## Output format

```
【Type】Article / Research Note / Correspondence (cap met? Y/N)
【Anonymized】no names/affiliations/acknowledgments/funding/conference; third-person self-cites; metadata clean? [Y/N]
【Abstract】word count (<=150)
【Word count on title page】incl. notes + table/figure captions? [Y/N]
【Style】APSA or Chicago 18th, consistent, full names? [Y/N]
【SI】<= 25 pages? [Y/N/NA]
【IRB】human-subjects documentation ready? [Y/N/NA]
【Next】await decision -> ajps-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymizing, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AJPS URLs behind every fact in this pack
