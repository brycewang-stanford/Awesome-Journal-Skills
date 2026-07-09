---
name: tacas-artifact-evaluation
description: Use when packaging a TACAS (ETAPS) artifact for the ETAPS Artifact Badges (Available, Functional, Reusable), covering the two-round model (mandatory, PC-parallel evaluation for tool and tool-demo papers vs voluntary post-acceptance evaluation for research and case-study papers), what the AEC checks on the clean evaluation VM, DOI-issuing archives, and evaluator-proof documentation.
---

# TACAS Artifact Evaluation

Use this for the artifact track. TACAS treats the artifact as a **first-class citizen**, and the
process differs from most venues in two ways: for **tool** papers it is **mandatory and runs in
parallel with paper review**, and badging follows the **ETAPS Artifact Badge** guidelines, decided
by the **Artifact Evaluation Committee (AEC)** and printed on the paper's title page.

## The two rounds (know which one you are in)

| Round | Applies to | Timing | Consequence |
|---|---|---|---|
| Round 1 — mandatory | Regular **tool** + **tool-demonstration** papers | Submitted right after the paper, evaluated **with the PC** | Outcome **feeds the acceptance decision** |
| Round 2 — voluntary | Regular **research** + **case-study** papers | **After** acceptance notification | Earns title-page badges; does not gate acceptance |

The consequence for a tool paper is blunt: a package that does not build or run on the clean
evaluation VM can cost the paper, not merely a badge. Treat the artifact as a co-equal deliverable
due about two weeks after the paper.

## The ETAPS Artifact Badges

| Badge | What it certifies | What earns it |
|---|---|---|
| **Available** | The artifact is permanently, publicly retrievable | Deposit in a DOI-issuing archive (Zenodo, figshare, Software Heritage) |
| **Functional** | The artifact runs and does what the paper says | A clean-VM install, a smoke run, and documented expected outputs |
| **Reusable** | Others can build on and adapt it | The Functional bar plus careful docs, structure, licensing, and generality |

The AEC decides which subset a given artifact receives. *Available* is low-cost, high-value (archive
the package); *Functional* and *Reusable* require the evaluator's own run to succeed on the provided
VM, so the failure mode is always "did not run in their environment," never "the idea was weak."

## What the AEC opens first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A verification tool | The README and one smoke command on the VM | Undocumented deps; needs network; only-builds-on-authors'-machine |
| A benchmark comparison | The script that regenerates the headline table | Numbers in the PDF no script reproduces |
| A soundness claim | The validation / witness-checking path | "Fast" results that were never checked for correctness |
| A tool-demonstration | The documented demo walkthrough | The demo the paper describes cannot be driven on the VM |

Assume a bounded evaluator time budget on the **clean ETAPS VM**. Design for the first ten minutes
to succeed: a smoke run that finishes fast and prints an expected output.

## Packaging plan

```text
[VM-ready]    a package that builds/runs inside the provided VM image, offline, deps vendored
[README]      one screen: what it is, smoke run, per-claim reproduction, expected outputs + runtimes
[Mapping]     an explicit table: paper claim -> script -> expected result
[Benchmarks]  the actual task set vendored (or documented access), not just a pointer
[Validation]  a witness-checking or cross-tool script for any soundness/correctness claim
[License]     an OSI-approved license so the artifact can be badged Reusable
[Archive]     deposit in a DOI-issuing repository for the Available badge (esp. at camera-ready)
```

## Anonymity by category (do not get this backwards)

- **Round-1 tool / tool-demo artifacts are single-blind** — they may carry the tool identity and
  authorship, matching the single-blind paper.
- **Round-2 research artifacts are submitted after acceptance**, so anonymity is no longer the
  concern; but a **research review artifact** attached to the double-blind paper (if you choose to
  supply one at submission) must be anonymized — no owner strings, lab names, or identity-revealing
  repository URLs.

## Worked vignette: badging a model-checking tool

A regular tool paper contributes a new checker. To target Available + Functional + Reusable: ship a
VM-ready image with the tool prebuilt; a `smoke.sh` that verifies one small bundled task in under a
minute; a `reproduce/` directory whose scripts regenerate the benchmark table from logged runs; a
claim-to-script mapping in the README; the vendored benchmark set; a witness-validation script for
the soundness claim; and an Apache/MIT license. State honestly which results are turnkey and which
need the full (slow) benchmark run. Deposit the final version on Zenodo for the DOI.

## Calibration

- The badge set, the round structure, and the VM image are set per edition on the `tacas.info`
  artifact page — confirm the current guidelines and image before packaging.
- Do not conflate the mandatory Round-1 deadline with the voluntary Round-2 or the camera-ready;
  they are distinct dates.

## Output format

```text
[Round] mandatory (tool/tool-demo, PC-parallel) / voluntary (research/case-study, post-acceptance)
[Target badges] Available / Functional / Reusable
[Clean-VM test] does build + smoke run succeed offline on the provided VM? yes/no
[Claim mapping] <claim -> script -> expected result present? yes/no>
[Archive] DOI-issuing deposit ready for Available? yes/no
[Fixes before upload] <ordered list>
```
