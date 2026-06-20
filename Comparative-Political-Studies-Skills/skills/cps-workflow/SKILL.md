---
name: cps-workflow
description: Use when starting or navigating any Comparative Political Studies (CPS) manuscript and you need the right next sub-skill, chosen by lifecycle stage and whether the paper makes a genuinely comparative claim across countries or over time. It dispatches; it does not draft content.
---

# CPS Workflow Router (cps-workflow)

The orchestrator for a Comparative Political Studies submission. Figure out the stage, then send the
user to the matching skill. CPS is the discipline's **comparative-politics specialist** (SAGE, since
1968) — the router's first job is to confirm the paper makes a *comparative* argument (across countries,
subnational units, or over time), not a single-case study with no comparative leverage.

## When to trigger

- Starting a new CPS paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Unsure whether the paper is comparative enough for CPS (vs. a single-country area-studies piece)
- Returning with a decision letter (route to `cps-rebuttal`)

## First question: is it comparative?

| Situation | CPS fit | Route to |
|-----------|---------|----------|
| Cross-national or cross-regional claim | Strong | normal pipeline below |
| Subnational comparison or over-time within one country | Strong (intra-national counts) | normal pipeline |
| Single case used to build/test a portable theory | Conditional — must travel | `cps-topic-selection` + `cps-theory-building` |
| Single country, descriptive, no comparative leverage | Weak — likely off-fit | `cps-topic-selection` (reframe) |
| General US poli-sci or pure IR theory | Off-fit — see sibling guard | reconsider venue |

> CPS publishes work on democratization & regimes, institutions, political behavior & participation,
> ethnic politics & conflict, comparative political economy, and parties & elections — **comparative**
> in design or in the portability of the claim.

## Routing map (stage → skill)

```text
Idea / comparative fit?          → cps-topic-selection
Where does it sit in the field?  → cps-literature-positioning
What's the argument?             → cps-theory-building
Is the design defensible?        → cps-research-design
Are the analyses sound?          → cps-data-analysis
Are the exhibits clear?          → cps-tables-figures
Does it read for comparativists? → cps-writing-style
Replication & transparency?      → cps-transparency-and-data
How will it be judged?           → cps-review-process
Ready to submit?                 → cps-submission
Got an R&R / decision?           → cps-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most papers loop theory ↔ design ↔ analysis several times before writing-style.

## Comparative-fit routing check

Before selecting the next skill, force a one-minute CPS fit check:

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Comparative leverage | The variation that identifies the claim is *across* cases or time, not within one snapshot. | `cps-research-design` |
| Travel | The argument is stated as a portable mechanism a comparativist of another region can import. | `cps-theory-building` |
| Generality | The contribution speaks to a comparative-politics debate, not only to one country's specialists. | `cps-topic-selection` |
| Transparency | Quantitative results have a CPS Dataverse plan; qualitative evidence has a documentation plan. | `cps-transparency-and-data` |

If the paper fails the comparative-leverage check, do not route to writing-style — it needs a design or
fit repair, because CPS reviewers reject well-executed single-case papers that never become comparative.

## Anti-patterns

- Treating CPS like an area-studies outlet — a lone country case with no comparative leverage is off-fit
- Pitching to the whole discipline like APSR/AJPS — CPS wants the *comparative-politics* contribution
- Submitting a pure-IR or pure-formal-theory paper that never compares political systems
- Deferring the replication package to acceptance — quantitative papers cannot be finally accepted without it

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Comparative?】cross-national / subnational / over-time / single-case-that-travels / not-yet
【Route to】cps-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — comparative-politics data + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official CPS / SAGE URLs behind every fact in this pack
