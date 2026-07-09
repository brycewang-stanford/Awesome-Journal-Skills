# Official Source Map - IEEE ICSME

Access date: 2026-07-09

This map records the official and cross-check sources used for ICSME-specific facts in this
pack. ICSME is the **IEEE International Conference on Software Maintenance and Evolution**, the
field's dedicated venue for maintenance, evolution, reverse engineering, program comprehension,
technical debt, refactoring, and mining-software-repositories work. Its calendar, page budget,
and review mechanics are decided per edition. Reopen the current-cycle research-papers call, the
Important Dates page, and the co-located artifact/ROSE call before giving submission-ready advice.

## Access method note

Direct fetches of `conf.researchr.org`, `easychair.org`, and `ieeexplore.ieee.org` returned
**HTTP 403 / blocked CONNECT** from the verification gateway on 2026-07-09 (the standard egress
block in this build sandbox). Official pages were therefore read through **search-engine
renderings of the exact researchr URLs** and cross-checked against the ICSME EasyChair CFP
(`easychair.org/cfp/ICSME26`), the `se-deadlines` aggregator, dblp's ICSME proceedings stream,
and the ICSME 2025/2024 editions for track continuity. Facts that could not be pinned to a
primary rendering are labeled **待核实**.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://conf.researchr.org/track/icsme-2026/icsme-2026-papers | ICSME 2026 research-papers call: double-anonymous review, IEEEtran two-column 10+2 budget, EasyChair, abstract-then-paper deadlines, early-decision + author-response model | 2026-07-09 |
| 2 | https://conf.researchr.org/home/icsme-2026 | ICSME 2026 (42nd edition) home: Benevento, Italy, University of Sannio, September 14-18, 2026 | 2026-07-09 |
| 3 | https://conf.researchr.org/dates/icsme-2026 | ICSME 2026 Important Dates page (abstract 27 Feb 2026, paper 6 Mar 2026, early decisions 3 May 2026, notification 29 May 2026; all 23:59 AoE) | 2026-07-09 |
| 4 | https://easychair.org/cfp/ICSME26 | EasyChair CFP mirror: "42nd IEEE International Conference on Software Maintenance and Evolution"; submission via EasyChair `icsme2026`; desk-reject for guideline non-compliance | 2026-07-09 |
| 5 | https://conf.researchr.org/track/icsme-2026/icsme-2026-journal-first | Journal-First (J1C2) track: TSE and EMSE partner journals, papers accepted 1 Jan 2025 - 30 May 2026, not previously conference-presented, at least one author presents | 2026-07-09 |
| 6 | https://conf.researchr.org/track/icsme-2026/icsme-2026-registered-reports | Registered Reports track: initial report 11 May, PC reviews 4 Jun, response letter + revised report 9 Jun (two-stage in-principle-acceptance model) | 2026-07-09 |
| 7 | https://conf.researchr.org/track/icsme-2026/icsme-2026-replication-and-negative-results | RENE (Replication and Negative Results) track: systematic reproduction/replication/validation extended to new datasets, plus negative-result reports | 2026-07-09 |
| 8 | https://conf.researchr.org/track/icsme-2025/icsme-2025-artifact---rose | Joint Artifact Evaluation Track and ROSE Festival: IEEE "Open Research Object" and "Research Object Reviewed" badges; open to ICSME/SCAM/VISSOFT accepted papers except Journal-First (2025 edition, continuity source) | 2026-07-09 |
| 9 | https://conf.researchr.org/track/icsme-2026/icsme-2026-tool-demonstration | Tool Demonstration and Data Showcase Track (short-paper track) | 2026-07-09 |
| 10 | https://conf.researchr.org/track/icsme-2026/icsme-2026-industry-track + https://conf.researchr.org/track/icsme-2026/icsme-2026-nier | Industry Track and the Visions and Emerging Results (NIER) Track | 2026-07-09 |
| 11 | https://dblp.org/db/conf/icsm/index.html | dblp ICSME/ICSM proceedings stream for edition numbering and exemplar verification | 2026-07-09 |

