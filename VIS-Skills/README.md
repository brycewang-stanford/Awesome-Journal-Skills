# IEEE VIS Skills

Twelve agent skills for papers targeting **IEEE VIS — the IEEE Visualization Conference**, the
flagship venue of the data-visualization community and, since 2021, a single unified conference whose
full papers are published as **journal articles in IEEE TVCG (Transactions on Visualization and
Computer Graphics)**. The pack covers the full arc of a VIS campaign: deciding whether a project is
VIS-shaped (and which of the six areas is its home) or belongs at EuroVis, CHI, SIGGRAPH, or the TVCG
journal track; building a task-justified design and evidence matched to the contribution type;
packaging the author-optional double-blind PCS submission with its supplemental video and open
materials; navigating the **two-phase review** with its **conditional-accept second round**; and
delivering the TVCG camera-ready plus a Graphics Replicability Stamp.

Official basis checked on **2026-07-09**: the IEEE VIS 2026 Call for Full Papers, Paper Submission
Guidelines, Review Instructions, Area Model, and Open Practices pages; the VIS 2026 review-process
changes blog; the IEEE VGTC/TVCG template; and the Graphics Replicability Stamp Initiative. Direct
fetches of `ieeevis.org`, `ieeexplore.ieee.org`, and `precisionconference.com` returned 403 in the
verification environment, so official pages were read via search-engine renderings of the exact URLs
and cross-checked against the official `@ieeevis` announcements, IEEE Xplore/TVCG, the IEEE VIS
Wikipedia entry, and dblp; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Scope-collision warning: IEEE VIS is **not** IEEE VR and **not** ISMAR — sibling VGTC conferences
> on the same PCS society with separate calls. No fact in this pack derives from them.

## What makes VIS different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and most
of the mistakes made by authors arriving from CHI, from a vision/ML venue, or from graphics:

- **Papers are journal articles.** VIS full papers publish in **IEEE TVCG**, the field's top journal.
  The submission is judged at a journal bar that also earns a conference slot — the journal-integrated
  model.
- **Two-phase review with a real second round.** First-round outcomes include a **conditional
  accept**: selected papers enter a full revision-and-review cycle and are accepted only if they make
  the required changes — a journal-style revise-and-review, not a one-shot rebuttal.
- **The Precision Conference System (PCS), under VGTC.** Submission runs through PCS (society VGTC →
  VIS 2026 → Full Papers), not HotCRP, OpenReview, or CMT.
- **The IEEE VGTC/TVCG template and the 9+2 budget.** Papers use the VGTC document class: **up to 9
  pages of content plus up to 2 pages of references and acknowledgements**. This is not `acmart` and
  not a generic two-column IEEEtran habit.
- **Six areas, area-routed.** Since the 2021 unification of SciVis, InfoVis, and VAST, VIS routes each
  paper by a **primary area** — Theoretical & Empirical, Applications, Systems & Rendering,
  Representations & Interaction, Data Transformations, Analytics & Decisions — through Area Paper
  Chairs.
- **Author-optional double-blind.** Anonymizing is recommended but not mandatory — unusual among the
  flagships and a per-cycle choice authors must make deliberately.
- **A supplemental-video and open-practices culture.** Reviewers routinely watch the video; the
  **Graphics Replicability Stamp** (GRSI / TVCG Replicability Stamp) and the Open Practices program
  reward shared, reproducible code and data, with preregistration valued for studies.

## Skills

