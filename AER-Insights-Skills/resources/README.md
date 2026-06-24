# AER: Insights — Resources

Capability layer for the **American Economic Review: Insights** (AER: Insights) skill
pack. The runnable code is vendored for self-containment; the cross-cutting method
guidance lives once in the shared empirical-methods hub and is linked below. Everything
here serves the AER: Insights mandate: **one important idea, short, fast review**.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored 2026-06 for AER: Insights; venue-neutral, copy-and-adapt — change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before→after rewrite of a short-paper introduction in AER: Insights house style — lead immediately with the single clean result, name identification in one paragraph, push everything secondary to the appendix, and respect the length cap. Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AER: Insights papers** organized by method × topic. Design positioning only — no fabricated numbers; includes a sibling-confusion guard vs. *AER* / *AEJ* / *QJE*. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Critical here: AER: Insights has **no R&R**, so pre-empt before submitting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **Guidance → a fitted, audited result.** Maps each design family / reviewer objection to the concrete StatsPAI / Stata MCP tools in this environment, so this pack's identification / analysis skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (word/exhibit caps, fees, single-blind review, data policy, editor) with sourcing discipline. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to short empirical, structural, and methodological work. |

## How to use

1. **Before drafting** — confirm the single insight and run the design against the
   reviewer-objection checklist; with **no R&R**, an objection you cannot answer
   in-text or in the appendix is a likely reject.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator
   chain (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD).
3. **Before submission** — walk the reporting-standards inference audit and this pack's
   `official-source-map.md`, and reconcile the **word + exhibit caps** (auto-return gates).

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what AER: Insights specifically requires — above all the
> length cap and the single-insight discipline.
