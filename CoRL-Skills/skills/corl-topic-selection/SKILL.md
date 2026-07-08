---
name: corl-topic-selection
description: Use when deciding whether a project belongs at CoRL, the Conference on Robot Learning, or should be routed to ICRA, IROS, RSS, NeurIPS, ICLR, ICML, or a journal — based on whether the learned component is the contribution, what embodied evidence exists, and which reviewer community should judge the claim.
---

# CoRL Topic Selection

CoRL sits at a deliberate intersection: it was founded in 2017 precisely because
learning-centric robotics papers were being squeezed between robotics conferences
that undervalued the learning and ML conferences that undervalued the robot. Routing
to CoRL is therefore a two-axis decision, and a project must score on **both** axes
to belong here.

## The two-axis test

Ask the two questions separately and honestly:

1. **Is learning the contribution?** If you replaced the learned policy, model, or
   representation with a hand-engineered module and the paper's story survived, the
   learning is decoration. CoRL reviewers — drawn from the robot-learning community,
   not general robotics — will notice within one page.
2. **Does the claim need embodiment?** If the result would be equally convincing on
   a static vision benchmark or a gridworld, the robot is decoration. NeurIPS, ICML,
   or ICLR will serve that paper better and reach a larger methods audience.

Only a yes-yes project is CoRL-shaped. A yes-no project is an ML paper; a no-yes
project is a robotics-systems paper; a no-no project needs rethinking, not routing.

## Routing map

| Project profile | Best home | Why not CoRL |
|---|---|---|
| Imitation / RL / VLA policy with real-robot or credible sim evaluation | **CoRL** | — |
| Sim-to-real transfer method, transfer gap quantified | **CoRL** | — |
| Robot foundation model, data scaling, cross-embodiment training | **CoRL** | — |
| New gripper, SLAM pipeline, planner with hardware demo, learning peripheral | ICRA / IROS | Reviewers here score the learning question first |
| Broad robotics science where learning is one of several components | RSS | CoRL wants the learning claim central |
| Representation learning evaluated only on offline datasets | NeurIPS / ICLR / ICML | No embodied claim to judge |
| Benchmark or dataset for robot learning | CoRL (fits) or RA-L/journal for archival scope | Check the current CFP wording |
| Mature system with extensive field validation, long paper | T-RO / IJRR / Science Robotics | Conference format too small |

## Signals from the venue itself

- The CoRL 2026 Call for Papers (https://www.corl.org/contributions/call-for-papers,
  read 2026-07-08) frames the conference around the role of machine learning in
  robotics; the community's recent proceedings (PMLR v270 for 2024, v305 for 2025)
  are dominated by manipulation, locomotion, humanoid, VLA-model, and sim-to-real
  work.
- Exemplar routing datapoints: SayCan (PMLR v205) and RT-2 (PMLR v229) — language
  models grounded in robot affordances — went to CoRL, not to an NLP or ML venue,
  because the grounding on hardware *was* the claim. See
  `../../resources/exemplars/library.md`.
- CoRL is young (first edition 2017, Mountain View; the 2026 Austin edition is the
  10th) and single-track in spirit: it publishes far fewer papers than ICRA/IROS,
  so incremental fits that would survive at a mega-conference get filtered here.

## Timing reality for 2026-07-08

The CoRL 2026 deadline (paper: May 29, 2026) has passed. Routing decisions made
today are about the **next** deadlines, so build the comparison calendar forward:

```text
Routing calendar as of 2026-07-08 (verify each venue's own pages):
  CoRL 2027        — CFP not yet posted; recent cycles closed late May/early June  [待核实]
  ICRA 2027        — direct-submission deadline historically mid-September
  RSS 2027         — historically late January / early February
  NeurIPS 2026     — main deadline has also passed for this year
  ICLR 2027        — historically late September; nearest big ML deadline
  RA-L (journal)   — rolling; pairs with ICRA/IROS presentation options
```

A learning-heavy project missing CoRL 2026 typically weighs ICLR 2027 (if the sim
evidence stands alone) against ICRA 2027 (if the hardware story stands alone)
against waiting for CoRL 2027 (if the paper genuinely needs both audiences).

## Common misroutes seen in review

- **The benchmark-only RL paper.** Strong returns on standard sim suites, no
  robot-specific insight — reviewers ask "why is this not at an ML venue?" and
  score fit, not just quality.
- **The teleop-data demo.** Beautiful hardware video, but the learning method is an
  off-the-shelf recipe with no analysis; reviewers ask what the community learns.
- **The one-task policy.** Learning contribution present, but evaluated on a single
  task instance with no generalization axis; CoRL's evaluation culture (multiple
  tasks, objects, seeds, episodes — see `corl-experiments`) makes this fragile.
- **The theory paper without any environment.** Pure sample-complexity analysis
  travels better at COLT/NeurIPS unless it predicts something testable on a robot.

## Framing once you commit

If the answer is CoRL, write the fit into the paper rather than assuming it:

- Name the embodied task family in the first paragraph, and the learned component
  in the second — both before any architecture detail.
- State the evidence scale early (how many tasks, trials, robots, sim environments)
  so the reviewer's evaluation expectations are anchored by you, not by habit.
- Reserve explicit space for the **Limitations section — mandatory at CoRL and
  counted inside the 8-page limit** in the 2026 instructions — from day one.
- Choose baselines from the robot-learning literature (BC, offline RL, diffusion
  policies, VLA models), not only from the classical-control literature.

## Output format

```text
[CoRL fit] yes / no / borderline
[Axis 1 — learning is the contribution] yes / no + one-line justification
[Axis 2 — claim needs embodiment] yes / no + one-line justification
[Alternative venue] <name + reason, if either axis fails>
[Next actionable deadline] <venue, date, source URL to reverify>
```

Re-verify the current cycle at https://www.corl.org/ before acting: CoRL scope
wording, deadlines, and policies are re-issued each year by that year's chairs.
