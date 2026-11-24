# RSS Skills

Twelve agent skills for papers targeting **RSS — Robotics: Science and Systems**, the
single-track, deliberately selective robotics conference run under the RSS Foundation.
The pack covers the full arc: testing whether a project carries a genuine scientific
claim about robotics (and not only a working system), building hardware evidence that
can survive a science-minded audience, navigating the RSS 2027 two-stage shepherding
pipeline on OpenReview (Extended Abstract → invited rebuttal → Extension Charter → final
paper), and landing the final paper in the free open-access proceedings at
roboticsproceedings.org.

Official basis first checked on **2026-07-08** (RSS 2026, read via search-engine
renderings because `roboticsconference.org` returned HTTP 403) and **re-verified and
moved to RSS 2027 on 2026-11-24** by direct fetch of the RSS 2027 site, Call for Papers,
Author FAQ, Reviewer Guidelines and committee pages, plus the archived RSS 2026 call;
the roboticsproceedings.org volume archive, the dblp RSS index and the RSS Foundation
award pages complete the basis. The full trail — including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Where the cycle stands (as of 2026-11-24)

RSS 2027 — the 23rd edition — runs **July 6–11, 2027 in Athens, Greece** (Megaron Athens
International Conference Centre), and its call is out. **The first deadline is close:
the Stage 1 Extended Abstract is due December 4, 2026** (11:59pm AoE). Then: Stage 1
decision (reject or invitation to rebuttal) February 5, 2027; rebuttal February 12;
Stage 2 decision (reject or Extension Charter) February 26; final paper April 16;
supplementary material April 19; acceptance notification April 30; camera-ready May 14,
2027. RSS 2026 (Sydney, July 13-17, 2026) has met and is kept as labelled history.

## What makes RSS itself

These verified venue mechanics drive the advice in the skills:

- **One track, one audience.** Every accepted paper is presented to the whole
  conference. The decision question at the Area Chair meeting is not just "is this
  sound?" but "must the field hear this?" — which is why the pack pushes so hard on
  a single falsifiable claim.
- **A science bar, not a demo bar.** The venue's name is a thesis. "We built it and
  it works" needs an extractable insight — a mechanism isolated, a bottleneck
  measured, a property proved — before it is RSS-shaped.
- **Shepherding, not one-shot gatekeeping (new in 2027).** RSS 2027 replaced the single
  deadline + rebuttal with two stages. Stage 1 is a **6-page Extended Abstract (5 pages
  of content + 1 page of references)** — a semi-complete paper whose problem,
  hypotheses and methodology are complete while experiments may be preliminary;
  nothing beyond the 6 pages is reviewed. Invited papers get a Metareview and a
  rebuttal, then an **Extension Charter** listing the experiments or proofs the final
  paper must deliver. Stage 2 is the **final paper, at most 8 pages excluding
  references**, judged on whether the Charter was executed — and well-founded negative
  results are not grounds for rejection.
- **Hypothesis-scored review.** Reviewers score *Value of Hypothesis* and *Feasibility of
  Conclusion* (each 1-4) and propose Charter items; reviews of accepted papers are
  published **with the reviewers' and chairs' names**.
- **A ceiling that rewards brevity.** The page limits are cycle policy: 8 pages
  excluding references in 2026 (after 2021, 2022 and 2025 ran with no hard limit), and
  5 + 1 at Stage 1 / 8 + references at Stage 2 in 2027.
- **LLMs allowed, fabricated citations fatal.** RSS 2027 permits LLM use by authors and
  reviewers, encourages (but does not require) disclosure, and desk-rejects papers with
  hallucinated references after automated checks.
- **Free proceedings, no author fee.** Every RSS paper since 2005 is open-access at
  roboticsproceedings.org with a `10.15607/RSS.*` DOI. There is no APC; the cost
  model is registration.
- **Links wait for the camera-ready.** The 2027 CFP bars external links in the blinded
  submission (anonymous ones are discouraged too); supplementary material (zip, 100MB)
  is accepted only at Stage 2.
- **An early-December first deadline in a crowded year.** RSS 2027 moved its entry point
  from late January to December 4, ahead of the ICRA/IROS/CoRL rotation; choosing it is a
  calendar decision as much as a fit decision, and the pack teaches that calendar from
  RSS's seat.

## Skills

