---
name: soctheory-theory-construction
description: Use when building the actual theory for a Sociological Theory (ST) manuscript — turning a positioned problem into defined concepts, explicit mechanisms, internally consistent propositions, and scope conditions. Constructs the theory; it does NOT stress-test the argument's validity against rivals (soctheory-argument-development) or set the domain limits (soctheory-boundary-conditions).
---

# Theory Construction: Concepts, Mechanisms, Propositions (soctheory-theory-construction)

## When to trigger

- The problem and tradition are set; now you must build the theory
- You have propositions but no defined concepts underneath them
- Your relationships are asserted, not derived from a mechanism
- The theory's internal pieces do not yet hang together consistently

## The build order

ST theory is assembled in a disciplined sequence. Skipping a step is the most common reason a
draft reads as "assertions, not theory." This is **theory construction** in Abend's formal
sense (ST 2008, 26(2):173–199) — the explicit work of making concepts and their relations.

1. **Define the concepts.** For each new or re-specified concept: a precise definition, its
   **extension** (what it includes and, crucially, excludes), and how it differs from neighboring
   concepts. A concept that overlaps an existing one without distinction will be challenged as a
   relabel. Sociological theory lives or dies on conceptual clarity.
2. **State the assumptions.** What must be true about actors, situations, and the social world
   for the theory to operate (e.g., a Bourdieusian field assumes positions, capital, and stakes;
   a pragmatist account assumes habit interrupted by problem-situations)? Make them explicit;
   hidden assumptions are where reviewers attack.
3. **Specify the mechanism.** The *how/why* — the social process that makes the relationship
   hold. Sociological mechanisms are the engine: how individual action aggregates, how a
   situation channels conduct, how meaning is enacted. A proposition without a mechanism is a
   correlation-in-waiting, not theory. (Cf. mechanism-based theorizing in contemporary ST.)
4. **Derive the propositions.** Each proposition is a theoretical claim that *follows from* the
   concepts + mechanism. Number them (P1, P2…). Each must be preceded by the reasoning that
   earns it — the proposition is the summary of an argument, not a bullet.
5. **Check internal consistency.** Do the propositions contradict one another? Does a later
   one quietly require an assumption you ruled out? Internal consistency is to ST what
   statistical validity is to ASR. (Validity against rivals is handled in
   `soctheory-argument-development`.)
6. **Hold the level of analysis.** Micro / meso / macro: keep it consistent, or theorize the
   transitions (the micro-macro link) deliberately rather than sliding across levels by accident.

## Concept definition template

For each concept, fill:

- **Label** (one term, used consistently throughout)
- **Definition** (one or two precise sentences)
- **Extension** — included instances / excluded instances
- **Distinction** — how it differs from the nearest existing concept
- **Level** (individual / interactional / organizational / field / societal)

## Proposition discipline

- A proposition states a *relationship between concepts*, not an empirical magnitude.
- Every proposition is preceded by its reasoning; the proposition summarizes an argument already made.
- Keep them theoretical (P: "the more A, the more likely B, because mechanism M"), never
  operational ("A measured by a scale predicts B at p<.05").
- Never write "H1" or "supported / not supported" — that is ASR/AJS vocabulary. A proposition
  should be **examinable in principle** but you do no testing here.
- Data, if used, is **illustrative**: a case shows the concept at work; it does not confirm it.

## Worked anchor (real ST exemplar)

Timmermans & Tavory, "Theory Construction in Qualitative Research: From Grounded Theory to
Abductive Analysis" (ST 2012, 30(3):167–186), is itself a theory of *how theory is constructed*
— it specifies abduction as the mechanism by which surprising observations generate new
theoretical claims. Study how it defines its central concepts and ties each move to an explicit
inferential mechanism rather than to data.

## Checklist

- [ ] Every concept has a definition, an extension, and a distinction from neighbors
- [ ] All assumptions are stated explicitly
- [ ] Each relationship is driven by a named social mechanism (the how/why)
- [ ] Propositions are numbered and each is earned by a preceding argument
- [ ] The propositions are internally consistent (no two contradict; none smuggles a ruled-out premise)
- [ ] Level of analysis is consistent, or level transitions are theorized
- [ ] No empirical claims ("data show…") stand in for theoretical ones

## Anti-patterns

- Propositions stated as bullets with no preceding reasoning
- A new concept that is an old concept with a new name (a relabel)
- "X affects Y" with no specified mechanism
- Assumptions left implicit, then exposed by reviewers
- Sliding across levels of analysis without theorizing the link
- Smuggling in empirical claims — at ST data is illustrative, never a test

## Output format

```
【Concepts】[name: definition / extension / distinction / level] for each
【Assumptions】[explicit list]
【Mechanisms】[concept → concept : the social process that makes it hold]
【Propositions】P1…Pn (each with one-line mechanism)
【Internal consistency】checked: yes / issues: [...]
【Next step】soctheory-argument-development (validity + rivals) → soctheory-boundary-conditions
```
