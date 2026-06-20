---
name: imfer-rebuttal
description: Use when working on rebuttal strategy for a IMF Economic Review manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Rebuttal Strategy (imfer-rebuttal)

## When to trigger
- The manuscript is aimed at **IMF Economic Review (IMFER)** and rebuttal strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's international macroeconomics, finance, development, policy, exchange rates, sovereign risk, and IMF-relevant evidence standard.
- The paper risks being confused with nearby venues: Journal of International Economics, JIMF, JMCB, and Economic Policy.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| international macro is central | Make the international macro assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| sovereign risk is central | Make the sovereign risk assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| capital-flow policy is central | Make the capital-flow policy assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| IMF policy audience is central | Make the IMF policy audience assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| macro-financial stability is central | Make the macro-financial stability assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## IMFER fit notes

- Publisher / owner context: Springer Nature for the International Monetary Fund.
- Submission route to re-check: Springer Nature submission.
- Signature vocabulary: international macro, sovereign risk, capital-flow policy, IMF policy audience, macro-financial stability.
- Sibling boundary: Journal of International Economics, JIMF, JMCB, and Economic Policy.
- House-style aim: policy-facing international macro evidence with transparent country coverage and model assumptions.
- Official URLs currently used by the pack:
- https://link.springer.com/journal/41308
- https://www.springer.com/journal/41308/submission-guidelines

## Stage-specific moves

1. State the exact rebuttal strategy question in one sentence.
2. Identify which IMFER audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `imfer-rebuttal` if the stage passes, or back to `imfer-workflow` if it does not.

## Checklist
- [ ] The IMFER audience can see why the paper belongs in international macroeconomics, finance, development, policy, exchange rates, sovereign risk, and IMF-relevant evidence.
- [ ] The draft distinguishes IMFER from Journal of International Economics, JIMF, JMCB.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for rebuttal strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Identification or model assumptions are separated from policy interpretation.
- [ ] Robustness checks are organized by threat, not by a mechanical appendix list.

## Anti-patterns
- Submitting a paper that is merely adjacent to IMFER without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】IMF Economic Review
【Skill】imfer-rebuttal
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking rebuttal strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of International Economics, JIMF
【Source status】verified URL / 待核实 / not asserted
【Next skill】imfer-rebuttal
```
