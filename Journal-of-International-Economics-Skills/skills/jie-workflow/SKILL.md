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

JIE (Elsevier; Editors Martin Uribe and Costas Arkolakis) is the leading field journal across **international trade and international macro/finance**. A submittable paper must (1) sit in scope, (2) be **original in its motivation or modelling structure**, (3) carry credible identification or a disciplined structural model, (4) report economic magnitudes, (5) deposit replication code and data in the JIE secure repository, and (6) be packaged for Editorial Manager (fee, 150-word abstract, 1-7 keywords, regular/Short Paper/PRP type, suggested Editor or Co-Editor). This router sequences the jie-* skills to get there.

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


## Router pass for Journal of International Economics

Treat this skill as an executable review pass, not a prose hint. First lock the cross-border margin, model or identification source, and replication/data readiness; then judge whether the current manuscript answers the venue's real reader: international-economics reviewers who separate trade, open-economy macro, international finance, and sovereign-risk audiences.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JPubE for public-finance policy, JDE for development settings, JME for monetary macro emphasis; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Triage by symptom (where to jump in)

Most manuscripts do not start at step one. Match the loudest current problem to the skill, then return to the default sequence.

- "A referee will say my gravity is biased" → jie-identification-strategy (PPML / multilateral resistance), then jie-data-analysis.
- "The RTA/tariff timing is staggered and I used plain TWFE" → jie-identification-strategy (modern DID), then jie-data-analysis.
- "My structural counterfactual hinges on one elasticity" → jie-data-analysis (elasticity-sweep robustness), then jie-tables-figures (targeted vs untargeted moments).
- "Editors might call it incremental" → jie-contribution-framing (motivation vs modelling axis), backed by jie-literature-positioning.
- "Not sure it's trade or macro-finance" → jie-topic-selection (scope half), which also fixes editor suggestion.
- "Heading to acceptance" → jie-replication-and-data-policy (Mendeley Data deposit) before jie-submission.

## Cross-pack guardrail (the trade vs macro-finance split)

Every skill in this pack forces the same first decision: which half of JIE you are in. The split changes the currency of the contribution (a trade elasticity / welfare gain versus a pass-through / cyclicality / default moment), the referee pool, and the (Co-)Editor to suggest. Carry the answer through the whole pipeline; a paper framed in one half's currency but routed to the other reads as a weaker fit than it is.

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
