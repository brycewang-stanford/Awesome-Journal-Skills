---
name: econometrica
description: Use when targeting Econometrica or deciding whether an economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Econometrica (econometrica)

## Journal positioning

Econometrica is the journal of the Econometric Society and one of the economics "top-5" (with AER, QJE, JPE, REStud) — the most technical of the five. It publishes econometric theory, economic theory, and highly rigorous structural and empirical work, where the contribution is typically a new theorem, a new identification result, or a new estimator, established to the field's highest formal standard. The readership is technically expert; a paper succeeds on the depth and correctness of its formal contribution, not on topical interest alone.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Econometric Society / Wiley site and the editorial submission system.

## When to trigger

- The author names Econometrica (or the top-5 with a technical contribution) as the target venue.
- A paper proves new theorems, establishes new identification, or develops a new estimator with full asymptotic theory.
- A structural or empirical paper rests on a genuinely new methodological contribution that needs the most rigorous venue.
- The author needs Econometrica's desk-reject risks and a credible top-5 / methods-journal alternative list.

## Scope & topic fit

- Econometric theory: estimation, inference, identification, asymptotics, nonparametrics, time series, panel, and high-dimensional methods.
- Economic theory: decision theory, game theory, mechanism and market design, general equilibrium, with general theorems.
- Highly rigorous structural econometrics where the identification and estimation argument is itself a contribution.
- Empirical work only when paired with a genuine new method or identification result, not standard applied designs.

## Method & evidence bar

- The formal bar is the filter: theory papers need correct, general theorems with complete proofs; econometrics papers need new identification or estimation results with rigorous large-sample (and where relevant finite-sample) theory.
- Assumptions must be minimal, stated precisely, and economically or statistically motivated; results should generalize beyond a worked example.
- New estimators require consistency, asymptotic distribution, valid inference, and ideally simulation and an empirical illustration.
- Proofs, regularity conditions, and Monte Carlo evidence are expected in heavy supplementary/proof appendices; correctness is non-negotiable.

## Structure & house style

- The introduction states the formal problem, the gap in existing theory, the precise contribution (theorem/estimator/identification result), and how it improves on prior results.
- Definitions, assumptions, propositions, and theorems are stated formally in the main text; long proofs and derivations move to appendices and supplementary material.
- Econometrica enforces a substantial supplementary material / proof appendix and replication standard; an unstructured abstract and JEL codes are standard.
- Notation must be consistent and economical; exhibits (where present) support a method's properties (size, power, coverage) rather than a topical narrative.

## Official-submission checklist

- Search the live site for "Econometrica submission guidelines" / "information for authors" and the Econometric Society replication and supplementary-material policy, and follow the current versions.
- Re-check the submission fee, LaTeX/formatting requirements, abstract/JEL, anonymization, and supplementary-material/proof-appendix conventions on the submission system.
- Re-check the current data, code, and replication-package deposit policy and any computational-verification workflow before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the new theorem, identification result, or estimator that is the contribution.
- [ ] The contribution is stated as a formal result, not as an empirical finding or statistical significance.
- [ ] The introduction positions the paper against the precise prior theory/econometrics it generalizes or corrects.
- [ ] All proofs are complete and correct; assumptions are minimal and motivated; asymptotics/inference are rigorous.
- [ ] Supplementary material, proofs, and any replication package match the current official guide.

## Common desk-reject triggers

- An applied paper with standard methods and no new theorem, estimator, or identification result.
- A theory result that is a narrow special case, lacks general proofs, or restates known results.
- An estimator proposed without asymptotic theory, valid inference, or simulation evidence.
- Incomplete or incorrect proofs, hidden assumptions, or sloppy formal exposition.

## Re-routing decision

- Rigorous but more topical applied econometrics → `journal-of-econometrics`, `journal-of-applied-econometrics`, `journal-of-business-and-economic-statistics`, or `quantitative-economics`.
- General economic-theory results without the top-5 importance → `journal-of-economic-theory` or `aej-microeconomics`; game theory → `games-and-economic-behavior`.
- General-interest empirical or applied work → `american-economic-review`, `quarterly-journal-of-economics`, or `journal-of-political-economy`.
- Frontier theory/methods with novelty over generality → `review-of-economic-studies`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Econometrica
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the formal contribution — theorem / estimator / identification — clear Econometrica's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / LaTeX / supplementary proofs / replication policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
