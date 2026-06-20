---
name: finman-robustness
description: Use when working on robustness strategy for a Financial Management manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Robustness Strategy (finman-robustness)

## When to trigger
- The manuscript is aimed at **Financial Management (FM)** and robustness strategy is the active bottleneck.
- A coauthor asks whether the draft meets the journal's corporate finance, investments, market institutions, and applied financial decision-making standard.
- The paper risks being confused with nearby venues: Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| corporate policy is central | Make the corporate policy assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| capital structure is central | Make the capital structure assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| payout and investment is central | Make the payout and investment assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| governance channel is central | Make the governance channel assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| FMA audience is central | Make the FMA audience assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## FM fit notes

- Publisher / owner context: Wiley for the Financial Management Association.
- Submission route to re-check: Wiley online submission.
- Signature vocabulary: corporate policy, capital structure, payout and investment, governance channel, FMA audience.
- Sibling boundary: Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies.
- House-style aim: applied finance evidence that ties estimates to managerial or market decisions.
- Official URLs currently used by the pack:
- https://onlinelibrary.wiley.com/journal/1755053x
- https://www.fma.org/financial-management

## Stage-specific moves

1. State the exact robustness strategy question in one sentence.
2. Identify which FM audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `finman-tables-figures` if the stage passes, or back to `finman-workflow` if it does not.

## Checklist
- [ ] The FM audience can see why the paper belongs in corporate finance, investments, market institutions, and applied financial decision-making.
- [ ] The draft distinguishes FM from Journal of Corporate Finance, Journal of Banking, Finance.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for robustness strategy names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Market, firm, or asset identifiers are documented enough to audit sample construction.
- [ ] Internet appendix material has a clear map from each table to the main claim.

## Anti-patterns
- Submitting a paper that is merely adjacent to FM without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Financial Management
【Skill】finman-robustness
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking robustness strategy
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Corporate Finance, Journal of Banking
【Source status】verified URL / 待核实 / not asserted
【Next skill】finman-tables-figures
```
