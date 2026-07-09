# Official Source Map - ACM SIGMETRICS

Access date: 2026-07-09

This map records the official and cross-check sources used for SIGMETRICS-specific facts in this
pack. ACM SIGMETRICS is the ACM Special Interest Group flagship for **computer-systems performance
measurement, modeling, and evaluation**; its research papers are published as journal articles in
**POMACS (Proceedings of the ACM on Measurement and Analysis of Computing Systems)** on a
**three-deadlines-per-year (summer / fall / winter) rolling model**. Its calendar, page budget,
track list, and review mechanics are decided per edition. Reopen the current-cycle call for
papers, the POMACS journal pages, and the per-deadline HotCRP sites before giving submission-ready
advice.

## Access method note

Direct fetches of `sigmetrics.org`, `dl.acm.org`, and the per-deadline `*.hotcrp.com` sites
returned **HTTP 403** from the verification gateway on 2026-07-09 (WebFetch of
`sigmetrics27summer.hotcrp.com` returned 403 Forbidden; the same block seen when verifying other
ACM venues). Official pages were therefore read through **search-engine renderings of the exact
URLs** and cross-checked across ≥2 independent surfaces: the SIGMETRICS conference site, the ACM
Digital Library POMACS tables of contents, dblp, the SIGARCH call-for-contributions posts, and the
OpenAccept statistics tracker. Facts that could not be pinned to two surfaces are labeled
**待核实** (to be verified). Note the acronym neighborhood: SIGMETRICS is **not** IMC (ACM Internet
Measurement Conference, pure network measurement), **not** SIGCOMM/NSDI (networking systems), and
**not** SIGMOD (databases) — no fact here derives from those.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.sigmetrics.org/sigmetrics2026/call_for_papers.html | SIGMETRICS 2026 call: three deadlines (summer/fall/winter), 20-page acmsmall limit + unlimited references, double-anonymous review, hybrid conference-journal model, one-shot revision, tracks, POMACS publication | 2026-07-09 |
| 2 | https://www.sigmetrics.org/sigmetrics2026/ | SIGMETRICS 2026 (52nd edition) home: University of Michigan, Ann Arbor, USA (Michigan Union), June 8-12, 2026 | 2026-07-09 |
| 3 | https://www.sigmetrics.org/sigmetrics2027/ and https://www.sigmetrics.org/sigmetrics2027/call_for_papers.html | SIGMETRICS 2027 (live next target): Atlanta, Georgia, USA, June 7-11, 2027; summer-round abstract registration July 3, 2026 AoE | 2026-07-09 |
| 4 | https://dl.acm.org/journal/pomacs | POMACS journal home: open-access ACM journal publishing SIGMETRICS research-track papers (Vol 10 N1 = March 2026) | 2026-07-09 |
| 5 | https://dl.acm.org/journal/pomacs/how-to-submit and https://dl.acm.org/journal/pomacs/author-guidelines | POMACS submission model: papers enter only through the SIGMETRICS deadlines; acmsmall single-column journal format | 2026-07-09 |
| 6 | https://sigmetrics26summer.hotcrp.com/ , https://sigmetrics26fall.hotcrp.com/ , https://sigmetrics26winter.hotcrp.com/ | The three per-deadline HotCRP submission sites for SIGMETRICS 2026 | 2026-07-09 |
| 7 | https://sigmetrics27summer.hotcrp.com/ | SIGMETRICS 2027 summer-deadline HotCRP site (abstract registration July 3, 2026 AoE) | 2026-07-09 |
| 8 | https://www.sigarch.org/call-contributions/acm-sigmetrics-2026-operational-systems-track/ | The new Operational Systems Track and its relaxed anonymity (may reveal the deploying organization / deployed system) | 2026-07-09 |
| 9 | https://www.acm.org/publications/policies/artifact-review-and-badging-current | ACM Artifact Review and Badging (Artifacts Available / Evaluated - Functional / Reusable / Results Reproduced) used across ACM venues | 2026-07-09 |
| 10 | https://www.sigmetrics.org/awards.shtml | SIGMETRICS awards: Achievement Award (career); Best Paper Award; Stephen S. Lavenberg and Kenneth C. Sevcik Outstanding Student Paper Award | 2026-07-09 |
| 11 | https://openaccept.org/c/sys/sigmetrics/ and https://dblp.org/db/journals/pomacs/index.html | Cross-check surfaces: historical acceptance statistics and the POMACS/SIGMETRICS proceedings stream for exemplar verification | 2026-07-09 |

## Verified 2026/2027 facts used in skills

- **SIGMETRICS 2026 is the 52nd edition**, held at the **University of Michigan, Ann Arbor, USA**
  (Michigan Union, 530 S. State Street), **June 8-12, 2026** (tutorials June 8, main conference
  June 9-11, workshops June 12). As of the 2026-07-09 access date this edition has already
  occurred, so the live *next* target is **SIGMETRICS 2027**.
