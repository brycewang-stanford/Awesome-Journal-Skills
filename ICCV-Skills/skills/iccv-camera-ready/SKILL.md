---
name: iccv-camera-ready
description: Use when an ICCV paper is accepted and the final version, releases, and October conference must be delivered, covering de-anonymization edits, the summer camera-ready window between June decisions and the autumn meeting, CVF open access plus IEEE Xplore publication, arXiv synchronization after the embargo lifts, and presenting at an international venue.
---

# ICCV Camera-Ready

Acceptance at ICCV opens an unusually long runway: decisions landed in late June
2025 and the conference ran October 19–23 in Honolulu, leaving roughly four months
between verdict and podium. The camera-ready deadline sits inside that window
(the exact 2025 date was not fetchable at verification time — 待核实; it is
communicated in the acceptance email and on the conference site). Use the runway
deliberately: most camera-ready damage happens in the first rushed week, and most
release-promise damage in the last.

## The publication pair

An ICCV paper is published through two channels with different jobs:

| Channel | What it is | What depends on it |
|---|---|---|
| CVF open access (openaccess.thecvf.com) | Free public copy of the accepted paper, posted around the conference | What the field actually reads and cites day-to-day |
| IEEE Xplore | Version of record under IEEE co-sponsorship | Institutional/indexing records, some tenure and reporting systems |

No article-processing charge exists in this pipeline; costs run through
registration. There is also no copy editor: the PDF you upload is what both
channels carry forever, so the proofreading pass below is the only one that will
ever happen.

## De-anonymization is a rewrite pass, not a toggle

Work through these in order, then rebuild and re-read the whole paper:

1. Author block, affiliations, and emails restored in the final class mode of the
   author kit.
2. Acknowledgements written for real: grants, compute providers, colleagues —
   everything the double-blind rules banned in March.
3. Self-citations un-contorted where third-person phrasing now misleads.
4. The availability statement upgraded from "code will be made publicly
   available" (the anonymity-era phrasing ICCV 2025 prescribed) to actual URLs —
   repository, model weights, project page. This is the moment links become legal.
5. Every rebuttal promise executed. Diff your rebuttal PDF against the final
   text: each "we will clarify/cite/report X" must correspond to a visible edit,
   because your reviewers are at the poster session in October.

```bash
# Promise-tracking during the camera-ready edit
grep -oiE 'we will [a-z ]+' rebuttal.pdf.txt | sort -u > promises.txt
# ...manually annotate each line with the section where it was honored
awk 'END{print NR" promises to verify"}' promises.txt
pdftotext camera_ready.pdf - | grep -nE '\?\?|Anonymous|under review' | head   # broken refs & leftovers
```

## Numbers that changed since review

Four months is long enough for bug fixes and longer training runs to move your
tables. The integrity rule: reviewed numbers may improve in the final version
only with a footnote saying what changed and why. Silent upgrades between the
version reviewers scored and the version the world reads are how post-publication
integrity threads start — at a venue whose proceedings are permanently public on
CVF open access, the diff is one script away for anyone.

## Synchronizing the public copies

The media embargo ends at acceptance, so the communications sequence inverts:

- Update the arXiv preprint to the camera-ready text once it is frozen; a stale
  arXiv version outranks the official copy in search for months.
- Choose one canonical BibTeX (the proceedings entry, once it exists) and put it
  in the repo README; ICCV papers routinely bleed citations across arXiv/ICCV
  duplicate entries for years.
- Point the project page and repo at the CVF open-access URL when it appears
  around conference time.
- Any press or lab publicity can now cite an *accepted* paper — coordinate it
  with the conference week when attention peaks.

## October in another country

ICCV's venues rotate internationally (Honolulu 2025; Hong Kong announced for
October 2027), which makes presentation logistics part of camera-ready season,
not conference week:

- Registration: confirm the current cycle's rules on paper registration and
  in-person presentation — these were not verifiable for 2025 (待核实) and vary
  across CVF venues; the acceptance email is authoritative.
- Visas: start the moment the decision arrives; some consulate queues are longer
  than the June-to-October gap (planning ledger in `iccv-workflow`).
- Tier deliverables: an oral needs a timed talk plus poster; a Highlight poster
  draws extra traffic and must narrate the paper alone; every poster faces a
  multi-thousand-person hall where one legible headline result beats four dense
  panels.
- Backup presenter: name one when travel is uncertain; a no-show poster helps
  nobody and can breach presentation obligations.

## Final-version defect list

Recurring faults in published CVF-venue PDFs, all catchable in an afternoon:
review-mode line numbers surviving into the final build; `\usepackage[review]`
left on; figures downsampled by a compression pass until the qualitative
comparison is invisible; references still citing arXiv identifiers for papers
long since published (fix per `iccv-related-work`); author-order or affiliation
mismatches between the PDF, OpenReview, and the publisher form — the mismatch
propagates into IEEE Xplore metadata and is painful to correct after indexing.

## Reverify for the current cycle (all 待核实 for 2027)

- Camera-ready deadline, page allowance for the final version, and whether an
  extra page is granted for acknowledgements.
- IEEE copyright form mechanics and PDF validation requirements.
- Registration-per-paper and presentation-mode rules.
- Poster dimensions, talk lengths, and any virtual-platform uploads.

## Output format

```text
[Camera-ready state] runway weeks left: <n>; blockers: <list>
[Promise diff] rebuttal commitments honored: n/m
[Number changes] none / footnoted: <table → reason>
[Links live] repo · weights · project page · availability statement updated
[Public sync] arXiv refreshed · canonical BibTeX set · CVF URL linked
[October plan] registration · visa · tier deliverables · backup presenter
```
