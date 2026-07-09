# ASE Skills

Twelve agent skills for papers targeting **ASE — the IEEE/ACM International Conference on Automated
Software Engineering**, the premier venue for research that *automates* software-engineering tasks:
analysis, testing, synthesis, repair, comprehension, and the two-way street of AI4SE and SE4AI. The
pack covers the full arc of an ASE campaign: deciding whether a project is ASE-shaped (an
automation) or belongs at ICSE, FSE, ISSTA, a PL venue, or an SE journal; building an evaluation
that survives an automated-SE reviewer's audit; packaging the double-anonymous HotCRP submission
with its mandatory Data Availability Statement; navigating the **early-rejection gate**, the
rebuttal, and the criteria-bound **Revision** round; and delivering a camera-ready plus an
ACM-badged artifact indexed in both IEEE Xplore and the ACM Digital Library.

Official basis checked on **2026-07-09**: the ASE 2026 (Munich) and ASE 2025 (Seoul) research-track
calls and Important Dates pages, the ASE HotCRP sites, the ACM Artifact Review and Badging policy,
and the ASE Most Influential Paper award pages. Direct fetches of `conf.researchr.org` returned 403
in the verification environment, so official pages were read via search-engine renderings of the
exact URLs and cross-checked against dblp (ASE proceedings under the historical series key
`conf/kbse`), the ACM Digital Library, IEEE Xplore, and the ASE HotCRP sites; the full trail,
including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Acronym-collision warning: "ASE" also names the *Association for Science Education* and the
> *Association for Surgical Education*, and the Springer journal *Automated Software Engineering*
> (AUSE) is a related but distinct venue. No fact in this pack derives from those.

## What makes ASE different from its siblings

These venue mechanics, verified for the 2025/2026 cycles, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from ICSE, FSE, ISSTA, or an ML venue:

- **The contribution is an *automation*.** ASE rewards a technique or tool that automates an SE task,
  evaluated on real subjects — not a broad empirical finding (which leans FSE), a testing-theory
  result (ISSTA), or a model advance (an ML venue). The model-swap test decides borderline cases.
- **Dual IEEE/ACM sponsorship, dual proceedings.** ASE is jointly sponsored by IEEE and ACM SIGSOFT,
  and accepted papers are indexed in **both IEEE Xplore and the ACM Digital Library** — unlike
  ACM-only FSE/PACMSE.
- **A template that follows the sponsorship.** Because of the dual sponsorship, the mandated format
  has varied by edition (IEEE two-column vs. ACM `acmart`). ASE 2026 requires the ACM Primary
  Article Template — `\documentclass[sigconf,review,anonymous]{acmart}`. Confirm per cycle; do not
  carry an old habit over.
- **A 10+2 page budget with a mandatory Data Availability Statement.** 10 pages for all content plus
  2 for references only; the Data Availability Statement sits after the Conclusions and counts
  inside the 10 pages. Accepted papers get one extra content page.
- **An early-rejection gate before rebuttal.** Papers with uniformly negative initial scores are
  rejected before the rebuttal period — a fast answer and a filter that concentrates rebuttal effort.
- **A criteria-bound Revision round.** First outcomes are Accept, **Revision**, or Reject. A Revision
  fixes concrete, actionable criteria in advance; reviewers accept in principle if they are met, and
  authors return a revised paper with a point-by-point summary of changes.
- **Co-located tracks: NIER, Tools-and-Datasets, Journal-First.** New Ideas and Emerging Results (4
  pages), tool demonstrations (≤4 pages), and a Journal-First path for TSE/TOSEM/EMSE work.

## Skills

