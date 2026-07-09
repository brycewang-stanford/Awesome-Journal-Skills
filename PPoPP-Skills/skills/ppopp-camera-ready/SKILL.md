---
name: ppopp-camera-ready
description: Use when preparing a PPoPP camera-ready, covering systematic de-anonymization, ACM rights/eRights and CCS concepts metadata, restoring the named hardware and acknowledgements, permanentizing the artifact DOI and any earned badges, and passing ACM production checks for the two-column acmart sigplan proceedings.
---

# PPoPP Camera-Ready

Prepare the final version after acceptance (PPoPP 2026: final paper due 9 January 2026). The
camera-ready converts an anonymized submission into an archival ACM proceedings paper in the
**two-column `acmart` `sigplan`** format. It is **separate from the artifact-evaluation deadline**;
do not let one slip because you were focused on the other. Work through de-anonymization, ACM
metadata, and production checks methodically — a rushed camera-ready is where identity leaks and
rights errors happen.

## De-anonymize systematically

The submission hid identity in several places; restore them all, deliberately:

```text
[Authors]        real names, affiliations, ORCIDs, contact author
[Machines]       restore the named cluster/supercomputer/GPU facility you abstracted for review
[Acknowledgements] funding, grant numbers, facility allocations, collaborators
[Self-citation]  switch "prior work [12]" back to "our prior work [12]" where accurate
[System names]   restore the real name of your runtime/library/tool
[Artifact links] replace the anonymized artifact link with the public DOI archive
```

Do a reverse pass of the double-blind sweep you ran at submission: every place you *removed*
identity now gets it back, and nowhere is left half-anonymized.

## ACM rights and metadata

- Complete the **ACM eRights** process; paste the returned **rights block, DOI, and conference
  citation** into the `acmart` preamble exactly as issued.
- Set `\documentclass[sigplan,...]{acmart}` per the current author kit; do not switch document
  class or column format at camera-ready.
- Fill **CCS Concepts** and **keywords** — required ACM metadata that also feeds indexing; choose
  concepts under computing methodologies / parallel computing that match your contribution.
- Confirm the paper title, author order, and abstract match what was accepted; late changes need
  chair approval.

## Artifact and badges

- If the artifact earned badges (Functional/Reusable and/or Results Reproduced), add the **ACM badge
  images** the AE chairs specify and cite the archived artifact.
- Add the **Artifacts Available** badge if you deposited the artifact and received the
  publisher-granted green badge from your DOI link.
- Replace every anonymized/placeholder link with the **permanent DOI** (Zenodo/figshare/Software
  Heritage); a personal GitHub URL is not archival and may rot before the proceedings do.
- Verify the paper's Data/Artifact Availability statement points at the final DOI, not a review-time
  placeholder.

## Production checks for the two-column proceedings

```text
[Class]        acmart sigplan, current kit revision; no manual margin/font overrides
[Fonts]        all embedded; check with pdffonts
[Figures]      vector where possible; speedup curves legible at print size; no column overflow
[Color]        readable in grayscale (many proceedings print/copy in B&W); don't encode data by hue alone
[References]   full author lists (no "et al."); DOIs present; ACM reference format
[Metadata]     rights block, DOI, CCS concepts, keywords, ORCIDs all filled
[Page count]   within the camera-ready limit (the extra page some venues grant is cycle-specific — confirm)
```

## Common camera-ready failures

- **Half de-anonymized** — real authors but a still-abstracted "an anonymous cluster," or a
  self-citation left in third person.
- **Placeholder artifact link** shipped to the archive — the anonymized URL never swapped for the
  DOI.
- **Wrong `acmart` mode** — switching away from `sigplan` two-column, or overriding the template.
- **Rights block mismatch** — DOI or conference string not the one ACM eRights issued.
- **Grayscale-illegible plots** — speedup lines distinguished only by color.

## Calibration

- Confirm the exact camera-ready page limit and whether an extra page is granted this cycle.
- Confirm the current ACM author-kit `acmart` revision and the badge-image requirements with the AE
  chairs.
- Keep the AE deadline and the camera-ready deadline on separate calendar entries.

## Output format

```text
[De-anon] authors/machines/acks/self-cites/system-names/artifact-link all restored? yes/no
[ACM metadata] rights block + DOI + CCS + keywords + ORCIDs filled? yes/no
[Artifact] DOI permanent, badges added as earned (incl. Available)? yes/no
[Production] acmart sigplan, fonts embedded, grayscale-legible, refs full, within page limit? yes/no
[Blockers] <ordered list before the camera-ready deadline>
```
