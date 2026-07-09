# Official Source Map - USENIX FAST

Access date: 2026-07-09

This map records the official and cross-check sources used for FAST-specific facts in this pack.
FAST is the **USENIX Conference on File and Storage Technologies**, the USENIX-run flagship for
file-system, SSD/NVM, key-value-store, and storage-reliability research. Its proceedings are
published open access by USENIX (not ACM or IEEE), review is USENIX **double-blind**, and the
calendar runs **two submission deadlines a year** (a Spring and a Fall deadline). Reopen the
current-cycle Call for Papers, the Important Dates block, the Call for Artifacts, and the USENIX
templates page before giving submission-ready advice.

## Access method note

Direct fetches of `usenix.org` and `dl.acm.org` returned **HTTP 403 / blocked CONNECT** from the
verification gateway on 2026-07-09 (the standard egress block in this build sandbox). Official
pages were therefore read through **WebSearch renderings of the exact USENIX URLs** and
cross-checked against **dblp** (the `conf/fast` stream and per-year proceedings pages), the **ACM
Digital Library** mirror of the USENIX FAST proceedings, and the USENIX HotCRP submission sites.
Facts that could not be pinned to at least two independent surfaces are labeled **待核实**. Note a
name collision to avoid: "FAST" is also an IEEE/other-community acronym in several fields; every
fact here derives specifically from the **USENIX** File and Storage Technologies conference
(`usenix.org/conference/fastNN`, dblp `conf/fast`).

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.usenix.org/conference/fast26/call-for-papers | FAST '26 (24th) identity, two deadlines, double-blind review, one-shot revision, shepherding, page limits, USENIX template | 2026-07-09 |
| 2 | https://www.usenix.org/conference/fast26 | FAST '26 home: Feb 24-26, 2026, Hyatt Regency Santa Clara, Santa Clara, CA | 2026-07-09 |
| 3 | https://www.usenix.org/conference/fast27/call-for-papers | FAST '27 (25th) research call: two deadlines (Spring 17 Mar 2026, Fall 15 Sep 2026 AoE), author-response windows, notification and final-file dates, 12-page long / 6-page short limits excluding references | 2026-07-09 |
| 4 | https://www.usenix.org/conference/fast27 | FAST '27 home: Feb 23-25, 2027, Hyatt Regency Santa Clara, Santa Clara, CA | 2026-07-09 |
| 5 | https://www.usenix.org/conference/fast26/double-blind-guidance | FAST double-blind submission and reviewing guidance (anonymize PDF and references; refer to own prior work in the third person) | 2026-07-09 |
| 6 | https://www.usenix.org/conference/fast27/call-for-artifacts | FAST '27 Call for Artifacts: AEC process, USENIX badges, artifact appendix, post-acceptance timing | 2026-07-09 |
| 7 | https://fast27spring.usenix.hotcrp.com/ | FAST '27 Spring HotCRP submission site (the Fall deadline uses a separate HotCRP instance) | 2026-07-09 |
| 8 | https://www.usenix.org/conferences/test-of-time-awards | USENIX Test of Time Awards: FAST honors a paper published 10+ years earlier (e.g. F2FS and SHARDS, both FAST '15) | 2026-07-09 |
| 9 | https://www.usenix.org/conferences/best-papers | USENIX Best Paper Awards, including FAST (e.g. Skylight, FAST '15; WiscKey, FAST '16) | 2026-07-09 |
| 10 | https://dblp.org/db/conf/fast/index.html | dblp FAST proceedings stream, used for exemplar verification and to cross-check the per-year table of contents | 2026-07-09 |

## Verified 2026/2027 facts used in skills

- **FAST '26 is the 24th USENIX Conference on File and Storage Technologies**, held at the Hyatt
  Regency Santa Clara, Santa Clara, CA, **February 24-26, 2026**. It ran **two submission
  deadlines** (a Spring deadline, 18 March 2025, and a Fall deadline, 16 September 2025, both
  23:59 AoE) and introduced **one-shot revisions** into the FAST decision set (sources 1-2). As of
  the 2026-07-09 access date this edition has concluded, so the live *next* target is FAST '27.
