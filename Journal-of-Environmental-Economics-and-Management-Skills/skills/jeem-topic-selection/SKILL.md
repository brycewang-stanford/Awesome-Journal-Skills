---
name: jeem-topic-selection
description: Use when scoping or scope-testing a Journal of Environmental Economics and Management (JEEM) manuscript — confirming the environmental/resource mechanism is load-bearing and the question clears the field-journal bar before any analysis is finalized. Decides fit and routes; it does not invent evidence or citations.
---

# Topic Selection (jeem-topic-selection)

## When to trigger

- The paper is aimed at JEEM and you are not sure the **environmental or resource mechanism is doing the work** versus being a label on a generic applied-micro result
- A coauthor asks "is this JEEM, JAERE, JPubE, AEJ: Policy, or Ecological Economics?"
- The result is interesting but the **policy or welfare stakes** are not articulated
- The paper is a method/valuation exercise and you must show it speaks to a substantive environmental question, not just a technique

## Data first or question first

Environmental economics is data-rich — satellite imagery, sensor networks, administrative permit registries, parcel records — and that abundance tempts a "we have a great dataset, what can we estimate?" approach. JEEM rewards the reverse: a sharp environmental-economic *question* that the data then answer. A novel dataset is an asset only if it identifies a welfare-relevant parameter the field wants; on its own it is a desk-reject risk ("interesting data, no contribution"). Before committing, write the one-sentence question and the regulator-usable number it targets, then ask whether the data identify it — not the other way around.

## The JEEM fit test

JEEM is a **field** journal: the environmental, resource, or climate content is the point, and the economics must be credible. A paper passes the fit test only if the environmental mechanism is *necessary* to the contribution — remove it and the paper collapses. Run the question through these gates in order:

1. **Is the object environmental/resource-economic?** pollution & climate, energy, water, fisheries/forests/land, ecosystem services, environmental regulation & permits, or the **nonmarket value** of an environmental good. If the externality or resource is just a setting for a labor/IO/public-finance result, JEEM is the wrong field journal.
2. **Is there a welfare or policy stake?** JEEM rewards numbers a regulator could use — a marginal damage, a willingness-to-pay, a compliance cost, an abatement-cost curve, a resource rent. "X correlates with pollution" is not a JEEM contribution; "the marginal external cost of X is $Y, so the efficient tax is Z" is.
3. **Does the method clear the bar for its branch?** A causal claim needs a real design (not OLS + controls); a valuation needs a defensible preference-recovery argument; a theory paper needs a comparative static that bites.

## Branch-specific scoping

| Archetype | What makes it a JEEM paper | What makes it a desk-reject |
|-----------|----------------------------|------------------------------|
| Environmental-policy causal | a regulation/permit-market/standard generates clean variation; welfare or compliance-cost interpretation | reduced-form correlation with no design; environment is incidental |
| Revealed-preference valuation | hedonic/travel-cost recovers a WTP for a defined environmental amenity | a house-price regression with no amenity/welfare claim |
| Stated-preference valuation | CV/DCE elicits WTP for a policy-relevant good with credible survey design | a survey with no incentive compatibility or scope test |
| Resource/pollution theory | a model yields a testable or policy-relevant prediction about resource use or abatement | math with no environmental comparative static or empirical hook |
| Climate / damages | weather/climate variation maps to an economic outcome and adaptation margin | a climate-impacts paper with no economics (belongs in a science journal) |

## Sibling boundaries (be explicit in the paper)

- **vs. JAERE** — AERE's own journal and the closest substitute; JEEM is the older Elsevier flagship. Position on contribution, not prestige; do not claim "AERE official journal" status without checking current ownership (待核实).
- **vs. AEJ: Economic Policy / JPubE** — those reward the general policy/public-finance contribution; JEEM rewards the *environmental* mechanism and field audience.
- **vs. Ecological Economics** — that journal is pluralist/interdisciplinary; JEEM is neoclassical welfare economics.
- **vs. Nature Climate Change** — that is a science venue; JEEM needs the economics (preferences, welfare, optimization), not just an impact estimate.

