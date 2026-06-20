---
name: jep-accessibility-and-translation
description: Use when translating technical results, models, and methods into plain language for a Journal of Economic Perspectives (JEP) article — minimizing jargon and notation without dumbing down. Handles language and translation of ideas; defer evidence/number presentation to jep-evidence-without-equations and exhibits to jep-exhibits-for-general-readers.
---

# Accessibility & Translation (jep-accessibility-and-translation)

## When to trigger

- The draft reads like a working paper with the proofs deleted
- A labor or macro economist who doesn't work on the topic gets lost
- Sentences carry notation, estimator names, or subfield jargon a generalist won't know
- You worry that simplifying will make the piece sound shallow

## The JEP accessibility bar

JEP articles should be readable by **90 percent or more of the AEA membership** and useful to economists **not conversant with the author's subspecialty**; the journal is "scholarly without relying too heavily on mathematical notation," explaining ideas through **economic intuition** rather than derivations (检索于 2026-06；以官网为准). Translation is **not** simplification of the *ideas* — it is removing the *barriers* (notation, jargon, insider shorthand) that hide the ideas from a smart non-specialist.

## Translation moves (technical → JEP)

| Technical draft | JEP move |
|-----------------|----------|
| An estimating equation in the body | State what the equation *says* in words; the design goes to a note or appendix if at all |
| "We instrument X with Z" | "We exploit [the natural experiment] so that the variation in X is plausibly unrelated to [confounder]" |
| A Greek-letter parameter | Name the *economic quantity* it stands for and give its sign/magnitude in plain units |
| Subfield jargon ("the intensive margin," "MPC," "ATT") | Define on first use in a clause, or replace with plain words where precision allows |
| "Statistically significant at 1%" | A number with a plain sense of precision (see `jep-evidence-without-equations`) |
| A model's machinery | The *economic mechanism* — the story of what drives what — first; the formalism is optional scaffolding |

## Principles

- **Intuition first, formalism optional.** Lead with the mechanism in words. If notation appears at all, it follows the intuition and could be skipped without losing the thread.
- **Define on first use, sparingly.** Every necessary term gets a one-clause gloss the first time. Better: avoid the term.
- **Concrete over abstract.** A vivid example or a number anchors an abstract claim.
- **Don't condescend.** The reader is a professional economist, just not in your field — explain the *subfield-specific*, assume the *general*.
- **Cut insider signaling.** Citations-as-name-dropping, method-flexing, and "as is well known" add nothing for a generalist.

## Calibrating depth (not dumbing down)

The test is not "could a layperson read this" but "could a *non-specialist economist* follow the argument and trust it." Keep the rigor of the *reasoning*; remove the rigor-*display*. If a precise technical point is essential, state it plainly and put the formal version in a footnote or short appendix — the body must stand on its own.

## Checklist

- [ ] No estimating equations or proofs in the body (intuition in words instead)
- [ ] Every subfield term defined on first use or replaced
- [ ] Each Greek/parameter symbol replaced by the economic quantity it denotes
- [ ] A non-specialist economist can restate the main mechanism after one read
- [ ] No method-flexing or citation name-dropping
- [ ] Necessary technical precision moved to a note/appendix, body self-contained
- [ ] Simplified language did not silently weaken or overstate a claim (cross-check `jep-balance-and-objectivity`)

## Worked vignette (illustrative)

A working-paper sentence reads: "We identify β via a shift-share instrument, exploiting Bartik-style variation in local labor demand, and recover an IV estimate that survives the Borusyak–Hull exogeneity diagnostics." The JEP translation: "To separate cause from coincidence, we lean on the fact that some towns were more exposed to a **national hiring boom** simply because of the industries they happened to host — exposure that had little to do with anything local. Comparing more- and less-exposed towns lets us read off how the boom changed wages." The mechanism and the credibility are now legible to any economist; the estimator name and diagnostics, if needed at all, go to a footnote.

## Anti-patterns

- "Translating" by deleting the math but keeping the jargon — still unreadable
- Dumbing down the *ideas* instead of removing the *barriers* (loses rigor and respect)
- Leaving one estimating equation "for the experts" in an otherwise accessible body
- Defining nothing because "everyone knows this" — they don't, across fields
- Over-simplifying into vagueness so the claim no longer means anything checkable

## Output format

```
【Jargon/notation removed】[list of terms translated or cut]
【Mechanism in plain words】[one paragraph]
【Equations/proofs relocated】[to note / appendix / cut]
【Non-specialist read test】can a general economist restate it? [Y/N]
【Rigor preserved?】reasoning intact, only display removed? [Y/N]
【Next step】jep-evidence-without-equations
```
