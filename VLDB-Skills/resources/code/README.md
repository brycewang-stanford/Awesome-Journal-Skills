# VLDB Reproducibility Code Pointer

PVLDB expects artifacts, and its Reproducibility Committee eventually reruns them. This
directory deliberately contains no tooling of its own — it points at the collection's
shared CS-conference artifact scaffold and explains how to read it with PVLDB eyes.

## Where the shared scaffold lives

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Smoke-testing a PVLDB artifact before release

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/pvldb-artifact
```

## Translating the checks for a data-systems paper

The scaffold speaks ML dialect; PVLDB artifacts need a systems reading of each check.
Where it asks about training seeds, substitute every source of run-to-run variance in a
storage or query experiment: data-generator seeds, cache state (declare warm vs. cold),
client thread counts, and cluster placement. Where it asks for an experiment matrix,
supply the datasets × workloads × systems grid behind each figure, including the exact
versions and tuning of competitor systems. Where it wants an entry script, provide the
end-to-end path the pVLDB evaluators actually walk: build the prototype from source,
generate or fetch the input data, replay the workload, and regenerate every figure and
table in the PDF from the raw measurements.

What no script can certify — whether baselines were tuned in good faith, whether the
hardware description is complete enough to re-provision, whether each plotted point
traces to logged raw output — is the subject of
[`../../skills/vldb-reproducibility/SKILL.md`](../../skills/vldb-reproducibility/SKILL.md)
and [`../../skills/vldb-artifact-evaluation/SKILL.md`](../../skills/vldb-artifact-evaluation/SKILL.md).

Current PVLDB availability and reproducibility policy comes from
[`../official-source-map.md`](../official-source-map.md) and the live volume guidelines,
never from a checker's exit code.
