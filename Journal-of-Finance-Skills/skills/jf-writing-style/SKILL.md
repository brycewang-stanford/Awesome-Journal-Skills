---
name: jf-writing-style
description: Use when polishing the prose of a The Journal of Finance (JF) manuscript for accessible, general-interest exposition. Tightens writing and framing; it does not change results or run analyses.
---

# Writing Style & Exposition (jf-writing-style)

## When to trigger

- The introduction does not deliver the question, finding, and magnitude in the first page
- Prose is dense, jargon-heavy, or written for a subfield rather than the broad AFA reader
- The main finding is buried; the reader has to work to extract the takeaway
- Sentences hedge so much the claim disappears

## JF house voice: accessible, precise, general-interest

JF articles are read across asset pricing, corporate finance, banking, microstructure, and household finance. The writing must be **accessible to a finance reader outside your subfield** while staying precise. Lead with economics, not machinery. Move technical depth to the Internet Appendix and let the prose carry the intuition.

## The JF introduction (first ~3 pages do the work)

A strong JF introduction, in order:
1. **The question and why it matters** — concrete, general-interest, one or two paragraphs.
2. **What you do** — the design / data / test in plain terms.
3. **What you find** — the headline result with its **economic magnitude** in interpretable units.
4. **Why it is identified / credible** — one paragraph on the source of variation or the test.
5. **Contribution** — the closest papers and your specific delta (see `jf-literature-positioning`).
6. **Roadmap** — brief, if at all.

A reader who stops after page 3 should know the question, the answer, the size of the answer, and why to believe it.

## Sentence-level discipline

- Prefer the active voice and short declaratives for the main claims.
- State magnitudes in interpretable units (bps, % of market cap, fraction of the spread, Sharpe gain), not only t-stats.
- Define notation once; do not re-derive in prose what a table already shows.
- Cut hedging stacks ("may potentially suggest that it is possible that…") down to one calibrated claim.
- Replace "significant" (statistical) with the economic interpretation where you mean economic importance.

## Checklist

- [ ] Question, finding, and economic magnitude appear within the first ~3 pages
- [ ] The headline number is in interpretable economic units, not just significance
- [ ] A non-specialist finance reader could follow the introduction
- [ ] Heavy notation/derivation lives in the Internet Appendix, not the prose
- [ ] Active voice and short declaratives carry the main claims
- [ ] Hedging is calibrated, not reflexive
- [ ] Tense and terminology are consistent; the abstract matches the introduction's claims
- [ ] No unexplained jargon from a single subfield

## Anti-patterns

- An introduction that opens with three paragraphs of literature before the question
- Reporting "statistically significant at the 1% level" as if it were the finding
- Subfield jargon with no plain-language gloss for the broad AFA reader
- A finding the reader cannot locate without reading the whole results section
- Over-hedged claims that leave the contribution ambiguous
- An abstract that promises more than the introduction delivers

## Output format

```
【Question+finding+magnitude in first 3 pp?】yes / no
【Magnitude in economic units?】yes / no
【Accessible to non-specialist?】yes / no
【Notation moved to appendix?】yes / no
【Hedging trimmed?】yes / no
【Next step】jf-submission
```
