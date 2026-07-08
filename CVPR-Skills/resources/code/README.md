# CVPR Reproducibility Code Adapter

This directory adapts the repository's shared ML-conference reproducibility kit for
CVPR authors. CVPR is a benchmark-and-artifact venue, so the generic kit covers a lot —
but several CVPR-specific checks live only in this pack's skills and cannot be
automated by the shared script.

## Shared kit entry points

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check the anonymous supplement's code directory before zipping it
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/supplement/code
```

## What the shared kit does NOT check (CVPR-specific, do manually)

- **Compute Reporting Form consistency** — the hardware row in CRF Section 1 must match
  every latency/"real-time" claim in the paper (`../../skills/cvpr-reproducibility/SKILL.md`).
- **External-link ban** — no URLs in the supplement that expand content; the script does
  not scan PDFs or videos for links.
- **Video metadata** — MP4/MOV containers carry author tags; strip them
  (`../../skills/cvpr-supplementary/SKILL.md`).
- **Dataset-release clause** — a dataset claimed as a contribution must be public by
  camera-ready; that is a calendar obligation, not a lint check
  (`../../skills/cvpr-camera-ready/SKILL.md`).

Policy always comes from the current cvpr.thecvf.com pages via
[`../official-source-map.md`](../official-source-map.md), never from tooling defaults.
