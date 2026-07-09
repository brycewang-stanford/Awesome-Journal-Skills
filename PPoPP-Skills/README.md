# PPoPP Skills

Twelve agent skills for papers targeting **PPoPP — the ACM SIGPLAN Symposium on Principles and
Practice of Parallel Programming**, the premier forum for parallel and concurrent programming:
languages, compilers, and runtimes for parallelism; lock-free/wait-free data structures and
concurrency-correctness proofs; GPU/accelerator and NUMA performance engineering; parallel
algorithms; and large-scale scalability studies. The pack covers a full PPoPP campaign: deciding
whether a project is PPoPP-shaped or belongs at PLDI, CGO, POPL, ASPLOS, or SC; building the twin
evidence PPoPP demands — **concurrency correctness *and* measured parallel performance**; packaging
the two-column double-blind HotCRP submission; working the **author-response rebuttal**; and
delivering the camera-ready plus a CGO-shared, ACM-badged artifact.

Official basis checked on **2026-07-09**: the PPoPP 2026 (Sydney) and PPoPP 2027 (Salt Lake City)
research-track calls and Important Dates pages, the sigplan.org PPoPP announcements, the PPoPP
HotCRP sites, the PPoPP/CGO artifact-evaluation pages, the ACM Artifact Review and Badging policy,
and the ACM Digital Library proceedings. Direct fetches of `conf.researchr.org`, `sigplan.org`,
and `dl.acm.org` returned 403 in the verification environment, so official pages were read via
search-engine renderings of the exact URLs and cross-checked against the ACM Digital Library, dblp,
and the SIGARCH/SIGPLAN calls; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes PPoPP different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from PLDI, POPL, CGO, or an HPC/systems venue:

- **It is a SIGPLAN symposium about parallelism, not a compiler or a semantics venue.** PPoPP
  rewards work whose *point* is concurrency and parallel performance. A clever compiler pass belongs
  at **CGO/PLDI**; a new logic for concurrency belongs at **POPL**; a machine/microarchitecture
  result belongs at **ASPLOS/HPCA**. PPoPP wants the parallel-programming lesson.
- **Two-column ACM format, tight 10 pages.** Submissions use the **two-column `acmart` `sigplan`**
  proceedings template (`ppopp-acmart-sigplanproc-template.tex`), **10 pages of text and figures**,
  with **references excluded and unlimited**. This is not PLDI's single-column budget and not an
  IEEE box — do not carry either habit over.
- **Double-blind with a real rebuttal.** Review is **double-blind**; there is a scheduled
  **author-response period** (a rebuttal), reviewer matching may use **TPMS**, and there is an
  **External/Extended Review Committee (ERC)** alongside the PC.
- **The co-located four-conference week.** PPoPP runs inside the **HPCA / CGO / PPoPP / CC** umbrella
  event (Sydney 2026; Salt Lake City 2027), so its calendar, artifact process, and even its
  registration are entangled with CGO's — a fact authors use to their advantage.
- **A distinctive artifact-badge policy.** The AE committee awards **Functional *or* Reusable** plus
  **Results Reproduced**; PPoPP deliberately **does not award "Results Replicated"**, and the green
  **Artifacts Available** badge is granted by the publisher from a deposit link with **no audit**.
- **Rejected papers are auto-considered for posters.** Papers not accepted for a regular talk are
  automatically considered for the **poster track**, with **two-page summaries in the proceedings** —
  a genuine second outcome, not a consolation email.
- **A twin evidence bar: correctness and scalability.** A parallel result is judged on *both* that
  it is correct under concurrency (races, linearizability, the memory model) *and* that it actually
  scales (speedup curves, core counts, NUMA effects, GPU occupancy) against a real baseline.

## Skills

