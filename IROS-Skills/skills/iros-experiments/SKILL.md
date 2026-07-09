---
name: iros-experiments
description: Use when designing or auditing IROS experiments — real-robot trial counts, success criteria set in advance, reset procedures, failure taxonomies, baseline fairness on matched hardware, sim-to-real gap reporting, small-n statistics, and the claim-to-evidence ladder that embodied-systems reviewers apply before they trust a demo.
---

# IROS Experiments

Use this before submission when the empirical story is not yet locked. At IROS, experiments exist to
prove a robot did something reliably, under stated conditions — not to top a leaderboard.

## Experiment audit

- Map each claim to the evidence that supports it: a real-robot trial set, a simulation study, an
  ablation, or a field deployment. A claim with no matched evidence is an overclaim.
- Define the **success criterion before running**, in one sentence a skeptic would accept, and hold to
  it; a criterion invented after seeing results is a reviewer red flag.
- Report **trial counts and resets**: how many attempts, how start conditions were randomized, and what
  reset happened between trials. Hidden resets inflate reliability.
- Publish a **failure taxonomy** with counts, not just a success rate; the failures are where reviewers
  calibrate trust.
- Make **baselines fair**: run them on the same platform, sensors, and route, with comparable tuning
  effort, or state precisely why not.
- Separate **simulation from real** and report the **sim-to-real gap** as a number; an implied zero gap
  is the fastest way to lose a reviewer.

## The evidence ladder

| Claim altitude | Evidence IROS expects | Reject pattern avoided |
|---|---|---|
| "The system works" | Trials with n, success interval, and resets stated | "One hero run shown as if typical" |
| "It is reliable" | Failure taxonomy with counts across conditions | "Success rate with no failures reported" |
| "It transfers" | Real-robot numbers plus the measured sim-to-real gap | "Sim results implying real performance" |
| "It beats prior work" | Same-hardware baseline on the same task | "Comparison against a weaker or re-tuned baseline" |
| "It runs onboard" | Measured rate and power under the real compute budget | "Real-time asserted, never measured" |

## Small-n statistics for real robots

Real trials are expensive, so n is small — but small n does not excuse a bare mean. Report a success
count as a proportion with a confidence interval (a Wilson interval behaves better than normal
approximation at small n), and for paired system-vs-baseline comparisons on the same trials, prefer a
paired test over independent means. State n every time; "usually succeeds" is not a measurement.

## Vignette: a manipulation reliability study

Suppose the system claims reliable grasping of unseen objects. The matching plan: fix an object set and
a success criterion (lifted and held 3 seconds), run a stated number of trials per object with
randomized poses, log every failure by cause (slip, mis-localization, collision), and report the
per-object and pooled success rates with intervals. A simulation sweep over object mass then maps where
the grasp model degrades, and the real-vs-sim gap is stated — every panel tied to a specific claim.

```text
Trial-logging template (one row per attempt):
  trial_id, object/scenario, start_pose_seed, outcome{success|fail},
  failure_cause, reset_type, wall_time, notes
Aggregate to: success rate + interval per condition, failure histogram, sim-to-real delta.
```

## Reporting floor

- Every reliability figure carries n and a criterion; every timing claim carries a measured rate and the
  compute/power budget it ran under.
- Report the compute actually consumed on the robot, not a desktop proxy.

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: trials/sim/ablation/deployment>
[Missing evidence] <trials/resets/failures/baseline/transfer>
[Statistics] criterion set? interval reported? paired where paired?
[Decision-critical next run] <one experiment on the robot>
```
