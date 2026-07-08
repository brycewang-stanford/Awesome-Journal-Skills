# EMNLP Skills

Twelve agent skills for papers targeting **EMNLP — the Conference on Empirical Methods in
Natural Language Processing**, the ACL-family venue whose identity is empirical: datasets,
benchmarks, evaluation design, error analysis, and measured claims about what language
systems actually do. The pack covers the full arc of an EMNLP cycle: deciding whether a
project is EMNLP-shaped, building contamination-proof and significance-tested evidence,
surviving ACL Rolling Review, playing the commitment step well, and converting acceptance
— Main or Findings — into a correct ACL Anthology record.

Official basis checked on **2026-07-08**: the EMNLP 2026 site and main-conference CFP, the
ACL Rolling Review CFP, dates, and author pages, the Responsible NLP Research checklist,
the ARR May 2026 and Industry Track OpenReview groups, and the ACL Anthology's EMNLP
volumes. The verification environment blocked direct fetches of `2026.emnlp.org` and
`aclrollingreview.org`, so official pages were read via search-engine renderings of exact
URLs and cross-checked against OpenReview and the Anthology; the full trail, including
every item still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes EMNLP different from its siblings

These mechanics, verified for the 2026 cycle, drive most of the advice in the skills —
and most of the surprises for authors arriving from non-ARR venues:

- **There is no EMNLP paper deadline.** Papers enter the ACL Rolling Review May 2026
  cycle (deadline May 25, 2026), get reviewed there, and are *committed* to EMNLP by
  August 2, 2026. The conference only decides; ARR reviews.
- **One cycle, two conferences.** The May 2026 cycle also fed AACL-IJCNLP 2026, with the
  intended venue declared at submission time.
- **The checklist has teeth.** The Responsible NLP checklist is desk-reject enforced for
  incorrect, incomplete, or misleading answers (ARR policy since December 2024), and
  EMNLP 2025 published completed checklists as paper appendices.
- **Two acceptance surfaces.** Committed papers land in the main conference or in
  Findings of EMNLP — a real Anthology-indexed publication, historically without a
  guaranteed presentation slot.
- **A mandatory Limitations section**, uncounted against the 8-page long / 4-page short
  caps, which reviewers audit against the weaknesses they find themselves.
- **No anonymity period, still double-blind.** Preprints may be posted anytime; the
  submitted PDF must stay anonymized.
- **Integrity is named policy.** The 2026 call singles out thinly sliced submissions,
  hallucinated citations, and entirely AI-generated papers (AI writing assistance is
  permitted).
- **Evaluation culture is the venue.** The methodology critiques other fields cite —
  budget-controlled comparisons, statistical power in NLP — were published *at* EMNLP,
  and its reviewers apply them.

## Skills

| Skill | What it does |
| --- | --- |
| [`emnlp-topic-selection`](skills/emnlp-topic-selection/SKILL.md) | Apply the empirical-identity test, match the paper to EMNLP's welcomed genres (including negative results and reproductions), and route among ACL siblings, CoNLL, LREC-COLING, TACL, ML venues, and the industry/demo pipelines. |
| [`emnlp-workflow`](skills/emnlp-workflow/SKILL.md) | Run the ARR-anchored calendar: backward-plan annotation and experiments to May 25, staff the July response window, and pre-draft the 72-hour commit-vs-revise decision. |
| [`emnlp-writing-style`](skills/emnlp-writing-style/SKILL.md) | Enforce claim scoping to tested languages, load-bearing examples with counted frequencies, content-ful Limitations writing, and calibrated hedging. |
| [`emnlp-related-work`](skills/emnlp-related-work/SKILL.md) | Cover the five lineage axes (task, dataset ancestry, methods, evaluation critique, adjacent fields), cite Findings/workshop/TACL correctly, and pass the hallucinated-citation gate. |
| [`emnlp-experiments`](skills/emnlp-experiments/SKILL.md) | Design against the five reviewer probes: baseline fairness, coverage-claim match, contamination, variance, and mechanism — plus prompt-sensitivity grids and designed error analysis. |
| [`emnlp-reproducibility`](skills/emnlp-reproducibility/SKILL.md) | Answer the checklist as a contract, pin model versions and API query dates, log decoding and prompts, and state an honest release level. |
| [`emnlp-supplementary`](skills/emnlp-supplementary/SKILL.md) | Divide material across the four surfaces — content pages, uncounted Limitations, appendices, optional uploads — by review contract, not convenience. |
| [`emnlp-artifact-evaluation`](skills/emnlp-artifact-evaluation/SKILL.md) | Package data, prompts, scoring code, and output dumps for the reviewer's actual inspection order, with data statements and an anonymize-once release plan. |
| [`emnlp-submission`](skills/emnlp-submission/SKILL.md) | Final pre-upload audit: template and page caps, anonymization sweep, checklist consistency, citation resolution, venue declaration, and reciprocal-reviewing obligations. |
| [`emnlp-review-process`](skills/emnlp-review-process/SKILL.md) | Model the two-stage pipeline — ARR scores (soundness / excitement / overall), meta-review, commitment, SAC decision into Main or Findings — and where author leverage lives. |
| [`emnlp-author-response`](skills/emnlp-author-response/SKILL.md) | Triage objections by score axis, add only in-window-addable evidence, and write for the meta-review and the post-commitment record. |
| [`emnlp-camera-ready`](skills/emnlp-camera-ready/SKILL.md) | Execute the three-way merge (reviewed PDF + promised edits + de-anonymization), protect Anthology metadata, restore artifacts publicly, and handle Findings and Budapest logistics. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven official sources with URLs and access dates, the verified 2026-cycle facts, the access-method note, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | The live conference and ARR surfaces plus five author-side verification passes to run before upload. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Six Anthology-verified EMNLP papers (GloVe to power-analysis methodology) across six topic × method lanes, with an anti-misattribution guard for sibling venues. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional multilingual-summarization abstract and introduction rebuilt from architecture-first to phenomenon-first, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit, plus the NLP-specific checks (prompts, snapshots, decoding, annotation materials) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./EMNLP-Skills
claude plugin install emnlp-skills
```

Or use the files directly: each `skills/emnlp-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this benchmark paper EMNLP or LREC-COLING material?" → `emnlp-topic-selection`
- "Audit my draft before the ARR deadline" → `emnlp-submission`
- "Reviews are out — should we commit or resubmit?" → `emnlp-review-process` + `emnlp-author-response`
- "Package the corpus and prompts for release" → `emnlp-artifact-evaluation`

