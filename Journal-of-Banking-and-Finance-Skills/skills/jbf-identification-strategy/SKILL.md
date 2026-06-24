---
name: jbf-identification-strategy
description: Use when stress-testing the empirical identification strategy for a Journal of Banking & Finance manuscript, including bank panels, policy shocks, event studies, IV, staggered DID, dynamic panels, and endogeneity threats.
---

# Identification Strategy (jbf-identification-strategy)

## When to trigger

- The main result is empirical and could be challenged as endogenous
- The design uses bank panels, regulatory shocks, event studies, IV, RDD, or dynamic panels
- You need to decide which robustness and falsification tests JBF referees will ask for

## JBF credibility bar

Finance referees usually ask whether the result is driven by omitted risk,
selection, reverse causality, market-wide shocks, or correlated bank/firm traits.
The design must make the identifying variation visible.

## Design checks by strategy

### Bank or firm panels

- State the unit, time period, and identifying variation.
- Use fixed effects that match the claim: bank, firm, borrower, market, time,
  bank-by-market, industry-by-year, or borrower-by-year as needed.
- Cluster at the treatment or shock level; use two-way clustering when shocks vary
  by unit and time.

### Staggered DID / policy shocks

- Show treatment timing and untreated/control units.
- Avoid relying only on plain TWFE when treatment effects may be heterogeneous.
- Report modern DID/event-study estimates and pre-trend tests.
- Explain why anticipation, selection into treatment, and concurrent shocks do not
  drive the result.

### IV / dynamic panels

- Defend exclusion, not just relevance.
- Report first-stage strength and weak-IV-robust inference where relevant.
- For system GMM, limit instrument proliferation and report serial-correlation
  and overidentification diagnostics.

### Event studies

- Define event, estimation window, event window, benchmark model, and clustering.
- Separate market reaction from real effects.
- Add placebo event dates or unaffected securities when possible.

## Regulation-shock design picker

| Variation available | Preferred JBF design | What referees will check |
| --- | --- | --- |
| Staggered adoption across states/countries (deregulation, Basel phase-ins) | Stacked or heterogeneity-robust DID with an event-study plot | negative-weight risk of plain TWFE; control-group composition |
| Supervisory size thresholds ($10bn/$50bn-style cutoffs) | Local comparison around the cutoff with donut and bunching checks | asset manipulation near the cutoff; other rules at the same threshold |
| Single national shock (LCR, IFRS 9, deposit-insurance change) | Pre-determined bank-level exposure × post | exposure correlated with business models; bank and time FE plus exposure trends |
| Examiner or supervisory assignment | Quasi-random assignment design | evidence the rotation/assignment process is plausibly exogenous |

## Worked threat audit (illustrative)

Claim: banks crossing a $10 billion supervisory threshold cut small-business lending.

- Naive estimate: −3.1% loan growth for crossers (illustrative). Threat: banks time acquisitions to cross, so crossers differ.
- Fix 1: restrict to organic-growth crossers; suppose the estimate moves to −2.2% — report both.
- Fix 2: donut specification plus a bunching plot of the asset distribution; visible bunching below the cutoff must be discussed, not assumed away.
- Fix 3: placebo thresholds at $8bn and $12bn where no rule changes; effects there should be near zero.

## Clustering quick rules for bank data

- Policy varies by state or country → cluster at the policy level; with few clusters, wild-cluster bootstrap.
- Bank-quarter panel with bank-level treatment → cluster by bank; two-way (bank and quarter) when macro shocks load on outcomes.
- Loan-level data with repeat borrowers → cluster by borrower (or two-way with bank), and justify the choice in the table note.

## Pushbacks JBF referees raise

- "The regulation applied to everyone — where is the control group?" → switch to an exposure design with pre-period balance evidence.
- "Pre-trends look noisy." → add a joint pre-trend test and a sensitivity bound, not only the plot.
- "Weak banks attract supervision (reverse causality)." → show treatment does not predict pre-period outcomes.
- "Banks adjust before the rule binds (anticipation)." → re-center event time on the announcement date and show both timelines.
- "Other Basel rules phased in simultaneously." → restrict to windows where only one rule changes, or exploit exposure differences across rules.

## Minimum referee-proof package

- Main specification table with transparent controls and fixed effects
- Alternative fixed effects, clustering, and sample restrictions
- Placebos / pre-trends / falsification outcomes
- Mechanism or heterogeneity tests tied to the finance theory
- Economic magnitudes, not only statistical significance

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JBF is empirical banking/finance — corporate/bank causal designs around regulation and shocks.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Claim] causal / predictive / descriptive
[Identifying variation] ...
[Core threat] ...
[Design defense] ...
[Required robustness] ...
[Next step] jbf-data-analysis
```