## Verified 2026 facts used in skills

- **ICSME 2026 is the 42nd IEEE International Conference on Software Maintenance and Evolution**,
  held in **Benevento, Italy** (hosted by the University of Sannio), **September 14-18, 2026**
  (sources 2, 4). It is co-located with **SCAM** (Source Code Analysis and Manipulation) and
  **VISSOFT** (Software Visualization), which share the ROSE-Festival artifact track (source 8).
- **Research-track calendar:** abstract submission **27 February 2026**, full paper
  **6 March 2026**, early decisions **3 May 2026**, final notification **29 May 2026**; all
  deadlines 23:59 AoE, via **EasyChair** (`icsme2026`) (sources 1, 3, 4).
- **Format and budget:** IEEE two-column conference proceedings format, `\documentclass[conference]{IEEEtran}`;
  **10 pages** including all figures, tables, and appendices, **plus up to 2 pages containing only
  references**. Non-compliant PDFs are **desk-rejected** before review (sources 1, 4).
- **Review is double-anonymous** with a single research-track round and an **early-decision cut**:
  at the start of the author-response period some papers already receive Accept or Reject (no
  response requested), and the rest receive "Response Recommended" and may submit a rebuttal that
  answers the PC's specific questions (source 1).
- **Journal-First (J1C2)** admits TSE / EMSE papers accepted between 1 Jan 2025 and 30 May 2026,
  not previously presented at a conference, presented (not re-reviewed) at ICSME (source 5).
- **Registered Reports** runs a two-stage in-principle-acceptance model (Stage 1 protocol review,
  then Stage 2), and **RENE** rewards replications/reproductions extended to new data and honest
  negative results (sources 6, 7).
- **Artifacts** are evaluated in the **Joint Artifact Evaluation Track and ROSE Festival** and earn
  the **IEEE badges "Open Research Object" and "Research Object Reviewed"** — the IEEE scheme, not
  ACM's four-badge scheme (source 8).

## The single-round IEEE model (honest reading of the cycle question)

Unlike the journal-style PACMSE model at ESEC/FSE, ICSME runs a **conference-style single annual
research round**: one abstract-then-paper deadline, double-anonymous review, an early-decision cut,
an author-response rebuttal, and a final accept/reject — there is **no journal-style Major Revision
round** on the research track. A paper that needs deep rework is rejected and resubmitted next
cycle (or rerouted to SCAM, a journal, or the Journal-First path once a journal accepts it). The
maintenance/evolution community also gives unusual weight to **replication and negative results**
(the RENE track) and to **open science** (the ROSE Festival), so evidence culture, not a revision
round, is where author effort concentrates.

## No editor-in-chief; conference registration model

Like every conference in this collection, ICSME has **no standing editor-in-chief**; leadership is
the per-edition General and Program Co-Chairs appointed by the ICSME steering committee under IEEE
TCSE. Proceedings publish in **IEEE Xplore**; the cost model is conference registration, and at
least one author registers and presents each accepted paper (including Journal-First contributions).

## Still cycle-volatile (verify every year)

- All dates and AoE cutoffs, and whether the abstract-then-paper two-step is retained.
- Exact page budget and which IEEEtran revision is required (2026 posts 10+2, two-column).
- Whether the early-decision cut and author-response period are offered, and the response length.
- Registered Reports / RENE deadlines and their exact stage mechanics.
- ROSE-Festival badge set, eligibility (which tracks), and whether evaluation is single/double-anonymous.
- Open-science / data-availability wording and any generative-AI disclosure policy (**待核实**).
- **ICSME 2026 General Chairs and Research-Track Program Co-Chairs rosters (待核实** — the committee
  page was not cleanly retrievable through the gateway on the access date).
- **Camera-ready deadline and IEEE eCopyright mechanics (待核实** — not shown in the retrieved
  Important Dates rendering).
