# Execution Bridge — from guidance to a fitted, audited result (StatsPAI / Stata MCP)

> **What this file is.** The other shared docs say *what good looks like*
> ([`reviewer-objection-checklist.md`](reviewer-objection-checklist.md)) and *what to
> report* ([`reporting-standards.md`](reporting-standards.md)). This file closes the
> last mile: it maps each design family and each reviewer objection to the **concrete,
> callable MCP tools** an agent has in this environment, so the skill does not just
> *advise* a Callaway–Sant'Anna estimate or a weak-IV-robust CI — it **runs one and
> reports the number**.
>
> **Venue-neutral.** Tool *choice* is method, not policy. Where the result *goes*
> (body vs. appendix, page limits, table house style, data-sharing/replication policy)
> is venue-specific — always defer to the pack's own skills and
> `resources/official-source-map.md`.

These tools are available in this environment as MCP servers:

- **StatsPAI** (`mcp__statspai__*`) — agent-native causal inference & econometrics
  (~600 functions: DiD, IV, RDD, DML, synthetic control, sensitivity, multiple
  testing, decompositions, plus verified-citation `bibtex`).
- **Stata MCP** (`mcp__stata-mcp__stata_do`, `mcp__stata-code__stata_run`) — run real
  `.do` code against the user's data when a result must match a Stata-first house style
  or a package that only exists in Stata.

If a server is **not** connected in the current session, fall back to the vendored
`code/` skeleton (copy-and-adapt) and say so explicitly — never report a number you
did not actually compute.

---

## 0. The orchestration spine (always start here)

StatsPAI is designed to be driven in this order. Follow it rather than jumping
straight to a single estimator:

1. **`detect_design`** — let the data declare its shape (DiD / IV / RDD / panel / …),
   or pass `design=` if you already know it.
2. **`preflight`** + **`recommend`** — surface design problems (no clean control
   group, weak first stage, manipulation at the cutoff) and let it pick an estimator
   *before* you commit.
3. **Fit with `as_handle=true`** so you get a `result_id` you can chain. Pass
   `detail='minimal'` on cheap sub-steps; default `'agent'` carries violations +
   next-steps.
4. **`audit_result(result_id=…)`** — enumerate the robustness checks the design still
   owes; for each gap it emits the exact `suggest_function` to call next.
5. **Design-specific sensitivity from the handle** —
   `honest_did_from_result`, `sensitivity_from_result`, `evalue_from_result` — no need
   to re-ferry betas/sigma.
6. **`bibtex(keys=[…])`** for every method citation. **`paper.bib` / the StatsPAI
   citation store is the single source of truth — never invent a reference.**

> Hard rule for "publish faster": the value here is *fewer rejection cycles*, which
> means **run → audit → report**, not "looks reasonable." If you assert a coefficient,
> a CI, an F-stat, or a sensitivity bound, it must come from an actual tool call in the
> transcript.

---

## 1. Design family → estimator tool chain

| Design | Run (fit with `as_handle=true`) | Then audit / sensitivity |
|---|---|---|
| **Staggered DiD** | `callaway_santanna`, `sun_abraham`, `did_imputation` / `borusyak_jaravel_spiess`, `gardner_did`, `etwfe` | `bacon_decomposition` (+`bacon_plot`) to expose bad-comparison weight; `event_study` / `parallel_trends_plot` for pre-trends; `honest_did_from_result` (Rambachan–Roth) for what a pre-trend violation would do to the estimate |
| **2×2 / simple DiD** | `did`, `did_2x2`, `drdid` | `pretrends_test`, `pretrends_power` |
| **IV / 2SLS** | `iv`, `ivreg`, `liml`, `jive` | `effective_f_test` (Montiel-Olea–Pflueger), `anderson_rubin_ci` / `anderson_rubin_test` & `weakrobust` (weak-IV-robust inference), `tF_adjustment`, `iv_diag` |
| **RDD (sharp/fuzzy)** | `rdrobust` (bias-corrected, robust CI), `rdplot` | `rddensity` / `mccrary_test` (manipulation), `rdbwselect` (bandwidth), `rdpower`, `rd_honest` |
| **DML / high-dim controls** | `dml` | `dml_diagnostics`, `dml_sensitivity` |
| **Synthetic control** | `synth`, `scest`/`scpi`, `sdid` (synthetic DiD) | `synth_placebo`/`synth_time_placebo`, `synth_sensitivity` |
| **Selection on observables** | `psm`, `ipw`, `aipw`, `tmle`, `cbps`, `ebalance` | `love_plot`/`balance_diagnostics`, `oster_bounds`/`oster_delta`, `sensemakr`, `evalue` |
| **Mechanism / mediation** | `gelbach` (decomposition, not naive controlling-away), `mediate` | report share explained; avoid the "add a control, watch it shrink" anti-pattern |

For end-to-end convenience StatsPAI also exposes `pipeline_did`, `pipeline_iv`,
`pipeline_rd` — useful once the design is settled, but still run `audit_result` after.

### Worked examples — the chain run end to end (synthetic data, real tool returns)

Each shows the bias the naive approach hides, the corrected estimate, and the diagnostic
that licenses it — every number an actual MCP return, nothing hand-typed:

