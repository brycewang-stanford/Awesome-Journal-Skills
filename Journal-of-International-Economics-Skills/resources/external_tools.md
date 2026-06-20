# External Tools & Resources for JIE-Style International Economics

Data sources, software, and packages useful when preparing a *Journal of International
Economics* (JIE) submission — work in international trade (gravity, structural trade,
commercial policy, GVCs) and international macroeconomics/finance (exchange rates,
open-economy macro, sovereign debt, capital flows, international pricing). JIE publishes
both empirical and theoretical work, so this list spans data, estimation, and structural
model toolkits. Check licenses and current access terms before use.

## 1. Trade & commercial-policy data

| Source | Provider | Typical use |
|--------|----------|-------------|
| UN Comtrade | United Nations | Bilateral product-level trade flows |
| BACI (HS bilateral, cleaned) | CEPII | Gravity-ready cleaned bilateral trade |
| CEPII Gravity database | CEPII | Distance, RTAs, contiguity, language, gravity covariates |
| WITS / TRAINS | World Bank / UNCTAD | Tariffs, NTMs, market access |
| WTO Tariff & I-TIP databases | WTO | Bound/applied tariffs, trade agreements, disputes |
| OECD–WTO TiVA | OECD / WTO | Trade in value added, global value chains |
| WIOD / EORA / ADB MRIO | Multiple | Input-output linkages, GVC participation |
| Exporter Dynamics Database | World Bank | Firm-level export margins (cross-country) |

## 2. International macro & finance data

| Source | Provider | Typical use |
|--------|----------|-------------|
| IMF IFS / BOP / DOTS | IMF | Exchange rates, balance of payments, bilateral trade |
| IMF WEO | IMF | Cross-country macro aggregates and forecasts |
| BIS statistics (banking, debt, FX, EER) | BIS | Cross-border banking, effective exchange rates |
| Lane & Milesi-Ferretti External Wealth of Nations | Brookings / IMF | International investment positions, gross/net foreign assets |
| Penn World Table | UC Davis / Groningen | Real income, PPP, long-run cross-country growth |
| Reinhart–Rogoff / sovereign default datasets | Multiple | Sovereign debt, default, crisis history |
| Jordà–Schularick–Taylor Macrohistory | Multiple | Long-run macro-financial cross-country panel |
| EPFR / IMF capital-flow datasets | EPFR / IMF | Portfolio and capital flows |

## 3. Statistical & structural software

### Stata (common in empirical trade & open-economy macro)
- Gravity / PPML: `ppmlhdfe` (Poisson with high-dimensional FE), `ppml`, `gravity`-style multi-way FE via `reghdfe`
- Panel & FE at scale: `reghdfe`, `xtabond2` / `xtdpdgmm` (dynamic panels for macro growth)
- IV / weak-IV: `ivreg2`, `ivreghdfe`, `weakiv`
- Time series / open-economy macro: `var`, `svar`, local projections (`lpirf`), `dfactor`
- Inference: `boottest` (wild-cluster bootstrap), multi-way clustering

### R
- Gravity / trade: `gravity`, `fixest` (`fepois` for PPML with multiple FE, fast), `cepiigeodist`
- Panel / macro: `plm`, `lpirf` / `lpdid`, `vars`, `BVAR`
- IV / inference: `fixest::feols` IV, `sandwich`/`clubSandwich`, `fwildclusterboot`
- Reproducibility: `renv` (pin versions), `targets` (pipeline)

### Python
- `pandas`, `numpy` — data wrangling; trade-flow panel construction
- `statsmodels`, `linearmodels` (panel IV / FE), `pyfixest` (PPML / fast FE)
- `statsmodels.tsa` / `arch` — time series, GARCH for exchange-rate volatility
- `matplotlib` / `seaborn` — figures
- `pip freeze` / `requirements.txt` — pin the environment

### Structural / quantitative trade & macro
- Eaton–Kortum, Melitz, and Armington solvers; exact-hat algebra ("hat algebra") for counterfactuals
- Dynare / Dynare++ — DSGE and open-economy macro (RBC/NK small-open-economy, sovereign-debt) solution and estimation
- MATLAB / Julia (`SolveDSGE`, `QuantEcon`) — value-function iteration for default models (Eaton–Gersovitz / Arellano-style), occasionally-binding constraints

## 4. Identification & method toolkit by design

| Design | Core checks | Tools |
|--------|-------------|-------|
| Gravity (PPML) | Multilateral-resistance / importer×exporter×time FE, zeros retained, Santos Silva–Tenreyro diagnostics | `ppmlhdfe`, `fixest::fepois` |
| Trade-policy shock (tariffs, RTAs) | Pre-trends, staggered-adoption estimators, lagged-effects of agreements | `csdid`, `reghdfe`, `fixest` |
| Shift-share / Bartik exposure (e.g., China shock) | Exogeneity of shares vs shifts, Adao–Kolesar–Morales inference, Borusyak–Hull–Jaravel | `ssaggregate`, custom |
| Exchange-rate pass-through / pricing | Currency-of-invoicing controls, horizon-specific local projections | `lpirf`, `arch` |
| Sovereign default / open-economy DSGE | Model fit to spreads/cyclicality, calibration vs estimation, sensitivity | Dynare, Julia/MATLAB |

## 5. Figures
- Gravity/event-study coefficient plots; exchange-rate pass-through impulse responses with bands
- Counterfactual welfare/trade-share bar charts from structural models
- Vector output (PDF/EPS) for print resolution; confidence bands shown; avoid chartjunk

## 6. Reproducibility & replication (JIE requires deposit)
- All published JIE papers must deposit computer programs and data sets in the **journal's secure repository (Mendeley Data)** — build the package as you go
- One master script (`run_all`) regenerating every table and figure from raw data
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` versions); set and report seeds for any simulation/estimation
- For structural papers, ship the solver code and calibration files, not just regression scripts

## 7. Writing, references & process
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote. JIE applies its reference style at the **proof stage**, so submit in any consistent style with all required elements (author names, title, year, volume, article number/pages); **DOIs encouraged**
- Abstract: **150 words max**, factual, single paragraph, references avoided; **1-7 keywords**
- Submission portal: **Editorial Manager**; non-refundable fee **USD 190 / EUR 169.20 / JPY 20,660** (USD 95 if all authors are PhD students); the **Prior Review Process (PRP)** carries decision letters + referee reports from AER/Econometrica/JPE/QJE/REStud at no extra fee
- Short Papers: **≤6,000 words** and **≤5 exhibits**, with the required word-count PDF; do not apply this cap to regular submissions
- Prepare JEL classification codes only if the live submission system asks for them; the current Guide-confirmed metadata are the abstract and **1-7 keywords**

## 8. Cautions
1. **Verify volatile specifics** (fee, editors, deposit rules, portal URL) on the official Guide for Authors before upload.
2. **Use PPML, not log-OLS, for gravity** when zeros and heteroskedasticity matter (Santos Silva–Tenreyro).
3. **Match the estimator to the design** — staggered RTA/tariff adoption needs modern DID estimators; shift-share needs share-exogeneity arguments.
4. **Reproducibility is mandatory at JIE** — assemble the Mendeley Data deposit before acceptance, not after.
