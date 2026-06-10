---
name: ectj-identification-strategy
description: Use when stress-testing the identification, assumptions, asymptotics, regularity conditions, proofs, and leading-case theory in a The Econometrics Journal submission.
---

# EctJ Identification Strategy

Use this for theory and methods integrity. EctJ readers will tolerate compactness, but not
hidden assumptions or vague asymptotic claims.

## Audit

- State the population object, identifying restrictions, estimator or test statistic, and
  target parameter before derivations.
- Label each regularity condition by role: existence, identification, consistency,
  asymptotic normality, bootstrap validity, finite-sample approximation, or computation.
- Show why the leading case is not a toy example; connect assumptions to the empirical
  application.
- Keep proofs in the main text or printed appendix when current RES guidance requires that;
  do not park mathematical proofs only in the online appendix.
- Separate theorem statements from implementation advice and simulation claims.
- Flag any assumption that is convenient but empirically fragile.

## Referee attack surface

EctJ referees usually attack the bridge between compact theory and practical use. Pre-answer these points:

- **Object drift**: the target parameter in the theorem is not the object estimated in the application.
- **Assumption opacity**: a regularity condition is stated but never tied to a data feature or estimator step.
- **Leading-case weakness**: the theorem solves a toy case whose constraints make the empirical example
  irrelevant.
- **Proof placement risk**: critical derivations are hidden in unreviewed online material or an untraceable
  appendix.
- **Simulation mismatch**: the Monte Carlo design does not probe the assumption most likely to fail.

For each attack, write the exact theorem, assumption, table, or paragraph that will answer it.

## Output format

```text
[Identification status] defensible / needs repair / not ready
[Target object] <parameter, estimator, test, or procedure>
[Critical assumptions] <condition -> role>
[Proof gaps] <missing lemma, rate, regularity, or edge case>
[Applied connection] <how the application validates the setup>
```
