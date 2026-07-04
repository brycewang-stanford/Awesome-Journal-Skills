---
name: sci-framing
description: Use when locking the conceptual advance and the "why now" before drafting for Science (AAAS) — converts a correct result into a Science-shaped narrative that leads with the broad advance rather than the background, and seeds the title, abstract, and cover letter.
---

# Advance Framing (sci-framing)

## When to trigger

- The science is solid but the manuscript reads like a lab report.
- The introduction opens with three paragraphs of background before the contribution.
- Reviewers/colleagues say "so what?" or "I don't see what's new."
- You can state the result but not the *lesson*.

## The one-sentence advance

Force the entire paper into a single sentence of the form:

> "We show that **[surprising, general claim]**, which means **[consequence for a broad field]**."

If you cannot fill both brackets without jargon, the framing is not ready. This sentence seeds the one-sentence summary (`sci-abstract`), the cover letter (`sci-cover-letter`), and the last line of the intro.

## Science introduction shape (≈3 short paragraphs)

1. **The gap that matters broadly** — what the community has been unable to do/explain, stated so a non-specialist grasps the stakes. One paragraph, not a literature dump.
2. **Why it has been hard / why now** — the obstacle, and what (new tool, idea, dataset, scale) finally makes it tractable. This is the "why now" that journalists and editors look for.
3. **What we did and found** — the advance, in plain terms, ending on the broad implication. The reader should know your result before the Results section.

## The "why now" checklist

Editors favor work that is timely. Name explicitly which applies:

- [ ] A new method/instrument made the impossible measurable.
- [ ] A new dataset/scale reached a threshold that changes conclusions.
- [ ] A field-wide controversy is ripe for resolution.
- [ ] A theoretical prediction is now testable.
- [ ] A real-world event (pandemic, climate milestone) makes it urgent.

If none apply, the work may be correct but not *Science-timely* → revisit `sci-fit`.

## Worked micro-rewrite: opening paragraph

**Before (background-first, field-internal):**

> "The Wnt signaling pathway has been extensively studied since its

- **Declarative and specific** beats vague and grand. "X regulates Y by Z" > "Insights into the regulation of Y."
- Avoid "Towards", "A study of", "Investigating", "Novel".
- Keep it parseable by a non-specialist; the noun phrase should carry the advance.
- Science titles are short (often < 90 characters). No question marks unless the question is the point.

## Narrative anti-frames (rewrite these)

| Anti-frame                                      | Reframe                                              |
|-------------------------------------------------|-----------------------------------------------------|
| "We applied method M to system S."              | "We discovered that S does X — revealed by M."      |
| "Little is known about…"                        | "Whether [specific question] has been unresolved because…" |
| "Our results are consistent with…"              | "Our results decide between competing models, favoring…" |
| Chronological lab-notebook order                | Logical order toward the single claim               |

## Worked example: reframing a solid-but-narrow result

*Raw finding:* a new cryo-EM structure of a bacterial transporter, resolved at 2.9 Å, showing an unexpected occluded state.

- **Method-led (rejectable) frame:** "We determined the structure of transporter T by cryo-EM and observed a new conformation." — a specialist result; a physicist would not read it.
- **Advance-led (Science-shaped) frame:** "We show that transporter T captures substrate through a previously unseen occluded state, revealing a general gating mechanism shared across the superfamily — which means models of secondary active transport must include an intermediate step." — the claim now generalizes beyond one protein and carries a lesson for the whole field.

The move is not spin: the occluded state and the superfamily conservation must be *in the data*. Framing surfaces the general claim the evidence already supports; it never manufactures one (if it would, return to `sci-fit`).

## Editor/referee expectation checklist for framing

- [ ] The first 150 words contain the advance, stated so a non-specialist grasps the stakes.
- [ ] The "why now" is explicit and matches one of the five triggers below — editors screen for timeliness.
- [ ] The general claim is demonstrated by a specific result, not asserted in the closing paragraph.
- [ ] The title is declarative and parseable by an outside-field editor.
- [ ] No superlatives doing the work that data should ("unprecedented", "paradigm-shifting").

## Output format

```
【One-sentence advance】 "We show that ... which means ..."
【Why-now trigger】 which of the 5 applies
【Intro 3-paragraph skeleton】 gap / why-now / advance+implication
【Working title】 declarative, < 90 chars
【Risk】 is the implication demonstrated or asserted? (link back to sci-fit if asserted)
【Next】 sci-writing
```

## Anti-patterns

- **Do not** bury the advance below the fold; the broad claim belongs in the first 150 words.
- **Do not** inflate with "novel/unprecedented/paradigm-shifting" — show, don't label.
- **Do not** frame around the method when the discovery is the point (method-led framing is for methods journals).
