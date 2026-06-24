# AEJ: Macroeconomics — Resources

Capability layer for the **AEJ: Macroeconomics** skill pack. The runnable code is
vendored for self-containment; the cross-cutting method guidance lives once in the
shared empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored from `shared-resources/empirical-methods/code` (2026-06); copy-and-adapt, change no command blindly. **For macro this is a starting point** — it covers the cross-sectional/panel empirical chain but not time-series macro. Add **SVAR / proxy-VAR**, **local-projection IRF**, and **DSGE/HANK-calibration & simulation** code as your paper requires (see `external_tools.md` §2 for the relevant Stata/R/Julia/Dynare packages). |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before→after rewrite of a paper introduction in AEJ: Macro house style (macro question → identified design or quantitative model → headline quantity with uncertainty → mechanism → lesson; ≤100-word-abstract discipline). Illustrative fictional empirical-macro paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AEJ: Macro papers** organized by method × topic. Design positioning only — no fabricated numbers; includes a sibling-confusion guard vs. *AER* / *J. Monetary Economics* / *RED* / *AEJ: Applied*. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the empirical design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, reproducibility. |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **Guidance → a fitted, audited result.** Maps each design family / reviewer objection to the concrete StatsPAI / Stata MCP tools in this environment, so this pack's identification / analysis skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (fees, length, blinding, data policy, editors) with sourcing discipline. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to this venue, including macro time-series and DSGE/HANK toolchains. |

## How to use

1. **Before drafting tables** — run the empirical design against the reviewer-objection checklist; every objection you cannot answer in one paragraph + one exhibit is a hole. For time-series identification, pair it with this pack's `aejmac-identification`.
2. **When building results** — adapt `code/` for the cross-sectional/panel parts; for the macro core, add SVAR/LP/DSGE code per `external_tools.md` and keep the AEA-compliant chain (heterogeneity-robust estimators, weak-IV-robust bands, documented solver/seeds).
3. **Before submission** — walk the reporting-standards inference audit and this pack's `official-source-map.md` for venue limits (≤100-word abstract, ~40-page length, single-blind, per-coauthor disclosure).

> Method guidance in the shared hub is venue-neutral; always defer to this pack's
> skills and `official-source-map.md` for what *AEJ: Macro* specifically requires.
> The vendored `code/` kit is cross-sectional/panel-oriented; macro papers must
> add their own time-series and quantitative-model code.
