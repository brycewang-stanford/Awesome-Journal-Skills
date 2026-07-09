---
name: sigmetrics-artifact-evaluation
description: Use when packaging an ACM SIGMETRICS artifact for the ACM Artifact Review and Badging scheme (Artifacts Available, Evaluated Functional and Reusable, Results Reproduced), covering what performance-evaluation evaluators check first (does the simulation regenerate the figures and match the analysis?), DOI-issuing archives, evaluator-proof documentation, and confirming whether an artifact track runs this cycle.
---

# SIGMETRICS Artifact Evaluation

Use this for artifact/reproducibility packaging. SIGMETRICS sits in the ACM ecosystem and, where an
artifact track runs, follows the **ACM Artifact Review and Badging** scheme. Two things to
internalize: badges are earned by evaluators actually using your package, and — distinctively for
SIGMETRICS — the package usually has to let an evaluator **regenerate the figures from a seeded
simulation and see them match the analytic prediction**, not only run a tool. Confirm on the current
cycle whether a formal artifact track exists and its timing (**待核实**).

## The ACM badges (verify the current set and names)

| Badge | What it certifies | What earns it |
|---|---|---|
| Artifacts Available | The artifact is permanently, publicly retrievable | Deposit in a DOI-issuing archive (Zenodo, figshare, Software Heritage) |
| Artifacts Evaluated - Functional | The artifact runs and does what the paper says | A clean-machine install, a demo run of the simulator, documented expected outputs |
| Artifacts Evaluated - Reusable | Others can build on it | The Functional bar plus careful docs, structure, and licensing |
| Results Reproduced | An evaluator reproduced the paper's key results | A turnkey path from the artifact to the headline figures/numbers (and the analytic overlay) |

Available is a low-cost, high-value badge (archive the package); Functional/Reusable/Reproduced
require the evaluator's own run to succeed, so the failure mode is "did not run / figures did not
match on their machine," never "the theorem was weak."

## What performance-evaluation evaluators open first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| An analytic bound + simulation | The script that regenerates the analysis-vs-simulation figure | Figure hard-coded; simulator does not actually produce the plotted curve |
| A measurement study | The scripts that turn the trace into the paper's tables | Numbers in the PDF that no script reproduces; trace missing |
| A scheduling/queueing policy | The seeded simulator and its steady-state handling | Non-deterministic runs; no seeds; warm-up not handled |
| A learning-for-systems result | Code plotting empirical regret against the proven bound | Requires unavailable data; guarantee not empirically checked |

Assume an evaluator gives your package a bounded time budget on a clean machine. Design for the
first ten minutes to succeed: a small demo that regenerates one headline figure quickly.

## Packaging plan

```text
[Container]   ship a Dockerfile or a pinned environment (requirements/lockfile); avoid
              "install these 40 things by hand"
[README]      one-screen orientation: what the model is, how to install, how to run the simulator
              demo, how to regenerate each figure, expected runtime and outputs
[Mapping]     an explicit table: paper claim/figure -> script -> expected result (incl. the
              analytic overlay it should match)
[Simulator]   seeded, steady-state-aware; a fast demo config and the full (slow) config
[Data]        the processed trace/dataset (or documented access), not just the collection query
[Proofs]      the derivation appendix, so the analytic side is checkable alongside the code
[License]     an OSI-approved license so the artifact can be badged Reusable
[Archive]     deposit in a DOI-issuing repository for the Available badge
```

## Anonymized review artifact vs. badge artifact

- **At submission:** the artifact is anonymized for the paper's reviewers — no owner strings,
  cluster paths, group names, or identity-revealing trace provenance (Operational Systems Track
  excepted).
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-issuing
  archive; this is the version the badges attach to and the POMACS camera-ready cites.

## Worked vignette: packaging a scheduling-policy paper

A paper contributes a scheduling theorem and a trace-driven evaluation. To target Reusable and
Reproduced: ship a Docker image with the simulator pre-built; a `run_demo.sh` that regenerates the
analysis-vs-simulation figure on a small config in under a minute; a `reproduce/` directory whose
scripts regenerate each table and the trace-driven comparison from logged runs; a
claim-to-figure-to-script mapping in the README; the processed trace with pinned provenance; the
proof appendix; and an MIT/Apache license. State honestly which figures are turnkey and which need
the full (slow) simulation sweep.

## Calibration

- Whether an artifact/reproducibility track runs a given cycle, its badges, timing, and whether it
  is mandatory or optional — all cycle-volatile; confirm on the current call (**待核实**).
- For POMACS, badges are typically pursued around/after acceptance; do not conflate the artifact
  process with the paper's shepherding.

## Output format

```text
[Target badges] Available / Functional / Reusable / Reproduced
[Artifact role] anonymized review artifact / public badge artifact
[Contents] <model/simulator/trace/proofs/provenance/license>
[Ten-minute test] does install + demo regenerate one headline figure on a clean machine? yes/no
[Claim mapping] <claim/figure -> script -> expected result (matches analysis?) present? yes/no>
[Fixes before upload] <ordered list>
```
