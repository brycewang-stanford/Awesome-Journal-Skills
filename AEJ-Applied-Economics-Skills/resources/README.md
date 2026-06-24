# AEJ: Applied — Resources

Capability layer for the **American Economic Journal: Applied Economics** skill
pack. The runnable code is vendored for self-containment; the cross-cutting method
guidance lives once in the shared empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored from `shared-resources/empirical-methods/code` (Stata 18 MP, 2026-06); copy-and-adapt as the backbone of your openICPSR replication package — change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a paper introduction in AEJ: Applied house style (question → credible identification → headline causal estimate with SE → mechanism → policy/economic lesson). Illustrative fictional applied-micro paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AEJ: Applied papers** (confirmed `10.1257/app.` DOI stem) organized by method × topic. Design positioning only — no fabricated numbers; includes a sibling-confusion guard vs. *AER* / *AEJ: Economic Policy* / field journals. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **Guidance → a fitted, audited result.** Maps each design family / reviewer objection to the concrete StatsPAI / Stata MCP tools in this environment, so this pack's identification / analysis skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (scope, editors, fee, single-blind review, data policy, house citation style) with sourcing discipline. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to this venue. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection
   checklist; every objection you cannot answer in one paragraph + one exhibit is a
   hole (see [`../skills/aeja-referee-strategy/SKILL.md`](../skills/aeja-referee-strategy/SKILL.md)).
2. **When building results** — adapt `code/` to your data; keep the modern-estimator
   chain (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD), and grow
   it into the openICPSR package the AEA Data Editor will check
   ([`../skills/aeja-replication-package/SKILL.md`](../skills/aeja-replication-package/SKILL.md)).
3. **Before submission** — walk the reporting-standards inference audit and this
   pack's `official-source-map.md` for venue rules
   ([`../skills/aeja-submission/SKILL.md`](../skills/aeja-submission/SKILL.md)).

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *this* journal specifically requires.
