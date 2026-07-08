# SIGIR IR Reproducibility Code Adapter

This directory routes SIGIR authors to the repo-level ML conference methods kit and
adds the IR-specific packaging notes the generic kit does not cover. It is not an
econometrics code library; it is an artifact/reproducibility scaffold for retrieval
and recommendation papers.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-repro-package
```

## IR-specific additions the generic kit misses

The smoke checker validates package structure; a SIGIR reviewer additionally expects:

1. **Run files** (TREC format) behind every reported table row, under `runs/`.
2. **Qrels/collection identifiers** as `ir_datasets` ids or checksummed pointers —
   never redistributed judgment files whose licenses forbid it.
3. **A one-command scorer** (`trec_eval`/`ir_measures` invocation with exact flags)
   that regenerates each table from the shipped runs.
4. **The significance script** that produced the paper's p-values, runnable on the
   shipped runs.
5. **Index-build scripts** with analyzer settings pinned — the silent score-movers.

See [`../../skills/sigir-artifact-evaluation/SKILL.md`](../../skills/sigir-artifact-evaluation/SKILL.md)
for the full repository layout and
[`../../skills/sigir-reproducibility/SKILL.md`](../../skills/sigir-reproducibility/SKILL.md)
for the drift-pinning table. Venue policy always comes from
[`../official-source-map.md`](../official-source-map.md) and the current track pages,
not from this kit.