## Worked vignette (illustrative)

A team has clean administrative data on a firm subsidy and finds it raised employment. They want to submit to JEEM because the firms happen to be in renewable energy. Run the fit test: the *object* is a labor/IO subsidy effect, the *welfare stake* is jobs not an environmental externality, and the *environmental mechanism is not load-bearing* — strip out "renewable" and the paper is unchanged. Verdict: reroute to a public-finance or labor venue. Contrast a version that estimates how the subsidy changed **abatement and emissions**, recovers the **implied cost per ton of CO2 abated**, and compares it to the social cost of carbon — now the environmental mechanism carries the contribution and a regulator-usable number emerges. That version is a JEEM paper.

## Short-paper route

JEEM accepts short papers / notes that make a contribution comparable to a full paper, with expedited review (检索于 2026-06；以官网为准; exact word ceiling 待核实). This route fits a sharp, single-result environmental contribution: a clean new estimate of one parameter, a decisive robustness correction to a published result, or a focused methodological note for valuation. If the contribution is one crisp number rather than a multi-part argument, scope it as a short paper rather than padding it to full length.

## The desk-reject self-test

Before investing, simulate the editor's scope screen with three blunt questions. (1) If I deleted the word "environmental/climate/pollution" from the title and abstract, would the paper still make sense as a labor/IO/public-finance paper? If yes, the mechanism is not load-bearing — reroute. (2) Can I state a number a regulator could use (a damage, a WTP, an abatement cost, a quota)? If no, there is no welfare contribution yet. (3) Is there a recent JEEM or JAERE paper a referee would say I am merely re-running on new data? If yes, find what I fix. Passing all three is the minimum bar before topic selection is settled.

## Checklist

- [ ] One sentence states the environmental/resource object and why it matters for policy or welfare
- [ ] Removing the environmental mechanism would collapse the contribution (it is load-bearing)
- [ ] The branch is named (policy-causal / RP valuation / SP valuation / theory / climate) and its method bar is met
- [ ] A regulator-usable parameter (damage, WTP, abatement cost, rent, elasticity) is the target, not a bare correlation
- [ ] The paper distinguishes itself from JAERE and from the general-interest / interdisciplinary siblings
- [ ] Short-paper route considered if the contribution is sharp but narrow (JEEM accepts short papers / notes)
- [ ] Process facts cited are in `resources/official-source-map.md` or marked 待核实

## Anti-patterns

- "Environmental" as a setting, not a mechanism — a generic DiD that happens to use a green outcome
- Estimating an effect with no welfare interpretation and no number a policymaker could use
- Picking JEEM for prestige when the audience is really public finance or development
- A pure climate-science impact paper with no economic model of behavior or welfare
- Asserting JEEM is "the AERE official journal" without verifying current ownership (待核实)

## Timeliness without chasing headlines

JEEM rewards questions that matter for current environmental policy — carbon pricing, air-quality regulation, water and fisheries management, climate adaptation, the energy transition — but it is a welfare-economics journal, not a news outlet. A topic earns durability when it pins down a parameter or mechanism that remains useful after the specific policy episode passes: the marginal damage of a pollutant, the WTP for an ecosystem service, the abatement-cost response to a price signal. Choose a question whose answer a regulator could cite in five years, not one that depends entirely on a fleeting policy debate. The best JEEM topics pair a salient policy context with a parameter of lasting interest.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-topic-selection
【Verdict】pass / revise / reroute
【Environmental mechanism】is it load-bearing? [Y/N] — one sentence
【Branch】policy-causal / RP-valuation / SP-valuation / theory / climate
【Policy-relevant target】damage / WTP / abatement cost / rent / elasticity
【Sibling boundary】why JEEM not JAERE / JPubE / Ecological Economics
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-literature-positioning
```
