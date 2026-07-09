# IROS Skills

Twelve agent skills for papers targeting **IROS — the IEEE/RSJ International Conference
on Intelligent Robots and Systems**, the fall robotics mega-venue co-sponsored by the
IEEE Robotics and Automation Society (RAS) and the Robotics Society of Japan (RSJ). The
pack covers the whole arc: deciding whether a project is IROS-shaped (versus ICRA, RSS,
CoRL, or the RA-L journal route), building real-robot evidence, cutting the 60-second
video attachment, surviving a review pipeline with **no rebuttal**, and landing the
camera-ready in IEEE Xplore.

Official basis checked on **2026-07-09**: the IROS 2026 (Pittsburgh) call-for-papers and
important-dates pages, the IEEE RAS co-sponsored-conference and RA-L pages, and
PaperPlaza. Direct fetches of `2026.ieee-iros.org` returned HTTP 403 in the verification
environment, so official pages were read via search-engine renderings of the exact URLs
and cross-checked against IEEE RAS pages, PaperPlaza, and independent conference mirrors;
the full trail — including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes IROS different from its siblings

These venue mechanics, verified for the 2026 cycle, drive the advice in the skills — and
most of the mistakes made by authors arriving from ML conferences or from ICRA:

- **The IEEE/RSJ joint identity.** IROS is co-sponsored by IEEE RAS *and* the Robotics
  Society of Japan, established 1988 — a genuinely bi-organizational conference that
  rotates its host region yearly. That is why it is "IEEE/RSJ," and why committees and
  rules reset every edition.
- **The fall slot.** IROS is the **autumn** IEEE-RAS mega-venue, the seasonal counterpart
  to ICRA's spring. Teaching the robotics calendar from IROS's seat: a spring paper
  deadline, a summer of review silence, a mid-June notification, a July camera-ready, and
  a late-September/October conference.
- **A tighter video envelope.** The optional video attachment is **60 seconds and 10 MB**
  in the 2026 cycle — half of ICRA's 180 s / 20 MB — with its **own deadline** a few days
  after the paper. A video cut for ICRA must be re-edited, not just re-uploaded.
- **References count inside the page budget, and there is no supplementary PDF.**
  Everything load-bearing lives in the body; an argument that needs an appendix is
  mis-sized for IROS.
- **Double-anonymous in 2026.** IROS carried a long single-blind tradition, but the 2026
  cycle presents as double-anonymous — author names out of the PDF, full list in
  PaperPlaza metadata. Habits like "our prior rover [9]" and lab-branded video footage
  became review-time leaks.
- **No rebuttal.** Reviews traditionally arrive *with* the decision. Objections must be
  pre-answered in the paper and the video; the video is the only asynchronous rebuttal a
  reviewer gets.
- **The RA-L pathway changed.** IROS 2026 has **no combined RA-L+IROS submission option**;
  instead, already-published RA-L (and T-RO, T-ASE, RAM) papers are eligible for
  presentation via a transfer window. This is a departure from older cycles and from how
  ICRA is often described.
- **Embodied-evidence culture.** Reviewers are calibrated to hardware ledgers, trial
  counts, reset procedures, failure taxonomies, and sim-to-real deltas; a polished demo
  without them reads as an advertisement.

## Live-cycle snapshot (2026-07-09)

As of the access date, IROS 2026 is **past submission and mid-cycle**: the March 2 paper
deadline and March 5 video deadline have closed, **notifications landed June 16, 2026**,
and the **live obligation is the camera-ready and registration** — the final-paper
deadline is **July 10, 2026**, the day after this pack's access date. IROS 2027 is
reported (not first-party verified) for Florence, Italy in late September/early October
2027. Plan accordingly: if you are reading this for a 2027 submission, you are on the
*next* spring deadline, not this one.

## Skills

