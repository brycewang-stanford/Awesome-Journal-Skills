# External Tools - SIGIR

Access date: 2026-07-08. (Direct fetches of several domains below were blocked in the
build environment; contents were verified via search renderings — see the access-method
note in [`official-source-map.md`](official-source-map.md). Open them directly before
relying on dates or budgets.)

## Official venue systems

- SIGIR 2026 site: https://sigir2026.org/en-AU
- Track pages (per-track rules live here, not in one CFP):
  - Full papers: https://sigir2026.org/en-AU/pages/submissions/full-papers-track
  - Short papers: https://sigir2026.org/en-AU/pages/submissions/short-papers-track
  - Resources: https://sigir2026.org/en-AU/pages/submissions/resources-track
  - Reproducibility: https://sigir2026.org/en-AU/pages/submissions/reproducibility-track
  - Perspectives: https://sigir2026.org/en-AU/pages/submissions/perspectives-track
  - Industry: https://sigir2026.org/en-AU/pages/submissions/industry-track
  - Low Resource Environments: https://sigir2026.org/en-AU/pages/submissions/low-resource-environments-track
  - Cross-track policies: https://sigir2026.org/en-AU/pages/submissions/submission-policies-and-information
  - Key dates: https://sigir2026.org/en-AU/pages/attending/key-dates
- OpenReview groups (per track): https://openreview.net/group?id=ACM.org/SIGIR/2026/Conference
  and https://openreview.net/group?id=ACM.org/SIGIR/2026/Short_Papers_Track
- ACM SIGIR (the SIG): https://sigir.org/ · ACM SIG page:
  https://www.acm.org/special-interest-groups/sigs/sigir
- ACM Digital Library SIGIR proceedings (2025 volume):
  https://dl.acm.org/doi/proceedings/10.1145/3726302
- ACM authoring: TAPS workflow, the Primary Article Template (`acmart`/sigconf), CCS
  concept selector — via https://www.acm.org/publications/taps/ and
  https://www.acm.org/publications/proceedings-template

## IR research tooling the skills assume

- Evaluation: `trec_eval`, `ir_measures` (https://ir-measur.es),
  `ranx` — one canonical scorer per paper, flags recorded.
- Collections plumbing: `ir_datasets` (https://ir-datasets.com) for versioned
  collection identifiers used in configs and papers.
- Retrieval toolkits: Anserini/Pyserini, PyTerrier — pin versions; index settings are
  part of the method.
- Campaign ecosystem: TREC (https://trec.nist.gov), NTCIR, CLEF — sources of test
  collections and the community's evaluation lineage.

## Author-side checks per cycle

- The **track page** for your target track: budget, anonymity regime, dates, and the
  PC-nomination duty. SIGIR has no single CFP — per-track pages are controlling.
- The cross-track policy page: AI-use disclosure, authorship, dual-submission and
  cross-track bans.
- Your track's OpenReview group id and required submission-form fields.
- After acceptance: the e-rights email, TAPS instructions, registration terms, and
  the ACM Open status of your institution.

## Do not infer

- Do not carry 2026 budgets, dates, or the track lineup into a later cycle — SIGIR
  restructured its own tracks between 2025 and 2026 (Resource & Reproducibility split),
  and can again.
- Do not assume all tracks share the full-paper anonymity regime — Resources was
  single-anonymous in 2026.
- Do not assume a rebuttal exists or does not exist; read your submission's OpenReview
  timeline.
- Where a track page, the policy page, and an OpenReview announcement disagree, treat
  the newest chair communication as controlling and record the conflict in your notes.
