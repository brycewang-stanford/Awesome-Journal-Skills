---
name: hpca-reproducibility
description: Use when strengthening HPCA reproducibility: pinning the result chain from simulator commit through config, workload, sampled region, and statistics, building one manifest per figure, recording machine state for silicon runs, and keeping the environment resurrectable for the IEEE artifact-badging round.
---

# HPCA Reproducibility

Use this to make an HPCA paper's results reconstructable — by a reviewer during the
window, by an artifact evaluator after acceptance, and by you six months later when
the environment has drifted. HPCA's artifact badges are **IEEE reproducibility
badges** earned on a separate AE HotCRP, so build toward that pipeline, not the ACM
one.

## Pin the result chain

Every figure in the paper should trace back through an unbroken chain:

```text
simulator commit (or machine + firmware)
  -> configuration file (core, cache, DRAM, interconnect)
    -> workload + input + sampled region
      -> raw output logs
        -> statistics script
          -> the figure/table in the PDF
```

If any link is unpinned — a simulator built from "latest," a config edited by hand, a
region chosen ad hoc — the result is not reproducible, only re-runnable by you.

## One manifest per figure

Give each headline figure a manifest that names its commit, config, workload, region,
seed/trial count, and the exact command that regenerates it. A `regen.sh` per figure
that reproduces the artifact from raw logs turns "trust me" into "run this."

| Chain link | What to pin | Failure if unpinned |
|---|---|---|
| Simulator | Commit hash + local-patch diff | Silent behavior drift between builds |
| Config | Versioned file, not manual edits | Unreproducible operating point |
| Workload/region | Suite version + sampling recipe | Cherry-picked region suspicion |
| Statistics | Scripted, seeded | Numbers that cannot be regenerated |
| Silicon runs | Governor/turbo/SMT/NUMA + kernel/firmware | Noise mistaken for signal |

## Record machine state for silicon

A real-hardware result is only reproducible with its host state captured: frequency
governor, turbo, SMT, NUMA policy, kernel and firmware versions, and the trial count
with dispersion. Archive it next to the logs, not in your memory.

## Handle non-redistributable workloads

SPEC-class and other licensed suites cannot ship in the artifact. Provide the
**recipe and checksums** to reconstruct them, plus at least one freely available
workload that exercises the full pipeline so an evaluator without a license can still
reproduce a headline result.

## Keep the environment resurrectable

Between submission and the badge round, environments rot. Containerize or script the
build, pin dependency versions, and do a **cold-start resurrection drill** on a clean
machine before you promise a reviewer or evaluator anything. The single
rebuttal/revision window is not the time to discover your simulator no longer builds.

## Reproducibility checklist

```text
[Result chain] every figure pinned commit->config->workload->region->stats? (Y/N)
[Manifests] one per headline figure with a regen script? (Y/N)
[Silicon state] governor/turbo/SMT/NUMA + kernel/firmware + trials archived? (Y/N/NA)
[Licensed workloads] recipe+checksums + one free workload provided? (Y/N/NA)
[Resurrection] cold-start build drill passed on a clean machine? (Y/N)
[Badge readiness] packaged for the IEEE AE HotCRP? (Y/N)
[Top gaps] <ordered>
```

Reopen the current artifact-evaluation page for the badge set and calendar before
relying on any AE detail here — the AE mechanics are per-edition.
