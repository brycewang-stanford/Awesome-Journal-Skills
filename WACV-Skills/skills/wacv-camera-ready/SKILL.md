---
name: wacv-camera-ready
description: Use when preparing a WACV camera-ready after acceptance, covering de-anonymization, IEEE Xplore plus CVF open-access dual publication, IEEE copyright and PDF checks, the dataset and code release obligation, per-paper registration, and preparing the winter-conference talk or poster once a paper clears Round 1 or Round 2.
---

# WACV Camera-Ready

Use this once a paper is accepted — at Round 1 outright or after the Round 2 decision — to
turn the reviewed submission into the version of record. WACV publishes **dually** (CVF open
access and IEEE Xplore), so camera-ready has both a CVF and an IEEE side. Facts are the WACV
2026/2027 cycles as read on 2026-07-09; confirm the exact camera-ready deadline, page
allowance, and forms on the current Author Guidelines (some items are 待核实).

## From reviewed PDF to version of record

| Step | What changes | Watch for |
|---|---|---|
| De-anonymize | Add author names, affiliations, acknowledgements, funding | Do not also re-break a claim reviewers accepted |
| Incorporate final edits | Fold in required revision changes, fix typos | Stay within the page allowance (待核实 if extra page granted) |
| Add real links | Project page, code repo, dataset now permitted | These were banned at review — add them only now |
| IEEE + CVF forms | IEEE copyright, PDF validation, metadata | Author list and title must match OpenReview exactly |
| Registration | At least one author registers per paper | Miss it and the paper can be pulled |

## De-anonymize carefully

The camera-ready is the first time author identity, acknowledgements, funding, and real
repository links are allowed. Add them — but do not use the de-anonymization pass to quietly
strengthen a claim the reviewers accepted in weaker form; the accepted content is what was
reviewed. Restore only identity and the links that review forbade.

## Dual publication: CVF open access + IEEE Xplore

```text
Where a WACV paper lands after camera-ready:
  CVF open access (openaccess.thecvf.com) → the accepted version, free, with a watermark
  IEEE Xplore                             → the version of record (indexed, citable)
Both come from the same camera-ready package; there is no article-processing charge, and the
conference is funded by registration. Cite the IEEE/CVF WACV proceedings, not an arXiv id.
```

## Honor the release obligation

If a dataset or code was claimed as a contribution, the camera-ready is when it must be
genuinely available: public repository, stated license, and (for datasets) any consent or
collection basis documented. Turn the anonymous review artifact into the public release (see
`wacv-artifact-evaluation`), and make sure the paper's links point to it.

## Prepare the winter presentation

WACV is a **winter conference** (January 2027 window; exact dates/location 待核实). Once
accepted, prepare the assigned format — poster or talk — and plan for the venue and travel.
Because applications work is judged visually, a poster or talk that shows the system working
under its real constraint lands better than one that only reports a table.

## Reverify each cycle

- The camera-ready deadline and whether an extra page over the 8-page body is granted.
- The exact IEEE copyright / PDF validation steps and CVF metadata fields.
- Per-paper registration and in-person vs virtual presentation obligations (待核实).
- The dataset/code public-availability deadline.

## Output format

```text
[De-anonymized] names/affil/acks/funding added; claims unchanged: yes/no
[Links] real repo/project/dataset links added (were banned at review): yes/no
[Forms] IEEE copyright + PDF validation + CVF metadata complete: yes/no
[Release] dataset/code public with license by the obligation: yes/no
[Registration] at least one author registered per paper: yes/no
[Presentation] winter talk/poster prepared for the real-constraint story: yes/no
```
