---
name: tacas-camera-ready
description: Use when preparing an accepted TACAS (ETAPS) paper for its Springer LNCS camera-ready, covering de-anonymization of a double-blind research paper, the llncs.cls format and LNCS metadata (ORCID, references, the Springer copyright/consent-to-publish form), the gold-open-access CC-BY licensing, integrating reviewer-required changes without scope creep, permanentizing artifact links, and adding earned ETAPS artifact badges to the title page.
---

# TACAS Camera Ready

Use this after acceptance. TACAS papers publish in **Springer LNCS** as a **gold-open-access
(CC-BY)** volume, so the camera-ready is an LNCS production step with a Springer rights form, not
just a formatting pass. Reopen the current LNCS author instructions, the acceptance email, and the
ETAPS/TACAS artifact and registration pages before advising.

## Camera-ready audit

- **De-anonymize (research papers only):** a **regular research** paper was double-blind — restore
  the author block, affiliations, ORCIDs, acknowledgements, funding, and the real tool and
  repository names. A **tool / case-study** paper was single-blind and already named; just confirm
  correctness.
- **Apply the final LNCS format:** `llncs.cls`, within the camera-ready page allowance stated in the
  acceptance letter (references and appendix handled per the current instructions).
- **Complete LNCS metadata:** title/abstract, correct author order with **ORCIDs**, references
  consistent with DOIs where available, and the running head. LNCS metadata errors are harder to fix
  after publication than conference ones.
- **Integrate reviewer-required changes** from the reviews and rebuttal faithfully — without
  strengthening claims beyond what was evaluated (or beyond what the artifact supports).
- **Add earned badges:** if the AEC awarded **Available / Functional / Reusable**, add the badge(s)
  to the **title page** per the current guidelines.
- **Permanentize the artifact:** replace any anonymized or placeholder location with a public,
  licensed, **DOI-issuing** archive (Zenodo/figshare/Software Heritage), and make the paper point at
  it.
- **Complete the Springer rights form:** ETAPS proceedings are gold open access under **CC-BY**;
  submit the consent-to-publish / license form correctly so the paper is released open access with
  copyright retained by the authors.

## De-anonymization sweep (research papers)

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| Tool / system name | Real name throughout text, figures, artifact | A leftover placeholder name in a caption |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Anonymized artifact link | Public DOI archive | The old anonymized URL surviving in a footnote |

(A single-blind tool/case-study paper skips this sweep — it was never anonymized.)

## LNCS production checks

```text
[Template]   llncs.cls, current revision; no manual margin/font edits
[Metadata]   title, abstract, authors + ORCID, running head all entered and matching the PDF
[References] complete, consistent; DOIs where available; per the reference/appendix instructions
[Figures]    vector where possible; readable in print; captions self-contained
[Rights]     Springer consent-to-publish / CC-BY license form completed correctly
[Badges]     earned Available/Functional/Reusable badge(s) placed on the title page
[Links]      every artifact / benchmark link resolves from a logged-out browser
```

## Worked example: integrating a reviewer-required fix

The reviewers required stating the timeout in the benchmark table and adding a validation note for
the soundness claim. Camera-ready move: add the timeout and machine to the table caption, add one
sentence pointing to the witness-validation script, restore the real tool name throughout (research
paper), point the artifact reference at the now-public Zenodo DOI, and add the earned Functional
badge to the title page — without expanding the claim the reviewers accepted.

## Hedged logistics

- Page allowances, metadata fields, the rights-form mechanics, badge placement, and exact
  camera-ready dates change each cycle; confirm against the decision email and current LNCS/ETAPS
  instructions rather than a prior year.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[Category] research (de-anonymize) / tool|case-study (already named)
[De-anonymization] author block / tool name / acks / links restored? yes/na
[LNCS metadata] ORCID / references / running head / rights form complete? yes/no
[Badges] earned badge(s) added to title page? yes/na
[Reviewer-change map] <required change -> final edit, no scope creep>
[Open science] anonymized/placeholder links replaced by DOI archive? yes/no
```
