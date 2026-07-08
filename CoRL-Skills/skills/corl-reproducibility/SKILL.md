---
name: corl-reproducibility
description: Use when making a CoRL robot-learning paper reproducible — pinning simulator and driver versions, releasing training configs, demonstration data and checkpoints, documenting hardware setups that cannot be rerun, seed policy, evaluation scripts, and honest availability statements for code, data, and robot platforms.
---

# CoRL Reproducibility

Robot-learning papers have a split reproducibility problem: the *training* half is
software and can in principle be rerun anywhere, while the *hardware* half is a
physical setup nobody else owns. Strong CoRL papers treat these halves
differently — the software half is made **rerunnable**, the hardware half is made
**auditable** — and say plainly which is which.

## The rerunnable half: simulation and training

The silent reproducibility killers in this field are version-shaped:

- **Simulator versions change physics.** Contact solvers, default damping, and
  collision margins shift between releases of MuJoCo, Isaac, PyBullet, and
  friends; a policy's success rate is a function of the simulator build. Pin the
  exact version and any physics-relevant flags.
- **Environment wrappers drift.** Task-suite repositories (benchmark forks,
  custom reward shims) move under you; record the commit hash of every env repo,
  not just your own.
- **GPU nondeterminism.** cuDNN autotuning and atomics make bit-identical
  training runs unrealistic — so define reproducibility at the *distribution*
  level: same configs + fresh seeds should land inside your reported seed spread.

```yaml
# repro-manifest.yaml — ship at the repo root; one block per results table
table_3:
  code_commit: ""            # your repo @ exact hash
  env_suite:  {repo: "", commit: "", sim: "mujoco==X.Y.Z", physics_flags: []}
  training:   {config: "configs/table3.yaml", seeds: [0,1,2,3,4], gpu: "1xA100-80GB", hours: 14}
  data:       {demos: "dataset-v2 (1,204 episodes)", url_or_status: "", license: ""}
  checkpoints: {released: true, path: "ckpts/table3/", selection_rule: "last epoch, no eval peeking"}
  evaluation: {script: "eval/run.py", episodes_per_task: 50, init_state_list: "eval/states.json"}
expected_tolerance: "per-task success within ±4 pts of Table 3 mean"
```

The `selection_rule` line matters more than it looks: checkpoint selection via
test-set peeking is the field's quiet irreproducibility engine, and stating the
rule is the cheapest credibility purchase available.

## The auditable half: hardware

Nobody will re-run your robot, so the goal is that a skeptical expert could
*verify the experiment happened as described* and *rebuild an equivalent rig*:

| What to document | Why an auditor needs it |
|---|---|
| Robot model, end-effector, firmware/driver versions | Behavior differs across firmware, not just robots |
| Sensor models, mounting poses, calibration procedure | Camera extrinsics silently dominate visuomotor results |
| Control interface: frequency, action space, safety filters | "30 Hz end-effector deltas" vs "torque control" are different papers |
| Deployed compute + inference latency | Policy behavior is latency-dependent |
| Scene inventory: objects (make/size), fixtures, lighting | Enables an equivalent-rig rebuild and honest comparison |
| Raw episode logs and unedited evaluation video | The audit trail for every printed success rate |

Log every evaluation episode at capture time (timestamped video plus a CSV of
outcomes); retrofitting an audit trail after reviews ask for it is impossible.

## Data and checkpoint release

- Demonstration datasets are results: release episode counts, collection method
  (teleop rig, scripted, crowdsourced), operator count, and filtering rules.
- Released checkpoints let others reproduce *evaluation* even when training is
  too expensive to repeat — for large policies this is often the highest-value
  artifact you can ship.
- If data or weights cannot be released (proprietary platform, human-subject
  footage), say so in the paper with the reason, and release what remains:
  configs, eval scripts, sim environments, and metrics logs. A precise
  partial-release statement outperforms a vague "code available upon request."

## During review vs after acceptance

- During review everything must be anonymous (see `corl-submission`): anonymized
  repo mirrors, no lab-identifying video, no cloud buckets with named projects.
- The 2026 camera-ready pipeline has a sharp constraint: **PMLR does not accept
  video as supplementary material**, so post-acceptance videos, code, and data
  live on external hosting (project site, GitHub, archive), linked from the main
  text (corl.org author instructions, read 2026-07-08). Plan the public homes of
  artifacts before the October camera-ready deadline, and prefer DOI-stamped
  archives for anything you cite as permanent.
- No formal reproducibility checklist was verified for the 2026 cycle in this
  pack (待核实) — but reviewer expectations enforce one informally; use the
  manifest above regardless of what the form requires.

## Availability statement patterns

```text
Strong:  "Code, training configs, evaluation scripts, and the 1,204-episode
          teleop dataset: <URL>. Checkpoints for Tables 2-4: <URL>. Hardware
          evaluations are documented in Appendix C (rig spec, logs, uncut video);
          the platform itself cannot be redistributed."
Weak:    "Code will be released upon acceptance."      (unverifiable promise)
Broken:  "Results reproducible with standard settings." (no artifact at all)
```

## Pre-submission audit

```text
[ ] repro-manifest present; one block per headline table
[ ] Simulator/env/driver versions + commits pinned everywhere
[ ] Seed policy stated; checkpoint selection rule stated
[ ] Hardware rig spec complete enough for an equivalent rebuild
[ ] Episode-level logs + uncut eval video archived internally
[ ] Data/checkpoint release plan with named blockers, if any
[ ] Anonymous during review; external hosting plan ready for camera-ready
```

Verify the live cycle's supplementary and camera-ready rules at
https://www.corl.org/contributions/instruction-for-authors before promising any
artifact channel — PMLR-side constraints and CoRL-side forms both change yearly.
