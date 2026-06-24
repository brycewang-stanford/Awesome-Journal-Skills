# JFE Resources

Action-oriented resources for the Journal of Financial Economics (JFE) skill pack. The `skills/` give
advice; this directory lets an agent **act** — run the empirical pipeline, model a JFE-style section, and
benchmark against verified exemplars. Pair these with the relevant `skills/jfe-*/SKILL.md`.

JFE is **empirical finance** (Elsevier / North-Holland; ISSN 0304-405X): rigorous, methodologically
demanding asset pricing and corporate finance, plus the financial-economics theory that supports them.
The shared causal-inference code kit (DiD / IV / RDD / DML) applies directly to empirical asset-pricing
and corporate-finance designs.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`code/`](code/) | Run a reproducible Stata + Python causal-inference pipeline (TWFE → heterogeneity-robust DID, IV with effective-F, RDD, DML, mechanism, robustness, three-line tables) — for natural-experiment and quasi-experimental designs in corporate finance and asset pricing. Vendored, command-verified on Stata 18 MP. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of an empirical-finance paper introduction in JFE house style (question → what → finding → credibility → contribution, on page one). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified JFE papers** organized by method × topic — and avoid the JF/RFS misattribution traps. Design positioning only; no fabricated numbers. |
| [`official-source-map.md`](official-source-map.md) | **JFE-specific policy & facts:** Editorial Manager submission, US$850 fee, abstract ≤100 words, Mendeley Data code/data policy, the Whited-era masthead, prizes (Jensen / Fama-DFA), and a do-not-misattribute list. The authoritative pack source. |
| [`external_tools.md`](external_tools.md) | External tools and services referenced by the pack. |

## Shared empirical-methods kit (venue-neutral, cross-pack)

JFE-specific policy lives in [`official-source-map.md`](official-source-map.md). The general
empirical-craft prose is shared across journal packs and lives in the repo's shared kit:

- [`../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
  — the standard referee objections (identification, inference, robustness, mechanism) and how to
  pre-empt them. Pairs with [`../skills/jfe-identification`](../skills/jfe-identification/SKILL.md) and
  [`../skills/jfe-referee-strategy`](../skills/jfe-referee-strategy/SKILL.md).
- [`../../shared-resources/empirical-methods/reporting-standards.md`](../../shared-resources/empirical-methods/reporting-standards.md)
  — what every empirical result must report (estimator, SE/clustering, sample, diagnostics) to clear a
  top-3 finance reviewer. Pairs with [`../skills/jfe-empirical-design`](../skills/jfe-empirical-design/SKILL.md).
- [`execution-with-mcp`](../../shared-resources/empirical-methods/execution-with-mcp.md)
  — **the last mile: guidance → a fitted, audited result.** Maps each design family to the concrete StatsPAI / Stata MCP tools, so this pack's empirical skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number.

The [`code/`](code/) directory is **vendored** from
[`../../shared-resources/empirical-methods/code`](../../shared-resources/empirical-methods/code) so this
plugin is self-contained; its commands are verified on Stata 18 MP (2026-06). Fix issues upstream and
re-vendor rather than editing the copy here.

## Suggested workflow

1. Scope and frame with [`../skills/jfe-topic-selection`](../skills/jfe-topic-selection/SKILL.md) and
   [`../skills/jfe-writing-style`](../skills/jfe-writing-style/SKILL.md); model the intro on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
2. Position against the frontier with
   [`../skills/jfe-literature-positioning`](../skills/jfe-literature-positioning/SKILL.md), benchmarking
   design against verified JFE papers in [`exemplars/library.md`](exemplars/library.md).
3. Identify and estimate with [`code/`](code/), guided by
   [`../skills/jfe-identification`](../skills/jfe-identification/SKILL.md) (causal designs) and
   [`../skills/jfe-empirical-design`](../skills/jfe-empirical-design/SKILL.md) (factor construction,
   clustering, multiple-testing) and [`../skills/jfe-robustness`](../skills/jfe-robustness/SKILL.md).
4. Pre-empt referees with the shared
   [`reviewer-objection-checklist.md`](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
   and report to the shared
   [`reporting-standards.md`](../../shared-resources/empirical-methods/reporting-standards.md).
5. Confirm submission, fee, and data/code policy in [`official-source-map.md`](official-source-map.md)
   before submitting via [`../skills/jfe-submission`](../skills/jfe-submission/SKILL.md).
