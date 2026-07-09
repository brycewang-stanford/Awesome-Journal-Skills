---
name: ase-artifact-evaluation
description: Use when preparing an accepted ASE (IEEE/ACM Automated Software Engineering) paper's tool and data for the Artifact Evaluation track, targeting the ACM Artifacts Available and Artifacts Reusable badges on the track's own deadline, with the badge shown on the paper's front page in both IEEE Xplore and the ACM Digital Library.
---

# ASE Artifact Evaluation

Convert the accepted paper's package into **badges**. ASE runs an **Artifact Evaluation** track
offering the **Artifacts Available** and **Artifacts Reusable** badges (ACM scheme). Because ASE
proceedings are indexed in **both IEEE Xplore and the ACM Digital Library**, an earned badge appears
on the paper's front page in both. Evaluation happens on the track's **own deadline**, separate from
the research-track notification — stage the package before then.

## The two badges (verify the current call)

- **Artifacts Available** — the artifact is placed in a **publicly accessible archival repository**
  with a **DOI** (Zenodo, figshare, Software Heritage, or an institutional/ACM repository). A
  personal GitHub link alone is not archival; mint a DOI.
- **Artifacts Reusable** — the artifact significantly exceeds minimal functionality: it is
  **carefully documented and well-structured** so a third party can **reuse** the tool, not merely
  reproduce your tables. This is the higher bar and where automated-SE tools usually need the most
  work.
- Whether **Functional** and **Results Reproduced** badges are also offered at a given edition is
  **待核实** — confirm on the current Artifact Evaluation call.

## From the submission artifact to the badge artifact

The review-time (anonymized) artifact and the badge artifact are the same package matured. After
acceptance you can **de-anonymize** it, but the substance should already be there if you followed
`ase-reproducibility`.

```text
[De-anonymize]  restore the real tool name, authors, repository, license.
[Archive]       deposit in a DOI-issuing archive; the DOI is what "Available" certifies.
[Document]      README with exact run path, expected outputs, and a small worked example.
[Environment]   container/lockfile pinning deps + the exact tool commit; note hardware needs.
[Reuse story]   show how to run the tool on a NEW input, not just replay your experiments.
```

## Reusable is about strangers, not your tables

Evaluators judge **reusability**, so write for someone who wants to use your automation on their own
code:

- A clear entry point and documented inputs/outputs.
- Instructions to run on a **new** subject, with a template config.
- Sensible structure (source vs. data vs. scripts), an open **license**, and dependency pinning.
- Removal of dead scripts, secrets, and machine-specific paths.

## Evaluator-proofing checklist

```text
[Runs clean]   fresh environment (container) -> documented command -> expected output, no manual patching
[DOI]          archival deposit with a DOI + open license (for Available)
[Docs]         README covers install, run, expected results, and reuse on a new input (for Reusable)
[Provenance]   subject SHAs, dataset version, seeds, model IDs/dates + cached outputs included
[Scope honesty] hardware/time requirements and known limitations stated up front
[No secrets]   API keys, tokens, private paths removed
```

## Timing and scope

- The Artifact Evaluation deadline follows research-track acceptance; treat it as a real milestone,
  not an afterthought — a strong tool with a weak package earns no badge.
- Evaluators are often students and junior researchers on a schedule: an artifact that needs a live
  API key, unpinned dependencies, or your specific cluster will fail on setup regardless of the
  underlying quality.
- Badges are recognition, not re-review of the science; the paper is already accepted. The goal is
  durable, reusable automation.

## Output format

```text
[Target badges] Available / Reusable (Functional/Reproduced 待核实 for this edition)
[Archive] DOI minted? open license?
[Runs clean] fresh-env command -> expected output, no manual fixes?
[Reusable] docs + run-on-new-input path present?
[Provenance] SHAs / dataset version / seeds / model IDs / cached outputs bundled?
[Blockers] <ordered fixes before the AE deadline>
```
