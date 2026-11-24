# Official Source Map - ESEC/FSE

Access date: 2026-07-09. FSE 2027 research-papers call, Important Dates, organizing committee,
page budget, review process, open-science, generative-AI and open-access/APC policy
**re-verified 2026-11-24** against the live conf.researchr.org pages (direct fetch); the
ESEC/FSE Test of Time page was re-read the same day.

**Edition status, checked 2026-11-24.** The latest published edition is **FSE 2027**, the 35th
ACM International Conference on the Foundations of Software Engineering, **Shenzhen, China,
July 12-16, 2027**. Its research-papers call and Important Dates page are live and its single
research deadline has passed (full paper **October 2, 2026**, extended by one day to **October
3, 2026** AoE after a system-wide HotCRP outage), so FSE 2027 is mid-review: author response
**December 14-18, 2026**, initial notification **January 22, 2027**, major-revision submission
**March 5, 2027**, final notification **March 31, 2027**. This pack describes FSE 2027. FSE 2026
(Montreal, July 5-9, 2026) has met and is kept below as labelled history. The next FSE edition has no
page yet (`conf.researchr.org/home/fse-2028` returns 404 on 2026-11-24): location, dates and
call not announced.

This map records the official and cross-check sources used for FSE-specific facts in this
pack. FSE is the ACM SIGSOFT flagship whose research papers are published as journal articles
in **PACMSE (Proceedings of the ACM on Software Engineering)**; its calendar, page budget, and
review mechanics are decided per edition. Reopen the current-cycle research-papers call, the
Important Dates page, the PACMSE journal pages, and the ACM artifact policy before giving
submission-ready advice.

## Access method note

On 2026-07-09 direct fetches of `conf.researchr.org` and `dl.acm.org` returned **HTTP 403** and
official pages were read through search-engine renderings of the exact URLs. On **2026-11-24**
every `conf.researchr.org` page, the FSE HotCRP front pages and `esec-fse.org` were fetched
**directly** (HTTP 200); `dl.acm.org` and `acm.org` still return HTTP 403 to automated fetches,
so the PACMSE journal-page and ACM badging rows are carried from 2026-07-09. Beware a name
collision: `fse.iacr.org` is *Fast Software Encryption*, a cryptography conference, and is
**not** this FSE — no fact here derives from it.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://conf.researchr.org/track/fse-2027/fse-2027-papers | FSE 2027 (35th) research-papers call: submission at fse2027.hotcrp.com; deadline extended one day to Oct. 3 AoE after the HotCRP outage; at submission **no more than 18 pages** for all text and figures **plus 4 pages** for references; major revisions **no more than 20 pages** plus 4 for references; ACM templates, LaTeX `\documentclass[acmsmall,screen,review,anonymous]{acmart}` (sample-acmsmall-conf), single-column, numeric or author-year citations, non-compliant papers desk-rejected; double-anonymous "heavy" review (anonymity kept through all reviewing and discussion, including the major-revision response letter), third-person self-citation, no author-revealing URLs, anonymized organization names, acknowledgements discouraged at submission, arXiv preprints allowed without naming FSE 2027, non-compliant papers desk-rejected; **Data Availability** section after the Conclusion required, not counted toward the page limit; open science policy (replication package link or explanation; state intent to share on acceptance); decisions accept / reject / major revision; **early rejection** (consistently negative papers may be rejected before all planned reviews, so may get fewer than three); same reviewers assess the revision against a response letter; ACM Policy on Authorship and generative-AI policy (AI used in the research described in the methods section; writing assistance need not be disclosed; fabricated citations desk-rejected; prompt injection prohibited); attendance not mandatory for publication; ACM open access — APC for authors not at ACM Open institutions, subsidized 2027 rates **USD500** ACM/SIG members and **USD750** non-members, waivers available; author list and title frozen at submission; Program Chairs Michael Pradel and Baishakhi Ray; area chairs listed. | 2026-11-24 |
| 2 | https://conf.researchr.org/dates/fse-2027 | FSE 2027 dates: research full paper Oct 2, 2026; author response Dec 14-18, 2026; initial notification Jan 22, 2027; major revision submission Mar 5, 2027; final notification Mar 31, 2027; other tracks (industry Jan 23, tool demos Jan 26, SE education Jan 29, IVR Feb 12, journal-first Feb 25, 2027); conference July 12-16, 2027. | 2026-11-24 |
| 3 | https://conf.researchr.org/home/fse-2027 | FSE 2027 home: Shenzhen, China, July 12-16, 2027; tracks (How to Submit, IVR, Industry, Journal-First, Research, SE Education, Tool Demos, Workshops); co-hosted AIware and SSBSE. | 2026-11-24 |
| 4 | https://conf.researchr.org/committee/fse-2027/fse-2027-organizing-committee | FSE 2027 General Co-Chairs Zhi Jin and Xiaoxing Ma; PC Chairs Michael Pradel and Baishakhi Ray; Artifact Evaluation Co-Chairs Shuai Wang and Fernanda Madeiral. | 2026-11-24 |
| 5 | https://fse2027.hotcrp.com/ | FSE 2027 research HotCRP site ("The deadline for registering submissions has passed"). | 2026-11-24 |
| 6 | https://conf.researchr.org/track/fse-2026/fse-2026-research-papers | History: FSE 2026 research-papers call — same 18+4 / 20+4 budget, acmsmall template, heavy double-anonymous review; "reviewed by at least three members of the program committee"; 8-week major-revision period; attendance not mandatory; FSE/ICSE/ASE steering committees coordinate deadlines so they stay spread through the year. | 2026-11-24 |
| 7 | https://conf.researchr.org/home/fse-2026 | History: FSE 2026 (34th edition), Montreal, Canada, Concordia SGW Campus, July 5-9, 2026. | 2026-07-09 |
| 8 | https://conf.researchr.org/dates/fse-2026 | History: FSE 2026 research registration 4 Sep 2025, submission 11 Sep 2025 AoE. | 2026-07-09 |
| 9 | https://fse2026.hotcrp.com/ | History: FSE 2026 research-track HotCRP submission site. | 2026-07-09 |
| 10 | https://dl.acm.org/journal/pacmse | PACMSE journal home: ACM journal publishing FSE research-track papers (HTTP 403 on 2026-11-24; carried). | 2026-07-09 |
| 11 | https://dl.acm.org/journal/pacmse/how-to-submit | PACMSE submission model: new submissions considered once a year through the FSE call; no journal-only submissions (HTTP 403 on 2026-11-24; carried). | 2026-07-09 |
| 12 | https://www.acm.org/publications/policies/artifact-review-and-badging-current | ACM Artifact Review and Badging (Artifacts Available / Evaluated - Functional / Reusable / Results Reproduced) used across SIGSOFT venues (HTTP 403 on 2026-11-24; carried). | 2026-07-09 |
| 13 | http://www.esec-fse.org/test_of_time_awards | ESEC/FSE Test of Time Award (installed 2018; annually honors a paper published ten years earlier); 2026 award to "Deep API learning" (FSE'16). | 2026-11-24 |
| 14 | https://sigsoft.medium.com/major-revisions-at-esec-fse-2023-2ce6b8caecd7 | Background on the Major Revision decision category and its journal-style revise-and-resubmit round. | 2026-07-09 |

