---
name: smr-submission
description: Use when running the final Sociological Methods & Research (SMR) pre-submission check for ScholarOne — double-anonymization, separate title page, ASA style, ≤150-word non-parenthetical abstract, data-and-code availability statement, AI disclosure, and file formats. Preflights the submission; does not draft the science.
---

# SMR Submission

Use this immediately before submitting through ScholarOne Manuscripts. Reverify every volatile item on
the live SAGE author page first; portals and policies change.

## Preflight

- Confirm submission goes through **ScholarOne Manuscripts** for SMR; create/log in to the Author
  Center and start a new submission (检索于 2026-06；以官网为准).
- Prepare a **separate title page** and an **anonymized main document** — SMR uses **double-anonymized**
  review, so the main file must carry no author-identifying content.
- Accepted file formats are **Word, LaTeX, or PDF** (检索于 2026-06；以官网为准).
- Citations and references in **ASA** style; dataset references in **DataCite** style.
- **Abstract ≤150 words with no parenthetical citations.**
- Include the **data-and-code availability statement** describing how data, code, and materials can be
  permanently accessed (repository/DOI, access conditions for restricted data).
- Add the **generative-AI disclosure** in the back matter if AI tools were used; if not, none is needed.
- **Fees**: there is **no submission fee** (verified 2026-06-22); open access is optional and paid via
  **Sage Choice** (a figure around **US$3,900 + taxes** surfaced on the SAGE author page — confirm the
  current charge on the live SAGE OA page before quoting).
- **No hard word/length limit** is stated for SMR; treat any circulating "~10,000 words" figure as
  descriptive, not a cap (需复核 on the live author page).
- If submitting a **revision**, respond to each reviewer comment by **copying the comment verbatim and
  replying beneath it**.
- Confirm the **methods-paper completeness**: contribution + derived properties + simulation +
  empirical illustration + released software.

## Final-hour order

1. **Venue facts**: reopen `resources/official-source-map.md` and verify portal, review model, abstract
   limit, citation style, data policy, AI policy, and any fee against live SAGE pages.
2. **Anonymization**: scan the main document, exhibits, code, and PDF metadata for author identity;
   move all identity to the separate title page.
3. **Conformance**: abstract word count and parenthetical-citation check; ASA reference pass; file
   format; figure/table format.
4. **Scientific gate**: read the introduction only — it must state the method contribution, the
   problem it solves, and the evidence types without relying on later sections.
5. **Reproducibility gate**: confirm the availability statement and that the (anonymized) code/scripts
   reproduce the main exhibits.
6. **Administrative gate**: ScholarOne metadata (keywords, ORCID self-link), conflict-of-interest and
   funding declarations, preregistration statement if applicable.

## Worked preflight: a missing-data estimator vignette

Illustrative run on a hypothetical new IPW-plus-imputation estimator paper:

1. Venue facts reopened: review model (double-anonymized), abstract rule, and availability policy
   reverified on live SAGE pages; one wording change noted in the source map.
2. Anonymization: the main PDF's metadata still carried the author name and the code README said
   "developed at [University]." Both stripped; identity moved to the title page.
3. Conformance: abstract is 168 words and contains "(Rubin 1987)" — cut to 147 words and rewritten as
   "Rubin (1987)." ASA reference pass fixes three hand-formatted entries.
4. Scientific gate: the introduction names the incumbent (complete-case / single MI), its failure
   regime (informative missingness), the contribution, and that proofs + simulation + an illustration
   on public survey data support it.
5. Reproducibility gate: the anonymized repository's master script reproduces the grid in a smoke-test
   run; availability statement points to the blinded archive, with the public DOI to be revealed at
   acceptance.
6. Administrative gate: ORCID self-linked, COI and funding declared.

Result after fixes: 147-word non-parenthetical abstract, fully anonymized files, availability statement
present — submit.

## ScholarOne slip list

- Author identity left in the main document, exhibits, code, or PDF metadata under double-anonymized
  review.
- Abstract over 150 words or containing parenthetical citations.
- References not in ASA style; dataset references not in DataCite style.
- Availability statement missing, vague ("available on request"), or deferred to acceptance.
- AI-use undisclosed where generative tools were used.
- Revision response that paraphrases rather than copies each reviewer comment verbatim before replying.
- ScholarOne metadata (keywords, ORCID, COI, funding) inconsistent with the manuscript.

## Output format

```text
[Submission readiness] Ready / Needs fixes / Not ready
[Anonymization] clean / identity found where
[Format checks] <abstract words/parenthetical cites/ASA/file format>
[Reproducibility] availability statement + code reproduce exhibits? yes/no
[Administrative] <ScholarOne metadata / ORCID / COI / funding / AI disclosure>
[Blocking fix] <one issue to resolve first>
```
