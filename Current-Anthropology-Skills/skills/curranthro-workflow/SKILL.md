---
name: curranthro-workflow
description: Use when starting or navigating any Current Anthropology (CA) manuscript as the entry point. Routes to the right CA sub-skill based on lifecycle stage, subfield (sociocultural, archaeology, biological, linguistic), and article type (Major Article under the CA✩ Treatment, Report, Forum, Discussion/Comment). It dispatches; it does not draft content.
---

# CA Workflow Router (curranthro-workflow)

The orchestrator for a *Current Anthropology* submission. Figure out the **stage**, the **subfield**,
and the **article type**, then send the user to the matching skill. CA is the transnational, all-fields
journal **published by the University of Chicago Press for the Wenner-Gren Foundation**, and its defining
feature is the **CA✩ Treatment**: an accepted Major Article is circulated to invited commentators whose
**signed Comments are published alongside it**, followed by the **author's Reply**. The router's first
job is to make sure the work is built to *survive and reward* that public, multi-voice scrutiny.

## When to trigger

- Starting a new CA paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits (Major Article vs. Report vs. Forum vs. Discussion/Comment)
- Returning with a decision letter or with **published Comments to reply to** (route to `curranthro-rebuttal`)

## First questions: subfield and article type

| Situation | Article type | Route to |
|-----------|--------------|----------|
| Field-shaping theoretical/methodological intervention, broad reach | **Major Article** (6,000–10,000 words) → gets the **CA✩ Treatment** | normal pipeline below |
| Sharp finding, provocation, or new framework, shorter | **Report** (3,000–5,000 words) | `curranthro-topic-selection` + `curranthro-data-analysis` |
| Curated multi-author debate on a pressing issue | **Forum** | `curranthro-topic-selection` + `curranthro-writing-style` |
| Critique/reply to a CA piece from the last ~8 months | **Discussion / Comment** (≤ 800 words) | `curranthro-rebuttal` + `curranthro-writing-style` |
| Bridging academic and applied work | **Current Applications** (open-access section) | `curranthro-topic-selection` |

> CA spans all subfields: **sociocultural, archaeology, biological/physical, linguistic** (plus
> ethnohistory, prehistory, applied). Method and ethics demands differ by subfield — name yours before
> routing (see `curranthro-research-design`). Only **Major Articles** get the full CA✩ commentary.

## Routing map (stage → skill)

```text
Idea / fit / article type?       → curranthro-topic-selection
Where does it sit in the field?  → curranthro-literature-positioning
What's the conceptual argument?  → curranthro-theory-building
Is the fieldwork/design sound?   → curranthro-research-design
Is the analysis/inference sound? → curranthro-data-analysis
Are exhibits clear & ethical?    → curranthro-tables-figures
Does it read across the fields?  → curranthro-writing-style
Ethics, consent, accountability? → curranthro-transparency-and-data
How does CA✩ review work?        → curranthro-review-process
Ready to submit?                 → curranthro-submission
Got Comments / an R&R?           → curranthro-rebuttal
```

## Default order

`topic-selection → literature-positioning → theory-building → research-design → data-analysis →
tables-figures → writing-style → transparency-and-data → review-process → submission → rebuttal`

Iterate: ethnographic and theory-driven papers loop theory ↔ fieldwork ↔ interpretation many times, and
the **ethics-and-accountability** check (`curranthro-transparency-and-data`) should run *early* and again
before submission. The **CA✩** logic also runs throughout — from `topic-selection` onward, ask "who are
my likely commentators, and what will they attack?"

## CA✩ fit check (run before routing to the next skill)

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Reach | A scholar in another subfield (e.g., a linguist reading an archaeology paper) can state why it matters to anthropology writ large. | `curranthro-topic-selection` |
| Commentary worthiness | The argument is bold and synthetic enough that international commentators would have something substantive to debate. | `curranthro-theory-building` |
| Mode honesty | The method (ethnographic, archival, material, lab) is defended in its own idiom, not forced into a quantitative template. | `curranthro-research-design` |
| Ethics of care | Consent, anonymization, heritage/repatriation obligations have an explicit plan. | `curranthro-transparency-and-data` |

If the paper fails the reach or commentary-worthiness check, do not route to writing-style — a CA Major
Article that no one would bother commenting on is not yet a CA Major Article.

## Anti-patterns

- Treating CA like a one-subfield outlet — the Major Article should reach all of anthropology
- Forgetting the **CA✩ Treatment** exists: writing a paper that cannot withstand published, signed Comments
- Confusing CA with its siblings: it is **not** *American Anthropologist* (AAA flagship, no comment apparatus), *American Ethnologist*, or *Cultural Anthropology* — CA is **Wenner-Gren-sponsored** and defined by the comment-and-reply format
- Forcing ethnographic/interpretive work into a hypothesis-test template
- Deferring ethics, consent, and anonymization to the end (they are design decisions)

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / ethics / review / submit / reply
【Subfield】sociocultural / archaeology / biological / linguistic / ethnohistory-applied
【Article type】Major Article (CA✩) / Report / Forum / Discussion-Comment / Current Applications
【Route to】curranthro-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — anthropology data sources, archives, CAQDAS, lab/quant tooling by subfield
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official CA / Wenner-Gren / UChicago Press URLs behind every fact in this pack
