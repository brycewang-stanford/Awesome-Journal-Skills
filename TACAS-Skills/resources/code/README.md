# TACAS Replication-Package Code Adapter

This directory routes TACAS authors to the repository-level shared tooling. It stays deliberately
thin: TACAS-specific *policy* (the four categories, per-category anonymity, mandatory tool-paper
artifact evaluation, ETAPS Artifact Badges, LNCS open access, SV-COMP) lives in the skills and in
[`../official-source-map.md`](../official-source-map.md); reusable *tooling* lives in the shared
kits so packs do not carry diverging copies.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — packaging and clean-machine checks that transfer to any artifact submission.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout.
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  and [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — generic pre-submission and response scaffolding; adapt the latter to the TACAS rebuttal in
  [`../../skills/tacas-author-response/SKILL.md`](../../skills/tacas-author-response/SKILL.md).

## Typical use for a TACAS artifact

```bash
# Smoke-check the artifact layout before the EasyChair / AE upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/tacas-artifact-staging
```

Treat the script as a layout smoke test only. Venue policy still comes from the current ETAPS joint
CfP, the TACAS page, and the TACAS skills for experiments, reproducibility, and artifact
evaluation.

## TACAS-specific checks the generic tooling cannot make

- **The tool-paper artifact is mandatory and gates acceptance.** For a **regular tool** or
  **tool-demonstration** paper the artifact is submitted right after the paper and evaluated with
  the PC — a package that does not build on the ETAPS evaluation VM can cost the paper, not just a
  badge (`../../skills/tacas-artifact-evaluation/SKILL.md`).
- **Design for the clean ETAPS VM.** TACAS artifact evaluation runs inside a provided virtual
  machine image; pin dependencies, avoid network access at run time, and document expected runtime,
  because "works on my machine" is exactly what the AEC rules out
  (`../../skills/tacas-reproducibility/SKILL.md`).
- **Badges map to concrete deliverables.** *Available* needs a public DOI-issuing archive (Zenodo/
  figshare/Software Heritage); *Functional* needs a reproducible run of the paper's claims;
  *Reusable* needs documentation and licensing letting others build on it
  (`../../skills/tacas-artifact-evaluation/SKILL.md`).
- **Anonymity depends on category.** A **regular research** artifact submitted for review must be
  anonymized (no owner strings, lab names, or identity-revealing repository URLs); a **tool /
  case-study** artifact is single-blind and may carry the tool identity
  (`../../skills/tacas-submission/SKILL.md`).
- **SV-COMP has its own pipeline.** A competition contribution follows the SV-COMP benchmark and
  rule format and its verifier is run by the organizers on the common task set — this is separate
  from a TACAS tool paper's artifact (`../../skills/tacas-experiments/SKILL.md`).

This is not the econometrics/Stata kit used by the journal packs in this repository, and TACAS
evidence is not ML-leaderboard evidence: do not import DiD notebooks or benchmark-score framing
that ignores soundness here.
