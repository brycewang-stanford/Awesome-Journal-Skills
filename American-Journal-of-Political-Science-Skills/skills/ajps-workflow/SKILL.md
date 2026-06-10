---
name: ajps-workflow
description: Use as the entry point for any American Journal of Political Science (AJPS) manuscript. Routes to the right AJPS sub-skill based on lifecycle stage and which submission type (Article, Research Note, Correspondence) fits, and reminds you that AJPS re-runs your code via a third-party verifier before publishing. It dispatches; it does not draft content.
---

# AJPS Workflow Router (ajps-workflow)

The orchestrator for an AJPS submission. Figure out the stage and the **submission type**, then send
the user to the matching skill. AJPS is the MPSA's flagship, **Wiley**-published, **double-blind**
journal whose defining feature is **mandatory third-party verification of replication materials before
publication** — so this router also makes sure reproducibility is engineered from the start, not bolted
on at acceptance.

## When to trigger

- Starting a new AJPS paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether the paper is an **Article**, **Research Note**, or **Correspondence**
- Returning with a decision letter (route to `ajps-rebuttal`)

## First question: which submission type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full original study | **Article** (<= 10,000 words) | normal pipeline below |
| A **methodology** advance or a **meta-analysis** | **Research Note** (<= 4,000 words) | normal pipeline, tighter scope |
| Critique / correction of a paper already published in AJPS | **Correspondence** (<= 4,000 words) | `ajps-literature-positioning` + `ajps-data-analysis` |

> The Research Note is **not** a short empirical paper — at AJPS it is reserved for methodology
> (including methodology in normative theory) and meta-analyses. Do not mis-route a small empirical
> study into it.

## Routing map (stage -> skill)

```text
Idea / fit?                       -> ajps-topic-selection
Where does it sit in the field?   -> ajps-literature-positioning
What's the argument?              -> ajps-theory-building
Is the design identified?         -> ajps-research-design
Are the analyses sound?           -> ajps-data-analysis
Are the exhibits clear?           -> ajps-tables-figures
Does it read well + fit caps?     -> ajps-writing-style
Will the code re-run for a verifier? -> ajps-replication-and-verification
How will it be judged?            -> ajps-review-process
Ready to submit?                  -> ajps-submission
Got an R&R / decision?            -> ajps-rebuttal
```

## Default order

`topic-selection -> literature-positioning -> theory-building -> research-design -> data-analysis ->
tables-figures -> writing-style -> replication-and-verification -> review-process -> submission ->
rebuttal`

Iterate: theory <-> design <-> analysis usually loops several times. Critically, start the
**replication-and-verification** package while you analyze — at acceptance an independent verifier
re-runs your code, and an unscripted analysis cannot be fixed quickly under deadline.

## Anti-patterns

- Treating reproducibility as a post-acceptance chore — AJPS verifies before publishing
- Mis-routing a short empirical study into the methodology-only Research Note type
- Sending a critique of a non-AJPS paper as Correspondence (it is for published AJPS work)
- Forgetting that table/figure captions and footnotes count toward the word limit


## Router pass for American Journal of Political Science

Run this as a concrete capability pass. First lock the political theory, design leverage, measurement validity, and scope condition; then test whether the manuscript addresses political-science reviewers who expect tight theory, transparent design, and a contribution that travels across political settings.

- **Primary move:** Run the pack as fit gate, evidence gate, writing gate, source-map gate, and output contract; stop when a gate lacks evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against APSR for field-wide breadth, Journal of Politics for broader political-science audience, Political Analysis for methods-first work; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / replication / review / submit / rebut
【Type】Article / Research Note (methodology|meta-analysis) / Correspondence
【Route to】ajps-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — political-science data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AJPS URLs behind every fact in this pack
