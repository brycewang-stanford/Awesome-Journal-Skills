# AEJ: Microeconomics — Resources

Capability layer for the **American Economic Journal: Microeconomics (AEJ: Micro)** skill pack.
AEJ: Micro is **theory-first**, so this layer is split deliberately: the proof-and-modeling craft
lives in the skills (above all [`aejmic-theory-model`](../skills/aejmic-theory-model/SKILL.md)),
while the runnable empirical code below is **relevant only to the journal's empirical / structural /
experimental subset**. For a **pure-theory** paper, do not reach for the code kit — go to
[`aejmic-theory-model`](../skills/aejmic-theory-model/SKILL.md) for model and proof architecture and
[`aejmic-replication-package`](../skills/aejmic-replication-package/SKILL.md) for proof-appendix craft
(and to deposit any numerical-example code).

## Contents

| Resource | What it gives an agent |
|---|---|
| [`code/`](code/) | Reproducible Stata + Python causal-inference / empirical skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). **For the structural / empirical-IO / experimental subset only** — pure-theory papers should skip it. Vendored 2026-06 from the shared empirical-methods hub (Stata 18 MP); copy-and-adapt, change no command blindly. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A before→after rewrite of a **theory-paper** introduction in AEJ: Micro house style (question/puzzle → model + equilibrium concept → main result as a proposition in words → which assumption is doing the work → contribution & scope). Illustrative fictional paper. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified AEJ: Micro papers** (confirmed `10.1257/mic…` DOI stem) organized by area: mechanism/market design, IO theory, game theory, contract/information, decision theory, applied/structural/experimental. Positioning only — no fabricated numbers; includes a sibling-confusion guard vs. JET / GEB / TE / Econometrica / AEJ: Applied. |
| [reviewer-objection-checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | (Applied subset) the objections referees actually raise, by identification strategy, each with its preemption. |
| [reporting-standards](../../shared-resources/empirical-methods/reporting-standards.md) | (Applied subset) modern inference + reporting table stakes: SE clustering, weak-IV diagnostics, multiple-testing, reproducibility. |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **Guidance → a fitted, audited result.** Maps each design family / reviewer objection to the concrete StatsPAI / Stata MCP tools in this environment, so this pack's identification / analysis skills *run* the modern DiD / weak-IV-robust CI / multiple-testing correction and report the number. |
| [`official-source-map.md`](official-source-map.md) | Venue-specific facts (fee, abstract limit, single-blind review, JEL, data/code policy, Data Editor) with sourcing discipline and 待核实 flags. |
| [`external_tools.md`](external_tools.md) | External tools / packages relevant to AEJ: Micro theory and its empirical/experimental applications. |

## How to use

1. **If the paper is pure theory** — ignore `code/`. Use [`aejmic-theory-model`](../skills/aejmic-theory-model/SKILL.md)
   for the model/proof, [`aejmic-identification`](../skills/aejmic-identification/SKILL.md) for what makes the
   result tight, and [`aejmic-replication-package`](../skills/aejmic-replication-package/SKILL.md) for the proof
   appendix (and to deposit numerical-example code).
2. **If the paper has structural / empirical / experimental content** — run the design against the
   reviewer-objection checklist, then adapt `code/` to your data, keeping the modern-estimator chain.
3. **Before submission** — walk the reporting-standards inference audit (applied subset) and this pack's
   [`official-source-map.md`](official-source-map.md) for venue requirements.

> Method guidance in the shared hub is venue-neutral; always defer to this pack's skills and
> `official-source-map.md` for what AEJ: Micro specifically requires.
