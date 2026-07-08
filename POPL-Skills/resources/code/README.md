# POPL Proof-Artifact Code Adapter

This directory adapts the repo-level ML-conference methods kit to POPL's artifact
reality. It is neither the economics Stata/DiD/IV library nor a training-run
scaffold: a POPL artifact is most often a **mechanized proof development**, and its
"reproduction" is a type-checker run, not a seeded experiment.

## Shared kit (use with translation)

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-artifact
```

## Translation table: ML-kit concept → POPL proof artifact

| Kit concept | POPL equivalent |
| --- | --- |
| Random seeds, run variance | Not applicable — proof checking is deterministic; the analogue is the pinned assistant version (opam switch, `lean-toolchain`) |
| Experiment matrix | Correspondence table: paper theorem → formal name → file:line → status → axioms (`popl-reproducibility`) |
| Dataset provenance | Trusted base disclosure: assistant version, axioms used, `--safe`/`coqchk` status |
| Training-time budget | Full-build wall-clock time plus a `make quick` target that checks one headline theorem |
| Metric tables regenerate from scripts | Proof-effort tables regenerate from `coqwc` / declaration counts (`popl-experiments`) |

The smoke checker above verifies package hygiene (README, manifest, no obvious
identity leaks); it knows nothing about `admit`/`sorry`. Add the completeness and
axiom audits from
[`../../skills/popl-artifact-evaluation/SKILL.md`](../../skills/popl-artifact-evaluation/SKILL.md)
on top — those are the checks a POPL evaluator actually runs. Badge criteria and
policy wording come from [`../official-source-map.md`](../official-source-map.md)
and the live artifact-evaluation track page, never from this adapter.
