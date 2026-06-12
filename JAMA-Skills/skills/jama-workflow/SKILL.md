---
name: jama-workflow
description: Use when deciding which jama-* sub-skill to invoke next, or when sequencing a clinical manuscript from scope check through revision for JAMA (Journal of the American Medical Association). Routes — does not replace — the specialized skills.
---

# JAMA Manuscript Workflow (jama-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jama-* skill to use for the stage you are at** when preparing an Original Investigation (or systematic review / meta-analysis) for JAMA.

Default assumption: unless the user says the target is a different journal, treat the manuscript as aimed at JAMA — a big-four general medical journal (alongside NEJM, The Lancet, The BMJ) that demands **general medical importance**, a clean **EQUATOR-aligned reporting standard** (CONSORT / STROBE / PRISMA / STARD), prospective **trial registration**, and dedicated **statistical review**.

## When to trigger

- "What should I do next?" on a clinical manuscript
- A draft is handed over and the current bottleneck is unclear
- You are bouncing between design, stats, writing, and reviewer replies
- You received JAMA decision letter / reviewer comments and must switch to revision mode

## Routing table

| Current symptom                                                      | Next skill                   |
|----------------------------------------------------------------------|------------------------------|
| Unsure the topic clears JAMA's general-medical-importance bar        | `jama-scope-fit`             |
| Design questions: RCT vs cohort vs diagnostic vs review; ITT, bias   | `jama-study-design`          |
| Need the right EQUATOR checklist + flow diagram (CONSORT/PRISMA…)    | `jama-reporting-standards`   |
| p-values only, no effect sizes/CIs; multiplicity not handled         | `jama-statistics`            |
| Figures/tables cluttered, no CONSORT/PRISMA diagram, units wrong     | `jama-figures-tables`        |
| Abstract not in JAMA structure; no Key Points box                    | `jama-structured-abstract`   |
| Trial not registered / registered late; missing IRB, consent, COI    | `jama-ethics-registration`   |
| Prose verbose, jargon-heavy, "spin" in conclusions                   | `jama-writing-style`         |
| Need a cover letter pitching importance to the editor                | `jama-cover-letter`          |
| Ready to submit; need the pre-submission preflight                   | `jama-submission`            |
| Received reviewer comments / a revise decision                       | `jama-peer-review-revision`  |

## Default order

1. `jama-scope-fit` — decide whether JAMA is the right home before investing more
2. `jama-study-design` — lock the design and its internal-validity safeguards
3. `jama-reporting-standards` — choose and complete the EQUATOR checklist + diagram
4. `jama-statistics` — pre-specified outcomes, effect sizes + 95% CIs, multiplicity
5. `jama-figures-tables` — finalize the flow diagram, baseline table, main exhibits
6. `jama-structured-abstract` — JAMA structured abstract + Key Points box
7. `jama-ethics-registration` — registration, IRB/consent, ICMJE disclosures, data sharing
8. `jama-writing-style` — tighten prose, remove spin, match house style (polish)
9. `jama-cover-letter` — editor-facing pitch of general medical importance
10. `jama-submission` — final preflight against author instructions
11. `jama-peer-review-revision` — response after the decision letter

> `jama-structured-abstract` and `jama-writing-style` are **late-stage polish** — do not perfect prose while the design or primary outcome is still unsettled.

## Decision shortcuts

- "I have a finding but it's narrow / subspecialty-only" → `jama-scope-fit`
- "Reviewers will ask if this is ITT or per-protocol" → `jama-study-design`
- "I don't know whether I need CONSORT or STROBE" → `jama-reporting-standards`
- "My results are all p < 0.05 with no CIs" → `jama-statistics`
- "My RCT has no participant flow diagram" → `jama-figures-tables`
- "My abstract is one block paragraph" → `jama-structured-abstract`
- "I registered the trial after enrollment started" → `jama-ethics-registration`
- "My conclusion overstates a secondary outcome" → `jama-writing-style`
- "I need to convince the editor this matters to clinicians" → `jama-cover-letter`
- "Submitting tomorrow" → `jama-submission`
- "I got three reviews and a major-revision letter" → `jama-peer-review-revision`

## Differences vs. specialty-journal skills

If the work is mechanistic, bench, or narrowly subspecialty (e.g., molecular oncology), a specialty journal stack fits better than JAMA. Core contrast:

- JAMA: broad clinician readership; demands **general medical importance** and pragmatic clinical relevance.
- Specialty / basic-science journals: tolerate narrow scope and mechanistic depth that JAMA would consider off-fit.

## Worked routing example (illustrative)

A team hands over a near-complete multicenter randomized clinical trial (illustrative: N = 4,200, 90-day mortality, absolute risk difference -3.3 percentage points [95% CI, -5.9 to -0.7]) bound for the Journal of the American Medical Association, but the abstract is one block paragraph, the registration date is unverified, and the Results report only p-values. Route in dependency order, not symptom order: `jama-ethics-registration` first (registration timing is a hard gate), then `jama-statistics` (effect sizes with CIs, ITT), then `jama-figures-tables` (CONSORT diagram reconciles all 4,200), then `jama-structured-abstract`, with style and submission last. The job is to stop teams from polishing prose while a registration defect sits unaddressed.

## Router output format

```
【Stage detected】scope / design / stats / exhibits / abstract / ethics / submit / revision
【Hard gate unresolved?】registration timing / primary outcome / none
【Recommended next skill】jama-...
【Why this order】what must precede polish
【Sibling-venue check】NEJM / Lancet / specialty re-route? yes-with-reason / no
```

## Anti-patterns

- **Do not** skip `jama-scope-fit` and polish a manuscript that a JAMA editor will desk-reject for narrow importance.
- **Do not** let `jama-figures-tables` beautify exhibits before the reporting standard and primary outcome are settled.
- **Do not** let `jama-peer-review-revision` draft a response letter before the manuscript itself is actually revised.
- **Do not** defer `jama-ethics-registration` — a retrospectively registered trial cannot be fixed at submission.
