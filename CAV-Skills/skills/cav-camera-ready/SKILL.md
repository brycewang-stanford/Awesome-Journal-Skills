---
name: cav-camera-ready
description: Use when preparing an accepted CAV (Computer Aided Verification) paper for its Springer LNCS open-access camera-ready, covering de-anonymization for the previously double-blind categories, the LNCS llncs template and Springer metadata (ORCID, author order, running heads), the copyright/open-access forms, integrating reviewer-required changes without scope creep, permanentizing artifact links, and the AEC badge handoff.
---

# CAV Camera Ready

Use this after acceptance. CAV papers are published **open access as Springer LNCS chapters**, so the
camera-ready is a Springer production step with its own metadata and rights forms. Reopen the current
LNCS author instructions, the decision email, and the artifact-track page before advising.

## Camera-ready audit

- **De-anonymize (Regular and Application papers):** restore the author block, affiliations,
  acknowledgements, funding, and the real tool/solver and repository names that double-blind review
  forced you to hide. (Tool and Industrial papers were never anonymized.)
- **Apply the final LNCS format:** the `llncs` document class, within the category page allowance and
  any camera-ready extension the acceptance letter grants, with correct running heads and the
  Springer copyright line.
- **Complete Springer LNCS metadata:** title/abstract, author order and ORCIDs, corresponding author,
  affiliations, and keywords — entered in the Springer system and matching the PDF exactly. Metadata
  errors are harder to fix after the volume is published than formatting ones.
- **Integrate reviewer-required changes** faithfully — the scoping edits and added clarifications the
  reviews and rebuttal committed to — without strengthening claims beyond what was evaluated.
- **Permanentize the artifact/open-science links:** replace any anonymized artifact link with a
  public, licensed, DOI-issuing archive, and make the paper's availability statement point at it.
- **Complete the open-access / copyright forms:** CAV proceedings are open access, so confirm the
  correct license and the open-access consent/rights form for the volume.

## De-anonymization sweep (anonymized categories)

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the LNCS citation and DOI metadata |
| Tool / solver / prover name | Real name throughout text, figures, artifact | A leftover anonymized name in a caption or a benchmark path |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Artifact / repository link | Public archive DOI + tool homepage | The old anonymized URL surviving in a footnote |

## LNCS production checks

```text
[Template]   llncs document class, current revision; correct running heads; no manual margin edits
[Metadata]   title, abstract, authors+ORCID, affiliations, corresponding author, keywords entered
             in the Springer system and matching the PDF
[References] complete, consistent; DOIs where available; venue strings correct (do not misattribute
             a TACAS/FMCAD paper to CAV)
[Figures]    vector where possible; cactus/scatter plots readable in print; captions self-contained
[Rights]     Springer open-access consent-to-publish / copyright form completed for the volume
[Links]      every artifact and availability link resolves from a logged-out browser
```

## Worked example: integrating a rebuttal commitment

The reviews required scoping the generality claim to the supported theory and moving a lemma's full
proof into the paper. Camera-ready move: narrow the claim sentence to the theory actually covered,
promote the lemma proof from the appendix into the correctness section (space permitting) or keep it
clearly in the appendix with a body pointer, restore the real tool name in the benchmark tables, and
point the availability statement at the now-public DOI archive — without expanding the claim the PC
accepted.

## Artifact-badge handoff

The camera-ready and the AEC evaluation are separate deadlines, and the badge outcome may arrive
after the camera-ready is due. Do not block the paper on the badge; but make the paper's availability
statement consistent with the badges you are pursuing (Available at minimum; Functional/Reusable if
granted), and add any badge acknowledgement only per the current LNCS/AEC instructions.

## Hedged logistics

- Page allowances, metadata fields, the open-access rights mechanics, and exact camera-ready dates
  change each cycle; confirm against the decision email and current Springer LNCS instructions rather
  than a prior year (camera-ready date for 2026 is **待核实**).

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / tool name / acks / links restored (if applicable)? yes/no
[LNCS metadata] ORCID / author order / affiliations / keywords / rights form complete? yes/no
[Reviewer-change map] <required change -> final edit, no scope creep>
[Open science] anonymized links replaced by DOI archive? availability statement updated? yes/no
[Remaining owner] <person -> task>
```
