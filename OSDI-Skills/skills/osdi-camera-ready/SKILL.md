---
name: osdi-camera-ready
description: Use when converting an OSDI acceptance into the published paper — the June final-paper deadline (June 3, 2027 for OSDI '27), expansion to 14 pages plus references, any appendix or Artifact Appendix the cycle allows, de-anonymization and restored acknowledgments, USENIX open-access publication from day one, and presenter obligations in Baltimore.
---

# OSDI Camera-Ready

Deliver the final paper and the conference obligations. Dates and budgets below are
the OSDI '27 cycle (notification **March 16, 2027**; final papers due **June 3, 2027**;
conference **July 7–9, 2027, Baltimore** — re-verified 2026-11-24 from the CFP). The
'27 CFP fixes the final budget at **14 pages plus references**; the detailed final-paper
rules (appendices, the Artifact Appendix, forms) were not yet posted and are 待核实 — the
OSDI '26 rules quoted below as history were 14 pages plus references **and appendices**,
due June 9, 2026, with a two-page Artifact Appendix.

## The June 3 deliverable

The final paper is not the submission with names added. Between March and June three
transformations happen, in this order:

1. **Shepherd-mandated changes** (conditional accepts): completed and approved, or
   the acceptance lapses — this dominates the calendar (`osdi-author-response`).
2. **Expansion into the final budget**: up to **14 pages** including figures and
   tables, plus unlimited pages for references (and, if the '27 final rules again
   allow them as the '26 rules did, appendices — 待核实). Execute the expansion plan annotated in the
   source at submission time (`osdi-supplementary`): restore cut failure cases,
   attach the full proof, publish the complete result grids.
3. **De-anonymization**: real authors and institutions on the title page; the
   renamed system optionally reverts to its public name — decide deliberately,
   update *every* occurrence (body, figures, artifact, README), and keep paper and
   artifact names consistent forever after.

Plus the earned extra under the '26 rules: papers that passed artifact evaluation could
add a **two-page Artifact Appendix** in the standard format, condensed from the AE
runbook (`osdi-artifact-evaluation`); confirm whether '27 keeps it (待核实).

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
- **No author publication charge.** USENIX funds events through registration; there
  is no APC line item to budget.
- **Slides and video** posted after the event are likewise open. Assume the talk is
  a permanent public artifact and prepare it to that standard.
- **Registration duty:** by submitting, the authors agreed that at least one author
  registers at **full price** (not the student rate) and presents; an author presenting
  several papers still needs one full-price registration per paper. Rates are 待核实 —
  confirm on the attend pages before booking. An embargo before the event can be requested
  from USENIX Production.

Consequence worth planning for: the paper is public **during** the conference, so
reproduction attempts, blog dissections, and follow-up emails start in July, not
after some embargo. Have the artifact live and the README polished by the event.

## Presentation and the event

- One author presents in Baltimore (July 7–9, 2027); check the
  Instructions for Presenters page for slide specs, session logistics, and A/V
  deadlines.
- The **Jay Lepreau Best Paper Awards** are announced from the accepted program —
  the opening-session tradition since OSDI '08.
- Prepare the talk against the same arc as the paper (pain → idea → evidence), not
  as a section tour; the audience holds the free PDF in their laps.

## Between final paper and Baltimore

The five weeks from June 3 to the July 7 opening are not idle:

- **Talk first draft within a week** of the final paper, while the argument is warm;
  systems talks fail from cramming the evaluation, so pick the two results that
  carry the idea and cut the rest to backup slides.
- **Dry-run twice**, once with systems people (they attack the design) and once with
  outsiders (they reveal which slide loses the room).
- **Artifact final polish**: the README's public debut is effectively July 7; run
  one last cold-start reproduction on a fresh machine or fresh container.
- **Coordinate the announcement**: with open-access publication at event start, the
  lab blog post, the repository going public under its real name, and any preprint
  update should all land the same week, pointing at the canonical `usenix.org` URL.
- **At the venue**: sessions are recorded and posted openly; treat Q&A answers as
  citable statements about the system's limits.

## Final-week mechanics

```text
final-week checklist (against the current Requirements for Authors)
[ ] shepherd approval recorded (conditional accepts) — BLOCKING
[ ] 14-page budget respected; refs unlimited but clean; appendices only if allowed
[ ] artifact appendix (if badged and allowed this cycle) in standard format
[ ] de-anonymization table above executed; grep for the anonymized name
[ ] figures regenerate from the ledger at the final commit (no stale panels)
[ ] printable PDF validates: fonts embedded, no overfull cropping, metadata set
[ ] uploaded to the submissions system before June 3; confirmation archived
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
[Expansion] 14-page budget used how; appendix/artifact-appendix allowed this cycle? plan executed?
[De-anonymization] checklist rows outstanding: <list>
[Open-access readiness] artifact live + README public-grade before the event? yes/no
[Presenter logistics] registration/attendance items confirmed vs 待核实
```
