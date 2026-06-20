---
name: wber-theory-model
description: Use when working on theory and model craft for a The World Bank Economic Review manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Theory and Model Craft (wber-theory-model)

## When to trigger
- The manuscript is aimed at **The World Bank Economic Review (WBER)** and theory and model craft is the active bottleneck.
- A coauthor asks whether the draft meets the journal's policy-relevant development economics, impact evaluation, institutions, trade, labor, agriculture, and poverty standard.
- The paper risks being confused with nearby venues: Journal of Development Economics, World Development, Economic Development and Cultural Change, and AEJ Applied.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| policy counterfactual is central | Make the policy counterfactual assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| program evaluation is central | Make the program evaluation assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| World Bank audience is central | Make the World Bank audience assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| developing-country data is central | Make the developing-country data assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| implementation margin is central | Make the implementation margin assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## WBER fit notes

- Publisher / owner context: Oxford University Press for the World Bank.
- Submission route to re-check: OUP / ScholarOne submission.
- Signature vocabulary: policy counterfactual, program evaluation, World Bank audience, developing-country data, implementation margin.
- Sibling boundary: Journal of Development Economics, World Development, Economic Development and Cultural Change, and AEJ Applied.
- House-style aim: development-policy evidence with transparent data construction and actionable interpretation.
- Official URLs currently used by the pack:
- https://academic.oup.com/wber
- https://academic.oup.com/wber/pages/General_Instructions

## Stage-specific moves

1. State the exact theory and model craft question in one sentence.
2. Identify which WBER audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `wber-robustness` if the stage passes, or back to `wber-workflow` if it does not.

## Checklist
- [ ] The WBER audience can see why the paper belongs in policy-relevant development economics, impact evaluation, institutions, trade, labor, agriculture, and poverty.
- [ ] The draft distinguishes WBER from Journal of Development Economics, World Development, Economic Development.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for theory and model craft names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to WBER without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】The World Bank Economic Review
【Skill】wber-theory-model
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking theory and model craft
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Development Economics, World Development
【Source status】verified URL / 待核实 / not asserted
【Next skill】wber-robustness
```
