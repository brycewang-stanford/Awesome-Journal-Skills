# Official Source Map - ACM SoCC

Access date: 2026-07-09

This map records the official and cross-check sources used for SoCC-specific facts in this
pack. SoCC — the **ACM Symposium on Cloud Computing** — is the only conference **jointly
sponsored by ACM SIGMOD and ACM SIGOPS**, so it sits at the systems-and-data intersection of
cloud research. Its calendar (two review rounds per year), page budget, review mechanics, and
awards are decided per edition. Reopen the current-cycle call-for-papers, the Important Dates /
HotCRP deadlines page, and the ACM artifact policy before giving submission-ready advice.

## Access method note

Direct fetches of `acmsocc.org` and `dblp.org` returned **HTTP 403** from the verification
gateway on 2026-07-09 (the same egress block seen when verifying other ACM/systems venues in
this collection). Official pages were therefore read through **WebSearch renderings of the exact
URLs** (snippets and cached text) and cross-checked across at least two independent surfaces:
the SoCC HotCRP deadlines page, the ACM Digital Library SoCC proceedings, dblp's `conf/cloud`
stream, and wikicfp/PaperPilot deadline mirrors. Facts that could not be pinned to a primary
rendering plus one cross-check are labeled **待核实**. Name-collision guard: **IEEE SoCC** is the
*IEEE International System-on-Chip Conference* (`ieee-socc.org`), an unrelated hardware venue —
**no fact in this pack derives from it**; this pack is exclusively the ACM Symposium on Cloud
Computing at `acmsocc.org`.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://acmsocc.org/2026/ | SoCC 2026 (17th edition) home: Singapore, Nov 18-20, 2026; only conference co-sponsored by ACM SIGMOD and SIGOPS | 2026-07-09 |
| 2 | https://acmsocc.org/2026/papers.html | SoCC 2026 research-papers call: two review rounds, 12-page + unlimited-references full papers, 6-page short papers, dual-anonymous review, acmart/sigconf template, topics of interest | 2026-07-09 |
| 3 | https://socc26.hotcrp.com/ and https://socc26.hotcrp.com/deadlines | SoCC 2026 HotCRP submission site and machine-readable round deadlines | 2026-07-09 |
| 4 | https://acmsocc.org/2025/papers.html | SoCC 2025 (16th edition) papers call: 12-page full / 6-page short, unlimited references, acmart 9pt anonymous, author-response period 10-12 Sep 2025 | 2026-07-09 |
| 5 | https://dl.acm.org/conference/socc | ACM DL SoCC series landing: proceedings volumes and DOIs across editions | 2026-07-09 |
| 6 | https://dblp.org/db/conf/cloud/index.html | dblp SoCC (`conf/cloud`) proceedings stream used for exemplar verification and edition numbering | 2026-07-09 |
| 7 | https://www.acm.org/publications/policies/artifact-review-and-badging-current | ACM Artifact Review and Badging (Artifacts Available / Evaluated - Functional / Reusable / Results Reproduced) applicable to ACM venues including SoCC | 2026-07-09 |
| 8 | https://acmsocc.org/2026/program-committee.html | SoCC 2026 program-committee page (PC co-chairs and committee roster) | 2026-07-09 |
| 9 | http://www.wikicfp.com/cfp/program?id=2720 + https://www.getpaperpilot.com/deadlines/socc-2026.html | Cross-check mirrors for SoCC 2026 round deadlines and location | 2026-07-09 |
| 10 | https://dl.acm.org/doi/proceedings/10.1145/3772052 | SoCC 2025 proceedings (16th edition, Virtual Event, USA, Nov 19-21, 2025) | 2026-07-09 |

## Verified 2025/2026 facts used in skills

- **SoCC 2026 is the 17th ACM Symposium on Cloud Computing**, held **in person in Singapore,
  November 18-20, 2026**. It is described on the official site as the only conference
  **co-sponsored by the ACM Special Interest Groups on Management of Data (SIGMOD) and on
  Operating Systems (SIGOPS)** — the defining systems-and-data identity of the venue (sources
  1-2).
