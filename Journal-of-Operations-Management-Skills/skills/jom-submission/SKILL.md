---
name: jom-submission
description: Use when preparing a Journal of Operations Management (JOM) submission for the Wiley Research Exchange (ReX) portal — Department routing, the prescriptive cover-letter naming/recommendation protocol, the mandatory submission checklist, double-anonymization, required disclosures, and formatting/similarity compliance.
---

# Submission Preflight for JOM (jom-submission)

## When to trigger

- The manuscript is written and you are about to submit
- You need to assemble the cover letter, checklist, and disclosures
- You must choose Departments and recommend reviewers
- You are anonymizing files for double-anonymous review

## Where and how

Submit through the **Wiley Research Exchange (ReX)** portal at `wiley.atyponrex.com/journal/JOOM`. There is **no submission fee**; JOM is hybrid open access (subscription publication is free; an APC applies only if you choose CC-BY — amount 待核实, confirm on the Wiley JOM page).

## The cover-letter protocol (prescriptive — do not skip)

JOM's cover letter has unusual, mandatory requirements:

1. **Name 2 Departments, one marked preferred**, from the 12: Healthcare Operations; Innovation and Project Management; Inter-organizational Operations; Intervention Based Research; Operational Systems; Operations Interfaces; Public Policy and Industry Studies; Social Impact; Strategy and Organization; Sustainable Operations; Technology Management; Empirical Research Methods.
2. **Recommend at least 3 Associate Editors and at least 3 Editorial Review Board (ERB) reviewers** who are free of conflicts of interest.
3. **Disclose** any AI use, prior dissertation/conference versions, prior use of the data, and any previous "reject and resubmit" decision on this work.
4. **Justify the similarity score** if overall iThenticate/CrossCheck similarity exceeds 15% (and ensure no single source exceeds ~1% outside quotations).

## The required checklist

A completed **submission checklist** must accompany the manuscript — "Submissions will not be considered in the absence of this checklist." Complete every item before uploading (see `templates/checklist.md`).

## Double-anonymous (asymmetric) anonymization

Review is double-anonymous with an asymmetric rule: author identities are shared with the **Editors-in-Chief and Department Editors** but **not** with reviewers or Associate Editors. Practically: strip author names, affiliations, acknowledgements, and self-identifying citations/file metadata from the manuscript, while supplying full identities in the portal's author fields.

## Format compliance

Double-spaced, single-column, 12-point, one-inch margins, numbered pages, no running headers/footers; **~40-page** guidance (over-long manuscripts are returned for streamlining); **APA** style; Wiley **Data Availability Statement** required for research/synthesis articles; ORCID linked.

## Checklist

- [ ] Submitted via Wiley ReX (JOOM)
- [ ] 2 Departments named, one marked preferred
- [ ] ≥3 Associate Editors and ≥3 ERB reviewers recommended, conflict-free
- [ ] AI / dissertation / prior-data / prior reject-and-resubmit disclosures made
- [ ] Manuscript fully anonymized (names, affiliations, metadata, self-cites)
- [ ] Completed JOM submission checklist attached
- [ ] ~40 pp, double-spaced 12-pt, one-inch margins, APA, no headers/footers
- [ ] Similarity: single-source <1%, overall <15% (or justified in cover letter)
- [ ] Data Availability Statement included; ORCID linked

## Submission-package readiness table

A JOM submission is returned without review if mandatory elements are missing. The map below ties each requirement to its failure mode; verify exact current requirements (APC amount, length guidance, similarity policy) against the Wiley/JOM author pages, as several values change.

| Package element | Requirement | Return/desk-reject if absent |
|-----------------|-------------|-------------------------------|
| Department routing | Name 2 Departments, one preferred | Misrouting or no routing stated |
| Reviewer recommendations | ≥3 AEs and ≥3 ERB reviewers, conflict-free | Cover letter incomplete |
| Disclosures | AI use, prior dissertation/conference, prior data use, prior reject-and-resubmit | Undisclosed prior use surfaces later |
| Submission checklist | Completed and attached | "Not considered in the absence of this checklist" |
| Anonymization | Names, affiliations, metadata, self-cites stripped | Identity leak to AEs/reviewers |
| Similarity | Single-source <1%, overall <15% or justified | Unexplained high similarity |

## Desk-reject and return triggers at the portal

- The mandatory checklist is missing — an automatic non-consideration.
- The cover letter omits the two-Department naming or the reviewer recommendations.
- The manuscript exceeds the ~40-page guidance and reads as un-streamlined.
- Author identity is inferable from un-stripped acknowledgements or file metadata.

## Worked vignette: assembling a clean cover letter

A team submitting an archival operations study marks Inter-organizational Operations preferred and Operational Systems alternate, names three conflict-free AEs and three ERB reviewers, and discloses a prior conference version plus prior, non-overlapping use of the dataset (illustrative). They report an iThenticate score of 12% with no single source above 1%, so no justification paragraph is needed. They confirm double-spaced 12-point with no headers, attach the completed checklist, and include the Wiley Data Availability Statement. That package clears the portal's mechanical gate and routes cleanly to the Department Editor.

## Referee and editor friction points to pre-empt

- *"Routing is unclear"* — state the preferred Department and why the phenomenon fits its mission.
- *"Prior use not disclosed"* — disclose dissertation, conference, and prior-data use proactively; surprises erode editor trust.

## Output format

```
【Portal】Wiley ReX (JOOM)
【Departments】preferred ...; alternate ...
【Reviewer recs】AEs: ...; ERB: ...
【Disclosures】AI/dissertation/prior-data/reject-resubmit ...
【Anonymization】pass/issues
【Checklist attached】yes/no
【Next step】jom-review-process
```

See `templates/cover_letter_template.md` and `templates/checklist.md`.
