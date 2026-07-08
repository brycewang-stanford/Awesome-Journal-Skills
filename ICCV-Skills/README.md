# ICCV Skills

Twelve agent skills for papers targeting **ICCV — the IEEE/CVF International
Conference on Computer Vision** — the vision field's biennial international
flagship, held only in odd years. The pack is organized around the consequence of
that cadence: an ICCV decision is a two-year commitment, so these skills treat
venue choice, the early-March single deadline, the May rebuttal week, reviewer-duty
compliance, and the retreat routes to CVPR and ECCV as one connected campaign
rather than a sequence of forms.

Official basis checked on **2026-07-08**: the ICCV 2025 Call for Papers, Dates,
Author Guidelines, Reviewer Guidelines, the 2025 **Changes** page (which announced
that cycle's process redesign), the Submission Checklist, the ICCV 2025 OpenReview
group, CVF open access, the CVF upcoming-conferences list, and the PAMI-TC awards
page. Direct fetches of `iccv.thecvf.com` and `tc.computer.org` were blocked
(HTTP 403) in the verification environment, so official pages were read through
search-engine renderings of the exact URLs and cross-checked against OpenReview,
dblp, CVF, and official conference-account announcements. The full trail — sources,
access dates, reported-only facts, and everything marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

**Cycle status:** ICCV 2025 (Honolulu, October 19–23, 2025) is the most recent
completed edition and supplies every verified anchor here. ICCV 2027 is announced
for **Hong Kong, October 2–8, 2027**, but had published no CFP, deadlines, or
policies at check time — all 2027 process details are 待核实.

## The facts this pack is built around

Verified 2025-cycle mechanics (each traced in the source map):

- **Biennial, odd years.** Miss the deadline and the next ICCV is two years out;
  the rational fallback ladder runs through CVPR (annual, November) and ECCV
  (even-year spring). Several skills treat that triangle explicitly.
- **One upload event.** Since 2025, the paper *and* supplementary material are due
  together (March 7, 2025, 11:59pm **HST** — note the timezone), after a March 3
  registration. The traditional trailing supplement week is gone.
- **Every author reviews.** Not just "qualifying" authors — all of them, unless
  exempt as new to or outside the vision community, with a 25-submission cap per
  author.
- **Enforcement with receipts.** The 2025 chairs desk-rejected 29 papers because
  25 of their authors reviewed irresponsibly (one-sentence, LLM-written, or
  off-target reviews) — 12 of those papers would otherwise have been accepted.
- **Scale.** 11,239 valid submissions, 2,699 accepted, 24% acceptance; Highlights
  and orals are further tiers (counts reported, not officially re-verified).
- **One page in May.** Reviews out May 9, rebuttal May 10–16, one-page PDF on the
  official template, no links, no attachments; decisions in late June, conference
  in mid-October — a four-month runway this pack tells you to spend on artifact
  release and international travel logistics.
- **Publication.** CVF open access (free) plus IEEE Xplore (version of record); no
  author-side fee; chairs rotate per edition. ICCV's best-paper award is the
  **Marr Prize** — its lineage (Mask R-CNN 2017, Swin 2021, ControlNet 2023,
  BrickGPT 2025) doubles as a taste signal in the topic-selection skill.
- **A 2025 novelty:** the **Findings** workshop took technically sound papers
  rejected from or withdrawn during ICCV 2025 review — a post-decision outlet
  factored into the rejection playbook.

## Skills

| Skill | What it does |
| --- | --- |
| [`iccv-topic-selection`](skills/iccv-topic-selection/SKILL.md) | Decide whether the project should pay the biennial option cost: calendar-first routing across CVPR/ECCV/WACV/journals, the Marr Prize lineage as a fit signal, five-question interrogation. |
| [`iccv-workflow`](skills/iccv-workflow/SKILL.md) | Run the odd-year campaign: the autumn CVPR-vs-ICCV fork, March deadlines, May rebuttal, June decision, visa-aware October conference plan, and the fallback ladder. |
| [`iccv-writing-style`](skills/iccv-writing-style/SKILL.md) | Write for the international generalist reviewer: mechanism-first prose, the inclusive-8-page space market, claims sized for a one-page defense, skim-order structure. |
| [`iccv-related-work`](skills/iccv-related-work/SKILL.md) | Position across the intervening CVPR/ECCV cycles, handle March-deadline concurrency, keep self-reference and the do-not-cite-your-repo rule clean, verify venue attribution. |
| [`iccv-experiments`](skills/iccv-experiments/SKILL.md) | Design evidence under a fixed date: benchmark-drift audit, fairness ledger for the foundation-model era, isolating ablations, run sequencing with falsifiers first. |
| [`iccv-reproducibility`](skills/iccv-reproducibility/SKILL.md) | Meet the two-year checkability test without a mandated form: recipe ledgers, foundation-model protocol pinning, variance honesty, volunteered compute disclosure. |
| [`iccv-supplementary`](skills/iccv-supplementary/SKILL.md) | Produce the supplement as a parallel workstream under the same-day deadline: placement rules, archive-specific anonymity leaks, seven-minute navigability. |
| [`iccv-artifact-evaluation`](skills/iccv-artifact-evaluation/SKILL.md) | Package review-time code under the sealed-archive rules, then spend the June-to-October runway on a release engineered to the venue's infrastructure standard. |
| [`iccv-submission`](skills/iccv-submission/SKILL.md) | Final audit: registration and profiles, the three caps (pages, per-author submissions, rebuttal length), anonymity and embargo sweeps, 48-hour triage. |
| [`iccv-review-process`](skills/iccv-review-process/SKILL.md) | Model the pipeline and its teeth: every-author reviewing, the 2025 enforcement outcome, the reviewer LLM ban, decision tiers, and the Findings option after rejection. |
| [`iccv-author-response`](skills/iccv-author-response/SKILL.md) | Turn the May 10–16 window into a schedule and the single page into an argument budget: what fits, what to concede, what to escalate confidentially. |
| [`iccv-camera-ready`](skills/iccv-camera-ready/SKILL.md) | Deliver the CVF + IEEE Xplore record: de-anonymization as a rewrite pass, rebuttal-promise diffing, arXiv synchronization, and presenting abroad in October. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Fourteen sources with access dates, verified vs reported vs 待核实 classification, and the access-method disclosure. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces and five author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Seven venue-verified ICCV papers as an era time-lapse (SIFT → Mask R-CNN → CycleGAN → Swin → ControlNet → SAM → BrickGPT), with the big-three misattribution guard list. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional 3D-reconstruction paper's first page, before → after, with a transfer checklist. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit plus five ICCV-only checks. |

## Installation and use

This directory is a self-contained Claude Code plugin with its own marketplace
manifest:

```bash
# From a clone of the repository
claude plugin marketplace add ./ICCV-Skills
claude plugin install iccv-skills
```

Or use the skills as plain instruction files — each
`skills/iccv-*/SKILL.md` declares in its frontmatter when it should fire. Typical
prompts:

- "Should we hold this for ICCV 2027 or submit to CVPR in November?" →
  `iccv-topic-selection` + `iccv-workflow`
- "Audit the submission before the March deadline" → `iccv-submission`
- "Reviews landed, rebuttal due in a week" → `iccv-author-response`
- "We got in — what happens between June and Honolulu/Hong Kong?" →
  `iccv-camera-ready` + `iccv-artifact-evaluation`

## Pack structure

```text
ICCV-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover (biennial-orbit motif)
├── skills/
│   └── iccv-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## Fact discipline

Statements in this pack come in three grades, kept distinguishable everywhere:

1. **Verified 2025-cycle facts** — traceable to a numbered source-map entry (the
   unified March 7 deadline and its HST clock, the 8-page inclusive cap, the
   every-author-reviews rule, the 29-paper enforcement outcome, the 24% rate).
2. **Reported facts** — consistent secondary sources, labeled as reported (the
   263 Highlights, the ~0.56% oral share, the exact late-June decision date, the
   2027 chair rosters as listed by CVF).
3. **待核实 items** — phrased as open questions (2025 camera-ready mechanics,
   supplement size caps, presentation obligations, and the *entire* 2027 process).

A skill stating grade-2/3 material as grade-1 is a bug; fix it against the live
pages.

## Maintenance notes

- The next real update moment is when **iccv.thecvf.com/Conferences/2027** goes
  live: deadline chain and timezone, page caps, supplement mechanics, reviewer-duty
  wording, rebuttal format, and the Findings workshop's recurrence all need
  re-verification then.
- The 2025 process redesign (single deadline, universal reviewer duty, submission
  caps, strict enforcement) was announced on a dedicated Changes page; look for the
  2027 equivalent first — it is the highest-density source for what moved.
- Tier statistics and enforcement numbers are cycle events, not constants; requote
  only with the new cycle's own figures.
- Exemplar additions must pass the venue-verification recipe at the bottom of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); the big three
  are the most misattributed venues in vision bibliographies.

## License

MIT — see [`LICENSE`](LICENSE). 中文说明见 [`README.zh-CN.md`](README.zh-CN.md)。
