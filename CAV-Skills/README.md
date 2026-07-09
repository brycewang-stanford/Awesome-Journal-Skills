# CAV Skills

Twelve agent skills for papers targeting **CAV — the International Conference on Computer Aided
Verification**, the flagship venue for computer-aided formal analysis of hardware and software
systems. The pack covers the full arc of a CAV campaign: deciding whether a project is CAV-shaped or
belongs at TACAS, FMCAD, VMCAI, a PL venue, or a journal; choosing among CAV's **four submission
categories** (Regular, Short Tool, Short Application, Industrial Experience & Case Study); building a
verification evaluation that survives a reviewer's audit (pinned benchmarks, fair baselines,
checkable proof witnesses); surviving the **two-stage review** with its early-reject filter and
rebuttal; earning **AEC artifact badges**; and delivering the **Springer LNCS open-access**
camera-ready.

Official basis checked on **2026-07-09**: the CAV 2026 Call for Papers and Artifact Evaluation
pages, the SIGPLAN announcement of the 38th CAV, the FLoC 2026 site, the Springer LNCS proceedings
for CAV 2024 and CAV 2025, and dblp. Direct fetches of `i-cav.org` and `sigplan.org` returned 403 in
the verification environment, so official pages were read via search-engine renderings of the exact
URLs and cross-checked against Springer LNCS and dblp; the full trail, including everything still
marked 待核实, is in [`resources/official-source-map.md`](resources/official-source-map.md).

## What makes CAV different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and most
of the mistakes made by authors arriving from an ACM-journal SE venue, a PL conference, or a sibling
formal-methods venue:

- **Springer LNCS, open access — not an ACM journal, not IEEE.** CAV papers are single-column LNCS
  chapters in the `llncs` class, published open access (CAV 2025 = LNCS 15931-15934). Do not carry an
  `acmart` or IEEEtran double-column habit across.
- **Four categories, and a first-class Tool Paper track.** Regular Papers (18 pages) sit alongside
  Short **Tool** Papers, Short **Application** Papers, and **Industrial Experience Reports & Case
  Studies** (10 pages each). A usable verification tool on standard benchmarks is a native CAV
  contribution, not an afterthought.
- **Partial double-anonymity.** Regular and Application papers are **anonymized**; Tool and
  Industrial papers are **not** — because a tool paper that hid its tool would be unreviewable. This
  split is unusual; verify it every cycle.
- **A two-stage review with an early reject.** Stage 1 gives each paper two reviews and rejects the
  weakest early; only survivors get two more reviews and a **rebuttal**. A paper can be rejected
  before the rebuttal exists.
- **Optional, non-conditional artifact evaluation.** A dedicated **AEC** awards **Available /
  Functional / Reusable** badges across a smoke-test and a full-review phase, after notification.
  Acceptance is **not** conditional on it; authors declare artifact intent at submission.
- **Verification-specific evidence culture.** Pinned benchmark revisions (SV-COMP, SMT-COMP, HWMCC,
  VNN-COMP), fair baselines with equal resource limits, timeout-aware cactus/scatter reporting, and
  checkable proof witnesses are community norms the reviewer pool enforces.

## Skills

