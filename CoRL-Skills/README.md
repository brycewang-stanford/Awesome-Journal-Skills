# CoRL Skills

Twelve agent skills for papers targeting **CoRL — the Conference on Robot
Learning**, the annual venue built around one intersection: machine learning as
the engine of robot capability. Founded in 2017 (Mountain View, PMLR v78) and
stewarded by the Robot Learning Foundation, CoRL has grown in under a decade
into the default home for imitation and reinforcement learning on hardware,
sim-to-real transfer, and the vision-language-action model wave — while staying
small and selective compared with the robotics mega-conferences.

Official basis checked on **2026-07-08**: the CoRL 2026 year-site (Austin),
Call for Papers, Instruction for Authors, rebuttal and reviewer instructions,
the CoRL 2026 OpenReview group, and PMLR volumes v78–v305. Direct fetches of
`corl.org` returned 403 in the verification environment, so official pages were
read via search-engine renderings of the exact URLs and cross-checked against
OpenReview, PMLR volume pages, and organizer statements; the full trail —
including everything still marked 待核实 — lives in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Where the 2026 cycle stands right now

The pack is tuned to the live state of the calendar as of 2026-07-08:

- The CoRL 2026 deadlines have **passed** (abstract May 26, paper May 29, 2026).
- Submitted papers are **in review**; reviews land in early August, the
  **one-page PDF rebuttal** is due **August 11, 2026 (AoE)**, and reviewer–AC
  discussion runs **August 12–19**.
- Decisions follow in September (exact date 待核实), camera-ready is due
  **October 12**, and the conference meets in **Austin, Texas, November 9–12**
  (workshops November 9) — the 10th edition of the series.
- Teams starting fresh are planning for **CoRL 2027** (no year-site verified
  yet); the routing and workflow skills cover that branch explicitly.

## What makes CoRL unlike its neighbors

- **The intersection is the identity.** A paper must clear two bars at once:
  learning is the contribution, *and* the claim needs embodiment. Miss the
  first and you belong at ICRA/IROS/RSS; miss the second and you belong at
  NeurIPS/ICLR/ICML. The routing skill turns this into an explicit test.
- **A mandatory, counted Limitations section.** The 2026 instructions require
  it inside the 8-page body — failure modes are part of the reviewed argument,
  not an appendix courtesy.
- **A one-page PDF rebuttal with a gate in front of it.** Papers with no
  weak-accept-or-above score from any reviewer or the AC can be rejected in the
  first round *without* rebuttal; for everyone else, one page, days after
  reviews, is the whole author voice.
- **Public reviews for accepted papers.** The rebuttal exchange becomes part of
  the paper's permanent public record.
- **Video as evidence, then a PMLR pivot.** Review-time supplementary video is
  strongly encouraged (≤ 250 MB, ~3 min), but PMLR accepts no video — so every
  accepted paper ships an external artifact surface at camera-ready.
- **Evaluation-episode culture.** Seeds × episodes × task breadth, measured
  sim-to-real gaps, and baseline fairness across BC/RL/VLA families are the
  reviewer pool's reflexive checks.

## Skills

| Skill | What it does |
| --- | --- |
| [`corl-topic-selection`](skills/corl-topic-selection/SKILL.md) | Run the two-axis test (learning is the contribution / claim needs embodiment) and route between CoRL, ICRA/IROS, RSS, and the ML conferences. |
| [`corl-workflow`](skills/corl-workflow/SKILL.md) | Drive the single annual cycle: May deadlines, the summer quiet period as rebuttal-prep time, the August gauntlet, autumn decisions, November in Austin. |
| [`corl-submission`](skills/corl-submission/SKILL.md) | Audit the OpenReview package: corl_2026 template, 8 pages with Limitations counted, video cap, anonymity for project pages and robot footage, GenAI-policy check. |
| [`corl-review-process`](skills/corl-review-process/SKILL.md) | Model reviewers → AC → SAC → PC meetings, the rubric with weak accept as threshold, the first-round gate, and public reviews on acceptance. |
| [`corl-author-response`](skills/corl-author-response/SKILL.md) | Build the one-page PDF: advocate-first triage, budgeted layout, compact new-evidence tables, tone for a public record. |
| [`corl-camera-ready`](skills/corl-camera-ready/SKILL.md) | Spend the ninth page on review commitments, flip to final mode, merge the appendix, and stand up the external video/code surface PMLR cannot host. |
| [`corl-artifact-evaluation`](skills/corl-artifact-evaluation/SKILL.md) | Package code, data, checkpoints, and benchmarks by declared release tier, anonymous during review and durable after. |
| [`corl-reproducibility`](skills/corl-reproducibility/SKILL.md) | Split the rerunnable (sim/training) half from the auditable (hardware) half: version pins, manifests, episode logs, honest availability statements. |
| [`corl-supplementary`](skills/corl-supplementary/SKILL.md) | Place content across appendix / supplementary upload / external hosting; make the video evidentiary — uncut runs, labeled speeds, failures shown. |
| [`corl-writing-style`](skills/corl-writing-style/SKILL.md) | Serve the dual ML+robotics audience: page-1 contract, calibrated claims with scale attached, and a Limitations section written as an asset. |
| [`corl-related-work`](skills/corl-related-work/SKILL.md) | Cover the three lanes plus the VLA wave and concurrent arXiv; PMLR citation hygiene including the conference-vs-publication year offset. |
| [`corl-experiments`](skills/corl-experiments/SKILL.md) | Design two-layer randomness protocols (training seeds × evaluation episodes), generalization splits, fair cross-family baselines, and measured transfer gaps. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and access dates, the access-method note, verified vs reported facts, and the 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five verification passes to run each cycle. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Six PMLR-verified exemplars (Chen in-hand RL, SayCan, RT-2, OpenVLA, VideoMimic, AnyPlace) with misattribution guards and a verification recipe. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional force-aware imitation paper's abstract/introduction, before → after, mapped to the pack's standards. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference repro kit plus the robot-specific checks it cannot make. |

