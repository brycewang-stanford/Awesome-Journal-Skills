# External Tools - SIGIR

Access date: 2026-07-08; SIGIR 2027 links re-verified 2026-11-24 by direct fetch (see
[`official-source-map.md`](official-source-map.md)). Open them directly before relying on
dates or budgets.

## Official venue systems

- SIGIR 2027 site (current edition): https://sigir2027.org/
- Track pages (per-track rules live here, not in one CFP):
  - Tracks overview and dates: https://sigir2027.org/pages/submit-tracks.html
  - Full papers: https://sigir2027.org/pages/submit-full.html
  - Short papers (TBA on 2026-11-24): https://sigir2027.org/pages/submit-short.html
  - Resource: https://sigir2027.org/pages/submit-resource.html
  - Reproducibility and Replicability: https://sigir2027.org/pages/submit-reproducibility.html
  - Perspectives: https://sigir2027.org/pages/submit-perspectives.html
  - Demonstrations: https://sigir2027.org/pages/submit-demo.html
  - SIRIP / industry (TBA): https://sigir2027.org/pages/submit-industry.html
  - Policies (TBA): https://sigir2027.org/pages/policies.html
  - Organizers: https://sigir2027.org/pages/general-chairs.html
- Submission systems: OpenReview for full papers (link to come); EasyChair
  (https://easychair.org/my/conference?conf=sigir2027) for Resource, Reproducibility and
  Replicability, Perspectives.
- SIGIR 2026 (historical edition, Melbourne): https://sigir2026.org/en-AU; its OpenReview
  groups: https://openreview.net/group?id=ACM.org/SIGIR/2026/Conference and
  https://openreview.net/group?id=ACM.org/SIGIR/2026/Short_Papers_Track
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
- Your track's submission system (OpenReview or EasyChair), its venue/track id, and required form fields.
- After acceptance: the e-rights email, TAPS instructions, registration terms, and
  the ACM Open status of your institution.

## Do not infer

- Do not carry 2026 budgets, dates, or the track lineup into SIGIR 2027 — SIGIR
  restructured its own tracks between 2025 and 2026 (Resource & Reproducibility split),
  renamed Reproducibility for 2027, has no Low Resource Environments track in the 2027
  overview (2026-11-24), and can change again.
- Do not assume all tracks share the full-paper anonymity regime — Resource and
  Demonstration papers are single-anonymous in 2027 (Resources was in 2026 too).
- Do not assume a rebuttal exists or does not exist for full papers; read your
  submission's OpenReview timeline (the 2027 Resource track states there is none).
- Where a track page, the policy page, and an OpenReview announcement disagree, treat
  the newest chair communication as controlling and record the conflict in your notes.
