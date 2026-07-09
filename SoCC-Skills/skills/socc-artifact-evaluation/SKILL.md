---
name: socc-artifact-evaluation
description: Use when packaging an ACM SoCC artifact for the ACM Artifact Review and Badging scheme (Artifacts Available, Evaluated Functional and Reusable, Results Reproduced), covering what a cloud-systems evaluator checks first, reproducing tail-latency and cost results on a testbed, DOI-issuing archives, and the fact that whether SoCC runs a dedicated artifact-evaluation track for a given edition must be verified.
---

# SoCC Artifact Evaluation

Use this for artifact preparation. SoCC — as an ACM venue — follows the **ACM Artifact Review and
Badging** scheme where an edition offers evaluation. **First, verify whether the current SoCC
edition runs a dedicated artifact-evaluation track, and which badges it offers** — unlike some
sibling systems flagships that run a standing AE process, SoCC's artifact track and badge set are
decided per edition and are **待核实** as of 2026-07-09. The advice below applies once the edition's
call confirms evaluation.

Two things to internalize: badges are earned by evaluators actually **reproducing** your cloud
results, and the review artifact (anonymized, for the paper's reviewers) is not the same deliverable
as the badge artifact (de-anonymized, permanently archived).

## The ACM badges (verify the current set and names)

| Badge | What it certifies | What earns it for a cloud paper |
|---|---|---|
| Artifacts Available | The artifact is permanently, publicly retrievable | Deposit in a DOI-issuing archive (Zenodo, figshare, Software Heritage) |
| Artifacts Evaluated - Functional | The artifact runs and does what the paper says | A documented testbed setup, a workload replay, and expected outputs |
| Artifacts Evaluated - Reusable | Others can build on it | Functional plus careful docs, structure, licensing, and a portable harness |
| Results Reproduced | An evaluator reproduced the paper's key results | A turnkey path from the artifact to the headline throughput/tail/cost numbers |

Available is a low-cost, high-value badge (archive the package); Functional/Reusable/Reproduced
require the evaluator's own run to succeed, so the failure mode is always "did not run on their
testbed," never "the idea was weak."

## What a cloud-systems evaluator opens first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A cloud system/mechanism | The README and one setup+run command | Undocumented cluster assumptions; only-runs-on-authors'-testbed |
| A measurement/trace study | The scripts that turn the trace into the paper's figures | Numbers in the PDF no script reproduces; trace missing |
| A scheduling/serverless result | The workload generator + the tail/cost measurement scripts | Only the mean reproduces; tail and cost cannot be regenerated |
| A large-scale deployment | A scaled-down but faithful reproduction path | Requires a proprietary cluster; no smaller-scale replay |

Assume an evaluator has a bounded time budget and **cannot** reserve your 200-node cluster. Provide
a **scaled-down reproduction** that still regenerates the shape of the tail and cost results, plus a
clear statement of what needs full scale.

## Packaging plan

```text
[Environment] ship a Dockerfile / pinned environment AND a testbed description (node counts,
              instance types, OS, kernel) so a run is reproducible
[Workloads]   the workload generator or the (anonymized, then released) trace, not just a pointer
[README]      one-screen orientation: what it is, how to set up, how to run a small demo, how to
              reproduce each figure, expected runtime and outputs
[Mapping]     an explicit table: paper claim -> script -> expected result (incl. tail and cost)
[Scaled path] a small-scale reproduction that runs without the full cluster
[Provenance]  commit SHAs, trace extraction dates, instance types, seeds, run counts
[License]     an OSI-approved license so the artifact can be badged Reusable
[Archive]     deposit in a DOI-issuing repository for the Available badge
```

## Anonymized review artifact vs. badge artifact

- **At submission:** the artifact is anonymized for the paper's reviewers — no cluster names,
  provider hints, owner strings, or identity-revealing trace provenance, and no live repository that
  discloses authors.
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-issuing
  archive; this is the version any artifact evaluators badge and the camera-ready cites.

## Worked vignette: packaging an autoscaler + trace study

A paper contributes a tail-aware autoscaler and a measurement of the cost-tail gap. To target
Reusable and Reproduced: ship a Docker image with the controller pre-built; a `run_demo.sh` that
replays a short trace slice on a few nodes in minutes and prints p99 and instance-seconds; a
`reproduce/` directory whose scripts regenerate each figure from logged runs; a claim-to-script
mapping table in the README; the (released) trace-replay harness with pinned SHAs; and an
MIT/Apache license. State honestly which figures are turnkey at small scale and which need the full
testbed.

## Calibration

- **Confirm the track exists** for this edition before planning; SoCC's AE track and badge set are
  **待核实** per cycle.
- Reproducing **tail and cost**, not just the mean, is the cloud-specific bar; design the package so
  an evaluator can regenerate them.
- Badge names, the exact set offered, and whether evaluation is single- or double-anonymous vary by
  edition — confirm on the current call.

## Output format

```text
[Track status] SoCC AE track confirmed for this edition? yes/no/待核实
[Target badges] Available / Functional / Reusable / Reproduced
[Artifact role] anonymized review artifact / public badge artifact
[Contents] <system/workloads/trace/scripts/testbed-desc/provenance/license>
[Small-scale test] does setup + demo reproduce tail+cost shape without the full cluster? yes/no
[Claim mapping] <claim -> script -> expected result (incl. tail/cost) present? yes/no>
[Fixes before upload] <ordered list>
```
