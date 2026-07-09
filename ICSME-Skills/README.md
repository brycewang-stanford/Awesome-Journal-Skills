# ICSME Skills

Twelve agent skills for papers targeting **ICSME — the IEEE International Conference on Software
Maintenance and Evolution**, the field's dedicated venue for the software lifecycle *after* first
release: maintenance, evolution, reverse engineering, program comprehension, technical debt,
refactoring, and mining-software-repositories evidence. The pack covers the full arc of an ICSME
campaign: deciding whether a project is ICSME-shaped (and which ICSME track fits) or belongs at ICSE,
FSE, SANER, MSR, or SCAM; building maintenance-empirical evidence that survives a reviewer's audit;
packaging the double-anonymous EasyChair submission on the IEEEtran 10+2 budget with its open-science
obligations; navigating the **single-round** research process with its early-decision cut and
author-response rebuttal; and delivering the IEEE Xplore camera-ready plus a ROSE-Festival-badged
artifact.

Official basis checked on **2026-07-09**: the ICSME 2026 research-track and Important Dates pages,
the EasyChair CFP, the Journal-First / Registered Reports / RENE / artifact-and-ROSE track pages, and
the IEEE author templates. Direct fetches of `conf.researchr.org`, `easychair.org`, and
`ieeexplore.ieee.org` returned 403 in the verification environment, so official pages were read via
search-engine renderings of the exact URLs and cross-checked against IEEE Xplore, dblp, and the
`se-deadlines` aggregator; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Naming note: the venue was **ICSM** through 2013 and **ICSME** from 2014, when "and Evolution" was
> added. A 10-year Most Influential Paper awarded *at ICSME 20XX* honors an *ICSM 20(XX-10)* paper.

## What makes ICSME different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and most
of the mistakes made by authors arriving from an ACM venue, from ICSE/FSE, or from a technique-first
conference:

- **It is the maintenance/evolution venue.** ICSME rewards contributions grounded in the
  *post-release lifecycle* — aging systems, change impact, debt, refactoring safety, comprehension,
  and how software evolves — not greenfield techniques whose maintenance payoff is incidental.
- **The IEEE path, not ACM.** ICSME uses the **IEEEtran two-column** template, publishes in **IEEE
  Xplore**, and awards **IEEE** artifact badges. The 2026 budget is **10 pages** (figures and
  appendices included) **+ 2 reference-only pages**. Do not carry an ACM `acmart` single-column habit
  across.
- **A single research round — no Major Revision.** The research track reviews each paper once,
  double-anonymously, then accepts or rejects. Unlike ESEC/FSE's journal-style revise-and-resubmit,
  there is no revision round: the evidence must be complete on submission.
- **An early-decision cut plus an author-response rebuttal.** At the start of the response period,
  the strongest and weakest papers already receive Accept or Reject; the rest get "Response
  Recommended" and answer the PC's specific questions in a single rebuttal.
- **EasyChair, abstract-then-paper.** Submission is via EasyChair with an abstract-registration step
  a week before the full-paper deadline — not HotCRP, CMT, or OpenReview.
- **A rich set of alternative tracks.** A strong **Journal-First (J1C2)** track presents TSE/EMSE
  papers at the conference; **Registered Reports** review a protocol first; **RENE** rewards
  replications and honest negative results — a maintenance-community distinctive.
- **Open science and ROSE by default.** The **Joint Artifact Evaluation Track and ROSE Festival**
  (shared with co-located SCAM and VISSOFT) awards the IEEE **Open Research Object** and **Research
  Object Reviewed** badges, and a data-availability statement with pinned mining provenance is
  expected at review time.

## Skills

