---
name: jegeo-writing-style
description: Use when the prose, intro, or abstract of a Journal of Economic Geography (JEG) manuscript must reach economists and geographers at once. Tunes voice, structure, and the 100-word abstract; it does not invent results.
---

# Writing Style (jegeo-writing-style)

## When to trigger

- The intro lands for one community but alienates the other — too much formalism for geographers, or too much narrative for economists
- The abstract is over the JEG limit or buries the spatial contribution
- The paper reads as "applied economics with maps" rather than economic geography
- Jargon from one tradition (NEG notation, or geography theory-speak) is unexplained for the other half of the audience

## Writing for two audiences without watering down

The hardest craft problem at JEG is that **every paragraph is read by an economist and a geographer**, and the masthead is drawn from both. The goal is not to dilute to a lowest common denominator but to make each move legible across the bridge:

- **Lead with the spatial economic question and its stakes**, in plain English, before any model or method. Both communities should agree on what the paper is about by the end of paragraph one.
- **Translate, don't drop, the technical apparatus.** A formal modeler should state the mechanism in prose before the equations; a conceptual theorist should give a concrete instance before the abstraction.
- **Name the mechanism, not just the result.** "Cities X because of agglomeration force Y, which weakens at distance" travels; "we find a significant coefficient" does not.
- **Respect both vocabularies but gloss them once.** If you use "relatedness," "embeddedness," or "spatial equilibrium," define it the first time so the other half of the room stays with you.

## The JEG intro arc

1. The spatial economic puzzle and why it matters (place does real work here).
2. What we knew — from *both* literatures — and the gap where they meet.
3. What you do (data/design/model) in two or three sentences, mechanism-first.
4. What you find, as a magnitude and a mechanism, not an asterisk.
5. Why it matters for how we understand the economy in space (and, where relevant, for policy — but argued, not asserted).

## The abstract (a hard constraint)

- **≤100 words** (检索于 2026-06；以官网为准), followed by **four keywords** and **JEL codes**. This is tighter than most economics journals — every word fights for space.
- Front-load the spatial contribution; name the place/scale, the mechanism, and the headline magnitude. No literature throat-clearing.
- It must read as economic geography to both communities in the first sentence.

## Prose discipline

- Active voice; one idea per paragraph; topic sentences that state the spatial claim.
- Magnitudes in interpretable units (per 10km, per region, percent of the gradient), not just coefficients.
- Keep the 8,000-word main text self-contained; the online appendix supports, it does not carry the argument (检索于 2026-06；以官网为准).
- Double-anonymous review: scrub self-identifying phrasing ("in our earlier work in [city]") from the prose, not just the title page.

## Where to put the model and the geography

A structural feature of JEG papers is deciding how much formal apparatus sits in the main 8,000 words versus the online appendix. The house solution that satisfies both communities:

- Keep in the main text the **mechanism, the key equation(s) that carry intuition, the identification argument, and the central maps/figures** — everything a geographer needs to follow the story and an economist needs to trust the design.
- Push to the online appendix the **full derivations, the complete parameter tables, secondary robustness, and method minutiae** — support, not argument.
- Never let the appendix carry a load-bearing claim; if a referee must open the appendix to believe the result, the main text has failed its self-containment test.

This keeps the paper readable across the bridge while respecting the length limit — and it is exactly the balance the editors look for.

## Checklist

- [ ] Paragraph one states the spatial economic question in plain English, no jargon
- [ ] Both literatures appear in the framing; the gap is where they meet
- [ ] Mechanism named in prose before any formal apparatus
- [ ] Technical terms from each tradition glossed once on first use
- [ ] Abstract ≤100 words, contribution-first, with four keywords + JEL
- [ ] Findings stated as magnitude + mechanism, never as bare significance
- [ ] Main text self-contained; appendix supports, not carries
- [ ] Self-identifying phrasing removed for double-anonymous review

## Anti-patterns

- An intro that only an economist (or only a geographer) can follow past page one
- Equations or notation dropped in with no prose statement of the mechanism
- Geography theory-speak or NEG jargon left unglossed for the other half of the audience
- An abstract that spends its 100 words on the literature instead of the contribution
- "We find significant effects" with no magnitude, mechanism, or spatial interpretation
- Leaving traces of authorship in the body text under a double-anonymous policy

## Worked vignette (illustrative)

An abstract opens: "Building on the new economic geography literature and recent advances in quantitative spatial models, this paper estimates a multi-region general equilibrium model with CES preferences to..." By word 30 a geographer has tuned out and no contribution has appeared. Rewritten contribution-first: "Where high-speed rail connects a region, manufacturing employment rises 7% — but neighboring unconnected regions lose 3%, so the network redistributes activity rather than creating it. We show this with a quantitative-spatial model disciplined by [data]." Now the place, mechanism, magnitude, and the net-vs-redistribution insight land in two sentences, legible to both communities, well under 100 words, with room for keywords and JEL.

## Translating across the bridge — concrete moves

- Replace "we exploit exogenous variation in W_ij" with "we use the fact that two regions' exposure was set by [pre-existing geography], unrelated to later outcomes" — then keep the formal version for the methods reader.
- Replace bare "path dependence" or "lock-in" with a one-clause gloss the first time ("path dependence — early advantages compounding into persistent regional specialization").
- After any equation block, add a sentence: "In words, this says..." so the non-modeling half of the audience stays.
- State every key magnitude in a unit a policymaker or geographer can picture (per 10km, per region, share of the gradient), not only as a coefficient.

## Output format

```text
【Journal】Journal of Economic Geography
【Skill】jegeo-writing-style
【Para-1 question】plain-English spatial puzzle? [Y/N]
【Two-audience legibility】mechanism in prose + terms glossed? [Y/N]
【Abstract】≤100 words, contribution-first, 4 keywords + JEL? [Y/N]
【Findings】magnitude + mechanism, no bare significance? [Y/N]
【Anonymity】self-identifying phrasing scrubbed? [Y/N]
【Next skill】jegeo-replication-package
```