| Skill | What it does |
| --- | --- |
| [`vis-topic-selection`](skills/vis-topic-selection/SKILL.md) | Route between IEEE VIS and its siblings (EuroVis, PacificVis, CHI, SIGGRAPH, the TVCG journal track) and choose among the six VIS areas by contribution type and evidence maturity. |
| [`vis-workflow`](skills/vis-workflow/SKILL.md) | Run the annual cycle backward from the abstract deadline through the full paper, the two-phase review, the conditional-accept second round, the TVCG camera-ready, and presentation. |
| [`vis-writing-style`](skills/vis-writing-style/SKILL.md) | Build the visualization skeleton: a task-grounded contribution on the first page, encodings justified by task, evaluation matched to the contribution type, honest limitations. |
| [`vis-related-work`](skills/vis-related-work/SKILL.md) | Cover the visualization lanes (VIS areas, EuroVis/CGF, PacificVis, adjacent HCI/graphics), write delta-first positioning, and keep self-citations double-blind. |
| [`vis-experiments`](skills/vis-experiments/SKILL.md) | Match evidence to the contribution type: perceptual and controlled studies with power and effect sizes, CVD-safe encodings, benchmarks, and design-study validation. |
| [`vis-reproducibility`](skills/vis-reproducibility/SKILL.md) | Build the open-practices story: an honest open-materials statement, preregistration for studies, provenance, and a runnable archive. |
| [`vis-supplementary`](skills/vis-supplementary/SKILL.md) | Split content between the reviewed 9 pages and the supplement — including the first-class video — by decision-criticality. |
| [`vis-submission`](skills/vis-submission/SKILL.md) | Final PCS audit: the abstract-then-paper deadlines, the VGTC template and 9+2 budget, the optional double-blind sweep, open materials, desk-risk triage. |
| [`vis-review-process`](skills/vis-review-process/SKILL.md) | Model the pipeline — six-area routing, primary/secondary/external/student reviewers, the two-phase conditional-accept second round — and where author leverage exists. |
| [`vis-author-response`](skills/vis-author-response/SKILL.md) | Write both turns: the first-round engagement and the conditional-accept summary-of-changes that maps every required change to a tracked edit. |
| [`vis-artifact-evaluation`](skills/vis-artifact-evaluation/SKILL.md) | Convert the accepted paper's package into a Graphics Replicability Stamp via an independent volunteer's reproduction, plus Open Practices disclosures. |
| [`vis-camera-ready`](skills/vis-camera-ready/SKILL.md) | De-anonymize, complete TVCG journal metadata, permanentize open-materials links, and pass IEEE production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified IEEE VIS / TVCG papers across five contribution types — Test-of-Time honorees — with self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional uncertainty-encoding study's abstract and introduction rebuilt to the VIS arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the VIS-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./VIS-Skills
claude plugin install vis-skills
```

Or use the files directly: each `skills/vis-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a VIS paper or should it go to EuroVis/CHI, and which area?" → `vis-topic-selection`
- "Audit my draft against the IEEE VIS full-paper rules" → `vis-submission`
- "We got a conditional accept — plan the second-round revision" → `vis-author-response`
- "Get this package ready for the Graphics Replicability Stamp" → `vis-artifact-evaluation`

## Pack structure

```text
VIS-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── vis-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `vis-topic-selection`; VIS overlaps EuroVis and CHI at the edges, and
   choosing the right area routes you to the right reviewers. Skim the exemplars library to see what
   decade-influential VIS contributions look like.
2. **While building evidence** — keep `vis-experiments` and `vis-reproducibility` beside the study;
   an encoding justified by task and a preregistered study cannot be retrofitted.
3. **While writing** — `vis-writing-style` for the body against the worked example,
   `vis-supplementary` for the body/video/archive split, `vis-related-work` for delta-first
   positioning.
4. **Deadline weeks** — submit the abstract with final authors before its cutoff, then `vis-submission`
   end to end on the final PDF and the supplemental package.
5. **After submission** — `vis-review-process` to calibrate, `vis-author-response` for the first round
   and any conditional-accept revision, then `vis-artifact-evaluation` and `vis-camera-ready` — or the
   routing table in `vis-topic-selection` if the decision goes the other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- IEEE VIS 2026 is in **Boston, Massachusetts, USA**, in **November 2026** (reported as 9-13 Nov;
  confirm the day span — 待核实). Abstract deadline **21 March 2026**, full paper **31 March 2026**,
  supplemental **7 April 2026**, first-round notification **15 July 2026** (all 23:59 AoE).
- Publication: **IEEE TVCG**, journal-integrated. Submission: **PCS** under **VGTC**. Review:
  **two-phase, author-optional double-blind**, with a **conditional-accept second round**. Reviewers:
  **primary + secondary + external** (2026 adds an optional student reviewer). Template: **IEEE
  VGTC/TVCG**, **9+2** pages.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the TVCG publication, the 9+2 budget, the two-phase review, the six-area model).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   conference day-span, the full Area Paper Chair roster).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the exact VIS 2026 day span,
   short-paper length and cycle, any generative-AI disclosure policy).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it against
the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. VIS re-decides its structure per edition —
  including area boundaries, reviewer-count rules, and whether double-blind is optional — so verify on
  the current call before anything else each year.
- The **conference** has no standing editor-in-chief; chairs rotate per edition. TVCG (the **journal**)
  has its own editorial board, but VIS papers enter through the **conference call**, not a standalone
  TVCG submission — do not conflate the two intake paths.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar system name is not
  proof of an IEEE VIS placement (it may be EuroVis, CHI, or SIGGRAPH).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