## Verified FSE 2027 facts used in skills

- **FSE 2027 is the 35th edition**, Shenzhen, China, **July 12-16, 2027** (sources 1-3). General
  Co-Chairs Zhi Jin and Xiaoxing Ma; PC Chairs Michael Pradel and Baishakhi Ray (source 4).
- **Single research deadline:** full paper **2 October 2026**, extended to **3 October 2026** AoE
  after a HotCRP outage; author response **14-18 December 2026**; initial notification
  **22 January 2027**; major-revision submission **5 March 2027**; final notification
  **31 March 2027** (sources 1-2).
- **Page budget:** **≤18 pages** for all text and figures plus **4 pages** of references at
  submission; **≤20 + 4** for a major revision. The Data Availability section does not count.
- **Template:** ACM `acmart` with `acmsmall,screen,review,anonymous` (single column; numeric or
  author-year citations). Non-compliant papers are desk-rejected.
- **Review is double-anonymous ("heavy"):** anonymity holds through all reviewing and discussion
  periods, and a major-revision response letter must itself stay anonymous. Avoid acknowledgements
  at submission; arXiv preprints are allowed but must not say they were submitted to FSE 2027.
- **Decisions:** accept, reject, or major revision. New wording in 2027: **early rejection** —
  consistently negative papers may be rejected before all planned reviews are in, so some get
  fewer than three reviews (FSE 2026 said "at least three"). In a major revision the same
  reviewers check the revision against a response letter.
- **Open science:** a replication package link (private or public repository, Zenodo, Figshare) or
  an explanation why not; a **Data Availability** section after the Conclusion, not counted; the
  separate FSE 2027 artifact evaluation committee serves accepted papers.
- **Generative AI:** FSE 2027 follows the ACM Policy on Authorship and the Use of Generative AI
  Tools — AI used in the research must be described in the methods section; AI used to assist
  writing need not be disclosed; fabricated/hallucinated citations lead to desk rejection; prompt
  injection is prohibited.
- **Publication venue is PACMSE**, ACM's open-access *Proceedings of the ACM on Software
  Engineering*. PACMSE Issue FSE volumes: Vol 1 = FSE 2024, Vol 2 = FSE 2025, Vol 3 = FSE 2026.
