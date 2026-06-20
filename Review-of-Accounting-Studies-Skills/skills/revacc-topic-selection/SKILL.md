---
name: revacc-topic-selection
description: Use when scoping or pressure-testing the research question for a Review of Accounting Studies (RAST) manuscript — confirming it is a contribution-driven financial-accounting question that fits RAST's archival/analytical/experimental lanes. Locks the question; it does not build the model (revacc-theory-development) or design identification (revacc-methods).
---

# Topic Selection (revacc-topic-selection)

## When to trigger

- You have a setting or a dataset (Compustat/CRSP/I/B/E/S, audit data, a disclosure event) but not yet a sharp accounting question
- The idea reads as a generic finance/economics paper that merely uses accounting data
- You cannot say in one sentence what a reader *learns about accounting* that they did not know
- The paper could plausibly go to TAR, JAR, JAE, or CAR and you are unsure RAST is the right home
- You have an analytical idea and need to decide whether RAST's modeling lane is the better fit than an empirical reframing

## What RAST rewards vs. desk-rejects

RAST publishes work whose payoff is to **financial accounting and reporting**: disclosure (voluntary and mandatory), earnings quality and management, accruals, valuation and the value-relevance of accounting numbers, capital-market consequences, analysts and forecasting, audit, and taxation. The journal's distinguishing feature is that it takes **analytical (modeling) accounting** as seriously as empirical archival work, plus a thinner experimental stream. A topic earns its place when the *accounting construct is the object of study*, not a control variable.

Desk-reject risks at RAST:

- **Finance-with-accounting-data.** A return-predictability or asset-pricing paper that happens to use an accounting variable but has no accounting mechanism or implication.
- **Atheoretical mining.** A correlation between two accounting variables with no friction, model, or institutional reason.
- **Method demonstration.** A new estimator showcased on accounting data with no accounting payoff.
- **Pure economics.** A model whose comparative statics carry no accounting reading.

## A topic-fit triage for RAST

| Signal in the draft | Inspect | Passes when |
|---------------------|---------|-------------|
| Disclosure / reporting choice is the focus | Is the disclosure the *treatment or the object*, with a friction it acts on? | The accounting choice, not a market outcome, is what we explain |
| Earnings quality / management / accruals | Is the construct measured with precedent and a clear incentive story? | A named incentive (contracting, capital-market, regulatory) drives it |
| Valuation / value-relevance / capital markets | Is there an accounting-information channel, not just a pricing pattern? | The accounting number changes beliefs or decisions, traceably |
| Analysts / forecasting | Is the information environment the mechanism, not just a proxy? | Forecast properties illuminate accounting information, not vice versa |
| Audit / tax / regulation | Is there a reporting consequence, not only an institutional description? | The institutional detail bites on a measurable reporting outcome |
| Analytical model | Is it the minimal structure yielding an *accounting* implication? | The equilibrium delivers a comparative static a reporting reader cares about |

## Lock the question

1. State the question in one sentence: "Does [accounting construct] affect [outcome] through [friction/channel]?" For analytical work: "What is the optimal [disclosure/contract/measurement] when [friction] is present?"
2. Name the lane explicitly — archival, analytical, or experimental — because it sets the rest of the chain.
3. Identify the RAST sub-audience (disclosure theorists, capital-markets empiricists, audit/tax researchers) who would cite it, and the one who would desk-reject it.
4. Separate what the current draft already establishes from what still needs data work, a model, or a literature pass.

## Checklist

- [ ] The accounting construct is the object of study, not a control
- [ ] The one-sentence question names a friction/channel (archival) or a friction/equilibrium (analytical)
- [ ] The lane (archival / analytical / experimental) is declared and matches the question
- [ ] A specific RAST sub-audience would cite this; the desk-reject risk is named
- [ ] The paper is distinguishable from a pure-finance or pure-economics submission
- [ ] Process facts (fee, portal, decision norm) are cited from the source map or marked 待核实

## Anti-patterns

- **Accounting-as-garnish:** an asset-pricing or corporate-finance paper dressed with one accounting variable.
- **Topic without payoff:** "we document an association" with no statement of what accounting learns.
- **Lane confusion:** an analytical idea jammed into an empirical frame because archival feels safer.
- **Sibling drift:** writing for TAR's contribution bar or JAR's identification bar without asking if RAST is the home.
- **Inventing fit:** asserting RAST relevance instead of naming the construct, friction, and audience.

## Output format

```text
【Journal】Review of Accounting Studies (Springer)
【Lane】archival / analytical / experimental
【One-sentence question】[accounting construct] → [outcome] via [friction/channel]
【Verdict】pass / revise / reroute
【Binding issue】the one thing blocking a clean RAST question
【RAST sub-audience】who cites it / who desk-rejects it
【Sibling boundary】why RAST and not TAR / JAR / JAE / CAR
【Source status】verified URL / 待核实 / not asserted
【Next skill】revacc-theory-development
```
