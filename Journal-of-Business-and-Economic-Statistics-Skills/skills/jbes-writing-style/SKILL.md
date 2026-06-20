---
name: jbes-writing-style
description: Use when polishing prose, theorem statements, the abstract, and the introduction for a Journal of Business & Economic Statistics (JBES) methods paper so the methodological contribution and its empirical relevance both land. Polishes exposition; it does not change theory or results.
---

# Writing Style (jbes-writing-style)

## When to trigger

- The prose buries the method, or the theorem statements are hard to parse
- The abstract leads with generic motivation instead of the methodological contribution
- The introduction reaches the method only after pages of setup
- Notation is overloaded and a reader cannot follow the conditions

## JBES house style: method-first, application-anchored

JBES is read by both econometricians and applied economists/statisticians, so the writing must make a **methodological contribution legible** while keeping its **empirical relevance** front and center. Unlike a general-economics journal (which leads with a finding) or a pure-statistics journal (which can lead with a theorem in the abstract), a JBES paper should pair the two: state what is methodologically new **and** why it matters for a real application, early and plainly. Theorem statements should be precise and self-contained; the heavy proofs belong in an appendix.

## The introduction arc (JBES template)

1. **The problem** — the empirical/statistical problem that motivates the method, in plain terms.
2. **Why existing methods fall short** — the gap (assumptions, robustness, computation) that blocks a clean answer.
3. **The contribution** — what the new method is and what it delivers (consistency / valid inference / feasibility).
4. **Evidence preview** — the Monte Carlo properties and the empirical application, in one breath.
5. **Relation to prior methods** — concise positioning, not a survey.
6. **Roadmap** — brief.

## Abstract and exposition

- Open with the methodological contribution and its empirical relevance; do not bury the method behind generic motivation.
- State theorems in words once before the formalism; define notation as you introduce it, not all at once.
- Quantify the gains ("controls size where method X over-rejects by 12 points") rather than vague claims.
- Check the abstract length and required style on the live JBES instructions page before filing.

## Checklist

- [ ] Abstract names the methodological contribution and its empirical relevance
- [ ] The method appears on page one, not after pages of setup
- [ ] Theorem statements are precise and self-contained; proofs in the appendix
- [ ] Notation introduced incrementally, not dumped
- [ ] Gains quantified against named incumbents
- [ ] Abstract length / citation style checked on the live instructions page

## Anti-patterns

- An abstract of generic motivation that never states what is methodologically new
- Leading the intro with the application and never foregrounding the method (or vice versa)
- Theorems stated in dense notation with no plain-language gloss
- Notation overload that forces the reader to hold many symbols at once
- Vague "performs better" claims with no dimension or magnitude


## Worked vignette: repairing one opening

A hypothetical JBES paper proposes a regularized HAR forecaster for realized volatility on 5-minute S&P 500 returns (numbers **illustrative**). A draft abstract that says only "forecasting matters; our model works" states neither delta nor payoff. The repair leads with both legs: dependence-robust lag selection cuts one-day-ahead QLIKE loss by an illustrative 8% versus standard HAR and stays valid under heavy-tailed intraday returns.

## Style pushback patterns (venue-specific fixes)

| JBES pushback | Fix |
|----|----|
| "Could not tell what is new until Section 4." | Contribution sentence into the abstract; defer the survey |
| "Application feels bolted on." | Weave the macro-finance use into the problem and evidence |

Calibration anchor (hedged): JBES prose tolerates a precise theorem in the abstract *provided*
empirical relevance sits beside it. Word limit and style are live T&F preflight items.

## Style execution pass for Journal of Business & Economic Statistics

Run this as a concrete capability pass. First lock the statistical estimand, identification/simulation evidence, empirical illustration, and reproducibility path; then test whether the manuscript addresses econometrics/statistics reviewers who expect methodological credibility plus a business or economic use case.

- **Primary move:** Rewrite the opening and transitions so the venue-level claim, evidence object, and contribution are visible before technical detail; keep house-style limits tied to the source map.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Journal of Econometrics for theory-heavy methods, Econometric Theory for proof-first work, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Abstract verdict】contribution + relevance stated? [Y/N] — fix: ...
【Intro arc】problem / gap / contribution / evidence / positioning present? [Y/N each]
【Theorem clarity】precise + glossed + proofs in appendix? [Y/N]
【Notation】introduced incrementally? [Y/N]
【Style facts】abstract length + citation style verified live? [Y/N]
【Next step】jbes-replication-and-data-policy
```
