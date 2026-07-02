---
name: jae-theory-development
description: Use when building the economic argument and predictions for a Journal of Accounting and Economics (JAE) manuscript — grounding hypotheses in agency, information-economics, contracting, or disclosure theory so the paper applies economic theory to explain accounting phenomena rather than reporting a bare correlation.
---

# Theory Development for JAE (jae-theory-development)

## When to trigger

- Your predictions read as "A is associated with B" with no economic logic
- A reviewer asks "what is the economic mechanism?" or "why would a rational agent do this?"
- You have a result but no model of the friction generating it
- You are deciding whether to support predictions with an analytical model or with cited economic theory

## JAE's theory bar: apply economics to accounting

JAE exists to **apply economic theory to explain accounting phenomena**. A prediction must follow from an economic primitive, not from intuition. The canonical building blocks are:

- **Agency theory** (Jensen-Meckling): contracting and monitoring of manager-shareholder and shareholder-creditor conflicts; accounting numbers as inputs to compensation and debt contracts.
- **Information economics / disclosure theory** (Grossman-Hart-Milgrom unraveling; Verrecchia, Diamond-Verrecchia): when and why managers disclose, and the price/liquidity consequences of information asymmetry.
- **Positive Accounting Theory** (Watts & Zimmerman, the founding editors): the bonus, debt-covenant, and political-cost determinants of accounting choice.
- **Contracting cost and the theory of the firm**: efficient-contracting explanations for accounting conservatism, recognition, and verifiability.

Your job is to derive a **directional, falsifiable prediction** from one of these, naming the agents, their objectives, the constraint, and the equilibrium behavior accounting affects.

## Build the argument

1. **State the friction.** Information asymmetry between whom? Which agency conflict? What contracting/regulatory constraint?
2. **Name the economic actors and incentives.** Managers, shareholders, creditors, analysts, auditors, regulators — each with an objective function.
3. **Derive the prediction.** Show how the friction plus incentives imply a sign on the relation; predictions are *a priori*, not reverse-engineered from the data.
4. **Specify cross-sectional variation.** JAE prizes partitioning tests: the effect should be stronger where the friction is more severe (e.g., higher information asymmetry, tighter covenants, weaker governance) — this is your sharpest evidence of mechanism.

## Micro-rewrite: from association to economic hypothesis

- **Before**: "H1: Accounting conservatism is positively associated with debt financing." — a sign with no agents, no friction, and no way to distinguish an equilibrium from a coincidence.
- **After**: "Creditors hold payoffs concave in firm value and cannot observe managerial actions, so they price protection they cannot fully contract on; timely loss recognition substitutes for costly direct monitoring. H1: After a shock that raises creditor monitoring demand, borrowers increase conditional conservatism, and the increase concentrates in firms with the least covenant slack." — the friction (asymmetric payoffs plus unobservable actions), the actors (creditors and borrowers), an a priori sign, and the mechanism partition are on the table before any regression runs.

## Opportunism vs. efficient contracting: pick a side

Positive-accounting predictions come in two flavors that JAE referees will force apart: **opportunism** (managers exploit reporting discretion for bonus, covenant, or political reasons) and **efficient contracting** (the same accounting choice minimizes contracting costs ex ante, anticipated and priced by counterparties). Both often predict the same first-order sign; they separate in the cross-section and in consequences — pricing penalties, contract redesign, turnover follow opportunism, not efficiency. Declare which interpretation your evidence supports and build at least one test that could tell them apart; a paper that never confronts the efficiency alternative reads as half a theory at this venue.

## A hypothesis table before the data

Keep a one-row discipline per hypothesis: friction → actors → predicted sign → cross-sectional partition → rival explanation it excludes. A blank cell means the hypothesis is not yet derived; two hypotheses sharing every cell are one hypothesis.

## Analytical vs. archival theory

JAE publishes both economics-style **analytical models** (clean assumptions, propositions, proofs in an appendix) and **archival** papers whose theory is cited rather than modeled. If your contribution is the model itself, develop it formally; if the contribution is empirical, ground the hypotheses in existing economic theory and reserve formal modeling for the appendix.

## Checklist

- [ ] Each prediction derives from an economic primitive (agency / information / contracting / political cost)
- [ ] Economic actors, objectives, and the friction are explicitly named
- [ ] Predictions are directional, falsifiable, and *a priori*
- [ ] Cross-sectional partitions tie effect size to friction severity
- [ ] Analytical claims have stated assumptions and proofs; archival claims cite the theory
- [ ] Alternative economic explanations are anticipated, not ignored

## Anti-patterns

- **Atheoretical correlation** dressed as a hypothesis.
- **HARKing** — predictions reverse-engineered after seeing the regression.
- **Behavioral hand-waving** ("managers feel...") where an economic incentive argument is expected.
- **Normative claims** ("the standard should require...") instead of positive predictions.
- **No cross-sectional mechanism test**, leaving the main result observationally equivalent to alternatives.

## Output format

```
【Friction】information asymmetry / agency / contracting cost / political cost
【Actors & incentives】...
【Prediction (sign, a priori)】H1 ...
【Cross-sectional partition】effect stronger when friction X is severe
【Modeled or cited?】analytical model / economic theory cited
【Rival explanations to rule out】...
【Next step】jae-literature-positioning
```
