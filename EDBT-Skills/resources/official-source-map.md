# Official Source Map - EDBT

Access date: 2026-07-09

This map records the official and cross-check sources used for EDBT-specific facts in this pack.
EDBT is the **International Conference on Extending Database Technology** — the European database-
systems flagship, held jointly with **ICDT** (its database-theory sibling) and published
**open-access on OpenProceedings.org** rather than in the ACM Digital Library or IEEE Xplore.
Its defining mechanic is a **multiple-cycle rolling submission model** (three cycles per year since
2022), each carrying an in-cycle **revise-and-resubmit** round. Reopen the current EDBT/ICDT host
site's research call, the Important Dates page, the OpenProceedings volume page, and the EDBT
Association pages before giving submission-ready advice.

## Access method note

Direct fetches of `edbticdt2026.github.io`, `edbt.org`, and `openproceedings.org` returned
**HTTP 403** from the verification gateway on 2026-07-09 (WebFetch of the EDBT 2026 research CFP
returned 403 Forbidden). Official pages were therefore read through **search-engine renderings of
the exact URLs** and cross-checked against the OpenProceedings.org volume tables of contents, the
EDBT Association site (`edbt.org`), dblp, WikiCFP, and the co-located ICDT call on
`databasetheory.org`. Facts that could not be pinned to at least two independent surfaces are
labeled **待核实**. Do not confuse EDBT (databases) with unrelated acronyms such as EDTM (IEEE
Electron Devices Technology and Manufacturing); no fact here derives from any non-database venue.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://edbticdt2026.github.io/ | EDBT/ICDT 2026 Joint Conference: 29th EDBT, Tampere, Finland, 24-27 March 2026 | 2026-07-09 |
| 2 | https://edbticdt2026.github.io/?contents=EDBT_CFP.html | EDBT 2026 Research Track call (identity, cycles, OpenProceedings publication) — read via rendering; 403 on direct fetch | 2026-07-09 |
| 3 | https://edbticdt2026.github.io/?contents=call_for_IAP.html | EDBT 2026 Industrial and Application Track existence | 2026-07-09 |
| 4 | https://edbt.org/ | EDBT Association: three submission/publication cycles since 2022; Microsoft CMT review; 12-month resubmission ban; publication timeline (Jul/Nov/Mar) | 2026-07-09 |
| 5 | https://openproceedings.org/ | OpenProceedings.org: open-access platform started by ICDT and EDBT; CC-BY-NC-ND, ISBN per volume, DBLP/Scholar/SCOPUS indexing | 2026-07-09 |
| 6 | https://openproceedings.org/html/pages/2026_edbt.html | OpenProceedings EDBT 2026 (29th) proceedings volume page | 2026-07-09 |
| 7 | https://conferences.inf.ed.ac.uk/edbticdt2022/contents/EDBT_CFP.html | EDBT 2022 research CFP: Regular & Experiments-&-Analysis ≤12 pages + unlimited references; Vision ≤6 pages; the five-step cycle timeline (submit → author feedback → accept/revise/reject → revision → accept/reject) | 2026-07-09 |
| 8 | http://www.wikicfp.com/cfp/program?id=830 | EDBT series cycle deadlines; EDBT 2027 cycle deadlines 4 Feb 2026 / 10 Jun 2026 / 7 Oct 2026 | 2026-07-09 |
| 9 | https://dblp.org/db/conf/edbt/index.html | EDBT proceedings series and the EDBT 2026 (29th) Tampere volume for edition number and exemplar verification | 2026-07-09 |
| 10 | https://databasetheory.org/node/152 + https://easychair.org/cfp/ICDT2026 | ICDT 2026 co-located theory call — the boundary between EDBT (systems/applied) and ICDT (theory) | 2026-07-09 |

## Verified 2026/2027 facts used in skills

- **EDBT 2026 is the 29th International Conference on Extending Database Technology**, held as the
  **EDBT/ICDT 2026 Joint Conference** in **Tampere, Finland, 24-27 March 2026**, organized by
  Tampere University (sources 1, 6, 9; Tampere University news). As of the 2026-07-09 access date
  this edition has already been held, so the live *next* research target is the EDBT 2027 cycle.
