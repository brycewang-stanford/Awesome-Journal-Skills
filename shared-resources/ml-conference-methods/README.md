# ML Conference Methods Resource

Shared method and reproducibility resources for AI/ML conference depth packs
(NeurIPS, ICML, ICLR, AAAI, IJCAI, AISTATS). This is not an econometrics kit:
it is for ML papers whose evidence depends on benchmarks, ablations, seeds,
artifacts, proofs, and compute reporting.

## What to Use

- `experiment-matrix.md` - a compact claim-to-evidence matrix for ML papers.
- `reproducibility-artifact-checklist.md` - anonymous-review and public-release
  checks for code, data, models, logs, and supplements.
- `code/check_repro_package.py` - dependency-free smoke checker for a local
  reproduction package layout.

## Scope

Use this kit when a skill needs to inspect or draft:

- experiment design and ablation coverage;
- seed, variance, compute, and dataset reporting;
- anonymous review artifacts and post-acceptance public releases;
- mapping from paper claims to exact commands or proof scripts.

Current-cycle conference policies still live in each pack's
`resources/official-source-map.md` and must be reopened before final advice.
