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

## Minimum referee-proof package

- Main specification table with transparent controls and fixed effects
- Alternative fixed effects, clustering, and sample restrictions
- Placebos / pre-trends / falsification outcomes
- Mechanism or heterogeneity tests tied to the finance theory
- Economic magnitudes, not only statistical significance

## Output format

```text
[Claim] causal / predictive / descriptive
[Identifying variation] ...
[Core threat] ...
[Design defense] ...
[Required robustness] ...
[Next step] jbf-data-analysis
```
