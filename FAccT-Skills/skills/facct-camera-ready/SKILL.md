---
name: facct-camera-ready
description: Use when preparing an accepted ACM FAccT paper for camera-ready — de-anonymizing and adding the withheld Positionality/Acknowledgements statements, switching to the acmart sigconf proceedings format, ACM metadata (DOI, ORCID, CCS concepts, rights), the two-round camera-ready calendar for Accept vs Revise papers, ACM Open Access, finalizing datasheets/model cards, and integrating required changes without scope creep.
---

# FAccT Camera Ready

Use this after acceptance. FAccT papers are **archival ACM proceedings** (unless you chose
non-archival), so the camera-ready is an ACM production step. Reopen the current camera-ready
instructions, the decision email, and the rights/Open-Access pages before advising — and note the
**two-round calendar**: Round-1 accepts and Revise-and-resubmit accepts have **different**
camera-ready deadlines (FAccT 2026: **24 April** and **11 May** respectively).

## Camera-ready audit

- **De-anonymize completely** and **add the withheld endmatter:** restore the author block,
  affiliations, and now add the **Positionality**, **Acknowledgements**, **Author Contributions**,
  and **Competing Interests** statements that mutual anonymity required you to hold back. The
  Positionality statement in particular exists only from this point on.
- **Switch to the proceedings format:** move from the anonymous `review` build to the acmart
  **`sigconf`** camera-ready, within the current page budget (Revised/accepted papers may use 15
  content pages; confirm).
- **Keep the required Generative AI Usage Statement** accurate for the final manuscript.
- **Complete ACM metadata:** title/abstract, author order, **ORCIDs**, **ACM CCS concepts** and
  keywords, and the DOI-bearing citation once assigned.
- **Integrate reviewer/AC-required changes** faithfully — without strengthening claims beyond what
  was evaluated in the Revise round.
- **Finalize accountability documentation:** replace anonymized artifact links with permanent,
  licensed ones, and align the **datasheet / model card / impact assessment** with the released
  version and the paper's tables.
- **Confirm presentation:** at least one author presents in person (archival or non-archival).

## De-anonymization + endmatter sweep

| Held back / anonymized at submission | Restore or add at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| Positionality statement | **Add now** (it was withheld) | Leaving it out entirely — it is expected here |
| Acknowledgements, funding, Competing Interests | Restored / added | Grant numbers required by funders |
| System / field-site name | Real name throughout text, figures, artifact | A leftover anonymized placeholder in a caption |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Artifact / data link | Public, licensed, persistent archive | The old anonymized URL surviving in a footnote |

## ACM production checks

```text
[Template]   acmart sigconf, current revision; no manual margin/font edits
[Metadata]   title, abstract, authors+ORCID, CCS concepts, keywords entered and matching the PDF
[Rights]     ACM e-rights form completed; correct rights/Open-Access statement on the first page
[Open Access] since 1 Jan 2026 ACM proceedings are 100% OA — confirm ACM Open coverage or the APC
             path (fee-waiver policy 待核实) well before the deadline, not at the last minute
[Endmatter]  Generative AI Usage kept; Positionality/Acks/Contributions added; ethics/adverse-impacts final
[References] complete, consistent; DOIs where available (references are unlimited)
[Links]      every artifact / data-availability link resolves from a logged-out browser
```

## Worked example: integrating a Revise-round fix

The Area Chair required adding disaggregation by an intersectional subgroup and correcting a
doctrinal framing. Camera-ready move: place the new subgroup table in the results with its
uncertainty and the utility trade-off, fix the legal framing and cite the doctrine to its real
origin, add the now-permitted Positionality statement reflecting on the authors' standpoint, and
point the data link at the public, licensed archive with a finalized datasheet — without expanding
the harm claim the reviewers accepted.

## Hedged logistics

- The two camera-ready dates, page allowances, metadata fields, rights mechanics, and the ACM Open /
  APC specifics change each cycle and differ by round; confirm against the decision email and current
  instructions rather than a prior year. APC/fee-waiver details are **待核实**.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[Round] round-1 accept / revise-and-resubmit accept (deadline differs)
[De-anonymization] author block / system name / links restored? yes/no
[Endmatter added] Positionality / Acknowledgements / Contributions present now? yes/no
[ACM metadata] ORCID / CCS / keywords / rights + Open-Access path complete? yes/no
[Reviewer-change map] <required change -> final edit, no scope creep>
[Documentation] datasheet/model card finalized and consistent? yes/no
```
