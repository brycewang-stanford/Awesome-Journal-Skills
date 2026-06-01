---
name: misq-theory-development
description: Use when building the theoretical engine of a MIS Quarterly manuscript — a behavioral mechanism and hypotheses, a design theory and testable design propositions for a design-science artifact, an economic mechanism for an economics-of-IS study, or an organizational process theory. Adapts the form of "theory" to the paper's IS tradition; does not run the analysis (misq-data-analysis) or frame the contribution (misq-contribution-framing).
---

# Theory Development (misq-theory-development)

## When to trigger

- Your claims are descriptive ("A is associated with B") with no IS mechanism
- You built an IT artifact but cannot say what *design knowledge* it embodies
- A Senior Editor or reviewer says "the theoretical contribution is unclear" or "this is a technical exercise"
- You need hypotheses or design propositions derived *before* you look at results

## Theory takes a different shape in each MISQ tradition

MISQ is pluralistic, so "develop theory" means different things. Pick the row that matches your tradition.

| Tradition | What "theory" means here | What you must produce |
|-----------|--------------------------|------------------------|
| **Behavioral** | A causal mechanism linking IT to cognition, behavior, or outcomes | A priori hypotheses with an explicit mechanism, boundary conditions, and any mediation/moderation logic |
| **Design science** | A *design theory*: the principles that make the artifact work | Justificatory (kernel) theory, design principles/requirements, and testable propositions about the artifact's utility |
| **Economics of IS** | An economic mechanism (incentives, information, matching, network effects) | A model or argument yielding signed, falsifiable predictions and an identification logic |
| **Organizational** | A process or variance theory of IT in context | Constructs, their relations, and the contextual conditions that govern them |

## Behavioral and economics: derive claims a priori

State the mechanism in words before the math: *what is the IT-enabled force, on whom, through what channel, and when does it reverse?* Then write hypotheses (behavioral) or comparative-statics predictions (economics) that follow from that mechanism. For mediation, theorize the channel; for moderation, theorize why the IT effect strengthens or weakens. Avoid HARKing — predictions precede results.

## Design science: ground the artifact in a design theory

A MISQ design-science contribution is not "we built a system." Anchor it in the Hevner, March, Park & Ram (2004) tradition: state the problem and its relevance, the kernel theory that justifies your design choices, the **design principles** that generalize beyond this one instantiation, and falsifiable propositions about utility you will later evaluate. The artifact is the vehicle; the prescriptive design knowledge is the contribution.

## Make boundary conditions explicit

IS effects are often contingent on the artifact, the user, the task, and the context. Name where the theory holds and where it breaks — reviewers reward a theorized scope condition over an over-claimed universal law.

## Checklist

- [ ] The tradition's correct *form* of theory is used (mechanism / design theory / economic model / process theory)
- [ ] The IT artifact is load-bearing in the mechanism, not decorative
- [ ] Hypotheses / design propositions / predictions are derived *before* results
- [ ] Mediation, moderation, or comparative statics are theorized, not just tested
- [ ] Boundary conditions and scope are stated
- [ ] For design science: kernel theory → design principles → testable utility propositions

## Anti-patterns

- "We applied [theory X] to [setting Y]" with no new IS mechanism — a borrowed-theory application.
- A design-science paper with an artifact but no generalizable design principles.
- Hypotheses that merely restate correlations the data already showed.
- Treating the IT artifact as an interchangeable "treatment."

## Output format

```
【Tradition & theory form】behavioral mechanism / design theory / economic model / process theory
【Core mechanism】IT-enabled force → on whom → through what channel
【Claims】H1..Hn / design propositions P1..Pn / signed predictions
【Boundary conditions】where it holds / reverses
【Next step】misq-literature-positioning or misq-methods
```
