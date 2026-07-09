# ACM SIGMETRICS Replication-Package Code Adapter

This directory routes SIGMETRICS authors to the repository-level shared tooling. It stays
deliberately thin: SIGMETRICS-specific *policy* (the rolling three-deadline POMACS process, the
one-shot revision, mandatory shepherding, double-anonymous review, ACM badging) lives in the skills
and in [`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the
shared kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any systems replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the **one-shot revision**
  response letter in [`../../skills/sigmetrics-author-response/SKILL.md`](../../skills/sigmetrics-author-response/SKILL.md).

## Typical use for a SIGMETRICS package

```bash
# Smoke-check the anonymized artifact before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/sigmetrics-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current call for
papers and the SIGMETRICS skills for experiments, reproducibility, and artifact evaluation.

## SIGMETRICS-specific checks the generic tooling cannot make

- **A proof is an artifact too.** SIGMETRICS papers frequently carry a theorem (a performance
  bound, a stability condition, a regret rate). The "artifact" a reviewer scrutinizes is often a
  proof appendix and a simulation that *validates the theorem numerically* — not only running
  code. Ship the derivation and the simulation that reproduces the theorem's predicted curve
  (`../../skills/sigmetrics-experiments/SKILL.md`).
- **Simulation reproducibility means logged seeds and a matched analytic curve.** For a
  queueing/stochastic result, the package should regenerate the paper's figures from logged
  simulation runs *and* overlay the analytic prediction, so a reviewer sees model and measurement
  agree (`../../skills/sigmetrics-reproducibility/SKILL.md`).
- **Measurement provenance is pinned.** For a measurement or trace-driven paper, record the trace
  source, collection window, sanitization, and access terms; archive the *processed* dataset (or
  document access) rather than only the collection script.
- **The one-shot-revision loop is single-shot.** Unlike an open-ended journal R&R, the revision is
  re-reviewed once against a list of required changes; the package and response must close every
  listed item in that single round (`../../skills/sigmetrics-author-response/SKILL.md`).
- **Badge readiness rides on the ACM scheme.** A DOI-issuing archive, an open license, and
  evaluator-proof docs target the ACM Available/Functional/Reusable/Reproduced badges; confirm
  whether an artifact track runs this cycle (`../../skills/sigmetrics-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and
SIGMETRICS evidence is not an ML leaderboard: do not import DiD notebooks or benchmark-score
framing here. The evidence bar is a stochastic model proven and measured, or a measurement study
whose methodology a skeptic would accept.
