# CVPR Skills

Twelve agent skills for papers targeting **CVPR — the IEEE/CVF Conference on Computer
Vision and Pattern Recognition**, computer vision's flagship venue and, by submission
volume, one of the largest peer-reviewed meetings in science. The pack covers the whole
arc of a CVPR campaign: deciding whether a project can survive a 16,000-submission
review machine, building benchmark-grade evidence, clearing the November triple
deadline on OpenReview, writing the one-page rebuttal, honoring author-side reviewer
duties, and landing the paper in CVF open access and IEEE Xplore.

Official basis checked on **2026-07-08**: the CVPR 2026 Author Guidelines, Dates page,
Call for Papers, Reviewer Guidelines, Compute Reporting Form pages, the CVPR 2026
OpenReview group, the `cvpr-org/author-kit` repository, CVF open-access indexes, and
official CVPR program/attendance announcements. Direct fetches of `cvpr.thecvf.com`
and `openaccess.thecvf.com` were blocked (HTTP 403) in the verification environment,
so official pages were read through search-engine renderings of the exact URLs and
cross-checked against OpenReview, dblp, GitHub, and press mirrors; the full trail —
including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

**Cycle status:** CVPR 2026 (Denver, June 3–7, 2026) is the most recent completed
cycle and supplies every verified anchor in this pack. CVPR 2027 (Seattle, reported
around June 20–24, 2027) had published no CFP, deadlines, or policies at check time.

## What makes CVPR unlike its siblings

Verified 2026-cycle mechanics that drive the advice in these skills:

- **Figures count against the cap.** Eight pages *including figures and tables*, with
  free pages for cited references only. Page budgeting is figure design.
- **Three deadlines a week apart.** Abstract registration + valid OpenReview profiles
  for every coauthor (Nov 6, 2025), paper + Compute Reporting Form (Nov 13), then the
  supplement (Nov 20). The first one is the silent killer.
- **Authorship is a reviewing contract.** Submitting authors are enrolled in the
  reviewer pool, and papers by reviewers who miss deadlines or write highly
  irresponsible reviews can be desk-rejected wholesale, at PC discretion.
- **A mandatory Compute Reporting Form** (new in 2026): hardware and verification
  sections required for every submission, with an opt-out path and transparency awards.
- **One page, no attachments.** The rebuttal is a single-page PDF on the official
  template; longer or reformatted responses are not read, and external links are
  banned there as everywhere in review.
- **arXiv is legal, links are not.** Preprinting is explicitly not an anonymity
  violation, but external links that expand content or subvert review are prohibited,
  and papers are media-embargoed until acceptance.
- **Scale as a fact of life.** 2026: 16,092 reviewed submissions, 4,090 acceptances
  (25.42%), ~25,149 reviewers, 909 area chairs, ~12,200 registrants. Publication is
  dual: CVF open access (free, watermarked accepted version) plus IEEE Xplore (version
  of record). No APC; no standing editor — chairs rotate each edition.

## Skills

