---
name: icra-reproducibility
description: Use when hardening an ICRA paper's reproducibility — specifying robot platform, firmware, ROS and driver versions, control rates, and sensor calibration; logging rosbags and seeds; separating what others can rerun (code, sim) from what they can only audit (your hardware trials); and writing honest availability statements.
---

# ICRA Reproducibility

Reproducibility at a robotics conference means something different than at an ML
venue: no reader can rerun your hardware trials without your robot, your room,
and your objects. The achievable standard is therefore two-tier — **rerunnable**
(code, simulation, analysis) and **auditable** (hardware evidence logged well
enough that a skeptic can verify you did what you claim). ICRA papers earn trust
by being explicit about which tier each result sits in.

## The specification ledger

A robotics result is unreproducible if the platform is underspecified. The paper
(body, since there is no appendix escape) plus released materials should pin:

| Layer | Must specify | Example of "enough" |
|---|---|---|
| Robot | model, DOF, payload, firmware version | "UR5e, PolyScope 5.11" |
| End effector | model, mods, wear state if relevant | "Robotiq 2F-85, stock pads" |
| Sensors | model, resolution, rate, mounting frame | "D435i @ 640×480, 30 Hz, wrist" |
| Compute | on-board vs off-board, GPU, latency path | "off-board 3080, 5G-free wired" |
| Middleware | ROS distro, key package versions | "ROS 2 Humble, MoveIt 2.5.4" |
| Control | loop rates, gains or their source | "impedance @ 500 Hz, gains in repo" |
| Calibration | method + residual error | "hand-eye via [ref], 1.8 mm RMS" |
| Objects/scenes | identity, source, dimensions | "YCB subset listed in Tab. II" |

Standard object sets (YCB and similar) exist precisely so that "graspable
household objects" can be a checkable claim; use them or publish the object
specs.

## Logging: the rosbag is the lab notebook

- Record every hardware session — including failed ones — with topic-complete
  rosbags (or vendor-equivalent logs) plus an untouched camera view.
- One log per trial, named by protocol: `trial_<cond>_<idx>_<date>.bag`; the
  analysis pipeline should consume these logs, so paper numbers regenerate from
  raw data with one command.
- Keep a session sheet: date, operator, firmware state, anomalies. Two months
  later, this distinguishes "the gripper was recalibrated between Tables II and
  III" from unexplainable drift.
- The video attachment should be cut from these recorded sessions, which
  guarantees footage corresponds to logged, reported trials.

## Determinism where it exists, honesty where it doesn't

Hardware trials are not seed-reproducible — contact, cables, lighting, and
thermal drift see to that. Split the claims accordingly:

- **Deterministic tier:** training runs, simulation experiments, and analysis
  scripts get pinned seeds, pinned dependency versions, and containerized
  environments. State seeds and repetition counts.
- **Stochastic tier:** hardware trials get *protocol* reproducibility — the
  documented procedure another lab could follow — plus dispersion reporting.
- Never write "results are fully reproducible" over a hardware table; write
  "code and simulation reproduce Tables I-II; hardware protocol and logs for
  Tables III-IV are released for audit."

## Release scaffold

```text
repo/
├── README.md            # claim → command map (Table III = run_hw_analysis.sh)
├── env/                 # Dockerfile or rosdep/lockfiles, pinned
├── sim/                 # simulation experiments, seeds fixed
├── control/             # controllers/planners as ROS packages
├── hw_protocol.md       # step-by-step trial procedure, success criterion,
│                        #   reset procedure, safety notes
├── logs/                # rosbags or download script (size!), session sheets
├── analysis/            # regenerates every figure/table from logs/
└── video/               # raw clips ↔ trial IDs mapping
```

Anonymize the repository for review under the double-anonymous policy (2026
cycle onward): anonymized hosting or an artifact stripped of names — an org URL
is an identity leak (see `icra-submission`).

## Compute and latency reporting

Robotics adds a real-time dimension absent from ML reproducibility norms:

- Report where each computation ran (on-board CPU/embedded GPU vs off-board
  workstation) and the link between them; an off-board 3090 over gigabit wire
  is a materially different system than on-board inference.
- State end-to-end latency per pipeline stage (sensing → perception → decision
  → actuation) at least once; "runs in real time" is unverifiable without it.
- Training compute (GPU-hours, hardware) belongs in the paper for learned
  components — cheap to report, increasingly expected by review forms.

## Availability statement patterns

Honest, specific statements outperform boilerplate promises:

- "Code, simulation environments, and trial logs: <link> (anonymized for
  review; public on acceptance)."
- "The gripper design files are released; the arm is commercial (UR5e)."
- "Raw rosbags total 1.2 TB; per-trial extracted features and a 40 GB sample
  are hosted, full logs on request."
- Avoid: "code will be released upon publication" with nothing at review time —
  reviewers discount unverifiable promises, and some cycles ask availability
  questions directly on the review form (verify the current form).

## Pre-submission reproducibility pass

1. Specification ledger complete in-paper (table above, compressed)?
2. Every reported number regenerates from logs via one documented command?
3. Seeds/versions pinned for the deterministic tier; container builds clean?
4. Hardware protocol written so a stranger could run trial 1 tomorrow?
5. Release scaffold anonymized; links leak-checked?
6. Availability statement matches what actually exists today?

## Output format

```text
[Tier split] rerunnable: <tables/figs> | auditable: <tables/figs>
[Spec ledger] missing rows: <list or none>
[Log coverage] trials logged <n>/<n>, analysis regenerates: y/n
[Determinism] seeds/versions pinned for sim+training: y/n
[Release] scaffold complete? anonymized? size plan?
[Statement] honest-specific / boilerplate-risk — rewrite: <line>
```
