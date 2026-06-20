---
name: jpam-workflow
description: Use when starting or orienting any Journal of Policy Analysis and Management (JPAM) manuscript and you need the entry point. Routes to the right JPAM sub-skill based on lifecycle stage and which article type (Feature Research Article, Point/Counterpoint, Methods for Policy Analysis, Policy Insights, Policy Retrospective) fits. It dispatches; it does not draft content.
---

# JPAM Workflow Router (jpam-workflow)

The orchestrator for a JPAM submission. Figure out the stage and the **article type**, then send the
user to the matching skill. JPAM is the **cross-disciplinary public-policy-analysis flagship** of APPAM
(published by Wiley) — the router's first job is to make sure the paper delivers a **credibly identified
effect of a real policy or program** *and* a **clear, non-overclaimed policy implication**, legible to
economists, political scientists, and public-management scholars alike.

## When to trigger

- Starting a new JPAM paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits the work
- Returning with a decision letter (route to `jpam-rebuttal`)

## First question: which article type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full causal evaluation of a policy/program with broad relevance | **Feature Research Article** | normal pipeline below |
| Invited debate between scholars on a timely policy question (not peer-reviewed) | **Point/Counterpoint** | `jpam-writing-style` + `jpam-literature-positioning` |
| A methodological advance for policy analysts | **Methods for Policy Analysis** | `jpam-research-design` + `jpam-data-analysis` |
| Short, fast-turnaround take on a pressing issue (≤ 3,000 words, not peer-reviewed) | **Policy Insights** | `jpam-writing-style` + `jpam-topic-selection` |
| Reflective look back at how a policy/literature evolved | **Policy Retrospective** | `jpam-literature-positioning` + `jpam-theory-building` |

> Point/Counterpoint and Policy Insights are **invited / not peer-reviewed** — confirm the current
> invitation and length rules on the author page before pitching (检索于 2026-06；以官网为准).

## Routing map (stage → skill)

```text
Idea / policy relevance + fit?    → jpam-topic-selection
Where does it sit across fields?  → jpam-literature-positioning
What's the theory of change?      → jpam-theory-building
Is identification credible?       → jpam-research-design
Are the estimates + CBA sound?    → jpam-data-analysis
Are the exhibits clear?           → jpam-tables-figures
Does the implication land?        → jpam-writing-style
Replication package ready?        → jpam-transparency-and-data
How will it be judged?            → jpam-review-process
Ready to submit?                  → jpam-submission
Got an R&R / decision?            → jpam-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most papers loop theory-of-change ↔ design ↔ analysis several times before writing-style.

## JPAM fit check (run before routing)

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Policy relevance | A policymaker or program designer can state what decision this evidence informs. | `jpam-topic-selection` |
| Identification | The causal claim rests on a credible design (RCT / DiD / RD / IV / synthetic control), not selection-on-observables hope. | `jpam-research-design` |
| Cross-disciplinary reach | An economist, a political scientist, and a public-management reader each see why it matters. | `jpam-literature-positioning` |
| Implication discipline | The policy takeaway is calibrated to what the design actually identifies — no overclaiming. | `jpam-writing-style` |

If the paper fails the identification check, do not route to writing-style — JPAM reviewers reject
well-written papers whose causal claim outruns the design. If it fails policy relevance, it may be a
better fit for a field economics/political-science journal (see sibling guard in README).

## Anti-patterns

- Treating JPAM like a field economics journal — the policy decision and cross-field reach must be explicit
- A clean estimate with no stated policy implication (or an implication the design cannot support)
- Confusing JPAM with AEJ: Economic Policy / J. of Public Economics (economics field venues) or PAR / JPART (public management)
- Pitching a peer-reviewed Feature article into the invited, non-reviewed Point/Counterpoint or Policy Insights slots

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Feature Research Article / Point-Counterpoint / Methods / Policy Insights / Policy Retrospective
【Route to】jpam-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — policy-evaluation data sources + software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JPAM / APPAM / Wiley URLs behind every fact in this pack
