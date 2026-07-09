# ISSTA Artifact & Replication-Package Code Adapter

This directory routes ISSTA authors to the repository-level shared tooling. It stays thin on
purpose: ISSTA-specific *policy* — ACM badge readiness, Zenodo archival, the 18-page/artifact
split — lives in the skills and in [`../official-source-map.md`](../official-source-map.md);
reusable *tooling* lives in the shared kits so conference packs do not carry diverging copies.

An ISSTA artifact is a specific thing: a **runnable tool bundled with its subject programs, pinned
benchmark versions, and the scripts that regenerate the paper's results**. That is neither the
econometrics Stata/DiD kit the journal packs use nor an ML-leaderboard submission, so keep DiD
notebooks and benchmark-ranking framing out of this directory.

## Shared kits

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  — anonymous-review and public-release checks that transfer directly to an ISSTA replication
  package.
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — dependency-free smoke checker for package layout (README, entry script, environment file).
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  — generic pre-submission scaffolding; adapt it to the HotCRP audit in
  `../../skills/issta-submission/SKILL.md`.

## Typical use for an ISSTA artifact

```bash
# Smoke-check the anonymized artifact staging directory before the HotCRP upload
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/issta-artifact-staging
```

Treat the script as a layout smoke check only. Whether an artifact earns *Functional*, *Reusable*,
or *Results Reproduced* is decided by the evaluators actually running it, not by a linter.

## ISSTA-specific checks the generic tooling cannot make

- **The tool actually runs from the documented entry point** on a clean machine or the provided
  container — an artifact that needs the authors' private cluster earns no badge
  (`../../skills/issta-artifact-evaluation/SKILL.md`).
- **Subjects and benchmark versions are pinned** — Defects4J revision, exact commit SHAs of subject
  programs, and fuzzing seed corpora archived, not just referenced by name
  (`../../skills/issta-reproducibility/SKILL.md`).
- **Non-determinism is disclosed and bounded** — where results vary across runs (fuzzing, timeouts,
  scheduling), the package states the run count and expected variance, not a single golden run.
- **Result tables regenerate from logged data** — the numbers in the PDF trace to a script over
  stored outputs, so paper and artifact cannot drift apart.
- **Availability is Zenodo-backed** — the *Artifacts Available* badge requires a DOI-issuing public
  archive (Zenodo), and that deposit is a distinct step from the anonymous review upload
  (`../../skills/issta-artifact-evaluation/SKILL.md`).
- **The review-time copy is anonymized** — repository owners, commit authors, and container labels
  scrubbed, because artifact review at ISSTA is double-anonymous alongside the paper.