| Skill | What it does |
| --- | --- |
| [`rss-topic-selection`](skills/rss-topic-selection/SKILL.md) | Apply the one question RSS asks, run the claim/audience/compression probes, and route toward ICRA, IROS, CoRL, HRI, WAFR, T-RO, or IJRR when the answer says so. |
| [`rss-workflow`](skills/rss-workflow/SKILL.md) | Plan against the real 2027 calendar: the December Extended Abstract, February rebuttal and Extension Charter, the April final paper, July conference week, and the sibling-venue rotation. |
| [`rss-submission`](skills/rss-submission/SKILL.md) | Audit the Stage 1 Extended Abstract (5 + 1 pages) and the Stage 2 final paper (8 pages + references), PDF self-containment, the no-links rule, and the robotics-specific double-blind sweep. |
| [`rss-writing-style`](skills/rss-writing-style/SKILL.md) | Build the claim-first page, size every sentence to the evidence, pre-answer objections, and treat brevity as the scored trait it is here. |
| [`rss-related-work`](skills/rss-related-work/SKILL.md) | Cover the five literature lanes, contrast instead of catalogue, handle arXiv concurrency, and defuse the platform-chain anonymity trap. |
| [`rss-experiments`](skills/rss-experiments/SKILL.md) | Derive experimental conditions from the claim's logical form: trial protocols, mechanism ablations, sim/real ledger discipline, failure attribution. |
| [`rss-reproducibility`](skills/rss-reproducibility/SKILL.md) | Declare a replication tier per claim, write the platform ledger, ship log-backed trial claims, and plan the open release the venue's culture expects. |
| [`rss-supplementary`](skills/rss-supplementary/SKILL.md) | Use the Stage 2 supplement (zip, 100MB, three days after the final paper) well: video cut as evidence, footage anonymization, archive hygiene, self-containment litmus test. |
| [`rss-artifact-evaluation`](skills/rss-artifact-evaluation/SKILL.md) | Package the six-layer robotics artifact stack in its anonymous review state and its public release state, with honest closure declarations. |
| [`rss-review-process`](skills/rss-review-process/SKILL.md) | Model the two-stage shepherding pipeline, the Stage 1 cascading filter, the Extension Charter, signed reviews, and what single-track selectivity does to reviewer expectations. |
| [`rss-author-response`](skills/rss-author-response/SKILL.md) | Draft the invited rebuttal to the Metareview as a memo to the Area Chair that shapes the Extension Charter — budgeted, coordinate-anchored, concession-calibrated — or triage forward if none came. |
| [`rss-camera-ready`](skills/rss-camera-ready/SKILL.md) | De-anonymize, restore platform attribution, add the newly-permitted links, verify roboticsproceedings.org metadata, and prepare the single-track talk. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Thirteen primary sources with URLs and access dates, the access-method note, verified RSS 2027 facts, the RSS 2026 history, the explicit 待核实 list, and the machine-readable rules block. |
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
- "Audit our Extended Abstract against the December 4 deadline" → `rss-submission`
- "We were invited to rebut the Metareview — due February 12" → `rss-author-response`
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

## RSS 2027 anchor facts (edition snapshot, not permanent rules)

- RSS 2027: 23rd edition, **July 6–11, 2027, Athens, Greece** (Megaron Athens
  International Conference Centre); single-track program.
- Deadlines (all 11:59pm AoE): Extended Abstract **December 4, 2026** · Stage 1
  decision **February 5, 2027** · rebuttal **February 12** · Stage 2 decision /
  Extension Charter **February 26** · final paper **April 16** · supplementary
  **April 19** · notification **April 30** · camera-ready **May 14, 2027**.
- Format: Stage 1 **6 pages = 5 content + 1 references**, appendices inside the 5,
  no supplement; Stage 2 **8 pages excluding references**; supplement zip ≤ 100MB at
  Stage 2 only; PDF only, unmodified template, no page numbers; no external links in
  the blinded paper.
- Review: **double-blind on OpenReview** (`roboticsfoundation.org/RSS/2027/Conference`);
  two-stage shepherding with a Metareview, rebuttal and Extension Charter; signed
  reviews published for accepted papers. Program Chair 2027: Amanda Prorok
  (Cambridge); General Chair: Matei Ciocarlie (Columbia, Program Chair in 2026).
- AI: LLM use permitted, disclosure encouraged, hallucinated citations desk-rejected.
- History: RSS 2026 (Sydney, July 13-17, 2026) used a single January deadline (abstract
  January 23, paper January 30), 8 pages excluding references, and a threshold-gated
  one-page rebuttal (April 3) before April 27 decisions.
- Publication: free open-access at **roboticsproceedings.org**, DOIs
  `10.15607/RSS.<year>.<vol>.<paper>`; no author fee anywhere in the pipeline.
- Award lineage used for exemplars: Test of Time (Square Root SAM; SARSOP; the
  RRT*/PRM* optimality paper; deep-learned grasp detection) and the Early Career
  Award / Spotlight series.
- RSS 2028: nothing posted as of 2026-11-24.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified RSS 2027 facts** — carry dates and trace to a numbered row in the
   source map (the two-stage calendar, the 5 + 1 and 8-page limits, the Extension
   Charter, signed reviews, the LLM policy).
2. **Patterns** — labeled as such where used for planning (e.g., the July-conference
   rhythm assumed for 2028).
3. **Unverified items** — marked 待核实 and phrased as questions (rebuttal format,
   in-person requirements, registration fees, acceptance rates).

If any skill presents class 2 or 3 material as class 1, treat it as a bug and repair
it against the live official pages.

## Maintenance notes

- The page ceiling is a **cycle policy, not a tradition** — RSS 2021, 2022 and 2025 ran
  with no page limit at all. Reopen the CFP every cycle before quoting format rules.
- The two-stage shepherding design is new in 2027 (2026 used a threshold-gated
  one-page rebuttal); confirm it survives before advising authors for 2028.
- `roboticsconference.org` rebinds to the newest edition each cycle: it switched from
  2026 to 2027 content between July and November 2026, and the 2026 pages moved under
  `/2026/`. Check the banner.
- Committees rotate per edition under the RSS Foundation; carry no names forward.
- New exemplars must be verified against a roboticsproceedings.org volume page (plus
  dblp) — arXiv pages and project sites do not establish that a paper is an RSS paper.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
