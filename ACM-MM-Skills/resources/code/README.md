# ACM MM Reproducibility Code Adapter

This directory points ACM MM authors to the repo-level ML-conference methods kit. It is not
a computer-vision-only kit and not the economics Stata/DiD/IV/RDD code library; it is a
lightweight artifact/reproducibility scaffold suited to multimedia papers whose evidence
spans several media at once.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-repro-package
```

Use the script as a smoke check only. For ACM MM, add three multimedia-specific passes the
generic checker does not cover:

- **Media renders anonymously.** Every supplementary video/audio/interactive demo plays with
  common open players and carries no author name in filename, metadata, or watermark (main
  track and BNI are double-blind).
- **Data access is real.** Datasets and media assets are reachable via an anonymous mirror
  for review, with the license and any consent/usage terms stated.
- **Badging readiness.** If aiming at the Reproducibility track, the package matches ACM's
  artifact-review expectations (environment, build, run, expected-output) for the Artifacts
  Evaluated / Results Reproduced badges.

Venue-specific policy still comes from [`../official-source-map.md`](../official-source-map.md),
the current official CFP and track calls, and the ACM MM skills for experiments,
reproducibility, supplementary material, artifact evaluation, and submission.
