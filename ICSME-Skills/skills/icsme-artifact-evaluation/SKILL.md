---
name: icsme-artifact-evaluation
description: Use when packaging an IEEE ICSME artifact for the Joint Artifact Evaluation Track and ROSE Festival, covering the IEEE "Open Research Object" and "Research Object Reviewed" badges, what evaluators check first, DOI-issuing archives, evaluator-proof documentation, the shared track with SCAM and VISSOFT, and the separate post-acceptance deadline.
---

# ICSME Artifact Evaluation

Use this for the artifact track. ICSME evaluates artifacts in the **Joint Artifact Evaluation Track
and ROSE Festival** (ROSE = Recognizing and rewarding Open Science in software Engineering), shared
with its co-located siblings **SCAM** and **VISSOFT**, and it awards the **IEEE** badge scheme —
not ACM's four badges. Two things to internalize: the badges are earned by evaluators actually
retrieving and using your package, and the review artifact (anonymized, for the paper's reviewers)
is not the same deliverable as the badge artifact (de-anonymized, permanently archived).

## The IEEE badges (verify the current set and names)

| Badge | What it certifies | What earns it |
|---|---|---|
| Open Research Object | The artifact is permanently, publicly retrievable and open | Deposit in a DOI-issuing archive (Zenodo, figshare, Software Heritage) with an open license |
| Research Object Reviewed | The artifact was examined and is exercisable, well-structured, and documented | Evaluators can run/inspect it and confirm it supports the paper's claims |

A package can earn **both** badges if it is open *and* exercisable, well-structured, and documented
for reuse and repurposing. Open Research Object is the low-cost, high-value badge (archive the
package cleanly); Research Object Reviewed requires the evaluator's own inspection/run to succeed,
so the failure mode is always "did not retrieve or run on their side," never "the idea was weak."

> Do not import ACM badge names (Available / Functional / Reusable / Reproduced) — those are the ACM
> scheme used at FSE and other ACM venues. ICSME is an IEEE venue with the IEEE research-object
> badges. Using the wrong badge names is a tell that the artifact author has not read the ROSE call.

## What ROSE evaluators open first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A maintenance tool | The README and one install/run command | Undocumented dependencies; only-works-on-authors'-laptop |
| A mining/evolution study | The scripts that turn the corpus into the paper's tables | Numbers in the PDF that no script reproduces |
| A mined dataset | The extraction scripts + the extracted corpus with SHAs | Query shipped, corpus missing; provenance unpinned |
| An LLM-based result | Cached prompts/outputs + model IDs | Requires live API keys; not reproducible |

Assume an evaluator gives your package a bounded time budget on a clean machine. Design for the
first ten minutes to succeed.

## Packaging plan

```text
[Container]   ship a Dockerfile or a pinned environment (requirements/lockfile); avoid
              "install these 40 things by hand"
[README]      one-screen orientation: what it is, install, run the demo, reproduce each claim,
              expected runtime and outputs
[Mapping]     an explicit table: paper claim -> script -> expected result
[Corpus]      the extracted mining dataset itself (or documented access), with SHAs and dates,
              not just the query
[Provenance]  repo SHAs, extraction dates, model IDs/dates, seeds, fork/bot handling
[License]     an OSI-approved open license so the artifact can earn Open Research Object
[Archive]     deposit in a DOI-issuing repository for a permanent, citable object
```

## Anonymized review artifact vs. badge artifact

- **At submission:** the artifact is anonymized for the paper's reviewers — no owner strings,
  cluster paths, lab names, your own org's repos, or identity-revealing subject-system names.
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-issuing
  archive; this is the version ROSE evaluators badge and the camera-ready cites.

## Worked vignette: packaging a debt-detection tool + mining study

A paper contributes a technical-debt detection tool and a mining study of debt over release history.
To target both badges: ship a Docker image with the tool pre-built; a `run_demo.sh` that detects
debt on a small bundled repository in under a minute; a `reproduce/` directory whose scripts
regenerate each table from logged mining results; a claim-to-script mapping in the README; the
extracted corpus with pinned SHAs and extraction dates; and an MIT/Apache license with a Zenodo DOI.
State honestly which results are turnkey and which need the full (slow) corpus re-mining.

## Calibration

- The ROSE-Festival artifact deadline is *after* acceptance and shared with SCAM and VISSOFT;
  Journal-First papers are typically excluded — confirm eligibility on the current call.
- Badge names, the exact set offered, and whether evaluation is single- or double-anonymous vary by
  cycle — confirm on the current artifact/ROSE call.

## Output format

```text
[Target badges] Open Research Object / Research Object Reviewed
[Artifact role] anonymized review artifact / public badge artifact
[Contents] <tool/corpus/scripts/provenance/license>
[Ten-minute test] does retrieve + install + demo succeed on a clean machine? yes/no
[Claim mapping] <claim -> script -> expected result present? yes/no>
[Fixes before upload] <ordered list>
```
