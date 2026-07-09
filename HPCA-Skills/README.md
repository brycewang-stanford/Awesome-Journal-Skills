# HPCA Skills

Twelve agent skills for papers aimed at **HPCA — the IEEE International Symposium
on High-Performance Computer Architecture**, the winter anchor of the computer-
architecture year and the venue that pairs a mid-summer deadline with a
February/March meeting. HPCA is run by the **IEEE Computer Society Technical
Committee on Computer Architecture (TCCA)** — a single-sponsor, IEEE-published
venue, which changes the template, the badging scheme, and the camera-ready
paperwork relative to its ACM-touched siblings. The pack walks the whole arc:
deciding whether a machine, a mechanism, or a measurement is the real
contribution; building evaluation that survives an architecture PC; clearing the
July abstract-then-paper gate on HotCRP; working the single rebuttal/revision
window; and turning acceptance into an IEEE-badged paper presented in the winter
slot.

Official basis checked on **2026-07-09**: the HPCA 2027 call-for-papers and
important-dates pages (`2027.hpca-conf.org`, mirrored on
`conf.researchr.org/home/hpca-2027`), the HPCA 2026 main-conference, artifact-
evaluation, and camera-ready pages (`2026.hpca-conf.org`), the HPCA 2025 call for
papers (`hpca-conf.org/2025/`) for the format and blinding wording, the HPCA 2026
HotCRP portal (`hpca2026.hotcrp.com`), the IEEE-CS TCCA site and the HPCA Test of
Time Award pages (`ieeetcca.org`), and the dblp HPCA series index. The
verification gateway returned HTTP 403 for direct fetches of `hpca-conf.org`,
`2026.hpca-conf.org`, `2027.hpca-conf.org`, `conf.researchr.org`, and
`ieeetcca.org`, so official pages were read through search-engine renderings of
those exact URLs and cross-checked against one another; the full trail — including
everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Where the cycle stands (as of 2026-07-09)

**The HPCA 2027 deadline is imminent.** HPCA 2027, the 33rd edition, is reported
for Salt Lake City, Utah, in March 2027; its paper submission deadline is
**July 24, 2026 (23:59 AoE)**, with abstract-and-conflict registration required
about **one week earlier (~July 17, 2026)**. If you are reading this in early
July 2026, the registration gate is days away, not months. HPCA 2026, the 32nd
edition, was held in **Sydney, Australia, January 31 - February 4, 2026** — so at
check time the previous edition had just concluded and the next deadline is the
live target. Reported acceptance notification for HPCA 2027 is **November 6,
2026**; the rebuttal/revision window between submission and notification was not
published at check time (待核实).

## What makes HPCA distinctive among its siblings

Verified 2025-2027-cycle mechanics that drive the advice in these skills:

- **Single IEEE sponsor, one publisher.** TCCA runs HPCA end to end; papers are
  IEEE-published and use an IEEE template, and artifacts are assessed under
  **IEEE reproducibility badging**, not the ACM Artifact Review and Badging policy
  that ISCA/MICRO/ASPLOS use. There is no ACM/IEEE alternation to track — but
  every ACM-specific habit (badge names, rights forms, DL metadata) is the *wrong*
  habit here.
- **The winter seat with a summer gate.** HPCA deadlines land in **late July**
  and the conference meets in **February or March**. In the four-venue calendar it
  is the last major architecture deadline of the summer and the first conference
  of the next year: ISCA (November deadline → June), MICRO (spring → October),
  ASPLOS (multiple gates), and HPCA (July → February/March) tile the year.
- **Two gates a week apart.** Abstract-and-conflict registration precedes the full
  paper by about a week; the earlier step finalizes the conflict list and seeds
  reviewer assignment, so it is a hard decision point, not a placeholder.
- **11 pages of text, unlimited references — with a reference rule.** The main
  body is capped (11 pages in recent cycles, excluding references), references are
  uncounted, and **every reference must list all its authors** or the paper can be
  rejected. Never abbreviate an author list to save a line.
