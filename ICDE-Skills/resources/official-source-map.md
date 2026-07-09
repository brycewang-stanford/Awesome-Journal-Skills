# Official Source Map - ICDE

Access date: 2026-07-09

This map records the official sources behind every ICDE-specific fact in this pack. ICDE
(the IEEE International Conference on Data Engineering) republishes its research-track call,
important-dates page, and submission guidelines for each edition on a fresh
`icdeYYYY.github.io` site, so a fact verified for one edition is only a historical anchor for
the next. Reopen the current edition's Call for Research Papers, Important Dates, and
Submission Guidelines before giving deadline-ready advice.

**Access-method note (2026-07-09):** direct automated fetches of `icde2027.github.io`,
`icde2026.github.io`, `ieee-icde.org`, `ieeexplore.ieee.org`, and `dblp.org` returned HTTP
403 through the verification environment. Official-page contents were therefore read through
search-engine renderings of those exact URLs and cross-checked across the 2026 and 2027
edition sites, the IEEE Computer Society TCDE award pages, and institutional press releases
(e.g., university news pages announcing award winners). Where a rendering could not be
independently corroborated, the fact is marked 待核实 below rather than stated. Open the
primary URLs directly before relying on any date or rule.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://icde2027.github.io/ | ICDE 2027 identity: 43rd IEEE International Conference on Data Engineering, Copenhagen, Denmark, May 17-21, 2027. | 2026-07-09 |
| 2 | https://icde2027.github.io/cf-research-papers.html | ICDE 2027 research call: two research-track submission rounds; single-blind review; at least 3 reviewers coordinated by an area chair; original-work requirement (no prior publication longer than 4 double-column pages); authors expected to submit supplemental material (code, data, artifacts), with availability considered in evaluation; round-1 rejected papers not eligible for the round-2 resubmission. | 2026-07-09 |
| 3 | https://icde2027.github.io/important-dates.html | ICDE 2027 round calendar: Round 1 paper submission June 11, 2026; Round 2 paper submission November 11, 2026 with notification February 10, 2027. Other per-round milestones (abstract registration, round-1 notification, camera-ready) 待核实 from live page. | 2026-07-09 |
| 4 | https://icde2027.github.io/submission-guidelines.html | ICDE 2027 submission mechanics: Microsoft CMT as the submission and conflict-declaration system (each author creates a CMT profile and files domain and individual conflicts); IEEE double-column format; supplemental-material expectation. Exact CMT URL and page limit re-confirmation 待核实. | 2026-07-09 |
| 5 | https://icde2026.github.io/cf-research-papers.html | ICDE 2026 research call: two rounds, each round with two reviewing phases; the first phase yields Revise & Resubmit, Accept, or Reject; revised papers get an additional review before a final Accept/Reject; long papers up to 12 pages plus unlimited references, short papers up to 6 pages plus references; IEEE format; single-blind; best papers invited for extended versions in IEEE TKDE. | 2026-07-09 |
| 6 | https://icde2026.github.io/important-dates.html | ICDE 2026 round calendar and revision windows (4-week revision window for invited revisions), used as the structural anchor for how ICDE runs its two rounds and phases. | 2026-07-09 |
| 7 | https://icde2026.github.io/ | ICDE 2026 identity: 42nd IEEE International Conference on Data Engineering, Montréal, Canada, May 4-8, 2026 (Fairmont The Queen Elizabeth). | 2026-07-09 |
| 8 | https://cmt3.research.microsoft.com/ICDE2026 | Microsoft CMT as the ICDE 2026 submission site, confirming CMT is the platform family ICDE uses; the 2027 instance URL is analogous but must be confirmed on the live 2027 CFP (待核实). | 2026-07-09 |
| 9 | https://tc.computer.org/tcde/icde-steering-committee/influential-papers/ | IEEE Computer Society Technical Committee on Data Engineering (TCDE): ICDE 10-Year / Ten-Year Influential Paper Award as the ICDE analogue of a test-of-time lineage, used for the exemplars library. | 2026-07-09 |
| 10 | https://cse.umn.edu/cs/news/mokbels-group-wins-2025-ieee-icde-10-year-influential-paper-award | 2025 ICDE 10-Year Influential Paper Award to Eldawy & Mokbel, "SpatialHadoop: A MapReduce Framework for Spatial Data," ICDE 2015 — exemplar verification via institutional press release. | 2026-07-09 |
| 11 | https://cse.umn.edu/cs/news/cse-alumni-justin-levandoski-earns-ieee-icde-2023-ten-year-influential-paper-award | 2023 ICDE Ten-Year Influential Paper Award to Levandoski, Lomet & Sengupta, "The Bw-Tree: A B-tree for New Hardware Platforms," ICDE 2013 — exemplar verification. | 2026-07-09 |
| 12 | https://www.alibabacloud.com/blog/alibaba-cloud-polardb-awarded-icde-2024-industry-and-applications-track-best-paper-award_601196 | ICDE 2024 Industry and Applications Track Best Paper to Alibaba PolarDB — industry-track exemplar. | 2026-07-09 |
| 13 | https://icde2026.github.io/cf-tkde-poster.html | ICDE-TKDE relationship: separate TKDE Poster track at ICDE (TKDE-accepted regular articles present a 2-page extended abstract in the ICDE proceedings and a poster), distinct from the best-paper TKDE extension invitation. | 2026-07-09 |

