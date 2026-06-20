# Comparative Political Studies — Resources

Capability layer for the **Comparative Political Studies (CPS)** skill pack. The runnable code is
vendored for self-containment; the cross-cutting method guidance lives once in the shared
empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored from the verified shared empirical-methods library (Stata 18 MP, 2026-06) for CPS self-containment; copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a comparative-politics introduction in CPS house style (comparative puzzle → stake → identification problem → design → finding+mechanism → portable contribution). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified CPS papers** organized by subfield × method (cross-national panel, natural experiment, survey experiment, comparative-historical, formal-empirical). Design positioning only — no fabricated findings; includes a sibling-journal do-not-misattribute list. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, few-cluster corrections, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (length, abstract, anonymity, data policy, APA house style, CPS Dataverse) with sourcing discipline and 待核实 markers. |
| [`external_tools.md`](external_tools.md) | Comparative-politics data sources, software, and packages relevant to this venue. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection
   you cannot answer in one paragraph + one exhibit is a hole (especially the few-clusters / cross-national
   measurement objections that CPS reviewers raise).
2. **When building results** — adapt `code/` to your comparative data; keep the modern-estimator chain
   (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD) and add few-cluster corrections.
3. **Before submission** — walk the reporting-standards inference audit and this pack's
   `official-source-map.md` for venue limits (11,000 words, ~150-word abstract, APA references, CPS
   Dataverse deposit).

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *CPS* specifically requires.
