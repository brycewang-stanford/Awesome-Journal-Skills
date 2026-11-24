# Official Source Map - OSDI

Access date: **2026-07-08** (OSDI '26 snapshot). OSDI '27 conference page, Call for Papers
(including its September and October 2026 updates), Requirements for Authors, the
`osdi27.usenix.hotcrp.com` deadline clock, the OSDI '26 conference page and Call for
Artifacts **re-verified 2026-11-24** against the live pages (direct fetch with `curl`; the
403 block recorded in July no longer applies to `usenix.org`).

**Edition status, checked 2026-11-24.** The live edition is **OSDI '27**, the **21st** USENIX
Symposium on Operating Systems Design and Implementation, **July 7–9, 2027, Hyatt Regency
Baltimore Inner Harbor, Baltimore, MD, USA** ("Sponsored by USENIX in cooperation with ACM
SIGOPS"). Its Call for Papers is published, so this pack now describes OSDI '27. The single
submission gate is **open**: abstract registration **Tuesday, December 1, 2026** and complete
papers **Tuesday, December 8, 2026**, both **5:59 pm EST (10:59 pm UTC)**; notification
**March 16, 2027**; final papers **June 3, 2027**. OSDI '26 (20th, Seattle, July 13–15, 2026)
has met; its facts are kept below as labelled history. The OSDI '27 Call for Artifacts is not
yet published (its URL returns 404), so the OSDI '26 artifact rules are the latest published.

This map records the official sources behind every OSDI-specific fact in this pack.
OSDI policy is re-set each cycle by rotating Program Co-Chairs; reopen the current Call
for Papers, Requirements for Authors, Call for Artifacts, and the HotCRP site before
giving submission-ready advice.

## Access-method note

On 2026-07-08 direct requests to `usenix.org` returned **HTTP 403** from the verification
environment, and the OSDI '26 facts were read through search-engine renderings of the exact
official URLs, cross-checked against dblp and the HotCRP site. On **2026-11-24** `usenix.org`
and `osdi27.usenix.hotcrp.com` answered direct `curl -sL` requests (HTTP 200), so every OSDI
'27 fact below was read from the live page text. dblp exemplar checks were not repeated.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.usenix.org/conference/osdi27 | OSDI '27 identity: 21st USENIX Symposium on Operating Systems Design and Implementation, July 7–9, 2027, Hyatt Regency Baltimore Inner Harbor, Baltimore, MD, USA; sponsored by USENIX in cooperation with ACM SIGOPS; abstract registrations due December 1, 2026, complete papers December 8, 2026. | 2026-11-24 |
| 2 | https://www.usenix.org/conference/osdi27/call-for-papers | OSDI '27 CFP (PDF edition `osdi27_cfp_112326.pdf`): dates (abstracts December 1, 2026 and papers December 8, 2026, 5:59 pm EST / 10:59 pm UTC; notification March 16, 2027; final papers June 3, 2027); "New in 2027" — possible preliminary/early review round, no stated goal acceptance rate, and (October 2026 update) a required **Volunteer Candidate Senior Reviewer** per submission who may review up to four papers (exemptions for PC-member papers or when no author qualifies); continued from 2026 — Operational Systems track, resubmissions must describe improvements, at most eight submissions per author, conditional acceptance with no revise-and-resubmit; October 2026 update: an early review round, if volume requires, reads at least the first two pages; wholly or largely AI-generated text is fraud, AI editing tools acceptable, coding-agent use must be disclosed in the paper (e.g. the Implementation section); September 2026 update: NSDI '27 Fall submissions count as simultaneous and are desk-rejected; USENIX Authorship Policy; improved resubmissions of papers rejected elsewhere must upload prior-submission information and an improvement summary (shared with reviewers after reviews, before decisions); workshop-paper upload and explanation; arXiv/tech reports/talks/social media permitted under a different anonymized project/system name, and authors may post submissions on arXiv; co-chair submission handling; at least one full-price registration per paper; 12 single-spaced pages including figures and tables plus references, 10-point Times-like type on 12-point leading, two columns, 7" x 9" block, numbered pages; accepted papers 14 pages plus references; non-conforming papers desk-rejected; Research and Operational Systems tracks (Operational titles end with "(Operational Systems)"; real company/system names allowed there); **supplementary material in separate files** permitted, not required reading; double-blind with mandatory institution anonymization for the Research track; placeholder abstracts desk-rejected; conflict definitions (collaboration window December 2024 through December 2026); conditional acceptance via heavyweight shepherding, changes due by the final paper deadline; Program Co-Chairs Philip Levis and Junfeng Yang. | 2026-11-24 |
| 3 | https://www.usenix.org/conference/osdi27/requirements-authors | Submission requirements: PDF; at most 12 single-spaced 8.5" x 11" pages including figures and tables plus references, **no supplementary material in appendices**; 10-point Times Roman on 12-point leading; 7" x 9" (178 mm x 229 mm) two-column block with 0.33" (8 mm) gap; papers not meeting the criteria rejected without review; numbered pages; double-blind; USENIX Word/LaTeX templates; Code of Ethics — no out-of-band author–PC contact, and "Authors must abide by the ACM Code of Ethics". | 2026-11-24 |
| 4 | https://osdi27.usenix.hotcrp.com/deadlines | OSDI '27 HotCRP clock: registration deadline Tuesday Dec 1, 2026, 2:59:59 PM PST; submission deadline Tuesday Dec 8, 2026, 2:59:59 PM PST (the same instants as 5:59 pm EST). | 2026-11-24 |
| 5 | https://www.usenix.org/conference/osdi26/call-for-artifacts | OSDI '26 artifact evaluation (latest published call; `osdi27/call-for-artifacts` returns 404 on 2026-11-24): single **Artifacts Available** badge (narrowed from prior multi-badge years); artifact submission after (conditional) acceptance, deadline May 8, 2026, 8:59 pm PDT; Zenodo encouraged, institutional and third-party repositories acceptable. | 2026-11-24 |
| 6 | https://www.usenix.org/conference/osdi26 | OSDI '26 identity: 20th edition, July 13–15, 2026, Seattle, WA, USA (The Westin Seattle). | 2026-11-24 |
| 7 | https://www.usenix.org/conference/osdi26/call-for-papers | OSDI '26 CFP (history): registration December 4, 2025 and submission December 11, 2025, 2:59 pm PST; 12-page limit; **no appendix or supplementary material at submission**; elimination of the author-response period; conditional acceptance; eight-submission cap; Program Co-Chairs Eddie Kohler (Harvard University) and Amar Phanishayee (NVIDIA). | 2026-07-08 |
| 8 | https://www.usenix.org/conference/osdi26/requirements-authors | OSDI '26 final papers: no longer than 14 pages plus references and appendices; due June 9, 2026; notification March 26, 2026; optional two-page Artifact Appendix for papers passing artifact evaluation. | 2026-07-08 |
| 9 | https://www.usenix.org/conferences/byname/179 | Index of all OSDI editions and their official pages. | 2026-07-08 |
| 10 | https://www.usenix.org/blog/announcement-about-osdi | USENIX announcement that OSDI runs annually beginning 2021. | 2026-07-08 |
| 11 | https://www.usenix.org/blog/usenix-atc-announcement | USENIX announcement ending the USENIX Annual Technical Conference after ATC '25; see also https://www.usenix.org/blog/preserving-legacy-usenix-atc on the transition of ATC to ACM SIGOPS stewardship. | 2026-07-08 |
| 12 | https://www.usenix.org/conference/osdi-08/inauguration-jay-lepreau-award-best-paper-presented-8th-osdi | Inauguration of the Jay Lepreau Award for Best Paper at the 8th OSDI (2008); USENIX open-access commitment (papers free to everyone once the event begins). | 2026-07-08 |

## Cross-checks

- dblp OSDI series: https://dblp.org/db/conf/osdi/index.html — used to verify exemplar
  papers (e.g., `conf/osdi/DeanG04`, `conf/osdi/YuJKKC22`) and edition numbering.
- sysartifacts community pages: https://sysartifacts.github.io/ — historical OSDI
  artifact-evaluation calls (e.g., `osdi2021/call`, `osdi2023/artifacts-call`) showing
  the earlier Available / Functional / Reproduced badge triple.

## Verified OSDI '27 facts used in skills (re-verified 2026-11-24)

- OSDI '27 = **21st** edition, **July 7–9, 2027**, Hyatt Regency Baltimore Inner Harbor,
  Baltimore, MD, USA; sponsored by USENIX in cooperation with ACM SIGOPS (source 1).
- Program Co-Chairs: **Philip Levis** (Stanford University and Google) and **Junfeng Yang**
  (Columbia University) (source 2).
- One gate: abstract registration **December 1, 2026** and complete papers **December 8,
  2026**, both **5:59 pm EST (10:59 pm UTC)**, shown on HotCRP as 2:59:59 PM PST; hard
  deadlines, no extensions; notification **March 16, 2027**; final papers **June 3, 2027**
  (sources 2, 4).
- Tracks: **Research** and **Operational Systems**; Operational titles end with
  "(Operational Systems)", the track is marked on the title page and the form, and real
  company/system names may be used there (source 2).
- Submissions: at most **12** single-spaced 8.5" x 11" pages including figures and tables,
  10-point Times-like type on **12**-point leading, two columns, 7" x 9" block, numbered
  pages, plus unlimited reference pages; **no appendices in the PDF**; non-conforming papers
  are desk-rejected (sources 2, 3). Accepted papers get **14** pages plus references (source 2).
- **Supplementary material** may be uploaded **in separate files** (proof details, code
  snippets, methodological detail); PC members need not read it and the paper must stand
  alone — a change from OSDI '26, which allowed no supplementary material (sources 2, 7).
- Review: double-blind; institution anonymization mandatory for the Research track; arXiv,
  tech reports, talks and social media permitted under an anonymized project/system name
  different from the submission's; placeholder abstracts desk-rejected; at most **eight**
  submissions per author (source 2).
- **New in 2027:** no stated goal acceptance rate; an **early review round** if volume
  requires, in which reviewers read at least the first **two** pages and vote on advancing;
  every submission names a **Volunteer Candidate Senior Reviewer** (an author with a PhD or
  equivalent and a significant OSDI/SOSP-class record, not on the PC) who may be invited to
  review up to **four** papers, unless exempt (source 2).
- **Resubmissions:** papers previously rejected by another conference or journal must upload
  the prior-submission information and a summary of improvements, shared with reviewers after
  reviews and before decisions; NSDI '27 Fall submissions (notified the same day as the OSDI
  '27 deadline) count as simultaneous submissions and are desk-rejected (source 2).
- **AI:** submitting a paper whose text was wholly or largely generated by AI is fraud; AI
  editing tools are acceptable; a system built with **coding agents** must disclose their use
  in the paper (e.g. in the Implementation section); USENIX Authorship Policy applies
  (source 2).
- **Outcomes:** conditional acceptance via heavyweight shepherding (changes may require new
  technical work and must be done by the final-paper deadline), **no revise-and-resubmit**; the
  '27 CFP describes no author-response period (OSDI '26 eliminated it) (sources 2, 7).
- **Registration:** at least one author per accepted paper registers at **full price** (not the
  student rate) and presents (source 2).
- **Ethics:** no out-of-band author–PC contact; authors must abide by the **ACM Code of
  Ethics** (source 3).
- Publication: USENIX open-access proceedings, free to everyone from the first day of the
  event; no author publication charge (sources 2, 12).
- Cadence: OSDI annual since 2021 (source 10). Awards: Jay Lepreau Best Paper Award,
  inaugurated at OSDI '08 (source 12). ATC: USENIX ATC ended after ATC '25; its successor is
  stewarded by ACM SIGOPS (source 11).

## OSDI '26 (history)

- 20th edition, Seattle, July 13–15, 2026; Program Co-Chairs Eddie Kohler and Amar
  Phanishayee (sources 6, 7).
- Registration December 4, 2025 and submission December 11, 2025 (2:59 pm PST);
  notification March 26, 2026; final papers June 9, 2026, 14 pages plus references and
  appendices, optional two-page Artifact Appendix (sources 7, 8).
- No appendix or supplementary material at submission; no author-response period (source 7).
- Artifacts: only the **Artifacts Available** badge, submission May 8, 2026, 8:59 pm PDT
  (source 5).

## 待核实 (could not be verified on 2026-11-24)

- **OSDI '27 Call for Artifacts** (badge set, dates) — URL returns 404.
- Whether OSDI '27 will actually run the early review round (decided by submission volume).
- OSDI '27 final-paper appendix allowance and Artifact Appendix rules (the '27 Requirements
  page covers submissions only; the '26 rules were 14 pages plus references and appendices).
- Registration rates, student grants and hardship discounts for OSDI '27.
- Poster session mechanics and co-located events.

## Still cycle-volatile

Deadlines and their time-zone convention, page budgets, the appendix/supplementary rules,
the author-response policy, early-review and reciprocal-reviewer mechanics, badge sets,
track structure, the per-author submission cap, shepherding practice, and every organizer
name. OSDI '27 changed at least three things relative to OSDI '26 (supplementary files,
senior-reviewer nomination, early review round) — assume nothing carries forward.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "USENIX OSDI '27",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 12, "source": "https://www.usenix.org/conference/osdi27/call-for-papers", "note": "OSDI '27 submissions: 12 single-spaced pages including figures and tables, references extra, no appendices; accepted papers get 14 pages plus references"},
    "page_limit_includes_references": {"value": false, "source": "https://www.usenix.org/conference/osdi27/requirements-authors"},
    "review_mode": {"value": "double-blind", "source": "https://www.usenix.org/conference/osdi27/call-for-papers", "note": "institution anonymization mandatory for the Research track; Operational Systems track may name companies and systems"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://www.usenix.org/conference/osdi27/call-for-papers", "note": "a system developed with coding agents must disclose their use in the paper (e.g. the Implementation section)"},
    "template": {"value": "USENIX two-column, 10-point Times Roman on 12-point leading, 7 x 9 inch (178 x 229 mm) block, 0.33 inch column gap, 8.5 x 11 inch paper, numbered pages; non-conforming papers desk-rejected", "source": "https://www.usenix.org/conference/osdi27/requirements-authors"},
    "file_format": {"value": "PDF", "source": "https://www.usenix.org/conference/osdi27/requirements-authors"},
    "portal": {"value": "HotCRP (osdi27.usenix.hotcrp.com); abstracts December 1, 2026 and papers December 8, 2026, 5:59 pm EST", "source": "https://osdi27.usenix.hotcrp.com/deadlines"},
    "supplement_policy": {"value": "no appendices in the paper PDF; supplementary material allowed in separate files, not required reading", "source": "https://www.usenix.org/conference/osdi27/call-for-papers"},
    "preprint_policy": {"value": "arXiv, tech reports, talks and social media permitted, but the submission must use an anonymized project/system name different from those used publicly", "source": "https://www.usenix.org/conference/osdi27/call-for-papers"},
    "llm_policy": {"value": "text wholly or largely generated by AI is fraud; AI editing tools acceptable; coding-agent use in building the system must be disclosed in the paper; USENIX Authorship Policy", "source": "https://www.usenix.org/conference/osdi27/call-for-papers"},
    "data_code_policy": {"value": "post-acceptance artifact evaluation; the latest published call (OSDI '26) evaluated only the Artifacts Available badge; OSDI '27 call not yet published", "source": "https://www.usenix.org/conference/osdi26/call-for-artifacts"},
    "submission_fee": {"value": null, "note": "no submission fee or APC stated on the official pages as of 2026-11-24; at least one author per accepted paper registers at full price"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24; placeholder abstracts are desk-rejected"}
  }
}
```
