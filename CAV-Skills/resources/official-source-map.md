# Official Source Map - CAV (Computer Aided Verification)

Access date: 2026-07-09

This map records the official and cross-check sources for the CAV-specific facts used across
this pack. CAV is the flagship formal-verification conference; its research papers are published
open access in **Springer Lecture Notes in Computer Science (LNCS)**, and its calendar,
submission categories, page limits, review mechanics, and artifact-evaluation rules are decided
per edition by the current Program Chairs. Reopen the current-cycle Call for Papers, the
Important Dates, the Artifact Evaluation page, and the Springer LNCS proceedings page before
giving submission-ready advice.

## Access method note

Direct fetches of `conferences.i-cav.org` / `i-cav.org` and `sigplan.org` returned **HTTP 403**
from the verification gateway on 2026-07-09 (the same egress block seen for other venue/publisher
domains). Official pages were therefore read through **search-engine renderings of the exact
URLs** (the CAV 2026 CFP, Artifact Evaluation, Organization, and Program pages, and the SIGPLAN
announcement) and cross-checked against **dblp**, the **Springer LNCS** book pages for CAV 2024
and CAV 2025, the **FLoC 2026** site, and the CAV 2025 pages. Facts that could not be pinned to
two independent surfaces are labeled **待核实**. Name-collision guard: CAV is *Computer Aided
Verification*; do not confuse it with unrelated "CAV" acronyms (connected/automated vehicles,
etc.), and do not attribute TACAS/FMCAD/VMCAI/POPL/PLDI papers to CAV — those sibling-venue traps
are documented in `resources/exemplars/library.md`.

## Primary and cross-check sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | http://conferences.i-cav.org/2026/cfp/ | CAV 2026 Call for Papers: four submission categories, LNCS format, page limits, anonymization matrix, two-stage review, rebuttal, artifact-intent declaration | 2026-07-09 |
| 2 | https://www.sigplan.org/announce/2025-11-21-cav-2026/ | SIGPLAN announcement of the 38th CAV (CAV 2026): identity, deadlines, review model | 2026-07-09 |
| 3 | http://conferences.i-cav.org/2026/ | CAV 2026 home: 38th edition, Lisbon, Portugal, July 26-29, 2026, part of FLoC 2026 | 2026-07-09 |
| 4 | https://conferences.i-cav.org/2026/organization/ | CAV 2026 Program Chairs: Anthony W. Lin, Eva Darulova, Philipp Rümmer | 2026-07-09 |
| 5 | http://conferences.i-cav.org/2026/artifacts/ | CAV 2026 Artifact Evaluation: Available / Functional / Reusable badges, ≥2 AEC members per artifact, smoke-test + full-review phases, optional and non-conditional | 2026-07-09 |
| 6 | https://www.floc26.org/ | FLoC 2026 (9th Federated Logic Conference), Lisbon, Portugal, July 2026, co-locating CAV, CP, CSF, FSCD, ICLP, IJCAR, ITP, KR, LICS, SAT | 2026-07-09 |
| 7 | https://link.springer.com/conference/cav | Springer LNCS CAV proceedings series (open access) | 2026-07-09 |
| 8 | https://link.springer.com/book/10.1007/978-3-031-65627-9 | CAV 2024 (36th), Montreal, LNCS 14681-14683, open access | 2026-07-09 |
| 9 | https://link.springer.com/book/10.1007/978-3-031-98679-6 | CAV 2025 (37th), Zagreb, open-access 4-volume set LNCS 15931-15934; 51 regular + 24 tool + 4 case-study papers from 305 submissions | 2026-07-09 |
| 10 | https://conferences.i-cav.org/2025/award/ | CAV Award (annual, fundamental contributions to computer-aided verification); 2025 laureates cited | 2026-07-09 |
| 11 | https://dblp.org/db/conf/cav/index.html | dblp CAV proceedings stream, for edition numbering and exemplar verification | 2026-07-09 |

## Verified CAV 2026 facts used in skills

- **CAV 2026 is the 38th International Conference on Computer Aided Verification**, held in
  **Lisbon, Portugal, July 26-29, 2026**, as part of **FLoC 2026** (the 9th Federated Logic
  Conference) (sources 2, 3, 6).
- **Program Chairs:** Anthony W. Lin (University of Kaiserslautern-Landau / MPI-SWS),
  Eva Darulova (Uppsala University), and Philipp Rümmer (University of Regensburg / Uppsala
  University) (source 4).
- **Submission categories (four):** Regular Papers, Short Tool Papers, Short Application Papers,
  and Industrial Experience Reports & Case Studies (sources 1, 2).
