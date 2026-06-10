---
name: geb-topic-selection
description: Use when judging whether a game-theory result is the right fit and scale for Games and Economic Behavior (GEB) — does it advance the frontiers of game theory and its applications? Tests the idea against GEB's specialist-but-general-interest bar before the paper is built out.
---

# Topic Selection (geb-topic-selection)

## When to trigger

- You have a model or experiment but are unsure it is "GEB-sized"
- The result is correct but feels incremental over a known theorem
- You are deciding between GEB and a field outlet (theory, behavioral, CS/EC venue)
- A referee or colleague said "true, but so what?"

## The GEB fit bar

GEB is the **leading specialist game-theory journal** and an official journal of the **Game Theory Society** (Elsevier; founded 1989 by Ehud Kalai; chief editor Hervé Moulin since 2021). The defining test is not general-economics policy interest — it is whether the work **significantly advances the frontiers of game theory and its applications**. The scope is deliberately broad across **methods**: equilibrium theory, mechanism and market design, behavioral game theory, learning and dynamics, and experimental/empirical work — and broad across **fields** that use game theory: economics, political science, biology, computer science, mathematics, and psychology. The audience is a general game-theory readership, so the contribution must be legible and interesting beyond one narrow sub-literature.

Selectivity is explicit and high: about **one-third of submissions are desk-rejected**, and only **~15%** are eventually published. The Editor in Charge will desk-reject papers judged to have no chance of meeting the publication criterion. That makes "what does this teach game theory that we did not know?" the first-page question.

## Fit tests (a GEB paper usually clears several)

- **Conceptual advance:** a new solution concept, a sharper characterization, a new class of games, an existence/uniqueness result, or a unifying framework.
- **Mechanism / design advance:** a new mechanism, an impossibility/possibility result, an optimal or constructive design.
- **Behavioral advance:** a model or experiment that changes how strategic behavior is understood, well-identified against alternatives.
- **Generality / surprise:** the result holds more broadly than expected, or overturns an intuition.
- **Cross-field reach:** game-theoretic content that speaks to CS/EC, biology, or political science — common at GEB, but it must still be a *game-theory* contribution.

## Anti-patterns

- A correct but routine extension ("Theorem 1 with one more player") with no new insight
- An applied paper that *uses* a game but contributes nothing to game theory itself (better at a field journal)
- A pure CS/EC conference result reframed with no added generality or economic interpretation
- Over-claiming a narrow special case as a general theory


## Fit pass for Games and Economic Behavior

Treat this skill as an executable review pass, not a prose hint. First lock the primitives, equilibrium concept, comparative statics, and proof or experiment boundary; then judge whether the current manuscript answers the venue's real reader: game theorists who ask what the model teaches beyond a clever example.

- **Do the pass:** Score the manuscript on venue fit, novelty, evidence readiness, and audience ownership; reject a prestige-only target when a sibling venue owns the contribution more directly.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JET for theory abstraction, Theoretical Economics for compact theory contribution, Experimental Economics for experiment-first designs; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Result type】theory / mechanism design / behavioral / experiment / cross-field
【Advance to game theory】one sentence — what we did not know before
【Fit tests cleared】[conceptual / design / behavioral / generality / cross-field]
【Desk-reject risk】low / medium / high — why
【Verdict】GEB-fit / borderline / better elsewhere
【Next step】geb-literature-positioning
```
