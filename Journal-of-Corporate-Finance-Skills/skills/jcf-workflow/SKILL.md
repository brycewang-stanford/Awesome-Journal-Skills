---
name: jcf-workflow
description: Use to orchestrate the full Journal of Corporate Finance (JCF) manuscript lifecycle — from a corporate-finance question through identification, robustness, the US$340 fee submission via Editorial Manager, single-anonymized review, and R&R. Routes to the other eleven jcf-* skills; it coordinates, it does not draft content.
---

# JCF Manuscript Workflow (jcf-workflow)

## When to trigger

- Starting a new empirical or theoretical corporate-finance paper aimed at JCF
- Deciding which jcf-* skill to invoke next at a given stage
- Sanity-checking that the project fits JCF's scope and process before investing

## What JCF is (verified; re-confirm on the official guide)

The **Journal of Corporate Finance** is an **Elsevier** journal publishing **original manuscripts or shorter format papers** in **empirical and theoretical corporate finance** — financial structure, governance, payout, financial contracting, risk management, innovation, M&A, and international corporate finance, including intersections with macro, asset pricing, household/behavioral finance, fintech/blockchain, law, financial intermediation, and market microstructure.

## Stage map (route to the named skill)

1. **Fit & question** → `jcf-topic-selection` (scope fit, "shorter format" option)
2. **Positioning** → `jcf-literature-positioning` (corporate-finance lineage)
3. **Design** → `jcf-identification-strategy` (causal credibility for firm data)
4. **Evidence** → `jcf-data-analysis` (WRDS-era panels, robustness)
5. **Exhibits** → `jcf-tables-figures` (self-contained tables, event-study plots)
6. **Pitch** → `jcf-contribution-framing` (what is new and why it matters)
7. **Prose** → `jcf-writing-style` (≤250-word abstract, author-date)
8. **Data** → `jcf-replication-and-data-policy` (Elsevier Option C)
9. **Process** → `jcf-review-process` (single-anonymized, two+ reviewers)
10. **Submit** → `jcf-submission` (Editorial Manager, US$340 fee preflight)
11. **Revise** → `jcf-rebuttal` (point-by-point R&R)

## Key process facts

- **US$340 non-refundable submission fee**, paid up front; not refunded on desk reject.
- **Active desk-rejection** policy — clear the editor screen first.
- **No fixed length ceiling** (待核实); shorter formats welcome.

## Anti-patterns

- Treating JCF like a double-blind journal (it is single-anonymized).
- Skipping identification because "it's a finance journal" — credibility still gates.
- Ignoring the up-front fee in planning.

## Output

```
【Stage】<current> → next skill: jcf-<role>
【Fit】scope/format OK? [Y/N]  【Blockers】<list>
```
