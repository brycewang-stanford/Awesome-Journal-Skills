---
name: jie-identification-strategy
description: Use when the identification or modelling strategy is the bottleneck for a Journal of International Economics (JIE) manuscript — gravity/PPML, trade-policy (tariff/RTA) shocks, shift-share/Bartik exposure, exchange-rate pass-through, or a structural open-economy model whose discipline against data is the "identification." Stress-tests the design to the JIE field bar before tables are drafted.
---

# Identification / Modelling Strategy (jie-identification-strategy)

## When to trigger

- Your gravity regression is log-OLS and a referee will ask about zeros and heteroskedasticity
- A trade-policy effect is identified off staggered RTA/tariff timing with plain TWFE
- A shift-share (China-shock-style) design lacks a share- or shift-exogeneity argument
- An open-economy/structural model's mapping to the data is not disciplined
- You are unsure your design clears JIE's field-level credibility bar

## The JIE identification bar

JIE judges credibility by the **standards of international economics**, where "identification" can be either a quasi-experimental design **or** the discipline a structural model imposes on the data. Both halves of the field have their own conventions; pick the branch that matches your paper.

## Branch A: Gravity (the workhorse of empirical trade)

- Use **PPML** (`ppmlhdfe`, `fixest::fepois`), not log-OLS: it handles **zeros** and the heteroskedasticity that Santos Silva–Tenreyro showed bias log-linear gravity.
- Control **multilateral resistance** with importer×time and exporter×time fixed effects; for policy effects add country-pair fixed effects.
- Report the elasticity with an economic interpretation, not just a t-stat.

## Branch B: Trade-policy shocks (tariffs, RTAs, NTMs)

- Staggered agreement/tariff adoption → move beyond TWFE: Callaway–Sant'Anna, Sun–Abraham, or de Chaisemartin–D'Haultfœuille; show pre-trends with an event study.
- Address anticipation and phase-in (agreements take effect over years).
- Falsification: effects absent for trade flows the policy should not touch.

## Branch C: Shift-share / Bartik exposure (e.g., the China shock)

- State whether identification rests on **exogenous shares** or **exogenous shifts**.
- Use design-based inference: Adao–Kolesar–Morales standard errors or the Borusyak–Hull–Jaravel shift-level approach.
- Show the exposure measure is not proxying for a confounding local trend.

## Branch D: Exchange rates, pass-through, international pricing

- Specify horizon (impulse responses / local projections) and control for currency of invoicing.
- Distinguish the exchange-rate movement's source (the "disconnect" problem); a raw correlation is not pass-through.

## Branch E: Structural / open-economy macro (model is the identification)

- Map the model to **targeted moments** (spreads, cyclicality of the current account, pass-through elasticities) and report untargeted moments it also matches.
- For sovereign default (Eaton–Gersovitz / Arellano) or small-open-economy DSGE, state calibration vs estimation and show sensitivity to key elasticities (trade elasticity, risk aversion).
- Counterfactuals (often via exact-hat algebra in trade) must be robust to the elasticity you cannot pin down precisely.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIE is international trade/macro; cross-country/firm panels — emphasize identification and clustering.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Design/branch named and matched to scope half (trade vs macro-finance)
- [ ] Gravity uses PPML with multilateral-resistance fixed effects (if applicable)
- [ ] Staggered policy timing uses a modern DID estimator with pre-trends (if applicable)
- [ ] Shift-share share/shift exogeneity argued with design-based inference (if applicable)
- [ ] Structural model disciplined against targeted + untargeted moments (if applicable)
- [ ] Inference matched to the design; counterfactuals shown robust to key elasticities
- [ ] The claim never exceeds what the design or model supports

## Anti-patterns

- Log-OLS gravity that drops zeros and ignores heteroskedasticity
- TWFE on staggered RTA/tariff adoption with no heterogeneity-bias discussion
- A shift-share design with conventional standard errors and no exogeneity argument
- A calibrated model that matches one moment and is sold as validated
- A local trade/pass-through estimate oversold as a structural global parameter

## Referee-pushback patterns with the venue fix

The four objections that sink identification at JIE, and the move that answers each: "gravity without multilateral resistance / on log-OLS" → PPML with importer×time and exporter×time fixed effects, zeros retained, elasticity reported; "trade-policy timing is endogenous" → pair fixed effects, a pre-trend event study, modelled phase-in, and a falsification on untouched flows; "shift-share exposure proxies a local trend" → an explicit share-vs-shift exogeneity claim with Adao–Kolesar–Morales or Borusyak–Hull–Jaravel inference; "the quantitative model is not disciplined by the data" → targeted and untargeted moments side by side, plus a counterfactual that survives a sweep over the un-pinned-down trade elasticity. Naming the branch (A–E) and pre-empting its signature objection in the design section is what separates a credible JIE identification from one a referee can puncture in a paragraph.

## Output format

```
【Branch】gravity / trade-policy shock / shift-share / pass-through / structural
【Scope half】trade / macro-finance
【Identifying variation or model discipline】one sentence
【Diagnostics done】[PPML+FE, pre-trends, AKM inference, moment fit, ...]
【Diagnostics missing】[...]
【Counterfactual robustness】key elasticities varied? [Y/N]
【Next step】jie-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `ppmlhdfe`/`fepois`, modern DID estimators, AKM inference, Dynare/Julia structural toolkits
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope and editor-roster sources
