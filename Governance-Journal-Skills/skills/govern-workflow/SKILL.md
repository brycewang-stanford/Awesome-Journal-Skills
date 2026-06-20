---
name: govern-workflow
description: Use when starting or navigating any Governance: An International Journal of Policy, Administration, and Institutions manuscript and you need the entry point that routes to the right govern- sub-skill based on lifecycle stage and the comparative/institutional fit of the paper. It dispatches; it does not draft content.
---

# Governance Workflow Router (govern-workflow)

The orchestrator for a *Governance* submission. *Governance* (Wiley-Blackwell, founded 1988, published
in association with IPSA Research Committee 27 — Structure & Organization of Government) is the leading
journal of **executive politics, public policy, public administration, and the organization of the
state**, read comparatively and internationally. The router's first job is to confirm the paper makes a
**comparative/institutional contribution to how we understand governing** — then send the user to the
matching skill. It dispatches; it does not write content.

## When to trigger

- Starting a new *Governance* paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Unsure whether the paper is in scope (executive politics / policy / PA / the state) vs. off-fit
- Returning with a decision letter (route to `govern-rebuttal`)

## Routing map (stage / symptom → skill)

```text
Is this a Governance question? fit?     → govern-topic-selection
Where does it sit in the field?         → govern-literature-positioning
What is the argument / contribution?    → govern-theory-building
Is the design defensible?               → govern-research-design
Are the analyses sound?                 → govern-data-analysis
Are the exhibits clear?                 → govern-tables-figures
Does it read for the SOG community?     → govern-writing-style
Data Availability Statement & materials?→ govern-transparency-and-data
How will it be judged (double-blind)?   → govern-review-process
Ready to submit (Wiley portal)?         → govern-submission
Got an R&R / decision letter?           → govern-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most *Governance* papers loop theory ↔ design ↔ analysis several times before writing-style,
and a comparative paper often revisits case/country scope after positioning.

## Governance fit check (run before routing)

Force a one-minute fit check; route to the repair skill if any check is weak.

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Comparative / institutional significance | The claim travels across countries or policy domains and speaks to how the state governs — not one agency in one country described once. | `govern-topic-selection` |
| In scope, not off-fit | It is executive politics / public policy / PA / organization of the state. It is **not corporate governance**, and **not a literature review or pure bibliometric study** (both out of scope). | `govern-topic-selection` |
| Method pluralism | Any rigorous approach is welcome — quantitative, qualitative, comparative-historical, mixed — and is defended on its own terms, not forced into a regression template. | `govern-research-design` |
| Transparency plan | A **Data Availability Statement** is planned (mandatory at submission); replication data/code location is identified where applicable. | `govern-transparency-and-data` |

If the paper fails the comparative/institutional check, do not route to writing-style. It needs a
theory or fit repair — *Governance* reviewers reject competent single-country administrative
descriptions that never become a contribution to comparative governance.

## Sibling-journal guard

If the contribution is really to a sibling audience, the paper may be misrouted to *Governance*:

- Practitioner-facing public-management lessons for US administrators → **Public Administration Review (PAR)**.
- PA theory development for its own sake → **JPART**.
- Policy-analysis / program-evaluation with a cost-benefit framing → **JPAM**.
- Pure regulatory-studies / regulatory-instrument design → **Regulation & Governance** (Wiley sibling).

*Governance* wins when the premium is **comparative/institutional reach across countries** and a
contribution to how we understand the state and governing.

## Anti-patterns

- Treating *Governance* like a single-country PA outlet — the contribution must travel comparatively/institutionally
- Submitting a literature review or bibliometric mapping (out of scope here)
- Confusing the journal's "governance" with **corporate governance** (hard out of scope)
- Deferring the Data Availability Statement until acceptance — it is required at submission

## Output format

```
【Stage】fit / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Scope verdict】in-scope (exec politics / policy / PA / state) / off-fit (corporate gov / lit-review / sibling journal)
【Route to】govern-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — comparative-governance data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official *Governance*/Wiley URLs behind every fact in this pack
