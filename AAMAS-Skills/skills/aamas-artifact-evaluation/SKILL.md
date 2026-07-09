---
name: aamas-artifact-evaluation
description: Use when packaging AAMAS multiagent code, environments, opponent and population sets, random seeds, game definitions, and logs as anonymous supplementary evidence or a public post-acceptance release, even without a separate artifact badge, so that game-theory and MARL reviewers can inspect and re-run the interaction claims.
---

# AAMAS Artifact Evaluation

Use this for evidence packaging around AAMAS. Because the venue is about interaction, an
artifact must make a *multiagent* claim inspectable: the game, the other agents, and the
protocol, not just a single trained model.

## Artifact plan

- Decide what a reviewer needs to believe the interaction claim: game or environment code,
  opponent/population definitions, the training regime, seeds, payoff logs, proofs, or
  qualitative episode traces.
- Keep decision-critical evidence in the main paper or appendix; optional bulk runs can live in
  the supplementary zip.
- Anonymize repository history, paths, environment names, license headers, cluster paths, and
  commit authors for the review version.
- Include a minimal reproduction map: environment build, dependencies, hardware, commands,
  expected outputs, per-run wall-clock, seeds, and known nondeterminism (especially in
  self-play).
- For a deployed or human-subject setting, give enough provenance for credible reproduction
  without violating data-use terms.
- After acceptance, replace anonymous archives with a public, licensed, citable artifact.

## What AAMAS evidence reviewers open first

The single fact that shapes packaging: a reviewer will re-run a small **game** far sooner than
they will retrain a large policy, so make the strategic core turnkey before polishing anything.

| Claim type | First artifact inspected | Common failure caught |
|---|---|---|
| Convergence to an equilibrium | The game definition and the learning-rule code | Solution concept named in the paper but not encoded in the evaluation |
| Emergent cooperation/defection | The environment and reward specification | Result depends on an undocumented reward-shaping constant |
| Beats other agents | The opponent/population set and match protocol | Only self-play reported; no held-out opponents |
| Mechanism is truthful | The payment rule plus a strategic-deviation test | No script that lets an agent try to game the mechanism |

## Worked vignette: packaging a self-play study

A hypothetical submission claims a learning rule that converges to a correlated equilibrium in a
repeated congestion game, shown by self-play.

- Ship the game as one parameterized generator (number of agents, capacity, payoff scale)
  rather than constants buried in a notebook, so reviewers can vary the interaction.
- Record the exact seed sequence and replication count behind every convergence plot; an
  equilibrium-convergence claim without seeds is unfalsifiable.
- Emit payoff and regret tables directly from logged results so PDF and artifact numbers cannot
  drift.
- Include a strategic-deviation harness: a script that drops in a non-conforming agent and
  measures whether it profits, because that is exactly what a game-theory reviewer will try.

## Calibration anchors

- Supplement inspection at AAMAS is at reviewer discretion; assume only the README and one entry
  script get opened, and design the top level accordingly.
- Supplement size and format caps vary by cycle (25 MB single zip in 2026); verify against the
  current OpenReview form rather than a past year.

## Output format

```text
[Artifact role] anonymous supplement / camera-ready release / public archive
[Contents] <game/env/opponents/seeds/proofs/logs>
[Anonymity risks] <paths/metadata/licenses/URLs>
[Reproduction level] turnkey / scripted / descriptive / weak
[Fixes before upload] <ordered list>
```
