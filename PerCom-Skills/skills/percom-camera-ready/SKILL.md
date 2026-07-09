---
name: percom-camera-ready
description: Use when preparing an accepted IEEE PerCom paper for its IEEE Xplore camera-ready, covering de-anonymization, the IEEEtran compsocconf template and page budget, IEEE Xplore metadata (PDF eXpress, eCopyright, ORCID, index terms), integrating reviewer-required changes without scope creep, permanentizing the dataset links, and IEEE production checks.
---

# PerCom Camera Ready

Use this after acceptance. PerCom papers publish in **IEEE Xplore**, so the camera-ready is an
**IEEE production step** with its own machinery — PDF eXpress compliance and the IEEE electronic
copyright (eCopyright) form — not just a formatting pass. Reopen the current camera-ready
instructions, the decision email, and the registration/presentation pages before advising.

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, ORCIDs, acknowledgements,
  funding, and the real testbed/system/dataset names that double-blind review forced you to hide.
- **Apply the final format:** IEEEtran `\documentclass[10pt, conference, compsocconf]{IEEEtran}`,
  within the current page budget (9+1) plus any camera-ready allowance the acceptance letter states.
- **Complete IEEE Xplore metadata:** title/abstract, author order and ORCIDs, and **IEEE index
  terms / keywords** (and ACM CCS concepts if requested). Journal-grade metadata errors are harder
  to fix after publication than they look.
- **Pass PDF eXpress:** validate the final PDF through IEEE PDF eXpress for Xplore-compatible fonts
  and embedding; a PDF that fails eXpress will not be accepted for the proceedings.
- **Complete the IEEE eCopyright form:** the correct copyright/rights statement must appear on the
  first page as the form dictates.
- **Integrate reviewer-required changes** faithfully — without strengthening claims beyond what was
  evaluated in the (single-round) review.
- **Permanentize open data:** replace every anonymized dataset/code link with a public, licensed,
  DOI-issuing archive, and update the availability statement to point at it.
- **Confirm registration and in-person presentation:** at least one author registers and presents;
  remote/pre-recorded presentation is not permitted except in stated special circumstances.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| Testbed / system / dataset name | Real name throughout text, figures, dataset | A leftover placeholder in a caption or figure |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Dataset/code link | Public archive DOI (IEEE DataPort / Zenodo) | The old anonymized URL surviving in a footnote |
| Sensor-rig / deployment photos | Real photos if desired | A face or building that needs consent to publish |

## IEEE Xplore production checks

```text
[Template]   IEEEtran compsocconf, current revision; no manual margin/font edits; 10pt two-column
[Metadata]   title, abstract, authors+ORCID, index terms/keywords entered and matching the PDF
[PDF eXpress] final PDF validated and Xplore-compatible (fonts embedded)
[eCopyright]  IEEE electronic copyright form completed; correct rights line on the first page
[References] complete, consistent; DOIs where available; within the 1 reference page
[Figures]    vector where possible; readable in print greyscale; captions self-contained
[Links]      every dataset/code link resolves from a logged-out browser
```

## Worked example: integrating a rebuttal-driven clarification

The reviewers asked you to make the cross-subject nature of the headline result explicit. Camera-
ready move: reorder §4.1 so the leave-one-subject-out F1 leads and the pooled number is clearly
secondary, restore the real system name in that table, point the availability statement at the
now-public IEEE DataPort dataset, and add the ORCID and index terms — **without** expanding the
claim beyond what the single review round evaluated.

## Dataset-release handoff

The camera-ready and any dataset/artifact deposit are related but separate tasks. Do not let the
paper's availability statement promise more than the public dataset delivers: align the statement
with what you actually deposit (a de-identified dataset under an open license with a DOI), and note
honestly anything (raw video, re-identifiable traces) that stays restricted and why
(`percom-reproducibility`, `percom-artifact-evaluation`).

## Hedged logistics

- Page allowances, metadata fields, PDF eXpress and eCopyright mechanics, and exact camera-ready
  dates change each cycle; confirm against the decision email and current instructions rather than a
  prior year. Whether a reproducibility-badge track runs is **待核实** per edition.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / system name / acks / links restored? yes/no
[IEEE metadata] ORCID / index terms / eCopyright / PDF eXpress passed? yes/no
[Reviewer-change map] <required change -> final edit, no scope creep>
[Open data] anonymized links replaced by DOI archive? yes/no
[Remaining owner] <person -> task>
```
