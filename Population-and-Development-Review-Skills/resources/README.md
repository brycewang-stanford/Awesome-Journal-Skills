# Population and Development Review — Resources

Capability layer for the **PDR** skill pack. The runnable code is vendored for self-containment; the
cross-cutting method guidance lives once in the shared empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored from the shared empirical-methods hub (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Before→after rewrite of a *PDR* introduction in the population-question → quantity-first → development-meaning style PDR rewards. Fictional teaching paper. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (editors, length norms, blinding, Free Format, fees, data policy, house style) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | Population + development data sources and software/packages relevant to this venue. |
| [`exemplars/library.md`](exemplars/library.md) | Real, web-verified *PDR* (Population Council / Wiley) papers by topic × contribution, with a sibling-journal omission guard. Design positioning only — read the originals before citing numbers. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection
   you cannot answer in one paragraph + one exhibit is a hole.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain
   (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD) where the question is causal.
3. **Before submission** — walk the reporting-standards inference audit and this pack's
   `official-source-map.md` for venue norms (length, Free Format, double-anonymized, fees).

> Method guidance here is venue-neutral; always defer to this pack's skills and `official-source-map.md`
> for what *PDR* specifically requires — above all, the **population-and-development** connection and the
> broad-interest argument that a clean estimate alone will not satisfy.
