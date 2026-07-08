# CoRL Repro Kit Adapter

This directory routes CoRL authors to the repository-level ML-conference
reproducibility kit and lists the robot-learning checks that generic ML tooling
does not cover. It is deliberately thin: policy comes from the live corl.org
pages via `../official-source-map.md`, and methodology comes from the skills.

## Shared kit (repo-level)

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check an anonymous supplementary code bundle before upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/corl-supplementary-bundle
```

## CoRL-specific checks the shared kit cannot make

The generic checker knows nothing about robots. Verify these by hand against
`../../skills/corl-reproducibility/SKILL.md` and
`../../skills/corl-supplementary/SKILL.md`:

1. Simulator + physics versions pinned (contact behavior changes across builds).
2. Hardware ledger present: robot model, firmware, sensors, control interface,
   deployed compute, latency.
3. Evaluation episode logs (per-trial CSV) archived for every hardware table.
4. Checkpoint selection rule stated; checkpoints keyed to tables and seeds.
5. Supplementary video ≤ 250 MB (2026 strict cap), audio stripped, frames swept
   for identity leaks.
6. Post-acceptance hosting plan drafted — PMLR accepts no video supplementary.
