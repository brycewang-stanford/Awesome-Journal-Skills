---
name: etp-review-process
description: Use when working on review process for a Entrepreneurship Theory and Practice manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Review Process (etp-review-process)

## When to trigger
- The manuscript is aimed at **Entrepreneurship Theory and Practice (ETP)** and review process is the active bottleneck.
- A coauthor asks whether the draft meets the journal's entrepreneurship theory, new ventures, founder teams, entrepreneurial finance, ecosystems, and family business standard.
- The paper risks being confused with nearby venues: Journal of Business Venturing, Strategic Entrepreneurship Journal, Research Policy, and Academy of Management Journal.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| venture formation is central | Make the venture formation assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| founder team is central | Make the founder team assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| entrepreneurial ecosystem is central | Make the entrepreneurial ecosystem assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| opportunity process is central | Make the opportunity process assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| startup finance is central | Make the startup finance assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## ETP fit notes

- Publisher / owner context: SAGE for Baylor University.
- Submission route to re-check: SAGE / ScholarOne submission.
- Signature vocabulary: venture formation, founder team, entrepreneurial ecosystem, opportunity process, startup finance.
- Sibling boundary: Journal of Business Venturing, Strategic Entrepreneurship Journal, Research Policy, and Academy of Management Journal.
- House-style aim: entrepreneurship theory with credible venture-level evidence and boundary conditions.
- Official URLs currently used by the pack:
- https://journals.sagepub.com/home/etp
- https://journals.sagepub.com/author-instructions/ETP

## Stage-specific moves

1. State the exact review process question in one sentence.
2. Identify which ETP audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `etp-rebuttal` if the stage passes, or back to `etp-workflow` if it does not.

## Checklist
- [ ] The ETP audience can see why the paper belongs in entrepreneurship theory, new ventures, founder teams, entrepreneurial finance, ecosystems, and family business.
- [ ] The draft distinguishes ETP from Journal of Business Venturing, Strategic Entrepreneurship Journal, Research Policy.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for review process names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to ETP without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Entrepreneurship Theory and Practice
【Skill】etp-review-process
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking review process
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Business Venturing, Strategic Entrepreneurship Journal
【Source status】verified URL / 待核实 / not asserted
【Next skill】etp-rebuttal
```
