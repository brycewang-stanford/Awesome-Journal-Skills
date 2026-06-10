---
name: jbf-topic-selection
description: Use when deciding whether an empirical or theoretical finance manuscript fits the Journal of Banking & Finance (JBF) scope, especially banking, financial intermediation, financial institutions, capital markets, investments, corporate finance, or financial regulation.
---

# Topic Selection (jbf-topic-selection)

## When to trigger

- A finance paper could go to JBF, JFI, JCF, JFQA, RFS, or a field journal and you need a fit call
- The project is about banks, intermediaries, regulation, liquidity, credit, investments, or capital markets
- You need to decide whether the paper is strong enough for JBF or should be routed elsewhere

## JBF fit bar

JBF is not a generic "any finance paper" outlet. It rewards papers that make a
clear contribution to banking, financial intermediation, institutions, markets,
investments, corporate finance, or regulation. A good JBF topic usually has:

1. **A finance question with institutional content**: banks, lenders, funds,
   markets, regulation, disclosure, risk-taking, liquidity, credit supply, or
   capital allocation.
2. **A credible design or model**: empirical identification, careful data
   construction, or a theoretical mechanism with testable implications.
3. **External relevance**: implications for financial institutions, investors,
   regulators, or corporate financing decisions.
4. **A result that changes a finance reader's prior** rather than only adding a
   new sample, country, or dataset.

## Strong fits

- Bank capital, liquidity, risk-taking, supervision, stress tests, or credit supply
- Financial intermediation, shadow banking, fintech lending, syndicated loans
- Market liquidity, trading, asset pricing with institutional frictions
- Corporate finance questions where banks or financing constraints are central
- Regulation/policy shocks with clear finance mechanisms

## Weak fits

- Pure accounting, management, macro, or development papers where finance is only context
- Asset-pricing factor papers with no JBF-specific institutional contribution
- Country case studies without credible identification or generalizable finance insight
- Routine event studies without an economic mechanism

## Neighbor-venue routing matrix

| Paper profile | Better-first venue | Why |
| --- | --- | --- |
| Intermediation theory or structural banking model with a tight mechanism | Journal of Financial Intermediation | narrower, mechanism-first intermediation outlet |
| Systemic risk / macroprudential policy evaluation | Journal of Financial Stability | stability-policy core audience |
| Monetary transmission through banks, macro-banking | JMCB | money-macro referee pool |
| Corporate finance where banks are peripheral | Journal of Corporate Finance | firm-side audience |
| Broad empirical banking/markets/regulation with solid identification and a policy angle | JBF | wide empirical scope, bank-focused readership |

These are stylized scope contrasts; check each journal's current aims-and-scope before final routing.

## Worked fit call (illustrative)

Candidate question: "Do BNPL fintech lenders substitute for credit-card lending by small banks?"

- Institutional content: yes — nonbank entry into consumer credit and the bank funding response; fit bar 1 passes.
- Design: staggered fintech entry across local markets with bank × market data; passes only if entry timing is defensibly exogenous (route to `jbf-identification-strategy`).
- Prior-changing: if the answer is "entry cuts incumbent card balances by an illustrative 6%," it shifts priors on fintech substitution versus market expansion — JBF-relevant.
- Verdict: strong JBF fit; JFI only if the paper builds a substitution model first.

## Two-minute screening questions

1. Which intermediation friction sits at the center: capital, liquidity, information, competition, or regulation?
2. Would a bank supervisor, risk officer, or lender change a decision given the result?
3. Does the design produce a magnitude in finance units (basis points, percentage points of assets) a referee can benchmark?
4. Is there a JBF-relevant strand where this is the next paper rather than a duplicate?

Answer all four before routing onward; a "no" on question 1 or 4 usually means reroute rather than rewrite.

## Scope-based desk risks

- Banking data used to answer a labor, IO, or development question → desk risk: the finance mechanism is incidental.
- A single-country banking-crisis case study without generalizable variation → desk risk unless the institutional setting isolates a mechanism.
- A risk-model horse race with no intermediation or policy stake → reroute, or add an economic application before submitting.

## Output format

```text
[Question] one sentence
[JBF fit] strong / possible / weak
[Core finance mechanism] ...
[Evidence or model needed] ...
[Closest alternatives] JFI / JCF / JFQA / field journal / other
[Next step] jbf-literature-positioning or reroute
```
