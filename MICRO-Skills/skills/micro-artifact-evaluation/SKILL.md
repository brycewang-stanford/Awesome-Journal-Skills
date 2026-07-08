---
name: micro-artifact-evaluation
description: Use when preparing a MICRO artifact for post-acceptance evaluation — packaging simulators, configs, traces, and scripts so evaluators can regenerate the paper's figures, targeting the ACM Available/Functional/Reproducible badges, handling licensed workloads and long simulations, and earning the optional artifact appendix.
---

# MICRO Artifact Evaluation

MICRO runs artifact evaluation **after acceptance**: authors of accepted papers are
invited to submit artifacts, an Artifact Evaluation Committee reviews them, and
successful papers carry ACM badges in the proceedings. Anchors here are the MICRO
2025 AE pages (`micro58/submit/artifacts.php`, verified 2026-07-08); the 2026
edition's AE page and calendar are 待核实 — expect the same architecture, verify
the dates.

## Badge targets and what each demands

| Badge (ACM) | Bar | Microarchitecture-specific gotcha |
|---|---|---|
| Artifact Available | Deposited on a **public archival repository** — Zenodo, FigShare, Dryad named in 2025 | A GitHub repo alone fails; it is not archival. Deposit a tagged snapshot, keep GitHub as the living mirror |
| Artifact Functional | Documented, complete, exercisable | Simulator builds on a clean machine — your decade of dotfiles is not in the package |
| Results Reproducible | Evaluators regenerate the paper's main claims | Simulation *time* is the enemy: full SPEC runs take days-weeks; provide a subset path |

Papers passing AE also earned, in 2025, the right to a **two-page artifact
appendix in the camera-ready, free of charge** — reproduction instructions
published with the paper.

## The time-budget problem is the design problem

A MICRO artifact's hardest constraint is that cycle-level simulation is slow and
evaluators have finite weeks. Design three nested entry points:

```text
make smoke      # ~30 min: one workload region, one config — proves the plumbing
make key        # ~1 day:  the headline figure (Fig. 3) on a representative subset
make full       # ~1 week: every figure, every sweep — for the determined evaluator
```

Document expected runtime and disk for each. State which paper claims each tier
supports. An evaluator who finishes `make key` in a day and sees Fig. 3 appear is
an evaluator who awards the badge.

## Package inventory

- **Top-level README:** paper title, badge targets, the three entry points, a
  figure-to-command map ("Fig. 5 ⇐ `make fig5`, ~6 h"), hardware/software
  requirements (the 2025 process asked for these to route artifacts to suitable
  evaluators).
- **Environment capture:** container image or pinned build script for the
  simulator toolchain; host assumptions stated (cores, RAM — parallel sims are
  memory-hungry).
- **Everything `micro-reproducibility` pinned:** simulator commit + patches,
  config files for baseline/mechanism/ablations, manifests, plotting scripts.
- **Raw stats for the paper's figures**, so evaluators can verify plots even
  before re-simulating — this alone often satisfies partial reproduction.

## Licensed and unshippable inputs

- **SPEC CPU binaries/inputs cannot be redistributed.** Ship the trace-generation
  recipe (tool version, SimPoint parameters, flags) plus, where licensing allows,
  the derived traces; otherwise document how an evaluator with a SPEC license
  regenerates them, and rest the Reproducible claim on shippable workloads.
- **Proprietary RTL or PDK data** (synthesis libraries are NDA'd): report the flow
  and constraints, mark the RTL numbers as not independently reproducible, and
  scope the badge request to the simulation results. Honest scoping beats a
  failed evaluation.
- **FPGA/silicon dependencies:** offer remote access if institutionally possible,
  or pre-recorded measurement logs with the analysis scripts.

## Common failure modes, ranked by frequency of pain

| Failure | Root cause | Prevention |
|---|---|---|
| Build breaks on evaluator machine | Undeclared host dependency (library, kernel version, python package) | Container or lockfile; test in a fresh VM |
| Numbers regenerate but differ slightly | Simulator nondeterminism or a config drifted after paper freeze | Determinism check + tagged commit at submission (`micro-reproducibility`) |
| Evaluator cannot find which command makes which figure | README written for the authors, not strangers | Figure-to-command map, tested by a labmate who did not build the artifact |
| Full run exceeds the AE window | No tiering | `smoke`/`key`/`full` entry points with honest runtime labels |
| Licensed inputs block everything | SPEC traces shipped nowhere, no fallback | Shippable-workload subset carrying the Reproducible claim |

A dry run fixes four of the five: hand the package to someone outside the project
with only the README, and watch — silently — where they stall.

## Working with evaluators

AE is collaborative, not adversarial: expect questions, fix breakage fast, and
keep a changelog of package updates during the window. Budget author-time in
August–September (the window overlaps the September 11 camera-ready in the 2026
calendar — plan both, see `micro-camera-ready`). The final deposit that carries
the Available badge must be the *fixed* package, re-uploaded to the archival
repository with a new version DOI.

## Minimal artifact layout that evaluators navigate well

```text
artifact/
├── README.md            # badges sought, 3 entry points, figure-to-command map
├── Dockerfile           # or install.sh with pinned versions
├── Makefile             # smoke / key / full targets
├── configs/             # baseline.json, mechanism.json, ablations/
├── manifests/           # one YAML per experiment batch (micro-reproducibility)
├── stats-paper/         # the raw stats behind every published figure
├── plots/               # scripts: stats -> exact paper figures
├── traces/RECIPE.md     # how to regenerate licensed traces (nothing licensed inside)
└── LIMITS.md            # known fidelity gaps; claims stay inside them
```

Two conventions matter more than the tree itself: the README's first screen must
answer "what do I run first and how long will it take," and nothing an evaluator
needs may require reading source code to discover. If the paper linked an
anonymized repo at submission (`micro-supplementary`), this layout should already
exist — AE prep is then a de-anonymization pass plus the archival deposit.

## Output format

```text
[Badge plan] Available: deposit target · Functional: yes/no · Reproducible: scoped to <claims>
[Entry points] smoke/key/full runtimes measured on clean machine: <times>
[Figure map] figures with regenerate-commands: N/M
[Unshippables] licensed inputs + documented workaround each
[Environment] container/build-script tested from scratch: yes / no
[Calendar] AE dates vs camera-ready overlap plan (2026 dates 待核实)
```
