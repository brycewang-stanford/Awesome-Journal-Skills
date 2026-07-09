# Official Source Map - IEEE PerCom

Access date: 2026-07-09

This map records the official and cross-check sources used for PerCom-specific facts in this
pack. PerCom is the **IEEE International Conference on Pervasive Computing and Communications**,
the IEEE flagship for human-centric ubiquitous computing; its papers publish in **IEEE Xplore**,
review runs a **single annual cycle with a rebuttal round and an early-rejection stage**, and the
page budget and format follow the **IEEE two-column conference template**. Its calendar, page
budget, and review mechanics are decided per edition. Reopen the current-cycle Call for Papers,
the Dates page, and the HotCRP site before giving submission-ready advice.

## Access method note

Direct fetches of `percom.org` (and its `www.percom.org` mirror) returned **HTTP 403** from the
verification gateway on 2026-07-09 (the same block pattern seen across conference sites in this
build). Official pages were therefore read through **search-engine renderings of the exact URLs**
(percom.org/dates, percom.org/call-for-papers, percom.org/call-for-wip-papers) and cross-checked
against the PerCom HotCRP site, IEEE Xplore / IEEE Computer Society Digital Library (CSDL) tables
of contents, dblp, and independent CFP aggregators (wikicfp, clocate). Facts that could not be
pinned to at least two surfaces are labeled **待核实**. Note the temporal frame: as of the
2026-07-09 access date, **PerCom 2026 (Pisa, 16-20 March 2026) has already concluded**, so the
live *next* research target is **PerCom 2027 (Goa, India, 8-12 March 2027)** — all
submission-cycle advice anchors to the PerCom 2027 call.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://percom.org/call-for-papers/ | PerCom 2027 research-papers identity, double-blind review, 9+1-page IEEEtran budget, rebuttal-based single round, IEEE publication | 2026-07-09 |
| 2 | https://percom.org/dates/ | PerCom 2027 Important Dates: paper registration 4 Sep 2026, submission 11 Sep 2026 AoE, early-reject/rebuttal invitation 20 Nov 2026, rebuttal 26 Nov 2026, notification 18 Dec 2026 | 2026-07-09 |
| 3 | https://percom.org/ | PerCom 2027 (25th edition) home: Goa, India, 8-12 March 2027, physical in-person | 2026-07-09 |
| 4 | https://percom2027.hotcrp.com/ | PerCom 2027 submission site (HotCRP) for the main conference and associated events | 2026-07-09 |
| 5 | https://percom.org/call-for-wip-papers/ | Work-in-Progress track: ≤4 pages two-column IEEE style; accepted to PerCom Workshops proceedings on IEEE Xplore; Best WiP award | 2026-07-09 |
| 6 | https://percom.org/2025/best-paper-award-details/ | Mark Weiser Best Paper Award (sponsored by Elsevier), PerCom's flagship paper award | 2026-07-09 |
| 7 | https://percom.org/2026/ | PerCom 2026 (24th): Pisa, Italy, 16-20 March 2026; inaugural PerCom Test of Time Award | 2026-07-09 |
| 8 | https://dblp.org/db/conf/percom/index.html | PerCom proceedings series (edition/year mapping) and exemplar verification | 2026-07-09 |
| 9 | https://www.ubicomp.org/ubicomp-iswc-2025/imwut_papers/ | Neighboring venue: ACM UbiComp/ISWC and its IMWUT journal (rolling quarterly deadlines), contrasted with PerCom's annual IEEE cycle | 2026-07-09 |
| 10 | https://www.hkust-gz.edu.cn/2026/03/21/hkustgz-wins-landmark-awards-at-ieee-percom-2026/ | PerCom 2026 Test of Time Award (inaugural) honoring "LANDMARC: Indoor Location Sensing Using Active RFID" (PerCom 2003) | 2026-07-09 |

## Verified 2026/2027 facts used in skills

- **PerCom 2027 is the 25th IEEE International Conference on Pervasive Computing and
  Communications**, held in **Goa, India, 8-12 March 2027**, as a physical in-person conference
  (remote/pre-recorded presentation is not permitted except in special circumstances). As of the
  2026-07-09 access date, this is the live next research target (source 1, 3).
