# COLM LM-Research Code Adapter

This directory routes COLM authors to the repo-level ML-conference methods kit and
records what that generic kit cannot check for language-modeling papers. There is no
Stata/econometrics tooling here; the relevant shared assets are the experiment-matrix
and artifact-checklist scaffolds.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check an anonymized reproduction package before OpenReview upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-package
```

## What the generic kit does NOT cover for a COLM paper

The smoke checker verifies package hygiene, not LM-specific validity. Audit these by
hand against [`colm-reproducibility`](../../skills/colm-reproducibility/SKILL.md) and
[`colm-experiments`](../../skills/colm-experiments/SKILL.md):

1. **Model pinning** — checkpoint revision hashes for open weights; version strings
   *and query dates* for API models; tokenizer versions.
2. **Decoding disclosure** — temperature, top-p/top-k, max tokens, stop sequences,
   system prompts, per experiment.
3. **Contamination evidence** — overlap analysis between evaluation items and known
   pre-training corpora, or an explicit statement of why it cannot be run.
4. **Compute disclosure** — GPU-hours or API spend for training *and* evaluation.
5. **Harness pinning** — the evaluation-framework commit, since scoring rules drift
   between harness releases.

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md)
and the live COLM pages, never from tooling defaults.