- **APC (corrects the earlier "no APC" statement):** papers are open access; authors with at
  least one co-author at an ACM Open institution pay nothing, others pay an APC unless waived —
  ACM Council's subsidized 2027 rates are **USD500** for ACM/SIG members and **USD750** for
  non-members (source 1).
- **Attendance:** authors are strongly encouraged to present, but attendance is not mandatory for
  publication; non-presenting authors need not register (sources 1, 6).
- **The ESEC/FSE Test of Time Award** was installed by the FSE steering committee in 2018 and
  recognizes a highly influential paper published ten years earlier (source 13).

## History: FSE 2026

- FSE 2026 was the 34th edition, Montreal, Canada (Concordia SGW Campus), July 5-9, 2026;
  mandatory paper registration 4 September 2025, submission 11 September 2025 (AoE) via
  `fse2026.hotcrp.com`; General Chairs Shin Hwei Tan and Foutse Khomh (sources 6-9).

## The PACMSE journal-style model (honest reading of the cycle question)

FSE's move into PACMSE (from FSE 2024) reframed the research track as a **journal**: accepted
papers are PACMSE articles, and the process carries a genuine **Major Revision** round.
Historically FSE ran a *two-deadline* structure so that a Major Revision from an earlier
deadline could be resubmitted to a later one within the same review year; FSE 2024 operated
that dual-deadline model. The 2025, 2026, and 2027 calls each advertise a **single annual
research-paper deadline** with the Major Revision round inside it, and the FSE 2026 call says the
FSE, ICSE and ASE steering committees intend the earlier schedule to "remain stable in the years
ahead". Whether a given year runs one deadline or two is still decided per edition — **verify the
cycle count on the current Important Dates page before advising**.

## No editor-in-chief

Like every conference in this collection, FSE has **no standing editor-in-chief**; the rotating
analogue is the per-edition General Chairs and PC Chairs, appointed by the FSE steering committee
and ACM SIGSOFT. The cost model is the APC described above (only for authors outside ACM Open)
plus registration for those who present.

## UNVERIFIED / 待核实

- FSE 2027 artifact-evaluation call (dates, badges): no AE track page was listed on the FSE 2027
  site on 2026-11-24, although AE co-chairs are named.
- FSE 2027 registration fees and the camera-ready deadline for research papers (not on the dates
  page as of 2026-11-24).
- PACMSE journal pages and ACM badging policy page: unreachable (HTTP 403) on 2026-11-24; facts
  carried from 2026-07-09.
- Removed from this list on 2026-11-24: the generative-AI disclosure policy and the FSE 2027
  chair roster (both now confirmed, sources 1 and 4).

## Still cycle-volatile (verify every year)

- Number of submission deadlines (one vs. two), all dates, and AoE cutoffs.
- Exact page budget and which template revision is required (FSE 2027 posts 18+4, revision 20+4).
- Major Revision mechanics, response-letter format and length, early-rejection rules, and
  re-review assignment.
- Artifact-evaluation track deadlines, offered badges, and whether evaluation is mandatory.
- APC rates (the 2027 rates are described as subsidized for that calendar year).

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "FSE 2027",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 18, "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers", "note": "FSE 2027 research papers: all text and figures; plus 4 pages of references; Data Availability section not counted; major revisions 20 + 4"},
    "page_limit_includes_references": {"value": false, "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers"},
    "review_mode": {"value": "double-blind", "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers", "note": "'heavy' double-anonymous: anonymity kept through discussion and the major-revision response letter"},
    "required_statements": {"value": ["data_availability"], "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers", "note": "section named Data Availability after the Conclusion, not counted toward the page limit"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers", "note": "AI used in the research must be described in the methods section; writing assistance need not be disclosed"},
    "template": {"value": "ACM acmart, \\documentclass[acmsmall,screen,review,anonymous]{acmart} (single-column; numeric or author-year citations)", "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers"},
    "portal": {"value": "HotCRP (fse2027.hotcrp.com)", "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers"},
    "data_code_policy": {"value": "open science policy: replication package link (repository, Zenodo, Figshare) or explanation why not; state intent to share on acceptance; keep anonymity", "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers"},
    "preprint_policy": {"value": "arXiv and similar preprints allowed, but do not state that the manuscript was submitted to FSE 2027", "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers"},
    "llm_policy": {"value": "ACM Policy on Authorship and the Use of Generative AI Tools: describe AI use in the research in the methods section; writing assistance need not be disclosed; fabricated citations desk-rejected; prompt injection prohibited", "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers"},
    "apc": {"value": "open access in PACMSE; no APC with an ACM Open institution, otherwise subsidized 2027 APC USD500 ACM/SIG members / USD750 non-members, waivers available", "source": "https://conf.researchr.org/track/fse-2027/fse-2027-papers"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
