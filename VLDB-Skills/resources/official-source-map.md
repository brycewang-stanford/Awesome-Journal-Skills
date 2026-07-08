# Official Source Map - VLDB / PVLDB

Access date: 2026-07-08

This map records the official sources behind every VLDB-specific fact in this pack.
VLDB research papers are submitted to PVLDB (Proceedings of the VLDB Endowment) on a
rolling monthly calendar, and each PVLDB volume re-publishes its own submission
guidelines. Reopen the guidelines page of the volume you are actually submitting to —
not last volume's page — before giving deadline-ready advice.

**Access-method note (2026-07-08):** direct fetches of `vldb.org`, `dl.acm.org`,
`dblp.org`, and `web.archive.org` all returned HTTP 403 through the network gateway
used for this build. Page contents were therefore verified through search-engine
renderings of the exact URLs, cross-checked across the VLDB 2026 and VLDB 2027 site
pages, award announcements from the winners' institutions, and a GitHub-hosted mirror
of the PVLDB Vol 16 formatting instructions. Where a rendering could describe either a
current or a historical page, the fact is dated to its volume or listed under 待核实.
Open the primary URLs in a browser before relying on any deadline or rule.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.vldb.org/2027/submission-guidelines.html | PVLDB Volume 20 rolling calendar: first monthly deadline April 1, 2026 and final deadline March 1, 2027; deadlines on the 1st of each month at 5:00 PM Pacific Time with a mandatory abstract by the 25th of the previous month; CMT opens for each cycle on the 20th of the previous month; strict deadlines with no extensions; initial reviews usually on the 15th of the month after the deadline with accept, reject, or revision outcomes; only one revision permitted, with up to three months to produce it; per-author caps of two papers per month (carried from Vol 19) plus a new twelve-papers-per-year cap; supplementary availability earns an official ACM badge; authors encouraged to enter the PVLDB Reproducibility Evaluation and compete for the Best Reproducible Paper Award. | 2026-07-08 |
| 2 | https://vldb.org/2027/call-for-research-track.html | PVLDB as the only submission channel for research papers appearing at the VLDB 2027 conference. | 2026-07-08 |
| 3 | https://vldb.org/2027/ | VLDB 2027 identity: 53rd International Conference on Very Large Data Bases, Athens, Greece, August 23-27, 2027. | 2026-07-08 |
| 4 | https://www.vldb.org/2026/submission-guidelines.html | PVLDB Volume 19 rolling calendar: monthly deadlines on the 1st (5:00 PM PT) with abstracts due the 25th of the prior month; papers accepted by June 15, 2026 form the VLDB 2026 research track, together with rollover papers from Volume 18. | 2026-07-08 |
| 5 | https://www.vldb.org/2026/call-for-research-track.html | Research-track paper categories and page budgets for the VLDB 2026 cycle: Regular Research Papers and Experiment, Analysis & Benchmark (EA&B) Papers up to 12 pages excluding references; Scalable Data Science Papers up to 8 pages; Vision Papers up to 6 pages; EA&B papers required to release all experimental data and software and to submit their experiments to the PVLDB Reproducibility Committee. | 2026-07-08 |
| 6 | https://vldb.org/2026/ | VLDB 2026 identity: 52nd International Conference on Very Large Data Bases, Boston, MA, USA, August 31 - September 4, 2026. (London hosted VLDB 2025, September 1-5, 2025 — do not confuse the two.) | 2026-07-08 |
| 7 | https://vldb.org/2026/call-for-demonstrations.html | VLDB demonstration submissions are single-anonymous and must carry author names and affiliations — the anonymity-model data point supporting the single-blind reading below. | 2026-07-08 |
| 8 | https://vldb.org/pvldb/reproducibility (cross-checked via https://dl.acm.org/doi/10.14778/3685800.3685840, "A Reproducible Tutorial on Reproducibility in Database Systems Research," PVLDB Vol 17) | The pVLDB Reproducibility Evaluation: developed jointly with SIGMOD's effort starting with pVLDB 2018; the artifact surfaces evaluators expect — the prototype with source, configuration, and build environment; input data and its generation process; the experiment workload and configuration; and the scripts that turn raw results into the paper's figures and tables. | 2026-07-08 |
| 9 | https://www.vldb.org/awards_10year.html (cross-checked via https://www.cwi.nl/en/news/2025-vldb-test-of-time-award-for-cwi-researcher-peter-boncz/ and https://cse.osu.edu/news/2024/09/cse-researchers-honored-2024-vldb-endowment-test-time-award) | VLDB Test of Time lineage used in the exemplars library: 2025 award to Leis, Gubichev, Mirchev, Kemper, Neumann & Boncz, "How Good Are Query Optimizers, Really?" (PVLDB 2015); 2024 award to the Hadoop-GIS spatial warehousing paper (2013); the VLDB 2015 ten-year award to C-Store (VLDB 2005). | 2026-07-08 |
| 10 | https://dblp.org/rec/journals/pvldb/HuangLCFMXSTZHW20.html (cross-checked via https://www.vldb.org/pvldb/vol13/p3072-huang.pdf) | Huang et al., "TiDB: A Raft-based HTAP Database," PVLDB 13(12): 3072-3084, 2020 — industrial-systems exemplar verification. | 2026-07-08 |
| 11 | https://github.com/BU-DiSC/pvldb-pdfa-resources/blob/main/VLDB-formatting.md | PVLDB Vol 16 formatting anchor (historical): volume-specific template from vldb.org/pvldb/volumes/16/formatting; PDF/A-2 or newer with all fonts embedded; no font below LaTeX scriptsize in figures; camera-ready file named p[ID]-[lastname].pdf plus a signed copyright form; demo and tutorial papers 4 pages in that volume. | 2026-07-08 |
| 12 | https://dmki-tuwien.github.io/news-2026.html | Secondary source: Katja Hose and Matthias Boehm serve as PC co-chairs of VLDB 2027 / Editors-in-Chief of PVLDB Volume 20 (April 2026 announcement); the official officers page https://www.vldb.org/2027/officers.html could not be fetched directly. | 2026-07-08 |

