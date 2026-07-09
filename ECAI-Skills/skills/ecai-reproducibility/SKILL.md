---
name: ecai-reproducibility
description: Use when building the reproducibility story for an ECAI paper — a complete proof appendix for theory/KR work, a seeded and cached package for empirical/ML work, provenance pinning for datasets and models, and an anonymized supplement that satisfies double-blind review inside ECAI's tight 7-page body with no separate artifact track.
---

# ECAI Reproducibility

ECAI reproducibility is **in-band**: there is no separate artifact-evaluation track, so the same
reviewers who judge the paper judge whether the results and proofs are believable, from the 7-page
body plus an anonymized supplement. Build the reproducibility story to survive *that* read — one
pass, double-blind, in a short window — not a badge committee.

Because ECAI is a **general-AI** venue, "reproducible" means different things across its breadth.
Pick the mode that matches your contribution.

## Mode 1 — Theory / KR / argumentation: proofs are the artifact

- The body sketches; the **supplement carries every full proof**. A theorem stated without a
  checkable proof is a claim, not a result.
- State **all assumptions explicitly** (finiteness, admissibility, monotonicity, language
  fragment). The most common reject-driving misreading is a reviewer assuming a hidden condition.
- If the theory has a computational side (a solver, an encoding, complexity results), include a
  **reference implementation or the exact encoding** so a reviewer can re-run a small instance.
- Define objects once, precisely; ECAI's symbolic-AI reviewers check definitions against lemmas.

## Mode 2 — Empirical / ML / planning: seed, cache, pin

- **Fix and report seeds**; report central tendency *and* spread across seeds, not a single lucky
  run (`ecai-experiments`).
- **Cache raw outputs** (model predictions, planner traces, API responses) so results reproduce
  **without live calls** — a package that re-queries an API re-samples rather than reproduces.
- **Pin provenance:** dataset name *and version/date*, preprocessing scripts, model identifiers
  with dates, hardware where it affects timing.
- Provide a **claim→file map**: each reported table/number points to the script that regenerates it.

## Provenance pinning (both modes, where applicable)

```text
[ ] Dataset: name, version/DOI, download date, license, preprocessing script committed
[ ] Splits: exact train/val/test (or instance sets) fixed and included or scripted
[ ] Models: identifiers + dates (for hosted/LLM components); prompts/configs committed
[ ] Seeds: fixed and reported; number of runs stated
[ ] Environment: dependency versions pinned (lockfile / environment.yml / requirements)
[ ] Outputs: raw results cached so re-run does not depend on a live service
```

## Double-blind, in the supplement too

The supplement is read under **double-blind** review. Anonymize it as carefully as the PDF:

```bash
# Sweep the staged supplement before zipping
grep -rniE 'university|@[a-z0-9.]+\.(edu|ac\.[a-z]+)|acknowledg|funded by|grant (no|number)' supplement/ | head
unzip -l supplement.zip | grep -Ei '\.git/|/home/|/Users/|\.DS_Store' | head
```

Strip repository owners, institution names, funding lines, and any system named after your group.
A de-anonymizing supplement can trigger a summary reject before the science is even read.

## Honesty over completeness

- If data cannot be shared (privacy, licensing, industrial confidentiality — common in **PAIS**
  applications), **say so and why**, and share what you can (code, a synthetic sample, the
  protocol). A silent gap reads worse than a stated, justified limitation.
- Do not claim reproducibility you have not tested. Run the package from a **clean checkout**
  yourself before submitting.

## Fit the 7-page body

Reproducibility content that a reviewer needs to *judge* the paper (the core proof idea, the
evaluation protocol, the key numbers) belongs in the **body**; full proofs, extra tables, and code
belong in the **supplement**. Nothing decision-critical may live only outside the 7 pages
(`ecai-supplementary`).

## Post-acceptance

Convert the anonymized supplement into a **permanent, open** release — DOI-issuing archive, open
license, de-anonymized owners — and link it from the open-access camera-ready
(`ecai-camera-ready`).

## Output format

```text
[Mode] theory (proof appendix) / empirical (seeded+cached) / mixed
[Proof completeness] every theorem has a full checkable proof + explicit assumptions? yes/no
[Provenance] datasets/models/seeds/env pinned? gaps: <list>
[Claim map] each table/number -> regenerating file
[Anonymity] supplement clean / leaks: <where>
[Body/supplement split] nothing decision-critical outside the 7-page body
[Post-acceptance] DOI + open license + de-anonymized link planned
```