- **SoCC runs a two-round annual review model.** For SoCC 2026 the rounds (verified via the
  HotCRP deadlines page and cross-check mirrors, sources 3/9):
  - **Round 1:** abstract **6 Feb 2026**, full submission **13 Feb 2026**, author response
    **12-14 Apr 2026**, notification **29 Apr 2026**.
  - **Round 2:** abstract **7 Jul 2026**, full submission **14 Jul 2026** (AoE), author response
    **10-12 Sep 2026**, notification **26 Sep 2026**.
  A paper **rejected in Round 1 may not be resubmitted to Round 2** of the same year (source
  2/9). As of the 2026-07-09 access date, the live target is **Round 2 (14 Jul 2026)**.
- **Page budget:** full research papers **12 pages** for all text and figures, **plus unlimited
  references**; short research papers **6 pages** plus unlimited references (sources 2, 4).
- **Template:** the **ACM Primary Article Template**, `sigconf` proceedings format, submitted
  with `\documentclass[sigconf, anonymous]{acmart}` at **9pt**; single PDF, US-Letter, ≤10 MB
  (source 4).
- **Review is dual-anonymous** (double-blind): author identities are withheld from reviewers and
  vice versa; authors make a good-faith anonymization effort in text, references, and
  acknowledgements (sources 2, 4). Each round includes an **author-response (rebuttal) period**
  before notification (sources 2-4).
- **SoCC welcomes both systems-building and measurement/experience papers**, and its scope
  explicitly spans data management and **cloud economics** (data markets / data economy) as well
  as datacenter systems — a breadth that follows from the joint SIGMOD+SIGOPS sponsorship
  (source 2).
- **Awards:** SoCC recognizes **Best Paper**, a **Distinguished Reviewer** award (awarded at
  SoCC 2025), and a **Test of Time** award (e.g., the SoCC 2012 Google-trace paper was honored)
  (sources 5-6; award pages).
- **Artifacts follow the ACM Artifact Review and Badging** policy where a SoCC edition offers
  evaluation; whether a **dedicated artifact-evaluation track** runs, and which badges are
  offered, is decided per edition (source 7; **see 待核实 list**).

## The two-round model (honest reading of the SoCC cadence)

SoCC's most distinctive process feature is the **two submission rounds per year** (historically a
winter/February round and a summer/July round), each with its own abstract, submission,
author-response, and notification dates. This is neither the single annual deadline of some
flagships nor the rolling model of a journal: it gives authors **two shots per calendar year at
the same venue**, but the "no resubmission across rounds within the same year" rule means a
Round-1 reject waits a full year, not a few months. **Verify the exact round dates and the
cross-round resubmission rule on the current Important Dates / HotCRP page** before planning — the
number of rounds and their offsets are set per edition.

## No editor-in-chief; conference cost model

SoCC is a **conference**, not a journal: it has **no standing editor-in-chief**. Its rotating
leadership is the per-edition **General Chair(s)** and **Program Committee Co-Chairs**, appointed
under ACM SIGMOD and SIGOPS. SoCC 2026 PC Co-Chairs are reported as **Eric Lo and Ivan
Beschastnikh** (source 8; reported via search rendering — confirm on the live committee page).
The cost model is conference registration; at least one author presents each accepted paper.

## Still cycle-volatile (verify every year)

- The number of review rounds, all abstract/submission/response/notification dates, and AoE
  cutoffs; the cross-round resubmission rule.
- Exact page budget and which acmart revision / font size is required.
- Author-response (rebuttal) length and format, and whether a second-round response differs.
- Whether SoCC runs a **dedicated artifact-evaluation track**, which ACM badges are offered, and
  whether evaluation is single- or double-anonymous (**待核实**).
- Open-science / reproducibility and any generative-AI disclosure policy (**待核实**).
- SoCC 2026 **General Chair(s)** and the full PC-Co-Chair roster beyond the reported names
  (**待核实**).
- Short-paper vs. full-paper scope, industry/experience-track rules, and any poster track
  (**待核实** per edition).
