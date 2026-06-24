# Journal of Policy Analysis and Management — Resources

Capability layer for the **Journal of Policy Analysis and Management (JPAM)** skill pack. The runnable
code is vendored for self-containment; the cross-cutting method guidance lives once in the shared
empirical-methods hub and is linked below.

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Vendored from the verified shared empirical-methods library (Stata 18 MP, 2026-06); copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a policy-evaluation introduction in JPAM house style (policy problem → credible design → effect in policy units → calibrated implication, without overclaiming). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified JPAM papers** organized by policy field × method (RD, DiD, RKD, within-study comparison). Design positioning only — no fabricated findings; includes a sibling-journal do-not-misattribute list. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | The objections referees actually raise, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with its preemption. Stress-test the design before drafting. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | Modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, DiD/RDD reporting, reproducibility. |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **Guidance → a fitted, audited result.** Maps each design family / reviewer objection to the concrete StatsPAI / Stata MCP tools in this environment, so this pack's empirical skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (fee/membership, article types, blinding, data policy, portal) with source-backed guardrails. |
| [`external_tools.md`](external_tools.md) | Policy-evaluation data sources, software, and cost-benefit / MVPF tooling relevant to JPAM. |

## How to use

1. **Before drafting tables** — run the design against the reviewer-objection checklist; every objection
   you cannot answer in one paragraph + one exhibit is a hole.
2. **When building results** — adapt `code/` to your data; keep the modern-estimator chain
   (heterogeneity-robust DiD, weak-IV-robust IV, bias-corrected RDD), then add the JPAM-specific
   cost-benefit and distributional layer (see [`../skills/jpam-data-analysis/SKILL.md`](../skills/jpam-data-analysis/SKILL.md)).
3. **Before submission** — walk the reporting-standards inference audit and this pack's
   `official-source-map.md` for venue limits, fee/membership, and the data-availability requirement.

> Method guidance here is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what *this* journal specifically requires.
