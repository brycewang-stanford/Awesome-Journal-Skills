# MLSys Measurement & Artifact Code Adapter

This directory routes MLSys authors to the repo-level ML conference methods kit and explains
how to bend it toward MLSys's distinctive needs: performance measurement and post-acceptance
badge-driven artifact evaluation, rather than accuracy-table reproduction alone.

## Shared Kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical Use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/artifact-package
```

## MLSys-specific adaptations

The shared kit was written with accuracy-centric ML papers in mind. For MLSys artifacts, layer
these on top:

- Add a **performance-reproduction tier** to the experiment matrix: for each headline
  throughput/latency/memory/cost number, record the hardware it requires and which numbers an
  AE reviewer can plausibly reproduce on smaller hardware (see
  [`../../skills/mlsys-artifact-evaluation/SKILL.md`](../../skills/mlsys-artifact-evaluation/SKILL.md)).
- Pin the **system layer**, not just Python: driver, CUDA/ROCm, container digest, interconnect
  topology. A `requirements.txt` alone cannot reproduce a latency claim
  ([`../../skills/mlsys-reproducibility/SKILL.md`](../../skills/mlsys-reproducibility/SKILL.md)).
- MLSys artifact evaluation is **post-acceptance and badge-based** (Availability, Functional,
  Reproducible in the 2026 cycle), so the anonymity constraints differ from submission-time
  supplements — check the current Call for Artifact Evaluations via
  [`../official-source-map.md`](../official-source-map.md) before packaging.

The smoke checker validates package hygiene only; badge criteria, deadlines, and appendix
templates come from the current mlsys.org AE call.
