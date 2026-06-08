# Organization Science — Resources

Capability layer for the **Organization Science** skill pack. The runnable code is vendored for
self-containment; the cross-cutting method guidance lives once in the shared
empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Adapted from the verified Economic-Research-Journal-Skills library (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper introduction in Organization Science house style (theoretical tension first, named organizational mechanism, explicit micro-to-macro level, contribution over novelty). Illustrative fictional paper. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (fees, limits, blinding, data policy, house citation style) with sourcing discipline. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to this venue. |
| [`exemplars/library.md`](exemplars/library.md) | Real, web-verified Organization Science papers by topic × method, with a sibling-journal omission guard. Design positioning only — read the originals before citing numbers. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection you cannot answer in one paragraph + one exhibit is a hole.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD).
3. **Before submission** — walk the reporting-standards inference audit and this pack's `official-source-map.md` for venue limits.

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *this* journal specifically requires.
