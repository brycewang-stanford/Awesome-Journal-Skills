---
name: icra-artifact-evaluation
description: Use when packaging the artifacts behind an ICRA paper — ROS packages, controllers, simulation environments, trained policies, CAD and PCB files, datasets, and trial logs — into something a robotics reviewer or reader can actually run or audit, given that ICRA has no formal artifact-badging track to certify it for you.
---

# ICRA Artifact Evaluation

ICRA, unlike several software-systems conferences, has had no standing artifact
evaluation committee or badge system in recent cycles (re-check the current
year's calls before asserting this to authors — tracks appear and disappear).
The absence cuts both ways: nobody will certify your artifact, and nobody will
catch its problems before readers do. This skill applies an artifact-evaluator's
discipline voluntarily, because in robotics the artifact often *is* the
contribution's proof.

## The robotics artifact stack

A robotics paper's artifact is rarely just "the code." Inventory all six layers
and decide, per layer, released / partially released / withheld-with-reason:

| Layer | Typical contents | Common blocker |
|---|---|---|
| Algorithms | planners, controllers, learning code | none — release |
| Integration | ROS launch files, configs, calibration | "works only on our stack" |
| Simulation | worlds, robot models (URDF/SDF), randomization | third-party asset licenses |
| Learned weights | trained policies, perception models | training data licensing |
| Hardware design | CAD, PCB, BOM for custom parts | patent/commercialization plans |
| Evidence | rosbags, trial videos, session sheets | raw-log size (TB-scale) |

A paper whose novelty is a custom end effector but which releases only Python
scripts has released the wrong layer. Match the release to the claim.

## The five-minute-skeptic standard

Package for a reviewer who gives you five minutes before forming a judgment:

```bash
git clone <anonymized-artifact-url> && cd artifact
docker build -t icra-artifact .          # or: ./setup.sh — one command, pinned deps
docker run icra-artifact make figure3    # regenerate a headline result in sim
docker run icra-artifact make table2     # recompute stats from released logs
cat CLAIMS.md                            # claim → command → expected output map
```

- The first runnable thing must not require a robot: a simulation reproduction
  or a log-replay analysis gives the skeptic a win in minutes.
- `CLAIMS.md` maps each paper claim to a command and its expected output, and
  explicitly lists which claims require physical hardware (audit tier — see
  `icra-reproducibility`).
- Pin everything: base image, ROS distro, Python deps, simulator version.
  "Latest Gazebo" is a bug report generator.

## Hardware-dependent artifacts

For layers that need the physical robot:

- Ship a **log-replay mode**: the perception and decision stack runs against
  released rosbags, letting readers verify the pipeline without the arm.
- Ship the **sim twin**: the same launch files targeting the simulated platform,
  clearly marked as not the source of the paper's hardware numbers.
- Document the hardware interface narrowly (which driver topics/services the
  stack expects) so ports to other platforms are feasible.
- For custom mechanisms, releasing CAD + BOM converts "trust our gripper" into
  "build our gripper"; if commercialization blocks this, say so in the paper
  rather than staying silent.

## Datasets and logs as artifacts

- Extracted per-trial features plus a representative raw sample beat an
  undifferentiated terabyte dump; provide a download script with checksums.
- License explicitly (CC-BY for data, permissive or copyleft choice for code);
  robotics data with humans in frame needs consent/ethics notes.
- Long-term hosting: university archives, Zenodo-style DOI services, or IEEE
  DataPort outlive lab NAS boxes and personal cloud links.

## Review-time vs acceptance-time states

Under the double-anonymous policy (2026 cycle onward), the artifact has two
lives:

1. **Review state:** anonymized hosting, no org/usernames in URLs, git history
   squashed (history leaks author emails), license file present but
   copyright-holder line deferred ("held for anonymity").
2. **Public state (post-acceptance):** real hosting, authors restored, DOI
   minted, README linking the IEEE Xplore entry, camera-ready pointing at the
   permanent URL (coordinate with `icra-camera-ready`).

Prepare both from the start; converting a name-riddled repo to anonymous form
in deadline week always misses something.

## Safety as an artifact property

Robotics artifacts can move mass. Before anyone external runs your controller:

- Ship conservative default limits (velocity, torque, workspace bounds) and
  make the paper's aggressive settings an explicit opt-in flag.
- Document the E-stop assumption and any human-proximity constraints in the
  hardware protocol, not just the lab's tribal knowledge.
- State firmware/driver versions known to behave; a controller tuned on one
  firmware can oscillate on another, and that failure lands on your artifact's
  reputation.

## Withholding honestly

Legitimate reasons to withhold layers exist (industrial partners, export
controls, safety of a hazardous procedure). The rule is disclosure: state in
the paper what is withheld and why, and maximize the released remainder — e.g.,
withheld weights but released training code and evaluation harness. Undisclosed
gaps discovered later cost more reputation than declared ones.

## Packaging sequence

1. Inventory the six layers; mark release state and blockers for each.
2. Build the Docker/pinned environment; verify `make figure3` on a clean machine.
3. Write `CLAIMS.md`; separate rerunnable from hardware-audit claims.
4. Add log-replay mode and sim twin for hardware-bound layers.
5. Produce the anonymized review state; leak-check URLs, history, metadata.
6. Stage the public state for acceptance day.

## Output format

```text
[Layer inventory] released: <layers> | partial: <layers> | withheld: <layers+reason>
[Five-minute test] clean-machine run of headline command: pass / fail
[CLAIMS.md] complete: y/n — hardware-only claims flagged: <list>
[Replay/sim twin] present: y/n
[Anonymity state] review-safe: y/n — leaks: <list>
[Hosting] review URL type + acceptance-day plan
```
