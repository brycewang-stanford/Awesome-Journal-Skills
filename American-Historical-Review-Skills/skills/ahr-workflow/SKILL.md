---
name: ahr-workflow
description: Use as the entry point for any American Historical Review (AHR) manuscript. Routes to the right AHR sub-skill based on where you are in the lifecycle of a history article — from significance and historiography through archives, interpretation, Chicago-style prose, review, and revision. It dispatches; it does not draft content.
---

# AHR Workflow Router (ahr-workflow)

The orchestrator for an AHR submission. Figure out the stage of the project, then send the user to the
matching skill. The AHR is the **flagship journal of the historical profession** — its articles are
**historiographical interventions** built on **primary sources**, judged by historians across all
fields. The router's first job is to make sure the project has both a significant question and a real
archival basis before polishing prose.

## When to trigger

- Starting a new AHR article and unsure where to begin
- Mid-project and unsure which skill applies next
- Sitting on rich archival material but no argument yet (route to `ahr-argument-development`)
- Returning with a decision letter (route to `ahr-revision-and-response`)

## What the AHR is (and is not)

- It is a **generalist history journal**: all periods, all places, all subfields, English-language.
- It is **not** a social-science venue: there is **no data-availability/replication policy**, no
  statistical-significance bar, no results tables. The currency is **argument, evidence, and
  interpretation** anchored in primary sources and a historiographical conversation.

## Routing map (stage → skill)

```text
Is the question significant?        → ahr-topic-selection
Where does it sit in the field?     → ahr-historiography-positioning
What is the argument / stakes?      → ahr-argument-development
What are the sources, and how good? → ahr-sources-and-archives
How am I reading the evidence?      → ahr-interpretation-and-method
Does the article hold together?     → ahr-structure-and-exposition
Does the prose work?                → ahr-writing-style
Are the notes correct (Chicago)?    → ahr-citation-and-style
How will it be judged?              → ahr-review-process
Ready to submit?                    → ahr-submission
Got a decision / R&R?               → ahr-revision-and-response
```

## Default order

`topic-selection → historiography-positioning → argument-development → sources-and-archives →
interpretation-and-method → structure-and-exposition → writing-style → citation-and-style →
review-process → submission → revision-and-response`

Iterate: history rarely moves in a straight line. Most projects loop **argument ↔ sources ↔
interpretation** many times as the archive talks back before the structure settles.

## Anti-patterns

- Polishing prose before the **argument** and **sources** are settled
- Treating the AHR like a subfield journal — the contribution must reach historians of other fields
- Importing a social-science template (hypotheses, data section, robustness) onto a history article
- Skipping historiography — "no one has studied X" is not, by itself, a contribution

## Output format

```
【Stage】significance / historiography / argument / sources / interpretation / structure / prose / citation / review / submit / revise
【Route to】ahr-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — archives, databases, and Chicago-notes tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AHR URLs behind every fact in this pack