## Pack structure

```text
EMNLP-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── emnlp-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to the shared repro kit
```

## Suggested use

1. **Before writing** — run `emnlp-topic-selection`; if the empirical-identity test
   fails, no amount of polish makes the paper EMNLP-shaped. Read the exemplars library
   to see the bar in accepted form.
2. **While building** — keep `emnlp-experiments` and `emnlp-reproducibility` beside the
   codebase; contamination audits and seed-variance runs are cheap early and impossible
   at deadline.
3. **While writing** — `emnlp-writing-style` for scoping and Limitations,
   `emnlp-supplementary` for the four-surface split, `emnlp-related-work` for lineage
   and the citation-resolution pass.
4. **Deadline week** — `emnlp-submission` end to end, including the mechanical
   anonymization and checklist-consistency checks.
5. **After submission** — `emnlp-review-process` to set expectations,
   `emnlp-author-response` for the July window, then `emnlp-camera-ready` or the
   revise-and-resubmit path depending on the meta-review.

## 2026 anchor facts (historical snapshot, not permanent rules)

- EMNLP 2026: **Budapest, Hungary, October 24-29, 2026**, hybrid.
- Pipeline: ARR May cycle submission **May 25** · author registration form May 27 ·
  reviews due Jul 6 · author discussion **Jul 7-13** · meta-reviews Jul 30 ·
  **commitment Aug 2** · notification Aug 20 · camera-ready Sep 20.
- Format: ACL templates only · long ≤ 8 / short ≤ 4 content pages · unlimited
  references · mandatory uncounted Limitations section.
- Tiers: Main conference + Findings of EMNLP (2025 anchor: 1,810 main, 1,406 Findings,
  194 industry, 78 demo papers).
- Industry Track: direct OpenReview submission, deadline June 16, 2026 AoE.
- Proceedings: ACL Anthology, open access, no author fee.

## Fact discipline

The pack keeps three classes of statement distinguishable:

1. **Verified 2026-cycle facts** — dates and caps traceable to a numbered source in the
   source map (e.g., the May 25 deadline, the August 2 commitment).
2. **Reported facts** — read from renderings or organizers' own posts and labeled as
   such (e.g., the 2026 chair names).
3. **Unverifiable-at-check-time items** — marked 待核实 and phrased as questions (e.g.,
   the camera-ready page bonus, Findings presentation options, demo-track dates).

Any statement presenting class 2 or 3 material as class 1 is a bug; fix it against the
live pages.

## Maintenance notes

- Every date above is a **snapshot of one cycle**; ARR redraws its calendar and
  conference alignments annually, and the conference resets tracks and logistics per
  edition.
- ARR policy (scores, checklist enforcement, form fields) changes midyear and is
  announced on `aclrollingreview.org` — reverify before repeating any reviewing-rule
  claim.
- Chairs rotate per edition; never carry a name forward from this pack without
  rechecking the organization page.
- When adding exemplars, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — an Anthology URL
  alone does not prove the venue.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
