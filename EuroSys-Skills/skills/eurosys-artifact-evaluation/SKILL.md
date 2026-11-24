---
name: eurosys-artifact-evaluation
description: Use when preparing a EuroSys artifact for the sysartifacts-run evaluation — choosing among the Available, Functional, and Reproduced badges, timing the post-notification artifact submission, building for an evaluator on foreign hardware, and aiming at the Gilles Muller Best Artifact Award rather than a minimal pass.
---

# EuroSys Artifact Evaluation

Use this when an accepted (or optimistically, submitted) EuroSys paper has code,
data, or hardware behind its claims. EuroSys artifact evaluation is organized
with the **sysartifacts** community (`sysartifacts.github.io/eurosys2027/`,
re-verified 2026-11-24); it is optional, **single-blind** (evaluators know the authors),
cooperative (authors may fix problems found during evaluation), happens **between
acceptance notification and camera-ready**, and awards up to three badges that appear on
the published paper.

EuroSys 2027 AE dates (all AoE):

| Cycle | Artifact due | Kick-the-tires ends | Functional/Reproduced decisions | Archival for Available | Camera-ready |
|---|---|---|---|---|---|
| Spring | August 31, 2026 | September 8, 2026 | September 21, 2026 | September 23, 2026 | September 25, 2026 |
| Fall | February 8, 2027 | February 16, 2027 | March 1, 2027 | March 3, 2027 | March 5, 2027 |

(The CFP marks the fall artifact dates "to be confirmed".) AE chairs: Redha Gouicem and
Solal Pirelli.

## The three-badge menu

Authors declare which badges they want; the AEC grants zero to three.

| Badge | EuroSys criterion (sysartifacts checklist) | Typical blocker |
|---|---|---|
| Available | Artifact retrievable from a public, DOI-backed archive | "It's on our GitHub" — mutable, not archival |
| Functional | Complete, documented, exercisable as described | Undocumented cluster assumptions; missing inputs |
| Reproduced | Paper's main claims independently re-obtained | Experiments needing hardware the AEC cannot access |

EuroSys 2027 allows exactly **three combinations**: all three for the vast majority of
software artifacts (and hardware where possible); Available + Functional for datasets or
custom-environment systems; Functional + Reproduced when the artifact itself cannot be
published. A first-target artifact may be downgraded to one of the other two if the
availability or reproducibility evaluation fails; other combinations cannot be requested. Pick the
target set *before* packaging — each badge changes what you build.

## Design for the evaluator you will actually get

The AEC member is a systems student on hardware you did not choose, with a fixed
time budget and no context beyond your paper. EuroSys 2027 runs a short
**kick-the-tires** phase in which at least one author must be reachable by email and
answer promptly, but the artifact should survive with zero interaction:

- One top-level document mapping each paper claim to a command and an expected
  output range — claims first, directory tour second.
- Pin the environment: container image or lockfile, exact kernel/library
  expectations stated, hardware floor declared honestly.
- Scale knobs: a minutes-long subset run for functionality, a full run for
  reproduction, clearly separated.
- Where results are hardware-sensitive (NUMA layout, NIC model, device speeds),
  state the expected deviation instead of letting the evaluator guess.

```text
artifact/
├── README.md          # claim -> experiment -> command -> expected result
├── Dockerfile         # or environment.lock + install script
├── run_functional.sh  # ~15 min, exercises every component
├── run_full.sh        # regenerates Figs 5-9, prints runtime estimate
├── data/              # inputs or fetch script with checksums
└── expected/          # reference outputs + tolerance notes
```

## Archival step for the Available badge

Push the evaluated snapshot — not a later fix — to a DOI-minting archive
(Zenodo is the norm in this community), record the DOI in the camera-ready
availability section, and keep the GitHub repository as the living mirror. A
tag on a mutable host does not satisfy the badge's permanence requirement.

## Why aim above the minimum

EuroSys names an artifact prize. EuroSys 2027's AE page offers a **Distinguished
Artifact** award to artifacts that earn all available badges and best exemplify
reusability and reproducibility; earlier editions gave it as the **Gilles Muller Best
Artifact Award** (EuroSys 2023 awards page; the award honors the late Gilles Muller,
whose EuroSys '08 Coccinelle work won the 2018 Test-of-Time award). Committees remember
artifacts that reproduce headline numbers unattended; that reputation follows
the system into follow-up papers and adoption.

## Timeline coupling with the paper lanes

- Start the artifact during review, not after notification: the gap between
  acceptance and artifact submission is weeks, and it overlaps camera-ready
  work that wants the same people.
- For EuroSys 2027 both cohorts run AE and camera-ready back to back: ten days from
  notification to artifact submission, about five weeks to camera-ready (spring:
  August 21 → August 31 → September 25, 2026; fall: January 29 → February 8 → March 5,
  2027). Assign separate owners for the artifact and the camera-ready.
- Freeze the artifact snapshot when the camera-ready evidence freezes;
  divergence between the published numbers and the archived artifact is the
  most embarrassing discrepancy the process can surface.

## Documentation pyramid

Write three layers, in this order of effort:

1. **The claims map** (one page): paper claim → command → expected result →
   tolerated deviation. This is what gets read.
2. **The environment contract** (half a page): image or lockfile, hardware
   floor, network assumptions, run times. This is what prevents failed setups.
3. **Everything else** (as needed): design notes, extension hooks, dataset
   documentation. This is what gets skimmed, if opened at all.

An artifact with only layer 3 — however thorough — evaluates as
undocumented, because the evaluator's clock runs out before the claims map
they needed emerges from the prose.

## Failure patterns the AEC reports

- Hard-coded paths and hostnames from the authors' cluster.
- The "works in our CI" artifact whose dataset download link needs a VPN.
- Reproduction scripts that emit numbers but never say which figure they rebuild.
- A 40-page wiki where a two-page claims-to-commands map was needed.

## Output format

```text
[Badge target] Available / +Functional / +Reproduced (with rationale)
[Evaluator path] <first command an AEC member runs, and its runtime>
[Claim coverage] <paper claim -> script -> expected output>
[Hardware honesty] <what the AEC cannot reproduce, and the declared fallback>
[Archival plan] <DOI host, snapshot timing relative to camera-ready>
[Dates] <artifact due / kick-the-tires / decisions / archival for this cohort>
```
