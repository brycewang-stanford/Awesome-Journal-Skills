---
name: icsme-camera-ready
description: Use when preparing an accepted IEEE ICSME paper for its IEEE Xplore camera-ready, covering de-anonymization, the IEEEtran two-column format and page budget, the IEEE eCopyright form, integrating the reviewer-required and author-response changes without scope creep, permanentizing data-availability links, and the ROSE-Festival artifact handoff.
---

# ICSME Camera Ready

Use this after acceptance. ICSME research papers publish in **IEEE Xplore**, so the camera-ready is
an IEEE production step. There is **no revision round**, so the camera-ready is where you fold in the
changes the reviews and your author response committed to — faithfully, without strengthening claims
the PC did not evaluate. Reopen the current IEEE author instructions, the decision email, and the
ROSE-Festival and registration pages before advising.

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, acknowledgements, funding,
  the real tool and repository names, and the real subject-system names that double-anonymity forced
  you to hide or genericize.
- **Apply the final format:** the IEEEtran two-column conference template, within the page budget
  (2026: 10 + 2 references), with any camera-ready allowance the acceptance letter states.
- **Complete IEEE metadata and rights:** title/abstract, author order and affiliations, the IEEE
  copyright / eCopyright form, and the correct IEEE copyright notice on the first page. Add ORCID and
  index terms/keywords as the template requires.
- **Integrate reviewer-required and author-response changes** faithfully — the clarifications and
  additions you committed to in the rebuttal — without expanding the claim beyond what was evaluated.
- **Permanentize open science:** replace every anonymized artifact link with a public, licensed,
  DOI-issuing archive, and update the data-availability statement to point at it.
- **Confirm registration and presentation** obligations; at least one author registers and presents.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the IEEE Xplore citation |
| Tool / system name | Real name throughout text, figures, artifact | A leftover placeholder name in a caption |
| Own subject-system name (genericized) | Real system name where accurate | A generic descriptor surviving next to a real one |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Artifact link | Public archive DOI | The old anonymized URL surviving in a footnote |

## IEEE Xplore production checks

```text
[Template]   IEEEtran two-column conference, current revision; no manual margin/font edits
[Metadata]   title, abstract, authors+affiliations+ORCID, index terms all entered and matching PDF
[Rights]     IEEE eCopyright completed; correct copyright notice on the first page
[References] complete, consistent; DOIs where available; within the 2 reference pages
[Figures]    vector where possible; readable in two-column print; captions self-contained
[PDF]        IEEE PDF-eXpress / compliance check passed if required by the current instructions
[Links]      every data-availability and artifact link resolves from a logged-out browser
```

## Worked example: folding in an author-response commitment

In the rebuttal you told the PC the held-out-system result was already in Table 3 and promised to
make the construct-validity threat explicit. Camera-ready move: keep Table 3, add one bounding
sentence to the threats section making the proxy limitation explicit, restore the real tool and
system names in that table, and point the data-availability statement at the now-public artifact —
without expanding the claim the PC accepted. Because there was no revision round, the camera-ready is
the first and only place these promised edits actually land.

## Artifact / ROSE handoff

The camera-ready and the ROSE-Festival artifact evaluation are separate deadlines (the artifact
track is shared with SCAM and VISSOFT). Do not wait for the badge result to finalize the paper, but
make the data-availability statement consistent with the IEEE badges you pursue (Open Research
Object at minimum; Research Object Reviewed if the track grants it). Add any badge acknowledgement
only per the current instructions.

## Hedged logistics

- Page allowances, IEEE rights-form mechanics, keyword/index-term requirements, and the exact
  camera-ready date change each cycle; confirm against the decision email and current IEEE
  instructions rather than a prior year. The ICSME 2026 camera-ready date is **待核实** on the access
  date.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / tool name / own-system name / acks / links restored? yes/no
[IEEE metadata] eCopyright / index terms / ORCID complete? yes/no
[Response-change map] <committed change -> final edit, no scope creep>
[Open science] anonymized links replaced by DOI archive? yes/no
[Remaining owner] <person -> task>
```
