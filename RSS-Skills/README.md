# RSS Skills

Twelve agent skills for papers targeting **RSS — Robotics: Science and Systems**, the
single-track, deliberately selective robotics conference run under the RSS Foundation.
The pack covers the full arc: testing whether a project carries a genuine scientific
claim about robotics (and not only a working system), building hardware evidence that
can survive a science-minded audience, navigating the OpenReview double-blind pipeline
and its invited one-page rebuttal, and landing the final paper in the free open-access
proceedings at roboticsproceedings.org.

Official basis checked on **2026-07-08**: the RSS 2026 (Sydney) conference site, Call
for Papers, and review-process pages; the RSS 2026 OpenReview venue group; the
roboticsproceedings.org volume archive; the dblp RSS index; and the RSS Foundation
award pages. Direct fetches of `roboticsconference.org` returned HTTP 403 through the
verification environment's gateway, so official pages were read via search-engine
renderings of the exact URLs and cross-checked against roboticsproceedings.org, dblp,
and OpenReview. The full trail — including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Where the cycle stands (as of the check date)

RSS 2026 — the 22nd edition — runs **July 13-17, 2026 in Sydney, Australia** (UTS and
the International Convention Centre): conference week begins five days after this
pack's verification date. The 2026 submission funnel is closed (abstracts January 23,
papers January 30, supplements February 6, invited rebuttals April 3, decisions
April 27 — all AoE). The pack therefore serves two live audiences: **accepted authors
in presentation and artifact-release mode**, and **teams planning RSS 2027**, whose
site, dates, and deadlines were not yet posted at check time.

## What makes RSS itself

These verified venue mechanics drive the advice in the skills:

- **One track, one audience.** Every accepted paper is presented to the whole
  conference. The decision question at the Area Chair meeting is not just "is this
  sound?" but "must the field hear this?" — which is why the pack pushes so hard on
  a single falsifiable claim.
- **A science bar, not a demo bar.** The venue's name is a thesis. "We built it and
  it works" needs an extractable insight — a mechanism isolated, a bottleneck
  measured, a property proved — before it is RSS-shaped.
- **Earned rebuttal.** The 2026 review was two-stage: only papers above a first-round
  threshold were invited to submit a one-page rebuttal, read primarily by the Area
  Chair. Below the threshold, the submission was the only word the authors got —
  so the writing must pre-answer objections.
- **A ceiling that rewards brevity.** At most 8 pages excluding references in 2026,
  explicitly framed as a ceiling and not a floor — and the CFP notes reviewers favor
  papers that are not unnecessarily long. (The 2021-2022 editions ran with *no* page
  limit; the format demonstrably moves between cycles.)
- **Free proceedings, no author fee.** Every RSS paper since 2005 is open-access at
  roboticsproceedings.org with a `10.15607/RSS.*` DOI. There is no APC; the cost
  model is registration.
- **Links wait for the camera-ready.** The 2026 CFP welcomed external links only in
  the final version — the anonymous submission argues entirely inside its PDF and
  supplement.
- **A late-January deadline in a crowded year.** RSS sits at the start of the annual
  ICRA/IROS/RSS/CoRL rotation; choosing it is a calendar decision as much as a fit
  decision, and the pack teaches that calendar from RSS's seat.

## Skills

