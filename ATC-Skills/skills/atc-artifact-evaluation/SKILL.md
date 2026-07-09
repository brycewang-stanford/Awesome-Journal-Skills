---
name: atc-artifact-evaluation
description: Use when packaging an ATC (ACM SIGOPS Annual Technical Conference, formerly USENIX ATC) artifact for the USENIX-lineage evaluation scheme — earning the Artifacts Available, Artifacts Functional, and Results Reproduced badges from the Artifact Evaluation Committee on its separate post-acceptance deadline, with evaluator-proof documentation and a turnkey path to the paper's numbers.
---

# ATC Artifact Evaluation

Use this for the artifact track. ATC follows the shared **USENIX/SIGOPS** artifact-evaluation scheme:
an **Artifact Evaluation Committee (AEC)** runs a **separate, post-acceptance** process through
HotCRP and awards up to three badges — **Artifacts Available**, **Artifacts Functional**, and
**Results Reproduced**. Two things to internalize: badges are earned by evaluators **actually using**
your package, and the review artifact (anonymized, for the paper's reviewers) is not the same
deliverable as the badge artifact (de-anonymized, permanently archived). ATC's artifact culture is
strong and high-participation — for USENIX ATC '25, most evaluated artifacts earned Functional and a
large majority earned Reproduced.

## The three badges (verify the current set and names)

| Badge | What it certifies | What earns it |
|---|---|---|
| Artifacts Available | The artifact is permanently, publicly retrievable | Deposit in a DOI-issuing archive (Zenodo, figshare, Software Heritage) |
| Artifacts Functional | It is documented, complete, and exercisable — it runs and does what the paper says | Clean-machine install, a demo, scripts + data to run the experiments |
| Results Reproduced | An evaluator reproduced the paper's main results | A turnkey path from the artifact to the headline figures/tables |

Available is low-cost, high-value (archive the package). Functional and Reproduced require the
evaluator's own run to succeed, so the failure mode is always "did not run on their machine," never
"the idea was weak."

## What AEC evaluators open first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A built system / mechanism | The README and one install/run command | Undocumented deps; only-works-on-authors'-hardware |
| A performance result | The scripts that turn a run into the paper's figures | Numbers in the PDF no script reproduces |
| A result needing specific hardware (RDMA/NVMe/NIC) | The documented host requirements + a small-scale mode | Requires unavailable hardware; no fallback |
| A trace-driven study | The traces + the processing scripts | Query shipped, data missing; provenance unpinned |

Assume the evaluator has a bounded time budget on a clean machine and may **lack your exact
hardware**. Design the first ten minutes to succeed and provide a reduced-scale path.

## Packaging plan

```text
[Container]   a Dockerfile or pinned environment; document any host/hardware the container cannot abstract
[README]      one-screen orientation: what it is, install, run the demo, reproduce each claim, expected runtime/outputs
[Mapping]     an explicit table: paper claim -> script -> expected figure/table -> tolerance
[Scale]       a full-scale path AND a small-scale mode for evaluators without the hardware
[Data]        the traces/datasets themselves (or durable documented access), not just the query
[Provenance]  kernel/OS versions, hardware models, commit SHAs, workload seeds, run counts
[License]     an OSI-approved license so the artifact can be shared and reused
[Archive]     deposit in a DOI-issuing repository for the Available badge
```

## Anonymized review artifact vs. badge artifact

- **At submission (review):** anonymized for the paper's double-blind reviewers — no owner strings,
  cluster hostnames, lab/product names, or identity-revealing links, and no live repo that discloses
  authors (see `atc-reproducibility`).
- **After acceptance (badge):** replace anonymized placeholders with the public, licensed,
  DOI-issuing archive; this is the version the AEC badges and the camera-ready cites.

## Worked vignette: a storage-cache policy + measurement

A paper contributes a flash-cache admission policy and a testbed evaluation. To target Functional and
Reproduced: ship a container with the modified server pre-built; a `run_demo.sh` that exercises the
policy on a bundled trace sample in a minute; a `reproduce/` directory whose scripts regenerate each
figure from logged runs; a claim-to-script mapping with tolerances in the README; the
production-derived trace sample (with pinned provenance) plus documentation of the full trace's
access; a documented note that the full-scale p99 result needs the 12-node testbed, with a
single-node small-scale mode; and an MIT/Apache license. State honestly which results are
full-scale-only.

## Calibration

- The AEC deadline is **after acceptance** and **independent** of the camera-ready — do not conflate
  them (plan both in `atc-workflow`).
- Badge names, the exact set offered, and whether evaluation is single- or double-anonymous can vary
  by cycle and moved in the SIGOPS transition — confirm on the current call for artifacts.

## Output format

```text
[Target badges] Available / Functional / Reproduced
[Artifact role] anonymized review artifact / public badge artifact
[Contents] <system/data/scripts/provenance/license/archive>
[Ten-minute test] install + demo succeed on a clean machine? yes/no
[Reproduce] claim -> script -> expected figure present? small-scale mode for missing hardware? yes/no
[Fixes before upload] <ordered list>
```
