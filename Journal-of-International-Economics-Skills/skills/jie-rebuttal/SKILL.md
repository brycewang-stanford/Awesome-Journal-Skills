---
name: jie-rebuttal
description: Use when drafting the response letter for a revise-and-resubmit at the Journal of International Economics (JIE) — answering international-trade or open-economy-macro referees on gravity/structural specification, identification, and model discipline, and keeping the revision within JIE's scope and originality bar. Structures the rebuttal; it does not invent results.
---

# R&R Rebuttal (jie-rebuttal)

## When to trigger

- You have an R&R decision from JIE and must write the response letter
- Referees split between a trade reviewer and an international-macro/finance reviewer
- A referee challenges your gravity specification, instrument, or structural model
- You need to revise without drifting outside JIE's scope or originality gate

## How JIE rebuttals work

JIE assigns referees from the relevant half of the field (international trade or international macro/finance), so a typical R&R has comments pulling in two methodological directions. Your letter must satisfy both while keeping the paper **original in its motivation or modelling structure** — the bar that got it past the desk. Address the handling **(Co-)Editor** first (Uribe, Arkolakis, or the editor assigned to your trade/macro topic), then each referee point by point.

## Structure

1. **Cover note to the editor**: one paragraph on the headline changes; reaffirm scope fit and what is now original/sharper.
2. **Per-referee, per-point**: quote the comment, state the change, point to the exact revised table/figure/section. Use a "Comment → Response → Where" pattern.
3. **Concessions and limits**: where a referee is right, fix it; where a request is out of scope or would dilute the contribution, decline politely with a reason.

## JIE-specific response tactics

- **Gravity / PPML challenges**: if asked about zeros, heteroskedasticity, or multilateral resistance, show the PPML (`ppmlhdfe` / `fepois`) results with importer×exporter×time fixed effects, not log-OLS patches.
- **Trade-policy identification**: defend pre-trends, staggered-adoption estimators for RTA/tariff timing, or shift-share share-exogeneity (Adao–Kolesar–Morales / Borusyak–Hull–Jaravel inference).
- **Open-economy-macro/structural challenges**: discipline the model against the targeted moments (spreads, cyclicality, pass-through), report sensitivity to calibration, and show counterfactuals are robust to alternative elasticities.
- **Exclusion / exogeneity**: argue in three registers — theory, institutional detail, falsification.
- **Replication**: confirm the revised code and data will be deposited in the JIE secure repository (Mendeley Data) on acceptance.

## Anti-patterns

- A defensive letter that argues rather than revises
- Satisfying the trade referee by breaking the macro referee's point (or vice versa)
- "We added a robustness check" with no table or location given
- Patching a gravity log-OLS objection instead of moving to PPML
- Expanding scope so far the paper loses the originality that earned the R&R

## Pushback-to-response patterns (JIE-specific)

The recurring R&R demands and the response that closes them. Use the Comment → Response → Where pattern for each.

- "Multilateral resistance not controlled / log-OLS gravity." Response: re-estimate in PPML with importer×time and exporter×time fixed effects, keep zeros, report the new elasticity; point to the revised gravity table.
- "RTA/tariff timing is endogenous." Response: add pair fixed effects, a pre-trend event study, and a placebo on untouched flows; point to the new event-study figure.
- "Structural model matches only targeted moments." Response: add an untargeted-moments panel and a counterfactual robustness sweep over the trade elasticity; point to the new moments table and appendix.
- "Pass-through estimate confounds the source of the exchange-rate move." Response: condition on currency of invoicing, switch to local projections with a clean horizon, and separate the disconnect channel; point to the revised impulse responses.

## Worked vignette (illustrative)

A pass-through paper gets an R&R: Referee 1 (macro) wants currency-of-invoicing controls; Referee 2 (trade) questions whether the import-price response is gravity-consistent. The letter opens to the handling editor with the headline change ("we now estimate horizon-by-horizon local projections with invoicing controls; the long-run pass-through estimate moves from, say, 0.6 to 0.5 — illustrative — and is now robust"). Then it answers Referee 1 point-by-point with the new controls and the revised figure location, and answers Referee 2 by showing the estimate is consistent with the structural elasticity in a short appendix — without conceding a control that would break the macro referee's identification. Concede where right, decline-with-reason where a request would dilute the originality that earned the R&R.

## Output format

```
【Decision】R&R (round __)
【Editor】handling (Co-)Editor + topic half (trade / macro-finance)
【Referee 1 points】[comment → response → where] x N
【Referee 2 points】[comment → response → where] x N
【Method fixes】PPML / staggered-DID / structural-discipline updates
【Declined (with reason)】[...]
【Replication】deposit confirmed for acceptance? [Y/N]
【Next step】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimators and structural tools to back each response
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — editor roster and data-policy sources
