---
name: jie-data-analysis
description: Use when building or auditing the empirical analysis for a Journal of International Economics (JIE) manuscript — constructing bilateral trade panels, estimating PPML gravity, running open-economy panels and local projections, calibrating/estimating structural models, and producing the robustness suite international-economics referees expect. Strengthens the analysis; it does not fabricate results.
---

# Data Analysis (jie-data-analysis)

## When to trigger

- Assembling a bilateral trade panel or a cross-country macro/finance panel
- Choosing the gravity estimator and fixed-effect structure
- Deciding which robustness checks an international-economics referee will demand
- Disciplining a structural open-economy or trade model against the data

## Empirical norms at JIE

JIE referees come from international trade or international macro/finance and apply that field's conventions. Match them.

### Data construction
- **Trade**: build bilateral product-level flows from UN Comtrade or the cleaned **BACI** (CEPII); merge gravity covariates from the **CEPII Gravity** database (distance, contiguity, common language, RTAs); tariffs/NTMs from WITS/TRAINS or WTO. Keep **zeros** — they are informative and PPML uses them.
- **International macro/finance**: assemble panels from IMF IFS/BOP/DOTS, BIS, the **External Wealth of Nations** (Lane–Milesi-Ferretti), Penn World Table; sovereign-debt/default histories from established crisis datasets.

### Estimation
- **Gravity → PPML** (`ppmlhdfe`, `fixest::fepois`) with importer×time, exporter×time, and pair fixed effects; report the trade elasticity.
- **Cross-country macro panels** → fixed effects with care for dynamic-panel bias (`xtabond2`/`xtdpdgmm` where lagged dependent variables matter); cluster appropriately.
- **Dynamics** → local projections (`lpirf`) for pass-through and impulse responses; VAR/BVAR where warranted.
- **Structural** → solve and calibrate/estimate (Dynare for DSGE; exact-hat algebra for trade counterfactuals); report targeted and untargeted moments.

### Robustness suite (referees will ask)
- Alternative fixed-effect structures and samples; alternative trade-cost proxies.
- Sensitivity to the **trade elasticity** (and, for macro, to risk aversion / discount factor).
- Modern DID estimators if any staggered policy timing is involved.
- Design-based inference for shift-share exposure; multi-way clustering for dyadic data.
- Counterfactual robustness to the elasticities that cannot be pinned down precisely.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIE is international trade/macro; cross-country/firm panels — emphasize identification and clustering.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Data sources documented and merge keys (ISO country, HS product, year) clean
- [ ] Zeros retained for gravity; PPML used with multilateral-resistance FE
- [ ] Estimator matched to data structure (dyadic, dynamic panel, time series, structural)
- [ ] Inference matched to the design (multi-way / design-based / cluster-robust)
- [ ] Economic magnitudes (elasticities, welfare, pass-through) reported, not just significance
- [ ] Robustness to key elasticities and specifications shown
- [ ] Every number traceable to a script for the replication deposit

## Anti-patterns

- Log-OLS gravity dropping zeros (biased per Santos Silva–Tenreyro)
- Single-clustered standard errors on dyadic trade data
- A structural model matched to one moment and declared validated
- Reporting stars without the trade/welfare/pass-through magnitude
- Ad hoc analysis with no script trail, breaking the mandatory replication deposit later

## Referee-pushback patterns and the JIE-specific fix

The objections an international-economics referee raises most, with the move that resolves each. Each maps to a concrete change in the empirical section.

- "Gravity estimates without multilateral resistance / still on log-OLS." Fix: re-estimate with PPML (`ppmlhdfe`/`fepois`), importer×time and exporter×time fixed effects, pair fixed effects for policy effects; keep zeros; report the elasticity, not just significance.
- "Trade-policy variable is endogenous — RTAs form where trade is already growing." Fix: pair fixed effects to absorb time-invariant selection, pre-trend event study, phase-in/anticipation modelled, and a falsification on flows the policy should not touch.
- "Shift-share exposure may proxy a local trend." Fix: state whether identification rests on exogenous shares or shifts, use Adao–Kolesar–Morales or Borusyak–Hull–Jaravel inference, and show exposure is uncorrelated with pre-period trends.
- "Quantitative model is not disciplined by the data." Fix: tabulate targeted vs untargeted moments, report counterfactuals under a range of trade elasticities, and show the headline result is not an artifact of one un-pinned-down parameter.
- "Inference ignores dyadic dependence." Fix: multi-way (exporter and importer) clustering, not a single cluster dimension.

## Worked micro-example (illustrative numbers)

A gravity panel of bilateral manufacturing trade, 60 countries × 20 years, asking whether an RTA raises members' trade. Log-OLS on positive flows returns an RTA coefficient of, say, 0.55 (about a 73% increase). Re-estimating in PPML with importer×time, exporter×time, and pair fixed effects — retaining the ~30% of dyad-years with zero trade — the coefficient falls to roughly 0.20 (about 22%). That drop is the textbook Santos Silva–Tenreyro pattern: log-OLS over-weighted small positive flows and discarded informative zeros. Multi-way clustering on exporter and importer widens the standard error enough that the honest takeaway is "a modest, precisely-bounded RTA effect," not the inflated log-OLS number. (Figures illustrative, chosen to show the mechanism.)

## Output format

```
【Data】sources + unit (dyad-year / country-year / firm-year)
【Estimator】PPML+FE / dynamic panel / local projection / structural
【Inference】multi-way / design-based / cluster-robust
【Magnitudes】[elasticity / welfare / pass-through reported]
【Robustness done】[FE structures, elasticity sensitivity, modern DID, ...]
【Robustness missing】[...]
【Next step】jie-contribution-framing or jie-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Comtrade/BACI/CEPII/WITS, IMF/BIS/EWN/PWT data + `ppmlhdfe`/`fepois`/Dynare toolkits
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope and data-policy sources
