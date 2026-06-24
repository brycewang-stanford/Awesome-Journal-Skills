---
name: aejpol-tables-figures
description: Use when building or revising exhibits for an AEJ: Economic Policy manuscript so they meet AEA house style and carry the policy message — no significance asterisks, a self-contained headline exhibit, and figures that show the policy effect with uncertainty. Designs exhibits; it does not run the estimation or write the surrounding prose.
---

# Tables & Figures — Exhibits that Carry the Policy Message (aejpol-tables-figures)

## When to trigger

- Tables are dense, over-decorated with significance stars, or hard to read
- The paper lacks one exhibit a reader could take away as the policy result
- Figures show coefficients but not the policy-relevant magnitude or its uncertainty
- You are preparing the final exhibit set for an AEA submission

## AEA / AEJ: Policy exhibit norms

- **Report standard errors (or confidence intervals), not significance asterisks/boldface.** Put SEs in parentheses below estimates; the reader judges significance from the SE/CI. This is the house convention to follow.
- **Self-contained.** Title and notes let an exhibit be read without the text: sample, units, estimator, clustering level, what is controlled, and what the number means in policy terms.
- **Self-contained, not anonymized.** Review is single-blind, so exhibits need not hide authorship; keep notes clean and neutral (avoid stray local file paths) for readability, not for blinding.
- **Figures** are the workhorse for policy communication: event-study plots with CIs, RDD plots with binned means and the fitted discontinuity, dose-response or cost-benefit curves with uncertainty bands. Vector output; ≥300 dpi raster only if unavoidable; readable greyscale.

### The headline exhibit (AEJ: Policy-specific)
Every AEJ: Policy paper should have **one exhibit a policymaker could screenshot**: the policy effect in interpretable units **with** its welfare/cost-benefit reading where possible. Examples (illustrative formats):
- An event-study figure of the outcome around the reform, with the long-run effect annotated in policy units.
- A cost-benefit / MVPF figure: net cost per unit of outcome across policy variants, with bands.
- An incidence figure: who gains and who pays, by income/region group.

### Table craft
- Three-line tables (`esttab`/`booktabs`), no vertical rules; align decimals; consistent digits.
- Lead column = the policy-relevant specification, not a kitchen-sink spec.
- Put the policy-relevant magnitude (elasticity, cost-per-X, MVPF) in the paper's units, not only a raw coefficient; add a row translating the coefficient into the policy number where natural.
- Sample size, mean of the dependent variable, and clustering level on every table.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id` — one variable definition, one set of numbers, body and appendix in sync.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering (from the result's diagnostics) and
  states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] No significance asterisks or boldface-for-significance anywhere; SEs/CIs shown
- [ ] One self-contained headline exhibit carrying the policy magnitude (and welfare reading if available)
- [ ] Every table notes: sample, units, estimator, controls, clustering level, N, dep-var mean
- [ ] Figures show effects with uncertainty bands (event study / RDD / dose-response)
- [ ] Policy-relevant magnitude in interpretable units, not only raw coefficients
- [ ] Vector figures, readable in greyscale, no chartjunk

## Anti-patterns

- Significance stars and bold "***" — disallowed by AEA house style here
- A coefficient table with no translation into the policy magnitude
- A 12-column kitchen-sink table where the policy spec is buried
- Figures with point estimates but no confidence bands
- Notes too thin to read the exhibit without the text
- An exhibit whose notes are too thin to read without the body text

## Exhibit-by-design-type quick guide

| Design | Workhorse figure | What the notes must state |
|---|---|---|
| DID / event study | Event-study coefficients with CI bands; flat pre-period leads visible | estimator (CS/SA), comparison group, clustering level |
| RDD | Binned means + fitted discontinuity + bandwidth | running variable, bandwidth, density-test result |
| Bunching | Empirical vs. counterfactual density at the kink | counterfactual construction, excluded region |
| RCT | Treatment-control means / dose-response with CIs | randomization unit, take-up, ITT vs. ToT |
| Welfare | MVPF / cost-per-outcome across variants, with bands | which estimates feed the ledger, assumptions |

## Worked vignette (illustrative)

A tax-credit paper's main table reports a coefficient of 0.08 (s.e. 0.02) on the credit. Reworked for AEJ: Policy: the lead exhibit becomes a figure of employment around the credit's introduction with a CI band, the long-run effect annotated as "+3.1 pp employment (90% CI [1.9, 4.3])," and a companion row translating it into **cost per additional job** with its band — the number a policymaker takes away. No asterisks; SEs in parentheses throughout.

## Output format

```
【Headline exhibit】figure/table + the policy magnitude it carries
【Significance reporting】SEs/CIs, no asterisks? [Y/N]
【Self-contained notes】sample/units/estimator/clustering/N/dep-mean present? [Y/N]
【Policy-units translation】coefficient → cost-per-X / MVPF / incidence shown? [Y/N]
【Next step】aejpol-writing-style
```
