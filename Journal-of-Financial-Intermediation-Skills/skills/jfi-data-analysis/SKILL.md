---
name: jfi-data-analysis
description: Use when planning or stress-testing the analysis behind a Journal of Financial Intermediation (JFI) paper — bank/loan-level panel work, demand-absorbing specifications, and the robustness battery for empirics, or numerical examples and calibrated illustrations for theory. It guides the analysis plan; it does not replace running the code.
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
  but there is no fixed robustness-table count; keep the main text compact and push secondary checks to
  appendices.

## Theory track (numerical illustration)

When the paper is a model, "data analysis" is lighter and means **reproducible computation**:

- A **numerical example** or calibrated figure showing the mechanism and comparative statics — illustrative,
  not estimation.
- Keep the code clean and deterministic (fixed seeds/parameters) so a reader can regenerate every figure.

## Data sharing (both tracks)

Prepare a **Data Statement** and link datasets via Editorial Manager; cite data with the `[dataset]` tag
(see jfi-replication-and-data-policy). Under Elsevier Option C, deposit/cite/link research data where
possible or explain why sharing is restricted.

## Dataset-to-mechanism decision table

Pick data for the intermediation mechanism, not the other way around — JFI referees notice when the
dataset cannot carry the claimed channel:

| Mechanism under study | Workhorse data | What the merge must support |
|---|---|---|
| Relationship lending / information capture | Credit register or DealScan loan-level | Multi-bank firms, so firm×time absorption is feasible |
| Capital / regulation transmission | Call Reports, FR Y-9C, stress-test exposures | Bank-level shock measured before announcement |
| Deposit competition / franchise value | FDIC Summary of Deposits, branch-level rates | Market-level (county/MSA) shares and pricing |
| Runs, liquidity, interbank stress | Supervisory or payment-system records (typically restricted) | Daily/weekly frequency around the stress window |
| Fintech displacement of banks | Platform loan tapes plus bank comparators | Comparable borrower-risk controls across lender types |

## Worked robustness pass: a capital-shock battery (illustrative)

A hypothetical JFI paper estimates that a 1pp rise in required capital cuts loan growth to the same firm
by 2.1pp (s.e. 0.6, firm×time FE, clustered by bank). The battery a JFI referee expects, each row tied to
a named threat:

- OLS without firm×time FE gives −3.0pp; report both, so the reader sees demand absorption moves the
  estimate by roughly a third — evidence the design bites, and a sorting fact worth a paragraph.
- Drop the three largest banking groups: −1.9pp — the channel is not one institution.
- Placebo reform date two years earlier: +0.2pp, insignificant — supports timing.
- Extensive margin (relationship termination) rises 1.4pp — the intermediation mechanism shows up beyond
  intensive-margin amounts.
- Few-cluster check: wild-cluster bootstrap p ≈ 0.03 with 31 banks.
- Multi-bank vs. full sample: re-estimate firm-FE-only specs on both, since the within-firm identifying
  sample skews toward larger, less bank-dependent borrowers.

## Analysis probes specific to this venue

- Referees here routinely ask for the **exposure-weighted firm-level aggregation** when real outcomes
  (investment, employment) are claimed — firm×time FE cannot be used there, so pre-shock bank shares must
  carry the identification.
- Magnitude sanity: convert the loan-level coefficient into aggregate credit terms and benchmark it
  against the range in the lending-channel literature; an estimate ten times the consensus invites a
  measurement question before a citation.
- For the theory track, a calibration table listing every parameter, its value, and its source (moment
  matched, literature, normalization) is the JFI-credible substitute for a robustness battery.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFI is banking and financial intermediation — typically corporate / bank causal designs built around regulation and shocks.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — the confounder strength that would
  overturn the headline.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each — no guessing the battery.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix. See the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
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
