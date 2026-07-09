# Official Source Map - ACM FAccT

Access date: 2026-07-09

This map records the official and cross-check sources used for FAccT-specific facts in this
pack. FAccT is the **ACM Conference on Fairness, Accountability, and Transparency** — the flagship
*interdisciplinary* responsible-AI venue, spanning computer science, law, the social sciences, the
humanities, and policy. Its calendar, page budget, review mechanics, and required endmatter
statements are decided per edition. Reopen the current-cycle Call for Papers, Author Guide,
Reviewer Guide, and Important Dates before giving submission-ready advice.

## Access method note

Direct fetches of `facctconference.org` and `dl.acm.org` returned **HTTP 403** from the
verification gateway on 2026-07-09 (the same block seen when verifying other ACM venues in this
collection). Official pages were therefore read through **search-engine renderings of the exact
URLs** (the FAccT 2026 CFP, Author Guide, Reviewer Guide, CRAFT call, and the FAccT Blog
announcement posts) and cross-checked against the OpenReview FAccT 2026 group, the ACM Digital
Library FAccT proceedings, dblp (`db/conf/fat`), and PMLR (for the pre-2019 FAT* editions
published in Proceedings of Machine Learning Research). Facts that could not be pinned to at least
two independent surfaces are labeled **待核实**. Note the naming history: the venue was **FAT\***
in 2018-2019 and was renamed **FAccT** after the 2020 edition — the dblp key is still `fat`.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://facctconference.org/2026/cfp.html | FAccT 2026 Call for Papers: scope, focus areas, 14-page limit (+1 endmatter page), mutually-anonymous review, Accept/Revise/Reject | 2026-07-09 |
| 2 | https://facctconference.org/2026/authorguide.html | Author Guide: acmart template + anonymous/review options, endmatter statements (Generative AI Usage, Ethical Considerations, Adverse Impacts, Positionality), archival vs non-archival, present-in-person requirement | 2026-07-09 |
| 3 | https://facctconference.org/2026/rguide.html | Reviewer Guide: review criteria, focus-area matching, rebuttal purpose, Revise recommendation and re-review | 2026-07-09 |
| 4 | https://facctconference.org/2026/index.html | FAccT 2026 (9th annual) home: Montréal, Canada, Le Centre Sheraton Montréal, June 25-28, 2026 | 2026-07-09 |
| 5 | https://facct-blog.github.io/2025-10-16/announce-cfp | FAccT Blog CFP announcement: deadlines (abstract 8 Jan, paper 13 Jan 2026), OpenReview adoption, Generative AI Usage Statement, revise-and-resubmit as the year's headline change | 2026-07-09 |
| 6 | https://facct-blog.github.io/2025-12-17/submit | "Submitting to FAccT 2026" blog post: OpenReview mechanics, abstract-registration gate, focus-area selection | 2026-07-09 |
| 7 | https://openreview.net/group?id=ACM.org/FAccT/2026/Conference | FAccT 2026 submission + reviewing platform (OpenReview, new for 2026) | 2026-07-09 |
| 8 | https://facctconference.org/2026/cfpcraft.html | Call for CRAFT (Critiquing and Rethinking Accountability, Fairness, and Transparency) proposals: participatory/world-building session formats | 2026-07-09 |
| 9 | https://facctconference.org/2026/committees.html + https://x.com/FAccTConference/status/1939643810016883171 | Organizing committee: General Chairs Su Lin Blodgett and Zeerak Talat; PC Chair Michael Madaio | 2026-07-09 |
| 10 | https://dl.acm.org/doi/proceedings/10.1145/3805689 | Proceedings of the 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT '26), ACM DL; cross-checked against dblp `db/conf/fat` | 2026-07-09 |

## Verified FAccT 2026 facts used in skills

- **FAccT 2026 is the 9th annual ACM Conference on Fairness, Accountability, and Transparency**,
  held in **Montréal, Canada** (Le Centre Sheraton Montréal), **June 25-28, 2026**, with in-person
  and online components. As of the 2026-07-09 access date this edition has just concluded, so the
  live *next* research target is FAccT 2027 (dates/venue **待核实**, see below).
- **FAccT 2026 research-track calendar (source 5):** abstract-registration deadline **8 January
  2026**, full-paper deadline **13 January 2026**; preliminary reviews released **20 February 2026**
  with a short **rebuttal** period; first notification (Accept / Revise / Reject) **2 March 2026**;
  **Revision deadline 25 March 2026**; camera-ready for Round-1 accepts **24 April 2026**;
  camera-ready for Revise-and-resubmit accepts **11 May 2026**. The exact final-notification date
  for Revise papers (reported as early-to-mid April) is **待核实**.
- **Submission platform is OpenReview** (`ACM.org/FAccT/2026/Conference`), newly adopted for 2026,
  replacing the prior EasyChair/Microsoft CMT-style workflow of earlier editions (sources 5-7).
- **Review is mutually anonymous** ("double-blind"): author and reviewer identities are hidden from
  each other. Submissions are matched to reviewers and Area Chairs by the **focus areas** authors
  select at registration (sources 1, 3).
