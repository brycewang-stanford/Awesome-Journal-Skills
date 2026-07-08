# VLDB Resources

Working material that complements the twelve `skills/`. The skills carry the advice;
this directory carries the evidence: verified sources, award-anchored exemplars, a
style demonstration, and the artifact tooling pointer.

## Contents

| File | What it is for |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Every PVLDB/VLDB fact in the pack with its URL and 2026-07-08 access date, the access-method note for the blocked hosts, and the 待核实 ledger. Open this before trusting any deadline. |
| [`external_tools.md`](external_tools.md) | The live official surfaces (volume guidelines, research-track calls, reproducibility pages) plus the do-not-infer rules for a venue that resets its policies every volume. |
| [`exemplars/library.md`](exemplars/library.md) | Four award-anchored real VLDB/PVLDB papers spanning the EA&B, architecture, scale-out, and industrial genres — and a list of famous papers that are *not* VLDB papers. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A fictional LSM-store paper's abstract and introduction rewritten before → after against the pack's page-one rules. |
| [`code/README.md`](code/README.md) | Pointer to the shared artifact smoke-check kit, with a systems-dialect translation of its ML-flavored checks. |

## Scope note

This is a database-systems conference pack. The evidence culture here is measured
systems behavior — throughput and tail-latency curves, scale sweeps, fair competitor
tuning — not statistical estimation, and not the econometrics tooling some journal
packs in this collection carry. Nothing in this directory assumes Stata, causal
inference designs, or training-run seeds beyond their systems analogues.

## A sensible order of use

1. Decide whether and where the project fits with
   [`../skills/vldb-topic-selection`](../skills/vldb-topic-selection/SKILL.md), then pick
   the submission month with [`../skills/vldb-workflow`](../skills/vldb-workflow/SKILL.md).
2. Close the evaluation and artifact gaps using
   [`../skills/vldb-experiments`](../skills/vldb-experiments/SKILL.md),
   [`../skills/vldb-reproducibility`](../skills/vldb-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Calibrate the writing against [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md)
   and the real papers in [`exemplars/library.md`](exemplars/library.md).
4. In the final week, re-verify every date and rule through
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) — PVLDB's clock is the 1st of the month at
   5:00 PM Pacific, and it does not move.
