# ATC Skills

Twelve agent skills for papers targeting **ATC — the ACM SIGOPS Annual Technical Conference**, the
venue known for about fifty years as the **USENIX Annual Technical Conference** and, from the 2026
edition, continued under **ACM SIGOPS**. ATC is the systems community's **broad, practical**
conference: it takes a wider slice of computer systems than the more selective OSDI/SOSP flagships,
prizes real implementations and experimental results, and runs a dedicated **Deployed Systems /
experience** lane. The pack covers a full ATC campaign: deciding whether a project is ATC-shaped or
belongs at OSDI, NSDI, EuroSys, FAST, or a workshop; surviving the **new two-round extended-abstract
review**; anonymizing the double-blind HotCRP submission; navigating **conditional acceptance and
shepherding**; and delivering the camera-ready plus a USENIX-lineage badged artifact.

Official basis checked on **2026-07-09**: the ATC 2026 SIGOPS call for papers and home page, the
ATC 2026 HotCRP site, the USENIX ATC '25 research and artifact calls, the USENIX-to-SIGOPS
transition record, the ACM SIGOPS conference list, and dblp. Direct fetches of `sigops.org`,
`usenix.org`, and the aggregator sites returned 403 in the verification environment, so official
pages were read via search-engine renderings of the exact URLs and cross-checked against the
USENIX ATC '25 pages, the Wikipedia history article, and dblp; the full trail, including everything
still marked 待核实, is in [`resources/official-source-map.md`](resources/official-source-map.md).

> Acronym-collision warning: **ATC** also names the *American Transplant Congress* and an *Academic
> Tax Conference*. Neither is this ATC, and no fact in this pack derives from them. This ATC is the
> computer-systems conference.

## What makes ATC different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and
most of the mistakes made by authors arriving from OSDI/SOSP, from NSDI, or from an older USENIX
ATC cycle:

- **It just changed sponsor, name, and calendar — all at once.** ATC 2026 is the **first ACM
  SIGOPS** edition after ~50 years as **USENIX ATC**. It kept the acronym, moved to **Hong Kong,
  15-18 November 2026**, switched to a **June deadline** (a break from the old winter-deadline /
  summer-conference rhythm), and moved to **ACM Open Access**. Do not carry a pre-2026 USENIX
  assumption forward.
- **Two-round, extended-abstract review.** Every submission uploads a **two-page extended abstract**
  with the full paper. Round 1: two experienced reviewers judge the abstract and cut below-bar
  papers early. Round 2: 3-4 reviewers read the full paper. The extended abstract is **review-only,
  not published**, and must stand alone.
- **Breadth is the point.** ATC's scope spans OS, storage, networking, virtualization, distributed
  systems, performance, reliability, energy, and troubleshooting, "of all scales from embedded
  devices to clouds," with an emphasis on **implementations and experimental results**. Papers a
  flagship might call incremental are in scope here if they are solid and useful.
- **Deployed Systems / experience papers are first-class.** A dedicated track accepts papers about
  real-world deployed systems that **need not present new ideas** — they are judged on practical
  insight. (Track continuity under SIGOPS is 待核实.)
- **Double-blind, then shepherded.** Review is double-blind; accepted papers are **conditionally
  accepted** and must satisfy a **shepherd** before final acceptance.