- **Three deadlines per year (rolling), all 23:59 AoE and hard.** SIGMETRICS 2026 cycle
  (source 1/6):
  - **Summer:** abstract registration **July 22, 2025**, paper submission **July 29, 2025**,
    notification **September 26, 2025**.
  - **Fall:** abstract registration **October 7, 2025**, paper submission **October 14, 2025**,
    notification **December 12, 2025**.
  - **Winter:** abstract registration **January 6, 2026**, paper submission **January 13, 2026**,
    notification **March 13, 2026**.
- **SIGMETRICS 2027 is in Atlanta, Georgia, USA, June 7-11, 2027** (source 3). The **summer-round
  abstract registration was July 3, 2026 (AoE)** — the round whose reviewing is live around the
  2026-07-09 access date. The winter-round paper submission is reported as **January 11, 2027**
  with notification **March 10, 2027** (source 3, cross-checked via wikicfp). The exact 2027
  summer *paper* deadline (a week after the July 3 abstract, per the venue's usual one-week
  offset) is **待核实**.
- **Publication venue is POMACS**, the open-access *Proceedings of the ACM on Measurement and
  Analysis of Computing Systems*. Accepted papers are POMACS journal articles that also earn a
  SIGMETRICS presentation slot; papers accepted from the **summer and fall** deadlines appear in
  POMACS **before** the conference (sources 1, 4).
- **Page budget:** up to **20 pages** of technical content in the **single-column acmsmall**
  template (including all tables and figures) **plus unlimited pages for references**; no changes
  to margins, spacing, or font sizes from the style files (source 1).
- **Review is a hybrid of the conference and journal models** with **three first-round outcomes**
  (source 1): **Accept** (every accepted paper is **shepherded** so reviewer-required changes land
  in the final version); **One-Shot Revision** (a major-revision decision — the authors receive a
  list of required changes and may resubmit a revised version to **one of the two subsequent
  SIGMETRICS/Performance deadlines**, where it is re-reviewed); and **Reject** (may **not** be
  resubmitted to any SIGMETRICS deadline within **12 months** of the initial submission).
- **Review is double-anonymous** ("double-blind"): authors make a good-faith effort to anonymize
  and do not identify themselves explicitly or by implication. The **Operational Systems Track**
  is the documented exception — it may reveal the deploying organization or deployed system where
  needed (sources 1, 8).
- **Tracks (SIGMETRICS 2026):** Theory; Measurement & Applied Modeling; Learning; and the new
  Operational Systems Track. Authors pick one track (a second only for strongly interdisciplinary
  work). The exact full track set and count each cycle is **待核实** (a rendering referenced
  "five tracks").
- **ACM Artifact Review and Badging** is the badging scheme in the ACM ecosystem (Artifacts
  Available / Evaluated - Functional / Reusable / Results Reproduced); source 9.

## The POMACS three-cycle rolling model (honest reading of the cadence)

SIGMETRICS moved its research track into **POMACS** (a journal in the Proceedings of the ACM
series), which reframed submission as a **rolling, three-deadlines-per-year** process rather than
a single annual conference deadline. The distinctive mechanic is the **one-shot revision**: unlike
a plain accept/reject conference, a paper that needs major work is given exactly one chance to
resubmit a revised version to one of the next two deadlines, and unlike an open-ended journal R&R,
it is **one shot, not an unbounded revise loop**. Combined with **mandatory shepherding of every
accepted paper**, this makes SIGMETRICS a genuine hybrid. Which deadline a revision may target,
and the precise notification offsets, are decided per cycle — **verify the current call and the
per-deadline HotCRP sites before advising**, and never carry a previous cycle's dates forward.

## No editor-in-chief in the journal sense; no APC

POMACS has editorial leadership (Editors / the SIGMETRICS Program-Committee Chairs per cycle), but
SIGMETRICS retains **rotating per-edition General and Program Chairs** appointed by the SIGMETRICS
executive committee, not a standing single editor-in-chief tied to the conference. POMACS is
**open access**; the cost model is conference registration, and at least one author presents each
accepted paper.

## Still cycle-volatile (verify every year)

- All three deadline dates, abstract-vs-paper offsets, notification dates, and AoE cutoffs.
- The exact page budget and which acmsmall template revision is required.
- One-shot-revision mechanics: which subsequent deadline(s) a revision may target and how the
  12-month resubmission bar is counted.
- The full track list and count, and each track's anonymity policy (Operational Systems differs).
- Whether a formal **artifact-evaluation / reproducibility track** runs a given cycle, its
  badges, timing, and whether it is mandatory (**待核实**).
- The precise SIGMETRICS 2027 summer *paper* deadline and full 2027 fall/winter calendar
  (**待核实** beyond the July 3, 2026 abstract and the reported Jan 11 / Mar 10, 2027 winter dates).
- Recent per-cycle acceptance rates (historical anchor: SIGMETRICS 2018 accepted 54 of 270
  submissions, ~20%; current-cycle rates **待核实**).
- Exact award names/eligibility (career Achievement Award vs. any Test-of-Time honor) (**待核实**).
