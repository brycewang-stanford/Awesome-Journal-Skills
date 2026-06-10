---
name: mind-workflow
description: Use as the entry point for any Mind (philosophy journal) article. Routes to the right Mind sub-skill based on where you are in the lifecycle and whether the piece is an article, discussion note, book review, or critical notice. Mind is analytic philosophy — argument, not data — so the router's first job is to confirm there is a sharp thesis and a sound argument. It dispatches; it does not draft content.
---

# Mind Workflow Router (mind-workflow)

The orchestrator for a Mind submission. Figure out the stage and the **content type**, then send the
user to the matching skill. Mind takes **quality as the sole criterion** and excludes no area, style,
or school of philosophy — but every accepted piece rests on a **clear thesis defended by a valid,
sound argument**. The router's first job is to make sure that argument exists before polishing prose.

## When to trigger

- Starting a new Mind paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether the piece is an **article**, **discussion**, **book review**, or **critical notice**
- Returning with a decision letter (route to `mind-revision-and-response`)

## First question: which content type?

| Situation | Type | Route to |
|-----------|------|----------|
| Original, free-standing argument | **Article** (~8,000 words) | normal pipeline below |
| Short response to a specific published paper | **Discussion** | `mind-thesis-and-argument` + `mind-objections-and-replies`, tighter scope |
| Evaluative summary of a recent book | **Book review** | `mind-literature-positioning` + `mind-writing-style` |
| Longer engagement developing your own ideas from a book | **Critical notice** | `mind-thesis-and-argument` + `mind-objections-and-replies` |

> Most submissions are **articles**. Discussions, reviews, and critical notices are tighter; do not
> inflate one into an article (or pad an article down into a note).

## Routing map (stage → skill)

```text
Idea / fit for Mind?            → mind-topic-selection
Where does it sit in the debate?→ mind-literature-positioning
What exactly is the thesis?     → mind-thesis-and-argument
Strongest objection answered?   → mind-objections-and-replies
Are the concepts precise?       → mind-conceptual-analysis-and-method
Is the paper well-built?        → mind-structure-and-exposition
Does it read clearly?           → mind-writing-style
References in MIND house style? → mind-citation-and-style
How will it be judged?          → mind-review-process
Ready to submit?                → mind-submission
Got a decision / R&R?           → mind-revision-and-response
```

## Default order

`topic-selection → literature-positioning → thesis-and-argument → objections-and-replies →
conceptual-analysis-and-method → structure-and-exposition → writing-style → citation-and-style →
review-process → submission → revision-and-response`

Iterate: most papers loop thesis ↔ objections ↔ conceptual analysis several times before exposition.

## Anti-patterns

- Polishing prose before the thesis and argument are actually settled
- Treating Mind like an empirical venue (it has no data, statistics, or robustness checks)
- A survey of a topic with no original thesis of one's own
- Skipping the strongest objection — at Mind the reply *is* much of the contribution


## Router pass for Mind

Use this as a second-pass capability check. First lock the target thesis, argument map, objection sequence, and dialectical payoff; then test whether the manuscript addresses analytic-philosophy reviewers who expect a precise thesis, live objection, argument structure, and contribution to an active debate.

- **Primary move:** Run fit gate, evidence gate, writing gate, source-map gate, and output contract; stop when a gate lacks evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Philosophical Review for broader top philosophy, Nous for analytic breadth, Ethics for normative/political theory; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Stage】idea / positioning / thesis / objections / concepts / structure / writing / citation / review / submit / revise
【Type】Article / Discussion / Book review / Critical notice
【Route to】mind-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — philosophy reference works, logic tools, the MIND Stylesheet
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Mind URLs behind every fact in this pack
