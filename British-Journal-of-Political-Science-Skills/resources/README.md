# British Journal of Political Science — Resources

Capability layer for the **British Journal of Political Science (BJPS / BJPolS)** skill pack. The
runnable code is vendored for self-containment; the cross-cutting method guidance lives once in the
shared empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored 2026-06 for BJPS from the shared empirical-methods kit (Stata 18 MP); copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a political-science paper introduction in BJPS house style (question → wide/international significance → argument → finding, with the contribution stated early for a broad readership). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified BJPS papers** organized by subfield × method (experiment, observational/panel, replication/reappraisal, cross-national institutional, review/synthesis). Design positioning only — no fabricated findings; includes a sibling-journal do-not-misattribute list. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (formats, limits, blinding, DA-RT replication policy, house citation style) with sourcing discipline. |
| [`external_tools.md`](external_tools.md) | External tools / packages and cross-national data sources relevant to this venue. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection you cannot answer in one paragraph + one exhibit is a hole.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD).
3. **Before submission** — walk the reporting-standards inference audit and this pack's `official-source-map.md` for venue limits, then the `bjps-submission` checklist.

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *this* journal specifically requires.
