# ISCA Reproducibility Code Adapter

Bridge from this pack to the repository's shared ML-conference reproducibility
kit — plus an honest list of the architecture-specific checks that kit cannot
perform. This is not the economics/Stata code library; nothing econometric
belongs in an ISCA artifact.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
# Smoke-check the anonymized artifact mirror before an ISCA submission
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
    /path/to/anonymous-artifact-mirror
```

The checker verifies generic package hygiene (README/manifest presence, obvious
identity leaks, structure). Treat a pass as necessary, never sufficient.

## What the generic kit cannot check — do these by hand

1. **Simulator pinning.** Commit hash + local-patch diff archived next to
   results; see the manifest format in
   [`../../skills/isca-reproducibility/SKILL.md`](../../skills/isca-reproducibility/SKILL.md).
2. **Config-to-figure traceability.** Every paper figure hash-matches a scripted
   regeneration (`regen.sh` per figure) — the freeze ritual in the same skill.
3. **Workload licensing.** SPEC-class suites are not redistributable: recipes
   and checksums in the artifact, plus one free workload that exercises the full
   pipeline (see
   [`../../skills/isca-artifact-evaluation/SKILL.md`](../../skills/isca-artifact-evaluation/SKILL.md)).
4. **Hardware-state records.** Governor/turbo/SMT/kernel captured for every
   real-machine number, with trial counts and dispersion.
5. **Evaluator wall-clock budget.** Reduced-input variants of headline
   experiments, with measured runtimes stated per step.

Venue policy always comes from the current official pages via
[`../official-source-map.md`](../official-source-map.md) — never from tooling
output.
