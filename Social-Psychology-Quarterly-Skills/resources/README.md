# Social Psychology Quarterly — Resources

Capability layer for the **Social Psychology Quarterly** skill pack. The runnable code is vendored for
self-containment; the cross-cutting method guidance lives once in the shared
empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper introduction in SPQ house style (the structure–individual link + named social-psychological mechanism + located tradition). Illustrative fictional sociological-social-psychology paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified SPQ papers** organized by tradition × method (identity / SSP / group processes / status / affect). Design positioning only — no fabricated numbers; sibling-journal confusion guard included. |
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Adapted from the verified Economic-Research-Journal-Skills library (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (fees, limits, blinding, data policy, house citation style) with sourcing discipline. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to this venue. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection you cannot answer in one paragraph + one exhibit is a hole.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD).
3. **Before submission** — walk the reporting-standards inference audit and this pack's `official-source-map.md` for venue limits.

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *this* journal specifically requires.
