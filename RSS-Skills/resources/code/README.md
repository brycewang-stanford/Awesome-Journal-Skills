# RSS Reproducibility Code Adapter

This directory routes RSS authors to the repo-level ML-conference methods kit and
lists the robotics-specific checks that kit cannot perform. It is not an econometrics
library; it is a scaffold for packaging the computational half of an RSS submission.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-supplement
```

## What the shared kit cannot check for an RSS paper

The smoke checker validates software hygiene (entry points, seeds, dependency
manifests). An RSS supplement carries evidence the script cannot see:

1. **Embodied-trial provenance** — whether logged runs correspond to the trial counts
   claimed in the PDF, and whether failure cases are present in the logs, not only
   successes.
2. **Platform specification** — robot model, end-effector, sensor suite, firmware,
   and control rates detailed enough for a lab with similar hardware to attempt
   replication (`rss-reproducibility`).
3. **Sim-vs-real labeling** — every result file unambiguously tagged as simulation or
   hardware, since conflating them undermines the paper's central evidence claim.
4. **Footage anonymity** — video frames free of faces, lab signage, institution
   colors, and file metadata that would break double-blind review
   (`rss-supplementary`).
5. **Self-containment of the PDF** — nothing decision-critical may live only in the
   archive; the 2026 CFP requires the main paper to stand alone.

Venue policy always comes from [`../official-source-map.md`](../official-source-map.md)
and the live CFP, never from this adapter.
