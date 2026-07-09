---
name: vis-artifact-evaluation
description: Use when packaging an IEEE VIS artifact for the Graphics Replicability Stamp Initiative (GRSI) / TVCG Replicability Stamp and the IEEE VIS Open Practices program, covering what an independent GRSI volunteer reproduces first, DOI-issuing archives, evaluator-proof documentation for visualization code and data, and how VIS reproducibility differs from ACM-style artifact badges.
---

# VIS Artifact Evaluation

Use this for the reproducibility track. IEEE VIS does not use ACM-style artifact badges; its
recognition is the **Graphics Replicability Stamp Initiative (GRSI)** — issued to TVCG papers as the
**TVCG Replicability Stamp** — plus the conference's **Open Practices** program. Two things to
internalize: the stamp is earned by an **independent volunteer actually reproducing your results**
from a public archive, and the review artifact (anonymized, for your paper's reviewers) is not the
same deliverable as the stamp artifact (de-anonymized, permanently archived).

## What GRSI certifies (verify the current process)

| Mechanism | What it certifies | What earns it |
|---|---|---|
| TVCG Replicability Stamp (GRSI) | An independent volunteer reproduced the paper's results from your code/data | A public repository + a single documented build/run path that regenerates the key figures/results |
| Open Practices disclosures | Transparent reporting of open code, data, preprints, preregistration | Filling the camera-ready Open Practices form honestly and posting the materials |

Unlike a graded badge ladder, the stamp is **binary**: an evaluator either reproduces your results
or does not. The failure mode is therefore always "it did not build/run on their machine," never
"the idea was weak" — design for a stranger's clean environment.

## What a GRSI volunteer opens first

| Claim type | First thing reproduced | Common failure caught |
|---|---|---|
| A visualization technique/algorithm | The build + a script that regenerates a key figure | Undocumented deps; only-builds-on-authors'-GPU |
| A system/tool | The install and a demo on bundled sample data | Requires a private server, API key, or paid license |
| A perceptual/empirical study | The analysis scripts that turn raw responses into the paper's stats | Numbers in the PDF no script reproduces; raw data missing |
| A rendering result | The pipeline + reference images with a comparison | Non-deterministic output with no tolerance/seed documented |

Assume the evaluator gives your package a bounded time budget on a clean machine. The first build
and the first regenerated figure must succeed.

## Packaging plan

```text
[Container]   ship a Dockerfile or a pinned environment (requirements/lockfile, exact toolchain
              versions); avoid "install these 40 things by hand" and undocumented GPU/driver needs
[README]      one-screen orientation: what it is, how to build, how to run the demo, how to
              regenerate each figure/result, expected runtime and outputs
[Mapping]     an explicit table: paper figure/result -> script -> expected output
[Data]        the actual dataset or stimuli (or documented access), not just a pointer
[Determinism] seeds, tolerances, and reference images for anything stochastic or GPU-dependent
[License]     an OSI-approved license so others can reuse the visualization code
[Archive]     deposit in a DOI-issuing repository (OSF, Zenodo, Software Heritage) for permanence
```

## Anonymized review artifact vs. stamp artifact

- **At submission (if double-blind):** the supplemental code/data/video is anonymized for the
  paper's reviewers — no owner strings, lab names, institutional URLs, or identity-revealing demo
  links, and no live repository that discloses authors.
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-issuing
  archive; this is the version a GRSI volunteer reproduces and the camera-ready cites.

## Worked vignette: stamping a technique + system paper

A paper contributes a new graph-layout technique and an interactive system. To target the stamp:
ship a Docker image with the layout code pre-built; a `run_demo.sh` that lays out a small bundled
graph and writes the teaser figure in under a minute; a `reproduce/` directory whose scripts
regenerate each quantitative figure from logged benchmark data; a figure-to-script mapping in the
README; the benchmark graphs themselves with provenance; and an MIT/BSD license. State honestly
which figures are turnkey and which need the full (slow) benchmark run.

## Calibration

- The GRSI review is **independent of and after** camera-ready; do not conflate them, and do not
  block the paper on the stamp result.
- The exact GRSI submission process, the Open Practices requirements, and whether any element is
  mandatory vary by cycle — confirm on the current Open Practices page and the GRSI site.

## Output format

```text
[Target recognition] TVCG Replicability Stamp / Open Practices disclosures
[Artifact role] anonymized review artifact / public stamp artifact
[Contents] <code/data/stimuli/determinism aids/license>
[Clean-machine test] does build + demo + one regenerated figure succeed? yes/no
[Figure mapping] <figure/result -> script -> expected output present? yes/no>
[Fixes before archiving] <ordered list>
```
