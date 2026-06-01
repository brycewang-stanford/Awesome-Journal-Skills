---
name: jie-workflow
description: Router for the Journal of International Economics (JIE) skill pack — given where a manuscript stands (idea, identification, data, framing, exhibits, polish, replication, review, submission, rebuttal), it names the next jie-* skill to use. Routes only; it does not produce manuscript content.
---

# Workflow Router (jie-workflow)

## When to trigger

- You are working on a JIE-targeted manuscript and are unsure which skill to use next
- You want the canonical order for the trade / international macro-finance pipeline
- You are mid-process (e.g., have data, no framing) and need the next step

## What JIE expects, end to end

JIE (Elsevier; Co-Editors-in-Chief Martin Uribe and Costas Arkolakis) is the leading field journal across **international trade and international macro/finance**. A submittable paper must (1) sit in scope, (2) be **original in its motivation or modelling structure**, (3) carry credible identification or a disciplined structural model, (4) report economic magnitudes, (5) deposit replication code and data in the JIE secure repository, and (6) be packaged for Editorial Manager (fee, 150-word abstract, 1-7 keywords, regular/short/PRP type, suggested editor). This router sequences the jie-* skills to get there.

## Default sequence

```text
jie-topic-selection            scope fit + originality gate
        ▼
jie-literature-positioning     stake the contribution vs the frontier
        ▼
jie-identification-strategy    gravity / policy-shock / open-economy design
        ▼
jie-data-analysis              PPML, panels, structural estimation, robustness
        ▼
jie-contribution-framing       originality of motivation or modelling
        ▼
jie-tables-figures             trade/macro exhibits
        ▼
jie-writing-style              abstract (≤150 words), balance, references
        ▼
jie-replication-and-data-policy   Mendeley Data deposit
        ▼
jie-review-process             handling, refereeing, PRP option
        ▼
jie-submission                 Editorial Manager preflight
        ▼
jie-rebuttal                   R&R response letter
```

## Routing logic

- No clear question / unsure it fits trade or macro-finance → **jie-topic-selection**
- Question set, contribution vague vs literature → **jie-literature-positioning**
- Causal/structural strategy is the bottleneck → **jie-identification-strategy**
- Estimation, gravity specification, or robustness work → **jie-data-analysis**
- Results exist, "so what / what's new" is unclear → **jie-contribution-framing**
- Tables/figures need building → **jie-tables-figures**
- Prose/abstract polish → **jie-writing-style**
- Heading to acceptance, need the data/code deposit → **jie-replication-and-data-policy**
- Want to understand handling / PRP before submitting → **jie-review-process**
- Final preflight → **jie-submission**
- Got an R&R → **jie-rebuttal**

## Output format

```
【Current stage】(one line)
【Use next】jie-<skill>
【Then】jie-<skill> → jie-<skill>
【Note】JIE-specific reminder (scope / originality / fee / deposit)
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data and tooling across the pipeline
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JIE / Elsevier sources