## Verified facts used across the skills (as of 2026-07-09)

- **Identity and lineage.** ICDE is the IEEE Computer Society's flagship data-engineering
  conference, one of the three top database venues alongside ACM SIGMOD and VLDB/PVLDB. It
  publishes classic conference proceedings in IEEE Xplore, not a journal-of-the-conference
  like PACMMOD or PVLDB.
- **Editions.** ICDE 2026 = 42nd edition, Montréal, Canada, May 4-8, 2026. ICDE 2027 = 43rd
  edition, Copenhagen, Denmark, May 17-21, 2027.
- **Two rounds per edition.** ICDE 2027 runs two research-track rounds. Round 1 paper
  submission was June 11, 2026 (closed as of this build date); Round 2 paper submission is
  November 11, 2026 with notification February 10, 2027. On 2026-07-09 the live target for
  ICDE 2027 is therefore Round 2.
- **Round-1 rejections are not eligible for Round 2**; a paper rejected in Round 1 waits for
  the next edition's Round 1 (ICDE 2028).
- **Single-blind review.** Author names remain on the submission; reviewers are anonymous to
  authors. This is the opposite of SIGMOD's double-anonymous model.
- **Assignment and outcome model.** At least 3 reviewers per paper, coordinated by an area
  chair. ICDE 2026 used two reviewing phases per round: the first yields Revise & Resubmit,
  Accept, or Reject; invited revisions had a 4-week window and were re-reviewed before a
  final Accept/Reject.
- **Format.** IEEE double-column template; long papers up to 12 pages plus unlimited
  reference pages; short papers up to 6 pages plus references (ICDE 2026 wording).
- **Platform.** Microsoft CMT for submission and conflict declaration; each author must hold
  a CMT profile and file domain and individual conflicts.
- **Artifacts.** Authors are expected to submit supplemental material (code, data,
  artifacts); its availability is considered in the evaluation of the paper.
- **TKDE relationship.** Selected best ICDE papers are invited to submit extended versions to
  IEEE Transactions on Knowledge and Data Engineering (TKDE). Separately, a TKDE Poster track
  lets recently TKDE-accepted articles present at ICDE.
- **Award lineage for exemplars.** The IEEE TCDE ICDE 10-Year / Ten-Year Influential Paper
  Award: 2025 to SpatialHadoop (ICDE 2015); 2023 to the Bw-Tree (ICDE 2013). ICDE 2024
  Industry and Applications Best Paper to Alibaba PolarDB.

## 待核实 (deliberately not guessed at build time)

- ICDE 2027 exact **revision-outcome status**: whether the ICDE 2026 two-phase
  Revise & Resubmit model is retained unchanged for 2027, or replaced by a binary
  accept/reject. Search renderings of the 2027 call were inconsistent on this point; confirm
  on the live `icde2027.github.io/cf-research-papers.html` before advising an author on
  revision odds.
- ICDE 2027 **Round 1 notification date**, **Round 2 abstract-registration deadline**, and
  **camera-ready deadlines** — the important-dates page lists them but they were not cleanly
  recoverable through renderings.
- The exact **ICDE 2027 CMT URL** (the 2026 instance was `cmt3.research.microsoft.com/ICDE2026`).
- ICDE 2027 **page-limit re-confirmation** from the live 2027 guidelines (12 pages is the
  standing ICDE norm but each edition re-declares it).
- Whether ICDE 2027 keeps **single-blind** or changes anonymity policy for any track.
- Author/paper **submission caps**, if any, per round or per edition.
- The **short-paper** track's exact status and page budget for ICDE 2027.

## Maintenance protocol

- Re-anchor the whole pack when a new edition site appears; carry only the two-round pattern,
  the CMT platform, the single-blind default, the IEEE-Xplore publication model, and the TKDE
  relationship forward as priors — and re-read even those.
- If two official pages disagree (call vs. important dates vs. guidelines), prefer the newest
  statement, record the conflict, and treat the program chairs' email as controlling.
- When updating exemplars, require an IEEE TCDE award citation or an IEEE Xplore record plus a
  second independent confirmation; exclude on any disagreement, and never attribute a paper to
  ICDE from a DBLP guess alone.
