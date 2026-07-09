# Official Source Map - ACM PODS

Access date: 2026-07-09

This map records the official and cross-check sources for PODS-specific facts in this pack.
**PODS** is the ACM SIGMOD/SIGACT Symposium on **Principles of Database Systems** — the
database-**theory** symposium held jointly with SIGMOD every year. Its research papers are
published in the **PODS track of PACMMOD** (Proceedings of the ACM on Management of Data), and its
calendar runs **multiple submission cycles per year**. Reopen the current-cycle PODS call, the
Important Dates page, the PACMMOD PODS pages, and the sigmod.org PODS awards pages before giving
submission-ready advice.

## Access method note

Direct fetches of `2026.sigmod.org`, `2027.sigmod.org`, `sigmod.org`, and `dl.acm.org` returned
**HTTP 403 Forbidden** from the verification gateway on 2026-07-09 (the same egress block seen when
verifying other ACM venues in this repository; a WebFetch of
`https://2026.sigmod.org/calls_papers_pods_research.shtml` returned 403). Official pages were
therefore read through **search-engine renderings of the exact URLs** and cross-checked against the
EasyChair CFP mirror, the ACM Digital Library / PACMMOD PODS tables of contents, dblp, and the
`databasetheory.org` community site. Facts that could not be pinned to at least two independent
surfaces are labeled **待核实**. Do not confuse this PODS with **PODC** (the ACM Symposium on
Principles of *Distributed* Computing) — a different venue; no fact here derives from it.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://2026.sigmod.org/calls_papers_pods_research.shtml | PODS 2026 research call: two submission cycles, `acmsmall,review,anonymous` format, 15 pages + unlimited references + appendix, lightweight double-anonymous review, COI-at-submission | 2026-07-09 |
| 2 | https://2026.sigmod.org/calls_papers_important_dates.shtml | PODS 2026 Important Dates: Cycle 1 (abstract 3 Jun 2025, paper 10 Jun 2025), Cycle 2 (abstract 3 Dec 2025, paper 10 Dec 2025); all 11:59pm AoE | 2026-07-09 |
| 3 | https://2026.sigmod.org/ | PODS 2026 co-located with SIGMOD, Bengaluru, India, 31 May - 5 Jun 2026 | 2026-07-09 |
| 4 | https://2027.sigmod.org/calls_papers_important_dates.shtml | PODS 2027 Important Dates: Cycle 1 (abstract 23 May 2026, paper 30 May 2026), Cycle 2 (abstract+COI 10 Oct 2026, paper 17 Oct 2026, feedback 10-17 Dec 2026, notify 19 Jan 2027, revision 19 Feb 2027, final 12 Mar 2027) | 2026-07-09 |
| 5 | https://2027.sigmod.org/ | PODS 2027 co-located with SIGMOD, Huntington Beach, California, USA, 13-19 Jun 2027 | 2026-07-09 |
| 6 | https://dl.acm.org/journal/pacmmod/pods | PACMMOD PODS track: PODS research papers publish in Proceedings of the ACM on Management of Data, invited for presentation at PODS | 2026-07-09 |
| 7 | https://www.easychair.org/my/conference?conf=pods2026 | PODS 2026 submission portal is EasyChair (`pods2026`) | 2026-07-09 |
| 8 | https://sigmod.org/pods-home/acm-pods-alberto-o-mendelzon-test-of-time-award/ | ACM PODS Alberto O. Mendelzon Test-of-Time Award (established 2007; paper published in PODS proceedings ten years prior) | 2026-07-09 |
| 9 | https://sigmod.org/pods-home/pods-best-paper-awards/ | PODS Best Paper Award; Best Newcomer Award (1997-2008) replaced by Best Student Paper Award from PODS 2009 | 2026-07-09 |
| 10 | https://2026.sigmod.org/org_pods_pc.shtml | PODS 2026 PODS Program Committee page (PC Chair Ke Yi, HKUST) | 2026-07-09 |
| 11 | https://databasetheory.org/taxonomy/term/17 | Community CFP mirror and scope statement for PODS (theoretical foundations of data management) | 2026-07-09 |

## Verified 2026/2027-cycle facts used in skills

