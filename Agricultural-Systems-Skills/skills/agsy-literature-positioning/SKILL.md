---
name: agsy-literature-positioning
description: Use when positioning an Agricultural Systems (AgSy) manuscript against the literature so it reads as a systems contribution. AgSy readers span agronomy, modelling, livestock, economics, environment, and food-system science, so the paper must engage the systems and modelling literatures they expect — not only one subfield. Stakes the contribution; it does not write the lit review.
---

# Literature Positioning (agsy-literature-positioning)

AgSy is read by a **systems-science** audience that spans crop and livestock modelling, whole-farm and
bio-economic analysis, sustainability assessment, and food-system science. Positioning is therefore not
throat-clearing — the paper must show it advances the **systems and modelling** conversation, not just
add another data point to one subfield.

## When to trigger

- Drafting or revising the introduction and the "contribution" paragraph
- A reviewer said you "ignored the relevant modelling work" or "don't engage the systems debate"
- Your agronomic or model results are solid but the framing reads as single-discipline
- You need to distinguish your contribution from the closest prior systems studies / models

## How AgSy wants the literature engaged

1. **Engage the systems debate, not a citation pile.** Identify the open systems question — an
   unresolved trade-off, a contested mechanism, a model limitation, a scaling gap — that your paper
   addresses. Cite the works that *define* it.
2. **Two literatures at once.** The **domain** literature (the crop/livestock/farm/food system you
   study) **and** the **methods** literature (the model family, calibration/evaluation, sensitivity,
   trade-off analysis). AgSy reviewers expect both.
3. **Locate your model among existing models.** Why this model and not the standard alternatives
   (APSIM/DSSAT/STICS, whole-farm/bio-economic, ABM, integrated assessment)? What does yours add?
4. **Name the gap precisely.** Not "little is known" — say what is mismodelled, untested across scales,
   or missing a trade-off, and why resolving it advances systems understanding.
5. **Pre-empt the obvious objection.** Acknowledge the strongest rival explanation or competing model
   and say how your design/evaluation adjudicates it (hand off to `agsy-data-and-model-evaluation`).

## Cross-system engagement (a distinctive AgSy demand)

| If your paper is… | also engage… |
|-------------------|--------------|
| a crop-model application | the whole-farm / trade-off literature it feeds into |
| a whole-farm or bio-economic study | the process-model and the economic/decision literatures |
| a landscape/regional analysis | the aggregation/emergence and land-use-competition literature |
| a food-system study | the production, environment, and policy literatures it connects |

## Worked micro-example: locating one contribution (illustrative)

A bioeconomic study of climate adaptation positions itself in two literatures at once:

- *Domain:* mixed crop–livestock adaptation studies, citing the works that frame the margin–environment
  trade-off as unresolved at farm scale.
- *Methods:* whole-farm bioeconomic modelling, naming why this model is chosen over a crop-only
  simulator (it represents the herd–manure–rotation feedback the trade-off depends on).
- *Gap, stated precisely:* prior models hold feed price exogenous and so cannot show how price shocks
  reshape land use — not "little is known."
- *Strongest rival:* a regional integrated-assessment paper, whose scale hides the farm-level feedback
  this study isolates and evaluates.

## Referee pushback → the AgSy-specific fix

- *"You ignored the relevant modelling work."* → Add the methods literature (model family, calibration,
  trade-off analysis), not just the domain papers.
- *"The contribution reads as incremental."* → Name the specific systems gap (a mismodelled interaction,
  an untested scale) your design closes.

## Anti-patterns

- A "literature dump" with no organizing systems question
- Engaging only the agronomy literature and ignoring the modelling/evaluation literature (or vice versa)
- Not situating your model among the standard model families
- Strawmanning prior models, or hiding the closest competing study
- Claiming "first to model" when the contribution is incremental


## Positioning pass for Agricultural Systems

Run this as a concrete capability pass. First lock the system boundary, actor decision, model/data linkage, and sustainability or food-security tradeoff; then test whether the manuscript addresses agricultural-systems reviewers who expect crop, farm, value-chain, environment, and policy components to be connected rather than listed.

- **Primary move:** Build a three-column map: incumbent conversation, unresolved tension, and this manuscript's delta; include one sibling-venue omission that would make a referee doubt the fit.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Field Crops Research for plot-level agronomy, Global Food Security for policy synthesis, Agricultural Economics for economics-first work; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Systems debate】the open trade-off / mechanism / scaling / model gap
【Key works】the 3-6 that define it (domain + methods)
【Model landscape】where your model sits among alternatives
【Gap】what is mismodelled / untested across scales / missing a trade-off
【Move】how this paper changes the systems conversation
【Strongest rival】and how evaluation will adjudicate it
【Next】agsy-systems-framing-and-modeling
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — model families and systems data sources
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AgSy scope and interaction-centered remit
