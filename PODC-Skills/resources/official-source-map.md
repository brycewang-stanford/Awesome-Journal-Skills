# Official Source Map - ACM PODC

Access date: 2026-07-09

This map records the official and cross-check sources used for PODC-specific facts in this pack.
PODC is the **ACM SIGACT-SIGOPS Symposium on Principles of Distributed Computing**, the flagship
for the *theory* of distributed computing; its calendar, page budget, and review model are decided
per edition. Reopen the current-cycle call for papers, the Important Dates page, and the HotCRP
site before giving submission-ready advice.

## Access method note

Direct fetches of `podc.org` and `dl.acm.org` failed from the verification gateway on 2026-07-09
(the same block seen when verifying other ACM venues). Official pages were therefore read through
**search-engine renderings of the exact URLs** and cross-checked against dblp, the ACM Digital
Library PODC proceedings, the **DMANET** call-for-papers announcement, wikicfp, and confsearch.
Facts that could not be pinned to a primary rendering are labeled **待核实**.

Two naming/attribution guards:

- **PODC is not PODS.** `PODS` (`Principles of Database Systems`) is the SIGMOD-week database-theory
  venue. No fact here derives from PODS. Search hits mentioning "PoDC / Proof of Double Committee"
  (a blockchain consensus product) are also unrelated and were discarded.
- **PODC is not DISC.** DISC (the EATCS International Symposium on DIStributed Computing) is the
  *other* distributed-theory flagship; PODC and DISC **share** the Dijkstra Prize and the Doctoral
  Dissertation Award but are distinct conferences with distinct calendars and proceedings (DISC uses
  LIPIcs; PODC uses the ACM proceedings). A famous result may have appeared at DISC, not PODC.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.podc.org/podc2026/call-for-papers/ | PODC 2026 call: scope, lightweight double-blind review, ACM Master template, 10-page-merits budget with unbounded full version, Brief Announcements track (≤5-page submission), arXiv freedom | 2026-07-09 |
| 2 | https://www.podc.org/podc2026/ | PODC 2026 (45th) home: Royal Holloway, University of London, Egham, England; July 6-10, 2026; co-located with SPAA 2026 | 2026-07-09 |
| 3 | http://dmatheorynet.blogspot.com/2026/01/dmanet-podc-2026-second-call-for-papers.html | PODC 2026 second CFP (DMANET): abstract 11 Feb 2026, full paper 16 Feb 2026, notification 29 Apr 2026, camera-ready 20 May 2026 (all 23:59 AoE) | 2026-07-09 |
| 4 | https://podc26.hotcrp.com/ | PODC 2026 submission site (HotCRP) | 2026-07-09 |
| 5 | https://www.podc.org/podc2026/program-committee/ | PODC 2026 program committee; Program Chair Eric Ruppert (roster beyond the chair is 待核实) | 2026-07-09 |
| 6 | https://dl.acm.org/doi/proceedings/10.1145/3732772 | ACM DL PODC 2025 proceedings (used to confirm the ACM two-column proceedings publication model and the conference series) | 2026-07-09 |
| 7 | https://dblp.org/db/conf/podc/podc2026.html | dblp PODC 2026 record (accepted-paper cross-check) and the PODC proceedings series for exemplar verification | 2026-07-09 |
| 8 | https://www.podc.org/dijkstra/ | Edsger W. Dijkstra Prize in Distributed Computing: joint PODC/DISC, decade-of-impact, presented alternately at PODC and DISC | 2026-07-09 |
| 9 | https://www.podc.org/dissertation/ | Principles of Distributed Computing Doctoral Dissertation Award (created 2012; joint PODC/DISC) | 2026-07-09 |
| 10 | https://spaa.acm.org/ | SPAA 2026 co-location at Royal Holloway, July 6-10, 2026 (confirms the shared venue/dates) | 2026-07-09 |

## Verified 2026 facts used in skills

