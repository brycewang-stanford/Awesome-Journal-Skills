---
name: jaar-workflow
description: Use as the entry point for any Journal of the American Academy of Religion (JAAR) manuscript. Routes to the right JAAR sub-skill by lifecycle stage, and enforces the journal's gatekeeping demand up front — the article must speak to a question of broad and fundamental interest to the study of religion, not just a subfield. It dispatches; it does not draft content.
---

# JAAR Workflow Router (jaar-workflow)

The orchestrator for a JAAR submission. JAAR's editorial office reads **every** submission and, before
any peer review, asks one decisive question: does this article address a problem of **"broad and
fundamental interest to the study of religion"** and reach **beyond the sub-specialty** it comes from?
If not, the editor **returns it for reframing before review**. The router makes you answer that first.

## When to trigger

- Starting a JAAR article and unsure where to begin
- Mid-project and unsure which skill applies next
- A draft reads as a contribution to one tradition/subfield only (reframing risk)
- Returning with a decision letter (route to `jaar-revision-and-response`)

## The gate before everything: the reframing test

Before drafting, state in one sentence what your article teaches **the study of religion as a whole**
— not just Buddhist studies, or American religious history, or philosophy of religion. If you cannot,
go to `jaar-topic-selection` and `jaar-scholarly-positioning` and reframe **now**; the editor will
otherwise bounce it back unreviewed.

## Routing map (stage → skill)

```text
Idea / fit + reframing?           → jaar-topic-selection
Where does it sit in the field?   → jaar-scholarly-positioning
What's the argument / "point"?    → jaar-argument-development
Texts, traditions, fieldwork?     → jaar-sources-and-evidence
Theory & method (reflexivity)?    → jaar-theory-and-method
How is the essay built?           → jaar-structure-and-exposition
Does the prose read well?         → jaar-writing-style
In-text citations + style?        → jaar-citation-and-style
How will it be judged?            → jaar-review-process
Ready to submit?                  → jaar-submission
Got a decision / R&R?             → jaar-revision-and-response
```

## Default order

`topic-selection → scholarly-positioning → argument-development → sources-and-evidence →
theory-and-method → structure-and-exposition → writing-style → citation-and-style → review-process →
submission → revision-and-response`

## Anti-patterns

- Drafting a subfield-only article and hoping the editor sends it out anyway (it won't)
- Treating JAAR like an empirical-social-science venue (no datasets/statistics/replication here)
- Using footnotes for citations (JAAR uses **in-text author-date**; see `jaar-citation-and-style`)
- Planning an unsolicited book review (JAAR reviews are **commissioned only**)

## Output format

```
【Stage】fit / positioning / argument / sources / theory-method / structure / prose / citation / review / submit / revise
【Reframing test】one sentence on what it teaches the study of religion writ large
【Route to】jaar-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference and research tools for the study of religion
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JAAR URLs behind every fact in this pack
