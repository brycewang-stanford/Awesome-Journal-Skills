# HPCA Reproducibility Code Adapter

Bridge from this pack to the repository's shared conference reproducibility kit —
plus an honest list of the architecture-specific checks that kit cannot perform.
This is not the economics/Stata code library; nothing econometric belongs in an
HPCA artifact.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
# Smoke-check the anonymized artifact mirror before an HPCA submission
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
    /path/to/anonymous-artifact-mirror
```

The checker verifies generic package hygiene (README/manifest presence, obvious
identity leaks, structure). Treat a pass as necessary, never sufficient — and
remember the HPCA badge round runs on the **separate AE HotCRP** under **IEEE
reproducibility badging**, so the packaging target is IEEE's, not ACM's.

## What the generic kit cannot check — do these by hand

1. **Simulator pinning.** Commit hash plus any local-patch diff archived next to
   results; see the manifest format in
   [`../../skills/hpca-reproducibility/SKILL.md`](../../skills/hpca-reproducibility/SKILL.md).
2. **Config-to-figure traceability.** Every paper figure hash-matches a scripted
   regeneration (`regen.sh` per figure) — the freeze ritual in the same skill.
3. **Workload licensing.** SPEC-class and other proprietary suites are not
   redistributable: ship recipes and checksums, plus one freely available workload
   that exercises the full pipeline (see
   [`../../skills/hpca-artifact-evaluation/SKILL.md`](../../skills/hpca-artifact-evaluation/SKILL.md)).
4. **Machine-state records.** For every real-silicon number, capture frequency
   governor, turbo, SMT, NUMA policy, and kernel/firmware versions, with trial
   counts and dispersion — a simulator-only artifact still needs host provenance.
5. **Evaluator wall-clock budget.** Reduced-input variants of the headline
   experiments, with measured runtimes stated per step, so a cold-start evaluator
   can finish inside the AE window.

Venue policy always comes from the current official pages via
[`../official-source-map.md`](../official-source-map.md) — never from tooling output.