| Skill | What it does |
| --- | --- |
| [`ase-topic-selection`](skills/ase-topic-selection/SKILL.md) | Route between ASE and its siblings (ICSE, FSE, ISSTA, PL venues, ML venues, TSE/TOSEM/EMSE) by the automation-centric contribution shape and the model-swap and re-label tests. |
| [`ase-workflow`](skills/ase-workflow/SKILL.md) | Run the year backward from the deadline, through abstract registration, the early-rejection gate, rebuttal, the Revision round, artifact evaluation, and the dual-proceedings camera-ready. |
| [`ase-writing-style`](skills/ase-writing-style/SKILL.md) | Build the automation-first arc: name the task, keep the tool runnable, pass the model-swap test, argue threats, and hold the 10+2 budget. |
| [`ase-related-work`](skills/ase-related-work/SKILL.md) | Cover the automated-SE lanes, write delta-first against named runnable tools, frame fair head-to-heads, and keep self-citations anonymous. |
| [`ase-experiments`](skills/ase-experiments/SKILL.md) | Match evidence to the automation claim: real subjects, fair tool baselines, ablations isolating a learned component, oracles, contamination-aware LLM handling, provenance. |
| [`ase-reproducibility`](skills/ase-reproducibility/SKILL.md) | Build the open-science story: the mandatory Data Availability Statement, anonymized-but-runnable tools, pinned provenance, cached LLM outputs. |
| [`ase-supplementary`](skills/ase-supplementary/SKILL.md) | Split content between the 10 reviewed pages and the artifact by decision-criticality — nothing that decides acceptance lives outside the body. |
| [`ase-submission`](skills/ase-submission/SKILL.md) | Final HotCRP audit: template and 10+2 budget, the double-anonymous sweep (incl. tool names), the Data Availability Statement, desk-risk triage. |
| [`ase-review-process`](skills/ase-review-process/SKILL.md) | Model the pipeline — double-anonymous review, the early-rejection gate, Accept/Revision/Reject, the criteria-bound revision — and where author leverage exists. |
| [`ase-author-response`](skills/ase-author-response/SKILL.md) | Write both turns: the rebuttal that first survives the early-rejection gate and the revision summary-of-changes that maps every criterion to a change. |
| [`ase-artifact-evaluation`](skills/ase-artifact-evaluation/SKILL.md) | Convert the accepted paper's tool into ACM Artifacts Available / Reusable badges on the artifact track's own deadline. |
| [`ase-camera-ready`](skills/ase-camera-ready/SKILL.md) | De-anonymize systematically, spend the extra page on feedback, permanentize the Data Availability link, and pass dual IEEE-Xplore/ACM-DL production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2025/2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified ASE papers across five contribution shapes — Most Influential Paper honorees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional flaky-test-repair tool's abstract and introduction rebuilt to the ASE arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the ASE-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ASE-Skills
claude plugin install ase-skills
```

Or use the files directly: each `skills/ase-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an ASE paper or should it go to FSE/ISSTA?" → `ase-topic-selection`
- "Audit my draft against the ASE research-track rules" → `ase-submission`
- "We got a Revision — plan the summary-of-changes" → `ase-author-response`
- "Get this tool ready for the ACM artifact badges" → `ase-artifact-evaluation`

## Pack structure

```text
ASE-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── ase-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `ase-topic-selection`; ASE overlaps ICSE/FSE/ISSTA, so the automation
   test and the calendar matter. Skim the exemplars library to see what decade-influential
   automated-SE contributions look like.
2. **While building evidence** — keep `ase-experiments` and `ase-reproducibility` beside the tool;
   fair baselines and pinned provenance cannot be retrofitted.
3. **While writing** — `ase-writing-style` for the automation-first arc against the worked example,
   `ase-supplementary` for the body/artifact split, `ase-related-work` for delta-first positioning.
4. **Deadline weeks** — register the abstract early, then `ase-submission` end to end on the final
   PDF and artifact.
5. **After submission** — `ase-review-process` to calibrate, `ase-author-response` for the rebuttal
   and any Revision round, then `ase-artifact-evaluation` and `ase-camera-ready` — or the routing
   table in `ase-topic-selection` if the decision goes the other way.

## 2025/2026-cycle anchor facts (historical snapshot, not permanent rules)

- ASE 2026 is the **41st** edition: Munich, Germany, **October 12-16, 2026**. Research submission
  **26 March 2026**; notification **25 May 2026**; portal `ase26.hotcrp.com`. As of 2026-07-09 the
  notification has passed, so ASE 2027 is the next submission target (host/dates 待核实).
- ASE 2025 was the **40th** edition: Seoul, Republic of Korea, **November 16-20, 2025**.
- Format: **ACM Primary Article Template** (`\documentclass[sigconf,review,anonymous]{acmart}` for
  2026); **10 pages** content **+ 2** reference pages; **mandatory Data Availability Statement** after
  Conclusions. Review: **double-anonymous**, with an **early-rejection gate** before rebuttal and
  **Accept / Revision / Reject** outcomes. Proceedings: **IEEE Xplore and the ACM Digital Library**.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2025/2026 facts** — carry dates/budgets and trace to a numbered source in the source
   map (e.g., the 10+2 budget, the ACM `acmart` requirement, the early-rejection gate, the
   Available/Reusable badges).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the ASE 2025
   acceptance rate reported by a community tracker).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the ASE 2026 abstract
   deadline, the full Program Co-Chair roster, ASE 2027 host/dates, whether Functional/Reproduced
   badges are offered, any AI-use disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. ASE re-decides its structure per edition —
  including the required template (IEEE vs. ACM), the deadline count, and the artifact badges — so
  verify before anything else each year.
- ASE has no standing editor-in-chief; chairs rotate per edition under IEEE and ACM SIGSOFT. The
  dual sponsorship, not a single society, is why proceedings land in both IEEE Xplore and the ACM
  DL.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar tool name is not
  proof of an ASE placement (dblp indexes ASE under `conf/kbse`).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
