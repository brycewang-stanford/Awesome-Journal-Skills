# HRI Skills

Twelve agent skills for papers targeting **HRI — the ACM/IEEE International Conference on
Human-Robot Interaction**, the flagship *interdisciplinary* venue where robotics, HCI, psychology,
and design meet around one question: how do people and robots interact? The pack covers the full
arc of an HRI campaign: deciding whether a project is HRI-shaped or belongs at CHI, ICRA/IROS,
RO-MAN, CoRL, or a journal; choosing among HRI's **five full-paper tracks**; designing a
human-subjects study that survives an interdisciplinary reviewer pool (Wizard-of-Oz,
between/within-subjects, power, effect sizes *and* qualitative rigor, validated scales, IRB);
packaging the double-blind **PCS** submission with its mandatory video figure; working the
**two-phase review with a rebuttal**; and delivering the ACM+IEEE dual-published camera-ready.

Official basis checked on **2026-07-09**: the HRI 2026 (Edinburgh) full-papers call, Overview of
Review Process, and Reviewer Guidelines; the alt.HRI, Late-Breaking Reports, video, and Student
Design calls; the ACM Digital Library and IEEE Xplore HRI proceedings; the IEEE-RAS co-sponsorship
listing; dblp; and the HRI 2027 (Santa Clara) announcement. Direct fetches of
`humanrobotinteraction.org`, `dl.acm.org`, and `ieeexplore.ieee.org` returned 403 in the
verification environment, so official pages were read via search-engine renderings of the exact
URLs and cross-checked against ACM DL, IEEE Xplore, dblp, and IEEE-RAS; the full trail, including
everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

> Name-collision warning: **THRI** (ACM *Transactions on Human-Robot Interaction*) and **JHRI**
> (*Journal of Human-Robot Interaction*) are **journals**, not this conference; **HAI** and
> **RO-MAN** are **other conferences**. No fact in this pack derives from them except as an
> explicit venue guard.

## What makes HRI different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills — and
most of the mistakes made by authors arriving from CHI, from a pure-robotics venue (ICRA/IROS/CoRL),
or from a psychology program:

- **Evidence about *people*, not just systems.** HRI's center of gravity is the **human-subjects
  study**. The dominant question is not "does the robot work?" but "what happens when a person
  interacts with it?" — measured with real participants, a defensible design, statistics *with
  effect sizes*, and, increasingly, qualitative rigor. This is the single biggest difference from
  ICRA/IROS/CoRL, whose culture is systems and learning benchmarks.
- **Robot *embodiment* is the point.** Unlike general HCI at CHI, HRI requires a robot — a physical
  or virtual embodied agent — and the interaction with it. A screen-only interface study without a
  robot is a CHI paper; an autonomy result with no human in the loop is an ICRA/IROS paper.
- **Five contribution-typed tracks, one subcommittee each.** Full papers pick exactly one of
  **User Studies · Technical · Design · Theory and Methods · Systems**, and are reviewed by the
  subcommittee matched to that contribution type. Reviewers judge the paper *as* that kind of
  contribution — a design paper is not held to a User Studies bar and vice versa.
- **Two-phase double-blind review with a rebuttal.** Each paper gets a 1AC and 2AC, three external
  reviewers, an **author rebuttal**, an online reviewer discussion, and a **program-committee
  meeting** where decisions are made. The rebuttal is a real lever — it routinely moves scores.
- **The video figure is a first-class artifact.** HRI interaction is temporal and embodied; a
  supplementary **video** that shows the interaction is expected and materially affects how
  reviewers understand the contribution.
- **ACM + IEEE, and the ACM `acmart` template.** HRI is dual-sponsored (ACM SIGCHI / AI SIG and
  IEEE RAS); accepted papers appear in **both** the ACM DL and IEEE Xplore. Full papers use the
  ACM Primary Article Template at **8 pages** (incl. figures, **excl.** references) — not a CHI
  page budget, not an IEEEtran robotics box.
- **Human-subjects ethics is enforced.** Submitting binds you to ACM's Policy on Research Involving
  Human Participants and Subjects; IRB/ethics review, informed consent, and honest reporting are
  community norms the reviewer pool actively checks.

## Skills

