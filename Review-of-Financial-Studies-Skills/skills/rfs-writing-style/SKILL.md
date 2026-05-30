---
name: rfs-writing-style
description: Use as a late-stage polish when prose, contribution framing, or the abstract/introduction is the bottleneck for a The Review of Financial Studies (RFS) manuscript. Sharpens exposition; does NOT change the empirics, identification, or results.
---

# Writing & Contribution Framing (rfs-writing-style)

## When to trigger

- The abstract or introduction buries what is new
- Prose is dense, over-hedged, or jargon-heavy
- The contribution is implied but never stated as a crisp claim
- The paper is technically done and needs a final exposition pass

> Run this only after identification, robustness, and exhibits hold up. Do not polish prose around an unsettled result.

## How RFS papers read

The best RFS papers make the **new question and the answer legible in the first two pages**. Reviewers decide early whether the paper is novel and credible; the writing's job is to make both obvious without overselling. RFS welcomes theory + empirics, so the prose must integrate them, not present a model and then an unrelated regression.

### The introduction formula (RFS-style)
1. **Hook**: the first-order question and why it matters now (one paragraph).
2. **What we do**: the design and data, in one paragraph — name the source of variation.
3. **What we find**: the headline result *with magnitude*, then the key robustness in a clause.
4. **Why it is new**: the explicit delta vs. the closest work (from `rfs-literature-positioning`).
5. **Mechanism / interpretation**: what the result means for theory or practice.
6. **Roadmap**: brief; one or two sentences.

### Abstract
- Lead with the question and the finding, not the literature.
- State the design and the headline magnitude.
- End with the contribution / implication.
- No undefined acronyms; no "we study the relationship between."

### Prose discipline
- Active voice; one idea per sentence; define each term once.
- Report **economic magnitudes** in interpretable units, not only significance.
- Integrate theory and evidence: state the prediction, then the test, then the result.
- Calibrate claims: "consistent with" vs. "demonstrates" vs. "suggests" — match the evidence.
- Cut hedging stacks ("may possibly suggest that perhaps").

## Checklist

- [ ] Abstract leads with question + finding + magnitude, not literature
- [ ] Introduction states the delta vs. the closest paper explicitly
- [ ] Headline result appears with economic magnitude on page 1–2
- [ ] Theory and empirics are integrated, not sequential and disconnected
- [ ] Claims are calibrated to the strength of the evidence (no overselling)
- [ ] Jargon and acronyms defined on first use; no undefined symbols
- [ ] Hedging reduced; active voice; one idea per sentence

## Anti-patterns

- An abstract that opens "The literature has long debated ..." and never states the finding.
- Burying the contribution in the conclusion.
- A model in Section 2 and a regression in Section 4 with no logical bridge.
- Reporting "highly significant" effects whose magnitude is economically trivial.
- Over-claiming causality the design does not support.
- A 1.5-page roadmap paragraph.

## Output format

```
【Abstract】leads with question+finding+magnitude? yes/no
【Intro delta】explicit vs. closest paper? yes/no
【Magnitude on p.1–2】yes/no
【Theory–empirics integration】tight / loose
【Overselling risk】[claims to recalibrate]
【Next step】rfs-submission
```
