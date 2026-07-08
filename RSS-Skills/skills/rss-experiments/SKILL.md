---
name: rss-experiments
description: Use when designing or auditing the experimental campaign for an RSS (Robotics: Science and Systems) paper — hypothesis-shaped robot experiments, trial protocols and per-condition counts, mechanism-isolating ablations, simulation-versus-hardware evidence splits, and failure attribution that supports a scientific claim rather than a demo reel.
---

# RSS Experiments

Design experiments that *test the paper's claim*, not experiments that showcase the
system. At RSS the evaluation section is where the scientific claim either becomes
falsifiable or is exposed as marketing.

## Start from the claim, derive the conditions

Write the claim, then derive what evidence its logical form demands:

| Claim form | Evidence the form demands |
|---|---|
| "X causes the improvement" | Ablation removing only X; everything else frozen |
| "the gain transfers" | Held-out tasks/objects/platforms named *before* running |
| "method M has property P" | The condition where P would break, deliberately tested |
| "T is the bottleneck" | Failure attribution showing T dominates the failure mass |
| "faster/cheaper at equal quality" | Matched-quality comparison, not best-vs-default |

An experiment matrix that cannot be traced back to a claim row is footage, not
evidence — cut it or move it to the supplement.

## Hardware trial protocol

- **Pre-register internally:** success criterion, reset procedure, object/task
  distribution, and stopping rule written down before the campaign. Post-hoc criteria
  are how demo bias enters honest labs.
- **Per-condition counts in every table.** "n = 25 per object, 6 objects" is
  auditable; "extensive trials" is not.
- **Report the denominator.** All attempts count — aborted runs, resets, operator
  interventions. A human silently rescuing the robot between trials is part of the
  system and must appear in the protocol.
- **Small-n honesty:** hardware budgets cap trials, so use interval estimates suited
  to small samples and let the language match their width. Twenty trials support "in
  our setting"; they do not support "reliably in general."

## Simulation and hardware: split the ledger

- Label every number sim or real; never average across the boundary.
- Simulation earns its place by *scale* (sweeps, distributions) or *danger* (failure
  regimes hardware cannot safely visit); hardware earns the claim's headline.
- If the claim mentions the physical world, at least one decisive result must be
  physical. A sim-only paper must scope its claim to simulation explicitly.
- When sim and real disagree, that gap is a finding — report it, do not tune it away
  silently.

## Failure attribution, the RSS signature move

A distribution over failure causes is often more scientifically valuable than the
success rate above it. Build one:

1. Define 4-6 mutually exclusive failure categories before the campaign (perception,
   planning, timing, slip, hardware fault, other).
2. Label every failed trial at collection time, from logs — retrospective labeling
   from memory drifts optimistic.
3. Report the distribution per condition; a method that shifts failure mass between
   categories is telling you *how* it works.

## Trial-budget arithmetic (do this before the campaign)

Hardware time is the binding constraint, so budget it explicitly:

```text
conditions:      2 methods x 3 environments x (1 ablation + 1 transfer) = 10
trials/condition: 25            -> 250 attempts
minutes/attempt (incl. reset):   6 -> 25 robot-hours
overhead (faults, recalibration, re-runs): x1.5 -> ~38 robot-hours
robot access: 4 h/day           -> ~10 working days, before any surprise
```

If the arithmetic says the matrix cannot finish before the January freeze, shrink
the *matrix*, not the per-condition counts — fewer conditions with auditable n beat
a full grid of anecdotes. Reserve the final week for zero data collection.

## Reporting floor

Non-negotiables for the results section, independent of subfield:

- Trials per condition and total attempts, including discards, with discard rules.
- Success criterion stated operationally (what sensor reading / judge decides).
- Dispersion for every stochastic number — interval, quartiles, or all raw points
  when n is small; never a bare mean.
- Failure distribution table matched to the labeled categories.
- Wall-clock and compute for learned components; trial duration for hardware.
- Which numbers are sim and which are real, in the table itself, not the caption.

## Baseline fairness

- Give baselines the same tuning budget, sensor stream, and reset quality as the
  proposed method, and say so in one sentence.
- Prefer the strongest *published* configuration over a reimplementation you cannot
  make fast; if reimplementing, report your version's score on a setting where the
  original published numbers exist.

## Vignette: turning a demo matrix into a claim test

A draft evaluates a new whole-body controller on eight household tasks and reports
success rates — a demo matrix. The claim, once written down, is "torque-limit
awareness, not trajectory optimality, drives the reliability gain." The redesign:
(1) an ablation running the same controller with torque-awareness disabled, same
eight tasks; (2) a stress condition where torque limits bind hard (heavy objects)
versus one where they never bind — the claim predicts the gain concentrates in the
first; (3) failure attribution distinguishing torque-saturation failures from
tracking failures. Three conditions replaced five decorative tasks, and the paper
gained a falsifiable spine without new hardware.

## Output format

```text
[Claim -> condition map] <each claim row -> experiment>
[Protocol status] pre-registered / drifting / post-hoc
[Counts] <per-condition n, denominators, interventions>
[Sim/real ledger] clean split / mixed (fix)
[Failure attribution] <categories + dominant mass>
[Decisive missing run] <the one experiment to add next>
```
