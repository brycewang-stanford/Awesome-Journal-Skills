---
name: infocom-artifact-evaluation
description: Use when packaging IEEE INFOCOM code, simulators, and datasets for credibility and optional IEEE reproducibility badges, given that INFOCOM runs no standing artifact-evaluation track, covering DOI-issuing archives, evaluator-proof documentation, what the absence of a formal track changes, and how a released package strengthens a no-rebuttal submission.
---

# INFOCOM Artifact Evaluation

Use this when you want to release an artifact. The first thing to internalize: **INFOCOM has no
standing artifact-evaluation track and no mandatory badge process** (as of 2026-07-09; 待核实
whether a cycle introduces one). Unlike SIGCOMM/NSDI/USENIX ATC — where a separate committee runs
your artifact and awards badges — an INFOCOM artifact is **entirely optional and self-directed**.
That changes the goal: you package not to pass an evaluator, but to make a large, skeptical,
no-rebuttal reviewer pool believe your numbers.

## What the absence of a formal track changes

| At an artifact-track venue (SIGCOMM/NSDI/ATC) | At INFOCOM |
|---|---|
| A committee runs your artifact on a deadline | No one is required to run it |
| Badges (Available/Functional/Reproduced) are awarded | No INFOCOM badge exists (待核实 per cycle) |
| Packaging is a graded deliverable | Packaging is a credibility investment you choose |
| The artifact can lift a borderline decision | A released package pre-empts "I don't believe this" in the PDF |

Because no evaluator is guaranteed, the payoff of a release is **reviewer trust and post-publication
impact**, not a badge. Optimize for a reader who *might* look, and for the researchers who will
build on your simulator after publication.

## IEEE reproducibility options you can opt into

- **IEEE DataPort** — deposit datasets/traces with a DOI and a license.
- **DOI-issuing archives** — Zenodo, figshare, or Software Heritage for a simulator or code release
  with a permanent identifier and an OSI-approved license.
- Some IEEE venues offer **code/data availability badges**; INFOCOM does not mandate them — confirm
  the current cycle's specifics before claiming one (**待核实**).

## What a credible networking release contains

| Contribution type | First thing a reader checks | Common failure to avoid |
|---|---|---|
| An algorithm/protocol | A README and one run command on a small example | Only-runs-on-authors'-cluster; undocumented deps |
| A simulation study | The scripts that regenerate the paper's figures from logged runs | Numbers in the PDF no script reproduces |
| A dataset/trace | The data plus its provenance and preprocessing | Query shipped, data missing; source unstated |
| A learning-for-networking result | Cached inputs/outputs, model IDs, seeds | Requires live API keys; not reproducible |

## Packaging plan (optional but persuasive)

```text
[Container]   a Dockerfile or a pinned environment (requirements/lockfile) for the simulator/tool
[README]      one screen: what it is, how to install, how to run a small demo, how to regenerate
              each figure, expected runtime and outputs
[Mapping]     an explicit table: paper claim/figure -> script -> expected result
[Config]      the exact topology, traffic model, seeds, and parameters used in the paper
[Data]        the trace/dataset (or documented access), not just the generator
[License]     an OSI-approved license so others can build on it
[Archive]     deposit in a DOI-issuing repository (Zenodo/DataPort/Software Heritage)
```

## Double-blind timing

- **At submission:** if you link an artifact for reviewers, anonymize it — no owner strings, cluster
  paths, lab names, or identifying repo — and host it behind an anonymizing service. Nothing
  decision-critical may live only there (reviewers need not open it).
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-issuing
  archive, and make the camera-ready's statements match it.

## Vignette: releasing a scheduling simulator + trace

A paper contributes an edge-scheduling algorithm evaluated by trace-driven simulation. A credible
optional release: a Docker image with the custom simulator pre-built; a `run_demo.sh` that runs one
small scenario in under a minute; a `figures/` directory whose scripts regenerate each plot from
logged runs; a claim-to-script table in the README; the request trace (or documented access) with
its provenance; and an MIT/Apache license with a Zenodo DOI. State honestly which figures are
turnkey and which need the full (slow) trace.

## Calibration

- There is **no artifact deadline** because there is **no artifact track** — do not invent one; the
  only related deadline is the IEEE Xplore camera-ready (`infocom-camera-ready`).
- If a future cycle adds an artifact/badge process, confirm its rules, timing, and anonymity model
  on the current call before advising (**待核实**).

## Output format

```text
[Release decision] release / no release, with reason
[Target] credibility only / IEEE DataPort / DOI archive / (badge if a cycle offers one, 待核实)
[Contents] <simulator/tool + config + data + license>
[Ten-minute test] does install + demo succeed on a clean machine? yes/no
[Figure mapping] <figure -> script -> expected result present? yes/no>
[Anonymity] anonymized for review; de-anonymized DOI archive for camera-ready? yes/no
```
