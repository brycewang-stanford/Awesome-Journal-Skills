# External Tools - RecSys

Access date: 2026-07-09

Use these tools after reopening the current RecSys cycle pages. RecSys rules can change by
year, and the 2026 edition already changed its track lineup (no LBR, new R&P Notes). Verify
before relying on any number.

**Access note:** direct fetches of `recsys.acm.org` and `dl.acm.org` were blocked by the build
gateway on the access date; the links below were confirmed through search renderings and ACM
DL cross-checks. Open them yourself before a deadline-sensitive decision.

## Official workflow

- RecSys 2026 home (Minneapolis): https://recsys.acm.org/recsys26/
- RecSys 2026 Call for Contributions: https://recsys.acm.org/recsys26/call/
- RecSys 2026 committees: https://recsys.acm.org/recsys26/committees/
- RecSys series home and steering committee: https://recsys.acm.org/
- RecSys Best Paper Awards: https://recsys.acm.org/best-papers/
- ACM Digital Library RecSys proceedings: search "ACM Conference on Recommender Systems" at https://dl.acm.org/
- dblp series index: https://dblp.org/db/conf/recsys/

## Author-side checks

- Submission-system account (the CFP's linked portal), profile, conflicts, author list, title,
  abstract, and topic areas before the abstract and paper deadlines.
- Current ACM two-column template, the correct content-page budget for your paper type (long /
  short / Past-Present-Future / Reproducibility / Industry / Resource), and the reference-page
  and appendix-inside-budget rules.
- Anonymous PDF: no names, affiliations, third-person self-citations, acknowledgements, funding
  lines, or identifying metadata; an anonymized repository link if you provide code or data.
- Reproducibility signals: dataset versions, split protocol, tuned baselines, seeds, and the
  anonymous artifact link that the Reproducibility Track expects.
- Rebuttal-phase text, camera-ready ACM rights form, registration, and presentation
  obligations for accepted papers.

## RecSys-native evaluation and reproduction frameworks

Unlike information-retrieval toolchains, RecSys reproduction work usually runs on recommender
libraries. Naming one and pinning its version removes a whole class of reviewer doubt:

- Elliot, RecBole, LensKit, Cornac, RecPack, and ReChorus for offline top-N pipelines.
- `ir_measures` / standard ranking scorers for nDCG, Recall, MAP, and MRR, with the cutoff and
  whether metrics are full-ranking or sampled recorded.
- Off-policy evaluation utilities (IPS / SNIPS / doubly-robust estimators) when the claim is
  about logged bandit feedback rather than a static test split.

## Do not infer

- Do not infer future-cycle dates, the host city, or camera-ready dates from RecSys 2026.
- Do not assume the LBR track still exists, that R&P Notes will recur, or that page budgets and
  the appendix rule carry forward without reopening the current CFP.
- If official pages disagree, treat the newest CFP, committee announcement, or direct chair
  communication as controlling and record the conflict.
