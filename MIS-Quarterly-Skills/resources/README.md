# MIS Quarterly — Resources

Capability layer for the **MIS Quarterly** skill pack. The runnable code is vendored for
self-containment; the cross-cutting method guidance lives once in the shared
empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Adapted from the verified Economic-Research-Journal-Skills library (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. Supporting infrastructure for the **economics-of-IS** tradition; behavioral / design-science / qualitative work uses SEM, artifact evaluation, or coded data structures instead. |
| [`worked-examples/`](worked-examples/) | Before→after rewrite of a (fictional) MISQ-style **introduction**, mapped to this pack's skills: front-load the IS phenomenon + IT artifact + contribution, problematize a named IS conversation, keep the artifact load-bearing, demote the estimator to evidentiary backbone. |
| [`exemplars/library.md`](exemplars/library.md) | **Verified** real MIS Quarterly papers by tradition × method × topic (behavioral / design science / economics of IS / organizational), web-checked against `misq.umn.edu` / `aisel.aisnet.org/misq`, with a sibling-confusion guard (not ISR / JMIS / JAIS / *Management Science*) and documented omissions. |
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
