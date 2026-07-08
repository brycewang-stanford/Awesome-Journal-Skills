# ICRA Skills

Twelve agent skills for papers targeting **ICRA — the IEEE International Conference
on Robotics and Automation**, the flagship conference of the IEEE Robotics and
Automation Society (RAS) and the largest annual robotics deadline. The pack covers
the whole arc: deciding whether a project is ICRA-shaped (and whether it should
travel as a direct conference paper or as an **RA-L journal paper with conference
presentation**), building real-robot evidence, producing the video attachment,
surviving a review pipeline with **no rebuttal**, and landing the camera-ready in
IEEE Xplore.

Official basis checked on **2026-07-08**: the ICRA 2026 (Vienna) call-for-papers and
final-submission pages, the announced ICRA 2027 (Seoul) year-site, IEEE RAS series
and RA-L author pages, and PaperPlaza. Direct fetches of the `ieee-icra.org`
year-sites returned 403 in the verification environment, so official pages were read
via search-engine renderings of the exact URLs and cross-checked against IEEE RAS
pages and IEEE Xplore records; the full trail — including everything still marked
待核实 — is in [`resources/official-source-map.md`](resources/official-source-map.md).

## What makes ICRA different from its siblings

These venue mechanics, verified for the 2026 cycle, drive the advice in the skills
— and most of the mistakes made by authors arriving from ML conferences:

- **Two roads to the same podium.** A direct ICRA submission (one September
  deadline) and an RA-L journal paper transferred for conference presentation
  (rolling deadline, revisions possible, journal publication) both end on an ICRA
  stage. Choosing between them is a strategic decision this pack teaches
  explicitly.
- **No rebuttal.** In the classic ICRA pipeline, reviews arrive together with the
  January decision. Objections must be pre-answered in the paper, and the video
  attachment functions as the asynchronous rebuttal.
- **The video is a first-class artifact.** Up to 180 seconds and 20 MB, uploaded
  only in fixed windows (one of which closes *after* the paper deadline), watched
  by reviewers before they read — with its own review-form field.
- **Tight page geometry, no appendix.** The 2026 cycle allowed 6 content pages
  plus 2 reference-only pages at submission, and 8 pages *total including
  references* at camera-ready. There is no supplementary PDF; everything
  load-bearing lives in the body.
- **Anonymity just flipped.** ICRA 2025 was single-blind; ICRA 2026 switched to
  double-anonymous. Habits like "our previous platform [7]" and lab-branded video
  footage became desk risks overnight.
- **Hardware evidence culture.** Reviewers are calibrated to trial counts,
  success criteria, failure taxonomies, and sim-to-real deltas; a polished demo
  without them reads as an advertisement.
- **Pacific-time deadline.** 23:59 PT in the 2026 cycle, not AoE — a five-hour
  trap for ML-conference-calibrated teams.

## Skills

| Skill | What it does |
| --- | --- |
| [`icra-topic-selection`](skills/icra-topic-selection/SKILL.md) | Run the embodiment test, weigh direct ICRA vs the RA-L pathway, and route against IROS, RSS, CoRL, T-RO, HRI, and CASE. |
| [`icra-workflow`](skills/icra-workflow/SKILL.md) | Plan backward from the September deadline through video windows, winter review silence, January notification, March camera-ready, and the conference. |
| [`icra-submission`](skills/icra-submission/SKILL.md) | Final PaperPlaza audit: 6+2 page geometry, template compliance, double-anonymous sweep, video specs and windows, dual-submission traps. |
| [`icra-writing-style`](skills/icra-writing-style/SKILL.md) | Task-first openings, figure-first structure, demo-speak-to-numbers rewrites, cross-stack notation, and the 6-page budget. |
| [`icra-related-work`](skills/icra-related-work/SKILL.md) | Cover the five lanes robotics reviewers check, handle concurrent arXiv work, and keep self-citations anonymous. |
| [`icra-experiments`](skills/icra-experiments/SKILL.md) | Match claim altitude to the evidence ladder; trials, resets, baseline fairness, sim-to-real deltas, failure taxonomies, small-n statistics. |
| [`icra-reproducibility`](skills/icra-reproducibility/SKILL.md) | Split rerunnable from auditable claims; hardware specification ledgers, rosbag logging discipline, honest availability statements. |
| [`icra-supplementary`](skills/icra-supplementary/SKILL.md) | Treat the 180-second video as evidence: storyboard, uncut takes, labeled speeds, shown failures, 20 MB encoding, footage anonymization. |
| [`icra-artifact-evaluation`](skills/icra-artifact-evaluation/SKILL.md) | Package the six-layer robotics artifact stack for the five-minute skeptic, with review-time and acceptance-time states. |
| [`icra-review-process`](skills/icra-review-process/SKILL.md) | Model the RAS Conference Editorial Board pipeline, the no-rebuttal consequences, and the contrast with RA-L journal review. |
| [`icra-author-response`](skills/icra-author-response/SKILL.md) | Respond in the channels that exist: camera-ready revision, RA-L response letters, and reject-to-IROS/RA-L resubmission memos. |
| [`icra-camera-ready`](skills/icra-camera-ready/SKILL.md) | The 8-page-total final limit, de-anonymization, IEEE copyright (eCF), registration obligations, final video, IEEE Xplore. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten primary sources with URLs and access dates, secondary-source labeling, verified 2026-cycle facts, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (geometry, anonymity, video, evidence, timing). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five DOI-verified ICRA papers (2000-2018) across five topic lanes, with self-check questions and a venue-misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional slip-regrasping abstract and introduction rebuilt from demo-speak to the ICRA arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit plus the five robotics-specific checks it cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ICRA-Skills
claude plugin install icra-skills
```

Or use the files directly: each `skills/icra-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to fire.
Typical invocations:

