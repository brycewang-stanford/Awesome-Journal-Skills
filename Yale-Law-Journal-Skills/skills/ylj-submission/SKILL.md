---
name: ylj-submission
description: Use when running the final pre-submission preflight for The Yale Law Journal (YLJ) via its own online author portal — track selection, anonymization, word/length caps, Bluebook readiness, and required materials. Final checks; it does not draft content.
---

# Submission Preflight (ylj-submission)

The last check before uploading to **YLJ's own online submission system** (not Scholastica/ExpressO).
YLJ review is **anonymized**, so the most common avoidable failure is leaving identity cues in the
manuscript. Verify volatile specifics on the official submissions page before relying on them
(检索于 2026-06；以官网为准).

## When to trigger

- "Submitting this week" — last pass before upload
- Unsure what the YLJ portal expects vs. the rest of your Scholastica slate
- Confirming the track's encouraged caps are met and the piece is anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** The Yale Law Journal Company, Inc., affiliated with Yale Law School;
  **student-edited**, **not peer-reviewed**.
- **Portal:** YLJ's **own online author submission system** — YLJ does **not** accept pieces through
  Scholastica/ExpressO (检索于 2026-06；以官网为准).
- **Review model:** **anonymized** — the Articles & Essays Committee reads without author name,
  affiliation, or prior publications.
- **Tracks & encouraged length (incl. footnotes):** **Article < 25,000 words** (~50 Journal pages);
  **Essay < 15,000 words** (~30 pages); **Forum < 10,000 words** (~20 pages); student **Note** first-time
  cap ~20,000 words; student **Comment** first-time cap ~7,000 words. Over-length weighs against
  acceptance (检索于 2026-06；以官网为准).
- **Style:** **Bluebook** (The Bluebook: A Uniform System of Citation) plus the Journal's own citation
  requirements; quotations need quotation marks + pinpoint cites.
- **Fee:** **no submission fee and no APC** — YLJ takes manuscripts on its own portal with article
  selection by **student editors**; no Scholastica/ExpressO fee attaches to its own intake (verified
  2026-06-22; 以官网为准).
- **Leadership:** led by an **annually-elected student Editor-in-Chief**; the masthead **rotates each
  volume** (current: Volume 135, 2025–2026, EiC **Jeremy N. Thomas '26** — a rotating student role, pinned
  2026-06-23 via Yale Law School news + YBLSA announcement) — **re-check the live masthead** before relying
  on any EiC name.

## Preflight checklist

### Track & length
- [ ] Track chosen; submit as Essay *or* Article to help the Committee assess it
- [ ] Encouraged word cap met (Article < 25k / Essay < 15k / Forum < 10k, incl. footnotes)
- [ ] (Students) Note/Comment first-time cap met (~20k / ~7k)

### Anonymization
- [ ] No author name, affiliation, or acknowledgments in the manuscript
- [ ] No self-identifying references ("as I argued in…") that reveal authorship
- [ ] Prior-publication / prestige cues removed (review is name-blind)
- [ ] File metadata (document properties, comments) stripped of identity

### Apparatus & format
- [ ] Footnotes complete; Bluebook form correct; pinpoints present (see `ylj-sources-and-bluebook`)
- [ ] Quotations marked + pinpointed; paraphrase cited; alterations flagged
- [ ] Manuscript is near-final and source-pull-ready (see `ylj-student-editor-review`)

### Portal & materials
- [ ] Submitting through the **YLJ author portal**, not Scholastica
- [ ] Any abstract/cover info the portal requests prepared
- [ ] Current-volume guidelines PDF or live submissions page checked; date and file/page noted
- [ ] Expedite (if any) filed in the YLJ portal — no queue priority expected (see `ylj-placement-strategy`)

## Gate decision

Classify the submission before upload:

- **STOP** if identity cues remain, file metadata is dirty, the manuscript is materially over the
  encouraged cap without a deliberate reason, or any load-bearing citation fails existence/support.
- **HOLD** if the current-volume guidelines PDF, portal fields, or fee/window status have not been
  checked on the live YLJ page this cycle.
- **GO** only when track, length, anonymization, footnote apparatus, portal path, and expedite handling
  are all confirmed.

Record the evidence packet in a short note: track, word count including footnotes, live guideline page
or PDF checked, anonymization sweep result, cite-check status, and any expedite deadline.

## Anti-patterns

- Sending YLJ through Scholastica/ExpressO and assuming it was received
- Leaving author name/affiliation/acknowledgments or file-metadata identity cues (breaks anonymization)
- Submitting an over-length piece (length weighs against acceptance)
- Uploading with an incomplete footnote apparatus, planning to finish cites later
- Budgeting for a submission fee — YLJ charges none (no submission fee / no APC)

## Output format

```
【Track】Article / Essay / Feature / Note / Comment / Forum (cap met? Y/N)
【Anonymized】text + self-refs + metadata clean? [Y/N]
【Apparatus】Bluebook + pinpoints + quotations marked? [Y/N]
【Portal】submitting via YLJ's own system (not Scholastica)? [Y/N]
【Expedite】filed in YLJ portal (no priority)? [Y/N or N/A]
【Gate】GO / HOLD / STOP — blocker if any
【Evidence】guidelines page/PDF checked + word count incl. footnotes + cite-check status
【Next】await decision → ylj-revision-and-editing on acceptance
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — the printable preflight checklist
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official YLJ portal/length/style facts
