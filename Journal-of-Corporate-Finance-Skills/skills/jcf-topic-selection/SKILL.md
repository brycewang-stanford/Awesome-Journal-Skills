---
name: jcf-topic-selection
description: Use when judging whether a corporate-finance question fits the Journal of Corporate Finance (JCF) and whether it suits a full-length or "shorter format" paper. Helps scope the idea to JCF's empirical/theoretical corporate-finance remit; it does not run analysis or draft text.
---

# Topic Selection (jcf-topic-selection)

## When to trigger

- Deciding if a question belongs at JCF versus a general finance or accounting outlet
- Choosing between a **full-length original manuscript** and a **shorter format paper**
- Stress-testing a topic against JCF's active desk-rejection screen

## Scope fit (verified; re-confirm on the official guide)

JCF (Elsevier) publishes **empirical and theoretical corporate finance**. In-scope themes include:

- **Financial structure** (capital structure, debt design, leverage dynamics)
- **Governance** (boards, ownership, monitoring, control)
- **Payout** (dividends, repurchases)
- **Financial contracting** (loan covenants, security design, syndication)
- **Risk management**, **innovation/R&D financing**, **M&A**
- **International corporate finance**
- Intersections with **macro, asset pricing, household/behavioral finance, fintech/blockchain, law, financial intermediation, and market microstructure**

A pure asset-pricing test, a macro paper with no firm decision, or an accounting-measurement study with no corporate-finance question is off-fit.

## Full-length vs. shorter format

JCF explicitly invites **shorter format papers** alongside full articles, with **no fixed maximum length stated** (待核实 — no numeric ceiling found). Use the shorter format for a clean, well-identified single result; reserve full length for a multi-mechanism study with extensive robustness.

## Desk-rejection screen (self-check)

- [ ] A clear **corporate-finance decision or friction** is the object of study
- [ ] The question matters to the JCF readership, not only a niche literature
- [ ] Identification is plausible **before** you start (see jcf-identification-strategy)
- [ ] The contribution is statable in one sentence (see jcf-contribution-framing)

## Topic viability matrix

Write one row before committing:

```text
Decision/friction | Setting | Variation/model | Main outcome | Finance mechanism | Likely format
```

A viable JCF topic has a firm-side decision or contracting problem at the center. If the outcome is only a
stock return, macro shock, or accounting metric, explain how it changes corporate financing, governance,
investment, payout, risk management, innovation, or M&A. If you cannot name that mechanism, the project is
probably better routed to another finance or accounting outlet.

## Venue routing: JCF or elsewhere

```text
Project profile                                | Likely home
Firm decision + credible shock + one mechanism | JCF (shorter format if single-result)
Firm decision + broad theory contribution      | JCF full-length; a top general outlet if general-interest
Returns prediction with no firm decision       | Asset-pricing outlet, not JCF
Disclosure/earnings-quality core               | Accounting journal unless a financing decision is central
Bank/intermediary supply-side question         | Intermediation outlet; JCF if the borrowing firm is the object
Household or entrepreneur portfolio choice     | JCF only via an entrepreneurial-finance framing
Methods innovation shown on firm data          | Econometrics/methods venue; JCF wants the question
```

## Worked scoping: an M&A idea through the matrix

Hypothetical: "Do antitrust-review delays change acquirer behavior?" Matrix row (illustrative): Decision/friction = deal completion and renegotiation under regulatory uncertainty | Setting = deals near a review threshold | Variation = a threshold-rule change | Main outcome = completion rates and termination-fee design | Finance mechanism = bargaining power and deal-protection contracting | Likely format = full-length (two mechanisms: selection of announced deals plus contract redesign). The check that matters: completion is a firm decision and the fee design is a contracting outcome — both inside JCF's remit. Had the only defensible outcome been announcement returns, the row would fail and the project would belong in an asset-pricing conversation.

## Shock inventory before committing

A JCF-viable topic usually pairs the question with identifying variation on day one. Inventory candidates early: staggered statutes and governance mandates, regulatory size thresholds, index-membership rules and shareholder-vote margins (RDD material), tax reforms touching payout or financing, court rulings shifting creditor rights, disclosure-regime changes. If no plausible shock, structural model, or hand-collected wedge exists, expect the endogeneity objection to dominate the desk screen — pick a different question, or collect the data that creates the wedge (contract terms, within-firm variation).

## Anti-patterns

- A "data-availability" paper: you have CRSP/Compustat access, so you run a regression with no question.
- Repackaging a general-finance result with a thin corporate-finance label.
- Choosing full length to pad a one-result paper better suited to a shorter format.

## Output

```
【Fit】in-scope corporate-finance theme? [Y/N] — <theme>
【Format】full-length / shorter — <reason>
【Desk risk】<low/med/high> + fix
```
