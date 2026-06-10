---
name: jf-writing-style
description: Use when polishing the prose of a The Journal of Finance (JF) manuscript for accessible, general-interest exposition that reaches the broad AFA flagship readership. Tightens the introduction so question, finding, and economic magnitude land on page one, trims hedging, and offloads notation to the Internet Appendix; it does not change results or run analyses.
---

# Writing Style & Exposition (jf-writing-style)

## When to trigger

- The introduction does not deliver the question, finding, and magnitude in the first page
- Prose is dense, jargon-heavy, or written for a subfield rather than the broad AFA reader
- The main finding is buried; the reader has to work to extract the takeaway
- Sentences hedge so much the claim disappears

## JF house voice: accessible, precise, general-interest

JF is the **AFA flagship**, read across asset pricing, corporate finance, banking, microstructure, and household finance by 8,000+ readers. Writing must be **accessible to a finance reader outside your subfield** while staying precise. The manuscript also faces a **60-page limit** (≥1.5 spacing, 12-pt font), so lead with economics and **offload technical depth to the Internet Appendix** (bundled at the end of the same PDF; see `jf-internet-appendix`) rather than padding the body.

## The JF introduction (first ~3 pages do the work)

In order: (1) **the question and why it matters** — general-interest, concrete; (2) **what you do** — design/data/test in plain terms; (3) **what you find** — headline result with its **economic magnitude** in interpretable units; (4) **why it is credible** — the source of variation or the test; (5) **contribution** — the closest papers and your delta (see `jf-literature-positioning`); (6) brief roadmap. A reader who stops at page 3 should know the question, the answer, its size, and why to believe it.

## Sentence-level discipline

- Active voice and short declaratives for main claims.
- State magnitudes in interpretable units (bps, % of market cap, Sharpe gain), not only t-stats.
- Define notation once; do not re-derive in prose what a table shows.
- Cut hedging stacks to one calibrated claim.
- Use "significant" for economic importance, not as a synonym for the p-value.

## Page-one diagnostic grid

Test a JF introduction by reading only page one and asking whether each element is present — the pass an out-of-subfield editor makes:

| By the bottom of page one, the reader knows…    | If absent, the fix                                |
|-------------------------------------------------|---------------------------------------------------|
| The question and why it is first-order          | Open with the stake, not the literature           |
| What you do, in plain terms                     | One sentence on design/data/test, no notation     |
| The headline finding                            | State the result before its caveats               |
| Its economic magnitude in interpretable units   | Add the bps / Sharpe gain / % of value            |
| Why it is credible                              | Name the shock, instrument, or asset-pricing test |

A subfield draft typically fails on magnitude or credibility, assuming the reader cares.

## Worked vignette — rewriting a buried opening

*Illustrative.* A draft opens: "A large literature examines the cross-section of expected returns. We contribute to it." The result arrives three paragraphs later. The JF rewrite leads on page one:

> "Firms exposed to supply-chain concentration earn 45 bps per month higher returns (Sharpe gain ≈ 0.4, illustrative). The premium survives standard factor adjustment and concentrates where arbitrage is costly, pointing to mispricing over risk."

The page-one reader now has the question, answer, size, and reason to believe; the survey citation moves into the contribution paragraph (`jf-literature-positioning`).

### Referee-pushback patterns and the JF-specific fix
| Pushback on the prose                              | JF-specific fix                                                |
|----------------------------------------------------|-----------------------------------------------------------------|
| "I read three pages before the finding"            | Move question + result + magnitude to page one                  |
| "Significant at 1%' is reported as the result"     | Replace with the magnitude; keep the t-stat in a note           |
| "The body is padded toward 60 pages"               | Offload derivations/notation to the Internet Appendix           |

## Calibration anchors
- JF's voice is **accessible but precise** — not a popular-science register; the goal is a finance economist outside your niche following the argument. The "first three pages do the work" norm is durable, but exact length conventions vary; confirm against the journal's current author guidelines.

## Checklist

- [ ] Question, finding, and economic magnitude in the first ~3 pages
- [ ] Headline number in interpretable economic units
- [ ] A non-specialist finance reader could follow the introduction
- [ ] Heavy notation/derivation moved to the Internet Appendix, keeping the body ≤60 pages
- [ ] Active voice; calibrated (not reflexive) hedging
- [ ] Abstract matches the introduction's claims

## Anti-patterns

- Opening with three paragraphs of literature before the question
- Reporting "significant at the 1% level" as if it were the finding
- Subfield jargon with no plain-language gloss for the broad AFA reader
- Padding the body toward the 60-page cap instead of using the Internet Appendix
- Over-hedged claims that blur the contribution

## Output format

```
【Question+finding+magnitude in first 3 pp?】yes / no
【Magnitude in economic units?】yes / no
【Accessible to non-specialist?】yes / no
【Notation moved to Internet Appendix?】yes / no
【Body ≤60 pp / hedging trimmed?】yes / no
【Next step】jf-submission
```
