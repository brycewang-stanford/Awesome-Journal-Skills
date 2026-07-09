# SIGGRAPH Skills

Twelve agent skills for papers targeting the **ACM SIGGRAPH Technical Papers program** — the
computer-graphics flagship, and, with its sister conference **SIGGRAPH Asia**, the pair whose
accepted research is published as special issues of **ACM Transactions on Graphics (TOG)**. The
pack covers the full arc of a SIGGRAPH campaign: deciding whether a project is SIGGRAPH-shaped or
belongs at Eurographics/EGSR, SGP, SCA, or a vision venue; building **shown** graphics evidence
(teaser, results video, head-to-head comparisons, timings) that survives a domain-expert reviewer;
packaging the **Linklings** submission with its two-step form-then-upload deadline; navigating the
single-round review with its **1000-word rebuttal**, Technical Papers Committee meeting, and
**conditional-accept second stage**; and delivering the TOG camera-ready plus a runnable,
replicability-stamp-ready code release.

Official basis checked on **2026-07-09**: the SIGGRAPH 2026 and SIGGRAPH Asia 2026 technical-papers
calls, submissions FAQs, and reviewer-instructions pages; the ACM SIGGRAPH author instructions; the
ACM TOG journal and author guidelines; and the Graphics Replicability Stamp Initiative. Direct
fetches of `s2026.siggraph.org`, `asia.siggraph.org`, and `dl.acm.org` returned 403/405 in the
verification environment, so official pages were read via search-engine renderings of the exact
URLs and cross-checked against the ACM Digital Library (TOG), dblp, and the ACM SIGGRAPH blog; the
full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes SIGGRAPH different from its siblings

These venue mechanics, verified for the 2026 cycles, drive most of the advice in the skills — and
most of the mistakes made by authors arriving from a vision venue (CVPR/ICCV), a visualization
venue (VIS), or a specialized graphics symposium:

- **Papers are journal articles.** SIGGRAPH Technical Papers publish as a special issue of **ACM
  Transactions on Graphics (TOG)** — SIGGRAPH 2026 is **TOG Volume 45, Issue 4**. Acceptance yields
  a journal DOI and issue placement, not just conference proceedings.
- **Two integrated tracks, one review.** Every submission is **dual-track** (eligible for Journal or
  Conference publication) or **Journal-only**, scored on a **single 6-point scale** (Strong
  Reject … Strong Accept). The Technical Papers Committee assigns the track at accept time, being
  **less demanding on validation for the Conference track** to allow riskier/earlier-stage work.
- **Two cycles a year.** SIGGRAPH North America (deadline ~January, summer conference) and SIGGRAPH
  Asia (deadline ~May, December conference) run the same model — a rejected paper is naturally
  revised for the next cycle.
- **A short, text-only rebuttal.** After reviews, authors get **one turn of ≤ 1000 words, text
  only** (no images, video, or URLs) to correct factual errors — then a **Technical Papers Committee
  meeting** decides, and **conditionally accepted** papers pass a **second-stage** committee
  verification.
- **The ACM `acmart` path, journal format.** The required class is **`acmart` ≥ 2.16** in the
  `acmtog` lineage; the Conference-track body is **≤ 7 pages excluding references and up to two
  figures-only pages**. Submission is via **Linklings**.
- **The supplemental video is primary evidence.** Motion, temporal coherence, and rendering
  artifacts do not survive as stills; reviewers watch the results video, so it is a first-class
  deliverable (with rights cleared on every frame).
- **Community-run replicability, not ACM badges.** The graphics equivalent of artifact evaluation is
  the **Graphics Replicability Stamp (GRSI)** and **Code Replicability in Computer Graphics
  (CRCG)** — volunteers rebuild your code and reproduce your results, archived via Software
  Heritage — earned after acceptance, independent of review.

## Skills

