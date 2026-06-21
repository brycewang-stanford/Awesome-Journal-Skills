---
name: jedpsych-review-process
description: Use when you need to understand how the Journal of Educational Psychology evaluates a manuscript — masked peer review, editorial weighting of educational relevance, theory, design rigor (nesting/power), and transparency, desk-reject patterns, and the role of preregistration and JARS. Use when stress-testing a paper before submission or interpreting a decision letter. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (jedpsych-review-process)

The Journal of Educational Psychology combines selectivity for **educational importance** with rigorous
methodological scrutiny. Under **masked review**, both author and reviewer identities are hidden, and
editors and expert reviewers weigh not only whether the finding is interesting but whether it is
**theoretically grounded**, **rigorously designed for its nested setting**, and **transparent**. Knowing
this lets you pre-empt the common rejection reasons.

## When to trigger

- Before submitting, to stress-test the manuscript
- Deciding whether to preregister and how to present transparency
- Interpreting a decision letter and setting expectations

## How review works

1. **Masked review.** Identities of authors and reviewers are masked; keep author identity out of the
   manuscript, exhibits, and repository links (see `jedpsych-submission`).
2. **Editorial triage.** The editor (and associate/handling editors) assesses scope fit (educational
   relevance + primary psychological research), theory, design rigor, and contribution; weak-fit or
   out-of-scope papers (e.g., single-instrument validation, pure evaluation) may be desk-rejected.
3. **Expert external review** assesses the theoretical contribution, the design and analysis (especially
   whether nesting/power are handled), the strength of the claim relative to the evidence, measurement
   quality, and transparency/JARS reporting.
4. **Transparency and standards are weighed.** The Transparency and Openness subsection, JARS compliance,
   and preregistration (encouraged) factor into the evaluation.
5. **Decisions.** Reject, revise and resubmit (often major), or accept; expect substantive revision and
   frequent requests for added rigor (multilevel modeling, mechanism tests), disclosure, or analyses.

## What gets a paper through

- Make **educational relevance** and the **theoretical mechanism** explicit early.
- Show the design is **rigorous for its setting** — nesting modeled, powered at the cluster level,
  validated measures, fidelity reported.
- Report **effect sizes with CIs and educational interpretation**; test the mechanism, not just the total
  effect.
- Disclose fully (JARS) and prepare the Transparency and Openness subsection; preregister where feasible.

## Desk-reject and decline patterns

The scope and rigor screens mean many manuscripts never reach full external review. Confirm current
categories on the journal's submission guidelines, but recognize these shapes:

| Pattern an editor sees | Likely outcome | Pre-empt it by |
|------------------------|----------------|----------------|
| Reliability/validity of one instrument | desk reject (scope) | reframe around a learning question or choose a measurement venue |
| Program evaluation with no psychological theory | desk reject / decline | foreground the learning/motivation mechanism and a mechanism test |
| Classroom study analyzed as if students independent | major revision or reject | refit a multilevel model; power at the cluster level |
| Lab effect with no educational bridge | scope concern | argue the instructional/policy implication or go elsewhere |
| Stars-only stats, no effect sizes/CIs | rigor flag | estimation-first reporting with educational interpretation |
| Identity leaks under masked review | returned to author | scrub names, sites, grant numbers, first-person self-cites |

## Worked micro-example (illustrative triage)

```
Manuscript: preregistered cluster-randomized reading trial (48 classrooms),
            multilevel model, effect size + CI + mediation, TOP subsection.
Editor read: educational relevance (classroom reading), theory (strategy
            instruction → monitoring), rigor (cluster-powered, nesting modeled),
            transparency (data/code with DOIs).
Likely route: external review, probable major R&R for added robustness/
            measurement detail.
Counter-case: same effect, single-level OLS on clustered data, no mechanism,
            "data on request" → likely declined or heavy revision.
```

## How reviewers weigh the evidence (calibration anchors)

- A design that **matches its nesting** (randomized, powered, and analyzed at the cluster level) is the
  single strongest methodological signal at JEP; ignoring clustering is a routine reason for rejection.
- A tested **mechanism** is what marks the paper as educational *psychology* rather than evaluation;
  reviewers reward a mediation/moderation result tied to theory.
- Transparency is part of credibility: a candid restricted-data statement with an access path reads better
  than silent opacity; preregistration quality (specific, dated, followed) strengthens the paper.

## Anti-patterns

- A finding with no clear educational implication or theoretical mechanism
- Clustered data analyzed as independent (the classic JEP methodological reject)
- Stars-only reporting without effect sizes, CIs, or educational meaning
- Weak or absent transparency / JARS reporting
- Expecting acceptance without a rigor- and disclosure-heavy R&R

## Output format

```
【Educational relevance】clear early? [Y/N]
【Theory + mechanism】grounded and tested? [Y/N]
【Design rigor】nesting modeled, cluster-powered, measures valid? [Y/N]
【Transparency + JARS】subsection + reporting standards strong? [Y/N]
【Masked】no identity leaks? [Y/N]
【Realistic outcome】reject / major R&R / minor R&R / accept
【Next】jedpsych-submission (or jedpsych-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — masked review, scope, JARS, and preregistration policy
