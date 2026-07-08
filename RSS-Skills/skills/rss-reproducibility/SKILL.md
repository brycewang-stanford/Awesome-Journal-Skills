---
name: rss-reproducibility
description: Use when strengthening the reproducibility of an RSS (Robotics: Science and Systems) paper whose evidence lives partly on hardware — platform disclosure ledgers, log-backed trial claims, seeds and configs for the computational half, honest replication tiers, and release plans aligned with the free open-access proceedings culture.
---

# RSS Reproducibility

Make an embodied result checkable. Robotics reproducibility is two different problems
wearing one name: the computational half (code, seeds, configs) can be rerun by
anyone; the physical half (this robot, this room, this cloth) can only be *specified*
well enough for a peer lab to attempt replication. Treat the halves separately and
state which tier each claim sits in.

## Replication tiers — declare one per claim

| Tier | What a reader can do | Minimum you must provide |
|---|---|---|
| Rerunnable | Reproduce the number from the release | Code, seeds, configs, data, one entry command |
| Re-collectable | Regenerate equivalent data on similar hardware | Full platform ledger + protocol document |
| Auditable | Verify your numbers follow from your logs | Raw trial logs + analysis scripts |
| Testimonial | Trust the authors | Nothing — and reviewers price it accordingly |

A paper mixing tiers is fine; a paper *implying* Rerunnable while delivering
Testimonial is the credibility failure RSS reviewers punish hardest.

## The platform ledger

For the physical half, disclosure is the reproducibility. A peer lab needs:

- Robot make/model and any modifications; end-effector; sensor suite with mounting
  and calibration procedure; control frequency and stack (firmware through policy).
- Environment specifics that carry load: table friction, lighting, object sourcing
  (purchasable items beat lab-fabricated ones), workspace dimensions.
- Human procedure: reset steps, intervention rules, operator role — written as
  instructions, not narrative.
- Timing facts that gate feasibility: wall-clock per trial, total campaign hours,
  battery/thermal constraints that shaped the protocol.

## Log-backed claims

The strongest robotics reproducibility artifact is the raw trial ledger:

```text
trial_0142  cond=gripper_B  obj=towel_3  seed=1142
  result=fail  cause=release_timing  video=clips/0142.mp4
  notes=operator_intervention:none
```

- One row per attempt, appended at collection time, never edited afterward.
- Analysis scripts consume the ledger and emit every table in the paper — so PDF
  numbers cannot drift from evidence.
- Ship the ledger (anonymized) in the supplement; it converts "trust us" trial counts
  into auditable ones.

## What to capture during the campaign (not after)

Reproducibility in robotics is mostly a *collection-time* discipline; these cannot
be reconstructed later:

- Per-trial ledger rows (above) appended live, including aborted attempts.
- Camera footage of every trial, named by trial ID — storage is cheaper than a
  re-run campaign, and it doubles as `rss-supplementary` raw material.
- Calibration snapshots (camera extrinsics, force-torque zeroing) at session start,
  so drift between sessions is diagnosable.
- Software state per session: commit hash, config checksum, simulator build.
- Environmental incidentals that later become reviewer questions: object wear,
  lighting changes, floor surface swaps.
- A daily one-paragraph campaign log; six weeks later it is the only honest answer
  to "why does condition B have 19 trials instead of 25?"

## Computational half: standard, therefore mandatory

- Seeds for every stochastic component (policy training, sampler init, domain
  randomization) and the variance across them, not one lucky seed.
- Exact dependency manifest, simulator version and physics timestep, GPU/CPU spec,
  and training wall-clock.
- Config files as the single source of hyperparameters; no numbers living only in
  the paper text.

## Release plan and the venue's open culture

RSS proceedings are free to every reader at roboticsproceedings.org; a paywalled PDF
with closed evidence would be off-culture. Plan the release in two states: anonymized
supplement at submission (`rss-supplementary`), public repository + ledger + footage
at camera-ready (`rss-camera-ready`). If something cannot be released (proprietary
platform, safety), say what and why in the paper — a stated gap reads as honesty, a
silent one as concealment.

## Vignette: an honest tier map

A paper couples a learned grasp ranker (trained in simulation) with hardware
clutter-clearing trials. Its declared map: the simulation training curves and
ranker metrics are **Rerunnable** (seeds, configs, dataset, one command); the
hardware success rates are **Auditable** (ledger plus analysis scripts shipped) and
**Re-collectable** for labs with a comparable arm (platform ledger and protocol
document provided); the wear-dependent behavior of one deformable object is
**Testimonial**, and the paper says so in one sentence. Reviewers can now disagree
with the evidence, but not discover its limits by surprise — which is the entire
game.

## Simulator determinism caveats

- Physics engines are only conditionally deterministic: thread counts, contact
  solver iterations, and hardware can change trajectories under the same seed.
  Record engine version, timestep, solver settings — and state whether exact replay
  or statistical equivalence is the reproduction target.
- GPU nondeterminism in training means "same seed" still needs a variance report
  across seeds to be meaningful.

## Output format

```text
[Tier map] <claim -> Rerunnable/Re-collectable/Auditable/Testimonial>
[Platform ledger] complete / gaps: <list>
[Trial ledger] exists+shipped / exists / absent
[Computational gaps] <seeds/configs/versions/variance>
[Release plan] <submission state -> camera-ready state>
[Honesty debt] <implied tier above delivered tier, if any>
```
