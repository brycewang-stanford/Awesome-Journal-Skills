---
name: ectheory-workflow
description: Use as the router for an Econometric Theory (ET) manuscript — decides which ectheory-* skill to invoke next across the theorem-proof lifecycle, from topic selection through single-anonymous review and rebuttal. Start here when unsure where you are.
---

# Workflow Router (ectheory-workflow)

## When to trigger

- Starting a new theorem-proof paper aimed at *Econometric Theory* (ET) and unsure which step comes first
- Mid-project and unsure whether the bottleneck is the assumptions, the proofs, the simulations, or the framing
- Deciding whether the paper is a full **Article** or a short **Miscellanea** (typically <20 pages, often ~15)
- About to submit and wanting the right preflight and review-process skills

## What ET is, in one paragraph

ET, published by **Cambridge University Press** and founded by **Peter C. B. Phillips**, publishes the
mathematical and statistical foundations of econometrics — asymptotic theory, probability-theoretic
methods, time series and nonstationarity, high-dimensional and non-standard environments. Papers are
**theorem-proof in style** with supporting lemmas, derivations, and often Monte Carlo or numerical
illustration. From **1 January 2026** three joint Editors-in-Chief (Guggenberger, Su, Sun) succeed
founding editor Phillips, with a program of invited papers with discussions and themed special issues.

## Default sequence

```text
ectheory-topic-selection         (is the result general + foundational enough?)
        ▼
ectheory-literature-positioning  (stake the theorem against the frontier)
        ▼
ectheory-identification-strategy (assumptions, regularity conditions, asymptotics, proof plan)
        ▼
ectheory-contribution-framing    (state the theorem so its generality is legible)
        ▼
ectheory-data-analysis           (Monte Carlo / numerical illustration, if any)
        ▼
ectheory-tables-figures          (simulation tables, limit-behavior plots, self-contained notes)
        ▼
ectheory-writing-style           (proof exposition, notation discipline, APA references)
        ▼
ectheory-replication-and-data-policy (reproducible computation + ET Supplementary Material file)
        ▼
ectheory-review-process          (war-game referee objections; single-anonymous reality)
        ▼
ectheory-submission              (ScholarOne single-PDF preflight; Article vs Miscellanea; 50-page ceiling)
        ▼
ectheory-rebuttal                (response strategy when the decision letter arrives)
```

## Routing heuristics

- Proof has a gap or an assumption feels ad hoc → `ectheory-identification-strategy`
- Result is correct but reads as narrow/incremental → `ectheory-topic-selection` + `ectheory-contribution-framing`
- Paper exceeds 50 pages → `ectheory-submission` (overflow to online Supplement) + `ectheory-tables-figures`
- Simulations unconvincing or non-reproducible → `ectheory-data-analysis` + `ectheory-replication-and-data-policy`
- Decision letter in hand → `ectheory-rebuttal`

## Symptom-to-skill routing table

The fastest route is by symptom. At Econometric Theory the recurring bottlenecks are about the theorem and
its proof, not about empirical design — route accordingly.

| Symptom in the manuscript | Likely diagnosis | Route to |
| --- | --- | --- |
| A regularity condition is too strong or not primitive | assumption defect | `ectheory-identification-strategy` |
| A rate is stated but no limiting law | missing distribution theory | `ectheory-identification-strategy` |
| The introduction buries what is proved | framing defect | `ectheory-contribution-framing` |
| Referee will call it a special case | positioning gap | `ectheory-literature-positioning` |
| Monte Carlo never visits the boundary | weak finite-sample evidence | `ectheory-data-analysis` |
| Proof overflows the page ceiling | length / Supplement | `ectheory-submission` + `ectheory-replication-and-data-policy` |

## A worked routing pass

A draft proves a new estimator's rate but states no limiting law and reads as incremental. The router sends
it first to `ectheory-identification-strategy` (supply the limiting law and verify the assumptions are
primitive), then to `ectheory-contribution-framing` (re-lead the introduction with the theorem), then to
`ectheory-data-analysis` for a boundary-spanning Monte Carlo, and only then to `ectheory-submission` for the
single-PDF preflight. The order is deliberate: at a theorem-proof venue the math must be sound before any
framing or formatting work pays off. Confirm volatile process facts (length ceiling, submission system)
against the journal's current author guidelines as you reach the submission stage.


## Router pass for Econometric Theory

Treat this skill as an executable review pass, not a prose hint. First lock the primitive assumptions, theorem statement, proof route, and example showing why the result matters; then judge whether the current manuscript answers the venue's real reader: econometric theorists who read for assumptions, theorem novelty, proof architecture, and relation to known asymptotics.

- **Do the pass:** Run the pack as a sequence: fit gate, evidence gate, writing gate, source-map gate, and final output contract; stop when a gate lacks evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Econometrics for applied-method reach, Quantitative Economics for theoretical economics, Econometrica for general theory-plus-economics contribution; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Stage】topic / proof / framing / simulation / writing / submission / rebuttal
【Article type】Article or Miscellanea (and why)
【Bottleneck】one sentence
【Next skill】ectheory-...
```
