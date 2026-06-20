---
name: joe-writing-style
description: Use to make a Journal of Econometrics (JoE) manuscript read in house style — a precise abstract under 250 words, a contribution-first introduction, legible theorem-and-proof exposition, and Elsevier elsarticle/[dataset] reference conventions. Late-stage polish; it does not invent results.
---

# Writing Style (joe-writing-style)

## When to trigger

- The abstract exceeds 250 words or buries the methodological contribution
- The introduction lists what you did but never states the advance plainly
- Proofs are correct but unreadable — no roadmap, lemmas dumped without motivation
- References or math formatting do not follow Elsevier/elsarticle conventions

## JoE house style

The *Journal of Econometrics* publishes mathematically rigorous methodology, and its prose has to make rigor **legible**. Editors screen before assigning a **minimum of two referees**, so the abstract and introduction must land the contribution fast. Key house facts to write to:

- **Abstract ≤ 250 words**, concise and factual; avoid references unless essential, and if used cite author/year in the abstract.
- **elsarticle** LaTeX document class; **Elsevier** reference style (numbered or author-year, any CSL-compatible manager). Dataset citations tagged **`[dataset]`** with author/title/repository/version/year/persistent ID.
- Initial submission is a **single PDF** (~40 pages, ≥1.5 spacing, 11pt); write for that length norm rather than a hard word count.

## Abstract (≤ 250 words)

- Sentence 1: the econometric problem and why existing methods fail.
- Sentence 2: the proposed estimator/test/result and its key property (weaker assumptions, efficiency, valid inference).
- Sentence 3: the asymptotic guarantee and the Monte Carlo / empirical evidence.
- Keep it factual; no hype, no undefined notation. Spell out any cited reference in full.

## Introduction (contribution-first)

1. The problem and its stakes for econometric practice.
2. What is known and exactly where it falls short (the gap from `joe-literature-positioning`).
3. **The contribution, stated as a property**, in plain words before any notation.
4. A preview of the assumptions, the main theorem, and the finite-sample evidence.
5. A short roadmap. Write the introduction **last**, after theorems and Monte Carlo are settled.

## Theorem-and-proof exposition

- State assumptions once, label them, and refer back by label — do not silently re-use.
- Give each theorem a one-line **intuition** before the formal statement; say what drives the result.
- Provide a **proof roadmap** (consistency → rate → distribution); relegate routine algebra to an appendix but keep the logical skeleton in view.
- Define every symbol on first use; keep notation consistent across theory, Monte Carlo, and illustration.

## Anti-patterns

- A 300-word abstract, or one that states the model but not the contribution
- An introduction that is a related-work list with the advance hidden on page 6
- Proofs with no roadmap; lemmas appearing before the reader knows why
- Inconsistent or undefined notation; reference style that ignores Elsevier/elsarticle conventions


## Style execution pass for Journal of Econometrics

Use this as a second-pass capability check. First lock the estimand or theorem, assumptions, asymptotic/simulation evidence, and applied relevance; then test whether the manuscript addresses econometrics reviewers who expect methodological novelty, assumptions, simulation or empirical illustration, and reproducibility.

- **Primary move:** Rewrite the opening and transitions so the venue-level claim, evidence object, and contribution are visible before technical detail.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Econometric Theory for proof-first work, JBES for applied statistical methods, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Abstract】≤250 words, states problem + property + evidence? [Y/N]
【Intro】contribution stated as a property before notation? [Y/N]
【Proof exposition】intuition + roadmap + labeled assumptions? [Y/N]
【Notation】defined on first use, consistent throughout? [Y/N]
【References】Elsevier style + [dataset] tags? [Y/N]
【Next step】joe-replication-and-data-policy
```
