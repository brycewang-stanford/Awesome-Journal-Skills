# MICRO Reproducibility Code Adapter

This directory routes MICRO authors to the repo-level shared conference
reproducibility kit and lists the hardware-evaluation checks that generic tooling
cannot perform. It is an adapter, not a simulator distribution — no economics or
Stata material belongs here.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# structural smoke check of an anonymized artifact package before linking it
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
    /path/to/anonymous-artifact
```

## What the generic checker cannot see (do these by hand)

The shared kit was built for ML training runs; a MICRO artifact fails in different
places. After the smoke check, verify the microarchitecture-specific surface from
[`../../skills/micro-reproducibility/SKILL.md`](../../skills/micro-reproducibility/SKILL.md):

1. **Simulator pinning** — commit hash + patch set recorded in every run manifest,
   not just "gem5" or "ChampSim" by name.
2. **Config completeness** — baseline and mechanism configs as machine-readable
   files matching the paper's methodology table (pipeline width, cache latencies,
   predictor, prefetchers, DRAM timing).
3. **Trace provenance** — SimPoint parameters, warmup counts, and the licensing
   boundary: SPEC binaries and inputs must **not** be in the package; recipes must
   be.
4. **Power-model versioning** — McPAT/CACTI/Accelergy version and node recorded
   beside every energy/area number's manifest.
5. **Runtime tiering** — `smoke` / `key` / `full` entry points with measured
   durations, per [`../../skills/micro-artifact-evaluation/SKILL.md`](../../skills/micro-artifact-evaluation/SKILL.md).
6. **Anonymity of configs** — hostnames, cluster paths, and git author fields
   scrubbed from manifests and scripts before the link goes in the submission.

Venue policy always comes from the current official pages recorded in
[`../official-source-map.md`](../official-source-map.md) — never from this adapter.
