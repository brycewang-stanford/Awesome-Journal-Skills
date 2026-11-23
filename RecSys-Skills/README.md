# RecSys Skills

Twelve agent skills for papers targeting the **ACM Conference on Recommender Systems (RecSys)** —
the single-domain home of the recommender-systems research community. The pack concentrates on the
things that actually decide RecSys outcomes: recommendation-first framing, honest offline-versus-
online evaluation, equal-budget baseline tuning, leakage-aware splits, off-policy and
counterfactual estimation, the venue's dedicated Reproducibility track, anonymous in-paper code
release, the ACM two-column camera-ready, and a per-track project calendar.

RecSys is not a general machine-learning venue and not an information-retrieval venue. Its
reviewers are a tight community who have internalized the field's own reproducibility debates, so a
paper that wins here reads differently from one written for SIGIR, KDD, WSDM, or TheWebConf. This
pack encodes that difference.

## Why a RecSys-specific pack

Generic conference advice misses what RecSys reviewers reward and punish:

- **Recommendation, not retrieval.** The contribution has to matter to a recommender audience —
  ranking objectives, user/item and session modeling, feedback loops, exposure and fairness,
  deployed behavior — not merely be applicable to recommendation.
- **Evaluation honesty is load-bearing.** After the field's reproducibility critiques, reviewers
  read baseline tuning, split protocol, and metric choice as a proxy for whether the reported gains
  are real. Untuned baselines, random splits on sequential data, and sampled metrics presented as
  full-ranking numbers are recognizable reject patterns.
- **Offline is only a proxy.** RecSys uniquely values the bridge from an offline metric to a
  deployment quantity — an A/B test, an off-policy estimate (IPS / SNIPS / doubly robust), or a
  simulator — and rewards papers that are honest about the gap.
- **A dedicated Reproducibility track.** Repeating, refuting, or re-scoping prior results is
  first-class, publishable work here.
- **Industry density.** A standing Industry track means deployed-system papers with production
  constraints and live evidence have a real home.

## Official basis and access method

Official basis checked on **2026-07-09**. Verified against the RecSys 2026 Call for Contributions,
the `recsys.acm.org/recsys26` cycle pages, the RecSys Best Paper Award lineage, ACM Digital Library
proceedings records, and dblp. See [`resources/official-source-map.md`](resources/official-source-map.md)
for the exact source map with per-fact URLs and access dates.

**Access-method note:** the build environment's network gateway returned HTTP 403 on direct
fetches of `recsys.acm.org`, `recommender-systems.com`, and `dl.acm.org`. Every RecSys fact in this
pack was therefore verified through web-search renderings of those exact official pages,
cross-checked against ACM DL and dblp and the mailing-list Calls for Contributions that mirror the
CFP verbatim. Reopen the primary URLs directly before relying on any specific deadline, page
budget, or fee.

## Live cycle status (re-verified 2026-11-23)

- **Next edition:** **RecSys 2027**, the **21st** ACM Conference on Recommender Systems, **Honolulu,
  O‘ahu, Hawaii, August 23–27, 2027** (General Co-Chairs Christine Bauer, Joeran Beel, Bamshad
  Mobasher). **No RecSys 2027 call is published yet** — deadlines, program chairs, tracks and page
  budgets are unknown; note the conference is a month earlier than in 2026.
- RecSys 2026 was the **20th** edition, in **Minneapolis, Minnesota, USA**, September 28 -
  October 2, 2026 (Doctoral Symposium September 27; main sessions September 29 - October 1). Its
  call is the latest one published and anchors the rules in this pack.
- 2026 Main Track timetable (history): abstract April 14, paper April 21, rebuttal June 4-9
  (**500-character** factual-correction rebuttal), notifications July 9, camera-ready July 27
  (strict), recorded video within a week after camera-ready.
- **APC:** under ACM's open-access model (from January 1, 2026), authors from institutions outside
  ACM Open pay an APC for Main, Reproducibility and Industry papers — $250 ACM/SIG member / $350
  non-member at the 2026 subsidised rate.
- **R&P Notes and Demos** ran to a July 15, 2026 deadline. RecSys 2026 **dropped the
  Late-Breaking Results (LBR) track** and added **Research & Practice (R&P) Notes**, presented as
  posters, plus a new **"Past, Present and Future" paper** type in the Main Track.
