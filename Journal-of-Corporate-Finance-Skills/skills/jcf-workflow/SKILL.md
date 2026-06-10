---
name: jcf-workflow
description: Use when orchestrating the full Journal of Corporate Finance (JCF) manuscript lifecycle — from a corporate-finance question through identification, robustness, the US$340 fee submission via Editorial Manager, single-anonymized review, and R&R. Routes to the other eleven jcf-* skills with stage gates; it coordinates, it does not draft content.
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

## Stop-and-repair gates

Pause the route before submission if any of these are true:

- the paper cannot name the corporate-finance decision or friction affected by the result;
- the design depends on firm panels but sample construction, links, or event dates are not reproducible;
- robustness tables exist but economic magnitudes are absent;
- the contribution is "new data" without a mechanism, policy implication, or theory revision;
- the manuscript treats the fee/process checklist as ready while identification or data availability is still
  unresolved.

The fastest route through JCF is not more tables; it is a coherent chain from corporate-finance question to
credible design, magnitude, and reproducible evidence.

## Stage gates and deliverables

Each stage exits with an artifact; missing artifacts predict where JCF projects stall:

```text
Stage       | Exit artifact                                 | Stalls when…
Fit         | Viability-matrix row + format call            | The topic is data-first, question-second
Positioning | Closest-paper contrasts (2–3)                 | A gap is claimed without a recent-paper sweep
Design      | One-paragraph variation defense + diagnostics | The shock grades low; the selection story is unwritten
Evidence    | Audit ledger + magnitudes per main claim      | Robustness grows while magnitudes stay absent
Exhibits    | Self-contained main tables + an ID figure     | FE/clustering undisclosed; no event-study bands
Pitch/Prose | ≤250-word abstract carrying a number          | The abstract restates regressions
Data        | Option C statement + run_all archive          | The archive is deferred to acceptance
Submit      | EM package + US$340 budgeted                  | Metadata or PDF mismatches surface at upload
Revise      | Conflict table + per-comment change map       | The letter argues instead of changing the paper
```

## Worked routing: a payout project through the pipeline

Hypothetical, dates illustrative: a team spots a dividend-tax reform. Weeks 1–2, `jcf-topic-selection` grades the shock and calls shorter format. Weeks 3–4, `jcf-literature-positioning` finds the closest two papers and the composition-versus-level gap. Weeks 5–8, `jcf-identification-strategy` and `jcf-data-analysis` run in tandem: treated/exempt definitions, firm and year FE, firm clustering, pre-trend leads, an illustrative headline of a 0.6-point repurchase rise. Weeks 9–10, `jcf-tables-figures` and `jcf-contribution-framing` build five exhibits and the one-sentence claim. Week 11, `jcf-writing-style` trims the abstract to 198 words while `jcf-replication-and-data-policy` finalizes the Option C statement and archive. Week 12, `jcf-submission` runs the EM preflight. The discipline is the order: no exhibit work before the design survives shock grading, and no submission while any stop-and-repair gate stays open.

## Output

```
【Stage】<current> → next skill: jcf-<role>
【Fit】scope/format OK? [Y/N]  【Blockers】<list>
```