| Skill | What it does |
| --- | --- |
| [`icsme-topic-selection`](skills/icsme-topic-selection/SKILL.md) | Route between ICSME and its siblings (ICSE, FSE, SANER, MSR, ICPC, SCAM, TSE/EMSE) using the lifecycle and re-label tests, and pick the right ICSME track (research / journal-first / registered report / RENE / NIER / tool-demo / industry). |
| [`icsme-workflow`](skills/icsme-workflow/SKILL.md) | Run the single-round year backward from the abstract deadline, through the early-decision cut, the author-response rebuttal, the IEEE Xplore camera-ready, and the ROSE-Festival artifact. |
| [`icsme-writing-style`](skills/icsme-writing-style/SKILL.md) | Build the maintenance-empirical skeleton: the maintenance contribution on the first page, RQ contracts, threats that argue, and 10-page IEEEtran discipline. |
| [`icsme-related-work`](skills/icsme-related-work/SKILL.md) | Cover the maintenance/evolution literature lanes, write delta-first positioning, frame replications for RENE, and keep self-citations double-anonymous. |
| [`icsme-experiments`](skills/icsme-experiments/SKILL.md) | Match evidence to claim shape: real evolving subjects, mining provenance, fair baselines, SE statistics, survivorship and change-history confounds, contamination-aware LLM ablations. |
| [`icsme-reproducibility`](skills/icsme-reproducibility/SKILL.md) | Build the open-science story: an honest data-availability statement, pinned mining/LLM provenance, and anonymized-but-runnable artifacts complete on submission. |
| [`icsme-supplementary`](skills/icsme-supplementary/SKILL.md) | Split content between the reviewed 10 pages and the artifact by decision-criticality — nothing that decides acceptance may live outside the body. |
| [`icsme-submission`](skills/icsme-submission/SKILL.md) | Final EasyChair audit: the abstract-then-paper two-step, the IEEEtran budget, the double-anonymous sweep (incl. own-system leaks), open-science items, desk-reject triage. |
| [`icsme-review-process`](skills/icsme-review-process/SKILL.md) | Model the pipeline — double-anonymity, the early-decision cut, "Response Recommended", single-round accept/reject — and where author leverage exists. |
| [`icsme-author-response`](skills/icsme-author-response/SKILL.md) | Write the single-round rebuttal: read your bucket, answer the PC's specific questions with existing evidence, and stay anonymous. |
| [`icsme-artifact-evaluation`](skills/icsme-artifact-evaluation/SKILL.md) | Convert the accepted paper's package into IEEE ROSE badges (Open Research Object / Research Object Reviewed) on the shared SCAM/VISSOFT artifact deadline. |
| [`icsme-camera-ready`](skills/icsme-camera-ready/SKILL.md) | De-anonymize systematically, complete IEEE metadata and eCopyright, fold in response commitments, permanentize availability links, pass IEEE Xplore checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified ICSM/ICSME papers across five contribution shapes — Most-Influential-Paper honorees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional dependency-update-bot study's abstract and introduction rebuilt to the ICSME arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the ICSME-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ICSME-Skills
claude plugin install icsme-skills
```

Or use the files directly: each `skills/icsme-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an ICSME paper or should it go to MSR/SANER?" → `icsme-topic-selection`
- "Audit my draft against the ICSME research-track rules" → `icsme-submission`
- "We got 'Response Recommended' — plan the rebuttal" → `icsme-author-response`
- "Get this artifact ready for the ROSE badges" → `icsme-artifact-evaluation`

## Pack structure

```text
ICSME-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── icsme-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `icsme-topic-selection`; ICSME overlaps ICSE/FSE and the evolution
   siblings, and it offers many tracks, so choosing the venue *and the track* matters. Skim the
   exemplars library to see what decade-influential maintenance contributions look like.
2. **While building evidence** — keep `icsme-experiments` and `icsme-reproducibility` beside the
   study; mining provenance pinned at collection time cannot be retrofitted, and there is no revision
   round to add it in.
3. **While writing** — `icsme-writing-style` for the body against the worked example,
   `icsme-supplementary` for the body/artifact split, `icsme-related-work` for delta-first
   positioning.
4. **Deadline weeks** — register the abstract before its earlier cutoff, then `icsme-submission` end
   to end on the final PDF and artifact.
5. **After submission** — `icsme-review-process` to calibrate, `icsme-author-response` if you draw
   "Response Recommended", then `icsme-artifact-evaluation` and `icsme-camera-ready` — or the routing
   table in `icsme-topic-selection` if the decision goes the other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- ICSME 2026 is the **42nd** edition: **Benevento, Italy** (University of Sannio),
  **September 14-18, 2026**, co-located with SCAM and VISSOFT. Research abstract 27 Feb 2026, paper
  6 Mar 2026, early decisions 3 May 2026, notification 29 May 2026 (all AoE); submission via
  **EasyChair**.
- Format: **IEEEtran two-column**, **10 pages** (figures/appendices included) **+ 2** reference pages.
  Review: **double-anonymous**, **single round**, with an **early-decision cut** and an
  **author-response** rebuttal — **no Major Revision**.
- Tracks: Research, **Journal-First (J1C2**, TSE/EMSE), **Registered Reports**, **RENE** (Replication
  and Negative Results), NIER, Tool Demonstration and Data Showcase, Industry, Doctoral Symposium.
- Artifacts: **Joint Artifact Evaluation Track and ROSE Festival**, IEEE **Open Research Object** /
  **Research Object Reviewed** badges, post-acceptance, shared with SCAM/VISSOFT.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the 10+2 budget, the single-round early-decision model, the ROSE IEEE badges).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., exact track
   deadlines beyond the research track).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., ICSME 2026 General/Program
   Co-Chair rosters, the camera-ready date, any AI-use disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. ICSME re-decides its structure per edition —
  including whether the abstract-then-paper step and the early-decision cut are retained — so verify
  the current Important Dates page before anything else each year.
- ICSME has no standing editor-in-chief and no APC; chairs rotate per edition under IEEE TCSE.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar maintenance topic
  is not proof of an ICSM/ICSME placement (many are TSE, ICSE, or MSR).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
