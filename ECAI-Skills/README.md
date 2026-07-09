# ECAI Skills

Twelve agent skills for papers targeting **ECAI — the European Conference on Artificial
Intelligence**, the flagship general-AI conference of **EurAI (the European Association for
Artificial Intelligence)** and its member national societies. The pack covers the full arc of an
ECAI campaign: deciding whether a project is ECAI-shaped or belongs at IJCAI, AAAI, AAMAS, KR, or a
pure-ML venue (and whether it should go to the main track or the co-located **PAIS** applications
track); building evidence — a proof for a theory contribution, a fair comparison for an empirical
one — that survives a broad reviewer pool; packaging the **double-blind** submission through the
**abstract-then-paper two-deadline** flow into a tight **7-page body**; navigating the
**single-round review with a summary-reject phase and one rebuttal** (no journal-style revision
round); and delivering the **open-access** camera-ready.

Official basis checked on **2026-07-09**: the IJCAI-ECAI 2026 call and Important Dates, the ECAI
2024/2023 standalone calls, the IOS Press **FAIA** proceedings volumes, `eurai.org`, and dblp.
Conference and publisher domains were treated as egress-blocked in the verification environment, so
official pages were read via search-engine renderings of the exact URLs and cross-checked across ≥2
surfaces (IJCAI-ECAI 2026 pages, `ecai2024.eu`, IOS Press FAIA, researchr, EurAI, AIhub, dblp); the
full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> **The defining fact of this cycle:** ECAI 2026 is **not** a standalone edition — it is the
> **joint IJCAI-ECAI 2026** (Bremen, Germany, 15-21 August 2026), following IJCAI's process,
> template, and open-access proceedings. ECAI's *standing* identity — IOS Press FAIA, the `ecai.cls`
> template, and the PAIS co-located track — returns for the next standalone edition. Several skills
> turn on knowing **which regime** the target edition is in.
>
> Name-collision warnings: **FAIA** here is IOS Press's *Frontiers in Artificial Intelligence and
> Applications* book series, **not** the *Federated AI Meeting (FAIM)*; and **ECCAI** is the former
> name of **EurAI** (renamed 2015).

## What makes ECAI different from its siblings

These venue mechanics drive most of the advice in the skills — and most of the mistakes made by
authors arriving from an ML venue, a software-engineering conference, or a journal:

- **A general-AI flagship, governed by EurAI.** ECAI spans symbolic reasoning, KR, planning,
  search, multi-agent systems, ML, and applications — the reviewer pool is **broad**, so a
  contribution must be legible to a general AI audience, not just one niche.
- **Open-access book-series proceedings (IOS Press FAIA).** A standalone ECAI publishes in
  **Frontiers in Artificial Intelligence and Applications** (open access, no APC), using the
  **`ecai.cls`** template — **not** ACM `acmart`, **not** IEEE `IEEEtran`, **not** LNCS. This is a
  genuine formatting differentiator.
- **A tight 7-page body.** The reviewed paper is **7 pages**; references are the only overflow
  (1 page standalone, 2 pages in IJCAI-ECAI 2026). There is no unlimited in-paper appendix.
- **An abstract-then-paper two-deadline flow.** An abstract/registration deadline precedes the PDF
  by about a week; the registered abstract drives reviewer bidding.
- **Single-round, double-blind review with a rebuttal — and no revision round.** A summary-reject
  phase filters early; one author-response window follows; the decision is accept/reject. There is
  **no Major Revision safety net**, so the submitted paper must already be complete.
- **The PAIS applications track.** The co-located **Conference on Prestigious Applications of
  Intelligent Systems** is ECAI's home for credible real-world deployments (standalone editions).
- **No ACM/IEEE artifact badges.** Reproducibility is judged in-band by the same reviewers from the
  paper and its anonymized supplement — there is no separate badge committee or artifact deadline.
- **This cycle is joint with IJCAI.** ECAI 2026 = IJCAI-ECAI 2026 (Bremen), on IJCAI's process,
  `ijcai.sty`, a 7+2 page budget, and IJCAI's own open-access proceedings.

## Skills

