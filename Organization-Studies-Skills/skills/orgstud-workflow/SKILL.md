---
name: orgstud-workflow
description: Use when deciding which orgstud-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for an Organization Studies (OS) submission. Routes — it does not replace — the specialized skills.
---

# Organization Studies Workflow Router (orgstud-workflow)

## Overview

This is the router. It tells you **which orgstud-* skill to use at the current stage** of a manuscript aimed at *Organization Studies* (OS) — the flagship **European** organization-theory journal published by **SAGE for the European Group for Organizational Studies (EGOS)**, founded 1980. OS rewards papers that make a **genuine theoretical contribution to organization studies** — institutional theory, process and practice theory, sensemaking, power and critique, sociological and historical approaches to organizing. It is distinctively strong on **qualitative, processual, and theoretically ambitious** work and prizes conceptual depth over hypothesis-counting.

Operational tells that you are at OS and not a sibling: review is **double-anonymized** (a separate, identity-bearing title page; the manuscript itself anonymized); the cap is **13,000 words including references and appendices**; the abstract is **unstructured, ≤300 words**; you supply **5–7 keywords, four drawn from the OS ScholarOne keyword list**; submission is via **ScholarOne** (`mc.manuscriptcentral.com/orgstudies`). The journal sits on the **FT50** generalist-management list. Editors-in-chief are **Renate Meyer and Paolo Quattrone** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the SAGE OS and EGOS pages.

## When to trigger

- The user asks "what should I do next?" on an OS-bound manuscript
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between framing, fieldwork/analysis, exhibits, and the response letter
- An OS decision letter arrived and the user needs to switch into revision mode
- The team is weighing OS against ASQ, Organization Science, JMS, or AMR

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Phenomenon is interesting but its fit with OS's theory-first scope is unclear | `orgstud-topic-selection` |
| The theoretical engine (mechanism / process model) is thin or relabels the finding | `orgstud-theory-development` |
| Contribution vs. the conversation OS owns is fuzzy or undersold | `orgstud-literature-positioning` |
| Design and its match to the question (qualitative/process/quantitative) need work | `orgstud-methods` |
| Coding, the data structure, or estimation/robustness need execution | `orgstud-data-analysis` |
| The one-sentence theoretical contribution is not sharp | `orgstud-contribution-framing` |
| Data structures, process figures, or tables are hard to read | `orgstud-tables-figures` |
| Prose buries the argument; the European theoretical register is missing | `orgstud-writing-style` |
| Ready to submit via ScholarOne; need a preflight on anonymization/format | `orgstud-submission` |
| Want to understand the developmental review cycle / decision odds | `orgstud-review-process` |
| Received an R&R; need a response-letter strategy | `orgstud-rebuttal` |

## Default order

1. `orgstud-topic-selection` — lock the theoretically generative phenomenon
2. `orgstud-theory-development` — build the mechanism / process model
3. `orgstud-literature-positioning` — stake the contribution in OS's conversation
4. `orgstud-methods` — design (qualitative/process/historical/quantitative) that fits the question
5. `orgstud-data-analysis` — make the data-to-theory ladder visible
6. `orgstud-contribution-framing` — sharpen the one-sentence theoretical claim
7. `orgstud-tables-figures` — data structures, process models, exhibits
8. `orgstud-writing-style` — the discursive European register (abstract + intro last)
9. `orgstud-submission` — ScholarOne preflight (anonymization, word cap, keywords)
10. `orgstud-review-process` — calibrate the developmental cycle
11. `orgstud-rebuttal` — after the R&R

> `orgstud-writing-style` is late-stage polish; do not rewrite the intro before theory and evidence settle. Unlike a variance-template journal, at OS the *theory* is the deliverable, so `orgstud-theory-development` and `orgstud-contribution-framing` are the load-bearing steps, not the methods or tables.

## Routing by paper archetype

OS spans several theory-driven archetypes, and the binding constraint differs by archetype. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| inductive/process ethnography | data-to-theory transparency + process model | `orgstud-theory-development` → `orgstud-data-analysis` |
| institutional / field-level study | what is novel for neo-institutional theory | `orgstud-literature-positioning` |
| critical / power / reflexive | the critical theoretical contribution, not just critique | `orgstud-theory-development` |
| conceptual / essay (no new data) | a clearly novel theoretical move readers can use | `orgstud-contribution-framing` |
| quantitative organization theory | mechanism the design illuminates (not the estimator) | `orgstud-theory-development` → `orgstud-methods` |

## Worked routing example (illustrative)

A user says: "My ethnography of a merger is rich, but a reviewer says it 'reads like a case report' and 'doesn't move institutional theory.'" That is two OS pushbacks — *the data-to-theory ladder is invisible* (owned by `orgstud-data-analysis`) and *the contribution to the institutional conversation is unstated* (owned by `orgstud-contribution-framing` with positioning in `orgstud-literature-positioning`). Build the Gioia-style data structure and a process model first, then name the theoretical move; only then return to `orgstud-writing-style`.

## Anti-patterns

- Treating OS as interchangeable with **ASQ** (US sociology-of-organizations), **Organization Science** (US, multi-paradigm + modeling), **JMS** (pluralist), or **AMR** (theory-only, no data)
- Leading with a clean identification design as if the estimator were the contribution — at OS the *theory* is the contribution
- Polishing prose before the mechanism and evidence hierarchy are stable
- Importing a top-five-economics or US hypothesis-template structure into a European theory-first outlet
- Asserting facts (editor, word cap, fees) not in `resources/official-source-map.md` or not marked 检索于 2026-06

## Output format

```text
【Target】Organization Studies (SAGE / EGOS)
【Current bottleneck】fit / theory / positioning / design / evidence / framing / exhibits / style / submission / revision
【Archetype】inductive-process / institutional / critical / conceptual / quantitative
【Next skill】<one orgstud-* skill>
【Reason】why this is the binding constraint
【Source check】official facts verified or marked 检索于 2026-06；以官网为准 / 待核实
```
