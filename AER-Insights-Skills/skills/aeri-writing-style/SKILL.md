---
name: aeri-writing-style
description: Use when revising an American Economic Review: Insights (AER: Insights) short-format manuscript to lead with the result, fit the hard word cap (7,000 words minus 200 per exhibit), and write the ≤100-word abstract. Enforces the length budget and the lead-with-the-result arc; it does not change the analysis.
---

# Writing Style — Lead With the Result, Fit the Cap (aeri-writing-style)

## When to trigger

- The intro buries the headline result under setup, literature, or methods
- The draft is over the word cap and needs cutting, not just polishing
- The abstract exceeds 100 words or does not state the result
- Late-stage polish once identification, robustness, and exhibits have settled

## The two hard constraints (检索于 2026-06；以官网为准)

- **Word cap:** main text **≤7,000 words with no exhibits; each exhibit subtracts 200 words; ≤5 exhibits** (so ≥6,000 at the cap). The count includes body, footnotes, endnotes, and in-paper appendices; it **excludes** title, authors, abstract, acknowledgement footnote, references, exhibits, and the Supplemental Appendix. **Over the cap = returned unreviewed.**
- **Abstract: ≤100 words.** It must state the result, not promise it.

Treat the cap as a design constraint from the first draft, not a final trim. Every sentence competes with the insight for space.

## The AER: Insights arc (lead with the result)

Unlike a long paper that builds to its result, an AER: Insights paper **states the answer in the first paragraph**:

1. **Sentence 1–2:** the question and the **headline result with its magnitude and uncertainty** (estimate + SE / confidence set), no asterisks.
2. **Sentence 3–4:** why it matters / the prior it overturns (the surprise).
3. **One short paragraph:** how it is identified (the design or the model's key restriction), in plain terms.
4. **One sentence:** the single most important robustness/scope caveat, with a pointer to the appendix.
5. **Brief roadmap or none** — the paper is short enough that heavy signposting wastes words.

The body then delivers exactly that arc: setup (tight), identification, result, the one or two checks, a short discussion. No second result, no survey, no extended derivations in-text.

## Cutting to the cap (in priority order)

1. **Cut secondary results** to the Supplemental Appendix ([`aeri-robustness`](../aeri-robustness/SKILL.md)).
2. **Compress the literature** to one or two paragraphs ([`aeri-literature-positioning`](../aeri-literature-positioning/SKILL.md)).
3. **Move proofs/derivations and estimation detail** to the appendix ([`aeri-theory-model`](../aeri-theory-model/SKILL.md)).
4. **Delete throat-clearing** ("It is well known that…", over-signposted roadmaps).
5. **Merge exhibits** to reclaim 200 words each ([`aeri-tables-figures`](../aeri-tables-figures/SKILL.md)).
6. **Tighten prose** last — shorter sentences, fewer hedges, active voice.

## Writing the ≤100-word abstract

- State **the result with its magnitude**, the setting, and the identification in one breath.
- No literature, no "we examine"; say what you found.
- Verify the count; 100 words is a hard ceiling.

## Checklist

- [ ] **First paragraph states the headline result** with magnitude + SE/CI (no asterisks)
- [ ] Main text **under 7,000 − 200×(#exhibits)** words (counted per AEA scope rules)
- [ ] Abstract **≤100 words** and states the result
- [ ] One idea only in-text; secondary material in the Supplemental Appendix
- [ ] Literature compressed to ≤2 paragraphs; no in-text survey
- [ ] No significance asterisks/boldface anywhere
- [ ] Roadmap minimal or absent; throat-clearing removed

## Anti-patterns

- A long build-up that reveals the result only in Section 4
- Trimming prose while leaving a second result in-text (cut the result first)
- An abstract over 100 words, or one that promises rather than reports
- Counting the word budget only at the end and discovering you are 2,000 over
- AER-length signposting in a short paper

## Output format

```
【First paragraph】states result + magnitude + SE/CI? [Y/N]
【Word count】main text = __ ; cap = 7000 − 200×__ = __ ; under? [Y/N]
【Abstract】__ words (≤100?) and states the result? [Y/N]
【Cut list to hit cap】<secondary results / lit / proofs / exhibits merged>
【No-asterisk check】[Y/N]
【Next step】aeri-replication-package
```
