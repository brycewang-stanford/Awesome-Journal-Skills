---
name: jep-workflow
description: Use when deciding which jep-* sub-skill to invoke next, or when sequencing work on an accessible synthesis article from topic idea through editor revision for a Journal of Economic Perspectives (JEP) submission. Routes — it does not replace — the specialized skills.
---

# JEP Workflow Router (jep-workflow)

## Overview

This is the router. It tells you **which jep-* skill to use at the current stage** of an article aimed at the *Journal of Economic Perspectives* (JEP) — the **open-access, non-technical synthesis** journal of the **American Economic Association**, founded 1987. JEP is **not** a primary-research outlet. It rewards articles that **synthesize and communicate** a body of economics to a broad audience — readable by **90 percent or more of the AEA membership** — avoiding formal models and heavy econometrics in the body. The product is a **compelling, accessible, balanced essay**, not an identification strategy or a replication package.

Default assumption: unless the user says otherwise, treat the target as JEP. Operational tells that you are at JEP and not a research journal or its sibling *Journal of Economic Literature* (JEL): JEP is **largely invited / commissioned** and organized in **symposia**; almost all articles begin as a **2–5 page proposal** emailed to **jep@aeapubs.org** (about 10–15% of published articles originate as unsolicited proposals); the writing must be legible to non-specialists; there are recurring **features** ("Recommendations for Further Reading", retrospectives). Editor as of 2026: **Heidi Williams**; Managing Editor **Timothy Taylor** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the official AEA pages.

## When to trigger

- The user asks "what should I do next?" on a JEP article or proposal
- A draft reads like a research paper or a JEL survey, not a JEP essay
- Work is ping-ponging between idea, proposal, narrative, accessibility, and balance
- A JEP editor's letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Unsure the topic is broad/timely/synthesizable for non-specialists | `jep-topic-selection` |
| Need to pitch the article or a symposium to the editors | `jep-proposal-and-symposium` |
| Structure is a literature dump, not a story/argument | `jep-narrative-arc` |
| Prose is jargon-heavy; notation everywhere; reads like a working paper | `jep-accessibility-and-translation` |
| Evidence is presented with equations/regressions a general reader can't follow | `jep-evidence-without-equations` |
| Figures/tables are dense, not self-explanatory | `jep-exhibits-for-general-readers` |
| Voice is dry/hedged; abstract and opening don't land | `jep-writing-style` |
| Reads as advocacy; competing views or uncertainty underplayed | `jep-balance-and-objectivity` |
| Need to negotiate scope/length/symposium with the editorial team | `jep-editor-strategy` |
| Ready to email the proposal/manuscript; need a preflight | `jep-submission` |
| An editor asked for revisions (accessibility/balance/length/framing) | `jep-revision` |

## Default order

1. `jep-topic-selection` — confirm the topic is JEP-shaped (broad, timely, synthesizable)
2. `jep-proposal-and-symposium` — craft the 2–5 page proposal or symposium pitch
3. `jep-narrative-arc` — structure the essay as an argument, not a survey
4. `jep-accessibility-and-translation` — strip jargon/notation without dumbing down
5. `jep-evidence-without-equations` — present evidence credibly with minimal math
6. `jep-exhibits-for-general-readers` — build self-explanatory figures/tables
7. `jep-writing-style` — the JEP voice; abstract and opening last
8. `jep-balance-and-objectivity` — fair to competing views; honest about uncertainty
9. `jep-editor-strategy` — scope/length/symposium negotiation with the team
10. `jep-submission` — email-proposal preflight (accessibility bar, disclosure, JEL)
11. `jep-revision` — after the editor's letter

> `jep-writing-style` is a late polish; do not perfect sentences before the narrative arc and the balance settle.

## Anti-patterns

- Writing a **full unsolicited manuscript** before pitching a 2–5 page proposal (low odds; editors prefer proposals)
- Treating JEP like a research journal — leading with identification, a model, or a regression table
- Confusing JEP with **JEL**: JEL is the long, technical *survey of record*; JEP is the short, non-technical, broad-audience essay
- Letting `jep-exhibits-for-general-readers` polish a dense figure while the argument is still a literature dump
- Advocacy framing that an editor will read as an op-ed, not a balanced synthesis

## Routing by article archetype

JEP essays come in a few shapes, and the bottleneck differs. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| "State of a field" synthesis | scope too narrow or too technical | `jep-topic-selection` → `jep-narrative-arc` |
| Symposium contribution (invited) | fit with the symposium frame + length | `jep-editor-strategy` → `jep-narrative-arc` |
| Translating one's own technical agenda | jargon/notation; over-claiming | `jep-accessibility-and-translation` → `jep-balance-and-objectivity` |
| Policy-relevant debate | reads as advocacy; uncertainty buried | `jep-balance-and-objectivity` |

## Worked routing example (illustrative)

A user says: "I've drafted a 9,000-word piece summarizing my structural IO research for JEP, but a colleague says it reads like my JPE paper with the proofs deleted." That is two distinct JEP problems — *not yet translated for a general reader* and *no story for a non-specialist* — owned by `jep-accessibility-and-translation` and `jep-narrative-arc`. Route there first; only once a non-IO economist can follow the argument and one memorable through-line carries it do you return to `jep-writing-style` and `jep-exhibits-for-general-readers`. And before any of that, since this is an unsolicited full draft, `jep-proposal-and-symposium` would convert it into the 2–5 page proposal the editors actually want.

## Minimal decision snippet

```
if editor_letter_arrived:          -> jep-revision
elif ready_to_email:               -> jep-submission
elif reads_as_advocacy:            -> jep-balance-and-objectivity
elif exhibits_dense:               -> jep-exhibits-for-general-readers
elif math_or_jargon_heavy:         -> jep-evidence-without-equations / jep-accessibility-and-translation
elif structure_is_a_survey:        -> jep-narrative-arc
elif no_pitch_yet:                 -> jep-proposal-and-symposium
else:                              -> jep-topic-selection
```