- **Double-blind with a single rebuttal/revision window.** Names live only in the
  form; unlike ISCA's two review rounds, recent HPCA cycles run one combined
  window in which authors respond and the paper may be revised.
- **Voluntary, post-acceptance artifact evaluation** on a separate HotCRP, earning
  IEEE reproducibility badges printed on the paper — the architecture community's
  trust signal, delivered through the IEEE rather than the ACM pipeline.
- **An Industry track** alongside the main track, for work whose contribution is
  deployed-system evidence rather than a research prototype.
- **Simulation and silicon are both first-class instruments**, so a declared
  fidelity contract (tool, config, workload, sampling, validation) is where an
  HPCA review is won or lost.

## Skills

| Skill | What it does |
| --- | --- |
| [`hpca-topic-selection`](skills/hpca-topic-selection/SKILL.md) | Ask whether the machine, the mechanism, or the measurement is the contribution, route across the HPCA/ISCA/MICRO/ASPLOS year from the winter seat, and weigh the Industry track. |
| [`hpca-workflow`](skills/hpca-workflow/SKILL.md) | Run the year backward from the late-July gate: evidence freeze, the two-step registration, the autumn wait, the rebuttal/revision sprint, and branch plans per outcome. |
| [`hpca-writing-style`](skills/hpca-writing-style/SKILL.md) | Build the paper around one mechanism-to-behavior claim: measured motivation, a checkable mechanism, calibrated numbers, and slack for the revision window. |
| [`hpca-related-work`](skills/hpca-related-work/SKILL.md) | Sweep the HPCA/ISCA/MICRO/ASPLOS record on dblp and IEEE Xplore, write lineage with structural deltas, blind the voice, and never trim an author list from a reference. |
| [`hpca-experiments`](skills/hpca-experiments/SKILL.md) | Declare the fidelity contract — tool, configuration, workloads, sampling, validation — match each claim to its instrument, and tune baselines honestly. |
| [`hpca-reproducibility`](skills/hpca-reproducibility/SKILL.md) | Pin the result chain (simulator commit → config → workload → sampled region → statistics), one manifest per figure, and keep the environment resurrectable for the badge round. |
| [`hpca-supplementary`](skills/hpca-supplementary/SKILL.md) | Triage material across the four destinations HPCA offers: the 11 pages, the anonymized artifact mirror, the staging shelf for the window, and the post-acceptance release. |
| [`hpca-artifact-evaluation`](skills/hpca-artifact-evaluation/SKILL.md) | Scope reproducibility tiers, package simulator- and silicon-heavy workflows for cold-start evaluators, and earn IEEE badges on the separate AE HotCRP. |
| [`hpca-submission`](skills/hpca-submission/SKILL.md) | Final audit: the two-step July gate, the 11-page check, the IEEE template, the blinding rules plus the all-authors reference counter-rule, the AI-use disclosure, and HotCRP completion. |
| [`hpca-review-process`](skills/hpca-review-process/SKILL.md) | Model the double-blind pipeline, what a single rebuttal/revision window means, champion dynamics at the PC meeting, and how to read each outcome. |
| [`hpca-author-response`](skills/hpca-author-response/SKILL.md) | Triage objections by what the window can fix, run a small number of new experiments, write for the committee room, and revise diff-minimally. |
| [`hpca-camera-ready`](skills/hpca-camera-ready/SKILL.md) | Invert every blinding action, apply the IEEE template and rights forms, integrate badges and DOIs, and prepare the winter talk. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and 2026-07-09 access dates; the verified cycle facts; the reported-only items (2027 dates, chair roster); the explicit 待核实 list; the access-method note. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces and five author-side verification passes (calendar, format, blinding, portal, post-acceptance). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Six HPCA Test of Time Award winners as contribution shapes, each with a self-check question and an attribution guard checked against dblp. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional prefetcher abstract and introduction rebuilt to the venue's bar, before → after, move by move. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, plus five architecture-specific checks (simulator pinning, figure traceability, workload licensing, machine state, evaluator budgets) the kit cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./HPCA-Skills
claude plugin install hpca-skills
```

Or use the files directly: each `skills/hpca-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to trigger
it. Typical invocations:

