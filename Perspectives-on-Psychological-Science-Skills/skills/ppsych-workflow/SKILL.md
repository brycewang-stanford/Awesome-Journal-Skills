---
name: ppsych-workflow
description: Use when deciding which ppsych-* sub-skill to invoke next, or when sequencing a broad integrative review, theoretical statement, or meta-science piece from topic through revision for a Perspectives on Psychological Science (PoPS) manuscript. Routes by lifecycle stage and contribution type; it dispatches and does not draft content.
---

# PoPS Workflow Router (ppsych-workflow)

## Overview

This is the router. It tells you **which ppsych-* skill to use at the current stage** of a manuscript aimed at *Perspectives on Psychological Science* (PoPS) — the **SAGE** journal published in partnership with the **Association for Psychological Science (APS)**, a **bimonthly**, broad, integrative outlet (检索于 2026-06；以官网为准). PoPS does **not** publish single empirical studies (those go to *Psychological Science*) or routine meta-analyses (those go to specialized review journals). It publishes **broad integrative reviews, overviews of research programs, theoretical and conceptual statements, methodology and meta-science commentary, and big-picture "perspective" pieces** across all of psychology and adjacent behavioral, social, neuro, and methods fields (检索于 2026-06；以官网为准). The contribution is a **field-shaping synthesis or argument**, not a new dataset.

So the lifecycle is not "design → run → estimate → defend." It is: **find a synthesis- or argument-worthy question → decide whether a proposal is required → read across areas → impose an organizing framework → make the treatment comprehensive and balanced → model exemplary open science → manage the editor relationship → submit → revise.** Default assumption unless the user says otherwise: the target is PoPS and the artefact is a **broad integrative/theoretical/meta-science piece**, not a primary-research paper.

## When to trigger

- The user asks "what should I do next?" on a PoPS review, theoretical statement, or meta-science piece
- A draft reads like an annotated bibliography or a single-study report and needs a spine or a venue check
- Work is ping-ponging between coverage, framing, balance, open-science, and the proposal route
- A PoPS decision letter arrived and the user needs to switch into revision mode

## First question: contribution type

| Situation | Type | Route note |
|-----------|------|-----------|
| Broad cross-area synthesis / overview of a research program | **Stand-alone integrative review** | main pipeline; proposal optional |
| A unifying theoretical / conceptual / metatheoretical argument | **Theoretical statement** | `ppsych-organizing-framework` is the engine |
| Systematic evidence about the field's *practices* (replication, bias, methods) | **Meta-science / methodology** | `ppsych-transparency-and-reproducibility` early |
| Special issue, adversarial collaboration, multilab effort | **Cooperative contribution** | **proposal required** → `ppsych-proposal-and-commissioning` |
| Biography, book review, humor/opinion essay | **Miscellaneous** | **proposal required** → `ppsych-proposal-and-commissioning` |
| Single empirical study, or a routine meta-analysis | **Out of scope** | → *Psychological Science* / a specialized review journal |

> A positive editor reaction to a proposal is **not** an invitation; all manuscripts go through the same review (检索于 2026-06；以官网为准).

## Routing table (symptom → next skill)

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the question is PoPS-shaped (broad, integrative, not a single study) | `ppsych-topic-selection` |
| Need a proposal (cooperative/miscellaneous) or want to test a stand-alone idea | `ppsych-proposal-and-commissioning` |
| Reading is unsystematic; cross-area coverage gaps likely | `ppsych-literature-synthesis` |
| Draft is a list of papers, not an argument about the field | `ppsych-organizing-framework` |
| Coverage, balance, or fairness across areas/camps in doubt | `ppsych-comprehensiveness-and-balance` |
| Need a framework figure or who-found-what / practice-prevalence table | `ppsych-tables-figures` |
| Prose dense or insular; a psychologist from another area can't follow | `ppsych-writing-style` |
| Open data/materials/code, preregistration of a meta-science protocol | `ppsych-transparency-and-reproducibility` |
| Working with the editor on scope / what referees will weigh | `ppsych-editor-strategy` |
| Ready to submit; need a preflight and reviewer suggestions | `ppsych-submission` |
| Received a PoPS decision letter | `ppsych-revision` |

## Default order

1. `ppsych-topic-selection` — confirm the question is broad, integrative, PoPS-scale
2. `ppsych-proposal-and-commissioning` — proposal route (required for cooperative/miscellaneous)
3. `ppsych-literature-synthesis` — read across areas systematically
4. `ppsych-organizing-framework` — impose the analytical/conceptual spine
5. `ppsych-comprehensiveness-and-balance` — fair, field-spanning, reform-minded but evidence-based
6. `ppsych-tables-figures` — framework figure + summary/prevalence exhibits
7. `ppsych-writing-style` — the PoPS voice (broad, provocative, accessible); abstract ≤ 200 words last
8. `ppsych-transparency-and-reproducibility` — exemplary open science (PoPS is a leader)
9. `ppsych-editor-strategy` — scope and the editor relationship
10. `ppsych-submission` — ScholarOne preflight + suggested reviewers
11. `ppsych-revision` — after the decision letter

> `ppsych-writing-style` is a late polish — do not rewrite the intro before the framework and balance settle. For **meta-science**, pull `ppsych-transparency-and-reproducibility` forward: the systematic protocol is part of the design, not an afterthought.

## Anti-patterns

- Treating PoPS like *Psychological Science*: it does **not** take single empirical studies or routine meta-analyses (检索于 2026-06；以官网为准)
- Submitting a cooperative or miscellaneous piece with **no proposal**, or reading a proposal's positive feedback as an acceptance
- The annotated-bibliography failure: a "review" with no organizing argument
- Letting the author's own program become the review's center of gravity (self-promotion)
- Confusing PoPS with **Psychological Bulletin** (formal meta-analyses), **Annual Review of Psychology** (invited subfield surveys), or **Current Directions** (short, non-technical) — PoPS is the APS broad integrative + meta-science flagship

## Routing by archetype

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| field-defining integrative review | scope is enormous; needs a taxonomy | `ppsych-organizing-framework` |
| unifying theoretical statement | the argument itself, not coverage | `ppsych-organizing-framework` |
| meta-science / reform piece | systematic evidence + open protocol | `ppsych-transparency-and-reproducibility` |
| big-picture opinion / perspective | is it broad and defensible enough for PoPS? | `ppsych-topic-selection` |

## Minimal decision snippet

```
if decision_letter:                  -> ppsych-revision
elif ready_to_submit:                -> ppsych-submission
elif open_science_or_metascience:    -> ppsych-transparency-and-reproducibility
elif prose_dense_or_insular:         -> ppsych-writing-style
elif need_tables_or_figures:         -> ppsych-tables-figures
elif coverage_or_balance_in_doubt:   -> ppsych-comprehensiveness-and-balance
elif reads_like_a_list:              -> ppsych-organizing-framework
elif reading_unsystematic:           -> ppsych-literature-synthesis
elif needs_proposal_or_idea_test:    -> ppsych-proposal-and-commissioning
else:                                -> ppsych-topic-selection
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — search, preregistration, repositories, synthesis tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official PoPS URLs behind every fact in this pack
