---
name: aamas-experiments
description: Use when designing or auditing AAMAS experiments - self-play and population-based training, opponent selection, equilibrium and regret metrics, game-theoretic simulations, ablations, seeds, hyperparameters, compute, and claim-to-evidence fit - with emphasis on experiments that probe the interaction rather than chase a single-agent leaderboard.
---

# AAMAS Experiments

Use this before submission when the empirical or simulation story is not yet locked. At AAMAS
the experiment exists to test the *interaction* claim, not to top a benchmark.

## Experiment audit

- Map each empirical claim to a game, a self-play run, a population sweep, an ablation, or a
  deviation test.
- Choose opponents deliberately: self-play alone rarely suffices; include held-out opponents,
  population sets, or classical strategies as the claim requires.
- Separate simulations that validate a solution concept (where the equilibrium is known) from
  real or applied studies that show practical multiagent behavior.
- Report uncertainty for stochastic results over both seeds and opponents: standard errors,
  confidence intervals, or paired tests.
- Report the environment, number of agents, training regime, evaluation protocol, metrics,
  hyperparameter ranges, chosen settings, seeds, hardware, software versions, and runtime.
- Add ablations for the interaction mechanism (communication, reward sharing, the payment rule),
  not just cosmetic variants.
- Audit for the mismatch between the strategic claim and the setup: an equilibrium claim tested
  against only one fixed opponent, or a cooperation claim that hides a reward-shaping constant.

## What experiments are for at this venue

- The strongest design shows the interaction under stress: agents that *can* deviate, opponents
  the method did not train against, and populations that vary in size or composition.
- One experiment that lets agents try to exploit the mechanism and fails to profit is worth more
  than five extra environments where nothing strategic is tested.
- Reviewers, often game theorists, check whether the metric matches the claim: convergence to a
  named solution concept, exploitability, social welfare, or regret - not just episodic return.

## Interaction-validation design table

| Interaction claim | Matching experiment | Reject pattern avoided |
|---|---|---|
| Converges to equilibrium | Convergence/exploitability curve under simultaneous adaptation | "Equilibrium asserted, never measured" |
| Mechanism is truthful | Strategic-deviation test: an agent tries to misreport | "Truthfulness proved, never stress-tested" |
| Beats other agents | Round-robin vs held-out opponents and a population | "Self-play only" |
| Emergent cooperation | Sweep over reward/opponent settings with variance | "One seed, one setting, one story" |

## Vignette: a coordination-protocol study

Suppose the paper claims a learned protocol raises cooperation in a repeated public-goods game.
The matching plan: sweep group size and defector fraction for cooperation curves, add held-out
opponents that never appeared in training, and inject a free-rider agent to measure whether it
profits - every panel tied to a numbered claim or definition.

## Statistical reporting floor

- Seeds and replication counts for every stochastic curve; captions must state whether bands are
  standard errors, confidence intervals, or quantiles, and how many opponents were averaged.
- Report the compute actually consumed by self-play, not vague feasibility language.

## Output format

```text
[Experiment readiness] strong / adequate / weak
[Claim -> evidence map] <claim: game / self-play / population / deviation test>
[Missing interaction evidence] <opponents / deviation test / seeds / metric>
[Reproducibility gaps] <hyperparameters / compute / env / seeds>
[Decision-critical next run] <one experiment or simulation>
```
