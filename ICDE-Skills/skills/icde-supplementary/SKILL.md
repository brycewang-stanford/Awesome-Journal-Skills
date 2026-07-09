---
name: icde-supplementary
description: Use when preparing IEEE ICDE supplemental material for the CMT submission: what belongs in the 12-page body versus the supplement, the runnable artifact package (README, run_all.sh, run_small.sh, generators), extended experiments, and single-blind packaging that lets a reviewer assess availability without the body depending on it.
---

# ICDE Supplementary

Use this when assembling ICDE supplemental material. The supplement can support the paper, but
the 12-page body must stand on its own — a reviewer must be able to accept the headline result
without opening it.

## What goes where

- **Body (12 pages):** the mechanism, the pseudocode, the two or three decision-critical
  figures, the mechanism-isolating ablation, and the cost/crossover analysis.
- **Supplement:** extended sweeps, additional baselines, full workload documentation, secondary
  proofs or derivations, and the **runnable artifact package**.
- Do **not** hide essential motivation, the core mechanism, or the primary result in the
  supplement; a paper whose argument lives outside the page budget reads as unreviewable.

## The runnable artifact package

Because ICDE weighs **availability** in the score, treat the artifact as first-class:

- A **README** that orients a reviewer in about a minute: what the system is, how to build it,
  and which command reproduces which figure.
- `run_all.sh` (full reproduction) and `run_small.sh` (a fast subset for a reviewer without a
  cluster), both writing to a predictable output location.
- The **workload generators** with their seeds and parameters, and any real-dataset fetch or
  construction scripts.
- A claims map linking each paper figure to the script and log that produced it.
- A license and, for the camera-ready release, a tagged version matching the paper's numbers.

## What reviewers open first

| Supplement item | Inspection likelihood | Practical implication |
|---|---|---|
| README + run_small.sh | High | Must build and run cleanly on a stock machine |
| Figure-to-script claims map | Medium-high | Every headline figure needs a traceable command |
| Extended sweeps and baselines | Medium | Reference each from the body or it goes unread |
| Full raw logs | Low | Include for completeness, never depend on them |
| Secondary proofs | Variable | Restate the claim before proving it |

## Single-blind packaging

- ICDE is single-blind, so the package need **not** be anonymized. Do not strip author names,
  scrub commit history, or replace the repository URL with a placeholder — that effort is wasted
  here and can even confuse a reviewer expecting an attributed artifact.
- Do still remove **credentials, secrets, cache directories, and large irrelevant files** —
  hygiene, not anonymity, is the concern.

## Vignette: splitting an index-system paper

A submission on a write-optimized index: the body keeps the two-tier mechanism, the lazy-merge
pseudocode, the throughput and latency-tail figures, and the deferral ablation; the supplement
holds the full append-to-scan sweep, an extra RocksDB-style baseline, the trace documentation,
and the artifact with `run_small.sh` reproducing the crossover on one machine. Nothing
decision-critical lives only in the artifact, because deep artifact inspection is at reviewer
discretion.

## Output format

```text
[Supplement status] Ready / Needs fixes / Not ready
[Body vs supplement] <what stays in 12 pages vs moves out>
[Artifact package] <README / run_all.sh / run_small.sh / generators / claims-map>
[Availability signal] <does the supplement demonstrate a runnable artifact? y/n>
[Hygiene checks] <secrets / caches / bloat removed>
[Main-paper dependency] <what breaks if the supplement is ignored>
```
