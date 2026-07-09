---
name: aamas-reproducibility
description: Use when strengthening AAMAS reproducibility evidence for interaction claims, including proofs and game definitions, opponent and population sets, self-play protocols, random seeds, compute, uncertainty on strategic outcomes, baselines, and consistency between what the paper claims about agents and what the artifact can actually show.
---

# AAMAS Reproducibility

Use this before submission and again before camera-ready. The reproducibility question at AAMAS
is not only "can I rerun the model" but "can I reproduce the *interaction* - the same agents,
the same game, the same emergent outcome."

## Evidence map

- Map each theorem, mechanism property, convergence claim, and empirical interaction claim to a
  verifiable location in the paper, appendix, supplement, or artifact.
- For theory, state the game, the information structure, the solution concept, assumptions,
  proof dependencies, and failure modes clearly enough for a game theorist.
- For experiments, report the environment, number of agents, opponent/population set, training
  regime, evaluation opponents, metrics, hyperparameter ranges, chosen settings, seeds,
  repeated runs, compute, and runtime.
- For small or noisy strategic differences, add uncertainty: standard errors, confidence
  intervals, or paired tests over seeds and over opponents.
- Explain any missing code or environment honestly, and describe how a reader could reproduce
  the interaction in principle.
- Keep the artifact consistent with the paper; a claim the artifact cannot demonstrate is a
  review-risk multiplier.

## Claim-to-evidence audit table

| Claim | Pure-theory answer | Learning-plus-game answer |
|---|---|---|
| Solution concept reached | Proof with the game and information structure stated | Plus convergence curves under other agents' adaptation |
| Opponents / population | NA if fully analytical | The exact opponent set and how it was chosen |
| Seeds and variance | NA for deterministic results | Required for every stochastic curve and payoff table |
| Compute | NA | Hardware, per-run time, and total number of self-play runs |

Claiming an equilibrium result while the evaluation only shows two fixed agents playing once is
the recognizable AAMAS gap: reviewers read the mismatch between the strategic claim and the
thinness of the interaction evidence as carelessness about the rest.

## Vignette: a MARL-plus-convergence paper

Consider a submission proving convergence to a coarse-correlated equilibrium in a repeated game,
validated by self-play. Its reproducibility spine: the game generator and payoff scale, the
learning rule and its step sizes, the opponent set, the replication seeds, the convergence
metric, and one honest sentence on the regime where convergence is only empirical, not proved.

## Degrees of reproducibility

- Turnkey: one command reruns the game and regenerates each convergence figure from logged
  seeds.
- Scripted: scripts exist but require documented manual steps or an external environment.
- Descriptive: prose detailed enough that a competent reader could rebuild the game and agents.

For AAMAS, the strategic core should be turnkey because reviewers actually re-run small games;
large real-world or human-in-the-loop pipelines may stay scripted with deviations documented.
Stating the achieved level honestly beats overpromising turnkey behavior that fails on a clean
machine.

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Artifact consistency] complete / inconsistent / missing
[Interaction reproducibility gaps] <game/opponents/seeds/uncertainty/compute>
[Paper fixes] <must appear in main PDF>
[Supplement fixes] <appendix or artifact additions>
```
