---
name: jbf-contribution-framing
description: Use when sharpening the contribution claim for a Journal of Banking & Finance paper so the manuscript explains why the result matters for banking, financial intermediation, markets, regulation, or corporate finance.
---

# Contribution Framing (jbf-contribution-framing)

## When to trigger

- The result is statistically solid but the paper does not say why JBF readers should care
- The introduction sounds like a data exercise rather than a finance contribution
- You need a concise editor-facing pitch or cover-letter paragraph

## Contribution formula

A strong JBF contribution connects four elements:

1. **Finance problem**: the unresolved question in banking, intermediation,
   markets, corporate finance, investments, or regulation.
2. **Friction or mechanism**: information, agency, liquidity, risk, capital,
   market power, regulation, search, or behavioral channel.
3. **Credible evidence or model**: the design that lets the paper isolate the
   mechanism.
4. **Implication**: how the result changes understanding of financial institutions,
   investors, firms, or policy.

## Contribution types

- **Mechanism contribution**: identifies how a finance friction operates.
- **Measurement contribution**: creates a better measure and proves it changes inference.
- **Policy contribution**: evaluates regulation or supervisory change with credible variation.
- **Institutional contribution**: reveals bank/intermediary behavior that theory had not pinned down.
- **Theory-to-evidence contribution**: connects a formal model to a newly tested implication.

## Editor-facing paragraph

```text
We study [finance question] using [setting/design]. The key challenge is
[identification or measurement problem]. We address it by [variation/data/model],
and find [headline result with magnitude]. The paper contributes to JBF by
showing [mechanism/implication] for [banking/intermediation/markets/regulation].
```

## Anti-patterns

- Claiming contribution only because the setting is new
- Listing three literatures but not saying what each learns
- Over-selling policy relevance when the design identifies only a local effect
- Burying the magnitude until late in the paper

## Subfield framing ladder

Match the pitch to the JBF subfield the referee will come from:

| Subfield | What counts as the marginal contribution | Framing trap |
| --- | --- | --- |
| Bank capital / liquidity regulation | Quantifying a Basel-style margin (CET1, LCR, NSFR) on lending or risk-taking with credible variation | Restating "capital affects lending" without a new margin or mechanism |
| Credit risk / default modeling | Out-of-sample gain over standard benchmarks plus an economic story for the gain | Pure horse-race accuracy with no intermediation insight |
| Bank performance / financial stability | A risk-taking or stability channel (Z-score, NPLs, tail risk) theory had not pinned down | Cross-country correlations sold as causal stability lessons |
| Market microstructure / liquidity | An institutional friction that changes measured liquidity or price discovery | Generic asset-pricing result with banks as labels |
| Fintech / sustainable finance | Evidence the new technology or ESG margin changes credit allocation or risk pricing | Novelty of the setting standing in for a finance mechanism |

## Worked framing pass (illustrative)

Hypothetical draft: staggered state adoption of digital collateral registries and small-business lending, with DealScan-style loan-level data.

- Raw pitch: "We use new registry data to study lending." That fails the stress test — it is data, not mechanism.
- Reframed: "Collateral frictions limit small-business credit; registry adoption cuts verification costs. Spreads on affected loans fall by an illustrative 18 basis points (about 7% of the sample-mean spread) and the collateralized share rises 5 percentage points, with no movement for large syndicated borrowers."
- The JBF hook: a collateral-information mechanism in intermediation, a magnitude in basis points, and a boundary condition (no effect where information frictions were already low).

## Referee pushback on contribution claims

- "This is a known result in a new country." → Name the institutional feature (deposit-insurance design, supervisory regime, creditor rights) that changes the prediction, or reroute.
- "The policy implication overreaches." → Bound it: identified for treated banks near the threshold, not for system-wide Basel calibration.
- "Why JBF rather than a policy outlet?" → Anchor in an intermediation friction and the literature delta, not the policy narrative alone.

## Calibration anchor

Accepted JBF empirical papers typically state the question, design, headline magnitude, and contribution within the first two pages, with one paragraph per literature delta (a stylized pattern, not a journal rule).

## JBF contribution stress test

Before submission, answer these in the introduction, not only in the cover letter:

- Which financial decision-maker learns from the result: banks, borrowers, investors, regulators,
  boards, managers, intermediaries, or markets?
- What friction or institutional feature makes the result non-obvious?
- Which magnitude changes interpretation, and in what units?
- What competing finance explanation has been ruled out or bounded?
- Where does the result travel, and where does it not?

If the answer is "we have better data," route back to `jbf-literature-positioning` and `jbf-data-analysis`.
Better data become a contribution only after they identify a finance mechanism or revise a known result.

## Output format

```text
[One-sentence contribution] ...
[Mechanism] ...
[Why JBF] ...
[Magnitude] ...
[Boundary conditions] ...
[Next step] jbf-writing-style
```