## Installation and use

This directory is a self-contained Claude Code plugin with its own marketplace
manifest:

```bash
# From a clone of the repository
claude plugin marketplace add ./CoRL-Skills
claude plugin install corl-skills
```

Or use the files directly — each `skills/corl-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to fire.
Typical invocations:

- "Is this VLA fine-tuning project a CoRL paper or an ICLR paper?" → `corl-topic-selection`
- "Reviews arrive next month — what should we be doing now?" → `corl-workflow`
- "Reviews are in, two borderlines and a weak accept" → `corl-author-response`
- "How many seeds and episodes do we actually need?" → `corl-experiments`
- "We got in — what changes for camera-ready?" → `corl-camera-ready`

## Pack structure

```text
CoRL-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── corl-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # shared repro-kit adapter
```

## 2026 anchor facts (one cycle's snapshot, not permanent rules)

- CoRL 2026: 10th edition, JW Marriott, Austin, Texas, **November 9–12, 2026**.
- Deadlines: abstract **May 26**, paper **May 29, 2026**, on OpenReview
  (`robot-learning.org/CoRL/2026/Conference`), double-anonymous.
- Format: 8-page main text **including a mandatory Limitations section**;
  acknowledgments/references/appendix uncounted; supplementary video ≤ 250 MB.
- Process: first-round rejection possible without rebuttal; one-page PDF
  rebuttal due **Aug 11**; discussion **Aug 12–19**; decisions September
  (待核实); reviews of accepted papers made public.
- Camera-ready: 9-page main text, `\usepackage[final]{corl_2026}`, due
  **Oct 12, 23:59 AoE**; videos hosted externally (PMLR takes none).
- Proceedings: PMLR, open access. Verified anchors: v78 = 2017, v164 = 2021,
  v205 = 2022, v229 = 2023, v270 = 2024, v305 = 2025.
- 2026 organizers (reported): General Chairs Yuke Zhu and Peter Stone; Program
  Chairs Ani Majumdar, Dieter Fox, Georgia Chalvatzaki. Roles rotate annually.

## Fact discipline

Statements in this pack fall into three classes, kept distinguishable on
purpose:

1. **Verified 2026-cycle facts** — carry a date or cap and trace to a numbered
   source in the source map (the May 29 deadline, the 250 MB video cap).
2. **Reported facts** — read only through secondary or rendering-level
   provenance and labeled as such (the numeric score scale, the chair list).
3. **待核实 items** — unresolved at check time and phrased as questions, never
   as facts (decision date, GenAI policy text, 2026 PMLR volume number,
   registration rules).

If any skill statement presents class 2 or 3 material as class 1, treat it as a
bug and fix it against the live pages.

## Maintenance notes

- Every date and cap is a **2026 snapshot**; CoRL's rotating chairs re-issue
  rules annually — reopen the live year-site before deadline-sensitive advice.
- The page-accounting rule (what the 8 pages include) and the rebuttal format
  have both changed across CoRL's short history; never carry them forward.
- Expect corl.org to block automated fetches; use the search-rendering +
  cross-check method documented in the source map, and record access dates.
- When adding exemplars, follow the recipe in
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a PMLR
  URL alone does not prove the venue, and RSS/CoRL misattribution is endemic.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
