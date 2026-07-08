---
name: corl-camera-ready
description: Use when converting an accepted CoRL paper into its final form — the 9-page camera-ready main text with the extra page for review feedback, the final-mode corl LaTeX template, appendix merged into one PDF, de-anonymization, external hosting for videos because PMLR accepts none, and the October deadline into the PMLR volume.
---

# CoRL Camera-Ready

Acceptance converts the paper from a review object into a permanent PMLR record —
alongside, at CoRL, the *public release of its reviews and rebuttal*. The
camera-ready pass is therefore three jobs: absorb what the review process
demanded, de-anonymize cleanly, and stand up the external artifact surface that
the proceedings pipeline cannot host. The 2026 rules below were read from
corl.org author instructions on 2026-07-08; the deadline was October 12, 2026,
23:59 AoE.

## What changes at camera-ready (2026 cycle)

| Dimension | Submission | Camera-ready |
|---|---|---|
| Main-text pages | 8 (Limitations included) | **9** — the added page exists to accommodate review feedback |
| Template mode | anonymous review mode | `\usepackage[final]{corl_2026}` |
| Identity | double-anonymous | authors, affiliations, acknowledgments restored |
| Appendix | same PDF, optional | included at the **end of the camera-ready PDF**, not a separate file |
| Video | supplementary upload (≤ 250 MB) | **not accepted by PMLR** — host externally, link from the main text / project page |
| Audience | reviewers + AC | permanent open-access record, reviews attached |

## Spend the ninth page on the reviewers' record

The extra page is explicitly tied to review feedback, and your reviews will be
published next to the paper — so the highest-value use is closing the loop
visibly:

1. Reread reviews, rebuttal, and any AC comment; list every commitment you made
   ("we will add the 5-seed table," "we will scope the claim to tasks A–B").
2. Land each commitment in the body and note where — future readers *will* be
   able to diff your promises against the PDF.
3. Typical allocations that pay off: the rebuttal's new results table graduated
   into §5; an expanded Limitations section; the evaluation-protocol detail
   reviewers had to ask for.
4. Resist scope creep: camera-ready is not a second submission. New claims that
   were never reviewed do not belong in the archival version.

## De-anonymization sweep

- Restore the author block, affiliations, funding acknowledgments, and any
  personnel thanks (acknowledgments remain outside the page count).
- Reverse the review-time distancing: "the authors of [12]" becomes "our prior
  work [12]" where that is the honest phrasing.
- Swap anonymized artifact mirrors for the permanent public URLs — and only
  after those URLs exist and are populated (`corl-artifact-evaluation`).
- Scrub leftover review scaffolding: line numbers, draft watermarks, margin
  notes, `\anonymize{}` macros, and the anonymous-repo README inside your ZIPs.

## The external artifact surface (the PMLR no-video rule)

Because PMLR will not carry video — the field's core evidence medium — every
accepted CoRL paper effectively ships a project page. Build it to archival
standards before the PDF freezes:

- De-anonymized overview video (now free of the 250 MB review cap) plus the
  uncut per-task evaluation clips that back your tables.
- Code, checkpoints, and dataset links with the tier declarations from
  `corl-artifact-evaluation`; DOI-stamped archives for anything citable.
- Print durable URLs in the paper — a lab-server link that dies in three years
  takes your evidence with it; prefer organization-level or archival hosting.

```bash
# Final-PDF gate, run on the actual upload candidate
grep -c 'usepackage\[final\]{corl_2026}' main.tex          # exactly 1
pdftotext final.pdf - | head -40                            # author block present & correct
pdftotext final.pdf - | grep -nEi 'anonym|under review|paper #' # expect no hits
pdfinfo final.pdf | grep -i pages                           # 9pp body + refs + appendix merged
pdftotext final.pdf - | grep -oE 'https?://[^ ]+' | sort -u # every URL: live, permanent, deliberate
```

## PMLR metadata discipline

- The proceedings entry (title, author order, affiliations) is generated from
  what you submit to the camera-ready pipeline; a typo here propagates to
  citation indexes for good. Reconcile against every coauthor's preferred name
  form *in writing* before upload.
- Expect the PMLR publication year to postdate the conference for some volumes
  (see `corl-related-work` on the year-offset trap) — your own paper may be
  cited with either year; you cannot control it, but your project page can
  display the canonical BibTeX.
- The CoRL 2026 volume number was not yet assigned at verification time
  (待核实); recent anchors are v270 (2024) and v305 (2025).

## Registration, presentation, and the November venue

- CoRL 2026 runs November 9–12 at the JW Marriott in Austin, Texas (workshop day
  November 9). Registration and presentation obligations for accepted papers —
  who must register, in-person requirements, poster/talk formats — were not
  verified in this pack (待核实): read the acceptance email and the year-site's
  attendance pages as controlling.
- Plan the presentation assets against the public record: your poster and talk
  will be delivered to an audience that can read your reviews.

## Exit checklist

```text
[ ] All rebuttal commitments landed and locatable in the PDF
[ ] 9-page body; Limitations expanded, not amputated
[ ] [final] template mode; identity restored; scaffolding scrubbed
[ ] Appendix merged at end of the single PDF
[ ] Project page live: video, code, data, canonical BibTeX
[ ] Every printed URL durable and populated
[ ] Coauthor sign-off on names/affiliations/order, in writing
[ ] Uploaded before Oct 12 23:59 AoE (2026); confirmation archived
[ ] Registration/attendance obligations confirmed from the acceptance
    email [待核实 in this pack]
```

Camera-ready mechanics are re-issued with each cycle's acceptance emails and at
https://www.corl.org/contributions/instruction-for-authors — that text, not this
snapshot, controls.
