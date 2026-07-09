---
name: ipsn-camera-ready
description: Use when preparing an accepted IPSN-lineage paper for camera-ready, covering de-anonymization, the ACM Primary Article Template and the dual ACM/IEEE metadata (CCS concepts, ORCID, DOI, IEEE PDF eXpress/e-copyright), integrating required changes without scope creep, permanentizing dataset/firmware links, and the artifact-award handoff.
---

# IPSN Camera Ready

Use this after acceptance. IPSN papers appeared in **both the ACM Digital Library and IEEE Xplore**,
so the camera-ready has a **two-publisher** flavor: ACM template and metadata plus IEEE production
checks (PDF eXpress, e-copyright). The merged successor publishes regular papers in the **ACM**
proceedings and demos/posters in the **IEEE** proceedings — reopen the current successor author
instructions, the decision email, and the artifact/registration pages before advising.

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, acknowledgements, funding, and
  the real board/testbed/tool names and dataset links that double-blind forced you to hide — and
  restore any lab-logo board photos or scope screenshots you anonymized.
- **Apply the final format:** the ACM Primary Article Template, within the current page budget (IPSN
  2024: ≤12 pp inclusive; successor: verify), two-column 9 pt, with the camera-ready allowances the
  acceptance letter states.
- **Complete the dual metadata:** title/abstract, author order, **ORCIDs**, **ACM CCS concepts** and
  keywords, and the **DOI** once assigned. If the edition also lists in IEEE Xplore, satisfy **IEEE
  PDF eXpress** validation and the **IEEE electronic copyright** form.
- **Integrate required changes** from the reviews faithfully — without strengthening claims beyond
  what was evaluated (no new "state-of-the-art" the reviewers never saw).
- **Permanentize the dataset/firmware:** replace every anonymized link with a public, licensed,
  DOI-issuing archive (Zenodo / IEEE DataPort / figshare), and update the paper's release statement.
- **Confirm registration and presentation:** at least one author presents at CPS-IoT Week.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| Board / testbed / tool names | Real names throughout text, figures, artifact | A leftover placeholder name in a caption |
| Board photos, scope screenshots | Un-blurred with lab context restored | A watermark you forgot to bring back, or one you forgot to remove |
| Dataset / firmware links | Public DOI archive | The old anonymized URL surviving in a footnote |
| Acknowledgements, funding, facilities | Restored | Grant numbers and testbed-facility credits required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |

## Two-publisher production checks

```text
[Template]   ACM Primary Article Template, current revision; two-column 9 pt; no manual margin edits
[ACM metadata] title, abstract, authors+ORCID, CCS concepts, keywords entered and matching the PDF
[IEEE checks]  if listed in Xplore: PDF eXpress validation passed; IEEE e-copyright completed
[References]  complete, consistent, DOIs where available; counted within the inclusive budget
[Figures]     vector where possible; board photos readable in print; captions self-contained
[Rights]      correct ACM (and/or IEEE) rights statement on the first page
[Links]       every dataset/firmware link resolves from a logged-out browser
```

## Worked example: integrating a required change

The reviewers required reporting per-site false-alarm rates instead of a single pooled number and
adding the measured energy conditions. Camera-ready move: add the per-site table, add one sentence
naming the power-measurement instrument and clock, restore the real board name in the setup figure,
and point the release statement at the now-public DOI-archived dataset — without expanding the
detection claim the reviewers accepted.

## Artifact-award handoff

The camera-ready and the artifact evaluation are separate deadlines. Do not wait for the artifact
result to finalize the paper, but do make the paper's release statement consistent with the badges
and the **Best Research Artifact Award** you are pursuing (Available at minimum;
Functional/Reusable/Reproduced if the track grants them). Add any badge acknowledgement only per the
current instructions.

## Hedged logistics

- Page allowances, metadata fields, whether the edition lists in ACM DL, IEEE Xplore, or both,
  rights-form mechanics, and exact camera-ready dates change each cycle and across the merger; confirm
  against the decision email and current successor instructions rather than a prior IPSN year.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / board+testbed names / imagery / links restored? yes/no
[Metadata] ORCID / CCS / keywords / DOI + (IEEE PDF eXpress + e-copyright if applicable) complete? yes/no
[Reviewer-change map] <required change -> final edit, no scope creep>
[Open science] anonymized dataset/firmware links replaced by DOI archive? yes/no
[Remaining owner] <person -> task>
```
