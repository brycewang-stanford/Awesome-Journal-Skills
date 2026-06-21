---
name: ylj-workflow
description: Use as the entry point for any The Yale Law Journal (YLJ) piece. Routes to the right YLJ sub-skill based on lifecycle stage and which track (Article, Essay, Feature, student Note/Comment, or Forum) fits. It dispatches; it does not draft content.
---

# YLJ Workflow Router (ylj-workflow)

The orchestrator for a Yale Law Journal submission. YLJ is a **student-edited, generalist** law review
at Yale Law School — **not peer-reviewed**. Figure out the **track** and the **stage**, then send the
user to the matching skill. Unlike a peer-reviewed journal, the piece must already read as a **near-final,
heavily-footnoted, Bluebook-compliant** article when it is submitted, because student editors evaluate a
finished manuscript and then cite-check every footnote.

## When to trigger

- Starting a new piece for YLJ and unsure where to begin
- Mid-draft and unsure which skill applies next
- Deciding which **track** fits (Article / Essay / Feature / Note / Comment / Forum)
- Holding an offer from another review and weighing an **expedite** (route to `ylj-placement-strategy`)
- An offer landed and student editing is starting (route to `ylj-student-editor-review`)

## First question: which track?

| Situation | Track | Route to |
|-----------|-------|----------|
| Full original scholarship by a professional author | **Article** (encourage < 25,000 words incl. footnotes) | normal pipeline below |
| Shorter, more pointed professional piece | **Essay** (encourage < 15,000 words incl. footnotes) | normal pipeline, tighter scope |
| Curated multi-piece collection / symposium contribution | **Feature** | `ylj-thesis-and-contribution` + `ylj-placement-strategy` |
| Student-authored long-form scholarship (Yale Law student) | **Note** (first-time cap ~20,000 words) | `ylj-student-editor-review` (Notes Development) early |
| Student-authored short piece (Yale Law student) | **Comment** (first-time cap ~7,000 words) | `ylj-student-editor-review` early |
| Short, timely online response or essay | **YLJ Forum** (encourage < 10,000 words) | `ylj-revision-and-editing` (Forum path) |

> Caps are the figures YLJ "strongly encourages"; over-length weighs against acceptance
> (检索于 2026-06；以官网为准). Notes/Comments are written by **Yale Law students**; outside authors use
> Article/Essay/Feature/Forum.

## Routing map (stage → skill)

```text
Is the topic YLJ-worthy?         → ylj-topic-selection
What exactly is the claim?       → ylj-thesis-and-contribution
Has anyone said this already?    → ylj-preemption-check
Does the argument hold?          → ylj-argument-structure
Are the cites pinpointed/Bluebook?→ ylj-sources-and-bluebook
Does the prose read like YLJ?    → ylj-writing-style
Where + when to submit/expedite? → ylj-placement-strategy
Working with student editors?    → ylj-student-editor-review
Ready to upload?                 → ylj-submission
In the edit cycle / Forum?       → ylj-revision-and-editing
Final footnote + cite-check?     → ylj-footnotes-and-cite-check
```

## Default order

`topic-selection → thesis-and-contribution → preemption-check → argument-structure →
sources-and-bluebook → writing-style → placement-strategy → submission → student-editor-review →
revision-and-editing → footnotes-and-cite-check`

Iterate: most pieces loop thesis ↔ preemption ↔ argument several times before the prose polish. The
**footnote apparatus is built throughout**, not bolted on at the end — `ylj-footnotes-and-cite-check`
runs both before submission and again during the editorial source-pull.

## Generalist fit check (run before routing onward)

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Audience | A generalist legal reader (not just your subfield) can state why the claim matters. | `ylj-topic-selection` |
| Novelty | The thesis is not preempted by an existing article, student note, or working paper. | `ylj-preemption-check` |
| Apparatus | Every assertion of law or fact is footnoted with a pinpoint Bluebook cite. | `ylj-sources-and-bluebook` |
| Posture | The piece is **near-final** — not a draft you plan to finish after acceptance. | `ylj-writing-style` |

## Anti-patterns

- Treating YLJ like a peer-reviewed journal that will co-develop a rough draft — student editors evaluate a finished article
- Submitting before the footnote apparatus is complete and Bluebook-conforming
- Forgetting YLJ uses its **own online submission system** (not Scholastica/ExpressO) — see `ylj-submission`
- Assuming an expedite buys priority — at YLJ expedite gives **no competitive advantage** (see `ylj-placement-strategy`)
- Pitching a narrow doctrinal note as a generalist Article without a claim that travels

## Output format

```
【Stage】topic / thesis / preemption / argument / cites / prose / placement / submit / editing / forum / cite-check
【Track】Article / Essay / Feature / Note / Comment / Forum
【Route to】ylj-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — legal research databases + citation/Bluebook tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official YLJ URLs behind every fact in this pack