- **Staggered DiD** — [`Journal-of-Finance-Skills/.../02-execution-walkthrough.md`](../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)
  (TWFE −0.0227 vs clean Callaway–Sant'Anna −0.0272; pre-trends p = 0.155; honest-DiD breakdown).
- **IV / 2SLS** — [`worked-examples/iv-walkthrough.md`](worked-examples/iv-walkthrough.md)
  (OLS 0.196 → 2SLS 0.0997; Olea–Pflueger effective F = 272; Hausman p < 0.001).
- **Sharp RDD** — [`worked-examples/rdd-walkthrough.md`](worked-examples/rdd-walkthrough.md)
  (naive mean-diff 1.39 → rdrobust ~0.57–0.61 for a true 0.6; McCrary p = 0.965).
- **Synthetic control** — [`worked-examples/synthetic-control-walkthrough.md`](worked-examples/synthetic-control-walkthrough.md)
  (ATT 6.59 for a true +6; placebo p = 0.048; pre-RMSE 0.44; transparent donor weights).
- **Double ML** — [`worked-examples/dml-walkthrough.md`](worked-examples/dml-walkthrough.md)
  (the bias ladder: naive 3.57 → rich linear controls 2.89 → DML 2.07 for a true 2.0; audit flags overlap + OVB).

---

## 2. Reviewer objection → the tool that answers it

Pairs with [`reviewer-objection-checklist.md`](reviewer-objection-checklist.md): each
attack there now has an executable reply.

| Objection (from the checklist) | Execute |
|---|---|
| "Your TWFE DiD is contaminated by negative weights." | `bacon_decomposition` + re-estimate with `callaway_santanna` / `sun_abraham`; show both |
| "Parallel trends fails / pre-trends look off." | `pretrends_test` + `pretrends_power`; then `honest_did_from_result` to bound the sensitivity |
| "Your instrument is weak." | `effective_f_test`; report `anderson_rubin_ci` (valid under weak IV) instead of leaning on the 2SLS t-stat |
| "The exclusion restriction is violated." | `iv_diag` / plausibly-exogenous bounds; falsify the alternative channel |
| "Manipulation at the RD cutoff." | `rddensity` / `mccrary_test`; `rdplot` of the density |
| "Bandwidth-driven RD result." | `rdbwselect` + `rdrobust` across bandwidths (robustness table) |
| "Omitted-variable bias could overturn it." | `oster_delta`/`oster_bounds`, `sensemakr`, or `evalue` — quantify how strong a confounder would need to be |
| "You mined many specifications." | §3 multiple-testing tools — report an adjusted threshold |
| "Standard errors ignore the real dependence." | `cluster_robust_se`, `twoway_cluster`, `wild_cluster_bootstrap` (few clusters), `conley` (spatial) |

---

## 3. Reporting standards → tool

Pairs with [`reporting-standards.md`](reporting-standards.md):

- **Multiple testing:** `romano_wolf` (step-down, accounts for correlation across
  tests), `holm`, `benjamini_hochberg`, `bonferroni`, or `adjust_pvalues`.
- **Few-cluster inference:** `wild_cluster_bootstrap` / `wild_cluster_boot`,
  `cr2_se`, `subcluster_wild_bootstrap`.
- **Publication-ready exhibits:** `etable`, `event_study_table`,
  `did_summary_to_latex` / `did_summary_to_markdown`, `plot_from_result`,
  `enhanced_event_study_plot` — emit the table/figure in the format the pack's
  `tables-figures` skill specifies.
- **Verified citations:** `bibtex(keys=[…])` — the only sanctioned way to add a method
  reference.

---

## 4. When to drop to the Stata MCP

Use `mcp__stata-mcp__stata_do` / `mcp__stata-code__stata_run` (with the vendored
`code/*.do` skeleton) when:

- the venue/field is **Stata-first** and reviewers expect the canonical package
  (`reghdfe`, `csdid`, `did_multiplegt`, `ivreghdfe`/`weakivtest`, `rdrobust`,
  `boottest`, `eventstudyinteract`);
- the user's data and workflow already live in Stata and a parallel Python estimate
  would just add a reconciliation burden;
- you need a number to match an existing `.do` exactly for the replication package.

Inspect first with `get_data_info`, run the relevant numbered step, read back with
`read_log`. Keep the master `00_master.do` ordering (clean → descriptive →
DiD/IV/RDD/DML → mechanism → robustness → tables) so the output doubles as the
replication package.

---

## 5. Hard rules (the credibility contract)

1. **Run, don't claim.** Every reported estimate/CI/F/bound traces to a tool call.
2. **`bibtex` is the only citation source.** No invented references, ever.
3. **Copy-and-adapt, change nothing blindly.** The `code/` chain is a verified
   skeleton; adapt variable names and clustering to the user's design — do not swap an
   estimator without saying why.
4. **Method here, policy there.** Estimator choice is in this file; *where the result
   goes and how it is formatted* is the pack's `official-source-map.md` and
   `tables-figures` skill.
5. **Degrade honestly.** If a server is not connected, say which step is unverified and
   give the exact local command the user can run instead.

---
*Tool names reflect the StatsPAI / Stata MCP servers; confirm availability with
`available_methods` at runtime, as the catalog evolves.*
