---
name: eurosys-camera-ready
description: Use when converting an accepted EuroSys paper into its ACM proceedings version — flipping acmart out of review/anonymous mode, restoring authors and acknowledgments, completing ACM rights and metadata steps, attaching sysartifacts badges, and meeting the single camera-ready date that serves both the spring and fall cohorts.
---

# EuroSys Camera Ready

Use this after a EuroSys acceptance (direct or via a satisfied revision). EuroSys
proceedings are published by ACM and land in the ACM Digital Library
(`dl.acm.org/conference/eurosys`, confirmed 2026-07-08). For the 2027 edition, a
single camera-ready date around March 5, 2027 was reported for both decision
cohorts — that date comes from a third-party calendar, so treat it as 待核实 and
take the controlling date from the acceptance email and the conference site.

## What changes between acceptance and print

| Dimension | Submission state | Proceedings state |
|---|---|---|
| Template mode | `sigplan,review,anonymous` | `sigplan` final mode per author kit |
| Page 1 identity | Paper ID | Full author block with affiliations |
| Acknowledgments | Forbidden | Restored: funders, grants, shepherd thanks |
| Self-citations | Third person | Natural voice where clearer |
| Artifact links | Anonymized mirrors | Public DOI-backed archive |
| Rights | None | ACM eRights form, CCS concepts, keywords |

Because the template flip changes line breaks and float placement, never assume
the accepted PDF's pagination survives: rebuild, then re-inspect every figure,
table, and listing against the final page allowance in the author kit (the
camera-ready page budget can differ from the 12-page review budget — 待核实 per
edition).

## ACM pipeline specifics

- Complete the ACM eRights form early; the DOI and copyright block it generates
  must be pasted into the source before the final build.
- Supply CCS concepts and keywords through the ACM workflow, not by hand-editing.
- Check ORCID linkage for every author — ACM DL indexing pulls from it.
- Validate the PDF with whatever checker the publication chairs mandate; ACM
  rejects noncompliant PDFs at the production stage, after your deadline.

```bash
# Sanity pass on the final build before upload
pdffonts camera.pdf | awk 'NR>2 && $(NF-2)=="no" {print "UNEMBEDDED:", $1}'
pdfinfo camera.pdf | grep -E 'Pages|Page size'
```

## Reconciling the reviewed and final versions

- Fold in every change the reviews or revision conditions required, and nothing
  that alters the evaluated contribution.
- If the paper went through the one-shot revision path, keep the condition →
  change map from `eurosys-author-response`; publication chairs and shepherds
  (if the edition assigns them — 待核实) may ask for exactly that document.
- Keep section and figure numbering stable where possible so citations of the
  preprint stay meaningful.

## Artifact and badge coupling

Camera-ready is when artifact evaluation results become visible: badges awarded
through the sysartifacts process appear on the published paper. Sequence the
work so the archival DOI (Zenodo or equivalent) exists before the camera-ready
deadline, and cite that DOI — not a mutable GitHub URL — in the availability
section. Details in `eurosys-artifact-evaluation`.

## Metadata coherence sweep

The published record has more surfaces than the PDF; they must agree:

- Title capitalization and author ordering identical across the PDF, the
  eRights form, HotCRP, and the conference program listing.
- Affiliations as they should be archived — institutional name changes and
  authors who moved between submission and print are resolved now or never.
- Abstract in the ACM metadata matches the PDF abstract; DL search indexes
  the metadata, not the PDF.
- The availability/artifact paragraph names the DOI that will actually
  exist at publication time, not the one you intend to mint.
- Funding acknowledgments satisfy every grant's required wording — the
  camera-ready is the version funders audit.

## Final-week sequence

1. Read the acceptance email twice; extract every date, form, and
   shepherd/chair instruction into a checklist with owners.
2. Apply required review changes first, cosmetic polish last — if time
   collapses, compliance survives.
3. Flip the template, rebuild, and re-paginate; fix orphaned floats and
   column overflows introduced by the author block.
4. Run the font-embedding and PDF checks; fix at the source, not with
   post-processing hacks that ACM production will reject.
5. Upload a day early. Publication chairs answer questions before the
   deadline, not after it.

## Presentation logistics

EuroSys 2027 takes place in Rabat, Morocco, in April 2027. Registration
requirements and any in-person presentation obligation for accepted papers are
edition policy — 待核实 on the attendee pages before booking or skipping travel.
Both spring-cohort and fall-cohort papers present at the same April conference.

## Output format

```text
[Camera-ready state] compliant / rebuild needed / blocked on forms
[Template flip] done / pending; pagination re-checked yes/no
[ACM workflow] eRights / DOI block / CCS+keywords / ORCID status
[Review-change ledger] <required change -> where applied>
[Artifact coupling] DOI minted? badge status? availability text final?
[待核实] <camera-ready date, page allowance, shepherding, attendance rule>
```
