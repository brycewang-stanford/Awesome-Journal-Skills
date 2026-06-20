---
name: amanthro-workflow
description: Use when starting or navigating any American Anthropologist (AA) manuscript as the entry point. Routes to the right AA sub-skill based on lifecycle stage, subfield (sociocultural, archaeology, biological, linguistic), and section type (Research Article, Vital Topics Forum, World/Public/Multimodal Anthropologies, Review Essay). It dispatches; it does not draft content.
---

# AA Workflow Router (amanthro-workflow)

The orchestrator for an *American Anthropologist* submission. Figure out the **stage**, the
**subfield**, and the **section type**, then send the user to the matching skill. AA is the **four-field
AAA flagship** — the router's first job is to make sure the work reads as anthropology that speaks
across subfields, with reflexivity and an ethics of care built in from the start, not bolted on.

## When to trigger

- Starting a new AA paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **section** fits (full Research Article vs. a shorter forum/commentary)
- Returning with a decision letter (route to `amanthro-rebuttal`)

## First questions: subfield and section

| Situation | Section | Route to |
|-----------|---------|----------|
| Full original study, broad anthropological significance | **Research Article** (≤ 8,000 words) | normal pipeline below |
| Multi-voice debate on a pressing issue | **Vital Topics Forum** | `amanthro-topic-selection` + `amanthro-writing-style` |
| Anthropology produced outside the US/Anglophone center | **World Anthropologies** | `amanthro-topic-selection` + `amanthro-literature-positioning` |
| Engaged / activist / publicly-facing work | **Public Anthropologies** | `amanthro-topic-selection` + `amanthro-transparency-and-data` |
| Image / sound / film / installation as argument | **Multimodal Anthropologies** | `amanthro-tables-figures` + `amanthro-writing-style` |
| Assessing 2–5 recent books | **Review Essay** (≤ 5,000 words) | `amanthro-literature-positioning` |

> AA spans four fields: **sociocultural, archaeology, biological/physical, linguistic**, plus
> reflexive/public anthropology. The methods and the transparency/ethics demands differ by subfield —
> name yours before routing (see `amanthro-research-design`).

## Routing map (stage → skill)

```text
Idea / fit / section?            → amanthro-topic-selection
Where does it sit in the field?  → amanthro-literature-positioning
What's the conceptual argument?  → amanthro-theory-building
Is the fieldwork/design sound?   → amanthro-research-design
Is the analysis/inference sound? → amanthro-data-analysis
Are ethnographic exhibits clear? → amanthro-tables-figures
Does it read across the fields?  → amanthro-writing-style
Ethics, consent, accountability? → amanthro-transparency-and-data
How will it be judged?           → amanthro-review-process
Ready to submit?                 → amanthro-submission
Got an R&R / decision?           → amanthro-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: most ethnographic papers loop theory ↔ fieldwork ↔ interpretation many times, and the
**ethics-and-accountability** check (`amanthro-transparency-and-data`) should run *early* and again
before submission — consent and community accountability are designed in, not added at the end.

## Four-field routing check

Before selecting the next skill, force a one-minute AA fit check:

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Reach | A reader in another subfield (e.g., an archaeologist reading a linguistic paper) can state why it matters to anthropology. | `amanthro-topic-selection` |
| Mode honesty | The method (ethnographic, archival, material, lab, computational) is defended in its own idiom, not forced into a quantitative template. | `amanthro-research-design` |
| Reflexivity | Positionality and the author's relationship to the field/community are made explicit. | `amanthro-theory-building` |
| Ethics of care | Consent, anonymization, community accountability, and heritage/repatriation obligations have an explicit plan. | `amanthro-transparency-and-data` |

If the paper fails the reach check, do not route to writing-style — it needs a fit or theory repair,
because AA reviewers reject technically clean subfield papers that never become anthropological claims.

## Anti-patterns

- Treating AA like a single-subfield outlet — the contribution should reach four-field anthropology
- Forcing ethnographic/interpretive work into a hypothesis-test template (AA judges each mode on its own terms)
- Confusing AA with its AAA siblings: it is **not** *American Ethnologist* (sociocultural) or *Cultural Anthropology*, and not *Current Anthropology* with its CA✩ comment format
- Deferring ethics, consent, and anonymization to the end (they are design decisions)

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / ethics / review / submit / rebut
【Subfield】sociocultural / archaeology / biological / linguistic / reflexive-public
【Section】Research Article / Vital Topics Forum / World / Public / Multimodal / Review Essay
【Route to】amanthro-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — anthropology data sources, archives, CAQDAS, lab/quant tooling by subfield
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AA / AAA / Wiley URLs behind every fact in this pack
