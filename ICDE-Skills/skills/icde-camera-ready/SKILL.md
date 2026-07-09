---
name: icde-camera-ready
description: Use when preparing an accepted IEEE ICDE paper for camera-ready and IEEE Xplore publication: IEEE eCopyright and PDF-eXpress validation, the IEEE double-column final format, integrating required changes without scope creep, final artifact release, registration and presentation, and the TKDE extended-version invitation.
---

# ICDE Camera Ready

Use this after acceptance. Reopen the current edition's camera-ready instructions, the IEEE
author kit, the registration page, and the decision email before advising authors; IEEE
publication mechanics are exacting and edition-specific.

## Camera-ready audit

- Produce the **IEEE Xplore-compliant** final PDF: run the source through **IEEE PDF-eXpress**
  (or the current edition's validator) so fonts are embedded and the file passes Xplore checks.
- Complete the **IEEE eCopyright** form; the copyright notice line must appear on the first page
  exactly as IEEE specifies.
- Apply the final **page limit and IEEE double-column template** without margin or font edits;
  confirm the limit for this edition rather than assuming last year's.
- Because ICDE is **single-blind**, there is **no de-anonymization step** — author names were
  already on the paper. Do confirm the author list, order, and affiliations are final and
  correct for the permanent Xplore record.
- Integrate the reviewer- and area-chair-required changes precisely, without strengthening the
  contribution into something the reviewers never evaluated.
- Release the **final artifact**: the public, licensed repository and data, with the version
  that produced the paper's numbers tagged.
- Confirm **registration** and **in-person presentation** obligations; at least one author
  normally must register and present.

## IEEE publication checklist

| Step | Owner action | Failure if skipped |
|---|---|---|
| PDF-eXpress validation | Run source through the validator; fix font/embedding errors | Xplore rejects the final PDF |
| IEEE eCopyright | Complete the form; place the copyright line on page one | Paper is not published despite acceptance |
| Author list and order | Confirm final names/affiliations for the permanent record | Uncorrectable error in the Xplore citation |
| Required-change integration | Apply each area-chair/reviewer edit precisely | Meta-review promise unmet; possible hold |
| Artifact tag | Publish the licensed repo at the paper's version | Availability claim no longer reproducible |
| Registration + presentation | Register at least one author; confirm in-person slot | Paper withdrawn from proceedings |

## IEEE format reflow

- Switching from the review PDF to the camera-ready template can shift spacing; re-check every
  page break, figure placement, and table width after the flip.
- Wide system diagrams, algorithm listings, and multi-series performance plots often need
  full-column-width or full-page spans; verify nothing is clipped at column boundaries.
- Keep figure, table, algorithm, and theorem numbering identical to the reviewed version so the
  area chair's required-change list still maps onto the final text.
- Adding author blocks and acknowledgements can push content over the limit; budget the space
  before the deadline rather than discovering overflow on submission night.

## Worked example: integrating a required change

The area chair required that the mechanism's memory cost move from the supplement into the main
paper. Camera-ready move: add the cost table (or one summary row) to the evaluation section, one
sentence interpreting the trade, and a pointer to the fuller supplement analysis — without
adding new claims the reviewers did not see.

## The TKDE extended-version path

- Selected best ICDE papers are **invited to submit an extended version to IEEE TKDE**. If your
  paper is invited, treat the journal version as a distinct, longer artifact — not a copy —
  with the additional experiments and formal treatment the conference page budget excluded.
- The separate **TKDE Poster track** is the inverse lane (recently TKDE-accepted articles
  present at ICDE); do not confuse the two when planning.

## Hedged logistics

- Registration pricing, copyright-form mechanics, the PDF-eXpress validator link, and exact
  camera-ready dates change every edition; confirm against the decision email and the current
  author instructions.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF / source / IEEE eCopyright / PDF-eXpress pass / artifact tag>
[Policy checks] <page / author list / presentation / registration / artifact release>
[Required-change map] <reviewer/AC concern -> final edit>
[TKDE path] <invited? y/n -> extended-version plan>
[Remaining owner] <person -> task>
```