- Forward planning: treat every 2026 fact as a historical anchor and re-verify against the RecSys
  2027 call when it replaces the placeholder at `recsys.acm.org/recsys27/call/`.

## Skills

- `recsys-topic-selection` - decide whether a project is genuinely recommendation-shaped and route
  between RecSys, SIGIR, KDD, WSDM, TheWebConf, UAI, CHI, and ML venues, then pick the RecSys
  track.
- `recsys-submission` - audit track choice, ACM two-column content-page budgets with appendices
  counted inside, anonymization of logs and deployed-system names, the anonymous repository, and
  desk-reject triggers.
- `recsys-writing-style` - revise for a recommendation-first first page, honest offline-online
  framing, equal-budget baseline claims, leakage-aware wording, and 8-page two-column compression.
- `recsys-related-work` - position against recommender subfields and the right neighbor venues,
  cite canonical methods to their true venue, and survive double-blind.
- `recsys-experiments` - design offline-versus-online evaluation: temporal splits, equal-budget
  tuning, full-ranking versus sampled metrics, off-policy estimators, A/B tests, and bias handling.
- `recsys-reproducibility` - strengthen dataset/split/tuning/seed reporting, avoid sampled-metric
  distortion, and structure a Reproducibility-track study with honest divergence analysis.
- `recsys-artifact-evaluation` - package code, datasets, splits, checkpoints, and logged
  propensities as an anonymous in-paper repository or a public post-acceptance archive.
- `recsys-supplementary` - split a paper across the body, the appendix that counts inside the page
  budget, and the anonymous repository so evidence lands where reviewers use it.
- `recsys-review-process` - reason about the mutually-anonymous model (three PC members plus a
  Senior PC), the rebuttal phase, reviewer priorities, and ACM Digital Library publication.
- `recsys-author-response` - draft the short rebuttal narrative, anchored to submitted evidence,
  answering the recurring objections about tuning, leakage, and offline-online gaps.
- `recsys-camera-ready` - prepare the ACM two-column camera-ready, rights form, metadata,
  de-anonymization, public artifact release, registration, and presentation.
- `recsys-workflow` - manage the calendar from fit through abstract, paper, repository, rebuttal,
  decision, camera-ready, and presentation, with per-track dates and backward offsets.

## Resources

- [`resources/README.md`](resources/README.md) - index of the action-oriented resources.
- [`resources/official-source-map.md`](resources/official-source-map.md) - per-fact URLs, the
  access-method note, and the still-volatile list.
- [`resources/external_tools.md`](resources/external_tools.md) - official links plus RecSys-native
  reproduction frameworks (Elliot, RecBole, LensKit, Cornac, RecPack).
- [`resources/exemplars/library.md`](resources/exemplars/library.md) - six web-verified RecSys
  papers by contribution type, with a sibling-confusion guard against SIGIR / KDD / WWW / UAI.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) -
  a fictional before-to-after abstract and introduction in RecSys house style.
- [`resources/code/README.md`](resources/code/README.md) - adapter to the shared ML-conference
  reproducibility kit for a regenerable top-N ranking pipeline.

## Suggested workflow

1. Route and frame with `recsys-topic-selection` and `recsys-writing-style`.
2. Stress-test evidence with `recsys-experiments`, `recsys-reproducibility`, and the code adapter.
3. Package with `recsys-artifact-evaluation` and `recsys-supplementary`, then audit with
   `recsys-submission`.
4. After reviews, use `recsys-review-process` and `recsys-author-response`; after acceptance,
   `recsys-camera-ready`. Keep the whole thing on schedule with `recsys-workflow`.

## Maintenance notes

- Reopen current-cycle official sources before any deadline-sensitive advice; the 2026 track lineup
  already changed from 2025.
- Treat every RecSys 2026 fact as a historical anchor, not a permanent rule.
- Page budgets, the appendix-inside-budget rule, the reference allowance, track lineup, rebuttal
  window, camera-ready dates, registration, and presentation obligations can all change by cycle.
- Every fact carries a URL and a 2026-07-09 access date, or is marked 待核实; keep that discipline
  when updating.
