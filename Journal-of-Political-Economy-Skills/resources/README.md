# JPE Resources

Action-oriented resources for the Journal of Political Economy (JPE) skill pack. The `skills/` give
advice; this directory lets an agent **act** — run the empirical pipeline, model a JPE-style section, and
benchmark against verified exemplars. Pair these with the relevant `skills/jpe-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`code/`](code/) | Run a reproducible Stata + Python causal-inference pipeline (TWFE → heterogeneity-robust DID, IV with effective-F, RDD, DML, mechanism, robustness, three-line tables). Vendored, command-verified on Stata 18 MP. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper introduction in JPE house style (economics-first, mechanism-driven, Chicago author-date). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified JPE papers** organized by method × topic. Design positioning only — no fabricated numbers. |
| [`official-source-map.md`](official-source-map.md) | **JPE-specific policy & facts:** Editorial Manager submission, Chicago author-date, JPE Dataverse / DCAS data policy, the JPE Data Editor, editors/history/scope, the $250/$125 fee, and the 2023 JPE Micro / JPE Macro companions. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools and services referenced by the pack. |

## Shared empirical-methods kit (venue-neutral, cross-pack)

JPE-specific policy lives in [`official-source-map.md`](official-source-map.md). The general
empirical-craft prose is shared across journal packs and lives in the repo's shared kit:

- [`../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
  — the standard referee objections (identification, inference, robustness, mechanism) and how to
  pre-empt them.
- [`../../shared-resources/empirical-methods/reporting-standards.md`](../../shared-resources/empirical-methods/reporting-standards.md)
  — what every empirical result must report (estimator, SE/clustering, sample, diagnostics) to clear a
  top-5 reviewer.
- [`execution-with-mcp`](../../shared-resources/empirical-methods/execution-with-mcp.md)
  — **the last mile: guidance → a fitted, audited result.** Maps each design family to the concrete StatsPAI / Stata MCP tools, so this pack's empirical skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number.

The [`code/`](code/) directory is **vendored** from
[`../../shared-resources/empirical-methods/code`](../../shared-resources/empirical-methods/code) so this
plugin is self-contained; its commands are verified on Stata 18 MP (2026-06). Fix issues upstream and
re-vendor rather than editing the copy here.

## Suggested workflow

1. Scope and frame with [`../skills/jpe-topic-selection`](../skills/jpe-topic-selection/SKILL.md) (the
   mechanism / theory-linkage fit test and JPE-proper vs. JPE Micro / JPE Macro routing) and
   [`../skills/jpe-writing-style`](../skills/jpe-writing-style/SKILL.md); model the intro on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), positioning it with
   [`../skills/jpe-literature-positioning`](../skills/jpe-literature-positioning/SKILL.md).
2. Identify and estimate with [`code/`](code/), guided by
   [`../skills/jpe-identification`](../skills/jpe-identification/SKILL.md) and
   [`../skills/jpe-robustness`](../skills/jpe-robustness/SKILL.md); integrate theory with
   [`../skills/jpe-theory-model`](../skills/jpe-theory-model/SKILL.md).
3. Pre-empt referees with the shared
   [`reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
   and report to the shared
   [`reporting-standards.md`](../../shared-resources/empirical-methods/reporting-standards.md).
4. Benchmark against verified JPE papers in [`exemplars/library.md`](exemplars/library.md); confirm
   submission, fee, and data policy (JPE Dataverse / JPE Data Editor) in
   [`official-source-map.md`](official-source-map.md).