| Skill | What it does |
| --- | --- |
| [`iros-topic-selection`](skills/iros-topic-selection/SKILL.md) | Identify the integrated-system contribution and its embodiment constraint; route against ICRA, RSS, CoRL, RA-L, T-RO, HRI, and CASE from IROS's fall seat. |
| [`iros-workflow`](skills/iros-workflow/SKILL.md) | Plan backward from the spring deadline through the separate video cutoff, the summer review silence, the June notification, and the July camera-ready. |
| [`iros-submission`](skills/iros-submission/SKILL.md) | Final PaperPlaza audit: references-counted page budget, IEEE template, double-anonymous sweep, the 60 s / 10 MB video, and dual-submission traps. |
| [`iros-writing-style`](skills/iros-writing-style/SKILL.md) | Task-first openings, system-diagram-as-hero-figure, demo-speak-to-numbers rewrites, and the no-supplement body discipline. |
| [`iros-related-work`](skills/iros-related-work/SKILL.md) | Cover the robotics-systems lanes, handle concurrent arXiv work, and keep self-citations anonymous under double-anonymous review. |
| [`iros-experiments`](skills/iros-experiments/SKILL.md) | The claim-to-evidence ladder: trials, resets, baseline fairness on matched hardware, sim-to-real deltas, failure taxonomies, small-n statistics. |
| [`iros-reproducibility`](skills/iros-reproducibility/SKILL.md) | Split rerunnable from auditable claims; hardware ledgers, calibration disclosure, log capture, honest availability statements. |
| [`iros-supplementary`](skills/iros-supplementary/SKILL.md) | Treat the 60-second video as evidence: storyboard, uncut takes, labeled failures, honest speed, 10 MB encoding, footage anonymization. |
| [`iros-artifact-evaluation`](skills/iros-artifact-evaluation/SKILL.md) | Package the robotics artifact stack for the skeptic — hardware, logs, configs, code, data — with review-time and acceptance-time states. |
| [`iros-review-process`](skills/iros-review-process/SKILL.md) | Model the PaperPlaza Associate-Editor pipeline, the no-rebuttal consequences, and how the video steers reviewers. |
| [`iros-author-response`](skills/iros-author-response/SKILL.md) | Respond in the channels that exist: pre-answering in the paper, camera-ready edits, RA-L response letters, and reject-to-next-venue memos. |
| [`iros-camera-ready`](skills/iros-camera-ready/SKILL.md) | De-anonymization, meta-review integration, IEEE eCF copyright, the July deadline, registration, and IEEE Xplore publication. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eight primary sources with URLs and access dates, secondary-source labeling, verified 2026-cycle facts, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes (geometry, anonymity, video, evidence, timing). |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five DOI-verified IROS papers (2012-2020) across five system lanes, with self-check questions and a venue-misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional spring-loaded-door mobile-manipulation abstract rebuilt from demo-speak to the IROS arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit plus the five robotics-specific checks it cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./IROS-Skills
claude plugin install iros-skills
```

Or use the files directly: each `skills/iros-*/SKILL.md` is a standalone instruction file
whose frontmatter `description` tells an agent when to fire. Typical invocations:

- "Is this an IROS paper or a CoRL paper?" → `iros-topic-selection`
- "Audit my draft against the IROS submission rules" → `iros-submission`
- "Storyboard my 60-second video" → `iros-supplementary`
- "We were accepted — what's the camera-ready checklist?" → `iros-camera-ready`

## Pack structure

```text
IROS-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── iros-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Suggested use

1. **Before committing a cycle** — run `iros-topic-selection`; if the system does not
   meet an embodiment constraint, or the season favors ICRA, the pack just changed your
   plan for the better. Skim the exemplars library for your system lane.
2. **During the experimental campaign** — keep `iros-experiments` and
   `iros-reproducibility` beside the robot, and bank video footage from every session per
   `iros-supplementary`, because deadline-week filming produces worse evidence and worse
   anonymity.
3. **While writing** — `iros-writing-style` for the body, `iros-related-work` for
   positioning, the worked example as the before/after reference.
4. **Deadline fortnight** — `iros-workflow` for sequencing, then the full `iros-submission`
   audit including the separate video deadline and the references-inside page budget.
5. **After the decision** — `iros-review-process` to read the packet, `iros-author-response`
   for the channel that applies (with no rebuttal, that is usually camera-ready), then
   `iros-camera-ready` or the re-route toward ICRA / CoRL / RA-L.

## Fact discipline

The pack keeps three classes of statement distinguishable:

1. **Verified 2026-cycle facts** — carry dates/caps and trace to a numbered row in the
   source map (e.g., the 60 s / 10 MB video, the July 10 camera-ready).
2. **Reported facts** — found only in secondary renderings or aggregators and labeled as
   such (e.g., the June 16 notification and the IROS 2027 Florence venue).
3. **Unverifiable-at-check-time items** — marked 待核实 and phrased as questions (e.g., the
   exact 2026 page limit, whether double-anonymity persists, whether any rebuttal exists,
   the general/program-chair roster, registration fees).

If a skill ever presents class 2 or 3 material as class 1, treat it as a bug and fix it
against the live official pages.

## Maintenance notes

- Every number above is a **2026-cycle snapshot**. IROS rules genuinely change between
  cycles — the single-blind-to-double-anonymous posture and the removal of the combined
  RA-L option are proof; reopen `<year>.ieee-iros.org` before deadline-sensitive advice.
- IROS has no standing editor-in-chief; organizing committees and the PaperPlaza
  Associate-Editor/Editor assignments rotate per edition, and co-sponsorship alternates
  regions. Do not carry editor-continuity assumptions over from journal packs.
- Do not conflate IROS with ICRA: they share PaperPlaza and IEEE Xplore, not their
  calendars, video specs, or per-cycle policies.
- When adding exemplars, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — DOIs must resolve
  to IROS proceedings entries; a `10.1109/ICRA.*` DOI is not IROS.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
