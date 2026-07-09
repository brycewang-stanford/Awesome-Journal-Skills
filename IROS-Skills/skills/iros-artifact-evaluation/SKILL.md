---
name: iros-artifact-evaluation
description: Use when packaging IROS evidence for a skeptical reviewer even though IROS runs no formal artifact track — the robotics artifact stack of hardware ledger, logs, configs, code, and data, what an embodied-systems reviewer opens first, review-time anonymity versus acceptance-time public release, and making a claim auditable not asserted.
---

# IROS Artifact Evaluation

IROS has no formal artifact-evaluation track or badge, so "artifact" here means the evidence bundle a
reviewer *could* inspect and that a careful author prepares anyway. The audience is an embodied-systems
reviewer who trusts a logged trajectory over a claimed one, and who cannot rerun your robot but can read
your logs, configs, and code.

## The robotics artifact stack

- **Hardware ledger:** platform, sensors (make/model/firmware), actuators, onboard computer, and power
  budget — the embodiment the result depends on.
- **Logs:** time-stamped rosbag-equivalent recordings for representative trials, so a claim about a
  contact force or trajectory is auditable.
- **Configs:** the exact parameters, calibration, and launch files that produced the reported runs.
- **Code:** the system as run, with an entry point and a one-minute orientation in the README.
- **Data:** any dataset or object set, with provenance and licensing; for restricted data, enough detail
  for credible reproduction without violating terms.

## What an IROS reviewer inspects first

| Claim type | First artifact inspected | Common failure caught |
|---|---|---|
| "Runs onboard at rate X" | Timing logs and the compute/power spec | Rate measured on a desktop, not the robot |
| "Reliable across trials" | The trial log and failure record | Success rate with resets and failures omitted |
| "Transfers from sim" | Paired sim and real logs | Only sim logs exist; the gap is asserted |
| "Beats prior system" | Baseline configs on the same platform | Baseline run with different hardware or tuning |

Because a reviewer will read a log far sooner than rebuild a robot, make the **logs and configs**
legible first, and polish the code second.

## Review-time versus acceptance-time states

- **Review time (double-anonymous):** strip organization names, cluster paths, calibration files tagged
  with a lab, commit authorship, and any URL carrying a lab identity. If you link code, use an anonymized
  mirror or omit the link and describe the artifact.
- **Acceptance time:** replace anonymized stand-ins with a public, licensed, citable release; test every
  link from a logged-out browser; and add the DOI or archival link the IEEE Xplore record can point to.

## Worked vignette: packaging a field-robot result

A submission claims a lidar-inertial system runs onboard across three outdoor sites.

- Ship one representative rosbag per site plus the launch/config that processed it, so a reviewer can see
  the sensor streams and the estimated trajectory line up.
- Record the compute-and-power measurement method, not just a headline rate.
- Emit the trajectory-error tables directly from the logged runs so the paper numbers and the artifact
  cannot drift apart.
- State which site is easy and which stresses the system, since that mapping is what a reviewer grades.

```text
Artifact layout:
  /hardware.md      platform, sensors, compute, power
  /logs/<site>/     time-stamped bags for representative trials
  /config/          calibration, params, launch files
  /src/             system as run + README (1-minute orientation)
  /data/            provenance + license (or access instructions)
```

## Output format

```text
[Artifact role] review-time anonymous / acceptance-time public
[Contents] <hardware/logs/configs/code/data>
[Anonymity risks] <paths/metadata/URLs/calibration tags>
[Auditability] logged / scripted / described / asserted
[Fixes before upload] <ordered list>
```