- **Publication is open-access on OpenProceedings.org**, the platform **started by ICDT and EDBT**;
  papers are licensed **CC-BY-NC-ND 4.0** with copyright retained by authors, each volume carries
  an **ISBN**, and volumes are indexed in **DBLP, Google Scholar, and SCOPUS** (sources 5, 6). EDBT
  proceedings have appeared on OpenProceedings since 2014. There is **no ACM/IEEE paywall and no
  article-processing charge**.
- **Multiple-cycle rolling model:** since 2022 EDBT runs **three submission/publication cycles per
  year** (source 4). Cycle publication clusters historically fall around **July, November, and
  March** (source 4; verify per edition).
- **In-cycle revise-and-resubmit:** each cycle runs submit → **author feedback phase** →
  notification of **accept / revise / reject** → **revised paper submission** → notification of
  **accept / reject** on the revision (source 7, EDBT 2022 timeline; treat exact dates as
  per-cycle).
- **EDBT 2027 cycle deadlines:** **4 February 2026**, **10 June 2026**, and **7 October 2026**
  (source 8). As of 2026-07-09, cycles 1 and 2 have passed and **cycle 3 (7 Oct 2026)** is the live
  upcoming deadline.
- **Paper shapes and page budget (EDBT 2022 research CFP, source 7 — reverify per cycle):**
  **Regular** research papers and **Experiments & Analysis** papers at most **12 pages** plus
  unlimited references; **Vision** papers at most **6 pages** plus unlimited references.
- **Review is managed in Microsoft CMT** (Conference Management Toolkit), with a **12-month
  resubmission ban** on work rejected or withdrawn from an EDBT track in the same paper format
  (source 4).
- **Additional tracks** at EDBT include **Industrial & Application**, **Demonstrations**,
  **Tutorials**, **Workshops** (EDBT/ICDT 2026 workshop proceedings appeared in CEUR-WS Vol-4192),
  and a **PhD Workshop** (sources 3, 4; CEUR-WS).
- **EDBT Test-of-Time Award** has run since 2014; from 2018 it honors the most impactful EDBT paper
  from **ten years prior** (source 4; Athena Research Center announcement).

## The multiple-cycle rolling model (honest reading of the cadence question)

EDBT's identity as a submission process is the **rolling three-cycle model**, not a single annual
deadline. A paper submitted to any cycle receives real reviews, an author-feedback exchange, and an
accept/**revise**/reject verdict; a *revise* becomes a revised submission re-read within the **same
cycle** before a final accept/reject. **Papers accepted in the earlier cycles of a conference year
present at that year's conference; papers accepted in the last cycle roll to the next year's
conference** — so the same physical meeting draws from multiple cycles, and one cycle's acceptances
seed the following edition. Whether a given year runs exactly three cycles, and the precise author-
feedback and revision dates inside each, are decided per edition — **verify the cycle count and the
per-cycle timeline on the current host site before advising**, and never carry a previous year's
calendar forward.

## No editor-in-chief; no APC; open access by construction

EDBT has **no standing editor-in-chief**; the rotating analogue is the per-edition General Chairs
and Program/PC Chairs appointed with the EDBT Association. OpenProceedings is **open access with no
article-processing charge**: the cost model is conference registration, at least one author
presents, and the published PDF is freely redistributable under CC-BY-NC-ND. This is the sharpest
structural contrast with the US database flagships (SIGMOD/ICDE in the ACM/IEEE paywalled DLs;
PVLDB as a journal-style monthly).

## Still cycle-volatile (verify every year)

- The number of cycles (three since 2022) and every per-cycle date, including author-feedback and
  revision windows and any AoE cutoffs.
- Exact page budgets per paper shape and the required OpenProceedings/host LaTeX template revision
  (12+unlimited / 6+unlimited read from the EDBT 2022 CFP — **待核实** for the current cycle).
- Whether reviewing is single-blind or double-blind for the current cycle (**待核实**; EDBT has
  historically used author-identified single-blind reviewing, unconfirmed to two surfaces here).
- Whether a distinct **short-paper** category is offered (EDBT 2021 called for short papers; EDBT
  2022 used Regular / Experiments-&-Analysis / Vision) — **待核实** per cycle.
- The EDBT reproducibility / availability mechanism and whether artifact submission or a badge is
  offered or required (**待核实**; the database community's reproducibility roots trace to EDBT/
  SIGMOD, but EDBT's exact current program is unconfirmed here).
- EDBT 2027 host city and country, and the full EDBT 2026/2027 General/PC Chair rosters
  (**待核实**).
- Any generative-AI authorship or disclosure policy (**待核实**).
