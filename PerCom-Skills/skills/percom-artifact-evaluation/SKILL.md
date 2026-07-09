---
name: percom-artifact-evaluation
description: Use when packaging an IEEE PerCom sensing artifact and dataset for reproducibility and any badging (IEEE Open Research Objects / Results Reproduced, IEEE DataPort or Zenodo deposit), covering what a ubicomp evaluator checks first for human-subjects sensing data, cross-subject reproduction, de-identification, and honest degrees of reproducibility.
---

# PerCom Artifact Evaluation

Use this for reproducibility packaging. **First, a cycle caveat:** unlike SIGSOFT venues, PerCom
has not historically run a *mandatory* formal artifact-evaluation track with a fixed badge set, and
whether a given edition offers a reproducibility/badging track (e.g., **IEEE Open Research Objects
/ Results Reproduced**) is **待核实** — confirm on the current call. Regardless of whether a badge
is offered, a well-packaged, de-identified sensing dataset and reproducible pipeline is a scored
strength in the double-blind review and a lasting community contribution.

## What "reproducible" means for a ubicomp sensing paper

Two deliverables, kept distinct:

- **The anonymized review package** (at submission): dataset link and code scrubbed of owner,
  testbed, and lab identity, for the double-blind reviewers.
- **The public deposit** (after acceptance): a de-identified dataset and code in a DOI-issuing
  archive under an open license — the version others cite and reuse, and the version any badge
  program evaluates.

## What a ubicomp evaluator opens first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| An activity/context recognizer | The script that regenerates **cross-subject** (LOSO) results | Only a pooled-accuracy script; no leave-one-subject-out path |
| A sensing dataset | The data itself + a datasheet (subjects, sensors, labels) | Link present, data missing; no de-identification described |
| A deployed system | A demo on bundled sample data | Only-runs-on-authors'-testbed; hardware not documented |
| A model result | Trained weights + inference on sample input | Requires the full raw dataset or private compute to run |

Assume an evaluator gives your package a bounded time budget on a clean machine with **no access to
your sensors or subjects**. Design for the first ten minutes — a demo on bundled, de-identified
sample data — to succeed.

## Packaging plan

```text
[Container]   ship a Dockerfile or a pinned environment (requirements/lockfile); avoid
              "install these 40 things by hand"
[README]      one-screen orientation: what it is, install, run the demo, reproduce each claim,
              expected runtime and outputs
[Datasheet]   a dataset datasheet: subjects (count, relevant demographics), sensors (device,
              firmware, sampling rate, placement), labels + protocol, and known biases
[Mapping]     an explicit table: paper claim -> script -> expected result (with the LOSO split)
[Data]        the de-identified dataset itself (or documented restricted-access), not just a query
[Ethics]      IRB/consent status and the de-identification performed before release
[License]     an open, DOI-issuing deposit (IEEE DataPort, Zenodo) so others can reuse and cite
```

## De-identification is the ubicomp-specific bar

Human-subjects sensing data leaks identity in ways code does not: raw audio/video, GPS traces,
timestamps that pinpoint a home, and even accelerometer gait can re-identify. Before any release:

- Remove or transform direct identifiers and re-identifying traces; document exactly what you did.
- Confirm your consent and IRB approval **permit public release** of the de-identified data — some
  approvals do not, and then the honest move is restricted access with a documented request path.
- Never ship a dataset that a subject did not consent to have published.

## Worked vignette: a wearable-HAR dataset + recognizer

To make a HAR paper reproducible: ship a Docker image with the recognizer pre-built; a
`run_demo.sh` that classifies on a small bundled, de-identified sample in under a minute; a
`reproduce/` directory whose scripts regenerate the **leave-one-subject-out F1 table** (not just a
pooled number) from logged features; a datasheet listing subjects, sensor placement, and sampling
rate; the de-identified dataset with a documented consent/IRB basis; and an open license with a
DOI. State honestly which results are turnkey and which need the full (slow) training run.

## Calibration

- Whether a badge/reproducibility track runs, and which badges, is **待核实** per cycle — confirm
  on the current call rather than assuming a SIGSOFT-style scheme.
- The DOI-issuing deposit and datasheet are portable value even when no badge is offered.
- Anonymize the review package; de-identify (and confirm consent for) the public dataset — these
  are different obligations.

## Output format

```text
[Track status] formal reproducibility/badge track this cycle? yes/no/待核实
[Artifact role] anonymized review package / public de-identified deposit
[Contents] <recognizer/dataset/datasheet/scripts/ethics/license>
[Ten-minute test] does install + demo on bundled sample data succeed on a clean machine? yes/no
[Cross-subject reproduction] does a script regenerate the LOSO result? yes/no
[De-identification] documented + consent/IRB permits release? yes/no
[Fixes before deposit] <ordered list>
```
