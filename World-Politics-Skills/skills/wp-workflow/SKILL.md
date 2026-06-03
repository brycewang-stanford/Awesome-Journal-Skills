---
name: wp-workflow
description: Use as the entry point for any World Politics manuscript. Routes to the right World Politics sub-skill based on where you are in the lifecycle and whether you are writing a research article or a review article. World Politics is a comparative-politics + international-relations specialist, so the router's first job is to confirm the question travels across cases. It dispatches; it does not draft content.
---

# World Politics Workflow Router (wp-workflow)

The orchestrator for a World Politics submission. Figure out the stage and the **article type**, then
send the user to the matching skill. World Politics publishes scholarship in **comparative politics and
international relations** — it is a *specialist* in that joint domain, not a discipline-wide generalist
(unlike APSR/AJPS/JOP) and not IR-only. The router's first job is to confirm the question **travels
across cases or systems** and sits inside the journal's scope.

## When to trigger

- Starting a new World Politics paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding between a **research article** and a **review article**
- Returning with a decision letter (route to `wp-rebuttal`)

## First question: which article type, and is it in scope?

| Situation | Type | Route to |
|-----------|------|----------|
| Original study posing a substantive comparative/IR question | **Research article** (≤ 12,500 words) | normal pipeline below |
| Synthesis of thematically related books that reframes a field's agenda | **Review article** (usually commissioned; still triple-blind) | `wp-literature-positioning` + `wp-theory-building` |
| Opinion / policy piece, stand-alone political theory, historical or journalistic narrative | **Out of scope** | stop — World Politics does not publish these |

> Review articles "differ from conventional book reviews": they must **advance how a field should
> pursue future work**, not just summarize books. They are usually commissioned — confirm before
> investing (待核实).

## Routing map (stage → skill)

```text
Idea / fit & scope?              → wp-topic-selection
Where does it sit in the field?  → wp-literature-positioning
What's the argument that travels?→ wp-theory-building
Is the design defensible?        → wp-research-design
Are the analyses sound?          → wp-data-analysis
Are the exhibits clear?          → wp-tables-figures
Does it read across cases?       → wp-writing-style
Dataverse & transparency?        → wp-transparency-and-data-policy
How will it be judged?           → wp-review-process
Ready to submit?                 → wp-submission
Got an R&R / decision?           → wp-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data-policy → review-process → submission → rebuttal`

Iterate: most papers loop theory ↔ design ↔ analysis several times before writing-style.

## Anti-patterns

- Treating World Politics like a generalist venue (APSR/AJPS/JOP) — the contribution must sit in
  comparative politics or IR and speak across cases
- Treating it like an IR-only journal — comparative-politics questions are equally central
- Submitting an opinion/policy piece, stand-alone political theory, or a historical/journalistic
  narrative (explicitly out of scope)
- Pitching an unsolicited review article without checking the commissioning norm

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】research article / review article
【In scope?】comparative or IR, travels across cases? [Y/N]
【Route to】wp-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — comparative + IR data and software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official World Politics URLs behind every fact in this pack
