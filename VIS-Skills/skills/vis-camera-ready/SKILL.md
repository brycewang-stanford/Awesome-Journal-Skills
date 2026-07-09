---
name: vis-camera-ready
description: Use when preparing an accepted IEEE VIS paper for its IEEE TVCG camera-ready, covering de-anonymization, the VGTC/TVCG template and journal metadata (DOI, ORCID, IEEE keywords/index terms), integrating the second-round required changes without scope creep, permanentizing open-materials links, the Open Practices disclosure form, and the Graphics Replicability Stamp handoff.
---

# VIS Camera Ready

Use this after acceptance. IEEE VIS full papers are published as **IEEE TVCG journal articles**, so
the camera-ready is a journal production step, not just a formatting pass. Reopen the current TVCG
author instructions, the "Final Information for Paper Authors" page, and the Open Practices form
before advising.

## Camera-ready audit

- **De-anonymize completely (if you submitted double-blind):** restore the author block,
  affiliations, ORCIDs, acknowledgements, funding, and the real **system, tool, and repository
  names** the anonymization hid.
- **Apply the final format:** the VGTC / TVCG-conference template within the page budget (9 pages of
  content + up to 2 reference/acknowledgement pages), with the camera-ready allowances the
  acceptance letter states.
- **Complete TVCG journal metadata:** title/abstract, author order, ORCIDs, IEEE keywords / index
  terms, and the DOI-bearing citation once assigned. Journal metadata errors are harder to fix after
  publication than conference ones.
- **Integrate the second-round required changes** faithfully — without strengthening claims beyond
  what the reviewers evaluated.
- **Permanentize open materials:** replace every anonymized code/data/video link with a public,
  licensed, archival location (OSF, Zenodo, a tagged release), and make the paper point at it.
- **Complete the Open Practices form** (preprint, preregistration, open data/code, supplemental
  disclosures) that accepted authors fill in at camera-ready.
- **Confirm presentation obligations;** at least one author presents at the conference.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| System / technique name | Real name throughout text, figures, video, repo | A leftover placeholder name in a caption or the video |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Supplemental video | Re-render with real title/affiliation slate | The anonymized voice-over or blurred logo surviving |
| Code/data link | Public archival DOI (OSF/Zenodo) | The old anonymized URL surviving in a footnote |

## TVCG production checks

```text
[Template]   VGTC / TVCG-conference template, current revision; no manual margin/font edits
[Metadata]   title, abstract, authors+ORCID, IEEE keywords/index terms entered and matching PDF
[References] complete, consistent; DOIs where available; within the 2-page reference allowance
[Figures]    vector where possible; readable in print and grayscale; CVD-safe palettes; captions self-contained
[Rights]     IEEE copyright/eCF form completed; correct rights statement on the first page
[Links]      every open-materials and video link resolves from a logged-out browser
[Video]      supplemental video re-rendered, de-anonymized, correct codec/length
```

## Worked example: integrating a second-round required change

The reviewers required adding the perceptual pilot and rewriting the encoding rationale.
Camera-ready move: place the pilot's result with its effect size and CI in the evaluation section,
revise §4 so each visual channel is tied to a task, restore the real system name in the figures and
the video, and point the open-materials statement at the now-public OSF archive — without expanding
the claim the reviewers accepted.

## Replicability-Stamp and Open Practices handoff

The camera-ready and the **Graphics Replicability Stamp** review are separate tracks. Do not wait
for the stamp result to finalize the paper, but do make the paper's open-materials statement
consistent with what you are submitting to GRSI, and complete the Open Practices disclosures
honestly. The stamp is earned by an independent volunteer reproducing your code/data, so the public
archive must be the exact, runnable version the paper describes.

## Hedged logistics

- Page allowances, metadata fields, the IEEE rights-form mechanics, and exact camera-ready dates
  change each cycle; confirm against the decision email and current TVCG instructions rather than a
  prior year.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / system name / acks / links / video restored? yes/no
[TVCG metadata] ORCID / IEEE keywords / rights form complete? yes/no
[Required-change map] <second-round change -> final edit, no scope creep>
[Open practices] anonymized links replaced by archival DOI? disclosure form done? yes/no
[Remaining owner] <person -> task>
```
