---
name: ase-workflow
description: Use when planning an ASE (IEEE/ACM Automated Software Engineering) research-track campaign backward from the deadline, through abstract registration, the double-anonymous submission, the early-rejection gate, rebuttal, the criteria-bound revision round, artifact evaluation, and the camera-ready in both IEEE Xplore and the ACM Digital Library.
---

# ASE Workflow

Run the ASE year backward from the deadline. ASE is an annual conference (dual IEEE/ACM sponsored)
whose research track has an **early-rejection gate**, a **rebuttal**, and a first-class,
criteria-bound **Major revision** outcome ("Revision" in 2026); plan for all three. Every date below is a one-cycle snapshot —
reopen the current Important Dates page first (see `resources/official-source-map.md`).

## Anchor dates (ASE 2027 snapshot — verify each cycle)

- **Paper submission:** 10 March 2027. **Early-rejection notification:** 19 May 2027. **Author
  response:** 19-24 May 2027. **Initial notification:** 10 June 2027. **Major-revision
  submission:** 8 July 2027. **Final notification:** 27 July 2027. **Camera-ready:** 11 August
  2027 (all AoE). **Conference:** El Paso, Texas, USA, 24-28 October 2027.
- The call describes an abstract stage (title, abstract, areas, conflicts), but the dates page
  lists no separate **abstract-registration deadline** — **待核实**; confirm it, it is a hard gate.
- ASE 2026 (Munich, 12-16 October 2026) has met; its dates are history.

## Backward plan from the deadline

```text
T-16 wk  Route with ase-topic-selection: ASE research vs. NIER/Tools vs. FSE/ISSTA/journal.
T-14 wk  Lock the automation and the subject systems; freeze what the tool does and what it runs on.
T-10 wk  Build evidence (ase-experiments): real subjects, fair tool baselines, ablation isolating
         any learned component. Pin provenance now (ase-reproducibility) — it cannot be retrofitted.
T-6  wk  Draft to the ASE arc (ase-writing-style) against the worked example; write related work
         delta-first (ase-related-work). Keep to 10 content pages + 2 pages of references/Data Availability.
T-3  wk  Assemble the anonymized artifact and the Data Availability section.
T-1  wk  Register the abstract before its (earlier) deadline. Double-anonymous sweep (ase-submission)
         on tool names, repos, PDF metadata.
T-0      Submit on ase2027.hotcrp.com in the mandated template (IEEEtran conference for 2027).
```

## After submission — the review timeline

```text
[Reviews + early-rejection gate]  uniformly negative scores -> early reject, no rebuttal.
[Rebuttal]                        if you reach it, at least one reviewer saw value; move the
                                  borderline reviewer with facts and small checkable numbers.
[Outcome]                         Accept / Major revision / Reject.
[Major-revision round]            meet every stated criterion; return the revised paper + a
                                  point-by-point summary-of-changes, re-checked against the criteria.
[Camera-ready]                    de-anonymize, apply the extra content page, finalize IEEE/ACM
                                  metadata; 2027 publication of record is the IEEE Digital Library.
[Artifact evaluation]             on its own deadline: target Available and Reusable badges.
[Presentation]                    at least one author presents at ASE.
```

## Track fork (decide early, they have separate deadlines and sites)

- **Research Papers** — the full technique/tool contribution (this workflow).
- **NIER** — a bold early idea (4 pages) on its own HotCRP (`ase2026-nier.hotcrp.com` in 2026; 2027 call not yet posted).
- **Tools and Datasets** — a usable tool/dataset (≤4 pages) demo-oriented.
- **Journal-First** — TSE/TOSEM/EMSE work accepted after 1 Jan 2025, presented at ASE.
- **Industry Showcase / Doctoral Symposium / Workshops** — separate calls and timelines.

## Risk register (ASE-specific)

| Risk | When it bites | Mitigation |
|---|---|---|
| Missed abstract registration | Days before the full deadline | Register title/abstract/authors/conflicts a week early |
| Wrong template | Camera-ready or desk-check | Confirm IEEEtran (2027) vs. ACM `acmart` (2026) on the current call *before* drafting |
| Over 10 content pages | Final week | Freeze the body early; the 2 reference pages do not absorb text |
| Missing Data Availability section | Desk check | Draft it at T-3 wk, after the Conclusion (2027: with the references, outside the 10 pages) |
| Early-rejected | At the gate | Make the first three pages and the evaluation table land immediately |
| A revision criterion ignored | Revision re-check | Ledger every criterion in the summary-of-changes |
| Artifact not ready | Post-acceptance | Stage the DOI-archived, documented tool before the AE deadline |

## Parallelizable vs. sequential

- **Parallel:** artifact packaging can proceed alongside writing; provenance pinning must happen at
  data-collection time regardless.
- **Sequential:** venue routing → evidence → writing → anonymity sweep → submission; and
  reviews → (early-rejection gate) → rebuttal → revision → camera-ready → artifact evaluation.

## Output format

```text
[Target cycle] ASE 20XX, submission <date>, notification <date>, conference <city/dates>
[Track] research / NIER / tools-and-datasets / journal-first
[Milestones] <T-minus plan with owners>
[Gate readiness] abstract registered? template correct? 10+2 respected? Data Availability present?
[Post-submission plan] early-rejection risk / rebuttal targets / revision-criteria readiness / artifact
```
