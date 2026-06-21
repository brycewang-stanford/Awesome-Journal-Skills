---
name: conbio-workflow
description: Use as the entry point for any Conservation Biology manuscript. Routes to the right conbio sub-skill based on where you are in the science lifecycle and which article type (Contributed Paper, Research Note, Review, Essay, Conservation Practice and Policy, Comment) fits. It dispatches; it does not draft content.
---

# Conservation Biology Workflow Router (conbio-workflow)

The orchestrator for a *Conservation Biology* submission. Figure out the stage and the **article type**,
then send the user to the matching skill. *Conservation Biology* is the flagship journal of the
**Society for Conservation Biology** — the router's first job is to make sure the work has **direct,
transferable implications for the conservation of biological diversity**, not just a clean result.

## When to trigger

- Starting a new Conservation Biology paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits the work
- Returning with a decision letter (route to `conbio-revision-and-rebuttal`)

## First question: which article type?

| Situation | Article type | Route to |
|-----------|--------------|----------|
| Full empirical study, IMRAD, broad relevance | **Contributed Paper** (7,000 words in current Wiley listings) | normal pipeline below |
| Focused or preliminary result | **Research Note** | normal pipeline, tighter scope |
| Synthesis of a well-developed literature | **Review** | `conbio-literature-positioning` + `conbio-writing-style` |
| Forward-looking argument on a conservation issue | **Essay** | `conbio-conservation-relevance-and-implications` |
| Applied tools, policy, or management lessons | **Conservation Practice and Policy** | `conbio-study-design` + relevance |
| Response to a published paper | **Comment** | `conbio-literature-positioning` |

> Use the live Instructions for Authors page for upload-week per-type limits and article-type
> availability (see `resources/official-source-map.md`).

## Routing map (stage → skill)

```text
Idea / conservation fit?         → conbio-topic-selection
Where does it sit in the field?  → conbio-literature-positioning
Is the design sound?             → conbio-study-design
Are the analyses appropriate?    → conbio-data-analysis
Are the exhibits clear?          → conbio-figures-and-tables
Data + code archived?            → conbio-reporting-and-data-policy
Does it read accessibly?         → conbio-writing-style
Are the implications actionable? → conbio-conservation-relevance-and-implications
How will it be judged?           → conbio-review-process
Ready to submit?                 → conbio-submission
Got a decision / R&R?            → conbio-revision-and-rebuttal
```

## Default order

`topic-selection → literature-positioning → study-design → data-analysis → figures-and-tables →
reporting-and-data-policy → writing-style → conservation-relevance-and-implications → review-process →
submission → revision-and-rebuttal`

Iterate: most papers loop design ↔ analysis ↔ relevance several times before writing-style.

## Anti-patterns

- Treating a sound-but-inconsequential study as publishable — the journal demands conservation relevance
- Forcing every study into one statistical template (match design to the ecological question)
- Padding a Research Note into a Contributed Paper, or vice versa
- Leaving the data/code archive until acceptance instead of building it as you go


## Router pass for Conservation Biology

Treat this skill as an executable review pass, not a prose hint. First lock the species/system threat, conservation decision, and uncertainty relevant to action; then judge whether the current manuscript answers the venue's real reader: conservation-science reviewers who ask whether evidence changes biodiversity, management, or policy action.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Biological Conservation for applied conservation breadth, Global Change Biology for climate/ecosystem process, Ecology Letters for theory-forward ecology; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Submission-ready gate:** do not give final advice until the pack's
  `resources/official-source-map.md` has been checked for upload-week rules and the manuscript has one
  concrete fix for the largest venue-specific risk.

## Output format

```
【Stage】idea / positioning / design / analysis / exhibits / data-policy / writing / relevance / review / submit / revise
【Article type】Contributed Paper / Research Note / Review / Essay / Practice & Policy / Comment
【Route to】conbio-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — conservation data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Conservation Biology URLs behind every fact in this pack
