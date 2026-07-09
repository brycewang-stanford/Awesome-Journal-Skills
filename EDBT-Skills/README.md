# EDBT Skills

Twelve agent skills for papers targeting **EDBT — the International Conference on Extending Database
Technology**, the European database-systems flagship. EDBT is held as a **joint conference with
ICDT** (its database-theory sibling), publishes **open-access on OpenProceedings.org**, and runs a
distinctive **multiple-cycle rolling submission model** rather than a single annual deadline. The
pack covers the full arc of an EDBT campaign: deciding whether a project is EDBT-shaped or belongs
at SIGMOD, VLDB, ICDE, or ICDT; choosing a submission cycle and a paper shape (Regular,
Experiments & Analysis, or Vision); packaging the Microsoft CMT submission; navigating the in-cycle
**revise-and-resubmit** round; and delivering the OpenProceedings camera-ready with a reproducible
artifact.

Official basis checked on **2026-07-09**: the EDBT/ICDT 2026 (Tampere) research and industrial
calls, the EDBT Association pages on `edbt.org`, the EDBT 2027 cycle deadlines, the
OpenProceedings.org volume pages, and dblp. Direct fetches of `edbticdt2026.github.io`, `edbt.org`,
and `openproceedings.org` returned 403 in the verification environment, so official pages were read
via search-engine renderings of the exact URLs and cross-checked against OpenProceedings tables of
contents, dblp, WikiCFP, and the co-located ICDT call on `databasetheory.org`; the full trail,
including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Acronym-collision warning: **EDBT is a databases conference.** It is not EDTM (IEEE Electron
> Devices Technology and Manufacturing) or any similarly abbreviated venue. No fact in this pack
> derives from a non-database source.

## What makes EDBT different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from SIGMOD, VLDB, ICDE, or the ICDT theory side:

- **Open access on OpenProceedings.org, not a paywalled DL.** EDBT proceedings are published on
  **OpenProceedings.org** — the platform **founded by ICDT and EDBT** — under a **CC-BY-NC-ND 4.0**
  license with **copyright retained by authors**, an **ISBN** per volume, and DBLP/Scholar/SCOPUS
  indexing. There is **no ACM/IEEE paywall and no article-processing charge**. This is the sharpest
  contrast with SIGMOD/ICDE (ACM DL / IEEE Xplore) and PVLDB.
- **A multiple-cycle rolling model, not one annual deadline.** Since 2022 EDBT runs **three
  submission/publication cycles per year**. You pick the cycle that fits your readiness; earlier
  cycles present at that year's conference, and the last cycle rolls to the next edition.
- **A real in-cycle revise-and-resubmit.** Each cycle runs submit → **author feedback phase** →
  **accept / revise / reject** → **revised submission** → **accept / reject** on the revision. A
  *revise* is a genuine second read by the same reviewers within the cycle — closer to a journal
  R&R than to a one-shot rebuttal.
- **Paper shapes are first-class.** EDBT distinguishes **Regular** research papers, **Experiments &
  Analysis** papers (a benchmarking/repeatability contribution in its own right), and short
  **Vision** papers — each with its own page budget and its own reviewing expectations.
- **The European database-systems scope, with ICDT next door.** EDBT rewards *extending* database
  technology: systems, applied data management, and experiments-and-analysis work. Its co-located
  sibling **ICDT** takes the theory; routing between them is a live decision, distinct from the
  US SIGMOD/PODS pairing.
- **Microsoft CMT and a 12-month resubmission ban.** Reviewing runs in **Microsoft CMT**, and work
  rejected or withdrawn from an EDBT track cannot be resubmitted to any EDBT track in the same paper
  format for **12 months**.
- **A reproducibility-forward community.** The database community's reproducibility culture has deep
  EDBT/SIGMOD roots; Experiments & Analysis papers and inspectable artifacts are valued, not
  optional extras.

## Skills

