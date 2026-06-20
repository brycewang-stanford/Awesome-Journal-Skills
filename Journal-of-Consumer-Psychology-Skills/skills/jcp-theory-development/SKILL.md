---
name: jcp-theory-development
description: Use when working on theory development for a Journal of Consumer Psychology manuscript. Provides journal-specific decision checks and handoff criteria; it does not invent evidence or citations.
---

# Theory Development (jcp-theory-development)

## When to trigger
- The manuscript is aimed at **Journal of Consumer Psychology (JCP)** and theory development is the active bottleneck.
- A coauthor asks whether the draft meets the journal's consumer psychology, judgment and decision-making, persuasion, emotion, identity, and consumption behavior standard.
- The paper risks being confused with nearby venues: Journal of Consumer Research, Journal of Marketing Research, Marketing Science, and Psychological Science.
- The team needs a source-backed handoff rather than generic journal advice.

## Core decision map

| Signal | What to inspect | Pass condition |
|--------|-----------------|----------------|
| consumer mechanism is central | Make the consumer mechanism assumption, measurement, and interpretation explicit | Evidence block 1 names the data, identifying variation, or conceptual logic |
| experimental manipulation is central | Make the experimental manipulation assumption, measurement, and interpretation explicit | Evidence block 2 names the data, identifying variation, or conceptual logic |
| psychological process is central | Make the psychological process assumption, measurement, and interpretation explicit | Evidence block 3 names the data, identifying variation, or conceptual logic |
| moderation logic is central | Make the moderation logic assumption, measurement, and interpretation explicit | Evidence block 4 names the data, identifying variation, or conceptual logic |
| consumer welfare is central | Make the consumer welfare assumption, measurement, and interpretation explicit | Evidence block 5 names the data, identifying variation, or conceptual logic |

## JCP fit notes

- Publisher / owner context: Elsevier for the Society for Consumer Psychology.
- Submission route to re-check: Editorial Manager / Elsevier submission.
- Signature vocabulary: consumer mechanism, experimental manipulation, psychological process, moderation logic, consumer welfare.
- Sibling boundary: Journal of Consumer Research, Journal of Marketing Research, Marketing Science, and Psychological Science.
- House-style aim: psychological mechanism evidence tied to consumer behavior and marketing theory.
- Official URLs currently used by the pack:
- https://www.sciencedirect.com/journal/journal-of-consumer-psychology
- https://www.elsevier.com/journals/journal-of-consumer-psychology/1057-7408/guide-for-authors

## Stage-specific moves

1. State the exact theory development question in one sentence.
2. Identify which JCP audience segment would care and which would desk-reject the paper.
3. Separate evidence already in the draft from evidence that still needs analysis, coding, or literature review.
4. Convert each concern into an auditable action with owner, file, and expected output.
5. End with a handoff to `jcp-literature-positioning` if the stage passes, or back to `jcp-workflow` if it does not.

## Checklist
- [ ] The JCP audience can see why the paper belongs in consumer psychology, judgment and decision-making, persuasion, emotion, identity, and consumption behavior.
- [ ] The draft distinguishes JCP from Journal of Consumer Research, Journal of Marketing Research, Marketing Science.
- [ ] Claims using current process facts are backed by `resources/official-source-map.md` or marked 待核实.
- [ ] The role-specific deliverable for theory development names the next decision, not just prose edits.
- [ ] Tables, exhibits, appendices, or review material support the main claim without burying it.
- [ ] Construct definitions, boundary conditions, and theory mechanisms are aligned.
- [ ] Methods are justified by the phenomenon, not by convenience or fashion.

## Anti-patterns
- Submitting a paper that is merely adjacent to JCP without the journal's audience and mechanism.
- Relying on generic phrasing after the clone audit would strip out the journal name.
- Listing robustness checks without explaining which identifying threat each one addresses.
- Treating official process facts as permanent when the source map marks them as volatile.
- Inventing exemplar papers, editor names, fees, or word limits instead of marking uncertainty.

## Output format

```text
【Journal】Journal of Consumer Psychology
【Skill】jcp-theory-development
【Verdict】pass / revise / reroute
【Binding issue】one concrete issue blocking theory development
【Evidence needed】data, model, literature, exhibit, or policy source
【Sibling boundary】why not Journal of Consumer Research, Journal of Marketing Research
【Source status】verified URL / 待核实 / not asserted
【Next skill】jcp-literature-positioning
```
