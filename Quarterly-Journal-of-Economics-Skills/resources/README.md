# QJE Resources

Action-oriented resources for the Quarterly Journal of Economics (QJE) skill pack. The `skills/` give
advice; this directory lets an agent **act** — run the empirical pipeline, model a QJE-style section, and
benchmark against verified exemplars. Pair these with the relevant `skills/qje-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`code/`](code/) | Run a reproducible Stata + Python causal-inference pipeline (TWFE → heterogeneity-robust DID, IV with effective-F, RDD, DML, mechanism, robustness, three-line tables). Vendored, command-verified on Stata 18 MP. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper introduction in QJE house style (the question + answer + why-it-matters funnel). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified QJE papers** organized by method × topic. Design positioning only — no fabricated numbers. |
| [`official-source-map.md`](official-source-map.md) | **QJE-specific policy & facts:** Editorial Express submission, PDF-only, QJE Dataverse data policy, editors/history/scope, and a do-not-misattribute list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools and services referenced by the pack. |

## Shared empirical-methods kit (venue-neutral, cross-pack)

QJE-specific policy lives in [`official-source-map.md`](official-source-map.md). The general
empirical-craft prose is shared across journal packs and lives in the repo's shared kit:

- [`../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
  — the standard referee objections (identification, inference, robustness, mechanism) and how to
  pre-empt them.
- [`../../shared-resources/empirical-methods/reporting-standards.md`](../../shared-resources/empirical-methods/reporting-standards.md)
  — what every empirical result must report (estimator, SE/clustering, sample, diagnostics) to clear a
  top-5 reviewer.
- [`../../shared-resources/empirical-methods/execution-with-mcp.md`](../../shared-resources/empirical-methods/execution-with-mcp.md)
  — **the last mile: guidance → a fitted, audited result.** Maps each design family / reviewer objection to
  the concrete StatsPAI / Stata MCP tools in this environment, so `qje-identification` and `qje-robustness`
  *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number.

The [`code/`](code/) directory is **vendored** from
[`../../shared-resources/empirical-methods/code`](../../shared-resources/empirical-methods/code) so this
plugin is self-contained; its commands are verified on Stata 18 MP (2026-06). Fix issues upstream and
re-vendor rather than editing the copy here.

## Suggested workflow

1. Scope and frame with [`../skills/qje-topic-selection`](../skills/qje-topic-selection/SKILL.md) and
   [`../skills/qje-writing-style`](../skills/qje-writing-style/SKILL.md); model the intro on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Identify and estimate with [`code/`](code/), guided by
   [`../skills/qje-identification`](../skills/qje-identification/SKILL.md) and
   [`../skills/qje-robustness`](../skills/qje-robustness/SKILL.md).
3. Pre-empt referees with the shared
   [`reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
   and report to the shared
   [`reporting-standards.md`](../../shared-resources/empirical-methods/reporting-standards.md).
4. Benchmark against verified QJE papers in [`exemplars/library.md`](exemplars/library.md); confirm
   submission/data policy in [`official-source-map.md`](official-source-map.md).
