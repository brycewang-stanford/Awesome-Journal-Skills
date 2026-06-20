---
name: jams-submission
description: Use when working on submission preflight for a Journal of the Academy of Marketing Science manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Submission Preflight (jams-submission)

## When to trigger
- The manuscript is aimed at **Journal of the Academy of Marketing Science (JAMS)** and submission preflight is the active bottleneck.
- A coauthor asks whether the draft meets the journal's marketing strategy, consumer behavior, channels, branding, innovation, and marketing theory standard.
- The paper risks being confused with nearby venues: Journal of Marketing, Journal of Marketing Research, Marketing Science, and Journal of Consumer Research.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| marketing strategy is central | Make the marketing strategy assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| customer response is central | Make the customer response assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| brand mechanism is central | Make the brand mechanism assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| managerial relevance is central | Make the managerial relevance assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| marketing theory is central | Make the marketing theory assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JAMS fit notes

- Publisher / owner context: Springer for the Academy of Marketing Science.
- Submission route to re-check: Springer Nature submission.
- Signature vocabulary: marketing strategy, customer response, brand mechanism, managerial relevance, marketing theory.
- Sibling boundary: Journal of Marketing, Journal of Marketing Research, Marketing Science, and Journal of Consumer Research.
- House-style aim: marketing scholarship with clear managerial implications and theory contribution.
- Official URLs currently used by the pack:
- https://link.springer.com/journal/11747
- https://www.springer.com/journal/11747/submission-guidelines

## Stage-specific moves

1. State the exact submission preflight question in one sentence.
2. Identify which JAMS audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jams-review-process` if the stage passes, or back to `jams-workflow` if it does not.

## Checklist
- [ ] The JAMS audience can see why the paper belongs in marketing strategy, consumer behavior, channels, branding, innovation, and marketing theory.
- [ ] The draft distinguishes JAMS from Journal of Marketing, Journal of Marketing Research, Marketing Science.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for submission preflight names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to JAMS without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of the Academy of Marketing Science
【Skill】jams-submission
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking submission preflight
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Marketing, Journal of Marketing Research
【Source status】verified URL / 待核实 / not asserted
【Next skill】jams-review-process
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
