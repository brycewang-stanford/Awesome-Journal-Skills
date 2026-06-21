---
name: arpsych-workflow
description: Use when deciding which arpsych-* sub-skill to invoke next, or when sequencing an invited review article from topic through revision for an Annual Review of Psychology (ARPsych) manuscript. Routes — it does not replace — the specialized skills.
---

# ARPsych Workflow Router (arpsych-workflow)

## Overview

This is the router. It tells you **which arpsych-* skill to use at the current stage** of an **invited review article** aimed at the *Annual Review of Psychology* (ARPsych) — the **Annual Reviews** (nonprofit) survey series for psychology, founded **1950**, published as an **annual volume**, and edited by **Susan T. Fiske** (检索于 2026-06；editor since 2000；以官网为准). It is among the highest-impact journals in the field (检索于 2026-06；JIF ~29.4 in 2024, ranked #1 in Psychology；以官网为准). ARPsych does **not** publish original empirical studies. It publishes **authoritative, accessible review articles** that synthesize a topic — across cognitive, social, developmental, clinical, biological/neuro, I-O, and methods psychology — for the whole field and adjacent disciplines. So the lifecycle is not "design → run → analyze → defend"; it is **find a synthesis-worthy topic → get on the Editorial Committee's commission list → read the whole literature → impose an organizing framework → cover it even-handedly → land the ARPsych voice → handle production → revise.**

Default assumption: unless the user says otherwise, treat the target as ARPsych and the artefact as an **invited review**, not a primary-research paper. Operational tells that you are at ARPsych and not a sibling: the work **reviews other people's findings** rather than reporting its own studies; **unsolicited manuscripts are not accepted** — the **Editorial Committee plans each volume and invites authors** (you may suggest a topic, but you cannot self-submit a finished paper) (检索于 2026-06；以官网为准); there is **no study of your own to power or preregister** (you appraise the studies you cover); the contribution is an **analytical map of a literature**, not a new effect. If the user has original data, they want a primary outlet (a *Psychological Science*, a JPSP, a specialty journal) — say so. If they have a stand-alone meta-analysis or a self-submitted review, that is **Psychological Bulletin**, not ARPsych.

## When to trigger

- The user asks "what should I do next?" on an invited review
- A review draft reads like an annotated bibliography and needs a spine
- Work is ping-ponging between coverage, framing, balance, and the invitation
- An ARPsych production/peer-review letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the topic is mature/important enough to review for ARPsych | `arpsych-topic-selection` |
| Need to get a topic to the Editorial Committee / respond to an invitation | `arpsych-proposal-and-commissioning` |
| Reading is unsystematic; coverage gaps likely | `arpsych-literature-synthesis` |
| Draft is a list of studies, not an argument about the literature | `arpsych-organizing-framework` |
| Coverage feels lopsided, lab-centric, or self-promotional | `arpsych-comprehensiveness-and-balance` |
| Need a who-found-what table or a conceptual framework figure | `arpsych-tables-figures` |
| Prose is dense/jargon-laden; an adjacent psychologist can't follow | `arpsych-writing-style` |
| The review includes a meta-analysis or systematic search to document | `arpsych-transparency-and-reproducibility` |
| Working with the Editor / production editor on scope and timeline | `arpsych-editor-strategy` |
| Ready to deliver the commissioned draft; need a preflight | `arpsych-submission` |
| Received an editor/peer review on the delivered review | `arpsych-revision` |

## Default order

1. `arpsych-topic-selection` — confirm the topic is ARPsych-scale (mature, important, needs synthesis)
2. `arpsych-proposal-and-commissioning` — get the topic to the Committee / shape the accepted invitation
3. `arpsych-literature-synthesis` — gather and read the literature systematically
4. `arpsych-organizing-framework` — impose the analytical spine
5. `arpsych-comprehensiveness-and-balance` — even-handed coverage across labs and paradigms
6. `arpsych-tables-figures` — summary tables and the conceptual figure
7. `arpsych-writing-style` — the authoritative-yet-accessible ARPsych voice (abstract + intro last)
8. `arpsych-transparency-and-reproducibility` — document the search; make any meta-analysis reproducible
9. `arpsych-editor-strategy` — scope and the Editor/production relationship
10. `arpsych-submission` — Annual Reviews delivery preflight
11. `arpsych-revision` — after the editor/peer-review letter

> `arpsych-writing-style` is a late-stage polish; do not rewrite the intro before the framework and balance settle. The **invitation comes early** — ARPsych is commissioning-first, so `arpsych-proposal-and-commissioning` precedes the heavy reading and an agreed length lands before drafting.

## Anti-patterns

- Treating ARPsych as a journal you submit to cold — it is **invitation-driven; unsolicited manuscripts are not accepted** (检索于 2026-06；以官网为准)
- Treating the review as an annotated bibliography (no framework) — the cardinal review-article failure
- Centering the review on the author's own lab and citing oneself disproportionately (self-promotion)
- Importing primary-research instincts: there is no "preregistration" or "power analysis" of your own — you **appraise** others' designs
- Confusing ARPsych with **Psychological Bulletin** (submitted reviews/meta-analyses), **Annual Review of Clinical Psychology** (the clinical sister), or **Perspectives on Psychological Science** (shorter, opinionated essays)

## Routing by review archetype

A "review" is not one thing; the bottleneck differs by type. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| field-defining synthesis (broad subfield) | scope is enormous; needs a taxonomy | `arpsych-organizing-framework` |
| construct/theory review (one idea across paradigms) | accessibility + balance across rival accounts | `arpsych-comprehensiveness-and-balance` |
| quantitative stocktake (meta-analysis embedded) | reproducible search + effect synthesis | `arpsych-transparency-and-reproducibility` |
| emerging-area review (young, fast-moving) | is it mature enough for an ARPsych volume yet? | `arpsych-topic-selection` |

## Minimal decision snippet

```
if editor_or_review_letter:            -> arpsych-revision
elif ready_to_deliver_draft:           -> arpsych-submission
elif scope_or_timeline_with_editor:    -> arpsych-editor-strategy
elif meta_analysis_or_search_to_doc:   -> arpsych-transparency-and-reproducibility
elif prose_dense_or_inaccessible:      -> arpsych-writing-style
elif need_tables_or_figures:           -> arpsych-tables-figures
elif coverage_lopsided_or_selfpromo:   -> arpsych-comprehensiveness-and-balance
elif reads_like_a_list:                -> arpsych-organizing-framework
elif reading_unsystematic:             -> arpsych-literature-synthesis
elif no_invitation_yet:                -> arpsych-proposal-and-commissioning
else:                                  -> arpsych-topic-selection
```
