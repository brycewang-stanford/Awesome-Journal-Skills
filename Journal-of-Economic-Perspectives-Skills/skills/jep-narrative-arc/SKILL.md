---
name: jep-narrative-arc
description: Use when structuring a Journal of Economic Perspectives (JEP) article as a story/argument for a general economist reader rather than a literature survey. Builds the essay's spine (hook → tension → synthesis → takeaways); it does not handle sentence-level voice or evidence presentation.
---

# Narrative Arc for JEP (jep-narrative-arc)

## When to trigger

- The draft is organized like a survey ("Section 2 reviews X, Section 3 reviews Y")
- A reader can't say what the *argument* is, only what topics are covered
- The piece has no hook and no payoff — it informs but does not move
- You have takeaways from the proposal but no through-line connecting them

## The JEP arc

A JEP article is an **essay with an argument**, not a catalog. The reliable arc for a broad economist audience:

1. **Hook** — a concrete puzzle, surprising fact, vivid example, or live debate that a non-specialist immediately feels. Open with the *question*, never with "the literature on X is large."
2. **Stakes / "why now"** — why this matters and why now, in a paragraph anyone in the AEA can follow.
3. **Tension** — the central disagreement, puzzle, or shift the article will resolve or illuminate. Synthesis is interesting only when there is something *at issue*.
4. **Synthesis** — the body: organized by *ideas and the argument's logic*, not by paper or by author. Each section advances the through-line; evidence is recruited to the argument (see `jep-evidence-without-equations`), competing views are weighed (see `jep-balance-and-objectivity`).
5. **What we don't know** — honest open questions; JEP readers trust an author who marks the edges of knowledge.
6. **Takeaways** — the 3–5 memorable points (from the proposal) landed explicitly. The reader should be able to repeat them at a seminar.
7. **Brief close** — the broader lesson and why it travels beyond the immediate setting.

> Organize by **argument**, not by **literature**. "Three forces explain the puzzle" beats "Author A found…, Author B found…". The papers serve the argument; the argument does not serve the papers.

## Structural tests

- **The elevator test:** can you state the through-line in one sentence? If not, there is no arc yet.
- **The section-title test:** do section titles name *ideas* ("Why the effect fades over time") rather than *topics* ("The empirical literature")? Idea-titles signal an argument.
- **The deletion test:** could a section be cut without breaking the argument? If yes, it's a survey appendage, not a load-bearing beam.
- **The takeaway test:** does each takeaway clearly emerge from a section? Orphan takeaways mean the body and the conclusion disagree.

## Symposium-aware structuring

If the article is part of a symposium, its arc should occupy its **assigned angle** and gesture to the companion pieces rather than re-cover their ground — the symposium, not the single article, carries the full picture. Confirm scope with `jep-editor-strategy`.

## Checklist

- [ ] Opens with a hook (puzzle/fact/example/debate), not "the literature on…"
- [ ] Central tension stated early — there is something at issue
- [ ] Body organized by ideas/argument, not by paper or author
- [ ] Through-line stateable in one sentence (elevator test)
- [ ] Section titles name ideas, not topics
- [ ] "What we don't know" section present
- [ ] 3–5 takeaways land explicitly and each traces to a section
- [ ] Close states the lesson that travels

## Anti-patterns

- A literature-review skeleton ("Section 2: prior work") masquerading as an article
- No hook; opening with definitions or a history of the field
- Synthesis with no tension — a tour of findings that resolves nothing
- Burying the takeaways or never stating them
- Hiding all uncertainty to make the argument look cleaner (also a balance failure)
- In a symposium piece, re-covering a companion article's territory

## Output format

```
【Through-line (one sentence)】[...]
【Hook】[puzzle / fact / example / debate]
【Tension】[what is at issue]
【Body sections (idea-titled)】1) … 2) … 3) …
【What we don't know】[...]
【Takeaways (3–5)】[...]
【Lesson that travels】[...]
【Next step】jep-accessibility-and-translation
```
