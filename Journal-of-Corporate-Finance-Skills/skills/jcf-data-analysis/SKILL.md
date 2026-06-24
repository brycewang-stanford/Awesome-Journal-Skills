---
name: jcf-data-analysis
description: Use when building and running the empirical analysis for a Journal of Corporate Finance (JCF) paper — assembling WRDS-era firm panels (Compustat/CRSP/SDC/DealScan), constructing variables, estimating with fixed effects and clustered errors, and layering robustness. It guides the empirical build; pair it with jcf-identification-strategy for the design itself.
---

# Data Analysis (jcf-data-analysis)

## When to trigger

- Assembling the firm-level panel and constructing corporate-finance variables
- Choosing estimators, fixed effects, and clustering
- Planning the robustness battery a JCF referee will expect

## Data build (empirical corporate finance)

- Core sources: **Compustat** (fundamentals, leverage, payout), **CRSP** (returns/event windows), **CCM** (linked), **SDC/Refinitiv** (M&A, IPO/SEO, repurchases), **DealScan** (loans/covenants), **BoardEx/ISS/Execucomp** (governance, pay). Respect WRDS/vendor licenses — never redistribute raw vendor data.
- Document **sample construction** (filters, financials/utilities exclusions, fiscal-year alignment), **winsorizing** (e.g., 1/99), and every variable's formula.

## Estimation conventions

- **High-dimensional fixed effects** (`reghdfe` / `fixest`): firm, year, and often industry×year.
- **Cluster** standard errors at the firm level (and/or two-way firm-and-year) consistent with the variation.
- For staggered-adoption DID, use **modern estimators** (see jcf-identification-strategy), not plain TWFE.
- Report economic magnitudes, not just significance — JCF readers want the size of the effect on a corporate-finance outcome.

## Robustness the referee expects

- [ ] Alternative variable definitions and subsamples (size, period, industry)
- [ ] Alternative fixed-effects / clustering structures
- [ ] Endogeneity probes consistent with the design (placebo, falsification, alt. instrument)
- [ ] Sensitivity to outliers / winsorizing thresholds
- [ ] A short, honest discussion of remaining limitations

## Reproducibility (ties to data policy)

- One master script (`run_all`) regenerating every table/figure from the build.
- Pin software/package versions; set seeds for bootstrap/simulation.
- Prepare the **Elsevier Option C** data-availability statement and code/variable-construction archive now, not at acceptance (see jcf-replication-and-data-policy).

## Firm-panel audit ledger

Before adding robustness, build a ledger:

```text
Claim | Firm sample | Event/date rule | Variable formula | FE/clustering | Output file
```

Use it to catch the most common JCF weaknesses:

- fiscal-year alignment changes treatment timing;
- financial firms/utilities exclusions alter the estimand;
- winsorization or missing-value rules drive the result;
- two-way clustering is needed but only one dimension is reported;
- an event-window result uses CRSP/Compustat links that are not documented.

Every main result should also have an economic magnitude row. If the table cannot say what a coefficient
means for leverage, payout, investment, governance, innovation, or financing constraints, the result is not
ready for a corporate-finance audience.

## Variable-construction crosswalk (Compustat conventions)

JCF referees read variable definitions before coefficients. Anchor each outcome to a recognized construction and disclose deviations:

```text
Outcome            | Conventional construction                        | Disclosure trap
Book leverage      | (dltt + dlc) / at                                | Mixing book and market denominators across tables
Market leverage    | debt / (debt + prcc_f x csho)                    | Stale prices at fiscal-year ends
Payout             | dv and prstkc scaled by assets or earnings       | Repurchase proxy ignores option-related buybacks
Investment         | capx / lagged at (or PP&E)                       | Intangibles-heavy firms mismeasured; say so
Cash holdings      | che / at (or net assets)                         | Net-of-cash denominators change percentile meaning
Tobin's q          | (at + mkt equity - book equity) / at             | A dozen variants exist — name yours and cite it
Board independence | independent directors / board size (BoardEx/ISS) | Vendor classification shifts over sample years
CEO pay            | ExecuComp tdc1                                   | Option-valuation regime breaks across decades
```

## Worked build: a board-reform firm panel

Hypothetical (numbers illustrative): a governance mandate forces some boards to hit an independence threshold. Build trace: Compustat–CRSP universe 1996–2020 → drop financials (SIC 6000–6999) and utilities (4900–4999) → require BoardEx coverage → final panel of 2,400 firms and 21,000 firm-years. Treated = firms below the threshold pre-mandate (38% of the panel). Ledger rows written before estimation: the treatment-date rule (fiscal years ending after the compliance deadline), the independence formula, the FE plan (firm and industry-by-year), clustering (firm). When the headline says investment rises 1.1 percentage points of assets for treated firms, the magnitude row converts it: about 12% of the sample mean — a number a JCF reader can judge.

## Estimation pushback JCF referees raise

- "Cluster by firm AND year." → Re-estimate two-way; if inference survives, report it in the main table, not a footnote.
- "Your treated firms chose to be below the threshold." → Add a selection-into-treatment discussion plus a covariate-trend table comparing treated/control before the mandate.
- "Winsorizing drives this." → Re-run at 0.5/99.5, 2/98, and trimmed; one appendix table, three columns.
- "Industry-by-year shocks explain it." → Show the coefficient with and without industry × year FE side by side; if it dies, the paper has a confounding problem, not a formatting one.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JCF is corporate finance — endogeneity of corporate policies is the central threat; foreground IV/DiD identification.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Kitchen-sink controls with no design and no magnitudes.
- Hidden sample-selection steps that change the result.
- Significance-only reporting with no economic interpretation.

## Output

```
【Panel】sources + filters + winsor: documented? [Y/N]
【Spec】FE = <…>; cluster = <…>; estimator = <…>
【Robustness】<list run / planned>
```
