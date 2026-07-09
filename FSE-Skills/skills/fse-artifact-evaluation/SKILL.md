---
name: fse-artifact-evaluation
description: Use when packaging an ESEC/FSE artifact for the ACM Artifact Review and Badging scheme (Artifacts Available, Evaluated Functional and Reusable, Results Reproduced), covering what SIGSOFT evaluators check first, DOI-issuing archives, evaluator-proof documentation, and the separate post-acceptance artifact deadline.
---

# FSE Artifact Evaluation

Use this for the artifact track. FSE follows the **ACM Artifact Review and Badging** scheme, and
the artifact evaluation is a **separate, post-acceptance** process with its own deadline. Two
things to internalize: badges are earned by evaluators actually using your package, and the review
artifact (anonymized, for the paper's reviewers) is not the same deliverable as the badge artifact
(de-anonymized, permanently archived).

## The ACM badges (verify the current set and names)

| Badge | What it certifies | What earns it |
|---|---|---|
| Artifacts Available | The artifact is permanently, publicly retrievable | Deposit in a DOI-issuing archive (Zenodo, figshare, Software Heritage) |
| Artifacts Evaluated - Functional | The artifact runs and does what the paper says | A clean-machine install, a demo, and documented expected outputs |
| Artifacts Evaluated - Reusable | Others can build on it | The Functional bar plus careful docs, structure, and licensing |
| Results Reproduced | An evaluator reproduced the paper's key results | A turnkey path from the artifact to the headline numbers |

Available is a low-cost, high-value badge (archive the package); Functional/Reusable/Reproduced
require the evaluator's own run to succeed, so the failure mode is always "did not run on their
machine," never "the idea was weak."

## What SIGSOFT evaluators open first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A tool/technique | The README and one install/run command | Undocumented dependencies; only-works-on-authors'-laptop |
| An empirical study | The scripts that turn data into the paper's tables | Numbers in the PDF that no script reproduces |
| A mined dataset | The extraction scripts + the extracted data | Query shipped, data missing; provenance unpinned |
| An LLM-based result | Cached prompts/outputs + model IDs | Requires live API keys; not reproducible |

Assume an evaluator gives your package a bounded time budget on a clean machine. Design for the
first ten minutes to succeed.

## Packaging plan

```text
[Container]   ship a Dockerfile or a pinned environment (requirements/lockfile); avoid
              "install these 40 things by hand"
[README]      one-screen orientation: what it is, how to install, how to run the demo, how to
              reproduce each claim, expected runtime and outputs
[Mapping]     an explicit table: paper claim -> script -> expected result
[Data]        the extracted dataset itself (or documented access), not just the query
[Provenance]  repo SHAs, extraction dates, model IDs/dates, seeds
[License]     an OSI-approved license so the artifact can be badged Reusable
[Archive]     deposit in a DOI-issuing repository for the Available badge
```

## Anonymized review artifact vs. badge artifact

- **At submission:** the artifact is anonymized for the paper's reviewers — no owner strings,
  cluster paths, lab names, or identity-revealing links, and no live repository that discloses
  authors.
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-issuing
  archive; this is the version the artifact evaluators badge and the camera-ready cites.

## Worked vignette: packaging a detection tool + study

A paper contributes a defect-detection tool and an empirical evaluation. To target Reusable and
Reproduced: ship a Docker image with the tool pre-built; a `run_demo.sh` that detects on a small
bundled project in under a minute; a `reproduce/` directory whose scripts regenerate each table
from logged results; a claim-to-script mapping table in the README; the extracted evaluation
dataset with pinned SHAs; and an MIT/Apache license. State honestly which results are turnkey and
which need the full (slow) dataset run.

## Calibration

- The artifact deadline is *after* acceptance and independent of the camera-ready; do not conflate
  them.
- Badge names, the exact set offered, and whether evaluation is single- or double-anonymous vary by
  cycle — confirm on the current artifact-track call.

## Output format

```text
[Target badges] Available / Functional / Reusable / Reproduced
[Artifact role] anonymized review artifact / public badge artifact
[Contents] <tool/data/scripts/provenance/license>
[Ten-minute test] does install + demo succeed on a clean machine? yes/no
[Claim mapping] <claim -> script -> expected result present? yes/no>
[Fixes before upload] <ordered list>
```