- **Decisions are Accept / Revise / Reject.** The **Revise** decision — a genuine
  revise-and-resubmit round in which authors address Area-Chair-prioritized concerns and receive a
  re-review — is **new for the 2026 edition** and the cycle's headline structural change
  (sources 1, 3, 5).
- **Page budget:** up to **14 pages excluding references** (most papers 12-14), **plus one
  additional content page** for the ethics/adverse-impacts/other endmatter statements; **references
  are unlimited**. Papers sent to Revise and accepted papers may use **15 content pages**
  (sources 1, 2).
- **Format is the ACM `acmart` template.** The review PDF is built anonymized, e.g.
  `\documentclass[manuscript,screen,review,anonymous]{acmart}` (single-column review format);
  camera-ready uses the `sigconf` proceedings format (source 2).
- **Required endmatter — Generative AI Usage Statement (new for 2026):** every submission must
  describe whether and how generative AI was used; FAccT **prohibits** using generative AI to
  wholesale-generate manuscript text (sources 1, 2, 5).
- **Optional endmatter statements** (placed after the body, not counted in the page limit):
  **Ethical Considerations**, **Adverse Impacts**, **Positionality**, plus Author Contributions,
  Acknowledgements, and Conflicts of Interest. Statements that can reveal identity — Author
  Contributions, Acknowledgements, Competing Interests, and **Positionality** — must **not** appear
  in the anonymous submission and are added only upon acceptance (source 2).
- **Archival by default:** most accepted papers are **archival**, published in the *Proceedings of
  the FAccT Conference* and hosted/indexed on the **ACM Digital Library**. A **non-archival**
  option exists (presented but not published in proceedings). **Authors of all accepted papers must
  present** in person, archival or not (source 2).
- **ACM Open Access transition:** effective **1 January 2026**, all ACM publications (including
  FAccT proceedings) are **100% Open Access**; the cost model is the **ACM Open** institutional
  agreement or **Article Processing Charges (APCs)** where no agreement applies (source 5;
  whether/how FAccT waivers apply is **待核实**).
- **CRAFT** (Critiquing and Rethinking Accountability, Fairness, and Transparency) is a co-located,
  community-driven program of participatory and world-building sessions — workshops, experimental
  tutorials, fishbowls, unconferences, site visits, artistic interventions, games, and simulations
  — with its own proposal call and deadline (source 8; exact CRAFT deadline **待核实**).
- **Organizing committee (source 9):** General Chairs **Su Lin Blodgett** and **Zeerak Talat**;
  Program Committee Chair **Michael Madaio**. A **Doctoral Colloquium** runs with its own chairs
  (details/deadline **待核实**).

## What makes FAccT's model distinctive (honest reading)

FAccT is the *interdisciplinary* responsible-AI flagship. Unlike a pure-ML venue (NeurIPS/ICML) or
a pure-HCI venue (CHI), FAccT requires that **fairness, accountability, or transparency be a
first-class contribution**, and it convenes a genuinely mixed reviewer pool — computer scientists,
lawyers, social scientists, humanists, and policy scholars. A rigorous CS method paper **and** a
critical/qualitative or legal-analysis paper are **both in scope**; the review criteria reward
depth of exposition and honest treatment of strengths *and* limitations rather than a single
benchmark number. The 2026 edition adds three structural firsts — the **Revise-and-resubmit**
decision, the **OpenReview** platform, and the required **Generative AI Usage Statement** — on top
of the venue's established norms of **impact/positionality reflexivity** and **documentation
artifacts** (datasheets, model cards, data statements). Treat all three firsts as cycle-volatile
until re-confirmed.

## Naming, lineage, and no editor-in-chief

- The venue was **FAT\*** for its first two editions (**FAT\* 2018**, New York — proceedings in
  **PMLR vol 81**; **FAT\* 2019**, Atlanta — first ACM DL proceedings) and was renamed **FAccT**
  after 2020. The dblp key remains `db/conf/fat`.
- Like every venue in this collection, FAccT has **no standing editor-in-chief**; leadership is the
  per-edition General Chairs and Program Chair, rotating yearly. Do not carry a chair's name
  forward between editions.

## Still cycle-volatile (verify every year) — 待核实 register

- **FAccT 2027** dates, host city, edition specifics, and deadlines (**待核实**; a `2027/cfp.html`
  page exists but was not confirmed to two surfaces at access time).
- Exact **final-notification date** for Revise-and-resubmit papers (reported early-to-mid April
  2026; **待核实**).
- **CRAFT** proposal deadline and session-format list specifics; **Doctoral Colloquium** deadline
  and eligibility (**待核实**).
- Whether **APCs are charged to FAccT authors** or covered, and any fee-waiver policy under ACM
  Open (**待核实**).
- The exact page-budget wording (14 vs 15 content pages, endmatter-page counting) and which
  `acmart` revision/options the current Author Guide mandates.
- Full **Program Committee / Area Chair roster** beyond the named General and PC Chairs (**待核实**).
- Whether a given edition keeps the **Revise** decision, the **OpenReview** platform, and the
  **Generative AI Usage Statement** requirement — all first introduced in 2026.
