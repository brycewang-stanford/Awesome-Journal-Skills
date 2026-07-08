# CIKM Reproducibility Code Adapter

Pointer directory: CIKM work uses the repo-level ML-conference methods kit, applied
to the chained-pipeline artifacts (index + graph + model + evaluation) typical of
this venue. It is not an econometrics library.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-review-artifact
```

Run it against the anonymous review artifact before upload and again against the
public repository before camera-ready.

## CIKM-specific additions the generic kit does not check

The smoke checker knows nothing about this venue's habits, so verify by hand:

- **KG snapshot pinning** — upstream dump date, extraction queries, per-relation
  counts (see `../../skills/cikm-reproducibility/SKILL.md`).
- **Anonymity of the artifact itself** — commit authors, hostnames, notebook
  metadata; CIKM review is double-blind and the artifact is part of the submission
  surface.
- **GenAI-disclosure consistency** — generated code/data/labels in the package must
  match what the paper's GenAI Usage Disclosure section declares.
- **Budget reality** — nothing decision-critical may live only in the artifact,
  because CIKM 2026 budgets count appendices inside the page limit and artifact
  inspection is discretionary.

Venue policy always comes from `../official-source-map.md` and the current official
pages, never from this kit.
