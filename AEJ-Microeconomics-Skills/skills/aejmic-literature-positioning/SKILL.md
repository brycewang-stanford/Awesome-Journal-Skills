---
name: aejmic-literature-positioning
description: Use when the contribution of an American Economic Journal: Microeconomics (AEJ: Micro) manuscript is fuzzy or oversold relative to the closest existing results. Stakes the theorem-relative delta against the nearest theory; it does not build the model (see aejmic-theory-model) or frame the prose (see aejmic-writing-style).
---

# Literature Positioning (aejmic-literature-positioning)

## When to trigger

- The literature review lists papers but never says **what is new here**
- The contribution is stated relative to "the literature" in the abstract rather than to a **specific closest result**
- A referee may ask "how is this different from [Author, Year]?" and you do not have a crisp answer
- The claim of novelty is broader than the result actually supports

## Positioning a theory result

For a theory-first journal, positioning is **theorem-relative**: identify the **closest existing result** and state precisely the **delta** — what your model relaxes, generalizes, characterizes, or overturns. Vague "we contribute to the literature on X" framing is the most common avoidable weakness. AEJ: Micro referees are subject-matter experts; they know the nearest theorem and will measure your delta against it.

### How to find and state the delta
1. **Name the closest result**, not a vague body of work: "Closest is [Author, Year], who shows P under assumptions A. We…"
2. **Classify the delta**: a *weaker assumption* (more general), a *new environment* (broader scope), a *full characterization* where prior work had a special case, an *impossibility* where prior work conjectured possibility, or a *mechanism* prior work missed.
3. **Right-size the claim**: state what you do **not** improve on, so the genuine advance is credible.
4. **Map the neighborhood**: 3–6 anchor results, each with one clause saying how you relate. Avoid citation padding.

### Sibling-literature discipline
Position against the **theory** frontier (mechanism design, IO theory, information economics, decision theory…), not against empirical applied-micro papers — that signals an AEJ: Applied framing. If your result has an empirical or experimental companion literature, cite it as motivation, not as the bar your contribution clears.

### The delta taxonomy (which kind do you have?)

| Delta type | What it looks like | What the reader must see |
|---|---|---|
| Weaker assumption | Same conclusion, fewer/looser hypotheses | The dropped assumption named; that the old proof breaks without your argument |
| New environment | Old mechanism, richer setting (search, networks, dynamics) | What the new setting adds that the old result could not capture |
| Full characterization | Prior work had a special case or sufficiency only | Both directions; the boundary of the characterization |
| Impossibility / no-go | Prior work conjectured or assumed possibility | The exact obstruction and which primitive causes it |
| New mechanism | Same phenomenon, different economic force | Why the new force is the right explanation |

State which row you are in **in the contribution paragraph** — a referee who cannot classify your delta will undervalue it.

### Independent and contemporaneous work
If a close result appeared independently and around the same time, acknowledge it explicitly and state the relationship (different method, complementary result, prior circulation date). Silence here reads as either ignorance or concealment to an expert referee.

## Checklist

- [ ] The **single closest result** is named, with its assumptions and conclusion
- [ ] The delta is classified (weaker assumption / new environment / characterization / impossibility / new mechanism)
- [ ] The contribution paragraph says what is **not** improved, bounding the claim
- [ ] 3–6 anchor papers, each with a one-clause relation; no padding
- [ ] Positioning is against the theory frontier, not an empirical literature
- [ ] Independent/contemporaneous work acknowledged where it exists

## Anti-patterns

- "We contribute to the literature on X" with no named closest result
- A wall of citations establishing breadth but never the delta
- Overclaiming generality the proof does not deliver
- Ignoring a known closer result a referee will immediately recall
- Positioning against empirical papers, signaling the wrong journal

## Worked vignette (illustrative)

A persuasion paper says it "extends the Bayesian-persuasion literature." A referee asks how it differs from the canonical single-sender result. The fix: "Closest is the single-sender concavification result; we relax commitment to *partial* commitment and characterize the sender-optimal signal, which coincides with full commitment only when the state space is binary." That one sentence is the delta — environment relaxed (partial commitment), full characterization, and an explicit scope limit (coincides only in the binary case).

## Output format

```
【Closest result】[Author, Year]: shows [P] under [assumptions A]
【Our delta】[weaker assumption / new environment / characterization / impossibility / new mechanism]
【Not improved】[explicit scope limit]
【Anchor map】3–6 papers, one clause each
【Frontier check】positioned against theory, not empirics? [Y/N]
【Next step】aejmic-theory-model (build/sharpen the result) or aejmic-writing-style (intro)
```
