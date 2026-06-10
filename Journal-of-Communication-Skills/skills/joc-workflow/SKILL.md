---
name: joc-workflow
description: Use as the entry point for any Journal of Communication (JoC) manuscript. Routes to the right JoC sub-skill based on where you are in the lifecycle and which format (original research article, JoC Forum, special issue) fits. It dispatches; it does not draft content.
---

# JoC Workflow Router (joc-workflow)

The orchestrator for a JoC submission. Figure out the stage and the **format**, then send the user to
the matching skill. JoC is the **flagship, field-wide journal** of the International Communication
Association — the router's first job is to make sure the paper is pitched to communication research
broadly, not just one subfield or platform.

## When to trigger

- Starting a new JoC paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **format** fits (article, JoC Forum, special-issue call)
- Returning with a decision letter (route to `joc-rebuttal`)

## First question: which format?

| Situation | Format | Route to |
|-----------|--------|----------|
| Full original study, broad significance | **Original article** (main doc ≤ 35 pages) | normal pipeline below |
| Short, argument-driven contribution | **JoC Forum** (3,000–6,000 words) | normal pipeline, tighter scope |
| Responding to a themed call | **Special issue** | `joc-topic-selection` (fit to the call) + pipeline |
| Prospective design, data not yet collected | preregister first | `joc-open-science-and-transparency` early |

> If the design is prospective, preregister and plan Open Science Badge materials **before** collecting
> data — note the preregistration in the cover letter at submission.

## Routing map (stage → skill)

```text
Idea / fit?                      → joc-topic-selection
Where does it sit in the field?  → joc-literature-positioning
What's the argument?             → joc-theory-building
Is the design defensible?        → joc-research-design
Are the analyses sound?          → joc-data-analysis
Are the exhibits clear?          → joc-tables-figures
Does it read for the field?      → joc-writing-style
Data statement & open science?   → joc-open-science-and-transparency
How will it be judged?           → joc-review-process
Ready to submit?                 → joc-submission
Got an R&R / decision?           → joc-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → open-science-and-transparency → review-process → submission → rebuttal`

Iterate: most papers loop theory ↔ design ↔ analysis several times before writing-style.

## Anti-patterns

- Treating JoC like a niche subfield outlet — the contribution must reach communication research broadly
- Forcing a quantitative template onto computational, qualitative, or critical work (JoC judges each on its own terms)
- Padding a short, focused argument into a full article when the JoC Forum would land harder
- Leaving the Data Availability Statement and badge materials until acceptance


## Router pass for Journal of Communication

Treat this skill as an executable review pass, not a prose hint. First lock the communication process, platform/media setting, construct measurement, and study design; then judge whether the current manuscript answers the venue's real reader: communication reviewers who balance theory, media context, measurement, and social implications.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Communication Research for quantitative communication, New Media & Society for platform focus, Human Communication Research for theory testing; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Format】Original article / JoC Forum / Special issue
【Route to】joc-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — communication data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JoC URLs behind every fact in this pack
