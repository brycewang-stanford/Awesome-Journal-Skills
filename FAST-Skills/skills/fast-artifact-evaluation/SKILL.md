---
name: fast-artifact-evaluation
description: Use when packaging a USENIX FAST artifact for the USENIX Artifact Evaluation scheme (Artifacts Available, Artifacts Functional, Results Reproduced), covering what a storage AEC checks first, DOI-issuing archives, the artifact appendix, and the special challenges of storage artifacts that need specific devices, large traces, or long endurance runs on the separate post-acceptance timeline.
---

# FAST Artifact Evaluation

Use this for the artifact track. FAST follows the **USENIX artifact-evaluation** model, and
evaluation is a **separate, post-acceptance** process with its own timeline and an Artifact
Evaluation Committee (AEC). Two things to internalize: badges are earned by evaluators actually using
your package, and the review-time artifact (anonymized, for the paper's reviewers) is not the same
deliverable as the badge artifact (de-anonymized, permanently archived, with an artifact appendix).

## The three USENIX badges (verify the current set and names)

| Badge | What it certifies | What earns it |
|---|---|---|
| Artifacts Available | The artifact is permanently, publicly retrievable | Deposit in a DOI-issuing archive (Zenodo, figshare, Software Heritage) |
| Artifacts Functional | The artifact works and is useful for the paper's outcomes | A documented build/run, a demo, and expected outputs on the AEC's setup |
| Results Reproduced | An evaluator reproduced the paper's main results | A path from the artifact to the headline numbers |

Available is a low-cost, high-value badge (archive the package). Functional and Reproduced require the
evaluator's own run to succeed — and for a storage paper that run may need **specific hardware**,
which shapes everything below.

## The storage-artifact problem: hardware dependence

A storage result often depends on a particular SSD/NVM device, firmware, or a large trace. Design the
package so an AEC can get as far as possible without your exact drive:

```text
[Tier the claims]  which results are hardware-agnostic (analysis, plots from logs) vs. device-bound
                   (measured WA, tail latency)? Make the agnostic ones turnkey.
[Ship the logs]    include the raw device-counter logs and the scripts that turn them into figures,
                   so "Reproduced" is achievable from data even when the device is unavailable
[Document devices] state exact models + firmware; where feasible, offer a smaller commodity-SSD path
                   the AEC can run to see the trend, and say the factor is device-specific
[Bound the runtime] long endurance/aging runs: provide a short demo + the full slow protocol, and
                   label which results need the full run
```

## What a storage AEC opens first

| Claim type | First thing inspected | Common failure caught |
|---|---|---|
| A storage system/tool | The README and one build+run command | Undocumented deps; only-builds-on-authors'-kernel |
| A measured storage cost (WA/latency) | The logs + the script from logs to the figure | Numbers in the PDF no script regenerates |
| A trace-driven study | The replay tool + the archived trace | Trace named, not shipped; replay settings missing |
| A crash-consistency claim | The fault-injection / replay harness | Only the FS code, no way to reproduce the test |
| A reliability field study | The (de-identified) dataset + analysis scripts | Aggregates only; nothing an evaluator can re-run |

Assume an evaluator gives your package a bounded time budget. Design for the first ten minutes (build
+ a small demo + a figure-from-logs) to succeed.

## Packaging plan

```text
[Container]   ship a Dockerfile or a pinned environment; avoid "install these 40 things by hand"
[README]      one screen: what it is, build, run the demo, reproduce each claim, expected runtime/outputs
[Mapping]     an explicit table: paper claim -> script -> expected result (mark device-bound ones)
[Data]        the archived traces and raw device-counter logs, not just names
[Provenance]  device models + firmware, host/kernel, mkfs/mount options, seeds
[License]     an OSI-approved license so the artifact can be evaluated toward Functional/Reproduced
[Archive]     deposit in a DOI-issuing repository for the Available badge
[Appendix]    write the artifact appendix; add the earned badges to the camera-ready appendix after AE
```

## Anonymized review artifact vs. badge artifact

- **At submission:** anonymized for the paper's reviewers — no owner strings, hostnames, cluster
  paths, serials in device dumps, lab names, or identity-revealing trace hosts.
- **After acceptance:** replace anonymized placeholders with the public, licensed, DOI-issuing
  archive; write the **artifact appendix**; this is the version the AEC badges and the camera-ready
  cites, with badges shown on the first page.

## Worked vignette: packaging a KV-store + measurement study

A paper contributes an SSD-conscious KV store and a write-amplification study. To target Reproduced:
ship a Docker image with the store pre-built; a `run_demo.sh` that runs a short YCSB load on a
commodity SSD (or a loopback file) in minutes; a `reproduce/` directory whose scripts regenerate each
figure **from the shipped device-counter logs** so the headline numbers reproduce even without the
exact datacenter SSD; a claim-to-script table marking which results are device-bound; the archived
trace with replay scripts; and an MIT/Apache license. State honestly which numbers are the specific
drive's and which are the trend.

## Calibration

- The artifact timeline is *after* acceptance and independent of the camera-ready deadline; do not
  conflate them.
- Badge names, the exact set offered, and whether AE is single- or double-anonymous vary by cycle
  (**待核实** for the precise FAST '27 AEC anonymity model) — confirm on the current Call for
  Artifacts.

## Output format

```text
[Target badges] Available / Functional / Reproduced
[Artifact role] anonymized review artifact / public badge artifact
[Contents] <system/traces/device-logs/scripts/provenance/license>
[Hardware tiering] <which claims turnkey-from-logs vs. device-bound; demo path present?>
[Ten-minute test] does build + demo + a figure-from-logs succeed on a clean machine? yes/no
[Fixes before upload] <ordered list>
```
