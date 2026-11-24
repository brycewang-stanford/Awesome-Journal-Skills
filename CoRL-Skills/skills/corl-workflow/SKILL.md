---
name: corl-workflow
description: Use when planning a CoRL submission cycle end to end — the late-May abstract and paper deadlines, the summer review window, first-round rejection risk, the August one-page rebuttal and discussion period, autumn decisions, the October PMLR camera-ready, and the November conference — including what to do between milestones.
---

# CoRL Workflow

CoRL runs one cycle per year on a spring-submit / autumn-decide / November-meet
rhythm. This skill turns the CoRL 2026 calendar (re-verified 2026-11-24 against the
corl.org Instruction for Authors key-dates table) into a working plan for each phase.
As of 2026-11-24 the 2026 cycle is complete and CoRL 2027 has not been announced.

## The 2026 cycle as a reference timeline

| Milestone | CoRL 2026 date (AoE) | Status on 2026-11-24 |
|---|---|---|
| OpenReview submission opens | May 8, 2026 | passed |
| Abstract registration (authors frozen) | May 25, 2026 | passed |
| Paper deadline | May 28, 2026 (a Thursday) | passed |
| Supplementary deadline | June 4, 2026 | passed |
| Initial reviews due (reviewers) | July 28, 2026 | passed |
| Reviews released / early rejections | August 4, 2026 | passed |
| One-page PDF rebuttal due | August 11, 2026, 11:59 PM AoE | passed |
| Reviewer–AC discussion window | August 12–19, 2026 | passed |
| Acceptance notification | September 4, 2026 | passed |
| Camera-ready to PMLR pipeline | October 12, 2026, 23:59 AoE | passed |
| Conference (Austin, TX) | main conference November 9–11, workshops November 12, 2026 | held |

Every date above is a single cycle's snapshot. The 2027 cycle will publish its own
timeline at the corl.org year-site; nothing here transfers automatically.

## Phase playbooks

### The submitted-paper quiet period (June–July)

- **Do not update the OpenReview PDF** — the submission is frozen; focus energy on
  experiments you may need for the rebuttal instead.
- Pre-build rebuttal ammunition: the most predictable reviewer asks at CoRL are
  more seeds, more evaluation episodes, a missing robot-learning baseline, and a
  real-robot check for a sim-heavy paper. Run these *before* reviews land; the
  window between reviews and the August 11 rebuttal deadline is days, not weeks.
- Keep the anonymized project site (if any) untouched and unlinked from any
  identity; review is double-anonymous until decisions.
- Decide the fallback venue now (see `corl-topic-selection`), so a first-round
  rejection (August 4 in 2026) converts to a resubmission plan the same week.

### Reviews land (early August; August 4 in 2026)

- Triage against the first-round rejection rule first: in the 2026 process, a paper
  with no score of weak-accept-or-above from any reviewer or the AC is a candidate
  for rejection **without rebuttal**. If you are past that gate, the rebuttal is
  live — switch to `corl-author-response` immediately.
- Map each concern to: (a) already answered in the paper, (b) answerable with a
  prepared experiment, (c) requires concession. One page forces this triage anyway.

### Rebuttal through decision (mid-August – early September; notification September 4 in 2026)

- Submit the one-page PDF by August 11, 11:59 PM AoE; then remain reachable — the
  reviewer–AC discussion (Aug 12–19) can surface follow-ups, and reviewers are
  asked to update scores when a rebuttal warrants it.
- Decisions are finalized in SAC–AC meetings and a final SACs–PCs meeting; there is
  no author-visible activity in that stage, so use September for the camera-ready
  or resubmission branch prep.

### Acceptance branch (September – November)

- Camera-ready: 9-page main text (one page more than submission, explicitly to
  absorb review feedback), `\usepackage[final]{corl_2026}`, appendix merged into
  the same PDF, due October 12, 23:59 AoE — see `corl-camera-ready`.
- Remember that reviews and rebuttals of accepted papers are made public: write the
  camera-ready knowing the exchange will be readable next to it.
- Book Austin early; plan the poster/talk material and the public code release
  (`corl-artifact-evaluation`) in parallel, not sequentially.

## Team calendar template

```yaml
# corl-cycle-plan.yaml — assign an owner and a date to every row
paper_id: ""
phase_now: post-submission          # update as the cycle advances
rebuttal_prep:
  extra_seeds_run:        {owner: , status: }   # started before reviews arrive
  missing_baseline:       {owner: , status: }
  real_robot_spotcheck:   {owner: , status: }
  one_page_template_ready: {owner: , status: }  # LaTeX skeleton compiled
dates_to_watch:
  reviews_released: "2026-08-04 AoE (2026 pattern; reread the live key dates)"
  rebuttal_due: "2026-08-11 23:59 AoE"
  discussion: "2026-08-12..19"
  decision: "2026-09-04 AoE"
  camera_ready: "2026-10-12 23:59 AoE"
fallback:
  venue: ""                          # decided BEFORE decisions arrive
  required_rework: ""
```

## Planning a CoRL 2027 submission from scratch

Working backward from a late-May deadline (the 2026 pattern; CoRL 2027 dates, venue
and call not announced as of 2026-11-24):

1. **T minus 9–12 months** — lock the task suite and data-collection plan; hardware
   time and teleop data are the long poles in robot-learning projects.
2. **T minus 6 months** — baselines running end to end; if a claim needs
   sim-to-real evidence, the real-robot rig must exist by now, not in April.
3. **T minus 3 months** — full evaluation protocol frozen (seeds, episodes, task
   splits — `corl-experiments`); start the paper with the Limitations section
   drafted early, since it is mandatory and counts inside the 8 pages.
4. **T minus 1 month** — supplementary video storyboarded and shot
   (`corl-supplementary`); anonymization sweep of paper, video, and any site.
5. **Deadline week** — abstract registration a few days before the paper deadline
   (2026 spacing: May 25 vs May 28, with the supplement a week later on June 4);
   final OpenReview form checks per
   `corl-submission`.

## Risks specific to this venue's shape

- The rebuttal window is short and fixed; teams that start experiments after
  reviews arrive routinely miss it. Prepare in the quiet period.
- The single annual deadline means a miss costs a full year — hold the routing
  discussion (`corl-topic-selection`) before investing deadline-week effort.
- Hardware fails on deadline schedules: keep one robot-day of slack per claimed
  real-robot table in the final month.

Reconfirm every date at https://www.corl.org/ (2026 cycle) or the 2027 year-site
before acting; this file records the 2026-11-24 state of knowledge.
