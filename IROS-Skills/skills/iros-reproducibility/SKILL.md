---
name: iros-reproducibility
description: Use when strengthening IROS reproducibility evidence — splitting rerunnable claims from auditable-only real-robot claims, the hardware specification ledger, calibration and parameter disclosure, log capture discipline, honest code/data availability statements, and sim-to-real accounting, all inside a page budget with no supplementary PDF.
---

# IROS Reproducibility

Use this before submission and again before camera-ready. Robotics reproducibility is not the same as ML
reproducibility: a reader usually cannot rerun your robot, so the goal is to make every claim either
**rerunnable** (code/sim someone can execute) or **auditable** (logs and specs detailed enough to check),
and to be honest about which is which.

## Evidence map

- Split each claim into rerunnable or auditable. A simulation result should be rerunnable; a real-robot
  reliability number is auditable through logs and a stated protocol, not rerunnable by a reader.
- For the **rerunnable** part: pin dependencies, seeds, configs, and an entry point; state the hardware
  it assumes.
- For the **auditable** part: give the hardware ledger, calibration, parameters, trial protocol, resets,
  and representative logs.
- Report the **sim-to-real gap** explicitly; never let simulation numbers stand in for real ones.
- Write an **honest availability statement**: what code and data are released, what is withheld and why
  (proprietary hardware, safety, licensing), and how a reader could approximate reproduction.
- Keep it all in the **body** — there is no supplementary PDF to park a reproducibility appendix in.

## Rerunnable-versus-auditable table

| Claim | Rerunnable evidence | Auditable evidence |
|---|---|---|
| Simulation ablation | Seeded config + script a reader can run | Logged metrics per run |
| Onboard timing | Benchmark script for the compute stack | Power/rate measurement method + logs |
| Real-robot success rate | Not rerunnable by a reader | Trial log, criterion, resets, failure counts |
| Sim-to-real transfer | Sim side rerunnable | Paired real logs + the stated gap |

Marking a real-robot claim as if a reader could "just rerun it" is a recognizable IROS overstatement;
name it auditable and make the audit trail complete instead.

## The hardware specification ledger

A result that depends on a specific robot must specify it: platform and revision, sensor models and
firmware, actuator limits, onboard computer, and power budget. Two labs with "the same" robot but
different firmware or calibration can see different behavior, so the ledger is part of the claim, not
metadata.

## Vignette: a manipulation-reliability paper

Consider a paper reporting grasp success on unseen objects. Its reproducibility spine: the object set and
where to get it, the calibration and gripper parameters, the success criterion and reset procedure, the
per-object trial logs, and one honest sentence about the objects where the method fails and why — plus a
rerunnable simulation of the grasp planner so the algorithmic core is executable even if the robot is not.

```text
Availability statement skeleton:
  Code: <released? which parts? link at acceptance>
  Data/objects: <provenance + license, or access route>
  Logs: <representative bags for the reported trials>
  Withheld: <what + why: proprietary/safety/licensing>
  Reproduce-in-principle: <what a reader without the robot can still run>
```

## Output format

```text
[Claim inventory] <claim -> rerunnable | auditable + location>
[Hardware ledger] complete / gaps: <list>
[Sim-to-real] gap stated? / implied-zero risk?
[Availability] honest / overpromised / missing
[Body fixes] <what must appear in the paper body>
```