- **FAST '27 is the 25th edition**, **February 23-25, 2027**, Hyatt Regency Santa Clara, Santa
  Clara, CA. It also runs **two deadlines** (source 3):
  - **Spring:** submissions 17 March 2026; author-response 18-20 May 2026; notification 4 June
    2026; final files 28 July 2026 — all 23:59 AoE where a time applies.
  - **Fall:** submissions 15 September 2026; author-response 17-19 November 2026; notification 8
    December 2026; final files 26 January 2027.
  As of 2026-07-09 the Spring round has closed and been notified, so the **live actionable target
  is the FAST '27 Fall deadline, 15 September 2026**.
- **Page limits (verify per cycle):** a complete submission is **at most 12 pages for a long paper
  and 6 pages for a short paper, excluding references** (references do not count and are not
  capped). Camera-ready allowances are larger (reported as 13 pages long / 7 pages short excluding
  references). Format is the **USENIX two-column template**, 10-point on 12-point leading, 7" x 9"
  text block, 0.33" inter-column gap, US-letter (sources 1, 3).
- **Review is USENIX double-blind:** authors anonymize the PDF and references and refer to their
  own prior work in the third person; the program committee reviews (assisted by outside referees),
  and there is an **author-response (rebuttal) period** before notification (sources 3, 5).
- **Decision categories include one-shot revision.** Beyond accept and reject, FAST issues
  **accept-with-shepherding** (light, editor-guided fixes) and **one-shot revision** (a heavier
  revise-and-resubmit whose instructions may require running specific additional experiments). A
  one-shot revision is resubmitted at the *subsequent* deadline and can then only be accepted or
  rejected — not revised again, which is what makes it "one-shot." During revision the paper is
  still under review at FAST and may not be submitted elsewhere (source 1).
- **Publication is open access by USENIX:** the full proceedings and presentation slides are free
  and public; there is **no APC** and no paywall. The cost model is registration plus USENIX
  membership (sources 1-2).
- **Artifact evaluation is separate and post-acceptance.** An Artifact Evaluation Committee (AEC)
  awards up to three USENIX badges — **Artifacts Available**, **Artifacts Functional**, and
  **Results Reproduced** — shown on the paper's first page and the USENIX site, with an artifact
  appendix (source 6).
- **Awards:** FAST gives **Best Paper** award(s) each year and a **Test of Time Award** honoring a
  FAST paper published at least ten years earlier (sources 8-9).

## The two-deadline USENIX model (honest reading of the cycle question)

FAST's identity as a USENIX systems conference means the reviewing machinery differs sharply from
an ACM/IEEE flagship: open-access USENIX proceedings, USENIX double-blind norms, a rebuttal, PC
shepherding, and — distinctively — a **one-shot revision** track that spans the two deadlines
within a review year. A paper that misses (or is revised out of) the Spring deadline has a *second*
on-ramp at the Fall deadline of the same conference, which changes calendar strategy relative to a
single-annual-deadline venue. Whether a given edition posts one deadline or two, and the exact
author-response and revision mechanics, are decided per cycle — **verify the current Important
Dates block and CFP before advising**, and never carry a previous year's cadence forward.

## No editor-in-chief; no APC

FAST has **no standing editor-in-chief**; the rotating leadership is the per-edition Program
Co-Chairs and the program committee appointed by USENIX. USENIX proceedings are **open access with
no article-processing charge**; the cost model is conference registration, and at least one author
presents the accepted paper.

## Still cycle-volatile (verify every year)

- Number of submission deadlines (one vs. two), all dates, and AoE cutoffs.
- Exact page limits and which USENIX template revision is required (FAST '27 posts 12+6 for
  submission, larger for camera-ready).
- One-shot-revision and shepherding mechanics, response-letter format, and cross-deadline
  resubmission rules.
- Artifact-evaluation timing, the exact badge set, and whether evaluation is single- or
  double-anonymous (**待核实** for the precise FAST '27 AEC anonymity model).
- Open-science / data-availability wording and any generative-AI or LLM-use disclosure policy
  (**待核实**).
- FAST '26/'27 full Program Co-Chair and AEC-chair rosters (**待核实** beyond what the CFP names).
- The exact FAST '27 venue city: USENIX FAST '27 pages read as Santa Clara, CA, while one secondary
  aggregator listed Renton, WA — treat the **USENIX page as controlling** and re-confirm the hotel
  before booking (**待核实**).
