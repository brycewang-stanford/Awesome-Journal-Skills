# Shared Empirical-Methods Kit

A **canonical, venue-neutral** capability layer for the empirical journal packs in
this repo. Instead of duplicating modern causal-inference rigor into every
quantitative pack (and risking drift), the cross-cutting method content lives here
once, and individual packs reference it or vendor it with a thin venue-specific
layer (exemplars + word limits + house style from their own
`official-source-map.md`).

## Contents

| File | What it gives an agent |
|---|---|
| [`reviewer-objection-checklist.md`](reviewer-objection-checklist.md) | The objections referees actually raise at top empirical journals, by identification strategy (DiD / IV / RDD / DML / matching / mechanism), each with the preemption that defuses it. Stress-test a design *before* drafting. |
| [`reporting-standards.md`](reporting-standards.md) | The inference + reporting choices now treated as table stakes: SE clustering, weak-IV diagnostics, multiple-testing corrections, DiD/RDD reporting, reproducibility. Stata-first with R/Python equivalents. |
| [`execution-with-mcp.md`](execution-with-mcp.md) | **The last mile: guidance → a fitted, audited result.** Maps each design family and each reviewer objection to the concrete StatsPAI / Stata MCP tools available in this environment, so a skill *runs* the Callaway–Sant'Anna estimate / weak-IV-robust CI / multiple-testing correction instead of only recommending it. Includes validated worked-examples for DiD / IV / RDD / synthetic-control / DML. Venue-neutral; defers placement & house style to each pack. |
| [`replication-package.md`](replication-package.md) | **Assemble + validate the Data-Editor package** against the target venue's data-and-code policy (read live from its source-map): master script, pinned environment, README/roadmap, restricted-data plan, and a script→exhibit output map; a pre-submit checklist that catches the numbers a Data Editor would fail to reproduce. |
| [`code/`](code/) | A reproducible Stata + Python skeleton (clean → descriptive → DiD/IV/RDD/DML → mechanism → robustness → tables). Adapted from the **verified** ERJ library (run on Stata 18 MP, 2026-06). |

## Who should use this

Any pack whose research is **empirical / quantitative** — economics, finance,
accounting, management (empirical lane), marketing, political science, sociology,
education, demography, criminology, and the empirical natural/agricultural-science
packs. Theory-only and humanities packs (e.g. AMR, Econometric Theory, AHR, PMLA,
Mind) do **not** use the code kit, though the "so what" and inference sections of
the checklist still translate.

## How packs reference it

1. **Lightweight reference** — a skill body links to the relevant section, e.g.
   "For weak-IV reporting see `shared-resources/empirical-methods/reporting-standards.md §2`."
2. **Vendored copy** (for self-contained installable plugins) — copy `code/` into
   the pack's `resources/code/` and add a one-line provenance header. Shared *code*
   is legitimately templated infrastructure and is not flagged by the prose
   clone-audit (which scans only `SKILL.md`). The pack then adds its own
   `resources/exemplars/` (real papers from *that* venue) and at least one
   venue-specific worked example.

## What is verified vs heuristic

- The Stata command chains in `code/` were **run on synthetic data on Stata 18 MP
  (2026-06)** per the source library; see `code/README.md` for the exact list.
- The checklist and reporting standards are distilled from the published
  applied-methods literature (citations inline). They are method guidance, not
  venue policy — always cross-check venue-specific limits against each pack's
  `official-source-map.md`.