- **PODC 2026 is the 45th ACM Symposium on Principles of Distributed Computing**, jointly sponsored
  by **ACM SIGACT and SIGOPS**, held at **Royal Holloway, University of London, Egham, England**,
  **July 6-10, 2026**, co-located with **SPAA 2026** (sources 1, 2, 10).
- **Calendar (all 23:59 AoE):** abstract registration **11 February 2026**, full-paper submission
  **16 February 2026**, notification **29 April 2026**, camera-ready **20 May 2026**; submission via
  `podc26.hotcrp.com` (sources 3, 4).
- **Review is lightweight double-blind:** submissions must not reveal author identity — no names,
  affiliations, or email addresses anywhere in the submission (source 1). This is a change from
  PODC's historically single-blind practice; verify the exact wording each cycle.
- **Format is the ACM Master template (`acmart`), two-column proceedings.** Regular submissions have
  **no page limit**, but only the abstract and the **first 10 pages after the title page** are
  guaranteed to be read; material beyond is read at the committee's discretion. Authors are
  encouraged to submit the **full version** (with proofs). Accepted regular papers appear in **≤10
  pages** in two-column ACM proceedings format (source 1).
- **Brief Announcements** are a distinct track: the **submission is at most 5 pages** (including
  title, abstract, and references); accepted Brief Announcements are published at **up to 3 pages**
  in the proceedings (source 1).
- **arXiv/preprint freedom:** authors may post drafts on the web, submit to arXiv, and give talks
  about the work; a preprint is not treated as a dual-submission problem (source 1).
- **Journal invitations:** selected papers are invited to the **Journal of the ACM (JACM)** and to a
  special issue of **Distributed Computing** (reported on the call/series pages).
- **Awards:** every regular paper is eligible for **Best Paper** and **Best Presentation**;
  student-authored papers (full-time students principally responsible) are eligible for **Best
  Student Paper** (source 1, historical CFPs). The **Dijkstra Prize** and the **Doctoral Dissertation
  Award** are held **jointly with DISC** (sources 8, 9).
- **Program Chair: Eric Ruppert** (source 5). Full committee roster beyond the chair is 待核实.

## The proofs-venue model (why there is no artifact track)

PODC evaluates a **model, a theorem, and a proof**. There is **no artifact-evaluation track and no
ACM badge program** at PODC — the analogue of "does the code run" is "does the proof close and are
the model, timing, and failure assumptions stated precisely and honestly." The `podc-experiments`,
`podc-reproducibility`, and `podc-artifact-evaluation` skills are therefore written for a proofs
venue: tight/matching bounds, self-contained proof appendices, checkable assumptions, and — only
where a paper includes them — transparent optional simulations. Do not import an ACM
Available/Functional/Reusable/Reproduced badge workflow; it does not exist here.

## No editor-in-chief; no APC

Like every conference in this collection, PODC has **no standing editor-in-chief**; the rotating
analogue is the per-edition **Program Chair** and program committee, appointed under ACM
SIGACT/SIGOPS. Proceedings are published by ACM; there is no APC, the cost model is conference
registration, and at least one author must present each accepted paper in person.

## Still cycle-volatile (verify every year)

- All dates and AoE cutoffs, and whether abstract registration precedes the full-paper deadline
  (2026 splits them: 11 Feb / 16 Feb).
- The exact double-blind wording and how strictly it is enforced (**recently changed**, so do not
  carry a prior year's single-blind assumption forward).
- Whether the cycle runs an **author-response / rebuttal** phase — **待核实** for 2026; PODC has not
  always had one.
- The page-budget wording (the 10-page-merits rule and the ≤10 / ≤3 published limits) and which
  `acmart` option/revision is required.
- Best-paper / best-student-paper / best-presentation mechanics and eligibility for 2026 (**待核实**
  beyond the general eligibility statement).
- Any generative-AI-use disclosure policy (**待核实**).
- The full PODC 2026 program-committee roster beyond Program Chair Eric Ruppert (**待核实**).
