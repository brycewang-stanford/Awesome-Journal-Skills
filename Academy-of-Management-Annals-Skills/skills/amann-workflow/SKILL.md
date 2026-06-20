---
name: amann-workflow
description: Use when deciding which amann-* sub-skill to invoke next, or when sequencing a comprehensive review article from topic selection through revision for an Academy of Management Annals (Annals) submission. Routes — it does not replace — the specialized skills.
---

# Annals Workflow Router (amann-workflow)

## Overview

This is the router. It tells you **which amann-* skill to use at the current stage** of a **comprehensive, integrative review article** aimed at the *Academy of Management Annals* (Annals) — the Academy of Management's **review-of-the-field journal**, published with Taylor & Francis. Annals does **not** publish original empirical research or stand-alone new theory; it publishes **authoritative, theory-advancing reviews** that synthesize a management/organization literature. Its mission is "up-to-date, in-depth and integrative reviews of research advances in management," and its house identity is **"reviews with an attitude"**: a review must take a critical, integrative stance and set an agenda, not merely catalog papers (检索于 2026-06；以官网为准).

So the lifecycle is not "design → identify → estimate → defend." It is **judge whether a literature is Annals-scale → write the ≤5-page proposal (the gate) → if invited, read the whole literature → impose a novel organizing framework → appraise the evidence even-handedly → build synthesis exhibits → land the Annals voice → develop the full review through the editor-only process.** The single binding constraint at every step is the same: **does this review create a new way of seeing the field?** A review that summarizes accurately but reorganizes nothing is the canonical Annals reject.

Default assumption: unless told otherwise, treat the target as Annals and the artefact as a **comprehensive review**, not a primary paper. Tells that you are at Annals and not a sibling: the work **synthesizes other people's research** rather than reporting your own; the first deliverable is a **short proposal under a twice-yearly deadline**, not a full draft; there is **no hypothesis test or dataset of your own** — you appraise the studies you cover; the contribution is an **integrative map and agenda for a field**. If the user has original theory, route to **AMR**; original data, route to **AMJ** — say so.

## When to trigger

- The user asks "what should I do next?" on a review article
- A review draft reads like an annotated bibliography and needs an organizing spine
- Work is ping-ponging between coverage, framing, evidence appraisal, and the proposal
- An Annals proposal decision or a full-review referee letter arrived and the user must switch modes

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the literature is mature/important/fragmented enough for Annals | `amann-topic-selection` |
| Need to write the ≤5-page proposal that gates the whole process | `amann-proposal-framing` |
| Reading is unsystematic; coverage gaps a referee could name are likely | `amann-literature-synthesis` |
| Draft is a list of papers, not an argument about the field | `amann-organizing-framework` |
| Appraisal of cumulative evidence / balance across schools feels off | `amann-evidence-standards` |
| Need who-found-what tables or a framework diagram | `amann-tables-figures` |
| Prose is descriptive/jargon-laden; the "attitude" and agenda are missing | `amann-writing-style` |
| Negotiating scope with the editor or anticipating review-article referees | `amann-editor-strategy` |
| Ready to submit a proposal or invited full review via Manuscript Central | `amann-submission` |
| Need to understand the two-step proposal→invited-review choreography and timelines | `amann-review-process` |
| Received a proposal decision or full-review referee letter | `amann-revision` |

## Default order

1. `amann-topic-selection` — confirm the literature is Annals-scale (mature, important, fragmented, integrable)
2. `amann-proposal-framing` — write the ≤5-page, four-heading proposal (the gate)
3. `amann-literature-synthesis` — once invited, read the field systematically to saturation
4. `amann-organizing-framework` — impose the novel integrative spine (the acceptance bar)
5. `amann-evidence-standards` — appraise cumulative evidence and balance across schools
6. `amann-tables-figures` — synthesis tables and the signature framework figure
7. `amann-writing-style` — the authoritative, agenda-setting "attitude" voice (intro + abstract last)
8. `amann-editor-strategy` — scope negotiation and review-article referee expectations
9. `amann-submission` — Manuscript Central preflight (proposal or invited full review)
10. `amann-review-process` — the proposal→invited-review process and twice-yearly cadence
11. `amann-revision` — after the proposal decision or full-review letter

> `amann-writing-style` is a late polish; do not rewrite the intro before the framework and evidence appraisal settle. The **proposal comes early and is the gate** — at Annals you cannot submit a full review cold, so `amann-proposal-framing` precedes the heavy reading.

## Anti-patterns

- Submitting a full review cold — Annals is **proposal-first**; an uninvited full manuscript is out of process (检索于 2026-06；以官网为准)
- Treating the review as an annotated bibliography with no integrative framework — the named Annals reject
- Producing a descriptive map with no "attitude": no critique, no reconciliation, no agenda
- Centering the review on the author's own program (self-promotion; review-article referees punish this)
- Confusing Annals with **AMR** (original theory) or **AMJ** (empirical) — Annals is the review-of-the-field
- Missing the April 1 / October 1 proposal windows because the team treated intake as rolling

## Routing by review archetype

A "review" is not one thing; the bottleneck differs by type. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| field-defining integrative review (broad domain) | scope is enormous; needs a new organizing architecture | `amann-organizing-framework` |
| construct-clarification / reconciliation review | rival definitions and incommensurable measures; needs an integrating logic | `amann-organizing-framework` |
| cumulative-evidence stock-take (what do we know?) | even-handed appraisal of conflicting findings | `amann-evidence-standards` |
| emerging / fast-moving domain review | is it mature enough for Annals yet? | `amann-topic-selection` |
| systematic / bibliometric review | search transparency + turning the corpus into an argument | `amann-literature-synthesis` |

## Minimal decision snippet

```
if proposal_decision_or_referee_letter:  -> amann-revision
elif understanding_two_step_process:     -> amann-review-process
elif ready_to_submit:                    -> amann-submission
elif scope_or_referee_anticipation:      -> amann-editor-strategy
elif prose_descriptive_no_attitude:      -> amann-writing-style
elif need_tables_or_framework_figure:    -> amann-tables-figures
elif evidence_appraisal_or_balance_off:  -> amann-evidence-standards
elif reads_like_a_list:                  -> amann-organizing-framework
elif reading_unsystematic:               -> amann-literature-synthesis
elif no_proposal_yet:                     -> amann-proposal-framing
else:                                     -> amann-topic-selection
```
