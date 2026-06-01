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
