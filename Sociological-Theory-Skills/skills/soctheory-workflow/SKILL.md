---
name: soctheory-workflow
description: Use when deciding which soctheory-* sub-skill to invoke next, or when sequencing a Sociological Theory manuscript from theoretical-problem framing through peer-review revision for a Sociological Theory (ST) submission. Routes — does not replace — the specialized skills.
---

# Sociological Theory Workflow (soctheory-workflow)

## Overview

This is the router. It does not replace any specialized skill — it tells you **which
soctheory-* skill to use at the current stage** of a *Sociological Theory* (ST) manuscript.

Default assumption: unless the user says otherwise, treat the target as **Sociological
Theory**, the **American Sociological Association's (ASA) dedicated theory journal**, published
by SAGE. ST publishes work "in all areas of theory, including new substantive theories,
history of theory, metatheory, formal theory construction, and synthetic contributions"
(submission guidelines, 检索于 2026-06；以官网为准). The deliverable is a **conceptual
advance** — a new concept, a sharpened mechanism, a typology, a reconstruction of a tradition,
or a metatheoretical clarification. There is **no hypothesis-testing, no estimation, and no
results section**: data, when present at all, is **illustrative**, never a test. If the project
hinges on identifying a causal effect in a dataset, it belongs at ST's empirical siblings
(American Sociological Review, American Journal of Sociology), not at ST.

Two reference points keep the bar in view at every stage. **Gabriel Abend's "The Meaning of
'Theory'"** (ST 2008, 26(2):173–199) shows that "theory" means several distinct things in
sociology — be explicit about which kind you are doing. **Isaac Reed's "Justifying
Sociological Knowledge"** (ST 2008, 26(2):101–129) shows that the warrant for a theoretical
claim is itself a theoretical commitment. References follow the **ASA Style Guide** (author-date).

## When to trigger

- The user asks "what should I do next?" on a theory paper
- A draft arrives and you must locate its bottleneck (problem? concept? argument? contribution?)
- Work is thrashing between theorizing, diagram-building, and prose
- An ST decision letter has arrived and the work shifts to revision

## Routing table

| Current symptom                                                       | Next skill                       |
|----------------------------------------------------------------------|----------------------------------|
| Idea is vague; not sure there is a real theoretical problem          | `soctheory-topic-selection`      |
| Have a problem but concepts/mechanisms/propositions are not built    | `soctheory-theory-construction`  |
| Unsure which tradition or conversation you are intervening in        | `soctheory-literature-positioning`|
| Propositions exist but the chain of reasoning is missing or shaky    | `soctheory-argument-development`  |
| Theory over-reaches; scope and domain are unstated                   | `soctheory-boundary-conditions`  |
| Need a typology / mechanism diagram / process figure (not a table)   | `soctheory-conceptual-exhibits`  |
| Prose reads like a literature review, not an argument                | `soctheory-writing-style`        |
| Cannot say what new way of seeing the theory provides                | `soctheory-contribution-framing` |
| Want to understand ST's double-anonymous, multi-round review         | `soctheory-review-process`       |
| Ready to submit; need the Manuscript Central preflight               | `soctheory-submission`           |
| Received an R&R; need to write the response document                 | `soctheory-rebuttal`             |

## Default order

1. `soctheory-topic-selection` — lock the theoretical problem (what existing theory cannot see)
2. `soctheory-literature-positioning` — name the tradition/conversation you intervene in
3. `soctheory-theory-construction` — build concepts, mechanisms, propositions
4. `soctheory-argument-development` — make the reasoning valid; engage rival theories
5. `soctheory-boundary-conditions` — state scope, domain, and what the theory does NOT claim
6. `soctheory-conceptual-exhibits` — typology / mechanism diagram / process figure
7. `soctheory-contribution-framing` — the new way of seeing; the "before → after"
8. `soctheory-writing-style` — ASA Style Guide; argument-driven prose (polish)
9. `soctheory-submission` — Manuscript Central preflight
10. `soctheory-review-process` — understand the review you are about to enter
11. `soctheory-rebuttal` — after the R&R