| Skill | What it does |
| --- | --- |
| [`cvpr-topic-selection`](skills/cvpr-topic-selection/SKILL.md) | Test whether the contribution is a claim about visual data/computation, and route between CVPR, ICCV/ECCV, WACV, 3DV, NeurIPS, SIGGRAPH, and journals. |
| [`cvpr-workflow`](skills/cvpr-workflow/SKILL.md) | Run the campaign calendar from September scope-freeze through the November triple deadline, January rebuttal week, February decisions, and June conference. |
| [`cvpr-writing-style`](skills/cvpr-writing-style/SKILL.md) | Write for the two-pass reviewer: teaser figure, self-contained captions, eight inclusive pages, scoped claims, and responsibility for tool-assisted text. |
| [`cvpr-related-work`](skills/cvpr-related-work/SKILL.md) | Cover the five literature shelves, handle arXiv-speed concurrency, keep self-citations double-blind, and verify that cited "CVPR papers" are CVPR papers. |
| [`cvpr-experiments`](skills/cvpr-experiments/SKILL.md) | Design evidence for the four implicit review questions — works, why, when it fails, what it costs — with matched-baseline fairness and CRF-aligned efficiency reporting. |
| [`cvpr-reproducibility`](skills/cvpr-reproducibility/SKILL.md) | Maintain the recipe ledger, benchmark/split hygiene, seed-honesty at vision compute scale, and CRF consistency. |
| [`cvpr-supplementary`](skills/cvpr-supplementary/SKILL.md) | Split content between the 8-page body and the week-later supplement; package videos as evidence under the no-links rule. |
| [`cvpr-artifact-evaluation`](skills/cvpr-artifact-evaluation/SKILL.md) | Build the sealed anonymous review artifact and the public release, including the dataset-by-camera-ready obligation and license decisions. |
| [`cvpr-submission`](skills/cvpr-submission/SKILL.md) | Final OpenReview audit: profiles, page cap, CRF, anonymity/link sweep, dual-submission attestation, desk-reject triage, 72-hour sequence. |
| [`cvpr-review-process`](skills/cvpr-review-process/SKILL.md) | Model the 16k-scale pipeline — enrollment, reviewer LLM ban, discussion, decision tiers (oral/highlight/poster) — and where author leverage exists. |
| [`cvpr-author-response`](skills/cvpr-author-response/SKILL.md) | Triage multiple reviews into one skimmable page for the AC: factual kills first, mini-tables, calibrated concessions. |
| [`cvpr-camera-ready`](skills/cvpr-camera-ready/SKILL.md) | Deliver the version of record: de-anonymization, live links, dataset release, CVF/IEEE dual publication, tier-specific presentation prep. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Fourteen official sources with access dates, verified 2026-cycle facts, the access-method disclosure, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five metadata-verified CVPR papers across contribution types (ResNet, YOLO, PointNet, ImageNet, Latent Diffusion), plus a do-not-misattribute guard list. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional tracking paper's first page rebuilt for the flip-then-read reviewer, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit, plus CVPR-only checks (CRF consistency, video metadata, link ban). |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./CVPR-Skills
claude plugin install cvpr-skills
```

Or use the files directly: each `skills/cvpr-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to fire. Typical invocations:

- "Is this a CVPR paper or should it go to WACV?" → `cvpr-topic-selection`
- "Audit my draft against the CVPR page and anonymity rules" → `cvpr-submission`
- "Reviews are out — plan the one-page rebuttal" → `cvpr-author-response`
- "What must be public by camera-ready?" → `cvpr-camera-ready`

## Pack structure

```text
CVPR-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── cvpr-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- CVPR 2026: June 3–7, 2026, Colorado Convention Center, Denver (workshops/tutorials
  June 3–4; main conference and expo June 5–7).
- Deadlines: abstract + profiles Nov 6, 2025 · paper + CRF Nov 13 (AoE, fixed) ·
  supplement Nov 20 · reviews to authors Jan 22, 2026 · rebuttal through Jan 29 ·
  discussion Jan 30 – Feb 5 · decisions Feb 20, 2026.
- Format: 8 pages including figures/tables + references-only overflow; official
  author kit at `github.com/cvpr-org/author-kit`; one-page rebuttal template included.
- Scale: 16,092 reviewed submissions; 4,090 accepted (25.42%); ~25,149 reviewers from
  97 countries; 909 ACs; 44,011 authors; ~12,200 registrants. Program trackers report
  141 orals and 578 highlights (treat tier counts as reported).
- Publication: CVF open access + IEEE Xplore; no author-side fee.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — trace to a numbered source in the source map (e.g.,
   the 8-page inclusive cap, the Nov 13 deadline, the CRF's mandatory sections).
2. **Reported facts** — consistent secondary sources, labeled as such (e.g., oral and
   highlight counts, chair names from a university news item, CVPR 2027's Seattle
   dates).
3. **Unverifiable-at-check-time items** — explicitly 待核实 and phrased as questions
   (e.g., supplementary size caps, camera-ready forms and deadline, presentation
   obligations, any author-side AI-disclosure requirement, everything about the 2027
   cycle).

If a skill states class-2/3 material as class 1, treat it as a bug and fix it against
the live official pages.

## Maintenance notes

- Every date, cap, and enforcement rule here is a **2026-cycle snapshot**. CVPR
  policies are rewritten annually by rotating Program Chairs — reopen
  `cvpr.thecvf.com` for the current cycle before deadline-sensitive advice.
- The Compute Reporting Form was a 2026 novelty; assume it evolves (or disappears)
  rather than persists unchanged.
- Reviewer-duty enforcement, LLM policies, and the media embargo hardened recently and
  may harden further; check both Author and Reviewer Guidelines each cycle.
- When adding exemplars, follow the verification recipe at the bottom of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — famous vision
  papers frequently belong to ICCV/ECCV/ICLR, not CVPR.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
