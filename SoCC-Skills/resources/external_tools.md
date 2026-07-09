# External Tools - ACM SoCC

Access date: 2026-07-09

Use these surfaces after reopening the current SoCC cycle pages. SoCC mechanics — the two-round
calendar, page budget, rebuttal format, and any artifact-evaluation track — are decided per
edition, and the `acmsocc.org`/`dl.acm.org`/`dblp.org` gateway may block direct fetches (read via
search renderings and cross-check ACM DL and dblp). **Do not confuse this venue with
`ieee-socc.org`** (the IEEE International System-on-Chip Conference, a hardware venue).

## Official workflow

- SoCC series hub (via ACM SIGOPS/SIGMOD): https://acmsocc.org/
- SoCC 2026 home (Singapore, Nov 18-20, 2026): https://acmsocc.org/2026/
- SoCC 2026 research-papers call: https://acmsocc.org/2026/papers.html
- SoCC 2026 program committee: https://acmsocc.org/2026/program-committee.html
- SoCC 2026 HotCRP: https://socc26.hotcrp.com/  (deadlines: https://socc26.hotcrp.com/deadlines)
- SoCC 2025 research-papers call (prior cycle, for comparison): https://acmsocc.org/2025/papers.html
- ACM DL SoCC series: https://dl.acm.org/conference/socc
- ACM Artifact Review and Badging: https://www.acm.org/publications/policies/artifact-review-and-badging-current

## Cross-check surfaces (when the gateway blocks the primary page)

- dblp SoCC stream (`conf/cloud`): https://dblp.org/db/conf/cloud/index.html — edition numbering,
  proceedings, and exemplar verification.
- ACM DL SoCC proceedings tables of contents (per year) for DOIs and paper lists.
- wikicfp SoCC program: http://www.wikicfp.com/cfp/program?id=2720 — deadline mirror.
- PaperPilot / ds-deadlines mirrors for the two-round cutoffs the CFP paraphrases.
- The SoCC HotCRP `deadlines` endpoint for the machine-readable per-round dates.

## Author-side checks

- HotCRP profile, conflicts, coauthor emails, topic/subject tags, and the **abstract-registration
  step** that precedes each round's full-paper deadline (SoCC runs abstract + paper in the same
  week per round).
- ACM Primary Article Template (`sigconf`) compliance at **9pt**, the **12-page (full) / 6-page
  (short)** budget with **unlimited references**, and a single US-Letter PDF ≤10 MB.
- Dual-anonymous sweep: anonymize the PDF metadata, self-citations, tool/system names, cluster and
  dataset names, deployment/company hints, and any repository or data-availability link.
- A reproducibility/data-availability posture appropriate to a systems-and-data paper: released
  code, workload generators, traces, and measurement scripts where possible.
- Artifact-evaluation intent if the edition runs it (ACM Available / Functional / Reusable /
  Reproduced) and its timing relative to notification and camera-ready.

## Do not infer

- Do not infer the number of review rounds or their dates: SoCC runs (currently) **two rounds per
  year**; confirm both rounds' abstract/submission/response/notification dates and the **no
  cross-round resubmission** rule on the current Important Dates / HotCRP page.
- Do not assume the page budget, acmart revision, rebuttal format, artifact track, or
  reproducibility and AI-disclosure wording carry over between editions.
- Do not assume SoCC runs a heavyweight artifact-evaluation track like some sibling systems
  venues — whether it does, and which badges apply, is **待核实** per edition.
- If pages disagree, treat the newest research-papers call, the HotCRP deadline page, or a direct
  chair announcement as controlling, and record the conflict.
