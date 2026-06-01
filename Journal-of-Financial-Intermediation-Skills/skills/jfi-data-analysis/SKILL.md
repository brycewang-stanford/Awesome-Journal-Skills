---
name: jfi-data-analysis
description: Use to plan and stress-test the analysis behind a Journal of Financial Intermediation paper — bank/loan-level panel work and robustness for empirics, or numerical examples and calibrated illustrations for theory. It guides the analysis plan; it does not replace running the code.
---

# Data Analysis (jfi-data-analysis)

## When to trigger

- Building the empirical analysis on bank/firm/loan data, or its robustness battery
- Building a numerical example or calibration that illustrates a model's mechanism

## Empirical track (banking data)

- **Sample construction:** document the universe (e.g., Call Reports / FR Y-9C banks, DealScan loans,
  HMDA mortgages), merge keys, and every filter; intermediation samples are sensitive to mergers, charter
  changes, and reporting breaks.
- **Variables:** define balance-sheet and credit quantities precisely (levels vs. growth, winsorizing,
  deflation); state timing relative to the shock to avoid mechanical reverse causality.
- **Specifications:** high-dimensional fixed effects (reghdfe / fixest); for credit-supply questions, use
  firm×time effects in matched lender–borrower panels to absorb demand.
- **Robustness:** alternative samples and windows, placebo periods, leave-one-out by large institutions,
  alternative clustering, and a balance/parallel-trends check for DID. The expected battery is substantial
  but there is **no fixed length cap** (待核实).

## Theory track (numerical illustration)

When the paper is a model, "data analysis" is lighter and means **reproducible computation**:

- A **numerical example** or calibrated figure showing the mechanism and comparative statics — illustrative,
  not estimation.
- Keep the code clean and deterministic (fixed seeds/parameters) so a reader can regenerate every figure.

## Data sharing (both tracks)

Prepare a **Data Statement** and link datasets via Editorial Manager; cite data with the `[dataset]` tag
(see jfi-replication-and-data-policy). JFI has **no** mandatory code archive, but sharing is expected.

## Anti-patterns

- Undocumented sample filters that drive the result
- Mixing credit supply and demand without firm×time absorption
- A theory "calibration" presented as if it were estimation
- Non-reproducible figures (random seeds, manual steps)

## Output format

```
【Track】empirical / theory
【Sample / parameters】<universe + filters, or calibration>
【Core spec / example】<FE structure, or the numerical illustration>
【Robustness】<the battery, or seed/determinism notes>
【Next skill】jfi-contribution-framing
```