| Skill | What it does |
| --- | --- |
| [`rss-topic-selection`](skills/rss-topic-selection/SKILL.md) | Apply the one question RSS asks, run the claim/audience/compression probes, and route toward ICRA, IROS, CoRL, HRI, WAFR, T-RO, or IJRR when the answer says so. |
| [`rss-workflow`](skills/rss-workflow/SKILL.md) | Plan against the real calendar: the January cascade, conditional April rebuttal, late-April decisions, July conference week, and the sibling-venue rotation. |
| [`rss-submission`](skills/rss-submission/SKILL.md) | Audit the three-deadline cascade, the 8-page ceiling, PDF self-containment, the no-links rule, and the robotics-specific double-blind sweep. |
| [`rss-writing-style`](skills/rss-writing-style/SKILL.md) | Build the claim-first page, size every sentence to the evidence, pre-answer objections, and treat brevity as the scored trait it is here. |
| [`rss-related-work`](skills/rss-related-work/SKILL.md) | Cover the five literature lanes, contrast instead of catalogue, handle arXiv concurrency, and defuse the platform-chain anonymity trap. |
| [`rss-experiments`](skills/rss-experiments/SKILL.md) | Derive experimental conditions from the claim's logical form: trial protocols, mechanism ablations, sim/real ledger discipline, failure attribution. |
| [`rss-reproducibility`](skills/rss-reproducibility/SKILL.md) | Declare a replication tier per claim, write the platform ledger, ship log-backed trial claims, and plan the open release the venue's culture expects. |
| [`rss-supplementary`](skills/rss-supplementary/SKILL.md) | Use the one-week-later supplement deadline well: video cut as evidence, footage anonymization, archive hygiene, self-containment litmus test. |
| [`rss-artifact-evaluation`](skills/rss-artifact-evaluation/SKILL.md) | Package the six-layer robotics artifact stack in its anonymous review state and its public release state, with honest closure declarations. |
| [`rss-review-process`](skills/rss-review-process/SKILL.md) | Model the two-stage pipeline, the threshold gate, the AC-meeting decision, and what single-track selectivity does to reviewer expectations. |
| [`rss-author-response`](skills/rss-author-response/SKILL.md) | Draft the invited one-page rebuttal as a memo to the Area Chair — budgeted, coordinate-anchored, concession-calibrated — or triage forward if none came. |
| [`rss-camera-ready`](skills/rss-camera-ready/SKILL.md) | De-anonymize, restore platform attribution, add the newly-permitted links, verify roboticsproceedings.org metadata, and prepare the single-track talk. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten primary sources with URLs and access dates, the 403 access-method note, verified 2026-cycle facts, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (edition, format, anonymity, review mechanics, post-decision). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five proceedings-verified RSS papers (2005-2023), four of them Test of Time recipients, each with a self-check question and a misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional bimanual-cloth paper rewritten from demo report to falsifiable claim, before → after, mapped to the skills. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit plus the five robotics-specific checks it cannot perform. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./RSS-Skills
claude plugin install rss-skills
```

Or use the files directly: each `skills/rss-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to fire. Typical invocations:

- "Is this project actually an RSS paper or an ICRA paper?" → `rss-topic-selection`
- "Audit us against the January deadlines" → `rss-submission`
- "We were invited to submit a rebuttal — one page, due Friday" → `rss-author-response`
- "Cut the supplementary video" → `rss-supplementary`
- "We got in — what changes for the final version?" → `rss-camera-ready`

## Pack structure

```text
RSS-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json (12 skills declared)
├── README.md                # this file
├── README.zh-CN.md          # 中文说明
├── LICENSE                  # MIT
├── assets/cover.svg         # pack cover
├── skills/
│   └── rss-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md            # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md       # adapter to the shared repro kit
```

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- RSS 2026: 22nd edition, **July 13-17, 2026, Sydney, Australia** (University of
  Technology Sydney + International Convention Centre); single-track program;
  early-bird registration through May 11, 2026.
- Deadlines (all AoE): abstract **January 23**, full paper **January 30**,
  supplementary **February 6**, invited rebuttal **April 3**, decisions **April 27**,
  all 2026. Camera-ready deadline: never publicly surfaced — 待核实 from the
  acceptance email.
- Format: **8 pages maximum excluding references** (ceiling, not floor); PDF-only
  main file; self-contained body; appendices to the supplement; external links only
  at camera-ready; no separate demo-paper category.
- Review: **double-blind on OpenReview** (`roboticsfoundation.org/RSS/2026/Conference`
  group); two-stage with a threshold-gated one-page rebuttal read by the Area Chair;
  decisions from an AC meeting. Program Chair 2026: Matei Ciocarlie (Columbia).
- Publication: free open-access at **roboticsproceedings.org**, DOIs
  `10.15607/RSS.<year>.<vol>.<paper>`; no author fee anywhere in the pipeline.
- Award lineage used for exemplars: Test of Time (Square Root SAM; SARSOP; the
  RRT*/PRM* optimality paper; deep-learned grasp detection) and the Early Career
  Award / Spotlight series.
- RSS 2027: nothing posted at check time — site, dates, deadline all 待核实.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — carry dates and trace to a numbered row in the
   source map (the deadline cascade, the page ceiling, the rebuttal design).
2. **Patterns** — labeled as such where used for planning (the late-January-deadline
   / July-conference rhythm assumed for 2027).
3. **Unverified items** — marked 待核实 and phrased as questions (camera-ready date,
   in-person requirements, supplement size caps, acceptance rates, AI-use policy).

If any skill presents class 2 or 3 material as class 1, treat it as a bug and repair
it against the live official pages.

## Maintenance notes

- The 8-page ceiling is a **cycle policy, not a tradition** — RSS 2021 and 2022 ran
  with no page limit at all. Reopen the CFP every cycle before quoting format rules.
- The two-stage rebuttal design was verified for 2026 only; confirm it survives
  before advising authors to bank on (or write off) a response opportunity.
- `roboticsconference.org` rebinds to the newest edition each cycle: a URL that
  showed 2026 content will silently start showing 2027 content. Check the banner.
- Committees rotate per edition under the RSS Foundation; carry no names forward.
- New exemplars must be verified against a roboticsproceedings.org volume page (plus
  dblp) — arXiv pages and project sites do not establish that a paper is an RSS paper.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
