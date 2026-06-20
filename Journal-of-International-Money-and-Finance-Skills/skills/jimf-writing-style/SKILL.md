---
name: jimf-writing-style
description: Use when working on writing style for a Journal of International Money and Finance manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Writing Style (jimf-writing-style)

## When to trigger
- The manuscript is aimed at **Journal of International Money and Finance (JIMF)** and writing style is the active bottleneck.
- A coauthor asks whether the draft meets the journal's international finance, exchange rates, global banking, capital flows, and open-economy macro-finance standard.
- The paper risks being confused with nearby venues: Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| exchange-rate pass-through is central | Make the exchange-rate pass-through assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| capital-flow shocks is central | Make the capital-flow shocks assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| global financial cycle is central | Make the global financial cycle assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| sovereign risk is central | Make the sovereign risk assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| cross-border banking is central | Make the cross-border banking assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JIMF fit notes

- Publisher / owner context: Elsevier.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: exchange-rate pass-through, capital-flow shocks, global financial cycle, sovereign risk, cross-border banking.
- Sibling boundary: Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics.
- House-style aim: international-finance identification that respects exchange-rate regimes and cross-country comparability.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/journal-of-international-money-and-finance
- https://www.elsevier.com/journals/journal-of-international-money-and-finance/0261-5606/guide-for-authors

## Stage-specific moves

1. State the exact writing style question in one sentence.
2. Identify which JIMF audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jimf-submission` if the stage passes, or back to `jimf-workflow` if it does not.

## Checklist
- [ ] The JIMF audience can see why the paper belongs in international finance, exchange rates, global banking, capital flows, and open-economy macro-finance.
- [ ] The draft distinguishes JIMF from Journal of International Economics, Journal of Monetary Economics, JMCB.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for writing style names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Market, firm, or asset identifiers are documented enough to audit sample construction.
- [ ] Internet appendix material has a clear map from each table to the main claim.

## Anti-patterns
- Submitting a paper that is merely adjacent to JIMF without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of International Money and Finance
【Skill】jimf-writing-style
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking writing style
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of International Economics, Journal of Monetary Economics
【Source status】verified URL / 待核实 / not asserted
【Next skill】jimf-submission
```