- **USENIX-lineage artifact badging.** Artifacts earn **Available / Functional / Reproduced** badges
  from an Artifact Evaluation Committee on a separate post-acceptance schedule — an active,
  high-participation culture (ATC '25: 94% Functional, 77% Reproduced).
- **Open access with a new twist.** USENIX ATC published proceedings, slides, and talk videos free;
  the SIGOPS edition publishes under **ACM Open Access** with a subsidized transition APC.

## Skills

| Skill | What it does |
| --- | --- |
| [`atc-topic-selection`](skills/atc-topic-selection/SKILL.md) | Route between ATC and its siblings (OSDI, SOSP, NSDI, EuroSys, FAST, HotOS/workshops) using breadth-vs-selectivity, the deployed-systems test, and the calendar. |
| [`atc-workflow`](skills/atc-workflow/SKILL.md) | Run the year backward from the June deadline through the two review rounds, rebuttal, conditional-acceptance shepherding, artifact evaluation, and the ACM camera-ready. |
| [`atc-writing-style`](skills/atc-writing-style/SKILL.md) | Build the systems paper: a self-standing two-page extended abstract, an implementation-and-measurement narrative, and page-budget discipline in the two-column format. |
| [`atc-related-work`](skills/atc-related-work/SKILL.md) | Cover the systems literature lanes, position against OSDI/NSDI/EuroSys/FAST, and keep self-citation double-blind. |
| [`atc-experiments`](skills/atc-experiments/SKILL.md) | Match evidence to claim: real testbeds, honest baselines, end-to-end plus microbenchmarks, tail latency and variance, and workload realism. |
| [`atc-reproducibility`](skills/atc-reproducibility/SKILL.md) | Build the artifact story: pinned environments, a turnkey path to the headline numbers, and an anonymized-but-runnable review package. |
| [`atc-supplementary`](skills/atc-supplementary/SKILL.md) | Split content across the extended abstract, the paper body, the appendix, and the artifact by review-round and decision-criticality. |
| [`atc-submission`](skills/atc-submission/SKILL.md) | Final HotCRP audit: the paired abstract+paper upload, the two-column budget, the double-blind sweep, and desk-risk triage before the AoE cutoff. |
| [`atc-review-process`](skills/atc-review-process/SKILL.md) | Model the pipeline — two rounds, extended-abstract gate, 3-4 second-round reviewers, rebuttal, conditional acceptance, shepherding — and where author leverage exists. |
| [`atc-author-response`](skills/atc-author-response/SKILL.md) | Write the rebuttal and the description-of-changes that a shepherd will check line by line. |
| [`atc-artifact-evaluation`](skills/atc-artifact-evaluation/SKILL.md) | Convert the accepted paper's package into Available / Functional / Reproduced badges on the AEC's own deadline. |
| [`atc-camera-ready`](skills/atc-camera-ready/SKILL.md) | De-anonymize, satisfy the shepherd's required revisions, complete ACM Open Access metadata, and pass production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list, including the transition-driven volatilities. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (SIGOPS CFP, ATC HotCRP, USENIX legacy pages, ACM DL) plus cross-check sources for when the gateway blocks a direct fetch. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Verified USENIX ATC papers across contribution shapes — Test-of-Time and Best-Paper honorees — with self-check questions and sibling-venue guards. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional storage-cache paper's extended abstract + introduction rebuilt to the ATC arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the ATC-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ATC-Skills
claude plugin install atc-skills
```

Or use the files directly: each `skills/atc-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an ATC paper or should it go to OSDI/NSDI?" → `atc-topic-selection`
- "Audit my draft against the ATC 2026 rules" → `atc-submission`
- "Write the extended abstract so it survives round one" → `atc-writing-style`
- "We were conditionally accepted — plan the shepherd revision" → `atc-author-response`
- "Get this artifact ready for the ATC badges" → `atc-artifact-evaluation`

## Pack structure

```text
ATC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── atc-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `atc-topic-selection`; ATC overlaps OSDI/NSDI/EuroSys/FAST, and the
   breadth-vs-selectivity call plus the June calendar matters. Skim the exemplars for what durable
   ATC contributions look like.
2. **While building evidence** — keep `atc-experiments` and `atc-reproducibility` beside the system;
   testbed provenance and pinned environments cannot be retrofitted at submission time.
3. **While writing** — `atc-writing-style` for a self-standing extended abstract and body,
   `atc-supplementary` for the abstract/body/appendix/artifact split, `atc-related-work` for
   sibling-aware positioning.
4. **Deadline weeks** — `atc-submission` end to end on the paired extended-abstract + full-paper
   upload and the double-blind sweep, before the June AoE cutoff.
5. **After submission** — `atc-review-process` to calibrate the two rounds, `atc-author-response`
   for the rebuttal and the shepherd's description-of-changes, then `atc-artifact-evaluation` and
   `atc-camera-ready` — or the routing table in `atc-topic-selection` if the decision goes the
   other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- ATC 2026 is the **first ACM SIGOPS Annual Technical Conference** (formerly USENIX ATC):
  **Hong Kong (Hyatt, Shatin), 15-18 November 2026**. Submission deadline **early June 2026** (AoE;
  1 vs. 10 June unresolved across renderings — 待核实).
- **Two-round review:** a two-page extended abstract (review-only, not published) gated by two
  reviewers, then 3-4 reviewers on the full paper. **≤12 pages** full, **≤6** short, excluding
  references/appendices; **two-column**, 178×229 mm, 10pt. **Double-blind.** **Conditional
  acceptance + shepherding.** HotCRP: `atc26.hotcrp.com`.
- **Artifacts:** Available / Functional / Reproduced badges via an AEC on a separate post-acceptance
  schedule. **Publication:** ACM Open Access (subsidized transition APC).

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/limits and trace to a numbered source in the source map
   (e.g., the two-round model, the 12/6-page budget, the three artifact badges).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., submission
   volumes and the exact APC figures).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the exact June day, the
   mandated template file, Deployed-Systems-Track continuity, chair rosters, any AI-disclosure
   policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- ATC 2026 is a **transition edition**; the name, sponsor, publisher, calendar, and review structure
  all moved at once. Re-verify each against the current SIGOPS call before advising — none is a
  stable, permanent rule yet.
- ATC has no standing editor-in-chief; chairs rotate per edition under SIGOPS. USENIX's legacy ATC
  proceedings, slides, and videos remain on the USENIX site; new editions publish in the ACM DL
  under Open Access.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a famous systems name is not
  proof of an ATC placement (many landmark systems papers are OSDI/SOSP/NSDI, not ATC).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
