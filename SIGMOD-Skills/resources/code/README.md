# SIGMOD Artifact Code Adapter

This directory routes SIGMOD authors to the repository-level conference methods kit rather
than duplicating it. Nothing here is a database benchmark harness — it is the shared
artifact/reproducibility scaffold that this collection maintains for CS-conference packs,
useful as a smoke check on the package you will submit to reviewers and, later, to the
Availability & Reproducibility Initiative (ARI).

## Shared kit entry points

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Running the smoke check

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-artifact
```

## SIGMOD-specific interpretation

The kit was written with ML-conference packages in mind, so translate its checks for a
data-systems artifact: "experiment matrix" means your workloads × baselines × sweep grid;
"seeds" covers data generators and workload shuffles as well as any learned components; and
the checker's README/entry-script expectations map directly onto the claims-map and
`run_all.sh` / `run_small.sh` pattern taught in
[`../../skills/sigmod-artifact-evaluation/SKILL.md`](../../skills/sigmod-artifact-evaluation/SKILL.md).
What the script cannot check — baseline tuning fairness, hardware disclosure, per-figure
provenance — is covered by [`../../skills/sigmod-reproducibility/SKILL.md`](../../skills/sigmod-reproducibility/SKILL.md).

Venue policy always outranks tooling: current rules come from
[`../official-source-map.md`](../official-source-map.md) and the live CFP, not from any
script's exit code.
