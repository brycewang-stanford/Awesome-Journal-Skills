---
name: ppopp-artifact-evaluation
description: Use when packaging a PPoPP artifact for the post-acceptance, CGO-shared artifact-evaluation track, covering PPoPP's specific badge policy (Functional or Reusable plus Results Reproduced, no "Results Replicated"; Available granted by the publisher from a deposit link), reproducible parallel measurements on evaluators' hardware, and the separate AE deadline.
---

# PPoPP Artifact Evaluation

Use this for the artifact track. PPoPP runs a **post-acceptance** artifact evaluation with its own
deadline (PPoPP 2026: artifact submission 17 November 2025, notification 5 January 2026),
**separate from the camera-ready** and shared in culture with co-located **CGO**. Two things to
internalize: PPoPP has a **distinctive badge policy**, and the hard part of a *parallel* artifact is
that the results must reproduce on **someone else's hardware**, where core counts and topology
differ from yours.

## PPoPP's badge policy (verify the current set each cycle)

| Badge | Colour | What it certifies | How it is awarded |
|---|---|---|---|
| Artifacts Available | green | The artifact is publicly, permanently retrievable | By the **publisher**, from a deposited-artifact link — **no formal audit** |
| Artifacts Evaluated — Functional | lighter red | The artifact runs, is documented, consistent, complete, exercisable | AE committee runs it |
| Artifacts Evaluated — Reusable | darker red | Functional **plus** quality that exceeds minimal functionality; carefully documented and structured for reuse | AE committee runs it |
| Results Reproduced | darker blue | The paper's main results were obtained by the evaluators (within tolerance) | AE committee re-runs and matches |

Two PPoPP-specific facts to get right:

- The committee awards **one of Functional / Reusable** (Reusable is the higher bar) **plus**
  possibly **Results Reproduced**.
- PPoPP **does not award the lighter-blue "Results Replicated" badge** — do not target or claim it.
  **Available** is not evaluated; it is publisher-granted from a link, so it is the cheapest badge
  to secure and worth doing regardless.

## What makes a *parallel* artifact hard

An evaluator does not have your machine. A speedup that depended on your 96-core dual-socket node
will not reproduce on a reviewer's 16-core laptop, and "Results Reproduced" requires agreement
within a stated tolerance. Design for portability of the *conclusion*, not the absolute numbers:

```text
[Hardware doc]  state the exact machine you used (CPU/GPU model, sockets, cores, NUMA, memory,
                interconnect) and the minimum config on which the trend still holds
[Scaled runs]   provide a small/fast configuration whose *shape* (linear region, saturation)
                matches the paper, so an evaluator can reproduce the claim on modest hardware
[Tolerance]     state explicitly what "reproduced" means for your numbers (e.g. within 10%, or
                "monotone speedup to the machine's core count")
[Determinism]   fix seeds; pin threads; document warm-up; make runs repeatable
[GPU]           document driver/CUDA/ROCm versions and the GPU class needed; provide a CPU
                fallback path where possible
```

## What evaluators open first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A concurrent structure | README + a one-command throughput run | Only builds on the authors' toolchain; hardcoded core count |
| A runtime/scheduler | The script that reproduces a scaling figure | Numbers in the PDF that no script regenerates |
| A GPU technique | Build + a small kernel run | Requires a specific GPU with no fallback; missing driver versions |
| A parallel algorithm | Build + a scaled input run | Data missing; topology assumptions undocumented |

Assume a bounded time budget on a clean machine; make the first ten minutes succeed.

## Packaging plan

```text
[Container]   a Dockerfile or pinned environment (spack/conda/lockfile); avoid manual 40-step builds
[README]      one-screen orientation: what it is, how to build, how to run the demo, how to
              reproduce each figure, expected runtime, and the hardware each run needs
[Mapping]     an explicit table: paper claim/figure -> script -> expected result (+ tolerance)
[Scaling kit] scripts that sweep thread/core count and emit the paper's curve on the eval machine
[Provenance]  exact hardware used, compiler/flags, driver versions, seeds, pinning policy
[License]     an OSI-approved license so the artifact can be badged Reusable
[Archive]     deposit in a DOI-issuing repository (Zenodo/figshare/Software Heritage) for Available
```

## Anonymized review artifact vs. badge artifact

- **At paper submission:** the artifact (if attached for reviewers) is anonymized — no owner
  strings, cluster/account paths, lab names, or identifying links.
- **At the AE track (post-acceptance):** the de-anonymized, licensed, DOI-archived version is what
  evaluators badge and the camera-ready cites.

## Calibration

- The AE deadline is *after* acceptance and *independent* of the camera-ready; do not conflate them.
- Confirm each cycle whether AE is run jointly with CGO, the exact badge set and colours, and
  whether Available is auto-granted by the publisher (as verified) or handled by the committee.

## Output format

```text
[Target badges] Available (publisher) / Functional or Reusable / Results Reproduced  (NOT Replicated)
[Artifact role] anonymized review artifact / public badge artifact
[Portability] scaled config whose trend matches the paper on modest hardware? tolerance stated?
[Ten-minute test] build + demo succeeds on a clean machine? yes/no
[Claim mapping] each figure -> script -> expected result (+ tolerance) present? yes/no
[Fixes before upload] <ordered list>
```
