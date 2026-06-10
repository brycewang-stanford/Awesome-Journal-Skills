---
name: jbf-literature-positioning
description: Use when positioning a Journal of Banking & Finance manuscript against banking, intermediation, corporate finance, investments, regulation, and capital-market literatures so the contribution is precise rather than a generic finance literature review.
---

# Literature Positioning (jbf-literature-positioning)

## When to trigger

- The introduction lists papers but does not state the gap
- The paper risks being seen as "another setting" rather than a contribution
- You need to route citations across banking, finance, regulation, and adjacent economics literatures

## Positioning logic

JBF referees expect the paper to know the finance frontier. Positioning should
therefore compare the manuscript with the closest papers on question, mechanism,
data, and design, not with a broad topical survey.

1. **Identify the closest 5-8 papers** and state what each establishes.
2. **Separate literature families**: banking/intermediation, corporate finance,
   market microstructure/asset pricing, regulation, and method/design papers.
3. **State the delta**: new mechanism, better identification, new measurement,
   broader setting, sharper policy implication, or theory-to-evidence bridge.
4. **Explain why the delta matters for JBF readers**: bank behavior, credit
   allocation, market functioning, regulation, or investor outcomes.
5. **Avoid novelty by omission**: if a paper is close, cite it early and explain
   the difference directly.

## Standard contribution paragraph

```text
This paper contributes to [literature] by showing [finding/mechanism] in
[setting]. Relative to [closest paper], which [what it does], we [new data/design/
mechanism] and show [increment]. This matters because [banking/finance implication].
```

## Anti-patterns

- "To our knowledge" claims without naming the closest prior paper
- Putting all citations in one paragraph with no hierarchy
- Treating a proprietary dataset as the contribution by itself
- Ignoring identification papers that create the credibility bar

## Frontier map

Build a one-page map before rewriting the literature section:

```text
Paper | Finance question | Data/design | Mechanism | Your difference | Required citation location
```

Use the map to keep JBF positioning finance-first. A paper belongs near the introduction only if it
defines the closest banking, intermediation, corporate-finance, or market-functioning question. Purely
methodological references belong beside the identification or measurement choice, not in the contribution
paragraph.

If the manuscript relies on a proprietary dataset, the map must show why the data uncover a mechanism or
policy margin that public data cannot. Proprietary access is not a contribution unless it changes what can
be learned about finance.

## JBF strand map

Place the paper in one named strand before drafting the introduction; JBF referees are usually recruited from within the strand:

- Bank capital, liquidity, and credit supply (Basel margins, lending responses)
- Deposit franchise and funding fragility (insured vs uninsured funding, run risk)
- Relationship and small-business lending; loan contracting in syndicated markets
- Bank competition, governance, and risk-taking / financial stability
- Credit risk measurement and validation (PD/LGD models, distance-to-default)
- Fintech, digital banking, and sustainable finance as they touch intermediation

A manuscript spanning two strands should lead with the one whose referees can certify the contribution and treat the other as a secondary audience.

## Worked delta statement (illustrative)

Draft topic: climate-disclosure mandates and syndicated loan pricing.

- Closest strand: climate exposure and bank lending; suppose the nearest paper documents higher spreads for carbon-intensive borrowers.
- Stated delta: "Relative to that borrower-side evidence, we exploit lender-side disclosure mandates and show the price response comes from disclosing banks (illustrative +14 basis points on affected facilities) rather than borrower-risk repricing."
- The delta names the new variation (lender-side mandate), the mechanism (supervisory disclosure pressure), and the audience (banking-regulation readers), so the paragraph survives a strand-expert referee.

## Positioning pushbacks at JBF

- "The closest paper sits in an intermediation journal and is not cited." → search JFI/JFS-adjacent strands, not only top-3 finance outlets, before claiming a gap.
- "Your gap is a data gap." → restate the delta as mechanism or identification; data access alone reroutes to `jbf-data-analysis`.
- "The introduction reads as a survey." → cut to the 5-8 closest papers with explicit deltas; park the rest in a related-literature paragraph.

## Output format

```text
[Closest paper] citation + result
[Your delta] data / design / mechanism / scope / policy
[Literature buckets] ...
[Must-cite missing items] ...
[Positioning sentence] ...
[Next step] jbf-identification-strategy
```
