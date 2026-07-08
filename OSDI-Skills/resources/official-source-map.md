# Official Source Map - OSDI

Access date: **2026-07-08**

This map records the official sources behind every OSDI-specific fact in this pack.
OSDI policy is re-set each cycle by rotating Program Co-Chairs; reopen the current Call
for Papers, Requirements for Authors, Call for Artifacts, and the HotCRP site before
giving submission-ready advice.

## Access-method note

Direct `WebFetch` requests to `usenix.org` (HTML pages and `sites/default/files` PDFs)
returned **HTTP 403** from the verification environment on 2026-07-08. All facts below
were therefore read through **search-engine renderings of the exact official URLs**
listed here, and cross-checked against dblp (`dblp.org/db/conf/osdi/`), the
`osdi26.usenix.hotcrp.com` site, and university/lab announcements where available.
Anything that could not be pinned to an official rendering is listed under 待核实, not
stated as fact. If you can open `usenix.org` directly, prefer the live pages over this
snapshot.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.usenix.org/conference/osdi26 | OSDI '26 identity: 20th USENIX Symposium on Operating Systems Design and Implementation, July 13–15, 2026, The Westin Seattle, Seattle, WA, USA; hardship-discount registration language. | 2026-07-08 |
| 2 | https://www.usenix.org/conference/osdi26/call-for-papers | Two reviewing tracks (Research, Operational Systems); topic scope; deadlines (registration Dec 4, 2025 and submission Dec 11, 2025, both 2:59 pm PST); 12-page limit including figures/tables plus unlimited references; no appendix material at submission; down-ranking of padded papers; double-blind rules including institution anonymization and the renamed-system rule for arXiv/tech-report/talk precursors; elimination of the author-response period; conditional acceptance with heavyweight shepherding; eight-submissions-per-author cap; Program Co-Chairs Eddie Kohler (Harvard University) and Amar Phanishayee (NVIDIA) and the co-chair-submission recusal rule. | 2026-07-08 |
| 3 | https://www.usenix.org/sites/default/files/osdi26_cfp_120325.pdf | PDF edition of the OSDI '26 CFP (December 2025 revision); earlier preliminary editions osdi26_cfp_070225.pdf and osdi26_cfp_101325.pdf exist. | 2026-07-08 |
| 4 | https://www.usenix.org/conference/osdi26/requirements-authors | Final papers no longer than 14 pages including figures and tables plus as many pages as needed for references and appendices; final printable PDF due June 9, 2026; acceptance notifications March 26, 2026; optional two-page Artifact Appendix for papers passing artifact evaluation. | 2026-07-08 |
| 5 | https://osdi26.usenix.hotcrp.com/deadlines | HotCRP as the OSDI '26 submission system; per-track registration and submission cutoffs in PST. | 2026-07-08 |
| 6 | https://www.usenix.org/conference/osdi26/call-for-artifacts | OSDI '26 artifact evaluation: single **Artifacts Available** badge this cycle (narrowed from prior multi-badge years); artifact submission after (conditional) acceptance, deadline May 8, 2026, 8:59 pm PDT; Zenodo encouraged, institutional and third-party repositories acceptable. | 2026-07-08 |
| 7 | https://www.usenix.org/conferences/byname/179 | Index of all OSDI editions and their official pages. | 2026-07-08 |
| 8 | https://www.usenix.org/blog/announcement-about-osdi | USENIX announcement that OSDI runs annually beginning 2021. | 2026-07-08 |
| 9 | https://www.usenix.org/blog/usenix-atc-announcement | USENIX announcement ending the USENIX Annual Technical Conference after ATC '25; see also https://www.usenix.org/blog/preserving-legacy-usenix-atc on the transition of ATC to ACM SIGOPS stewardship. | 2026-07-08 |
| 10 | https://www.usenix.org/conference/osdi27 | OSDI '27 official page exists (21st edition). Dates/venue reported by secondary aggregators as July 7–9, 2027, Baltimore, MD — treat as reported until read from this page directly. | 2026-07-08 |
| 11 | https://www.usenix.org/conference/osdi-08/inauguration-jay-lepreau-award-best-paper-presented-8th-osdi | Inauguration of the Jay Lepreau Award for Best Paper at the 8th OSDI (2008); USENIX open-access commitment (papers and proceedings free to everyone once the event begins) confirmed via USENIX conference-policy pages. | 2026-07-08 |

