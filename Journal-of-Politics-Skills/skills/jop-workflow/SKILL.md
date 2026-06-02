---
name: jop-workflow
description: Use as the entry point for any The Journal of Politics (JOP) manuscript. Routes to the right JOP sub-skill based on where you are in the lifecycle and whether a Research Article (<= 35 pages) or a Short Article (<= 10 pages) fits. JOP counts pages, not words, and makes acceptance contingent on replicability. It dispatches; it does not draft content.
---

# JOP Workflow Router (jop-workflow)

The orchestrator for a JOP submission. Figure out the stage and the **category**, then send the user
to the matching skill. JOP is a **general-interest** journal that counts **pages, not words**, and makes
**acceptance contingent on replicability** — so the router's first jobs are to fix the category against
the **page budget** and to start the replication package early.

## When to trigger

- Starting a new JOP paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding between a **Research Article** (≤ 35 pp) and a **Short Article** (≤ 10 pp)
- Returning with a decision letter (route to `jop-rebuttal`)

## First question: which category?

| Situation | Category | Route to |
|-----------|----------|----------|
| Full original study, broad interest | **Research Article** (≤ 35 pages) | normal pipeline below |
| Single sharp contribution, fits tight | **Short Article** (≤ 10 pages) | normal pipeline, tighter scope |
| Lots of robustness / derivations / SI | keep main text lean | `jop-tables-figures` + Online Appendix (≤ 25 pp) |
| Empirical/formal results to deposit | replication package | `jop-replication-and-data-policy` early |

> JOP caps **pages** (double-spaced, 12-pt), not words. A paper that clears an APSR/AJPS word cap can
> still blow the 35-page budget — decide the category before you write.

## Routing map (stage → skill)

```text
Idea / fit?                      → jop-topic-selection
Where does it sit in the field?  → jop-literature-positioning
What's the argument?             → jop-theory-building
Is the design defensible?        → jop-research-design
Are the analyses sound?          → jop-data-analysis
Are the exhibits clear + lean?   → jop-tables-figures
Does it fit 35 / 10 pages?       → jop-writing-style
Repro package for the analyst?   → jop-replication-and-data-policy
How will it be judged?           → jop-review-process
Ready to submit?                 → jop-submission
Got an R&R / decision?           → jop-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → replication-and-data-policy → review-process → submission → rebuttal`

Iterate: most papers loop theory ↔ design ↔ analysis several times, and trim against the **page budget**
before writing-style is done.

## Anti-patterns

- Planning by word count — JOP's binding constraint is **pages**
- Padding a Short Article toward 35 pages instead of keeping one crisp contribution
- Leaving the replication package until acceptance — a **JOP replication analyst** re-checks it
- Dumping the whole paper into the Online Appendix to dodge the 35-page main-text budget

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / replication / review / submit / rebut
【Category】Research Article (≤35 pp) / Short Article (≤10 pp)
【Route to】jop-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — political-science data + software by method, page-budget conventions
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JOP URLs behind every fact in this pack
