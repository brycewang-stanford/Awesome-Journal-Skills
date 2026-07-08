---
name: eurosys-artifact-evaluation
description: Use when preparing a EuroSys artifact for the sysartifacts-run evaluation — choosing among the Available, Functional, and Reproduced badges, timing the post-notification artifact submission, building for an evaluator on foreign hardware, and aiming at the Gilles Muller Best Artifact Award rather than a minimal pass.
---

# EuroSys Artifact Evaluation

Use this when an accepted (or optimistically, submitted) EuroSys paper has code,
data, or hardware behind its claims. EuroSys artifact evaluation is organized
with the **sysartifacts** community (`sysartifacts.github.io/eurosys2026/`,
rendered 2026-07-08); it is optional, happens **after acceptance notification**,
and awards up to three badges that appear on the published paper. The EuroSys
2027 call for artifacts was not yet verifiable on 2026-07-08 — 待核实 before
committing to dates or badge criteria.

## The three-badge menu

Authors declare which badges they want; the AEC grants zero to three.

| Badge | EuroSys 2026 criterion (rendered) | Typical blocker |
|---|---|---|
| Available | Artifact retrievable from a public, DOI-backed archive | "It's on our GitHub" — mutable, not archival |
| Functional | Complete, documented, exercisable as described | Undocumented cluster assumptions; missing inputs |
| Reproduced | Paper's main claims independently re-obtained | Experiments needing hardware the AEC cannot access |

Sensible combinations tracked by the process: all three for ordinary software
artifacts; Available + Functional for datasets or custom-environment systems;
Functional + Reproduced when the artifact itself cannot be published. Pick the
target set *before* packaging — each badge changes what you build.

## Design for the evaluator you will actually get

The AEC member is a systems student on hardware you did not choose, with a fixed
time budget and no context beyond your paper. EuroSys evaluations have run a
kick-the-tires phase with author interaction in past cycles (待核实 for the
current one), but the artifact should survive with zero interaction:

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

EuroSys names an artifact prize — the **Gilles Muller Best Artifact Award**
(EuroSys 2023 awards page; the award honors the late Gilles Muller, whose
EuroSys '08 Coccinelle work won a Test-of-Time award). Committees remember
artifacts that reproduce headline numbers unattended; that reputation follows
the system into follow-up papers and adoption.

## Timeline coupling with the paper lanes

- Start the artifact during review, not after notification: the gap between
  acceptance and artifact submission is weeks, and it overlaps camera-ready
  work that wants the same people.
- Spring-cohort papers (notified in late August for 2027) have a long runway
  to the April conference; fall-cohort papers (notified late January) run
  artifact evaluation and camera-ready nearly concurrently — 待核实 the
  edition's actual AE dates, and assign separate owners if in the fall cohort.
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
[待核实] <current call-for-artifacts dates, badge wording, kick-the-tires>
```
