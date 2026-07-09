---
name: sigmetrics-camera-ready
description: Use when preparing an accepted ACM SIGMETRICS paper for its POMACS camera-ready, covering de-anonymization, the acmsmall template and POMACS journal metadata (DOI, ORCID, CCS concepts), incorporating the shepherd's required changes without scope creep, permanentizing artifact links, and the ACM artifact-badge handoff.
---

# SIGMETRICS Camera Ready

Use this after acceptance. SIGMETRICS research papers are published as **POMACS journal articles**,
so the camera-ready is a journal production step, and it runs **through shepherding**: an accepted
paper is shepherded to ensure the reviewers' required changes land in the final version. Reopen the
current POMACS author instructions, the shepherd's list, and any artifact-track page before
advising.

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, acknowledgements, funding,
  and the real system and trace names that double-anonymity forced you to hide (the Operational
  Systems Track may already have named them).
- **Apply the final format:** the ACM **acmsmall** single-column template, within the page
  allowance the acceptance/shepherd instructions state.
- **Complete POMACS journal metadata:** title/abstract, author order, ORCIDs, ACM CCS concepts and
  keywords, and the DOI-bearing citation once assigned. Journal metadata errors are harder to fix
  after publication than conference ones.
- **Incorporate the shepherd's required changes** faithfully — the shepherd verifies that specific
  reviewer requests are in the final version — without strengthening claims beyond what was
  evaluated.
- **Permanentize reproducibility:** replace every anonymized artifact link with a public, licensed,
  DOI-issuing archive, and make sure the seeded simulator, proofs, and processed data are the
  reviewed versions.
- **Confirm registration and presentation** obligations; at least one author presents at SIGMETRICS.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| System / tool name | Real name throughout text, figures, artifact | A leftover placeholder in a caption or a plot legend |
| Trace / dataset provenance | Real source named, with access terms | A provenance string still pointing at an anonymizing host |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |

## POMACS production checks

```text
[Template]   acmsmall single-column, current revision; no manual margin/font edits
[Metadata]   title, abstract, authors+ORCID, CCS concepts, keywords all entered and matching PDF
[References] complete, consistent; DOIs where available (references are unlimited pages)
[Figures]    vector where possible; readable in print; analysis-vs-simulation overlays legible
[Proofs]     final proof appendix matches the shepherded theorem statements and assumptions
[Rights]     ACM e-rights/copyright form completed; correct rights statement on the first page
[Links]      every artifact/data link resolves from a logged-out browser
```

## Worked example: incorporating a shepherd's required change

The shepherd required moving an assumption-validity check from a footnote into the model section and
adding the goodness-of-fit figure. Camera-ready move: place the assumption check in the model
section with the QQ-plot, restore the real trace name and its access terms, confirm the theorem
statement and proof appendix still match, and point the artifact link at the now-public DOI archive
— without expanding the bound the reviewers accepted.

## Artifact-badge handoff

Where an artifact track runs, badges are typically pursued around acceptance and are separate from
the shepherded camera-ready. Make the paper's reproducibility statement consistent with the badges
you are pursuing (Available at minimum; Functional/Reusable/Reproduced if the track grants them),
and add any badge acknowledgement only per the current instructions.

## Hedged logistics

- Page allowances, metadata fields, rights-form mechanics, shepherding timelines, and exact
  camera-ready dates change each cycle; confirm against the acceptance email, the shepherd's
  instructions, and current POMACS guidelines rather than a prior year.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / system name / trace provenance / acks / links restored? yes/no
[POMACS metadata] ORCID / CCS / keywords / rights form complete? yes/no
[Shepherd-change map] <required change -> final edit, no scope creep>
[Reproducibility] anonymized links replaced by DOI archive? proofs/simulator final? yes/no
[Remaining owner] <person -> task>
```
