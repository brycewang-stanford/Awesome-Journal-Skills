---
name: pubar-workflow
description: Use when starting or navigating any Public Administration Review (PAR) manuscript and unsure which skill applies. Routes to the right PAR sub-skill based on lifecycle stage and which article type (Scholarly Take, Conceptualizing PA, Early Career Intel, Practically Speaking, Public Administration in Print) fits. It dispatches; it does not draft content.
---

# PAR Workflow Router (pubar-workflow)

The orchestrator for a Public Administration Review submission. Figure out the **stage** and the
**article type**, then send the user to the matching skill. PAR is the **ASPA flagship that bridges
research and practice** — the router's first job is to confirm the paper carries a credible
contribution to scholarship *and* a defensible "so-what" for public managers.

## When to trigger

- Starting a new PAR paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits the work
- Returning with a decision letter (route to `pubar-rebuttal`)

## First question: which article type?

| Situation | Article type | Route to |
|-----------|--------------|----------|
| Full empirical study, broad PA significance | **Scholarly Take** (research manuscript, ≤ 8,000 words) | normal pipeline below |
| Conceptual / theoretical or "state of PA" thought piece | **Conceptualizing Public Administration** | `pubar-theory-building` early |
| Research manuscript by an early-career scholar | **Early Career Intel** | normal pipeline, scope tightly |
| Practitioner–scholar co-authored, practice-driven | **Practically Speaking** | `pubar-writing-style` (practitioner voice) early |
| Book review | **Public Administration in Print** | out of scope for this empirical stack |

> Whatever the type, **Evidence for Practice** (3–5 takeaway points for practitioners) is expected —
> encouraged at first submission, required at revision (检索于 2026-06；以官网为准).

## Routing map (stage → skill)

```text
Idea / fit?                       → pubar-topic-selection
Where does it sit in the field?   → pubar-literature-positioning
What's the argument / mechanism?  → pubar-theory-building
Is the design defensible?         → pubar-research-design
Are the analyses sound?           → pubar-data-analysis
Are the exhibits clear?           → pubar-tables-figures
Does it speak to scholars+practice? → pubar-writing-style
Repro / TOP transparency package? → pubar-transparency-and-data
How will it be judged?            → pubar-review-process
Ready to submit?                  → pubar-submission
Got an R&R / decision?            → pubar-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most PAR papers loop theory ↔ design ↔ analysis several times, and the **practitioner
"so-what"** should be drafted alongside the contribution, not bolted on at the end.

## The PAR bridge check (run before routing)

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Scholarly contribution | A PA scholar outside the subfield (HRM, budgeting, governance) sees the advance. | `pubar-topic-selection` |
| Practitioner relevance | A public manager can name a decision the finding would inform (Evidence for Practice). | `pubar-writing-style` |
| Sibling fit | The paper is broad/practice-bridging, not a JPART-style pure-theory or JPAM-style policy-analysis piece. | `pubar-topic-selection` |
| Transparency | Data/code/qualitative materials have a TOP-compliant plan. | `pubar-transparency-and-data` |

If the paper fails the practitioner-relevance check, do not route to writing-style for polish — it
needs a contribution repair, because PAR reviewers expect every article to earn its Evidence for
Practice points honestly rather than tack them on.

## Anti-patterns

- Treating PAR like a pure-theory venue (that is JPART) or a policy-analysis venue (that is JPAM)
- A finding with no credible practitioner takeaway — Evidence for Practice cannot be fabricated
- Forcing a quantitative template onto case-comparison or mixed-methods work PAR values
- Deferring the TOP transparency materials until acceptance

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Article type】Scholarly Take / Conceptualizing PA / Early Career Intel / Practically Speaking
【Route to】pubar-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — PA data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official PAR URLs behind every fact in this pack
