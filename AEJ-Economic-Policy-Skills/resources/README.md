# AEJ: Economic Policy — Resources

Capability layer for the **AEJ: Economic Policy** skill pack. The runnable code is vendored for
self-containment; the cross-cutting method guidance lives once in the shared empirical-methods hub and is
linked below. The through-line of every resource is the AEJ: Policy bar: a **broad-interest policy
question**, a **credible quasi-experimental / RCT evaluation**, and a **welfare / cost-benefit /
distributional reading**.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored 2026-06 from the shared empirical-methods hub (Stata 18 MP); copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before→after rewrite of a paper introduction in AEJ: Policy house style (policy question → credible identification → headline causal estimate with SE → cost-benefit / welfare / distributional implication → calibrated policy lesson; no significance asterisks). Illustrative fictional policy-evaluation paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AEJ: Policy papers** (confirmed `10.1257/pol…` DOI stem) organized by policy area (tax/public finance, environment/energy, health, education, labor/transfer, regulation). Design positioning only — no fabricated numbers; includes a sibling-confusion guard vs. *AER* / *AEJ: Applied* / *JPubE* / *J. Health Econ*. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **Guidance → a fitted, audited result.** Maps each design family / reviewer objection to the concrete StatsPAI / Stata MCP tools in this environment, so this pack's identification / analysis skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (AEA process, single-blind, JEL, Data Editor / openICPSR, disclosure) with sourcing discipline and honest 待核实 marks. |
| [`external_tools.md`](external_tools.md) | Data sources, software, welfare/cost-benefit tooling, and process notes for this venue. |

## How to use

1. **Before drafting tables** — run the design against the
   [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md);
   every objection you cannot answer in one paragraph + one exhibit is a hole.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain
   (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD), and add the **welfare/cost-benefit
   ledger** the policy reading needs (see [`../skills/aejpol-theory-model/SKILL.md`](../skills/aejpol-theory-model/SKILL.md)).
3. **Before submission** — walk the
   [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) inference audit
   and this pack's [`official-source-map.md`](official-source-map.md) for venue requirements (single-blind
   front matter, JEL codes, the AEA Data Editor deposit).

> Method guidance in the shared hub is venue-neutral; always defer to this pack's skills and
> [`official-source-map.md`](official-source-map.md) for what AEJ: Policy specifically requires — above
> all, the policy-question-and-welfare framing that distinguishes it from J. Public Economics and
> AEJ: Applied.
