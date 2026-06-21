---
name: psychrev-boundary-conditions
description: Use when setting the scope of a Psychological Review theory — what it explains, what it does NOT, and (for formal models) whether its parameters are identifiable. Bounds the theory; it does NOT derive its predictions (psychrev-argument-development) or frame its advance over rivals (psychrev-contribution-framing).
---

# Boundary Conditions, Scope & Identifiability (psychrev-boundary-conditions)

## When to trigger

- Your theory reads as if it explains everything (a red flag to reviewers)
- You have not said where the theory stops holding
- For a formal model: you have not checked whether distinct parameter settings are distinguishable
- A reviewer will ask "what would falsify this?" or "can you even estimate that parameter?"

## Why scope is a contribution, not a confession

At Psychological Review, stating where a theory holds and where it fails is part of the theory
itself, not a limitations paragraph tacked on at the end. A theory that "explains everything"
explains nothing — unbounded scope signals an unfalsifiable model. Editors read explicit
boundaries as a sign of theoretical maturity. Three kinds of limit must be stated.

### 1. Scope (the explanatory boundary)

- **Phenomena in scope** vs. **phenomena explicitly out of scope** (left to other processes).
- **Population / domain limits** — does the theory claim to hold across development, species,
  cultures, tasks, or only within a stated range?
- **Level of analysis** — computational, algorithmic, or implementational (Marr); be consistent,
  and theorize level shifts rather than sliding between them.
- **Conditions of breakdown** — name the regime where the mechanism should stop producing the
  phenomena, and treat that prediction as a test of the theory.

### 2. Identifiability (for formal/computational models)

This is the modeling-specific boundary reviewers probe hardest:

- **Structural identifiability** — can the parameters, in principle, be recovered from the kind
  of data the theory addresses, or do different settings produce identical predictions (a
  *mimicry* problem)?
- **Parameter recovery** — demonstrate, by simulation, that fitting the model to data it
  generated recovers the true parameters; report where recovery degrades.
- **Model mimicry** — can your model and a rival mimic each other on the available data? If so,
  the comparison is not diagnostic; say what data *would* separate them.
- **Sloppiness / sensitivity** — note parameters the predictions barely depend on (and resist
  over-interpreting them).

### 3. What it does NOT explain

A short, explicit list of phenomena the theory deliberately does not address, with one line
each on why (out of scope vs. genuinely open). This pre-empts the "but it can't handle Y"
reviewer objection by conceding Y on your own terms.

## Checklist

- [ ] Phenomena in scope and explicitly out of scope are both listed
- [ ] Population/domain/level limits are stated (development, species, culture, task, Marr level)
- [ ] A breakdown regime is named and treated as a test, not a disclaimer
- [ ] (Formal) structural identifiability is discussed; mimicry risk addressed
- [ ] (Formal) parameter recovery is demonstrated by simulation, with degradation noted
- [ ] (Formal) data that *would* separate the model from a mimicking rival are specified
- [ ] A short "what this theory does not explain" list is included with reasons

## Anti-patterns

- A theory presented as universal, with no stated breakdown condition
- Boundary conditions written as apologies ("a limitation is...") rather than as theory
- Skipping identifiability for a model with many free parameters
- Claiming parameters are meaningful without ever showing they can be recovered
- Ignoring that a rival model mimics yours on the available data
- Burying scope limits in a final paragraph instead of theorizing them up front

## Output format

```
【In scope】[phenomena explained]
【Out of scope】[phenomena left to other processes, with reasons]
【Domain limits】[development / species / culture / task / Marr level]
【Breakdown regime】[where the mechanism should stop — stated as a test]
【Identifiability】structural: ok/at-risk | recovery: demonstrated/degraded where [...] | mimicry: [rival], separating data: [...]
【Does NOT explain】[short explicit list]
【Next step】psychrev-conceptual-exhibits (diagram + simulation figures) → psychrev-contribution-framing
```
