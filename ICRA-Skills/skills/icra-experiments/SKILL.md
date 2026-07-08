---
name: icra-experiments
description: Use when designing or auditing the experimental section of an ICRA paper — real-robot versus simulation-only evidence, trial counts and success-rate reporting, task distributions and resets, baseline fairness on shared hardware, sim-to-real transfer claims, failure-mode analysis, and the statistics robotics reviewers actually expect.
---

# ICRA Experiments

Experimental evidence is where ICRA reviews are won and lost. The community's
core suspicion is the cherry-picked demo: one lucky run, filmed once, presented
as capability. The experiments section exists to prove the demo was not luck.

## The evidence ladder

Climb as high as the claim requires; state the rung explicitly in the paper.

| Rung | Evidence | Supports claims like |
|---|---|---|
| 1 | Simulation only, single environment | "the formulation is feasible" |
| 2 | Simulation, randomized dynamics/scenes | "the method is robust in sim" |
| 3 | Real robot, controlled lab task | "works on hardware" |
| 4 | Real robot, varied objects/terrains/subjects | "generalizes physically" |
| 5 | Extended/field deployment, uncontrolled conditions | "works in the world" |

Simulation-only papers are not banned at ICRA, but a rung-2 evidence base cannot
carry rung-4 language. The mismatch between claim altitude and evidence rung is
the single most cited weakness in robotics reviews. If hardware is unreachable,
scope the claims to simulation and say why the sim is trustworthy (validated
dynamics, established benchmark, physics-accurate contact).

## Trials, resets, and what a success rate means

- **Pre-register the protocol privately**: number of trials, success criterion,
  and abort rule *before* collecting headline numbers; report the criterion
  verbatim in the paper ("success = object lifted 10 cm and held 5 s").
- **Trial counts:** 5 trials per condition is anecdote, 10-25 is typical ICRA
  practice, more when variance is high. Report n everywhere, including captions.
- **Resets are part of the method.** If a human re-tees the object between
  trials, say so; automated-reset claims are different capability claims.
- **No silent trial deletion.** "Excluding two trials due to hardware fault"
  is fine when disclosed with cause; undisclosed exclusion is fabrication.
- **Report dispersion**, not just means: min/max or standard deviation over
  trials, and per-condition breakdowns rather than one pooled percentage.

## Baseline fairness on hardware

Hardware baselines are expensive, so reviewers scrutinize the shortcuts:

- Run baselines on the **same platform, same task instances, same sensor
  stream** — a baseline run in simulation against a method run on hardware is
  not a comparison, it is two anecdotes.
- Tune the baseline with comparable effort and say what that effort was; "the
  baseline used default parameters" invites the fatal review sentence "the
  baseline was not tuned."
- Include the naive-but-strong baseline (a well-engineered classical planner or
  PID stack). Beating only learned rivals while a 1990s controller would have
  matched the result is a known embarrassment pattern at robotics venues.
- When a competitor's code is closed, reimplement and mark results
  "reimplementation," or compare on published numbers with the setup delta
  stated.

## Sim-to-real claims

If the paper trains in simulation and deploys on hardware, quantify the gap,
never just bridge it rhetorically:

- Report the same metric in sim and real side by side; the delta *is* a result.
- Name the randomization/adaptation mechanism and ablate it — "domain
  randomization" as an unexamined incantation draws fire.
- Zero-shot vs fine-tuned transfer must be labeled; ten minutes of on-robot
  fine-tuning is legitimate but is a different claim.

## Failure analysis as a first-class section

ICRA reviewers trust papers that dissect their failures more than papers that
report none. Budget for a failure table:

```text
Failure taxonomy (example structure)
  F1 perception: slip not detected (4/50 trials) — cause: torque noise
     under 0.3 N·m threshold; mitigation: none in current sensing
  F2 planning: recovery pose in collision (2/50) — cause: stale octomap
  F3 hardware: gripper timeout (1/50) — excluded (disclosed), watchdog fixed
Reported: 43/50 success (86%); all 7 failures categorized above.
```

A reviewer reading this knows the team understands its own system. The video
attachment should show at least one failure case for the same reason
(see `icra-supplementary`).

## Ablations with hardware budgets

Full ablation grids are a simulation luxury. The hardware-honest pattern:

- Run the complete grid in simulation; run on hardware only the two or three
  ablations that test the paper's central mechanism.
- Say exactly this in the paper — reviewers accept the economics when the
  choice of which ablations earned hardware time is justified.
- Never present a simulation ablation in a way that lets a reader mistake it
  for a hardware result; label every table row's regime.

## Statistics that fit robotics sample sizes

- With n = 10-25 trials per condition, prefer exact binomial confidence
  intervals for success rates over normal approximations.
- Paired designs (same object set for method and baseline) plus a paired test
  beat unpaired comparisons at the same n.
- Do not run twelve significance tests on six pages; pick the one comparison
  the claim rests on and treat the rest descriptively.
- Learning components: report seeds and per-seed outcomes for training, then
  hold the *deployed* policy fixed across hardware trials so trial variance is
  physical, not training noise.

## Pre-deadline experiment audit

1. Claim altitude vs evidence rung matched for every abstract claim?
2. Success criterion stated verbatim; n visible in every table/caption?
3. Baselines: same hardware, tuned, includes strong classical option?
4. Sim-vs-real deltas reported numerically where transfer is claimed?
5. Failure taxonomy present, counts summing to total trials?
6. Statistics: intervals suited to small n; one load-bearing test?

## Output format

```text
[Evidence rung] <1-5> vs claim altitude <1-5> — mismatch: <y/n>
[Trial audit] n per condition, criterion stated, exclusions disclosed
[Baseline audit] hardware-matched? tuned? classical baseline present?
[Transfer audit] sim/real deltas numeric? adaptation labeled?
[Failure analysis] taxonomy present? counts reconcile?
[Single weakest table/figure] <which and why>
```
