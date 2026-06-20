---
name: jfm-internet-appendix
description: Use when working on internet appendix for a Journal of Financial Markets manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Internet Appendix (jfm-internet-appendix)

## When to trigger
- The manuscript is aimed at **Journal of Financial Markets (JFM)** and internet appendix is the active bottleneck.
- A coauthor asks whether the draft meets the journal's market microstructure, asset pricing, liquidity, trading, and financial-market design standard.
- The paper risks being confused with nearby venues: Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| microstructure mechanism is central | Make the microstructure mechanism assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| liquidity measurement is central | Make the liquidity measurement assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| trading venue design is central | Make the trading venue design assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| price discovery is central | Make the price discovery assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| high-frequency evidence is central | Make the high-frequency evidence assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JFM fit notes

- Publisher / owner context: Elsevier.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: microstructure mechanism, liquidity measurement, trading venue design, price discovery, high-frequency evidence.
- Sibling boundary: Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science.
- House-style aim: precise institutional detail, clean market data, and careful measurement of frictions.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/journal-of-financial-markets
- https://www.elsevier.com/journals/journal-of-financial-markets/1386-4181/guide-for-authors

## Stage-specific moves

1. State the exact internet appendix question in one sentence.
2. Identify which JFM audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jfm-writing-style` if the stage passes, or back to `jfm-workflow` if it does not.

## Checklist
- [ ] The JFM audience can see why the paper belongs in market microstructure, asset pricing, liquidity, trading, and financial-market design.
- [ ] The draft distinguishes JFM from Journal of Finance, Journal of Financial Economics, Review of Financial Studies.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for internet appendix names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Market, firm, or asset identifiers are documented enough to audit sample construction.
- [ ] Internet appendix material has a clear map from each table to the main claim.

## Anti-patterns
- Submitting a paper that is merely adjacent to JFM without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Financial Markets
【Skill】jfm-internet-appendix
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking internet appendix
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Finance, Journal of Financial Economics
【Source status】verified URL / 待核实 / not asserted
【Next skill】jfm-writing-style
```
