---
name: ccs-experiments
description: Use when designing or auditing ACM CCS experiments, attack demonstrations, adaptive-attack defense evaluations, security measurements, baselines, overhead and cost reporting, ablations, and claim-to-evidence fit, with emphasis on evidence that survives an adversarial program committee rather than leaderboard wins.
---

# CCS Experiments

Use this before submission when the attack demonstration, defense evaluation, or measurement
story is not yet locked.

## Experiment audit

- Map each security claim to a specific artifact: an exploit run, an overhead measurement, a
  coverage number, a false-positive/false-negative table, or a measurement dataset.
- For attacks, demonstrate the exploit against a realistic, named target (software version,
  platform, configuration) and report the resource cost to the attacker.
- For defenses, evaluate against an adaptive attacker built with knowledge of the defense,
  and report performance overhead, memory cost, and any compatibility breakage.
- For measurements, validate sampling: document the population, the vantage point, coverage
  and blind spots, and ground-truth checks against known cases.
- Include baselines that represent the state of the art in attack or defense, not strawmen.
- Report variance for stochastic results and audit for leakage, selection bias, and any
  mismatch between the threat model and the tested configuration.

## What experiments are for at this venue

- CCS experiments exist to make a security claim undeniable to a skeptic, not to top a
  benchmark. One clean end-to-end exploit against a real target outweighs a table of
  micro-benchmarks.
- The strongest defense design triad: the attack it stops, an adaptive attack that knows the
  defense, and a deployment-cost measurement. Missing the middle element is the classic CCS
  defense reject.
- Reviewers, often practitioners, check whether the evaluation environment matches the threat
  model. A defense claimed for production but tested only on a toy in a lab invites the
  relevance question.

## Attack-and-defense evaluation table

| Security claim | Matching evidence | Reject pattern avoided |
|---|---|---|
| Exploit is practical | End-to-end run on named target with attacker cost | "Works only in a lab against a strawman" |
| Defense stops the attack | Detection/prevention rate on the original attack | "No numbers, only a design argument" |
| Defense resists adaptation | Adaptive attacker with defense knowledge, degraded results | "Only the non-adaptive attack was tried" |
| Deployment is feasible | Overhead, memory, compatibility on a realistic workload | "Security claimed, cost never measured" |

## Vignette: evaluating a control-flow-integrity defense

Suppose the paper proposes a fine-grained CFI scheme. The matching plan: reproduce a known
code-reuse attack and show it blocked; construct an adaptive attacker that respects the CFI
policy and search for surviving gadget chains; then measure runtime overhead and binary-size
growth on a standard benchmark suite. Every claim ties to a numbered table, and the adaptive
result is reported even when it dents the headline.

## Reporting floor

- Name every target's exact version and configuration; "a popular browser" is not a target.
- Report the attacker's resource budget (queries, time, samples) and the defense's measured
  overhead rather than vague "negligible cost" language.

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: exploit run / overhead table / measurement>
[Missing security evidence] <adaptive attack / baseline / cost / validation>
[Threat-model mismatch] <where the setup breaks the stated model>
[Decision-critical next run] <one experiment>
```
