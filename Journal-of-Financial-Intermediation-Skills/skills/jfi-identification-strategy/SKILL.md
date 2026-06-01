---
name: jfi-identification-strategy
description: Use to audit the core analytical engine of a Journal of Financial Intermediation paper — for empirics, the causal design for a banking/credit question; for theory, the assumptions, equilibrium discipline, and proof exposition. It pressure-tests the design; it does not run the analysis.
---

# Identification Strategy (jfi-identification-strategy)

## When to trigger

- Setting up or defending the empirical design of a banking/intermediation paper
- Setting up or defending the assumptions and propositions of a theory paper

## Empirical track (applied banking / credit)

JFI referees are unforgiving on identification in bank data. Build a credible **causal design** and defend
it:

- **Source of variation:** a regulatory change, supervisory shock, branching deregulation, a discontinuity
  in capital/eligibility rules, or a plausibly exogenous credit-supply shifter.
- **Modern estimators:** staggered DID with heterogeneity-robust estimators (Callaway–Sant'Anna,
  Sun–Abraham, de Chaisemartin–D'Haultfœuille), IV with weak-IV-robust inference, or RDD with the
  rdrobust toolkit.
- **Bank-data-specific threats:** bank selection into treatment, borrower–firm sorting, balance-sheet
  timing and mechanical reverse causality, and the **lending-channel separation** of credit supply from
  demand (firm×time fixed effects in matched lender–borrower panels).
- **Inference:** cluster at the level of treatment assignment (often bank or market); wild-cluster
  bootstrap when clusters are few.

## Theory track (intermediation models)

When the contribution is a **model**, identification means **analytical discipline**:

- State **assumptions** transparently and motivate each economically (what friction it encodes).
- Make **results** precise as propositions/lemmas; keep **proof exposition** readable — sketch the
  mechanism in the text, full proofs in an appendix.
- Argue **generality**: which results survive relaxed assumptions, and where the boundary lies.
- A **numerical example** (see jfi-data-analysis) can illustrate the mechanism without claiming empirical
  estimation.

## Anti-patterns

- OLS-plus-controls dressed up as identification on a bank panel
- Conflating credit supply and demand without firm×time absorption
- A theory whose key result silently depends on an unstated assumption
- Clustering at the wrong level, or ignoring few-cluster inference

## Output format

```
【Track】empirical / theory
【Design or assumptions】<the variation, or the key assumptions>
【Top threat / boundary】<the main objection + answer>
【Inference / generality】<clustering, or which results survive>
【Next skill】jfi-data-analysis
```