- **PerCom 2027 research-track calendar:** mandatory **paper registration 4 September 2026**, full
  **paper submission 11 September 2026** (23:59 AoE); **early rejection or invitation to submit a
  rebuttal 20 November 2026 AoE**; **rebuttal submission 26 November 2026 AoE**; **acceptance
  notification 18 December 2026** — all via `percom2027.hotcrp.com` (sources 2, 4).
- **Format and page budget:** IEEE two-column conference style, **`\documentclass[10pt,
  conference, compsocconf]{IEEEtran}`**, **at most 9 pages** of technical content (text, figures,
  tables, appendices) **plus up to 1 additional page for references only** (source 1).
- **Review is double-blind:** authors anonymize the submission in good faith and cite their own
  prior work in the third person (not omit it). Each reviewed paper is assigned to **three TPC
  members** (source 1).
- **Single-round rebuttal with early rejection:** after the initial reviews, papers for which at
  least one reviewer sees a path to publication (rates "weak accept" or better) are **invited to
  rebuttal**; papers with no positive review are **early-rejected** so authors can move on. The
  rebuttal addresses explicit reviewer questions and resolves misunderstandings; **additional
  experiments are not expected** (source 1).
- **Publication venue is IEEE:** accepted main-conference papers appear in the PerCom proceedings
  on **IEEE Xplore**; workshop, WiP, and demo papers appear in the separate **PerCom Workshops**
  proceedings on IEEE Xplore (sources 1, 5).
- **Mark Weiser Best Paper Award** (sponsored by Elsevier) is PerCom's flagship paper honor; the
  **Best WiP** award recognizes the top Work-in-Progress contribution (sources 5, 6).
- **PerCom Test of Time Award** was inaugurated at **PerCom 2026** (Pisa) and honored "LANDMARC:
  Indoor Location Sensing Using Active RFID" (PerCom 2003); it recognizes a paper of sustained
  impact from roughly the past two decades (sources 7, 10).

## The rebuttal single-round model (honest reading of the cycle)

PerCom runs **one annual submission deadline** feeding a **single review round with a rebuttal**,
not a journal-style revise-and-resubmit and not a multi-deadline conference. Two features shape
author strategy: (1) an **early-rejection stage** ends the process for papers with no positive
review before the rebuttal even opens — there is no rebuttal for those papers; (2) the **rebuttal
is bounded** — it answers explicit reviewer questions and clears misreadings, and the call states
that new experiments are not expected, so the submitted paper must already carry its evidence.
There is no second submission within the cycle: a rejected paper reworks and targets the next
PerCom (or a neighboring venue). Verify the exact rebuttal length, eligibility threshold, and the
early-reject wording on the current call before advising.

## No editor-in-chief; conference cost model

Like every conference in this collection, PerCom has **no standing editor-in-chief**; the rotating
analogue is the per-edition **General Chairs and TPC (Program) Co-Chairs**, appointed by the
PerCom steering committee under IEEE Computer Society sponsorship. There is no article-processing
charge in the open-access sense; the cost model is **IEEE conference registration**, and at least
one author must present in person.

## PerCom vs. its neighbor IMWUT/UbiComp (why the distinction matters)

PerCom and ACM **UbiComp/ISWC** overlap heavily in topic (activity recognition, wearables, smart
environments), but differ structurally: UbiComp presents papers published in the ACM journal
**IMWUT (Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies)**,
which runs **rolling quarterly deadlines** and a revise-cycle; PerCom is an **IEEE conference**
with a **single annual deadline**, a **rebuttal round**, and IEEE Xplore proceedings. Authors
choosing between them are choosing a publication model and a calendar as much as a community
(sources 1, 9).

## Still cycle-volatile (verify every year)

- All dates and AoE cutoffs, and whether the rebuttal window shifts.
- Exact page budget and the required IEEEtran options (PerCom 2027 posts 9+1 with
  `compsocconf`).
- Rebuttal length limit, the exact "weak accept" eligibility wording, and early-reject mechanics.
- Whether a formal **artifact-evaluation / reproducibility badge** track runs, and which badges
  (IEEE Open Research Objects / Results Reproduced, or none) — **待核实**.
- Open-data / dataset-sharing wording and any generative-AI or human-subjects (IRB) disclosure
  policy — **待核实**.
- PerCom 2027 full TPC/Program Co-Chair roster and camera-ready dates — **待核实**.
- Exact per-cycle acceptance rate; historically PerCom reports roughly **14-15%** full-paper
  acceptance, but the PerCom 2027 figure is **待核实** until published.
