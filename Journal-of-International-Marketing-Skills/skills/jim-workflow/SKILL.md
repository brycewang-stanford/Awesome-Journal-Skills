---
name: jim-workflow
description: Use when starting or unblocking a Journal of International Marketing (JIM) manuscript and you need to pick the right jim-* sub-skill for the current stage, from first idea through the response letter. It routes to the specialist skills; it does not do their work.
---

# JIM Workflow Router (jim-workflow)

## Overview

Router skill for manuscripts aimed at the *Journal of International Marketing* (JIM) — the American Marketing Association's specialist top journal for **international marketing**, published quarterly by **SAGE** (ISSN 1069-031X print / 1547-7215 online; founded 1993 by S. Tamer Cavusgil). Editor-in-Chief: **Ayşegül Özsomer** (Koç University), in office since 2024 — re-check the masthead on ama.org before relying on it (checked 2026-07-16). Submission runs through **ScholarOne** (mc.manuscriptcentral.com/ama_jim), review is **double-anonymized**, the abstract cap is **200 words**, and the whole manuscript — title through print appendices — must fit **50 formatted pages**.

What makes JIM unlike its AMA siblings (JM, JMR, JPP&M) is a single gate every paper must clear: the **international dimension has to be the theoretical engine**, not the setting. Crossing a border must change the theory — through cultural, institutional, or economic variation across countries — and the empirics must earn cross-national comparison, usually via multi-country data with **measurement invariance** evidence. A solid domestic study relabeled "…in emerging markets" is the house desk-reject.

## When to trigger

- A user asks "where do I start?" or "what's next?" on a JIM-bound project
- A draft is stuck and nobody can name the binding constraint
- The team is debating JIM vs. JIBS, International Marketing Review, or Journal of Marketing
- A decision letter from JIM has arrived and revision work needs sequencing
- Someone proposes adding a second country "for the reviewers" — a routing question in disguise

## Routing table

| Symptom | Route to |
|---------|----------|
| Unclear whether the question is genuinely international | `jim-topic-selection` |
| Culture/institutions invoked but not theorized; mechanism vague | `jim-theory-development` |
| Cannot state what the paper adds to the international marketing conversation | `jim-literature-positioning` |
| Country sampling, translation, invariance plan, or design unsettled | `jim-methods` |
| MGCFA, multilevel models, or multi-country panels need running/reporting | `jim-data-analysis` |
| Contribution reads as "we replicated X abroad" | `jim-contribution-framing` |
| Exhibits sprawl past the 50-page cap or hide the cross-national result | `jim-tables-figures` |
| Prose is fine English but not JIM's voice; abstract over 200 words | `jim-writing-style` |
| Ready to build the ScholarOne package | `jim-submission` |
| Waiting on / anticipating the editorial process | `jim-review-process` |
| Revising against a JIM decision letter | `jim-rebuttal` |

## Default order

1. `jim-topic-selection` — verify the border-crossing is doing theoretical work
2. `jim-theory-development` — theorize the cross-national mechanism a priori
3. `jim-literature-positioning` — stake the claim in the international marketing canon
4. `jim-methods` — design the multi-country study: sampling, translation, invariance plan
5. `jim-data-analysis` — invariance tests, multilevel/SEM estimation, country effects
6. `jim-contribution-framing` — the theory payoff plus the cross-border managerial payoff
7. `jim-tables-figures` — invariance table, country descriptives, model figure, page budget
8. `jim-writing-style` — 200-word abstract and intro written last
9. `jim-submission` — ScholarOne two-file preflight
10. `jim-review-process` — calibrate expectations while under review
11. `jim-rebuttal` — after the decision letter

Loop back freely: a failed scalar-invariance test at step 5 often forces a return to step 4 (or even step 2, if only partial invariance survives and the theory leaned on mean comparisons).

## Entry point by archetype

| Archetype | First hard question | Enter at |
|-----------|--------------------|----------|
| Multi-country consumer survey | will the scales pass invariance across these countries? | `jim-methods` |
| Cross-cultural experiment | is culture manipulated/measured, or just implied by location? | `jim-theory-development` |
| Export / entry-mode secondary data | does the panel identify anything beyond correlations? | `jim-methods` |
| Global branding / GCC study | globalness theorized or asserted? | `jim-theory-development` |
| Meta-analysis of international effects | country-level moderators coded a priori? | `jim-literature-positioning` |
| Short Insight paper (<4,000 words) | is one sharp finding enough to stand alone? | `jim-contribution-framing` |

## Minimal decision snippet

```
if decision_letter:              -> jim-rebuttal
elif submitting_this_week:       -> jim-submission
elif exhibits_or_page_budget:    -> jim-tables-figures
elif estimation_or_invariance:   -> jim-data-analysis
elif design_or_sampling:         -> jim-methods
elif contribution_fuzzy:         -> jim-contribution-framing / jim-literature-positioning
elif mechanism_untheorized:      -> jim-theory-development
else:                            -> jim-topic-selection
```

## Anti-patterns

- Sending a single-country paper to JIM because the sample "happens to be foreign" — the classic desk reject
- Treating culture as a post-hoc explanation for a surprise result instead of a hypothesized construct
- Polishing prose or exhibits while the invariance evidence is still unsettled
- Confusing JIM with JIBS (general international business) or IMR — the boundary is a positioning task, not a coin flip
- Citing the editor, portal, or page limits from memory instead of re-checking ama.org / the SAGE author page

## Output format

```text
【Target】Journal of International Marketing (JIM)
【Archetype】multi-country survey / cross-cultural experiment / export panel / global branding / meta / Insight
【International engine】what the border-crossing does for the theory (one line)
【Bottleneck】topic / theory / positioning / design / analysis / framing / exhibits / style / submission / revision
【Next skill】<one jim-* skill>
【Fact status】volatile facts (editor, limits, portal) verified 2026-07-16 or flagged re-check
```
