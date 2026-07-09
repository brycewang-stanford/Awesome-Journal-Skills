# WACV ML Reproducibility Code Adapter

This directory points WACV authors to the repo-level ML conference methods kit. It is not
the economics Stata/DiD/IV/RDD code library; it is a lightweight artifact/reproducibility
scaffold for computer-vision conference papers.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-repro-package
```

Use the script as a smoke check only. It confirms an artifact package is anonymized and
self-describing; it does not judge whether the evidence answers the reviewers.

## WACV-specific notes

- Keep a **Round 1 vs Round 2 build** of the artifact in mind: if a paper is invited to
  Revise and Resubmit, the reproduction package usually needs the same revisions the
  reviewers asked for in the manuscript, and the two must not diverge.
- For an **Applications-track** paper, the artifact should let a reviewer reproduce the
  systems claim (latency, memory, robustness under the stated real-world constraint), not
  only a headline accuracy number — see `../../skills/wacv-artifact-evaluation`.

Venue-specific policy still comes from [`../official-source-map.md`](../official-source-map.md),
the current official Author Guidelines, and the WACV skills for experiments,
reproducibility, supplementary material, and submission.
