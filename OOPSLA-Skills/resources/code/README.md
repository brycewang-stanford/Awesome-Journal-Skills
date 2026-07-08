# OOPSLA Artifact & Measurement Kit Pointer

OOPSLA papers are expected to survive two scrutiny events that plain manuscripts never face:
the SIGPLAN empirical-guidelines reading of the evaluation, and — after acceptance — the
SPLASH artifact evaluators' kick-the-tires phase on a machine you do not control. This
directory does not duplicate tooling for that; it routes to the repository-wide ML/CS
conference kit and explains what to reuse for a PL artifact.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Adapting the kit to a PL artifact

The kit was written with model-training experiments in mind; for an OOPSLA artifact map its
concepts as follows.

| Kit concept | OOPSLA reading |
| --- | --- |
| Experiment matrix rows | Benchmark programs / subject corpora, not datasets |
| Seeds and variance | JIT warmup, run repetition, and per-benchmark confidence intervals |
| Environment pinning | Compiler/runtime versions, build flags, container or VM image |
| Anonymous package check | Kick-the-tires dry run: can a stranger build and reproduce Table 1? |

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/oopsla-artifact
```

Treat the script as a structural linter only — it verifies the package's shape, not badge
worthiness. Badge criteria, kick-the-tires timing, and the Zenodo deposit step come from the
SPLASH artifact-evaluation track via [`../official-source-map.md`](../official-source-map.md)
and the [`oopsla-artifact-evaluation`](../../skills/oopsla-artifact-evaluation/SKILL.md)
skill; measurement discipline comes from
[`oopsla-reproducibility`](../../skills/oopsla-reproducibility/SKILL.md).