## Verified facts used across the skills (as of 2026-07-08)

- PVLDB, not the conference site, is where VLDB research papers are submitted: acceptance
  into the volume is what earns the conference slot.
- The live volume on 2026-07-08 is **Volume 20** (deadlines April 1, 2026 through
  March 1, 2027, feeding VLDB 2027 in Athens). Volume 19's final deadline passed on
  March 1, 2026; its papers accepted by June 15, 2026 present at VLDB 2026 in Boston,
  and later Vol 19 acceptances roll forward.
- The monthly rhythm: abstract by the 25th, CMT opens the 20th, paper due the 1st at
  5:00 PM Pacific Time (not AoE), reviews around the 15th of the following month.
- Outcomes are accept, revise, or reject; a revision verdict is one-shot, with up to
  three months to return the revised paper.
- Per-author caps in Vol 20: two submissions per month and twelve per year.
- Research-track categories in the VLDB 2026 cycle: Regular Research (12 pp),
  EA&B (12 pp), Scalable Data Science (8 pp), Vision (6 pp), all excluding references;
  references are not capped, but appendices and acknowledgements count against the limit.
- Review is **single-blind**: VLDB has historically required author names and
  affiliations on the manuscript, the VLDB 2026 demonstrations call is explicitly
  single-anonymous, and no double-blind switch could be found for Vol 19 or Vol 20.
  Because the live guidelines page could not be opened directly, re-confirm the exact
  wording before submission (see 待核实).
- The platform is Microsoft CMT.
- Reproducibility: availability of supplementary materials earns an official ACM badge;
  the PVLDB Reproducibility Evaluation is opt-in for most categories, mandatory for
  EA&B papers, and carries a Best Reproducible Paper Award.
- VLDB is run by the VLDB Endowment. Like the other CS conferences in this collection
  it has no APC; PVLDB papers are openly accessible on vldb.org, and the cost model is
  conference registration. The rotating leadership analogue is the per-volume PVLDB
  Editors-in-Chief (who double as conference PC chairs) — re-check the current officers
  page rather than carrying names forward.

## 待核实 (could not be verified at build time — do not guess)

- The exact single-blind wording in the live Vol 20 research-track guidelines (direct
  fetch blocked; the reading above rests on renderings, historical continuity, and the
  2026 demos call).
- Whether Vol 20 keeps a June-15-style acceptance cutoff for VLDB 2027 presentation,
  and the exact date if so.
- Whether PVLDB imposes a resubmission embargo after a rejection, and its length.
- Current-cycle page budgets for demonstrations, tutorials, and the industrial track
  (the 4-page demo/tutorial figure is a Vol 16 anchor).
- Vol 20 camera-ready mechanics: per-issue deadlines, copyright workflow, and whether
  the p[ID]-[lastname].pdf email process from Vol 16 still applies.
- Vol 20 Editors-in-Chief as stated on the official officers page (secondary source
  only, see source 12).
- VLDB 2026/2027 registration pricing and the presentation obligation for accepted
  papers.
- Continuation of the Scalable Data Science and Vision categories in Vol 20 with
  unchanged page budgets.

## Still cycle-volatile

- Volume-to-conference mapping, monthly deadline pattern, abstract mechanics, caps,
  category list, page budgets, revision terms, reproducibility logistics, template
  versions, and officer names all reset with every volume. The only durable assumption
  is the rolling monthly model itself — and even that should be re-read annually.
