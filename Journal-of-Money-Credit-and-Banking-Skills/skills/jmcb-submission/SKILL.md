---
name: jmcb-submission
description: Use when working on submission preflight for a Journal of Money, Credit and Banking manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Submission Preflight (jmcb-submission)

## When to trigger
- The manuscript is aimed at **Journal of Money, Credit and Banking (JMCB)** and submission preflight is the active bottleneck.
- A coauthor asks whether the draft meets the journal's monetary economics, banking, credit markets, financial intermediation, and macro-finance standard.
- The paper risks being confused with nearby venues: Journal of Monetary Economics, Review of Economic Dynamics, Journal of Finance, and Journal of Financial Intermediation.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| monetary transmission is central | Make the monetary transmission assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| bank balance sheets is central | Make the bank balance sheets assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| credit frictions is central | Make the credit frictions assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| central-bank relevance is central | Make the central-bank relevance assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| macro-finance identification is central | Make the macro-finance identification assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JMCB fit notes

- Publisher / owner context: Wiley for the Ohio State University Department of Economics.
- Submission route to re-check: Wiley online submission.
- Signature vocabulary: monetary transmission, bank balance sheets, credit frictions, central-bank relevance, macro-finance identification.
- Sibling boundary: Journal of Monetary Economics, Review of Economic Dynamics, Journal of Finance, and Journal of Financial Intermediation.
- House-style aim: policy-relevant macro-finance evidence with transparent timing and institutional detail.
- Official URLs currently used by the pack:
- https://onlinelibrary.wiley.com/journal/15384616

## Stage-specific moves

1. State the exact submission preflight question in one sentence.
2. Identify which JMCB audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jmcb-referee-strategy` if the stage passes, or back to `jmcb-workflow` if it does not.

## Checklist
- [ ] The JMCB audience can see why the paper belongs in monetary economics, banking, credit markets, financial intermediation, and macro-finance.
- [ ] The draft distinguishes JMCB from Journal of Monetary Economics, Review of Economic Dynamics, Journal of Finance.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for submission preflight names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Market, firm, or asset identifiers are documented enough to audit sample construction.
- [ ] Internet appendix material has a clear map from each table to the main claim.

## Anti-patterns
- Submitting a paper that is merely adjacent to JMCB without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Money, Credit and Banking
【Skill】jmcb-submission
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking submission preflight
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Monetary Economics, Review of Economic Dynamics
【Source status】verified URL / 待核实 / not asserted
【Next skill】jmcb-referee-strategy
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
