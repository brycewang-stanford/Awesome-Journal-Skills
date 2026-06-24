---
name: rt-execution-bridge
description: Use when an empirical analysis should be RUN and audited, not just advised — DiD, IV, RDD, synthetic control, DML, multiple-testing, sensitivity. Maps the design to the concrete StatsPAI / Stata MCP tools in this environment and reports the fitted, audited number. Defers result placement and house style to the target journal's pack.
---

# Execution Bridge (rt-execution-bridge)

Close the last mile: turn "you should use a heterogeneity-robust DiD / weak-IV-robust CI /
multiple-testing correction" into an actual fitted, audited estimate. Full map +
orchestration spine + validated worked-examples (DiD / IV / RDD / synthetic-control / DML):
[`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

## When to trigger

- You have data and a design and need the actual estimate + its diagnostics.
- A reviewer objection (real or simulated) needs an executed answer (e.g. "TWFE is biased
  under staggered adoption" → run Callaway–Sant'Anna + Goodman-Bacon).

## The spine (always)

1. `detect_design` → `preflight` / `recommend` → fit with `as_handle=true`.
2. `audit_result(result_id)` — enumerate the checks the design still owes; run each
   `suggest_function` it names.
3. Design-specific sensitivity from the handle (`honest_did_from_result`,
   `sensitivity_from_result`, `evalue_from_result`).
4. `bibtex(keys=[…])` for citations — never invent references.

## Design → tools (summary; full table in the canonical doc)

- **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` + `honest_did_from_result`.
- **IV:** `iv` + `effective_f_test` + `anderson_rubin_ci` (weak-IV-robust).
- **RDD:** `rdrobust` + `rddensity` / `mccrary_test`.
- **Synthetic control:** `synth` / `sdid` + placebo inference.
- **DML / high-dim:** `dml` + `dml_diagnostics` (overlap) + `oster` / `sensemakr`.
- **Multiple testing / inference:** `romano_wolf`, `wild_cluster_bootstrap`, `twoway_cluster`.
- **Exhibits:** `etable` / `did_summary_to_latex` straight from the handle.

## Hard rules

1. **Run, don't claim** — every reported estimate/CI/F/bound traces to a tool call.
2. **`bibtex` is the only citation source.**
3. **Method here, placement there** — where the result goes (body vs. appendix, page limit,
   house table style) is the target pack's skills + `official-source-map.md`.
4. **Degrade honestly** — if StatsPAI/Stata are not connected, adapt the `code/` skeleton
   and flag any unverified number.

## Output format

```
【Design】DiD / IV / RDD / SCM / DML / …
【Estimate】point [CI] (estimator)
【Key diagnostic】(first-stage/effective F, pre-trends p, overlap, placebo p, …)
【Audit gaps run】…
【Magnitude】interpretable units
【Next】rt-submission-readiness / the pack's tables-figures skill
```