| Skill | What it does |
| --- | --- |
| [`hri-topic-selection`](skills/hri-topic-selection/SKILL.md) | Route between HRI and its siblings (CHI, ICRA/IROS, RO-MAN, CoRL, THRI) with the robot-embodiment and human-in-the-loop tests, then pick the right one of the five HRI tracks. |
| [`hri-workflow`](skills/hri-workflow/SKILL.md) | Run the cycle backward from the September abstract deadline through the rebuttal, the PC meeting, camera-ready, and the March conference — with the parallel alt.HRI / LBR / video / Student Design calendars. |
| [`hri-writing-style`](skills/hri-writing-style/SKILL.md) | Build the HRI paper for an interdisciplinary reader: contribution and research questions up front, hypotheses and measures made explicit, the robot described, claims proportional to the study. |
| [`hri-related-work`](skills/hri-related-work/SKILL.md) | Cover HRI's crossing literatures (robotics + HCI + psychology + design), position with a delta, and keep self-citation double-blind. |
| [`hri-experiments`](skills/hri-experiments/SKILL.md) | Design the human-subjects study: between/within-subjects, Wizard-of-Oz done honestly, power and sample size, statistics *with effect sizes*, mixed methods, validated scales, manipulation checks, pre-registration. |
| [`hri-reproducibility`](skills/hri-reproducibility/SKILL.md) | Make an embodied, human-subjects study as reproducible as it can be: WoZ reporting, study materials, robot-behavior specs, pre-registration, and honest limits of replication. |
| [`hri-supplementary`](skills/hri-supplementary/SKILL.md) | Plan the mandatory-in-practice **video figure**, supplementary study instruments, and appendices — split by what a reviewer must see to judge the interaction. |
| [`hri-submission`](skills/hri-submission/SKILL.md) | Final PCS audit: the two-step abstract+paper deadline, track choice, the 8-page acmart anonymous format, the double-blind sweep, the human-subjects acknowledgment, desk-reject triage. |
| [`hri-review-process`](skills/hri-review-process/SKILL.md) | Model the pipeline — desk check, 1AC/2AC + 3 externals, rebuttal, online discussion, PC meeting, per-track subcommittees — and where author leverage exists. |
| [`hri-author-response`](skills/hri-author-response/SKILL.md) | Write the single, high-stakes rebuttal that answers three reviewers and two area chairs, triages study-design and statistics critiques, and promises only what a camera-ready can deliver. |
| [`hri-artifact-evaluation`](skills/hri-artifact-evaluation/SKILL.md) | Package code, robot behaviors, datasets, and study materials for openness and any ACM badges HRI offers — with honest limits on reproducing an embodied human study. |
| [`hri-camera-ready`](skills/hri-camera-ready/SKILL.md) | De-anonymize, complete ACM+IEEE dual-publication metadata (CCS concepts, ORCID, rights form), finalize the video, and pass production checks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; verified 2026 facts; the access-method note; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus cross-check sources for when the gateway blocks a direct fetch, and author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Verified HRI conference papers across contribution shapes, with sibling-venue guards and self-check questions. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional social-robot study's abstract and introduction rebuilt to the HRI arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared study-materials/replication tooling, plus the HRI-specific checks the generic kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./HRI-Skills
claude plugin install hri-skills
```

Or use the files directly: each `skills/hri-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an HRI paper or should it go to CHI/ICRA?" → `hri-topic-selection`
- "Which HRI track should this go to?" → `hri-topic-selection`
- "Audit my draft against the HRI full-paper rules" → `hri-submission`
- "Reviews are in — help me write the rebuttal" → `hri-author-response`
- "Design the user study so it survives HRI review" → `hri-experiments`

## Pack structure

```text
HRI-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── hri-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to shared study-materials tooling
```

## Suggested use

1. **Before designing the study** — run `hri-topic-selection` (HRI, CHI, and the robotics venues
   overlap; the track choice matters too) and keep `hri-experiments` beside the study from day one.
   A study whose design is wrong cannot be rescued in writing.
2. **While running the study** — pre-register where you can, log Wizard-of-Oz behavior, and collect
   validated-scale data with `hri-experiments` and `hri-reproducibility` open.
3. **While writing** — `hri-writing-style` for the interdisciplinary arc against the worked example,
   `hri-supplementary` to plan the video figure, `hri-related-work` for cross-community positioning.
4. **Deadline weeks** — submit the abstract before the earlier cutoff, then `hri-submission` end to
   end on the final anonymized PDF and video.
5. **After submission** — `hri-review-process` to calibrate, `hri-author-response` for the single
   rebuttal, then `hri-camera-ready` and `hri-artifact-evaluation` — or the routing table in
   `hri-topic-selection` if the decision goes the other way.

## 2026/2027-cycle anchor facts (historical snapshot, not permanent rules)

- HRI 2026 is the **21st** edition, theme **"HRI Empowering Society"**: **Edinburgh, Scotland, UK,
  16-19 March 2026**. Full-paper **abstract 22 Sep 2025**, **paper 30 Sep 2025** (AoE);
  **rebuttal ~12 Nov 2025**; decisions Dec 2025; camera-ready ~Jan 2026. As of the 2026-07-09
  access date this edition has already concluded.
- HRI 2027 is the **22nd** edition: **Santa Clara, California, USA, 8-12 March 2027** — the live
  next full-paper target as of 2026-07-09. Reopen its call for the exact dates and budget.
- Full papers: **8 pages** (incl. figures, **excl.** references), **ACM `acmart`** anonymous
  review format, **PCS** portal, **five tracks** (User Studies / Technical / Design / Theory and
  Methods / Systems), **double-blind two-phase** review with a **rebuttal**, published in **ACM DL
  and IEEE Xplore**. Companion tracks: **alt.HRI** (17 Oct 2025), **LBR / video / Student Design**
  (8 Dec 2025).

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026 facts** — carry dates/budgets and trace to a numbered source in the source map
   (e.g., the five tracks, the 8-page budget, the two-phase-with-rebuttal review, PCS).
2. **Reported facts** — read only via secondary renderings and labeled as such (e.g., exact
   acceptance counts, per-track best-paper winners, camera-ready exact date).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 (e.g., the exact `acmart` class
   options for the current cycle, any AI-use disclosure policy, whether a formal artifact-badge
   track runs).

If any statement presents class 2 or 3 material in class 1 voice, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every date and budget above is a **cycle snapshot**. HRI re-decides its structure per edition —
  including track names, the abstract/paper two-step, and the rebuttal format — so verify against
  the current full-papers call before advising.
- HRI has no standing editor-in-chief and rotates chairs per edition. Do not confuse the
  **conference** with the **THRI**/**JHRI** journals.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a famous robot or a familiar
  scale name is not proof of an HRI *conference* placement (many live in THRI, JHRI, IJSR, or CHI).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
