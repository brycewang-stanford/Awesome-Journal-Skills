---
name: dac-artifact-evaluation
description: Use when packaging the code, benchmarks, and flows behind an ACM/IEEE Design Automation Conference (DAC) Research Manuscript into a credible, reusable artifact — given that DAC has historically run no formal artifact-evaluation or badge-issuing track (verify per cycle), so the goal is reviewer credibility and community reuse via open EDA flows and DOI-archived releases, not an ACM badge.
---

# DAC Artifact Evaluation

Read the venue reality first. Unlike the software-engineering venues (FSE/ICSE/ISSTA) and the
computer-architecture venues (MICRO/ISCA/HPCA), **DAC has historically not operated a standing,
badge-issuing artifact-evaluation track** for research manuscripts; whether the current cycle adds
one is **待核实** (`resources/official-source-map.md`). So do not build for an ACM badge that DAC
does not award. Build instead for the two things that actually matter at DAC: **making a skeptical
reviewer trust your QoR numbers** and **making the community able to reuse and cite your work**.

## What an EDA artifact is for at DAC

| Goal | What it buys you | How it is earned |
|---|---|---|
| Reviewer credibility | A QoR claim that reads as real, not cherry-picked | Standard benchmarks, disclosed flow, a runnable path |
| Community reuse | Citations and follow-on work built on your tool | Clean open-source release, good docs, a license |
| Contest/leaderboard standing | Recognition on ISPD/TAU/CAD-contest tasks | A tool that runs on the contest harness |

There is no badge to chase, so the design target is a package a stranger can run and a reviewer
would believe — not a checklist an evaluator scores.

## Packaging plan for an EDA artifact

```text
[Flow]        pin the toolchain: OpenROAD / ABC / Yosys / KLayout versions, or a Docker image;
              avoid "install these commercial tools yourself" as the only path
[Benchmarks]  ship or clearly reference the exact benchmark release (ISPD/EPFL/ISCAS/ITC/TAU/
              CircuitNet) with its version
[PDK/library] include the open PDK/library used (Nangate/ASAP7) or document the NDA-gated one
[README]      what it is; how to install; how to run one small demo in minutes; how to reproduce
              each headline QoR number; expected runtime and outputs
[Mapping]     an explicit table: paper claim -> script + benchmark -> expected QoR result
[Seeds]       fixed seeds and a note on nondeterminism for stochastic/RL flows
[License]     an OSI-approved license so others can build on it
[Archive]     deposit a versioned release in a DOI-issuing archive (Zenodo/Software Heritage) after
              acceptance for a stable citation
```

## The clean-machine, bounded-time test

Even without formal evaluators, assume a reviewer or a future user gives your package a short,
bounded try on a clean machine. Design the **first ten minutes to succeed**:

- A one-command small demo that runs a tiny circuit through your tool and prints a recognizable QoR
  number.
- No dependency on the authors' cluster, private PDK, or a live license server for the demo path.
- A clear separation between the fast demo and the slow full-benchmark reproduction (which may take
  hours on large designs — say so).

## Anonymized review artifact vs public release

- **At submission (double-blind):** if you link the artifact for reviewers, anonymize it exactly like
  the paper — no author/lab names, no personal repos, no cluster paths, no commercial-flow
  fingerprints. Reviewers are not required to open it, so it can only strengthen a paper that already
  stands on six pages.
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-archived
  release cited in the camera-ready; this is the version the community reuses.

## Worked vignette: packaging a placement tool + benchmarks

A paper contributes an ML-guided placer evaluated on ISPD circuits. A credible, reusable package:
a Docker image with the placer and an OpenROAD flow pre-built; a `run_demo.sh` that places one small
ISPD circuit and reports wirelength/DRC in under a minute; a `reproduce/` directory whose scripts
regenerate each per-benchmark table with fixed seeds; a claim-to-script-to-benchmark mapping in the
README; the exact ISPD release and an open PDK; the trained model checkpoint and the train/test
design split; and an MIT/Apache license. State plainly which numbers are turnkey and which need the
slow full-suite run on a large machine.

## Calibration

- Do **not** assume a DAC artifact badge exists; verify the current cycle before promising one.
- If DAC or a co-located workshop *does* introduce an artifact/open-source track in a given year,
  re-read its specific rules — do not assume ACM SIGSOFT-style badge names transfer.
- The payoff is credibility and citations; budget the artifact accordingly, not as a graded
  deliverable.

## Output format

```text
[Artifact goal]   reviewer credibility / community reuse / contest harness
[Contents]        tool + flow versions / benchmarks + version / PDK / model + split / license
[Ten-minute test] does install + small demo succeed on a clean machine? yes/no
[Claim mapping]   claim -> script -> benchmark -> expected QoR present? yes/no
[Anon vs public]  anonymized review artifact / DOI-archived public release planned? yes/no
[Badge check]     does this cycle actually run an artifact track? verify -> yes/no/待核实
```
