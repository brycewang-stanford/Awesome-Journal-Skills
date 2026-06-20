---
name: finman-workflow
description: Use when deciding which finman-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Financial Management (FM) submission. Routes — it does not replace — the specialized skills.
---

# FM Workflow Router (finman-workflow)

## Overview

This is the router. It tells you **which finman-* skill to use at the current stage** of a manuscript aimed at *Financial Management* (FM) — the **flagship quarterly of the Financial Management Association International (FMA)**, published by **Wiley** (Online ISSN 1755-053X). FM is a **general-interest applied-finance journal**: corporate finance, investments, valuation, capital structure, payout, governance, banking, and financial markets are all in scope. Its editors describe the brand as "a finance journal that publishes academic articles that people actually read," and weigh submissions on **originality, rigor, timeliness, practical relevance, and quality** — with explicitly **less weight on trivial robustness tests** and real weight on the "so-what for managers and markets."

Default assumption: unless told otherwise, treat the target as FM. Operational tells that you are at FM and not a sibling or a generic top journal: submission begins on the **FMA portal and then hands off to ScholarOne**; there is a **per-manuscript submission fee** ($250 FMA member / $350 professional nonmember / $280 PhD nonmember, nonmember fee includes a one-year FMA membership — 检索于 2026-06；以官网为准); the editors advertise a **median 6–8 week turnaround including desk rejects**; and reviewers reward a sharp managerial implication over a wall of specification tables. Co-Editors as of 2026: **Michael Goldstein, Kathleen Kahle, and Shawn Thomas** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the FMA and Wiley pages.

## When to trigger

- The user asks "what should I do next?" on an FM-bound paper
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between framing, identification, evidence, exhibits, and the response letter
- An FM decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Topic feels niche, dated, or not clearly general-interest finance | `finman-topic-selection` |
| Contribution vs. the published finance frontier is fuzzy or oversold | `finman-literature-positioning` |
| The causal/structural credibility of the headline result is shaky | `finman-identification` |
| Sample construction, variable measurement, or panel design is fragile | `finman-empirical-design` |
| Results may be specification-, sample-, or inference-sensitive | `finman-robustness` |
| Exhibits are dense; the main estimate is hard to find | `finman-tables-figures` |
| Supporting analyses are sprawling and crowd the main paper | `finman-internet-appendix` |
| Prose buries the idea; abstract/intro/implications do not land | `finman-writing-style` |
| Anticipating likely referee objections before pressing submit | `finman-referee-strategy` |
| Ready to submit via FMA→ScholarOne; need a preflight | `finman-submission` |
| Received an R&R; need a response-letter strategy | `finman-rebuttal` |

## Default order

1. `finman-topic-selection` — lock a general-interest, topical finance question
2. `finman-literature-positioning` — stake the contribution vs. the published frontier
3. `finman-identification` — make the headline causal/economic claim credible
4. `finman-empirical-design` — sample, measurement, panel structure, inference
5. `finman-robustness` — defend the result without drowning it in trivial checks
6. `finman-tables-figures` — make the main estimate findable in seconds
7. `finman-internet-appendix` — house the supporting detail off the main stage
8. `finman-writing-style` — make the idea and its managerial payoff land (abstract + intro last)
9. `finman-referee-strategy` — pre-empt the objections FM referees actually raise
10. `finman-submission` — FMA→ScholarOne preflight (fee + membership + format)
11. `finman-rebuttal` — after the R&R

> `finman-writing-style` is a late-stage polish; do not rewrite the intro before identification and the evidence hierarchy settle.

## Routing by paper archetype

FM spans the breadth of applied finance, and the binding constraint differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Corporate-finance event/regulation study | DiD/event-study credibility around the shock | `finman-identification` |
| Cross-sectional asset-pricing / return predictability | factor controls, multiple-testing, transaction-cost realism | `finman-empirical-design` → `finman-robustness` |
| Governance / payout / capital-structure panel | endogeneity of the policy choice; economic-magnitude framing | `finman-identification` |
| Banking / market-microstructure | data provenance + measurement + clustered inference | `finman-empirical-design` |
| Descriptive "new fact" / practitioner-relevant measurement | why-it-matters framing + general-interest pitch | `finman-topic-selection` → `finman-writing-style` |

## Worked routing example (illustrative)

A user says: "My staggered-adoption governance result is fine, but a referee says it 'reads like a JCF replication' and the magnitudes feel small." That is two distinct FM pushbacks — *not differentiated from the corporate-finance specialist outlet* (owned by `finman-literature-positioning`) and *the economic-significance / managerial payoff is under-argued* (owned by `finman-writing-style`, with the estimate itself defended in `finman-identification`). Route to positioning first to sharpen why FM's broad audience should care, then to writing-style to make the magnitude speak to managers — not to a fourth robustness table, which FM explicitly under-weights.

## Sibling guard (where FM ends and its neighbors begin)

| Journal | What it is | When to route there instead of FM |
|---------|-----------|-----------------------------------|
| JF / JFE / RFS | the top-3, frontier-defining bar | a paradigm-shifting result with frontier identification |
| Journal of Corporate Finance | corporate-finance specialist | a CF-insider contribution with no broad general-interest hook |
| JFQA | quantitative/methods-forward finance | the contribution is the technique, not the economic finding |
| Journal of Banking & Finance | banking/intermediation specialist | a bank-only result that does not generalize |

FM sits between the top-3 and the specialists: **broad, novel, practitioner-aware, honestly sized.** If the paper is frontier-defining, aim higher; if it is subfield-only, aim specialist; FM is for the strong general-interest result in between.

## Anti-patterns

- Treating FM as interchangeable with the Journal of Corporate Finance, JFQA, or RFS — FM is the FMA's broad, practitioner-aware general-interest outlet
- Presenting a top-3 (JF/JFE/RFS) paper's identification bar as the FM exemplar
- Loading the paper with trivial robustness tables FM explicitly under-weights, while leaving the "so-what" thin
- Polishing prose before the contribution and evidence hierarchy are stable
- Quoting fees, editors, or limits as permanent when the source map marks them volatile

## Minimal decision snippet

```
if decision_letter_arrived:        -> finman-rebuttal
elif ready_to_submit:              -> finman-submission
elif anticipating_referees:        -> finman-referee-strategy
elif exhibits_hard_to_read:        -> finman-tables-figures
elif result_fragile:              -> finman-robustness
elif sample_or_measurement:        -> finman-empirical-design
elif causal_claim_shaky:           -> finman-identification
elif contribution_fuzzy:           -> finman-literature-positioning
else:                              -> finman-topic-selection
```
