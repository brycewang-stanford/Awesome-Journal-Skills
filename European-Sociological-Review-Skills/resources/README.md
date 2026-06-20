# European Sociological Review — Resources

Capability layer for the **European Sociological Review** skill pack. The runnable code is vendored for
self-containment; the cross-cutting method guidance lives once in the shared empirical-methods hub and
is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored from the verified shared empirical-methods library (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. Use it as the base for the ESR **replication package**. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a sociology paper introduction in ESR house style (question + mechanism + comparative leverage + a cross-level hypothesis stated before the tests). Illustrative fictional paper, derived from this pack's own skills. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified ESR papers** organized by method × topic — with a sibling-confusion guardrail (AJS / ASR / European Societies / European Journal of Sociology). Design positioning only — no fabricated numbers. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (caps, blinding, data/replication policy, house citation style) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | European data sources (ESS / EU-SILC / SOEP / EVS), harmonization schemes (ISCED/CASMIN, ISEI/EGP), and multilevel / SEM / panel software. |

## How to use

1. **Before drafting tables** — run the comparative/panel design against the reviewer-objection
   checklist; every objection you cannot answer in one paragraph + one exhibit is a hole. For ESR,
   add measurement equivalence and few-cluster inference to that stress test.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain
   (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD) and the master-script layout that
   becomes your replication package.
3. **Before submission** — walk the reporting-standards inference audit and this pack's
   `official-source-map.md` for venue limits, the Data Availability Statement, and the replication mandate.

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *this* journal specifically requires.
