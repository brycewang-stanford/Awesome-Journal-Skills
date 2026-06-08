# Journal of Accounting Research — Resources

Capability layer for the **Journal of Accounting Research** skill pack. The runnable code is vendored for
self-containment; the cross-cutting method guidance lives once in the shared
empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Adapted from the verified Economic-Research-Journal-Skills library (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. |
| [`worked-examples/`](worked-examples/) | Before->after rewrite of a JAR archival introduction in Journal of Accounting Research house style, derived from this pack's writing-style / contribution-framing / topic-selection / methods skills. Fictional illustrative paper; no invented journal policy. |
| [`exemplars/library.md`](exemplars/library.md) | Real, web-verified Journal of Accounting Research papers by method × topic (returns–earnings event study, disclosure quality, regime-change quasi-experiment, IFRS mandate, accruals measurement), each with a design self-check. Sibling-journal (TAR/JAE/CAR/RAST) misattributions are checked and omitted. Verified access date 2026-06-07. |
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