| Skill | What it does |
| --- | --- |
| [`edbt-topic-selection`](skills/edbt-topic-selection/SKILL.md) | Route between EDBT and its siblings (SIGMOD, VLDB, ICDE, ICDT, and data-management journals) by contribution shape, systems-vs-theory pull, and which submission cycle is nearest. |
| [`edbt-workflow`](skills/edbt-workflow/SKILL.md) | Run the rolling-cycle calendar: choose a cycle, plan backward through the author-feedback phase and the revise-and-resubmit window, and handle the cycle-to-conference roll. |
| [`edbt-writing-style`](skills/edbt-writing-style/SKILL.md) | Build the systems-paper skeleton: a data-management problem up front, a reproducible design, evaluation that survives a database reviewer, and page-budget discipline per paper shape. |
| [`edbt-related-work`](skills/edbt-related-work/SKILL.md) | Cover the data-management literature lanes, write delta-first positioning against SIGMOD/VLDB/ICDE/ICDT, and handle the 12-month resubmission ban and prior-version overlap. |
| [`edbt-experiments`](skills/edbt-experiments/SKILL.md) | Match evidence to claim shape for systems work: real workloads and datasets, fair baselines, honest measurement, and the Experiments & Analysis paper standard. |
| [`edbt-reproducibility`](skills/edbt-reproducibility/SKILL.md) | Build the reproducibility story: a runnable artifact, pinned environments and data provenance, and consistency between the paper and the package for an open-access record. |
| [`edbt-supplementary`](skills/edbt-supplementary/SKILL.md) | Split content between the reviewed pages and the artifact by decision-criticality, within the per-shape page budget and unlimited-references rule. |
| [`edbt-submission`](skills/edbt-submission/SKILL.md) | Final CMT audit: cycle choice, paper shape, OpenProceedings/host template and page budget, the resubmission-ban check, reproducibility items, and desk-risk triage. |
| [`edbt-review-process`](skills/edbt-review-process/SKILL.md) | Model the pipeline — CMT reviewing, the author-feedback phase, accept/revise/reject, the in-cycle second read, and the cycle-to-conference roll — and where author leverage exists. |
| [`edbt-author-response`](skills/edbt-author-response/SKILL.md) | Write both turns: the short author-feedback response and the revise-and-resubmit change letter that maps every reviewer request to a concrete revision. |
| [`edbt-artifact-evaluation`](skills/edbt-artifact-evaluation/SKILL.md) | Prepare a database-systems artifact and reproducibility package: a turnkey run, pinned workloads, and DOI-issuing archival for the open-access record. |
| [`edbt-camera-ready`](skills/edbt-camera-ready/SKILL.md) | Finalize the OpenProceedings camera-ready: the host LaTeX template, CC-BY-NC-ND license and ISBN metadata, permanent artifact links, and the copyright/e-rights form. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026/2027 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Verified EDBT papers across contribution shapes, with self-check questions and a sibling-confusion guard against SIGMOD/VLDB/ICDE/ICDT. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional query-optimization study's abstract and introduction rebuilt to the EDBT arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the EDBT-specific reproducibility checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./EDBT-Skills
claude plugin install edbt-skills
```

Or use the files directly: each `skills/edbt-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an EDBT paper or should it go to SIGMOD/VLDB/ICDT?" → `edbt-topic-selection`
- "Which EDBT cycle should we target, and what does the calendar look like?" → `edbt-workflow`
- "Audit my draft against the EDBT research-track rules before the CMT upload" → `edbt-submission`
- "We got a *revise* — plan the revised submission and the change letter" → `edbt-author-response`

## Pack structure

```text
EDBT-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── edbt-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `edbt-topic-selection`; EDBT, SIGMOD, VLDB, and ICDE overlap, and the
   EDBT/ICDT split matters, so choosing by contribution shape and the nearest cycle is the
   highest-leverage move. Skim the exemplars library to see what an EDBT contribution looks like.
2. **While building evidence** — keep `edbt-experiments` and `edbt-reproducibility` beside the
   system; workloads, baselines, and provenance pinned at measurement time cannot be retrofitted.
3. **While writing** — `edbt-writing-style` for the body against the worked example,
   `edbt-supplementary` for the body/artifact split, `edbt-related-work` for delta-first
   positioning against the data-management venues.
4. **Cycle weeks** — pick the cycle with `edbt-workflow`, then run `edbt-submission` end to end on
   the final PDF and artifact for the Microsoft CMT upload.
5. **After submission** — `edbt-review-process` to calibrate, `edbt-author-response` for the
   author-feedback turn and any revise-and-resubmit round, then `edbt-artifact-evaluation` and
   `edbt-camera-ready` — or the routing table in `edbt-topic-selection` if the decision goes the
   other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- EDBT 2026 was the **29th** edition: the **EDBT/ICDT 2026 Joint Conference**, Tampere, Finland,
  **24-27 March 2026**, organized by Tampere University. As of 2026-07-09 it has been held.
- **EDBT 2027 cycle deadlines:** **4 Feb 2026**, **10 Jun 2026**, and **7 Oct 2026**. As of
  2026-07-09, cycles 1 and 2 have passed and **cycle 3 (7 Oct 2026)** is the live upcoming deadline.
- Publication: **OpenProceedings.org**, open access, **CC-BY-NC-ND 4.0**, ISBN per volume, no APC.
  Review: **Microsoft CMT**, three cycles per year, in-cycle **accept/revise/reject**. Paper shapes
  (EDBT 2022 CFP): **Regular** and **Experiments & Analysis** ≤12 pages + unlimited references,
  **Vision** ≤6 pages + unlimited references (**待核实** for the current cycle).

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027 facts** — trace to a numbered source in the source map (e.g., the
   OpenProceedings CC-BY-NC-ND publication, the three-cycle model, the EDBT 2027 cycle deadlines,
   the Tampere edition).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   per-cycle author-feedback and revision dates, the publication-month clustering).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., single- vs double-blind
   for the current cycle, the exact current page budgets, the EDBT reproducibility/badge program,
   EDBT 2027 location, and full chair rosters).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. EDBT re-decides its structure per edition —
  including the number of cycles and the per-cycle timeline — so verify the cadence on the current
  host site before anything else each year.
- EDBT has no standing editor-in-chief and no APC; chairs rotate per edition, and the host site
  moves each year (Barcelona 2025, Tampere 2026). Treat people and URLs as per-edition.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar tool name is not
  proof of an EDBT placement rather than a SIGMOD/VLDB/ICDE/ICDT one.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