> `soctheory-writing-style` is a **late-stage polish**. Do not polish prose before the argument
> is valid (`soctheory-argument-development`) and the contribution is named
> (`soctheory-contribution-framing`).

## Session gate sheet

Open each ST work session by filling this sheet; the first blank or "no" is the route.
Gate 0 is ST-specific: a manuscript that cannot name its *kind* of theory will drift.

```text
SOCIOLOGICAL THEORY — SESSION GATE SHEET
Gate 0  Which sense of "theory" (Abend 2008) is this paper doing?  kind: ______________
Gate 1  What existing theory cannot see is stated ............. soctheory-topic-selection
Gate 2  Tradition / conversation intervened in is named ....... soctheory-literature-positioning
Gate 3  Concepts, mechanisms, propositions are built .......... soctheory-theory-construction
Gate 4  Chain of reasoning valid; rivals engaged .............. soctheory-argument-development
Gate 5  Scope + domain stated; over-reach trimmed ............. soctheory-boundary-conditions
Gate 6  Typology / mechanism / process figure drafted ......... soctheory-conceptual-exhibits
Gate 7  The new way of seeing is nameable (before -> after) ... soctheory-contribution-framing
Gate 8  Prose argues; ASA author-date style throughout ........ soctheory-writing-style
Gate 9  Manuscript Central preflight complete ................. soctheory-submission
Gate 10 Double-anonymous multi-round review understood ........ soctheory-review-process
Gate 11 R&R response revises the THEORY, then the letter ...... soctheory-rebuttal

Standing rule: Gates 6–8 wait on Gate 4; data mentioned anywhere stays illustrative, never a test.
```

## Decision shortcuts

- "I have an interesting phenomenon but no theory" → `soctheory-topic-selection`
- "I don't know whose tradition I'm arguing with" → `soctheory-literature-positioning`
- "My propositions read like assertions" → `soctheory-theory-construction` then `soctheory-argument-development`
- "A reviewer will say the theory claims too much" → `soctheory-boundary-conditions`
- "My figure is boxes and arrows with no mechanism" → `soctheory-conceptual-exhibits`
- "A reviewer will ask 'what's new here?'" → `soctheory-contribution-framing`
- "It reads like a review essay" → `soctheory-writing-style`
- "I'm about to hit submit" → `soctheory-submission`
- "I got a Major/Minor Revision" → `soctheory-review-process` then `soctheory-rebuttal`

## Differences vs. ASR / AJS empirical skill stacks

If the manuscript identifies an effect in data and the contribution is the *finding*, an
empirical-sociology stack (ASR / AJS) fits better. The core split:

- **Sociological Theory**: builds theory; the contribution IS the conceptual advance; data
  illustrative only; propositions, not hypotheses tested.
- **ASR / AJS**: test or demonstrate empirically; samples, measures, estimation, results.

ST is also **not** *Theory and Society*, the *European Journal of Social Theory*, or
*Sociological Methodology* — it is the ASA's flagship for theory proper (see
`soctheory-topic-selection` for the sibling-venue map).

## Anti-patterns

- **Do not** skip `soctheory-literature-positioning` and jump to building — reviewers first ask whose tradition you are in.
- **Do not** let `soctheory-conceptual-exhibits` pretty up a diagram before the mechanism exists.
- **Do not** let `soctheory-rebuttal` draft a response before the theory itself has been revised.
- **Do not** treat ST as a venue for an empirical test; route hypothesis-testing to ASR/AJS.

> Volatile specifics (exact fee, word limit, ASA Style edition, portal) change — see
> `resources/official-source-map.md` and confirm on the official ST / SAGE author page. The
> 2024–2026 co-editor team is identified in the source map (verified 2026-06-22), but editors
> rotate (next term begins 2027-01-01), so re-confirm the slate before naming editors.