- "Should this go to ICRA in September or to RA-L now?" → `icra-topic-selection`
- "Audit my draft against the ICRA submission rules" → `icra-submission`
- "Storyboard the video attachment" → `icra-supplementary`
- "We got the January reviews — what now?" → `icra-author-response`

## Pack structure

```text
ICRA-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── icra-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Suggested use

1. **Before committing a cycle** — run `icra-topic-selection`; if the embodiment
   test fails or the clock favors RA-L, the pack just changed your plan for the
   better. Skim the exemplars library for your topic lane.
2. **During the experimental campaign** — keep `icra-experiments` and
   `icra-reproducibility` beside the robot; bank video footage from every session
   per `icra-supplementary`, because deadline-week filming produces worse evidence
   and worse anonymity.
3. **While writing** — `icra-writing-style` for the body, `icra-related-work` for
   positioning, the worked example as the before/after reference.
4. **Deadline fortnight** — `icra-workflow` for sequencing, then the full
   `icra-submission` audit including the video-window dates and the Pacific-time
   conversion.
5. **After the decision** — `icra-review-process` to read the packet,
   `icra-author-response` for the channel that applies, then `icra-camera-ready`
   or the resubmission lattice toward IROS/RA-L.

## 2026-cycle anchor facts (historical snapshot, not permanent rules)

- ICRA 2026: **June 1-5, 2026, Messe Wien, Vienna, Austria**, theme "Robots for
  all," 8,000+ attendees.
- Live target: **ICRA 2027, May 24-28, 2027, COEX, Seoul, Republic of Korea**;
  registration opens early February 2027; **paper deadline not yet posted** at
  check time (recent pattern: mid-September of the prior year).
- 2026 submission: PaperPlaza, deadline September 15, 2025, 23:59 Pacific;
  6 content pages + 2 reference-only pages; double-anonymous.
- Video attachment: ≤ 180 s, ≤ 20 MB, mpeg/mp4/mpg, windows Aug 5-Sep 9 and
  Sep 17-22, 2025.
- Decision January 31, 2026 and camera-ready March 6, 2026 (secondary-sourced;
  reconfirm); final papers 8 pages total including references; IEEE Xplore
  publication after eCF copyright transfer.
- RA-L pathway: rolling submission, 6 pages including references (+2 at USD
  175/page), ~3-month first decision, conference presentation via transfer within
  270 days of acceptance.

## Fact discipline

The pack keeps three classes of statement distinguishable:

1. **Verified 2026-cycle facts** — carry dates/caps and trace to a numbered row in
   the source map (e.g., the 6+2 page split, the video specs).
2. **Reported facts** — found only in secondary renderings or aggregators and
   labeled as such (e.g., the January 31 notification date).
3. **Unverifiable-at-check-time items** — marked 待核实 and phrased as questions
   (e.g., the ICRA 2027 deadline, whether double-anonymity persists, registration
   fees, any AI-use policy).

If a skill ever presents class 2 or 3 material as class 1, treat it as a bug and
fix it against the live official pages.

## Maintenance notes

- Every number above is a **2026-cycle snapshot**. The 2025→2026 single-blind →
  double-anonymous flip is proof that ICRA rules genuinely change between cycles;
  reopen `<year>.ieee-icra.org` before deadline-sensitive advice.
- ICRA has no standing editor-in-chief; organizing committees and the RAS
  Conference Editorial Board assignments rotate per edition. Do not carry
  editor-continuity assumptions over from journal packs.
- Do not conflate conference rules with RA-L rules; they share PaperPlaza, not
  policy.
- When adding exemplars, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — DOIs must
  resolve to ICRA proceedings entries; community folklore about where a classic
  paper appeared is not verification.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
