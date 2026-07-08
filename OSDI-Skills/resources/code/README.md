# OSDI Artifact Code Adapter

This directory points OSDI authors at the repo-level ML-conference methods kit for
artifact-package hygiene. It is a generic smoke-check scaffold — useful because OSDI
artifacts are graded by an artifact evaluation committee working from your README on
unfamiliar machines — not a substitute for OSDI policy.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/osdi-artifact
```

## What the generic kit cannot check (OSDI-specific)

- **Badge scope.** OSDI '26 evaluated only the **Artifacts Available** badge, so the
  decisive requirement is a **permanent public archive** (Zenodo or equivalent), not a
  runnable demo. Earlier cycles also graded Functional/Reproduced — check the current
  Call for Artifacts before optimizing for the wrong badge.
- **Timing.** OSDI artifacts are submitted **after (conditional) acceptance** (May 8,
  2026, 8:59 pm PDT in the '26 cycle) — anonymity rules differ from submission time.
- **Systems-artifact realities** the script cannot see: kernel-version and hardware
  dependencies, testbed/cluster access instructions, trace and dataset licensing, and
  whether the artifact reproduces the *paper's* workloads rather than toy ones.

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md),
the live Call for Artifacts, and the `osdi-artifact-evaluation` and
`osdi-reproducibility` skills.
