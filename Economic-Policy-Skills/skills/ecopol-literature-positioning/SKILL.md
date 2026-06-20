---
name: ecopol-literature-positioning
description: Use when working on literature positioning for a Economic Policy manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Literature Positioning (ecopol-literature-positioning)

## When to trigger
- The manuscript is aimed at **Economic Policy (Economic Policy)** and literature positioning is the active bottleneck.
- A coauthor asks whether the draft meets the journal's policy-relevant economics papers written for an expert but broad policy audience standard.
- The paper risks being confused with nearby venues: AEJ Economic Policy, Journal of Public Economics, IMF Economic Review, and World Bank Economic Review.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| policy question is central | Make the policy question assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| European policy debate is central | Make the European policy debate assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| CEPR audience is central | Make the CEPR audience assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| welfare implication is central | Make the welfare implication assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| transparent counterfactual is central | Make the transparent counterfactual assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## Economic Policy fit notes

- Publisher / owner context: Oxford University Press / CEPR and partner institutions.
- Submission route to re-check: OUP submission.
- Signature vocabulary: policy question, European policy debate, CEPR audience, welfare implication, transparent counterfactual.
- Sibling boundary: AEJ Economic Policy, Journal of Public Economics, IMF Economic Review, and World Bank Economic Review.
- House-style aim: policy-first economics that states the decision problem, evidence, and limits plainly.
- Official URLs currently used by the pack:
- https://academic.oup.com/economicpolicy
- https://academic.oup.com/economicpolicy/pages/General_Instructions

## Stage-specific moves

1. State the exact literature positioning question in one sentence.
2. Identify which Economic Policy audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `ecopol-identification` if the stage passes, or back to `ecopol-workflow` if it does not.

## Checklist
- [ ] The Economic Policy audience can see why the paper belongs in policy-relevant economics papers written for an expert but broad policy audience.
- [ ] The draft distinguishes Economic Policy from AEJ Economic Policy, Journal of Public Economics, IMF Economic Review.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for literature positioning names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to Economic Policy without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Economic Policy
【Skill】ecopol-literature-positioning
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking literature positioning
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not AEJ Economic Policy, Journal of Public Economics
【Source status】verified URL / 待核实 / not asserted
【Next skill】ecopol-identification
```
