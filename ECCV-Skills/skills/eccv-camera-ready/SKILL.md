---
name: eccv-camera-ready
description: Use when preparing an accepted ECCV paper for Springer LNCS publication — the enlarged final page budget, Springer author kit and licensing, the June 30 AoE camera-ready cutoff in 2026, registration as a publication condition, ECVA open-access mirroring about four weeks before the conference, and arXiv synchronization.
---

# ECCV Camera Ready

Use this after an ECCV acceptance. Unlike its CVF-published siblings, ECCV's
version of record is a **Springer LNCS book series**, with a free mirror on
the **ECVA papers portal (ecva.net)** — two publication targets with different
mechanics, plus your own arXiv copy as a third. In 2026, decisions arrived
June 17 and the camera-ready deadline was extended to **June 30, AoE** — a
thirteen-day sprint.

## The three publication surfaces

| Surface | Who controls it | What to check |
|---|---|---|
| Springer LNCS proceedings | Springer, via the ECCV author kit | Final page budget, licence/copyright form, source archive requirements |
| ECVA open-access mirror | ECVA (ecva.net/papers.php) | Appears no earlier than ~4 weeks before the conference; PDF + supplement listed with the Springer DOI |
| arXiv v2+ | You | Update to the accepted text after checking Springer's self-archiving terms for LNCS |

ECCV 2024's record shows the scale of the machine you are feeding: LNCS
volumes 15059–15147 carried 2,387 papers. Metadata errors (author order,
affiliation spelling, title casing) propagate into a printed book series and
its DOIs — fix them in the source, not in a later erratum.

## Page budget and rewrite pass

- The 2026 Dates page listed a **15-page camera-ready limit excluding cited
  references** — one page more than the submission's 14-including-figures rule,
  but with a different counting basis, so re-verify the author kit wording
  before planning the extra space (page-count basis: 待核实 in detail).
- Spend the gained room in priority order: (1) rebuttal promises made to
  reviewers, (2) acknowledgements and funding, (3) camera-ready-only
  clarifications ACs asked for. Do not add claims nobody reviewed.
- De-anonymization is a rewrite, not a find-and-replace: restore first-person
  self-citations, insert the real code URL where the anonymous text said "will
  be released", and delete the anonymity scaffolding sentences.

## Springer-specific mechanics

- Publication in the proceedings required at least one author to **register
  for the conference** and a compliant camera-ready before the deadline —
  registration is a publication precondition, not a travel detail.
- Springer's pipeline consumes LaTeX source, not just a PDF; keep the project
  compilable with the official kit and expect a copyright/licence form per
  paper.
- ORCID, affiliation, and email fields feed SpringerLink's indexed metadata;
  have every co-author confirm their own entry.

## Rebuttal-promise ledger

```text
For each promise made in the one-page rebuttal:
  [P1] "clarify training schedule in Sec 4.1"  -> done in v_final? yes/no
  [P2] "add failure cases to supplement"       -> done? yes/no
  [P3] "cite reviewer-suggested prior work"    -> done + discussed? yes/no
Unkept promises are visible to the same reviewers at the poster in Malmö.
```

## June-to-September sequencing (2026 anchors)

1. **June 17–30**: camera-ready text, Springer forms, registration, metadata.
2. **July**: public code/model release while the paper is fresh
   (`eccv-artifact-evaluation`), arXiv update, project page.
3. **~Mid-August**: ECVA/Springer open-access copies surface (~4 weeks before
   the conference) — verify your PDF and supplement render correctly.
4. **September 8–13, Malmö**: poster/talk, workshops on the 8th–9th; Schengen
   visa and travel booked well before August.

## Output format

```text
[Camera-ready state] compliant / blocked / at-risk
[Springer package] <PDF + source + licence form + metadata status>
[Promise ledger] <rebuttal promise -> kept / dropped-with-reason>
[Open-access check] <ECVA mirror + arXiv version plan>
[Registration + Malmö logistics] <who registers, who presents, visa state>
```
