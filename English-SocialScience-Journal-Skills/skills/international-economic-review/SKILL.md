---
name: international-economic-review
description: Use when targeting International Economic Review (IER) or deciding whether a technically rigorous economics manuscript in theory, econometrics, or macro fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# International Economic Review (international-economic-review)

## Journal positioning

IER is a leading general-economics journal with particular strength in economic theory, econometrics, and macroeconomics, known for technical rigor. It rewards papers that make a clean, formal contribution — a theoretical result, a structural/econometric advance, or a quantitative-macro analysis executed with precision. The readership is technically oriented economists, so the bar is on rigor and the generality of the contribution, not on broad popular appeal.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the journal/Wiley site and the editorial submission system.

## When to trigger

- The author names IER as the target venue, or wants a rigorous general-economics home for theory/econometrics/macro.
- A technically demanding paper is excellent but narrower than a top-5 general-interest result.
- A structural or theoretical paper needs re-framing so the formal contribution and its generality are foregrounded.
- The author needs IER's desk-reject risks and a credible theory/econometrics/macro alternative list.

## Scope & topic fit

- Economic theory: micro and macro theory, dynamic models, mechanism and equilibrium analysis.
- Econometrics: estimation and inference methods, identification theory, structural econometrics.
- Macroeconomics, including quantitative and structural models disciplined by data.
- Applied work is in scope when it carries a substantive theoretical or methodological contribution.

## Method & evidence bar

- Formal rigor is the filter: theory needs clearly stated assumptions, correct and complete proofs, and results that generalize; econometrics needs proper derivation of properties.
- Structural and quantitative-macro papers need transparent identification of parameters, defensible solution/estimation, and robustness.
- Empirical claims need credible identification and modern inference; a regression without design is not a fit here.
- The contribution should be a result that advances theory, method, or quantitative understanding, not a significant coefficient.

## Structure & house style

- The introduction states the problem, the formal setup, the main result, and its generality early, and explains the technical contribution.
- Position against the relevant theory/econometrics/macro literature; relate assumptions and results to prior work explicitly.
- Uses an unstructured abstract and JEL codes; an online appendix or supplement carries proofs, derivations, and computational detail.
- Exhibits and propositions should be self-contained; the central result (theorem, estimator property, or quantitative finding) should be clearly stated.

## Official-submission checklist

- Search the live site for "International Economic Review submission guidelines / author guidelines" and follow the current version.
- Re-check submission fee, formatting, abstract/JEL requirements, anonymization, and proof/appendix conventions on the submission system.
- Re-check the current data and code availability / replication policy for empirical and quantitative papers.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the formal/quantitative contribution and why it generalizes.
- [ ] The contribution is stated as a theorem / estimator property / structural result, not as statistical significance.
- [ ] The introduction positions the paper against the current theory/econometrics/macro frontier.
- [ ] Proofs are complete and correct, or identification and inference meet current standards.
- [ ] Appendix, derivations, and (if empirical) data/code are ready for the official policy.

## Common desk-reject triggers

- A theory paper with incomplete proofs, fragile assumptions, or a non-general result.
- An econometrics contribution without derived properties or clear identification.
- A reduced-form empirical paper with no design and no theoretical/methodological advance.
- A narrow extension with no broader formal payoff.

## Re-routing decision

- General-interest at the top → `american-economic-review`; pure microeconomic theory → `journal-of-economic-theory`; game theory / mechanism → `games-and-economic-behavior`.
- Econometric methods core → `journal-of-econometrics`; methods-in-application → `journal-of-applied-econometrics` or `journal-of-business-and-economic-statistics`.
- Quantitative macro → `review-of-economic-dynamics` or `journal-of-monetary-economics`; broad general field → `european-economic-review` or `journal-of-the-european-economic-association`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] International Economic Review
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the formal / quantitative rigor clear IER's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / proofs-appendix / data-code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