| Skill | What it does |
| --- | --- |
| [`cav-topic-selection`](skills/cav-topic-selection/SKILL.md) | Route between CAV and its siblings (TACAS, FMCAD, VMCAI, IJCAR, POPL/PLDI, journals) and pick the right category (Regular / Tool / Application / Industrial). |
| [`cav-workflow`](skills/cav-workflow/SKILL.md) | Run the annual cycle backward from the deadline, through the two-stage review, rebuttal, AEC artifact evaluation, and the LNCS camera-ready. |
| [`cav-writing-style`](skills/cav-writing-style/SKILL.md) | Lead with the verification contribution and its guarantee; theorem-and-proof discipline; falsifiable benchmark claims; explicit scope. |
| [`cav-related-work`](skills/cav-related-work/SKILL.md) | Cover the verification lanes, write delta-first positioning, credit tool/benchmark lineages to the right venue, keep self-citations anonymous where required. |
| [`cav-experiments`](skills/cav-experiments/SKILL.md) | Match evidence to claim: standard benchmarks, fair pinned baselines, equal resource limits, timeout-aware reporting, soundness cross-checks and witnesses. |
| [`cav-reproducibility`](skills/cav-reproducibility/SKILL.md) | Pin benchmark revisions, tool versions, limits, seeds, and hardware; ship checkable proof certificates; keep paper and artifact consistent. |
| [`cav-supplementary`](skills/cav-supplementary/SKILL.md) | Split content between the body and the optional appendix/artifact — reviewers need not read the appendix, so decision-critical content stays in the body. |
| [`cav-submission`](skills/cav-submission/SKILL.md) | Final portal audit: category choice, LNCS page limits, the per-category anonymization matrix, artifact intent, desk-risk triage. |
| [`cav-review-process`](skills/cav-review-process/SKILL.md) | Model the pipeline — two-stage review, early reject, rebuttal, optional non-conditional AEC — and where author leverage exists. |
| [`cav-author-response`](skills/cav-author-response/SKILL.md) | Write the stage-2 rebuttal: answer soundness, benchmark-fairness, and novelty objections with verifiable evidence, anonymity intact. |
| [`cav-artifact-evaluation`](skills/cav-artifact-evaluation/SKILL.md) | Package for the AEC: Available / Functional / Reusable, smoke-test + full-review phases, DOI archives, benchmarks, seeds, and witnesses. |
| [`cav-camera-ready`](skills/cav-camera-ready/SKILL.md) | De-anonymize, complete Springer LNCS metadata and open-access rights, permanentize artifact links, and hand off to the AEC badges. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus the SV-COMP/SMT-COMP/SMT-LIB benchmark references and cross-check sources for when the gateway blocks a direct fetch. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five archival-verified CAV papers across contribution shapes (technique, algorithm, SMT-solver tool paper, new domain, framework), with sibling-venue guardrails. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional portfolio-SMT paper's abstract and introduction rebuilt to the CAV arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared replication-package tooling, plus the CAV-specific checks (benchmark provenance, seeds, resource limits, proof witnesses). |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./CAV-Skills
claude plugin install cav-skills
```

Or use the files directly: each `skills/cav-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this a CAV paper or should it go to TACAS/FMCAD?" → `cav-topic-selection`
- "Audit my draft against the CAV Regular-Paper rules" → `cav-submission`
- "We passed stage 1 — plan the rebuttal" → `cav-author-response`
- "Get this solver ready for the AEC badges" → `cav-artifact-evaluation`

## Pack structure

```text
CAV-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── cav-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `cav-topic-selection`; CAV and TACAS overlap, and the category (Regular
   vs. Tool vs. Application) sets your page limit and anonymity rule. Skim the exemplars library to
   see what decade-influential CAV contributions look like.
2. **While building evidence** — keep `cav-experiments` and `cav-reproducibility` beside the study;
   benchmark revisions, baseline versions, and resource limits pinned at run time cannot be
   retrofitted.
3. **While writing** — `cav-writing-style` for the body against the worked example,
   `cav-supplementary` for the body/appendix split, `cav-related-work` for delta-first positioning.
4. **Deadline weeks** — `cav-submission` end to end on the final PDF, the right category, and the
   artifact-intent declaration.
5. **After submission** — `cav-review-process` to calibrate the two-stage filter, `cav-author-response`
   for the stage-2 rebuttal, then `cav-artifact-evaluation` and `cav-camera-ready` — or the routing
   table in `cav-topic-selection` if the decision goes the other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- CAV 2026 is the **38th** edition: **Lisbon, Portugal**, **July 26-29, 2026**, part of **FLoC 2026**
  (the 9th Federated Logic Conference). Program Chairs: **Anthony W. Lin, Eva Darulova, Philipp
  Rümmer**.
- Paper deadline **28 Jan 2026** (AoE); tentative first-round (early-reject) outcome **~4 Mar 2026**;
  author response **30 Mar - 2 Apr 2026**; notification **17 Apr 2026**; artifact registration
  **22 Apr 2026**.
- Categories and limits (LNCS, excluding references + appendix): Regular **18 pp** (anonymized);
  Short Tool **10 pp** (not anonymized); Short Application **10 pp** (anonymized); Industrial
  Experience & Case Study **10 pp** (not anonymized).
- Publication: **Springer LNCS**, **open access**. Review: **two-stage** with rebuttal. Artifacts:
  **AEC**, badges **Available / Functional / Reusable**, invited and non-conditional.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/limits and trace to a numbered source in the source map
   (e.g., the four categories, the two-stage review, the LNCS open-access publication, the three AEC
   badges).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., the exact
   anonymization matrix per category, the tentative 4 Mar first-round date).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the 2026 submission portal
   EasyChair-vs-HotCRP, any separate abstract deadline, the camera-ready date, full PC/AEC rosters).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and limit above is a **cycle snapshot**. CAV re-decides its structure per edition —
  including the category set, the anonymization matrix, and the two-stage-review timing — so verify
  before anything else each year.
- CAV has no standing editor-in-chief and no author-facing per-paper APC; chairs rotate per edition
  and the LNCS proceedings are open access. Confirm the open-access funding arrangement each cycle.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar tool name is not
  proof of a CAV placement (Z3 is TACAS, IC3 is VMCAI, CBMC is TACAS).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
