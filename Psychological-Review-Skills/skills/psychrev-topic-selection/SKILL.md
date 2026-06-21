---
name: psychrev-topic-selection
description: Use when deciding whether an idea is a genuine theoretical problem with the scope and generality Psychological Review demands — and, critically, whether it is theory rather than an empirical report. Screens fit and frames the problem; it does NOT build the model (that is psychrev-theory-construction) or position it against rivals (psychrev-literature-positioning).
---

# Topic Selection & Theory-Fit Screening (psychrev-topic-selection)

## When to trigger

- You have an idea but are unsure it rises to a Psychological Review problem
- You have a rich empirical finding and are tempted to send it here
- You cannot say what existing theory *fails* to explain
- A collaborator asks "is this a Review paper or a JEP paper?"

## The first gate: is this theory at all?

Psychological Review is theory-only. Before anything else, run the **empirical-contribution
test**: if the manuscript's contribution is the *data* — a new effect, a better method, a
clean experiment — it is desk-rejected and redirected (to the JEP family, Psychological
Science, or a specialty venue). Data belong here only to **motivate** the problem or
**constrain** the theory. Ask:

- Could the paper survive if its data were replaced by *someone else's already-published*
  data? If yes, the contribution is the theory — good. If the paper collapses without *your*
  new experiment, it is empirical — wrong venue.
- Is the novelty a **phenomenon** or a **mechanism**? Review wants the mechanism.

## The second gate: is the problem big enough?

Review papers earn their length by **generality**. A theory that explains one paradigm in
one subfield rarely clears the bar; the journal prizes accounts that unify phenomena,
adjudicate between standing theories, or formalize something previously verbal. Screen on:

| Dimension          | Strong Review problem                              | Weak / wrong-venue                          |
|--------------------|---------------------------------------------------|---------------------------------------------|
| Generality         | Spans paradigms, tasks, or subfields              | One effect in one paradigm                  |
| Theoretical tension | Standing theories make conflicting predictions    | A gap that is merely unstudied              |
| Form of advance    | New mechanism / formal model / synthesis          | A new measure or a methodological fix       |
| What it replaces   | Names a prior account it improves on              | "No one has modeled this yet"               |
| Falsifiability     | Yields predictions that could be wrong            | Restates a phenomenon in new words          |

## Four routes onto the journal (pick one, name it early)

1. **New formal/computational model** of a phenomenon currently explained only verbally.
2. **New theoretical framework** (conceptual mechanism) that reorganizes a literature.
3. **Adjudication** between two or more standing theories using existing evidence and/or a
   formal contrast — a "systematic evaluation of alternative theories" (the journal's own phrasing).
4. **Major synthesis** that yields *new* theory (not a survey) — note this is the boundary
   with Psychological Bulletin; if you only summarize, it is Bulletin.

## Scoping questions to answer before building

- What is the **explanandum** — the precise set of phenomena the theory must account for?
- Which of those phenomena are **diagnostic** (rival theories disagree on them)?
- What existing data already exist to *constrain* the theory (so you need no new experiment)?
- Is the target a **process** (how) or only a **pattern** (what)? Review wants the how.

## Checklist

- [ ] The contribution is a theory/model, not a dataset (empirical-contribution test passed)
- [ ] The problem spans more than one paradigm or adjudicates standing theories
- [ ] A specific prior account the paper improves on is named
- [ ] The explanandum is stated as a concrete list of phenomena
- [ ] Existing (published) data suffice to motivate and constrain — no new experiment is the contribution
- [ ] The advance is a mechanism/formalism, not a measure or method
- [ ] The route onto the journal (model / framework / adjudication / synthesis) is explicit

## Anti-patterns

- Sending an empirical paper with a "theory" section bolted on — the defining desk-reject
- A "model" that is a redescription of the data with free parameters and no commitments
- A synthesis that only summarizes (that is Psychological Bulletin's lane)
- A problem so narrow it explains one effect in one task
- "No one has modeled X" offered as the contribution, with no phenomenon that demands a model
- Claiming generality the theory cannot deliver

## Output format

```
【Fit】theory not empirical (passed empirical-contribution test): yes / fix
【Route】new model | new framework | adjudication | synthesis
【Explanandum】[concrete list of phenomena the theory must explain]
【Prior account improved on】[named]
【Constraining data】[existing published data; no new experiment is the contribution]
【Next step】psychrev-literature-positioning (name rivals) → psychrev-theory-construction
```
