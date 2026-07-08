# Official Source Map - EuroSys

Access date: **2026-07-08**

This map records the official sources behind every EuroSys-specific fact in this pack.
EuroSys reissues its Call for Papers per edition and per round; reopen the current CFP,
the round's HotCRP instance, the sysartifacts call for artifacts, and eurosys.org before
giving submission-ready advice.

## Access method note

Direct HTTP fetches of `2027.eurosys.org`, `2026.eurosys.org`, and `eurosys.org` were
blocked (HTTP 403) in the verification environment on 2026-07-08. All facts below were
therefore verified through **search-engine renderings of the exact official URLs**,
cross-checked against the ACM Digital Library (`dl.acm.org/conference/eurosys`), dblp
(`dblp.org/db/conf/eurosys/`), the HotCRP instances, and the sysartifacts GitHub pages.
Facts that rest only on third-party renderings are flagged 待核实 below. When maintaining
this pack with direct access available, prefer the official pages themselves.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://2027.eurosys.org/cfp.html | EuroSys 2027 CFP: Rabat, Morocco, April 2027; two submission rounds; spring abstracts May 7 / papers May 14, 2026; fall abstracts September 17 / papers September 24, 2026 (AoE); 12 pages of technical content plus unlimited reference pages; A4/US letter with 178 x 229 mm text block, two columns ≥8 mm apart; `\documentclass[sigplan,twocolumn,review,anonymous]{acmart}`; double-blind with good-faith anonymization; violations not considered for review; accept / reject / one-shot-revision outcomes; same-round resubmission ban after rejection. | 2026-07-08 |
| 2 | https://eurosys27-spring.hotcrp.com/ and https://eurosys27-fall.hotcrp.com/ | The 2027 spring and fall HotCRP submission instances exist and carry round mechanics. | 2026-07-08 |
| 3 | https://2026.eurosys.org/ | EuroSys 2026 is the 21st edition, Edinburgh, UK, April 27–30, 2026; workshops/tutorials at the EICC. | 2026-07-08 |
| 4 | https://2026.eurosys.org/cfp.html | EuroSys 2026 round structure and revision policy wording: papers may be accepted, rejected, or offered a one-shot revision resubmitted at the subsequent deadline with a list of necessary conditions; season-specific resubmission bans. | 2026-07-08 |
| 5 | https://sysartifacts.github.io/eurosys2026/ (index and badges pages) | EuroSys artifact evaluation is run with the sysartifacts community; optional; artifacts submitted after acceptance notification; three badges — Available (public DOI-backed archive), Functional (complete, documented, works), Reproduced (main claims independently re-obtained) — with standard combinations by artifact type. | 2026-07-08 |
| 6 | https://www.eurosys.org/ (incl. /awards pages) | EuroSys is the European Chapter of ACM SIGOPS; community awards: EuroSys Test-of-Time Award (paper ≥10 years old with lasting impact), Roger Needham PhD Award (EUR 2000, best European systems dissertation), Jochen Liedtke Young Researcher Award (EUR 2000, junior European systems researcher). | 2026-07-08 |
| 7 | https://dl.acm.org/conference/eurosys | EuroSys proceedings are published by ACM in the ACM Digital Library. | 2026-07-08 |
| 8 | https://dblp.org/db/conf/eurosys/ | Edition-by-edition proceedings record since 2006; used to verify exemplar papers. | 2026-07-08 |
| 9 | https://www.eurosys.org/awards/test-of-time-award | Test-of-Time winners used as exemplars: Dryad (EuroSys '07, awarded 2017), Coccinelle collateral evolutions (EuroSys '08, awarded 2018), Borg (EuroSys '15, awarded 2019), Delay Scheduling (EuroSys '10, awarded 2020), Omega (EuroSys '13, awarded 2023). | 2026-07-08 |
| 10 | https://2026.eurosys.org/shadow-pc.html and https://2026.eurosys.org/artifact-evaluation.html | EuroSys 2026 ran a Shadow PC call and named artifact-evaluation chairs. | 2026-07-08 |

## Verified cycle facts used in the skills

- EuroSys 2027 (edition following the 21st): **Rabat, Morocco, April 2027**; spring round
  abstracts **May 7, 2026**, papers **May 14, 2026**; fall round abstracts
  **September 17, 2026**, papers **September 24, 2026**; all AoE (source 1).
- Reported notification dates: spring **August 21, 2026**; fall **January 29, 2027**;
  camera-ready for both cohorts around **March 5, 2027** — the notification and
  camera-ready dates surfaced via third-party calendar renderings of the CFP, so
  re-confirm on the official page (partially 待核实).
- Submission budget: **12 pages of technical content, unlimited reference pages**;
  text block **178 x 229 mm (7 x 9 in)**, two columns **≥8 mm** apart; recommended
  LaTeX `acmart` with `sigplan,twocolumn,review,anonymous` and the registration-issued
  paper ID (source 1).
- Review is **double-blind** with a good-faith anonymization standard; formatting or
  anonymization violations are **not considered for review** (source 1).
- Outcomes per submission: **accept, reject, or one-shot revision** targeted at the
  subsequent deadline with explicit necessary conditions; a rejected paper may not
  return **until the same round of the next edition** (sources 1, 4).
- Artifact evaluation: optional, post-notification, sysartifacts-run, three badges
  (Available / Functional / Reproduced); the **Gilles Muller Best Artifact Award**
  has been given at recent editions (sources 5, 10; 2023 awards page).
- EuroSys 2025 (20th edition): Rotterdam, March 30 – April 3, 2025, co-located with
  ASPLOS 2025 (the first joint ASPLOS–EuroSys conference, per the SIGARCH trip
  report); best papers **CacheBlend** (DOI 10.1145/3689031.3696098, pp. 94–109) and
  **SpInfer**; 85 accepted papers were reported from 696 submissions (secondary
  sources — treat counts as reported, not official).
- Organizer and fee model: EuroSys the conference is run by per-edition General and
  Program Chairs under the EuroSys chapter of ACM SIGOPS; there is **no standing
  editor-in-chief and no APC** — costs are conference registration, and proceedings
  access follows ACM DL policies. Chairs rotate every edition; re-check the current
  organization page before naming anyone.

## Still 待核实 (do not state as fact)

- EuroSys 2027 exact conference end date (April 19–23 vs 19–24 appear in different
  renderings), official notification and camera-ready dates as published on
  2027.eurosys.org itself.
- Whether the 2027 rounds include a rebuttal/author-response phase, its window and
  format (set per round in HotCRP).
- Whether appendices beyond references, or separate supplementary uploads, are
  permitted in the current round.
- The camera-ready page allowance, shepherding policy, registration and in-person
  presentation requirements for 2027.
- The EuroSys 2027 call for artifacts: dates, badge wording, kick-the-tires phase,
  and whether the Gilles Muller Best Artifact Award is given in 2027.
- EuroSys 2026/2027 program-chair names and acceptance statistics.
- Any AI/LLM-use policy for authors or reviewers in the 2027 cycle.
