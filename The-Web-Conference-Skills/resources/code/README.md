# Web Conference Reproducibility Code Adapter

Pointer to the repository-level ML-conference reproducibility kit, plus the
web-specific practices that kit does not cover. This is not the econometrics code
library used by the economics packs.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

```bash
# Smoke-check a review-time (anonymized) or camera-ready artifact package
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/artifact-package
```

## What to add on top for a Web Conference artifact

The shared checker validates generic ML packaging (README, environment, seeds,
run scripts). Web Conference artifacts additionally need, per
[`../../skills/webconf-reproducibility/SKILL.md`](../../skills/webconf-reproducibility/SKILL.md)
and [`../../skills/webconf-artifact-evaluation/SKILL.md`](../../skills/webconf-artifact-evaluation/SKILL.md):

- a **crawl/collection manifest** (source, window, sampling rule, per-file
  SHA-256) so corpus drift is detectable;
- **hydration pointers instead of content** where platform terms forbid
  redistribution, with the collection script included;
- a **dead-link / recrawl accounting script** so future users can quantify decay;
- **archival deposit with a DOI** (Zenodo, figshare, institutional) for the
  camera-ready and the Artifacts Available badge — a bare GitHub URL does not
  satisfy the badge's archival requirement.

Venue policy always comes from the current edition's pages via
[`../official-source-map.md`](../official-source-map.md), never from tooling
defaults.