- "Is this cache-coherence paper an HPCA paper or a MICRO paper?" → `hpca-topic-selection`
- "Audit my methodology section before the July deadline" → `hpca-experiments`
- "Reviews are in and the rebuttal/revision window opens Monday" → `hpca-author-response`
- "Package the gem5 artifact for the IEEE badge round" → `hpca-artifact-evaluation`

## Pack structure

```text
HPCA-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── hpca-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Suggested use across a campaign

1. **Early summer (now, for the July gate):** `hpca-topic-selection` with the
   exemplars library open; if fit holds, wire in `hpca-experiments` and
   `hpca-reproducibility` before the infrastructure hardens around bad choices.
2. **The deadline fortnight:** `hpca-writing-style` against the worked example;
   `hpca-related-work`'s dblp/Xplore sweep; `hpca-supplementary` for the
   repo/staging split; then `hpca-submission` end to end — twice, once at the
   registration step and once at the paper step.
3. **Autumn wait:** `hpca-review-process` to set expectations; pre-build the
   objection ledger; run the environment resurrection drill before reviews land.
4. **The window:** `hpca-author-response` for the combined rebuttal/revision
   sprint, revising diff-minimally.
5. **After:** `hpca-camera-ready` + `hpca-artifact-evaluation` on acceptance, or
   the outcome tree's retargeting branch (MICRO, ISCA, ASPLOS) on rejection.

## Cycle anchor facts (historical snapshot, not permanent rules)

- HPCA 2026 = **32nd edition**, Sydney, Australia, **January 31 - February 4,
  2026** (registration July 25, 2025; papers August 1, 2025; HotCRP
  `hpca2026.hotcrp.com`, AE on `hpca2026ae.hotcrp.com`).
- HPCA 2027 = **33rd edition**, reported for Salt Lake City, Utah, March 2027;
  papers **July 24, 2026 (AoE)**, registration ~one week earlier; reported
  notification November 6, 2026.
- Format (2025 cycle): **≤ 11 pages** of text, minimum 10pt font, references
  excluded and unlimited, **each reference must list all authors**; IEEE template;
  HotCRP submission.
- Double-blind: names only in the form; a **single rebuttal/revision window**;
  AI-generated content disclosed in the acknowledgments.
- Artifact evaluation: voluntary, post-acceptance, on a separate HotCRP, earning
  **IEEE reproducibility badges**.

## Fact discipline

Three classes of statement, kept distinguishable throughout the pack:

1. **Verified cycle facts** — dated and traceable to a numbered source in the
   source map (the 11-page rule, the July 24 deadline).
2. **Reported facts** — found only in secondary renderings and labeled as such
   (HPCA 2027's exact March dates, the 2027 chair roster).
3. **Unverified items** — marked 待核实 and phrased as questions to resolve (the
   2027 rebuttal window, the 2027 page limit, AE calendar, acceptance rates).

Treat any statement in the skills that presents class 2 or 3 as class 1 as a bug;
fix it against the live official pages.

## Maintenance notes

- Every date and cap here is a **cycle snapshot**; reopen the current
  `20XX.hpca-conf.org` before deadline-sensitive advice.
- HPCA's single IEEE sponsorship removes ISCA's publisher-alternation trap, but do
  not import ACM badge names, rights forms, or DL conventions — the IEEE pipeline
  differs at camera-ready and at artifact evaluation.
- Chairs and committees rotate per edition; never quote a roster without reopening
  the organization page.
- When adding exemplars, follow the Test-of-Time recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — verify
  through dblp and the TCCA award pages, not a single library's search.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