| Skill | What it does |
| --- | --- |
| [`ppopp-topic-selection`](skills/ppopp-topic-selection/SKILL.md) | Route between PPoPP and its siblings (PLDI, CGO, POPL, ASPLOS, HPCA, SC, SPAA, OOPSLA) using the "is the parallelism the point?" test and the co-located calendar. |
| [`ppopp-workflow`](skills/ppopp-workflow/SKILL.md) | Run the year backward from the summer deadline through the rebuttal, notification, the post-acceptance AE round, camera-ready, and the co-located presentation. |
| [`ppopp-writing-style`](skills/ppopp-writing-style/SKILL.md) | Build the parallel-programming skeleton in two columns: the concurrency+performance claim up front, a scalability story, and 10-page discipline. |
| [`ppopp-related-work`](skills/ppopp-related-work/SKILL.md) | Cover the parallel-programming lanes (runtimes, lock-free structures, memory models, GPU), write delta-first positioning, and keep citations double-blind. |
| [`ppopp-experiments`](skills/ppopp-experiments/SKILL.md) | Match evidence to claim: correctness under concurrency and measured scalability — speedup curves, core sweeps, NUMA/GPU, variance, and honest baselines. |
| [`ppopp-reproducibility`](skills/ppopp-reproducibility/SKILL.md) | Make parallel results reproducible: pinned hardware/topology, thread pinning, seeds, warm-up, and the environment description evaluators re-run. |
| [`ppopp-supplementary`](skills/ppopp-supplementary/SKILL.md) | Split content between the 10 reviewed pages and the artifact/appendix by decision-criticality — proofs and full sweeps that decide acceptance stay legible. |
| [`ppopp-submission`](skills/ppopp-submission/SKILL.md) | Final HotCRP audit: the two-column template and 10-page budget, the double-blind sweep, the abstract, conflicts against PC+ERC, and desk-risk triage. |
| [`ppopp-review-process`](skills/ppopp-review-process/SKILL.md) | Model the pipeline — double-blind, PC+ERC, TPMS matching, the rebuttal, the decision, and the automatic poster consideration — and where author leverage exists. |
| [`ppopp-author-response`](skills/ppopp-author-response/SKILL.md) | Write the rebuttal for a performance/concurrency paper: answer the missing-baseline and does-it-scale questions with numbers, not adjectives, inside the word cap. |
| [`ppopp-artifact-evaluation`](skills/ppopp-artifact-evaluation/SKILL.md) | Earn PPoPP's badges (Functional/Reusable + Reproduced; Available via the publisher) on the CGO-shared, post-acceptance AE track with reproducible parallel measurements. |
| [`ppopp-camera-ready`](skills/ppopp-camera-ready/SKILL.md) | De-anonymize, complete ACM rights/metadata, permanentize the artifact DOI, and pass ACM production checks for the two-column proceedings. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Archival-verified PPoPP papers across parallel-programming contribution shapes, with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional lock-free-index study's abstract and introduction rebuilt to the PPoPP arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the parallel-measurement checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./PPoPP-Skills
claude plugin install ppopp-skills
```

Or use the files directly: each `skills/ppopp-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a PPoPP paper or should it go to CGO/PLDI/ASPLOS?" → `ppopp-topic-selection`
- "Audit my draft against the PPoPP research-track rules" → `ppopp-submission`
- "Reviewers say it doesn't scale — plan the rebuttal" → `ppopp-author-response`
- "Get this artifact ready for the PPoPP/CGO badges" → `ppopp-artifact-evaluation`

## Pack structure

```text
PPoPP-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── ppopp-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `ppopp-topic-selection`; PPoPP overlaps CGO/PLDI/ASPLOS at the edges, so
   confirm the parallelism is the contribution. Skim the exemplars for what a durable PPoPP result
   looks like.
2. **While building evidence** — keep `ppopp-experiments` and `ppopp-reproducibility` beside the
   study; a scalability curve and a race-freedom argument cannot be retrofitted after the machine is
   gone, and pinned hardware/topology must be recorded at run time.
3. **While writing** — `ppopp-writing-style` for the two-column body against the worked example,
   `ppopp-supplementary` for the 10-page/artifact split, `ppopp-related-work` for delta-first
   positioning.
4. **Deadline weeks** — register the abstract, then `ppopp-submission` end to end on the final PDF
   and double-blind sweep before the AoE cutoff.
5. **After submission** — `ppopp-review-process` to calibrate, `ppopp-author-response` for the
   rebuttal, then `ppopp-artifact-evaluation` and `ppopp-camera-ready` — or the routing table in
   `ppopp-topic-selection` if the decision goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- PPoPP 2026 is the **31st** edition: Sydney, Australia, **January 31 – February 4, 2026**,
  co-located with **HPCA/CGO/CC 2026**. Full-paper submission **1 September 2025**; author response
  **27–29 October 2025**; notification **10 November 2025**; artifact submission **17 November 2025**;
  artifact notification **5 January 2026**; final paper **9 January 2026**.
- PPoPP 2027 is the **32nd** edition: Salt Lake City, Utah, **March 20–24, 2027**, co-located with
  **HPCA/CGO/CC 2027**; a **summer-round** submission **3 August 2026** (`ppopp27-summer.hotcrp.com`),
  author response **6–8 October 2026**, notification **26 October 2026**. Whether a **fall round**
  also runs is 待核实. This is the live next target as of 2026-07-09.
- Format: **two-column `acmart` `sigplan`**, **10 pages** text+figures, **references unlimited**,
  abstract **100–400 words**. Review: **double-blind** with an **author-response rebuttal**.
  Artifacts: **Functional/Reusable + Reproduced** (no "Replicated"); **Available** via the publisher.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — carry dates/budgets and trace to a numbered source in the source
   map (e.g., the 10-page two-column budget, the double-blind rebuttal, the artifact-badge policy).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., exact
   organizing-committee rosters beyond the named chairs, TPMS usage).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., a PPoPP 2027 fall-round
   deadline, any explicit "Revision" decision category, any AI-use disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. PPoPP re-decides its structure per edition —
  including whether a year runs one submission round or two (the 2027 "summer" HotCRP hints at a
  split) — so verify the cadence on the current Important Dates page before anything else.
- PPoPP has no standing editor-in-chief; chairs rotate per edition, appointed by ACM SIGPLAN.
- Because PPoPP shares its week and its artifact culture with CGO, confirm each cycle whether the AE
  track, deadlines, and badge set are run jointly and which committee owns them.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
