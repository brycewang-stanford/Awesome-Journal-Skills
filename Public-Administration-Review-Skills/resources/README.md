# Public Administration Review — Resources

Capability layer for the **Public Administration Review (PAR)** skill pack. The runnable code is
vendored for self-containment; the cross-cutting method guidance lives once in the shared
empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored 2026-06 from the shared empirical-methods library (Stata 18 MP); copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a public-administration paper introduction in PAR house style (question → field-wide significance → why hard to identify → design → finding → contribution → **Evidence for Practice**). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified PAR papers** organized by subfield × method. Design positioning only — no fabricated findings; includes a sibling-journal do-not-misattribute list (JPART / JPAM / Governance / ARPA). |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **Guidance → a fitted, audited result.** Maps each design family / reviewer objection to the concrete StatsPAI / Stata MCP tools in this environment, so this pack's empirical skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (word/abstract caps, double-blind, Evidence for Practice, TOP transparency, portal, editors) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | PA data sources (FedScope / FEVS / Census of Governments / WGI / QoG) and R / Stata / Python + qualitative/CAQDAS tooling. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection
   you cannot answer in one paragraph + one exhibit is a hole that also threatens your Evidence for Practice.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain
   (heterogeneity-robust DiD around reforms, weak-IV-robust IV, bias-corrected RDD).
3. **Before submission** — walk the reporting-standards inference audit and this pack's
   `official-source-map.md` for venue limits, then the
   [`../skills/pubar-submission/templates/checklist.md`](../skills/pubar-submission/templates/checklist.md).

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *PAR* specifically requires.