- **Page limits (LNCS format, excluding references and appendices):** Regular Papers **18 pages**;
  Short Tool Papers, Short Application Papers, and Industrial Experience Reports & Case Studies
  **10 pages** each. A clearly marked appendix is allowed but reviewers are **not obliged** to
  read it (source 1).
- **Anonymization matrix (partial double-anonymity):** Regular Papers and Short Application Papers
  **must be anonymized** (double-blind); Short Tool Papers and Industrial Experience Reports &
  Case Studies are **not anonymized** (sources 1, 2). *Verify per cycle — this split is unusual
  and cycle-volatile.*
- **Key dates (CAV 2026, AoE):** full-paper submission **28 January 2026**; tentative first-round
  outcome (early reject) around **4 March 2026**; author response / rebuttal **30 March - 2 April
  2026**; author notification **17 April 2026**; artifact registration **22 April 2026**;
  conference **26-29 July 2026** (sources 1, 2, 3).
- **Two-stage reviewing:** in stage 1 each paper receives **two** reviews; papers with sufficient
  support proceed to stage 2 for **two additional** reviews, and the rest are rejected early.
  Papers passing stage 1 get a rebuttal opportunity (sources 1, 2).
- **Artifact evaluation:** run by a dedicated **Artifact Evaluation Committee (AEC)**; each
  artifact is reviewed by **at least two** AEC members across a **smoke-test phase** and a
  **full-review phase**; three badges aligned with ACM criteria — **Available**, **Functional**,
  **Reusable**. Artifact submission is **invited but optional**, and **final paper acceptance is
  not conditional** on it; authors declare **artifact intent at submission time** (source 5).
- **Publication:** Springer **LNCS**, **open access** (Gold OA). CAV 2024 (36th, Montreal):
  LNCS 14681-14683. CAV 2025 (37th, Zagreb): LNCS 15931-15934, 4 volumes; 51 regular + 24 tool
  + 4 case-study papers accepted from **305 submissions** (sources 7-9).
- **CAV Award:** presented annually for fundamental contributions to computer-aided verification;
  a standing steering-committee award, separate from the conference decision (source 10).

## What makes CAV a distinctive process (honest reading)

CAV is not an ACM-journal conference and not an IEEE double-column one. Its research output is a
**Springer LNCS chapter**, single-column, in the `llncs` document class. Three features drive most
of this pack's advice and separate CAV from its siblings:

1. **A first-class Tool Paper track.** Short Tool Papers and Application Papers are a native
   category, not an afterthought — a working, usable verification tool evaluated on standard
   benchmarks is a recognized CAV contribution shape.
2. **Two-stage reviewing with an early reject.** Unlike a single-round rebuttal conference, CAV
   filters after two reviews, so a paper must survive stage 1 before it ever sees a rebuttal.
3. **Optional, non-conditional artifact evaluation with an unusual anonymity split.** Regular and
   application papers are double-blind; tool and industrial papers are not — because a tool paper
   that hid its tool's identity would be unreviewable.

## Still cycle-volatile (verify every year)

- All dates and AoE cutoffs, and whether a **separate abstract/registration deadline** precedes
  the paper deadline (**待核实** for 2026 — only the 28 Jan paper deadline was confirmed).
- The exact page limits per category and the LNCS template revision.
- The anonymization matrix per category (which categories are double-blind).
- The two-stage-review mechanics and the exact first-round (early-reject) notification date
  (**4 March 2026 is tentative**).
- The **submission portal** for 2026 — one rendering reports **EasyChair**; CAV 2025 used
  **HotCRP** (`cav2025.hotcrp.com`). Confirm the live link on the CFP before submitting
  (**待核实**).
- Artifact-evaluation badge set, phases, and whether the AEC is single- or double-anonymous.
- The **camera-ready deadline** and the LNCS open-access / copyright mechanics for 2026
  (**待核实**).
- Full Program Committee and AEC chair/member rosters beyond the three Program Chairs
  (**待核实**).
- Which verification competitions co-locate or affiliate in a given year (SMT-COMP historically
  began as a CAV 2005 satellite; SV-COMP runs at TACAS/ETAPS) (**待核实** for the 2026 affiliation
  set).

## No editor-in-chief; open-access cost model

CAV has **no standing editor-in-chief**; the rotating analogue is the per-edition Program Chairs
and Steering Committee. The LNCS proceedings are **open access** (Gold OA), so the cost model is a
per-volume open-access arrangement plus conference registration rather than an author-facing APC
per paper — confirm the exact open-access funding arrangement on the current proceedings notice.
