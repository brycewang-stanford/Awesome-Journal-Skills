---
name: geb-contribution-framing
description: Use when the "what does this advance in game theory?" sentence is missing or muddy for a Games and Economic Behavior (GEB) manuscript. Forges the single-sentence contribution and the introduction's claim structure so the Editor in Charge sees the advance immediately.
---

# Contribution Framing (geb-contribution-framing)

## When to trigger

- The introduction lists what you did but never states what is *new for game theory*
- A reader finishes the intro unsure whether to be impressed
- The contribution is buried under setup, notation, or related work
- You are about to write the cover letter and need a crisp claim

## Why framing decides the desk screen

At GEB the chief editor routes each paper to one of **seven Editors** as the **Editor in Charge**, who can desk-reject before any referee sees it — about **one-third of submissions are desk-rejected**. That Editor is a game theorist reading many papers; the advance must be unmistakable in the abstract and first page. With only **~15%** of submissions ultimately published, a paper whose contribution is implicit competes poorly against one that states it plainly. Framing is not spin — it is making a real advance legible fast.

## The GEB contribution sentence

Write one sentence of the form:

> "We show that [class of games / setting] admits [result], which [generalizes / overturns / characterizes / mechanizes] [prior understanding], implying [consequence for theory or applications]."

Then test it:

- **Is it about game theory?** The payoff must be to the theory or its methods, not only to an application domain.
- **Is it falsifiable-sized?** A specific theorem/mechanism/finding, not "we study X."
- **Does it name the advance verb?** Generalize, weaken an assumption, characterize, prove impossibility, identify a behavioral mechanism, etc.
- **Would a non-specialist game theorist care?** GEB's audience spans sub-fields and adjacent disciplines.

## Structure the claim cascade

1. **Headline claim** — the one sentence above, early in the intro.
2. **Why it was open** — the obstacle that left this unresolved.
3. **The key idea** — the one move (construction, technique, design, experiment) that cracks it.
4. **Scope of the advance** — how general; what it does and does not cover.
5. **Implications** — for theory, for mechanism design, or for applications (CS/EC, biology, behavior).

## Anti-patterns

- "We study a model of ..." with no claimed result in the intro
- A contribution that is really an application contribution dressed as theory
- Three competing "main" contributions with no ranking
- Overstating generality the proofs do not support (referees will check)
- Saving the contribution sentence for the conclusion

## Output format

```
【Contribution sentence】"We show that ... which ... implying ..."
【Advance verb】generalize / characterize / impossibility / mechanism / behavioral-ID
【Game-theory payoff】explicit? [Y/N]
【Claim cascade】headline / why-open / key idea / scope / implications present? [Y/N each]
【Over-claim flags】[...]
【Next step】geb-identification-strategy
```
