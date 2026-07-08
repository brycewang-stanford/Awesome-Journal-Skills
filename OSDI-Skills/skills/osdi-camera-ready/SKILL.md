---
name: osdi-camera-ready
description: Use when converting an OSDI acceptance into the published paper — the June final-paper deadline, expansion to 14 pages plus appendices, the two-page Artifact Appendix, de-anonymization and restored acknowledgments, USENIX open-access publication from day one, and presenter obligations in Seattle.
---

# OSDI Camera-Ready

Deliver the final paper and the conference obligations. Dates and budgets below are
the OSDI '26 cycle (notification March 26; final printable PDF due **June 9, 2026**;
conference July 13–15, Seattle — verified 2026-07-08); confirm the current
Requirements for Authors page before trusting any of them for another year.

## The June 9 deliverable

The final paper is not the submission with names added. Between March and June three
transformations happen, in this order:

1. **Shepherd-mandated changes** (conditional accepts): completed and approved, or
   the acceptance lapses — this dominates the calendar (`osdi-author-response`).
2. **Expansion into the final budget**: up to **14 pages** including figures and
   tables, plus unlimited pages for references **and appendices** — the appendix
   right the submission never had. Execute the expansion plan annotated in the
   source at submission time (`osdi-supplementary`): restore cut failure cases,
   attach the full proof, publish the complete result grids.
3. **De-anonymization**: real authors and institutions on the title page; the
   renamed system optionally reverts to its public name — decide deliberately,
   update *every* occurrence (body, figures, artifact, README), and keep paper and
   artifact names consistent forever after.

Plus the earned extra: papers that passed artifact evaluation may add a **two-page
Artifact Appendix** in the standard format, condensed from the AE runbook
(`osdi-artifact-evaluation`).

## De-anonymization checklist

| Restore / fix | Detail commonly botched |
|---|---|
| Author block + affiliations | Ordering agreed in writing; affiliations as of the work, footnotes for moves |
| Acknowledgments | Funders, grant numbers, testbed credits (e.g., shared-cluster acknowledgment policies), colleagues |
| System name | If reverting from the anonymized name: figures and config listings too, not just prose |
| Self-citations | Third-person contortions rewritten as honest first person |
| Artifact pointer | The permanent archive identifier (DOI) in the paper, matching the AE record |
| PDF metadata | Title/author fields now *should* be populated correctly |

## What USENIX publication means (and does not cost)

OSDI is a USENIX venue, which changes the publication economics authors expect from
ACM conferences:

- **Open access, immediately.** The proceedings PDF is free to everyone from the day
  the event begins — no paywall, no ACM DL entitlements, no separate "open access
  option" to purchase. Your paper's canonical, citable home is a free
  `usenix.org` URL.
- **No author publication charge.** USENIX funds events through registration (with
  hardship discounts offered for OSDI '26); there is no APC line item to budget.
- **Slides and video** posted after the event are likewise open. Assume the talk is
  a permanent public artifact and prepare it to that standard.
- Registration rates and any presenter-registration requirement were not readable at
  verification time (待核实) — confirm both on the attend pages before booking.

Consequence worth planning for: the paper is public **during** the conference, so
reproduction attempts, blog dissections, and follow-up emails start in July, not
after some embargo. Have the artifact live and the README polished by the event.

## Presentation and the event

- One author presents in Seattle (July 13–15 for the '26 cycle); check the
  Instructions for Presenters page for slide specs, session logistics, and A/V
  deadlines.
- The **Jay Lepreau Best Paper Awards** are announced from the accepted program —
  the opening-session tradition since OSDI '08.
- Prepare the talk against the same arc as the paper (pain → idea → evidence), not
  as a section tour; the audience holds the free PDF in their laps.

## Between final paper and Seattle

The five weeks from June 9 to the July 13 opening are not idle:

- **Talk first draft within a week** of the final paper, while the argument is warm;
  systems talks fail from cramming the evaluation, so pick the two results that
  carry the idea and cut the rest to backup slides.
- **Dry-run twice**, once with systems people (they attack the design) and once with
  outsiders (they reveal which slide loses the room).
- **Artifact final polish**: the README's public debut is effectively July 13; run
  one last cold-start reproduction on a fresh machine or fresh container.
- **Coordinate the announcement**: with open-access publication at event start, the
  lab blog post, the repository going public under its real name, and any preprint
  update should all land the same week, pointing at the canonical `usenix.org` URL.
- **At the venue**: sessions are recorded and posted openly; treat Q&A answers as
  citable statements about the system's limits.

## Final-week mechanics

```text
final-week checklist (against the '26 Requirements for Authors)
[ ] shepherd approval recorded (conditional accepts) — BLOCKING
[ ] 14-page budget respected; appendices compile; refs unlimited but clean
[ ] artifact appendix (if badged) in standard format, <= 2 pages
[ ] de-anonymization table above executed; grep for the anonymized name
[ ] figures regenerate from the ledger at the final commit (no stale panels)
[ ] printable PDF validates: fonts embedded, no overfull cropping, metadata set
[ ] uploaded to the submissions system before June 9; confirmation archived
[ ] consent/copyright forms: check current cycle's requirements (待核实)
```

## Discoverability after publication

Small June decisions determine how the paper is found for a decade: keep the title
byte-identical everywhere (final PDF, HotCRP record, talk slides, repository README)
so citation databases merge rather than fork the entries; put the artifact's DOI in
the paper and the paper's `usenix.org` URL in the artifact so each permanently
resolves the other; and once the dblp `conf/osdi/` entry appears, adopt it as the
canonical BibTeX rather than letting five hand-typed variants propagate from the
lab's webpage.

## Output format

```text
[Deadline runway] days to final-paper due; shepherd status (n/a | pending | approved)
[Expansion] 14-page budget used how; appendix plan executed? artifact appendix in?
[De-anonymization] checklist rows outstanding: <list>
[Open-access readiness] artifact live + README public-grade before the event? yes/no
[Presenter logistics] registration/attendance items confirmed vs 待核实
```