| Skill | What it does |
| --- | --- |
| [`ecai-topic-selection`](skills/ecai-topic-selection/SKILL.md) | Route between ECAI and its siblings (IJCAI, AAAI, AAMAS, KR, ML venues) and between the main track and PAIS, using contribution shape, the model-swap test, and the joint-2026 reality. |
| [`ecai-workflow`](skills/ecai-workflow/SKILL.md) | Run the single-round year backward from the paper deadline through the abstract step, summary reject, rebuttal, notification, and open-access camera-ready. |
| [`ecai-writing-style`](skills/ecai-writing-style/SKILL.md) | Build the first-page arc for a general-AI audience and match evidence to claim inside a dense 7-page body. |
| [`ecai-related-work`](skills/ecai-related-work/SKILL.md) | Cover the symbolic/learning/multi-agent/application lanes for a broad pool, write delta-first, keep self-citations double-blind, within a 1-2 page reference budget. |
| [`ecai-experiments`](skills/ecai-experiments/SKILL.md) | Choose proof vs experiment by claim shape, with fair baselines, seeds and spread, honest ablations, and pinned provenance. |
| [`ecai-reproducibility`](skills/ecai-reproducibility/SKILL.md) | Build the in-band story: a complete proof appendix for theory, a seeded/cached package for empirics, and an anonymized supplement. |
| [`ecai-supplementary`](skills/ecai-supplementary/SKILL.md) | Split content by decision-criticality — nothing a reviewer needs to judge the paper may live outside the 7-page body. |
| [`ecai-submission`](skills/ecai-submission/SKILL.md) | Final audit: the abstract-then-paper deadlines, the correct template/publisher regime, the 7-page budget, the double-blind sweep, the per-author cap, desk-risk triage. |
| [`ecai-review-process`](skills/ecai-review-process/SKILL.md) | Model the pipeline — double-blind, summary reject, area chairs, one rebuttal, accept/reject with no revision round — and where author leverage exists. |
| [`ecai-author-response`](skills/ecai-author-response/SKILL.md) | Write the single, short, double-blind rebuttal that corrects factual misreadings and supplies asked-for evidence. |
| [`ecai-artifact-evaluation`](skills/ecai-artifact-evaluation/SKILL.md) | Plan the reproducibility asset without an ACM/IEEE badge track — a proof appendix or a runnable package, judged in-band. |
| [`ecai-camera-ready`](skills/ecai-camera-ready/SKILL.md) | Deliver the open-access camera-ready in the correct regime: IOS Press FAIA (`ecai.cls`) or IJCAI proceedings (`ijcai.sty`). |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Twelve sources with URLs and access dates; verified 2026 facts for both regimes; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces for IJCAI-ECAI 2026 and standalone ECAI, plus cross-check sources and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five web-verified ECAI/PAIS Outstanding-Paper honorees across five contribution shapes, with self-check questions and a sibling-confusion guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional planning-with-learning paper's abstract and introduction rebuilt to the ECAI arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility tooling, plus the ECAI-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ECAI-Skills
claude plugin install ecai-skills
```

Or use the files directly: each `skills/ecai-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an ECAI paper, or should it go to IJCAI/AAAI/AAMAS?" → `ecai-topic-selection`
- "Audit my draft against the ECAI/IJCAI-ECAI 2026 rules" → `ecai-submission`
- "We got into the rebuttal window — plan the author response" → `ecai-author-response`
- "Prepare the open-access FAIA/IJCAI camera-ready" → `ecai-camera-ready`

## Pack structure

```text
ECAI-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── ecai-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared package tooling
```

## Suggested use

1. **Before writing** — run `ecai-topic-selection`; ECAI overlaps IJCAI/AAAI/AAMAS/KR, and the
   main-track-vs-PAIS fork matters. Skim the exemplars to see ECAI's breadth.
2. **While building evidence** — keep `ecai-experiments` and `ecai-reproducibility` beside the
   work; proofs and seeds cannot be retrofitted, and there is no revision round.
3. **While writing** — `ecai-writing-style` for the 7-page arc against the worked example,
   `ecai-supplementary` for the body/supplement split, `ecai-related-work` for delta-first
   positioning.
4. **Deadline weeks** — register the abstract before the earlier deadline, then `ecai-submission`
   end to end on the final PDF, supplement, and template regime.
5. **After submission** — `ecai-review-process` to calibrate, `ecai-author-response` for the single
   rebuttal, then `ecai-camera-ready` and `ecai-artifact-evaluation` — or re-route via
   `ecai-topic-selection` if the decision goes the other way.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- **ECAI 2026 is the joint IJCAI-ECAI 2026:** Bremen, Germany, **15-21 August 2026**; the 35th
  IJCAI held with ECAI under EurAI (with DFKI, the U Bremen Research Alliance, and the German
  Informatics Society GI). Abstract **12 Jan 2026**, paper **19 Jan 2026** (AoE); summary-reject
  notification **4 Mar 2026**; author response **7-10 Apr 2026**; notification **29 Apr 2026**.
  Body **7 pages + 2 reference pages** (optional ethics statement); **`ijcai.sty`**; per-author cap
  **8**; **IJCAI open-access proceedings**. The exact ECAI edition ordinal for 2026 is **待核实**.
- **Standing ECAI identity (standalone, e.g. ECAI 2024, 27th, Santiago de Compostela):** IOS Press
  **FAIA** (ECAI 2024 = Vol. 392), **`ecai.cls`**, **7 pages + 1 reference page**, abstract-then-
  paper two-deadline flow, and the co-located **PAIS** track (PAIS 2024 = 13th).
- Governance: **EurAI**; open access, **no APC**; review is **double-blind, single-round with a
  rebuttal** (no Major Revision).

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g. the IJCAI-ECAI 2026 dates and 7+2 budget, the FAIA Vol. 392 for ECAI 2024, the PAIS
   co-location).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g. exact organizer
   rosters, acceptance figures given as context).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g. the 2026 ECAI edition
   ordinal, ECAI 2025 specifics, whether a joint-year applied track substitutes for PAIS,
   supplement mechanics per edition).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. ECAI re-decides its structure per edition —
  including, critically, **whether it is standalone (FAIA/`ecai.cls`/PAIS) or joint with IJCAI**
  (IJCAI proceedings/`ijcai.sty`) — so confirm the regime before anything else.
- ECAI has no standing editor-in-chief and no APC; organizers rotate per edition under EurAI.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a familiar method or author
  is not proof of an ECAI (rather than IJCAI/AAAI/AAMAS/KR) placement.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
