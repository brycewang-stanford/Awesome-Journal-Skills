---
name: proghg-comprehensiveness-and-balance
description: Use when calibrating completeness vs. selectivity and ensuring fair, reflexive engagement across theoretical traditions, authors, and debates in a Progress in Human Geography (PiHG) review — including not over-promoting the author's own work or position. Audits coverage and even-handedness; it does not design the framework (proghg-organizing-framework) or write prose (proghg-writing-style).
---

# Comprehensiveness & Balance (proghg-comprehensiveness-and-balance)

## When to trigger

- The conceptual framework is set and you are filling cells with the literature
- You are unsure whether to cite *everything* or curate
- The subfield has rival theoretical traditions, a live political debate, or conflicting framings
- You are a contributor to this literature and worry the review tilts toward your own work or position

## Completeness vs. selectivity: the PiHG contract

A PiHG review must be **comprehensive in coverage** yet **selective and critical in emphasis**. The reader should trust that nothing important is missing, while the prose foregrounds the interventions that move the debate. Resolve the tension by **tiering** the corpus:

| Tier | Treatment |
|------|-----------|
| **Field-defining interventions** | engaged critically in the text — what they reframed and their limits |
| **Important contributions** | grouped and weighed within the framework's cells; cited with their conceptual move |
| **Confirmatory / extending** | cited in clusters ("see also …") to show coverage without bloating prose |
| **Tangential** | cited only where they bear on a specific claim; not every adjacent work belongs |

Comprehensiveness is proven by the *citation set* (the saturation log from `proghg-literature-synthesis`); selectivity is exercised in the *prose*. A review that summarizes every work at equal length has abdicated the critical judgment that is its value.

## Fair, reflexive engagement across traditions

PiHG is a **state-of-the-art** appraisal: its account of a debate becomes the discipline's shared reference. Human geography is also a politically and theoretically plural discipline, so balance is reflexive, not merely "neutral":

- **Steelman every tradition.** State each theoretical position's strongest case in terms its proponents would accept *before* critiquing it. Refute positions at their best, never their worst.
- **Respect theoretical pluralism.** Human geography runs on political-economic, feminist, poststructural, postcolonial, more-than-human, and quantitative/GIScience traditions; weigh interpretive, critical, and quantitative work each on its own terms rather than against a single yardstick. Dismissing a whole tradition is a classic PiHG balance failure.
- **Take a position without erasing rivals.** PiHG prizes argument, so you *should* say where you stand — but label it as your reading, lay out what divides the camps, and represent the others fairly. Position-taking is not partisanship.
- **Be reflexive about your own standpoint.** Where your theoretical or political commitments shape the appraisal, say so (see `proghg-transparency-and-reproducibility`); this is expected in a critical-geography review, not optional.
- **Attribute ideas correctly.** Credit originators of concepts and turns, not just popularizers — a recurring referee complaint, sharpened in a discipline attentive to whose contributions get erased.

## The self-citation trap

If you have published in the subfield, the review must **not** read as a retrospective of your program or a brief for your school. Guardrails:

- Your own work is cited at the tier its *importance to the field* warrants — no more.
- Rival traditions to your own are given their strongest statement.
- A reader who does not know who wrote the review cannot tell from the emphasis which camp the author belongs to.
- When the field disagrees with your position, say so plainly and represent the other side fairly.

## Checklist

- [ ] Corpus tiered (field-defining / important / confirmatory / tangential); prose emphasis matches tier
- [ ] Comprehensiveness provable from the citation set + saturation log
- [ ] Every rival tradition stated at its strongest before critique (steelman)
- [ ] Political-economic, feminist, poststructural, postcolonial, more-than-human, quantitative traditions each weighed on their own terms
- [ ] Conflicting framings reconciled by what-each-theorizes and credibility, not vote-counting
- [ ] Concept/turn attribution traces to originators
- [ ] Author's position taken openly *and* labelled as the author's reading; rivals represented fairly
- [ ] Reflexivity about the author's standpoint where it shapes the appraisal
- [ ] Self-citation audited: own work at field-warranted tier; rivals steelmanned; emphasis identity-blind
- [ ] No important author/tradition/turn an informed referee could say was slighted or omitted

## Anti-patterns

- Comprehensiveness theatre: equal-length summaries of every work (no critical judgment)
- Vote-counting conflicting findings instead of weighing what-each-theorizes and credibility
- Privileging one tradition and treating others as decorative (or dismissing quantitative work wholesale, or the reverse)
- Strawmanning the tradition the author disagrees with
- A review that doubles as the author's CV or as a manifesto for the author's school (the most-punished PiHG balance failures)
- Declaring a live debate "resolved" by assertion rather than laying out the conceptual state
- Crediting the popularizer of a concept over its originator

## Output format

```text
【Tiering】corpus split field-defining/important/confirmatory/tangential? Y/N
【Comprehensiveness evidence】saturation log + citation set support "nothing important missing"? Y/N
【Steelman】each rival tradition stated at its strongest? Y/N
【Tradition balance】political-economic/feminist/poststructural/postcolonial/more-than-human/quantitative each weighed fairly? Y/N
【Position-taking】author's reading stated and labelled; rivals represented fairly? Y/N
【Reflexivity】author's standpoint surfaced where it shapes the appraisal? Y/N
【Self-citation audit】own work at warranted tier; emphasis identity-blind? Y/N
【Next step】→ proghg-tables-figures (debate-mapping tables + conceptual figure)
```
