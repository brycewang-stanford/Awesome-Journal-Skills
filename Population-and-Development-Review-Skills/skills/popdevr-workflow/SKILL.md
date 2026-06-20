---
name: popdevr-workflow
description: Use when starting or orienting any Population and Development Review (PDR, Wiley / Population Council) manuscript and unsure which skill applies — the entry-point router that dispatches to the right PDR sub-skill by lifecycle stage and article type (Research Article, Notes & Commentary, Data & Perspectives, Archives, Book Review). It dispatches; it does not draft content.
---

# Population and Development Review Workflow Router (popdevr-workflow)

The orchestrator for a *PDR* submission. Figure out the stage and the **article type**, then send the
user to the matching skill. PDR is the **Population Council's journal at the intersection of demography
AND development** — the router's first job is to confirm the paper connects **population dynamics**
(fertility, mortality, migration, ageing, structure) to **social, economic, or environmental change and
public policy**, with the big-picture reach PDR is known for, not a narrow estimate that merely uses
population data.

## When to trigger

- Starting a new PDR paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding which **article type** fits (Article vs. Notes & Commentary vs. Data & Perspectives)
- Returning with a decision letter (route to `popdevr-rebuttal`)

## First question: which article type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full original study or substantial synthetic/conceptual essay | **Research Article** (typically ~8,000–10,000 words) | normal pipeline below |
| Short, focused argument or response on a current population question | **Notes & Commentary** (short) | `popdevr-literature-positioning` + `popdevr-writing-style` |
| A new dataset, indicator, or interpretation of population statistics | **Data & Perspectives** | `popdevr-data-analysis` + `popdevr-transparency-and-data` |
| Archival population document or official-agency text with framing | **Archives** | `popdevr-writing-style` |
| Evaluative review of a population/development book | **Book Review** (usually invited) | `popdevr-writing-style` |

> Length is a norm, not a hard portal cap. Confirm current limits and types on the Wiley author page
> (see 待核实). PDR uses **Free Format** submission for the first round.

## Routing map (stage -> skill)

```text
Idea / fit (pop ↔ development)?      -> popdevr-topic-selection
Where does it sit in the field?      -> popdevr-literature-positioning
What's the argument/mechanism?       -> popdevr-theory-building
Is the design/method sound?          -> popdevr-research-design
Are the analyses sound?              -> popdevr-data-analysis
Are the exhibits clear?              -> popdevr-tables-figures
Does it read for a broad audience?   -> popdevr-writing-style
Data statement & sharing plan?       -> popdevr-transparency-and-data
How will it be judged?               -> popdevr-review-process
Ready to submit (ScholarOne)?        -> popdevr-submission
Got an R&R / decision?               -> popdevr-rebuttal
```

## Default order

`topic-selection -> literature-positioning -> theory-building -> research-design -> data-analysis ->
tables-figures -> writing-style -> transparency-and-data -> review-process -> submission -> rebuttal`

Iterate: PDR papers loop **theory ↔ design ↔ analysis** as the population-and-development argument
sharpens; a synthetic essay loops **literature-positioning ↔ theory-building ↔ writing-style** instead,
since its contribution is the framework, not a new estimate.

## Anti-patterns

- Treating PDR like a methods-forward demography journal (that is *Demography* / *Population Studies*) —
  PDR rewards the population-and-development connection and the broad-interest argument
- A pure estimation paper with no development, policy, or environment payoff
- A policy op-ed with no population-science grounding (PDR is peer-reviewed, not a magazine)
- Leaving the data availability statement and double-anonymization until acceptance

## Router pass for PDR

Run this as a concrete capability pass. First lock the population process, the development/policy
linkage, the data and time scale, the selection/measurement issue, and the uncertainty; then test
whether the manuscript addresses PDR's broad audience — demographers, economists, environmental and
policy scholars — who inspect both the population evidence and its development meaning.

- **Primary move:** Run the pack as fit gate, evidence gate, writing gate, source-map gate, and output
  contract; stop at the first gate that lacks evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch
  the manuscript directly.
- **Sibling comparison:** compare against *Demography* and *Population Studies* (methods-forward),
  *Population Research and Policy Review* (applied policy), and *Studies in Family Planning* (programs);
  if a neighbor has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for
  volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Stage】idea / positioning / theory / design / analysis / exhibits / writing / data / review / submit / rebut
【Type】Research Article / Notes & Commentary / Data & Perspectives / Archives / Book Review
【Route to】popdevr-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — population + development data sources and software by method
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official PDR URLs behind every fact in this pack
