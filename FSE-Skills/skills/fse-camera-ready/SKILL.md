---
name: fse-camera-ready
description: Use when preparing an accepted ESEC/FSE paper for its PACMSE camera-ready, covering de-anonymization, the ACM Primary Article Template and PACMSE journal metadata (DOI, ORCID, CCS concepts), integrating reviewer-required changes without scope creep, permanentizing the Data Availability links, and the ACM artifact-badge handoff.
---

# FSE Camera Ready

Use this after acceptance. FSE research papers are published as **PACMSE journal articles**, so the
camera-ready is a journal production step, not just a formatting pass. Reopen the current PACMSE
author instructions, the decision email, and the artifact-track and registration pages before
advising.

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, acknowledgements, funding,
  and the real tool and repository names that heavy double-anonymity forced you to hide.
- **Apply the final format:** the ACM Primary Article Template, within the current page budget,
  with the camera-ready allowances the acceptance letter states.
- **Complete PACMSE journal metadata:** title/abstract, author order, ORCIDs, ACM CCS concepts and
  keywords, and the DOI-bearing citation once assigned. Journal metadata errors are harder to fix
  after publication than conference ones.
- **Integrate reviewer-required changes** from the reviews and any Major Revision faithfully —
  without strengthening claims beyond what was evaluated.
- **Permanentize open science:** replace every anonymized artifact link with a public, licensed,
  DOI-issuing archive, and update the Data Availability statement to point at it.
- **Confirm registration and presentation** obligations; at least one author presents.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| Tool / system name | Real name throughout text, figures, artifact | A leftover placeholder name in a caption |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Artifact link | Public archive DOI | The old anonymized URL surviving in a footnote |

## PACMSE production checks

```text
[Template]   ACM Primary Article Template, current revision; no manual margin/font edits
[Metadata]   title, abstract, authors+ORCID, CCS concepts, keywords all entered and matching PDF
[References] complete, consistent; DOIs where available; within the reference-page allowance
[Figures]    vector where possible; readable in print; captions self-contained
[Rights]     ACM e-rights/copyright form completed; correct rights statement on the first page
[Links]      every Data Availability and artifact link resolves from a logged-out browser
```

## Worked example: integrating a Major Revision fix

The reviewers required moving a construct-validity threat from a footnote into the main text and
adding the held-out-project result. Camera-ready move: place the threat in the threats section with
one bounding sentence, add the promised table with its effect sizes, restore the real tool name in
that table, and point the Data Availability statement at the now-public artifact — without
expanding the claim the reviewers accepted.

## Artifact-badge handoff

The camera-ready and the artifact evaluation are separate deadlines. Do not wait for the artifact
result to finalize the paper, but do make the paper's Data Availability statement consistent with
the badges you are pursuing (Available at minimum; Functional/Reusable/Reproduced if the track
grants them). Add the badge acknowledgement only per the current instructions.

## Hedged logistics

- Page allowances, metadata fields, rights-form mechanics, and exact camera-ready dates change each
  cycle; confirm against the decision email and current PACMSE instructions rather than a prior
  year.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / tool name / acks / links restored? yes/no
[PACMSE metadata] ORCID / CCS / keywords / rights form complete? yes/no
[Reviewer-change map] <required change -> final edit, no scope creep>
[Open science] anonymized links replaced by DOI archive? yes/no
[Remaining owner] <person -> task>
```
