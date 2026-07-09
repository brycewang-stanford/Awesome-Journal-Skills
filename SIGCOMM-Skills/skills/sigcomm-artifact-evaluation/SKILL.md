---
name: sigcomm-artifact-evaluation
description: Use when packaging an ACM SIGCOMM paper's code, traces, topologies, and configuration for the artifact-evaluation committee — choosing ACM badges (Artifacts Available, Evaluated, Results Reproduced) as claim calibration, building downscaled topologies and trace substitutes, and making a networking testbed result rebuildable by a reviewer.
---

# SIGCOMM Artifact Evaluation

Use this for the post-acceptance artifact submission. SIGCOMM helped establish artifact
evaluation in networking, and the venue's "runnable papers" culture sets a high bar: a
committee attempts to build and, where a badge requires it, reproduce your headline result.
Reopen the current Call for Artifacts for this edition's exact badge set and dates (待核实 for
2026).

## Badge selection is claim calibration

Choose the badges you can honestly support; the badge is a promise about what a stranger can
verify, not a participation ribbon.

| ACM badge | What it promises | What the AEC will do |
|---|---|---|
| Artifacts Available | Permanent public retrieval via an archival DOI | Confirm the archive resolves and is complete |
| Artifacts Evaluated (Functional) | The artifact builds and runs as documented | Follow your README end to end on their setup |
| Results Reproduced | The paper's main results follow from the artifact | Re-run to obtain the headline numbers within tolerance |

Aim the highest badge at the result you most want believed, and be candid where hardware or
scale makes full reproduction infeasible.

## The networking-specific hard part

Generic artifact tooling cannot judge what SIGCOMM evaluators care about most: a result
measured on a rack of switches or a wide-area testbed rarely rebuilds on a laptop. Plan for
the gap:

- **Downscale the topology.** Ship a small emulated or Mininet-style topology that reproduces
  the *mechanism's* behavior, with a documented map from the downscaled run to the paper's
  full-scale figure.
- **Substitute the trace legally.** If the production trace cannot ship, provide a synthetic
  or public-trace substitute with the same statistical character, and state exactly which
  figures used which input.
- **Pin the environment.** Kernel and NIC features, switch firmware or programmable-data-plane
  toolchain versions, and clock/timestamp sources all move results; record them.
- **Expose the run count.** Every reported percentile needs its replication count and the
  seed or workload driver, or the tail cannot be reproduced.

## What evaluators open first

```text
artifact/
  README            # 5-minute smoke run FIRST, then the full path
  smoke/            # one command -> one small figure that proves it runs
  topology/         # downscaled + a map to the paper's full-scale setup
  traces/           # substitute inputs + provenance + which-figure-uses-what
  configs/          # exact parameters per experiment
  scripts/          # regenerate each figure from logged results
  results/          # logged raw outputs the plots are built from
  ENVIRONMENT.md    # kernel/NIC/switch/toolchain versions, hardware
```

Assume the evaluator runs the smoke path first and stops if it fails, so make one command
produce one convincing small figure before anything else is polished.

## Vignette: packaging a data-center transport result

A paper reports a tail-FCT win on a 128-server testbed. Turnkey plan: a Mininet topology that
reproduces the incast dynamic at small scale; a synthetic RPC workload matching the trace's
flow-size distribution; a driver that emits the FCT distribution over 20 replays; and a script
that plots the 99th percentile directly from logged results so the artifact figure and the
paper figure cannot diverge. The README states plainly which numbers are full-scale (paper)
and which are downscaled (artifact).

## Output format

```text
[Badges sought] available / functional / reproduced — each justified
[Smoke path] one command -> one figure? yes/no
[Topology] full-scale -> downscaled map documented
[Trace handling] shipped / substituted (+ provenance) / described
[Environment] kernel/NIC/switch/toolchain pinned
[Fixes before AEC upload] <ordered list>
```
