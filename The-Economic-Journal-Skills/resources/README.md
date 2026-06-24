# The Economic Journal — Resources

Capability layer for the **The Economic Journal (EJ)** skill pack. The runnable code is vendored for
self-containment; the cross-cutting method guidance lives once in the shared empirical-methods hub
and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored from `shared-resources/empirical-methods/code` (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. Build it to pass the EJ Data Editor's pre-acceptance reproducibility check. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper introduction in EJ house style (broad-interest question → mechanism → identification → headline magnitude with a standard error → portable lesson; legible to a generalist). Illustrative fictional applied paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified EJ papers** organized by method × topic. Design positioning only — no fabricated numbers; includes a sibling-confusion guard vs. JEEA / EER / The Econometrics Journal. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **Guidance → a fitted, audited result.** Maps each design family / reviewer objection to the concrete StatsPAI / Stata MCP tools in this environment, so this pack's empirical skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (review model, data policy, portal, short-paper option, reference style) with sourcing discipline. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to this venue. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection you cannot answer in one paragraph + one exhibit is a hole.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD), and write it so the EJ Data Editor can rerun it.
3. **Before submission** — walk the reporting-standards inference audit and this pack's `official-source-map.md` for EJ's review model, data policy, and the full-length vs. short-paper choice.

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *The Economic Journal* specifically requires.
