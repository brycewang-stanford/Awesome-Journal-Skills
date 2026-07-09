---
name: vis-reproducibility
description: Use when strengthening IEEE VIS reproducibility and open-practices evidence, covering the open-materials statement, anonymized-but-runnable code and stimuli, preregistration of perceptual and user studies, provenance for datasets and rendering pipelines, claim-to-figure mapping, honest degrees of reproducibility, and consistency between what the TVCG paper says and what the supplemental archive contains.
---

# VIS Reproducibility

Use this before submission and again before camera-ready. IEEE VIS's Open Practices posture and the
**Graphics Replicability Stamp** make reproducibility a visible dimension, not a courtesy: reviewers
routinely open the supplemental code, data, and video, and the TVCG camera-ready collects
open-practices disclosures. The goal is that a competent reader could rebuild your figures, rerun
your study analysis, and reach your conclusions.

## Evidence map

- Map each **figure, quantitative result, and study finding** to a **verifiable location** — a
  section, a figure generated from logged data, or a script in the supplemental archive.
- For **techniques and rendering**, give enough of the algorithm, parameters, and environment
  (including GPU/driver assumptions and tolerances) that a reader could re-implement or re-run.
- For **empirical and perceptual studies**, report participants and recruitment, apparatus/stimuli,
  the task, the design (within/between), measures, statistics, and the analysis scripts.
- Keep the **open-materials statement** truthful and specific: what is shared, where it lives, and —
  if something cannot be shared — exactly why.
- Keep the paper and the archive **consistent**: a number in the PDF that no script reproduces is
  the contradiction reviewers read as carelessness.

## Open-materials statement audit

| Claim in the paper | Weak availability answer | VIS-ready answer |
|---|---|---|
| "We render/lay out X" | "Code available on request" | Public, licensed repo with a build path that regenerates the teaser figure |
| "Our system supports task Y" | "Demo will be released" | Runnable build (or Docker) with bundled sample data and a demo script |
| "N participants judged Z" | Nothing (privacy cited vaguely) | Anonymized responses, stimuli, the analysis notebook, and the ethics/consent note |
| "We evaluated on dataset D" | Named but not shared | The dataset or documented access + the preprocessing scripts |

"Available on request" reads as *not available*; convert every such line into a concrete,
anonymized archive or an explicit, justified exception.

## Preregistration for studies (a distinctly VIS-valued move)

Perceptual experiments and controlled user studies benefit from **preregistration** (e.g., on OSF):
locking hypotheses, design, sample size, and the analysis plan before data collection separates
confirmatory from exploratory findings and blunts the "you fished for that result" objection.

```text
[Preregister]  hypotheses, conditions, planned N + power analysis, primary DV, analysis plan
[Cite it]      reference the (anonymized) preregistration in the paper; report deviations honestly
[Separate]     label confirmatory vs. exploratory results; do not present post-hoc as planned
```

## Provenance pinning

```text
[Datasets]   record source and version; archive the actual data or stimuli, not just a query/URL;
             document any cleaning/filtering with the script
[Rendering]  pin toolchain and library versions; provide reference images and a comparison
             tolerance for GPU-dependent or non-deterministic output
[Studies]    store raw per-participant responses (anonymized), the exact stimuli, and timing
[Compute]    state hardware and runtime so a reader can size a reproduction
[Randomness] log seeds; say what is and is not deterministic
```

## Degrees of reproducibility (state the one you achieved)

- **Turnkey:** one documented command regenerates each figure/result from logged data.
- **Scripted:** scripts exist but need documented manual steps, large data, or specific hardware.
- **Descriptive:** prose detailed enough that a competent reader could rebuild the pipeline.

For VIS, aim **turnkey** for anything an evaluator might rerun quickly (a figure from logged
benchmark data, a study's statistics from anonymized responses); a large rendering benchmark or a
proprietary dataset may stay scripted with access clearly documented. Stating the achieved level
honestly beats promising turnkey behavior that fails on a clean machine — the GRSI stamp is decided
exactly there.

## Vignette: a technique-plus-study paper

A paper contributing a new encoding and a controlled study evaluating it. Its reproducibility
spine: the encoding code with a script that regenerates each figure; the study's stimuli and
anonymized per-participant responses; the preregistration for the confirmatory hypotheses; the
analysis notebook that turns responses into the reported effect sizes and CIs; and one honest
sentence about anything (identifiable video, proprietary data) that cannot be shared and why.

## Consistency and camera-ready pass

- Before submission: every scored number and figure traces to the archive; the open-materials
  statement matches reality; if double-blind, the archive is anonymized (no owner strings, lab
  names, or institutional URLs).
- Before camera-ready: swap anonymized links for permanent, DOI-issuing archives, complete the Open
  Practices form, and align the package with what you submit to GRSI (`vis-artifact-evaluation`).

## Output format

```text
[Claim inventory] <figure/result/finding -> evidence location>
[Open materials] concrete / vague / missing
[Preregistration] present / not applicable / should have (for studies)
[Provenance gaps] <dataset versions / rendering references / study raw data / seeds>
[Reproducibility level] turnkey / scripted / descriptive, stated honestly
[Paper fixes] <must appear in the PDF>
[Archive fixes] <additions before upload>
```