| Skill | What it does |
| --- | --- |
| [`siggraph-topic-selection`](skills/siggraph-topic-selection/SKILL.md) | Route between SIGGRAPH, SIGGRAPH Asia, direct-to-TOG, and siblings (CVPR/ICCV, CHI/UIST, Eurographics/EGSR/SGP/SCA/HPG/I3D), and choose dual-track vs Journal-only, using the visual-result, capability-axis, and model-swap tests. |
| [`siggraph-workflow`](skills/siggraph-workflow/SKILL.md) | Plan backward from the deadline across the two annual cycles, through the form-then-upload steps, the rebuttal, the committee decision, the conditional-accept second stage, TOG camera-ready, and in-person presentation. |
| [`siggraph-writing-style`](skills/siggraph-writing-style/SKILL.md) | Build the SIGGRAPH first-page arc: a teaser that carries the paper, a graphics contribution on a measurable axis, shown results, and acmart 7-page discipline. |
| [`siggraph-related-work`](skills/siggraph-related-work/SKILL.md) | Cover the graphics literature lanes (rendering, geometry, animation, simulation, imaging, learning-for-graphics), position by capability delta, and attribute correctly across SIGGRAPH/SA/TOG/EG/EGSR/SGP/SCA. |
| [`siggraph-experiments`](skills/siggraph-experiments/SKILL.md) | Match shown evidence to the graphics claim: faithful head-to-head comparisons, quality metrics with visuals, ablations, and timings on stated hardware at matched quality. |
| [`siggraph-reproducibility`](skills/siggraph-reproducibility/SKILL.md) | Build result-reproducibility: deterministic regeneration, pinned scenes/meshes/weights and hardware, honest tolerances, and a runnable code+asset release. |
| [`siggraph-supplementary`](skills/siggraph-supplementary/SKILL.md) | Craft the supplemental package — above all the results video — and split evidence between the 7-page body and the supplemental by decision-criticality. |
| [`siggraph-submission`](skills/siggraph-submission/SKILL.md) | Final Linklings audit: the form-then-upload two-step deadline, acmart ≥ 2.16 and the page budget, dual-track choice, the representative image and results video, desk-risk triage. |
| [`siggraph-review-process`](skills/siggraph-review-process/SKILL.md) | Model the pipeline — single 6-point scale, primary/secondary/tertiary reviewers, rebuttal, committee meeting, conditional accept + second stage, dual-track assignment — and where author leverage exists. |
| [`siggraph-author-response`](skills/siggraph-author-response/SKILL.md) | Write the ≤ 1000-word, text-only rebuttal that corrects factual errors for the pivotal reviewer, and plan the conditional-accept change list. |
| [`siggraph-artifact-evaluation`](skills/siggraph-artifact-evaluation/SKILL.md) | Pursue the Graphics Replicability Stamp (GRSI/CRCG): deterministic result reproduction, shipped assets, Software Heritage archiving — not the ACM badge scheme. |
| [`siggraph-camera-ready`](skills/siggraph-camera-ready/SKILL.md) | Clear the conditions, complete ACM TOG journal metadata and rights/DOI, finalize the results video and representative image, and permanentize code/data links. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified SIGGRAPH papers across five contribution shapes (1997-2022), with self-check questions and sibling-venue guardrails. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional real-time cloud-rendering paper's teaser, abstract, and introduction rebuilt to the SIGGRAPH arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility tooling, plus the SIGGRAPH-specific checks (results video, deterministic regeneration, assets, timings) the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./SIGGRAPH-Skills
claude plugin install siggraph-skills
```

Or use the files directly: each `skills/siggraph-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a SIGGRAPH paper or should it go to Eurographics/CVPR?" → `siggraph-topic-selection`
- "Audit my draft against the SIGGRAPH technical-papers rules" → `siggraph-submission`
- "We have the reviews — draft the 1000-word rebuttal" → `siggraph-author-response`
- "Get this code ready for the Graphics Replicability Stamp" → `siggraph-artifact-evaluation`

## Pack structure

```text
SIGGRAPH-Skills/
├── .claude-plugin/               # plugin.json + marketplace.json (12 skills declared)
├── README.md                     # this file
├── README.zh-CN.md               # 中文说明
├── LICENSE                       # MIT
├── assets/cover.svg              # pack cover
├── skills/
│   └── siggraph-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md                 # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md            # adapter to shared reproducibility tooling
```

## Suggested use

1. **Before writing** — run `siggraph-topic-selection`; SIGGRAPH overlaps with vision and with the
   graphics symposia, so choosing venue, cycle, and track matters. Skim the exemplars library to see
   what decade-influential SIGGRAPH contributions look like.
2. **While building results** — keep `siggraph-experiments`, `siggraph-supplementary`, and
   `siggraph-reproducibility` beside the work; the results video and faithful baseline comparisons
   cannot be improvised in the final week.
3. **While writing** — `siggraph-writing-style` for the teaser and first-page arc against the worked
   example, `siggraph-related-work` for capability-delta positioning.
4. **Deadline weeks** — complete the submission form (authors lock) before its earlier deadline,
   then `siggraph-submission` end to end on the final PDF, video, and representative image.
5. **After submission** — `siggraph-review-process` to calibrate, `siggraph-author-response` for the
   rebuttal and any conditional-accept revision, then `siggraph-camera-ready` and
   `siggraph-artifact-evaluation` — or the routing table in `siggraph-topic-selection` if the paper
   goes to the next cycle.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- SIGGRAPH 2026 is the **53rd** ACM SIGGRAPH conference: **Los Angeles Convention Center, July
  19-23, 2026**. Technical Papers submission form **15 Jan 2026** (22:00 UTC), complete submission
  **23 Jan 2026** (22:00 UTC); rebuttal **5-12 Mar 2026**; **> 1,120** submissions; published as
  **TOG Vol. 45, Issue 4**.
- SIGGRAPH Asia 2026: **Kuala Lumpur, Malaysia, Dec 1-4, 2026**; Technical Papers Stage-2 full paper
  **12 May 2026** (upload 13 May 2026); the next-cycle target after SIGGRAPH 2026.
- Publication: **ACM Transactions on Graphics**, journal-integrated. Review: single-round,
  historically **single-blind**, on a **6-point scale**, with a **≤ 1000-word text-only rebuttal**,
  a **Technical Papers Committee meeting**, and **conditional acceptance + second-stage**
  verification. Format: **acmart ≥ 2.16**; Conference track **≤ 7 pages** + up to two figures-only
  pages. Portal: **Linklings**.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the TOG Vol. 45 Issue 4 publication, the 7-page Conference-track budget, the 1000-word
   rebuttal, the acmart ≥ 2.16 requirement).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the > 1,120
   submission count; the SIGGRAPH 2025 acceptance figures).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the exact SIGGRAPH 2026
   acceptance count, the full Technical Papers Committee/Chair roster, the precise 2026 blinding and
   generative-AI disclosure wording).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. SIGGRAPH runs **two conferences a year** and
  re-decides its structure per edition — verify which cycle, and its exact **UTC** cutoffs, before
  anything else.
- The conference is run by a rotating **Technical Papers Chair** and **Technical Papers Committee**,
  not a standing editor-in-chief — even though the output is a TOG journal article. Do not conflate
  the conference path with ACM TOG's rolling direct-submission stream (which has its own EiC).
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar method name is not
  proof of a SIGGRAPH placement (many debuted at Eurographics, SGP, SCA, or UIST).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
