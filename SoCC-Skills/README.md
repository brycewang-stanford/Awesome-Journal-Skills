# SoCC Skills

Twelve agent skills for papers targeting **SoCC — the ACM Symposium on Cloud Computing**, the
**only conference jointly sponsored by ACM SIGMOD and ACM SIGOPS**. That joint sponsorship is the
pack's north star: SoCC sits at the **systems-and-data intersection** of cloud research, spanning
datacenter systems, storage, resource management, serverless, big-data and ML-systems
infrastructure, edge/fog, and cloud economics. The pack covers the full arc of a SoCC campaign:
deciding whether a project is SoCC-shaped or belongs at OSDI/NSDI/EuroSys/ATC or a data venue
(SIGMOD/VLDB); building measured evidence — throughput, **tail latency**, and **cost** — that
satisfies both sponsoring communities; packaging the dual-anonymous `acmart` submission through
SoCC's **two review rounds per year**; navigating the rebuttal; and delivering the ACM camera-ready
plus a reproducible artifact.

Official basis checked on **2026-07-09**: the SoCC 2026 (Singapore) and SoCC 2025 research-papers
calls and Important Dates, the SoCC HotCRP site, the ACM Artifact Review and Badging policy, and the
ACM DL / dblp SoCC proceedings. Direct fetches of `acmsocc.org` and `dblp.org` returned 403 in the
verification environment, so official pages were read via search-engine renderings of the exact URLs
and cross-checked against the SoCC HotCRP deadlines page, the ACM Digital Library, dblp's
`conf/cloud` stream, and deadline mirrors; the full trail, including everything still marked 待核实,
is in [`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warning: `ieee-socc.org` is the **IEEE International System-on-Chip Conference**, a
> hardware venue, and is **not** this SoCC. No fact in this pack derives from it.

## What makes SoCC different from its siblings

These venue mechanics, verified for the 2025/2026 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from a pure-systems flagship, a data conference,
or an ML venue:

- **Jointly sponsored by SIGMOD and SIGOPS.** SoCC is the one venue owned by *both* the data and the
  systems communities, so a paper is judged on both axes at once — the mechanism *and* the
  workloads, the deployment *and* the measurement. This is the identity that distinguishes SoCC from
  OSDI/NSDI (systems flagships) and from SIGMOD/VLDB (data flagships).
- **Two review rounds per year.** SoCC runs a winter and a summer round, each with its own abstract,
  submission, rebuttal, and notification dates — two shots per calendar year, but a **Round-1 reject
  cannot be resubmitted to Round 2** the same year.
- **Dual-anonymous review with a rebuttal.** Reviewers and authors are mutually anonymous; each round
  has an author-response window. There is **no journal-style Major-Revision round** — the rebuttal is
  the one written turn before an accept/reject verdict.
- **The ACM `acmart` path.** SoCC uses the ACM Primary Article Template, `sigconf`, 9pt, with a
  **12-page** full-paper budget (6 pages for short papers) and **unlimited references** — not the
  USENIX template that OSDI/NSDI/ATC use.
- **Systems-building and measurement/experience papers alike.** Clean-slate systems, production
  trace studies, benchmarks, deployment-experience papers, and cloud-economics work are all native
  here — a breadth that follows directly from the joint sponsorship.
- **Tail latency and cost are first-class.** A cloud paper that reports only the mean, or asserts a
  cost saving it never measures, reads as untested; p95/p99 and a concrete cost model are the
  currency.

## Skills

| Skill | What it does |
| --- | --- |
| [`socc-topic-selection`](skills/socc-topic-selection/SKILL.md) | Route between SoCC and its siblings (OSDI, NSDI, EuroSys, ATC, SOSP, SIGMOD/VLDB) using the systems-and-data intersection test, contribution shape, and the model-swap / re-label tests. |
| [`socc-workflow`](skills/socc-workflow/SKILL.md) | Run the two-round year backward from a round's abstract cutoff, through submission, rebuttal, notification, ACM camera-ready, and presentation in Singapore. |
| [`socc-writing-style`](skills/socc-writing-style/SKILL.md) | Build the cloud-systems skeleton: operator problem on the first page, contribution at the systems+data intersection, tail and cost as first-class, acmart page discipline. |
| [`socc-related-work`](skills/socc-related-work/SKILL.md) | Cover both the systems and data literature lanes, write delta-first positioning, and keep self-citations dual-anonymous. |
| [`socc-experiments`](skills/socc-experiments/SKILL.md) | Match measured evidence to claim shape: real/realistic deployments, production workloads, tail and cost, fair tuned baselines, scale and multi-tenancy. |
| [`socc-reproducibility`](skills/socc-reproducibility/SKILL.md) | Build the reproducibility story: testbed and workload description, released code and traces, provenance pinning, reproducing tail and cost. |
| [`socc-supplementary`](skills/socc-supplementary/SKILL.md) | Split content between the reviewed pages and the artifact by decision-criticality — nothing that decides acceptance (tail, cost, baselines) may live outside the body. |
| [`socc-submission`](skills/socc-submission/SKILL.md) | Final HotCRP audit: the two-round abstract+paper deadlines, the acmart budget, the dual-anonymous sweep, reproducibility posture, desk-risk triage. |
| [`socc-review-process`](skills/socc-review-process/SKILL.md) | Model the pipeline — dual anonymity, two rounds, the joint SIGMOD+SIGOPS pool, the rebuttal, accept/reject — and where author leverage exists. |
| [`socc-author-response`](skills/socc-author-response/SKILL.md) | Write the single rebuttal turn that answers both the systems and the data reviewer and supplies the tail/cost numbers, within dual anonymity. |
| [`socc-artifact-evaluation`](skills/socc-artifact-evaluation/SKILL.md) | Package for the ACM badges (Available / Functional / Reusable / Reproduced) where the edition offers evaluation, reproducing tail and cost at scale. |
| [`socc-camera-ready`](skills/socc-camera-ready/SKILL.md) | De-anonymize systematically, complete ACM metadata, permanentize released code and traces, and pass ACM production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2025/2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified SoCC papers across five contribution shapes (benchmark, trace study, storage QoS, resource management, serverless) with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional serverless-autoscaling study's abstract and introduction rebuilt to the SoCC arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility tooling, plus the SoCC-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./SoCC-Skills
claude plugin install socc-skills
```

Or use the files directly: each `skills/socc-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a SoCC paper or should it go to OSDI/NSDI/SIGMOD?" → `socc-topic-selection`
- "Audit my draft against the SoCC research-track rules" → `socc-submission`
- "We got reviews — help me write the SoCC rebuttal" → `socc-author-response`
- "Get this artifact ready for the ACM badges" → `socc-artifact-evaluation`

## Pack structure

```text
SoCC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── socc-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `socc-topic-selection`; SoCC overlaps OSDI/NSDI/EuroSys and SIGMOD/VLDB,
   so choosing by the systems-and-data intersection matters. Skim the exemplars library to see what
   SoCC contributions look like.
2. **While building evidence** — keep `socc-experiments` and `socc-reproducibility` beside the
   system; tail/cost measurement and pinned provenance cannot be retrofitted.
3. **While writing** — `socc-writing-style` for the body against the worked example,
   `socc-supplementary` for the body/artifact split, `socc-related-work` for delta-first positioning
   across both lanes.
4. **Round weeks** — pick the round you can make strong, register the abstract before its cutoff,
   then `socc-submission` end to end on the final PDF and artifact.
5. **After submission** — `socc-review-process` to calibrate, `socc-author-response` for the
   rebuttal, then `socc-artifact-evaluation` and `socc-camera-ready` — or the routing table in
   `socc-topic-selection` if the decision goes the other way (remembering a Round-1 reject cannot
   re-enter Round 2 the same year).

## 2025/2026-cycle anchor facts (historical snapshot, not permanent rules)

- SoCC 2026 is the **17th** edition: **Singapore, November 18-20, 2026**. Round 1: abstract 6 Feb,
  paper 13 Feb, response 12-14 Apr, notify 29 Apr 2026. Round 2: abstract 7 Jul, paper 14 Jul (AoE),
  response 10-12 Sep, notify 26 Sep 2026. A Round-1 reject may not be resubmitted to Round 2.
- Format: **ACM `acmart` sigconf, 9pt, dual-anonymous**; full papers **12 pages** + unlimited
  references, short papers **6 pages** + unlimited references. HotCRP: `socc26.hotcrp.com`.
- Sponsorship: the **only** conference co-sponsored by **ACM SIGMOD and SIGOPS**. Review:
  **dual-anonymous** with a per-round **rebuttal**; decisions **accept / reject** (no Major
  Revision). PC Co-Chairs reported as Eric Lo and Ivan Beschastnikh (confirm on the live page).

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2025/2026 facts** — carry dates/budgets and trace to a numbered source in the source
   map (e.g., the two-round calendar, the 12-page acmart budget, the SIGMOD+SIGOPS sponsorship).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the SoCC 2026
   PC Co-Chair names and full committee roster).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., whether SoCC runs a
   dedicated artifact-evaluation track for a given edition, the General Chair roster, any AI-use
   disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. SoCC re-decides its structure per edition —
  including the round dates and the cross-round resubmission rule — so verify the cadence before
  anything else each year.
- SoCC has no standing editor-in-chief; chairs rotate per edition under SIGMOD and SIGOPS. The
  publication is conference proceedings in the ACM DL, not a journal.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar system name is not
  proof of a SoCC placement (Mesos, Borg, Spark, and TensorFlow are all sibling-venue papers).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