- **PODS 2026 is the 45th edition** (PODS 2025 was the 44th, per the "Companion of the 44th
  Symposium on Principles of Database Systems", ACM DL DOI 10.1145/3722234). PODS 2026 was held with
  SIGMOD in **Bengaluru, India, 31 May - 5 June 2026** (source 3). As of the 2026-07-09 access date
  this edition has already taken place, so the live *next* target is **PODS 2027**.
- **PODS runs multiple submission cycles per year.** PODS 2026 had **two** cycles: Cycle 1
  (abstract **3 Jun 2025**, full paper **10 Jun 2025**; rebuttal 29 Jul - 1 Aug 2025; initial
  notification 11 Aug 2025; revision submission 25 Aug 2025; final notification 1 Sep 2025) and
  Cycle 2 (abstract **3 Dec 2025**, full paper **10 Dec 2025**; later phases follow the same shape
  a season later — exact Cycle-2 rebuttal/notification dates 待核实) (sources 1, 2).
- **PODS 2027 (46th edition)** is co-located with SIGMOD in **Huntington Beach, California, USA,
  13-19 June 2027** (source 5). Two cycles: Cycle 1 (abstract **23 May 2026**, paper **30 May
  2026**; rebuttal 29 Jul - 1 Aug 2026; initial notification 11 Aug 2026; revision 25 Aug 2026;
  final 1 Sep 2026) and Cycle 2 (abstract+COI **10 Oct 2026**, paper **17 Oct 2026**; author
  feedback 10-17 Dec 2026; notification accept/reject/revision **19 Jan 2027**; revised paper 19 Feb
  2027; final notification **12 Mar 2027**) (source 4). **As of 2026-07-09, PODS 2027 Cycle 1 has
  closed and Cycle 2 (10/17 Oct 2026) is the live upcoming deadline.**
- **Format is the ACM `acmart` class in the `acmsmall` review-anonymous variant:**
  `\documentclass[acmsmall,review,anonymous]{acmart}`. A submission may be **up to 15 pages, not
  including references**, plus **unlimited references**, plus a **clearly marked appendix of
  unlimited length incorporated at submission time**; **online/external appendices are not
  allowed** (source 1). This replaced the older two-column `sigconf` 12-page style; the change
  aligns PODS with the PACMMOD publication format.
- **Review is lightweight double-anonymous:** author names and institutions omitted, self-references
  in the third person; a list of conflicts of interest is declared at submission (source 1). PODS
  moved to double-anonymous from a long single-blind tradition in recent editions (the exact first
  double-anonymous edition is **待核实**).
- **Each cycle has two reviewing rounds with a revision/shepherd step.** Decisions are
  **accept / reject / revision** (a revision may be minor or major); a revision is invited, the
  authors have a bounded window to submit a revised version, and a shepherd judges whether the
  revision is satisfactory (sources 1, 2; decision-category wording cross-checked against the joint
  SIGMOD/PODS process — PODS-specific phrasing 待核实).
- **Publication venue is the PODS track of PACMMOD** (Proceedings of the ACM on Management of Data);
  PODS 2024 papers appear in PACMMOD Vol 2 (issues N2 and N5), PODS 2025 in PACMMOD Vol 3 N2 (source
  6). Accepted PODS-track articles are invited for presentation at the PODS symposium.
- **The ACM PODS Alberto O. Mendelzon Test-of-Time Award**, established by the PODS Executive
  Committee in 2007, honors a PODS paper published ten years earlier with the most impact; the 2025
  award went to "Joins via Geometric Resolutions" (PODS 2015) (source 8). A **PODS Best Paper Award**
  and a **Best Student Paper Award** (which replaced the 1997-2008 Best Newcomer Award in 2009) are
  also given (source 9).
- **PODS 2026 PODS PC Chair: Ke Yi (HKUST)** (source 10). Chairs rotate per edition; the **PODS 2027
  PC Chair roster is 待核实**.
- **Resubmission policy:** recent SIGMOD/PODS policy prohibits resubmitting research-track work that
  was rejected within roughly the prior year of cycles; the exact PODS 2026/2027 wording (and any
  cross-cycle carry rule for a *revision* decision) is **待核实** on the current call.

## PODS is a theory symposium: what "artifact" and "experiments" mean here

PODS is database **theory** (query languages, complexity, logic, finite model theory, data
integration/exchange, provenance, privacy theory, worst-case-optimal joins, KR/ontologies, streaming
and MPC theory). It has **no artifact-evaluation track in the systems sense** and no ACM reproducibility
badges. The analogue this pack adapts:

- The "artifact" is the **proof appendix and any formal-claims material** — complete proofs, the
  appendix incorporated at submission, and, by community norm, a **full version posted on arXiv**
  (open access, DOI-linked to the PACMMOD version). See `pods-artifact-evaluation` and
  `pods-reproducibility`.
- "Experiments" are **worst-case/average-case analyses, tight bounds, and separations** — with the
  occasional empirical validation where a paper claims practicality. See `pods-experiments`.

## No editor-in-chief; no APC in the systems sense

PODS has **no standing editor-in-chief**; the rotating leadership is the per-edition PODS PC Chair
and the PODS General/Steering officers appointed with ACM SIGMOD and SIGACT. PACMMOD is an
open-access ACM journal; the cost model is conference registration and at least one author presents
the accepted paper.

## Still cycle-volatile (verify every year)

- Number of submission cycles and every abstract/paper/rebuttal/notification/revision date and AoE cutoff.
- The exact page budget and which `acmart` variant/revision the current call requires.
- Decision-category wording, the revision/shepherd mechanics, and any cross-cycle resubmission rule.
- Whether double-anonymity is "lightweight" and exactly what author-identifying material is barred.
- PODS 2026/2027 full PC rosters beyond the named PC Chair (**待核实**), and any generative-AI use
  disclosure policy (**待核实**).