## Cross-checks

- dblp OSDI series: https://dblp.org/db/conf/osdi/index.html — used to verify exemplar
  papers (e.g., `conf/osdi/DeanG04`, `conf/osdi/YuJKKC22`) and edition numbering.
- HotCRP live site: https://osdi26.usenix.hotcrp.com/ — confirms the submission system
  and deadline framing independently of the CFP text.
- sysartifacts community pages: https://sysartifacts.github.io/ — historical OSDI
  artifact-evaluation calls (e.g., `osdi2021/call`, `osdi2023/artifacts-call`) showing
  the earlier Available / Functional / Reproduced badge triple.

## Verified 2026-cycle facts used in skills

- OSDI '26 = 20th edition, July 13–15, 2026, The Westin Seattle, Seattle, WA, USA.
- Program Co-Chairs: Eddie Kohler (Harvard University), Amar Phanishayee (NVIDIA).
- Tracks: Research and Operational Systems, both registered by December 4, 2025 and
  submitted by December 11, 2025, 2:59 pm PST, via HotCRP.
- Submissions: at most 12 single-spaced 8.5"×11" pages including figures and tables,
  10-point Times-like font on 12-point leading, two-column, 7"×9" text block, plus
  unlimited reference pages; appendices/supplementary material not permitted in the
  submission; reviewers encouraged to down-rank padded papers.
- Review: double-blind; authors anonymize themselves and their institutions; prior
  non-peer-reviewed exposure (arXiv, tech reports, talks, social media) permitted only
  under a project/system name different from the submission's; at most eight
  submissions per author; no author-response period; some papers accepted
  conditionally with shepherd-verified mandatory revisions; notification March 26, 2026.
- Artifacts: evaluation organized with the sysartifacts community after conditional
  acceptance; 2026 evaluates only the Artifacts Available badge; submission deadline
  May 8, 2026, 8:59 pm PDT; Zenodo and equivalent permanent repositories accepted.
- Final papers: due June 9, 2026; at most 14 pages plus references and appendices;
  optional two-page Artifact Appendix for AE-passing papers.
- Publication: USENIX open-access proceedings, free from the first day of the event;
  no author publication charge; the conference is funded by registration, with
  hardship discounts offered.
- Cadence: OSDI annual since 2021 (source 8); SOSP, its ACM sibling, annual since 2024
  (SIGOPS/sosp.org pages) — both flagships now offer a deadline every year.
- Awards: Jay Lepreau Best Paper Award, inaugurated at OSDI '08 (source 11).
- ATC: USENIX ATC ended after ATC '25; its successor is stewarded by ACM SIGOPS
  (source 9). OSDI '26 pages should not be assumed to carry ATC co-location logistics.

## 待核实 (could not be verified on 2026-07-08)

- **OSDI '27 CFP**: not yet readable — expected registration/submission deadlines
  (historically early-to-mid December of the prior year), page limits, response policy,
  and badge set for the '27 cycle. Official stub: source 10.
- **OSDI '27 dates/venue**: July 7–9, 2027, Hyatt Regency Baltimore Inner Harbor,
  Baltimore, MD appears only in secondary aggregators; confirm on source 10.
- **OSDI '26 registration rates and student grants**: hardship discounts are mentioned
  officially; exact fees, student grant program status, and presenter registration
  requirements were not readable.
- **AI/LLM authorship or disclosure policy** for OSDI '26: none surfaced in renderings;
  do not assert presence or absence.
- **Ethics-code citation**: one rendering attributed an "ACM Code of Ethics" clause to
  the OSDI '26 CFP; because OSDI is a USENIX venue this needs the exact CFP wording
  before being repeated.
- **Poster session mechanics** and the OSDI '26 call-for-posters details.
- **Camera-ready consent/copyright form specifics** beyond the June 9 PDF deadline.
- Whether any event is co-located with OSDI '26 after ATC's retirement.

## Still cycle-volatile

Deadlines and their time zone convention, page budgets, the no-appendix rule, the
author-response policy, badge sets, track structure, the per-author submission cap,
shepherding practice, and every organizer name. All were re-set at OSDI '26 relative
to OSDI '25 in at least two respects (response period, badges) — assume nothing
carries forward.
