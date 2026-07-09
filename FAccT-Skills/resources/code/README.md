# ACM FAccT Replication-Package & Documentation Adapter

This directory routes FAccT authors to the repository-level shared tooling. It stays deliberately
thin: FAccT-specific *norms* (mutually-anonymous review, the Revise round, endmatter statements,
datasheet/model-card documentation, disaggregation and consent) live in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared kits
so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer to any responsible-AI replication package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the Revise-and-resubmit
  response in [`../../skills/facct-author-response/SKILL.md`](../../skills/facct-author-response/SKILL.md).

## Typical use for a FAccT package

```bash
# Smoke-check the anonymized artifact before the OpenReview upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/facct-artifact-staging
```

Treat the script as a layout smoke test only. Venue norms still come from the current CFP/Author
Guide and the FAccT skills for experiments, reproducibility, and artifact/documentation.

## FAccT-specific checks the generic tooling cannot make

- **The reviewed anonymity is mutual, and the identity-revealing statements are withheld.** FAccT's
  mutual anonymity means the anonymized package must strip authors, institutions, funders, field
  sites, and repo owners — and the **Positionality / Acknowledgements / Author-Contributions /
  Competing-Interests** statements are held back until acceptance, not included at submission
  (`../../skills/facct-submission/SKILL.md`).
- **Accountability documentation exists and is honest.** For dataset or model work, ship a
  **datasheet** or **model card** whose disaggregated numbers match the paper's tables;
  "available on request" is a weakness, not a placeholder (`../../skills/facct-reproducibility/SKILL.md`).
- **Findings are disaggregated and proxies are validated.** A harm claim traces to per-subgroup
  results with uncertainty, and any proxy for a protected attribute has its error reported
  (`../../skills/facct-experiments/SKILL.md`).
- **The consent/ethics basis is documented and consistent with the release.** Human-subjects and
  community-facing work records consent, IRB or its considered absence, and re-harm avoidance,
  feeding the Ethical Considerations and Adverse Impacts endmatter
  (`../../skills/facct-supplementary/SKILL.md`).
- **This is not a badge task.** FAccT has no SIGSOFT-style Available/Functional/Reusable badging;
  the deliverable is documented, released, licensed material and a persistent archive at
  camera-ready (`../../skills/facct-artifact-evaluation/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and FAccT
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing here.
