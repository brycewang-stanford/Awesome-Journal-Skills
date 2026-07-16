---
name: jppm-workflow
description: Use when deciding which jppm-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Public Policy & Marketing (JPP&M) submission. Routes to the specialized skills — it does not do their work.
---

# JPP&M Workflow Router (jppm-workflow)

## Overview

This router directs work on a manuscript aimed at the *Journal of Public Policy & Marketing* (JPP&M) — the American Marketing Association journal, published by SAGE, that lives at the intersection of **marketing, public policy, and consumer/societal welfare**. Since April 1, 2026, new submissions are handled by joint Editors in Chief **Melissa Bublitz and Stacey Finkelstein**, who succeeded Jeremy Kees and Beth Vallen (checked 2026-07-16 on ama.org; re-check the masthead before submitting). The journal's home turf: consumer protection and deception, warning and disclosure design, public-health marketing (tobacco, alcohol, food and nutrition labeling), privacy and data policy, sustainability, financial well-being, vulnerable consumers, and equity in marketplaces.

What makes JPP&M unlike any other marketing outlet is a **hard policy-relevance bar**. Every submission must include a **Policy Contribution Statement** (max 300 words, first page of the main document, excluded from the page cap) that names the policy conversation the paper joins, the advance over existing marketing-and-policy literature, and the specific stakeholders — FTC, FDA, CFPB, state regulators, NGOs, or marketers navigating regulation — who could act on the findings. A technically excellent consumer study with a policy paragraph stapled to the discussion is the journal's signature desk reject. Review is **double-anonymized**; manuscripts run at most **50 double-spaced pages inclusive of everything** at every stage; submission goes through SageTrack at mc.manuscriptcentral.com/ama_jppm.

## When to trigger

- "What should I do next?" on a marketing-and-policy manuscript
- The paper has strong evidence but nobody can say which regulator would care
- Work is bouncing among framing, evaluation design, and the implications section
- A JPP&M decision letter arrived and you need to enter revision mode at the right link
- The team is torn between JPP&M and JM, JCR/JCP, Journal of Consumer Affairs, or a policy-school journal

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unclear whether the question is policy-first or just consumer research in a policy costume | `jppm-topic-selection` |
| No account of *why* the policy lever should change marketplace behavior | `jppm-theory-development` |
| Paper ignores the JPP&M canon or the regulatory record; gap statement is soft | `jppm-literature-positioning` |
| Choosing between an experiment, a quasi-experiment around a policy rollout, a survey, or a meta-analysis | `jppm-methods` |
| DiD/RDD estimates, treatment effects, or subgroup analyses need to be defensible | `jppm-data-analysis` |
| The Policy Contribution Statement is vague, or implications are not actionable | `jppm-contribution-framing` |
| Exhibits speak only to academics, not to a policy reader | `jppm-tables-figures` |
| Prose is jargon-heavy, advocacy-tinged, or the intro buries the policy problem | `jppm-writing-style` |
| Ready for SageTrack; need the anonymization, page-count, and statement preflight | `jppm-submission` |
| Need to understand the editor/AE pipeline, desk-reject odds, R&R norms | `jppm-review-process` |
| Drafting the response letter and revision plan for an R&R | `jppm-rebuttal` |

## Default order

`jppm-workflow → jppm-topic-selection → jppm-theory-development → jppm-literature-positioning → jppm-methods → jppm-data-analysis → jppm-contribution-framing → jppm-tables-figures → jppm-writing-style → jppm-submission → jppm-review-process → jppm-rebuttal`

> The Policy Contribution Statement is written twice: a draft at `jppm-topic-selection` (to test whether the paper deserves to exist) and a final version at `jppm-contribution-framing` (once the estimates are in). Do not polish prose before the counterfactual holds up.

## Routing by paper archetype

| Archetype | Binding constraint | Enter at |
|-----------|--------------------|----------|
| Policy evaluation (a law/rule changed; did behavior?) | counterfactual credibility (DiD/RDD design) | `jppm-methods` |
| Consumer-protection experiment (warning, disclosure, label) | realistic stimuli + regulator-usable treatment contrasts | `jppm-methods` |
| Vulnerable-population field study | ethics, access, and welfare framing | `jppm-topic-selection` → `jppm-theory-development` |
| Privacy / data-policy study | mapping findings to a live rulemaking debate | `jppm-literature-positioning` |
| Conceptual / review piece for policymakers | synthesis that yields decisions, not a tour | `jppm-contribution-framing` |

## Worked routing example (illustrative)

A user says: "We ran three studies showing calorie counts on menus reduce ordering; a friendly reviewer said 'nice JCP paper — why is this JPP&M?'" That is the classic boundary failure. Route to `jppm-topic-selection` to re-anchor the question in the live disclosure-regulation debate (what the FDA menu-labeling rule already requires, what remains contested), then `jppm-contribution-framing` to rewrite the Policy Contribution Statement around a decision a named stakeholder faces — e.g., whether to extend the rule to delivery platforms — and only then reconsider whether an extra study on the contested margin is needed (`jppm-methods`).

## Anti-patterns

- Treating JPP&M as "JCP plus a policy paragraph" — the mechanism is welcome, but the policy question must drive
- Routing straight to `jppm-writing-style` when the real problem is a missing counterfactual
- Advocating a regulation the data do not test — evidence-free advocacy is a desk reject here
- Writing implications no actual regulator has the authority or instrument to act on
- Quoting the editor team or portal from memory instead of re-checking ama.org / SAGE before submission

## Output format

```text
【Target】Journal of Public Policy & Marketing
【Archetype】policy-evaluation / protection-experiment / vulnerable-population / privacy-data / conceptual-review
【Current bottleneck】fit / theory-of-the-lever / positioning / design / estimates / policy-framing / exhibits / style / submission / revision
【Next skill】<one jppm-* skill>
【Reason】why this is the binding constraint now
【Source check】official facts verified (2026-07-16) or flagged "re-check on the official site"
```
