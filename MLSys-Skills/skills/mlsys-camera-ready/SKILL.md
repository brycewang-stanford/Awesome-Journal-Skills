---
name: mlsys-camera-ready
description: Use when preparing an accepted MLSys paper for publication on proceedings.mlsys.org, covering de-anonymization of the research-track PDF, restoring company and repository identity, reconciling promised rebuttal edits, the reserved-ticket registration window for authors, and sequencing camera-ready work against the artifact-evaluation deadline.
---

# MLSys Camera Ready

Use this after an MLSys acceptance. Two things make this venue's post-acceptance phase
unusual: proceedings are published on the conference's own open archive
(proceedings.mlsys.org, no publisher paywall and no APC), and the artifact-evaluation
deadline lands in the same post-notification stretch — in 2026, notifications came
January 25-26 and AE submissions were due March 8, so camera-ready and artifact packaging
compete for the same weeks. Plan them as one project.

## Post-acceptance timeline (2026-cycle anchors)

| Milestone | 2026 anchor | Owner risk |
|---|---|---|
| Notification | January 25-26, 2026 | — |
| Camera-ready deadline | 待核实 — appears in the decision email, not verified on a public page | Missing it silently drops the paper's polish window |
| Artifact submission to AE site | March 8, 2026 | Same people who owe the camera-ready |
| AE review window | March 8 - April 8, 2026 | Authors answer AE questions anonymously |
| Conference | May 18-22, 2026, Bellevue | Speaker travel, visas |

The camera-ready page allowance for accepted papers could not be verified from public
pages (待核实): take limits, forms, and the exact due date from the decision email and the
current author instructions, and treat any remembered number from prior cycles as stale.

## De-anonymization sweep (research track)

The flip from blinded to published touches more than the author block:

- Restore authors, affiliations, acknowledgements, and funding lines, then recheck page
  fit — the added block can push a tight 10-page body over whatever the final limit is.
- Reverse the anonymization rewrites: "the system of [12]" becomes "our earlier system
  X" where that improves clarity; anonymous repository mirrors become the real, licensed,
  citable repository.
- Reinstate the production context the research track forced you to blur — cluster names,
  deployment scale, company identity — exactly where it strengthens claims, and get any
  employer publication-approval done **before** the deadline, not after.
- Verify every URL in the PDF from a logged-out browser: the artifact link in particular
  will be followed by AE reviewers and by readers for years.

```bash
# Confirm no anonymization debris survived the flip
pdftotext camera_ready.pdf - | grep -inE 'anonym|blinded|redacted|under review' | head
# Confirm metadata now identifies the authors intentionally
pdfinfo camera_ready.pdf | grep -iE 'author|title'
```

## Reconciling the review record

- Implement every edit promised in the author response, and keep a private map from
  reviewer concern to the section where the fix landed — program chairs spot-check, and
  the discipline prevents accidental promise-dropping.
- Do not smuggle in new headline results. Numbers may be re-run for polish, but a claim
  the reviewers never saw does not belong in the proceedings version; route genuinely new
  material to the artifact appendix or a follow-up.
- Update the "why now" framing only if reviews demanded it — the LLM-systems literature
  moves fast enough that intros rot in three months, but rewriting the story post-
  acceptance risks inconsistency with what was evaluated.

## Camera-ready package checklist

- Final PDF built from the official style kit in its accepted-paper mode.
- Source files if the instructions require them (待核实 per cycle).
- Abstract and title in the conference system matching the PDF exactly — these feed the
  proceedings page and the schedule.
- Artifact Appendix aligned with the AE submission, so the paper's pointers and the
  evaluated artifact do not diverge.
- Whatever copyright or release form the decision email specifies (待核实; MLSys's own
  proceedings model means this may be lighter than ACM/IEEE norms — read, don't assume).

## Proceedings metadata and long-term findability

proceedings.mlsys.org is the paper's permanent address; its metadata is generated from
what you submit, so errors fossilize:

- Author name forms: agree the canonical spelling (diacritics, middle initials) across
  all authors before submission — proceedings pages, DBLP scraping, and citation
  managers will propagate whatever lands there.
- The abstract on the proceedings page is what most future readers see before deciding
  to click; re-read it as a standalone advertisement after de-anonymization, since
  blinding sometimes left it vaguer than it needs to be.
- Put the artifact repository URL and badge status in the paper's stated location
  (footnote or dedicated section per the current instructions) so the proceedings PDF
  and the badge record reinforce each other.
- If you also maintain an arXiv version, update it to the camera-ready after publication
  and add the proceedings reference — divergent public versions of an MLSys paper
  confuse the exact readers (practitioners) the venue reaches best.

## Talk and poster preparation

- MLSys audiences mix researchers with practitioners who may adopt the system that
  week; open the talk with the measured bottleneck and the mechanism, compress related
  work to one slide, and end with the artifact link and badge status.
- Prepare the demo-or-plot fallback: sessions run tight, and a talk that depends on a
  live cluster fails in predictable ways. Pre-record anything that touches a network.
- Poster sessions at this venue turn into whiteboard debugging conversations; bring the
  architecture diagram and the ablation table, not sixteen result plots.

## Registration and presentation logistics

- Verified: authors of accepted papers get a two-week window of access to reserved
  registration tickets (mlsys.org registration FAQ), protecting them if the conference
  sells out — but the window expires, so register inside it.
- Whether at least one author must present in person, and any remote-presentation
  fallback, could not be verified for 2026 (待核实) — confirm from the decision email
  before anyone declines travel.
- Prepare the talk/poster against the conference's published session format; MLSys mixes
  academic and industry audiences, so lead the talk with the measured bottleneck, not
  related work.
- Visa timelines are the silent killer for a late-May US conference with late-January
  notification; the presenting author's travel paperwork starts the week of acceptance,
  and a backup presenter is named at the same time.
- Budget the trip against the venue's hotel block early — the 2026 edition ran in a
  single conference hotel (Hyatt Regency Bellevue), where blocks sell out before
  camera-ready season ends.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Deadline sources] <decision email items confirmed: due date / page limit / forms>
[De-anonymization sweep] <author block/URLs/acknowledgements/approval status>
[Reviewer-promise map] <concern -> section where fixed>
[AE collision plan] <who does camera-ready vs artifact, and when>
[Registration] <reserved-window deadline + who registers>
```
