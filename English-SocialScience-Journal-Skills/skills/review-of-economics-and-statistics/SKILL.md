---
name: review-of-economics-and-statistics
description: Use when targeting Review of Economics and Statistics (REStat) or deciding whether an applied econometrics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Review of Economics and Statistics (review-of-economics-and-statistics)

## Journal positioning

REStat (Harvard/MIT, MIT Press) is a leading outlet for applied econometrics and empirical economics, with a long tradition in careful identification and measurement. It publishes sharply executed empirical papers across fields — often shorter and more focused than top-5 omnibus papers — where a clean design, careful measurement, or a useful applied-econometric contribution carries the work. The contribution is credible empirical evidence done well; the bar is high on identification and execution rather than on discipline-wide general interest.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the REStat / MIT Press site and the editorial submission system.

## When to trigger

- The author names REStat as the target, or has a focused empirical paper that is excellent but narrower than a top-5 swing.
- A paper's strength is careful identification or measurement rather than a discipline-wide general-interest hook.
- A solid applied-econometrics or empirical paper needs a venue that rewards clean execution and a sharp, contained contribution.
- The author needs REStat's desk-reject risks and a credible top-5 / applied-field alternative list.

## Scope & topic fit

- Applied empirical economics across fields — labor, public, development, health, IO, macro-empirical, trade — with credible identification.
- Careful measurement papers: new data, better estimates of an important quantity, or improved measurement of an economic object.
- Applied-econometric contributions: methods and estimators motivated by and demonstrated on a real empirical problem.
- Focused, sharply executed papers; REStat is comfortable with shorter, contained contributions that make one empirical point well.

## Method & evidence bar

- Identification and measurement are the filter: the design (DiD, IV, RDD, event study, structural) must be credible and the measurement careful and transparent.
- Modern estimators and inference are baseline — proper DiD under staggered treatment, valid first stages, RDD diagnostics, correct standard errors.
- Robustness should be thorough but disciplined; the empirical point must survive the obvious alternative explanations.
- Data and code transparency is expected; re-check the current replication and data/code availability policy, which is enforced for empirical work.

## Structure & house style

- The introduction states the empirical question, the identification or measurement contribution, the headline estimate, and what it adds to the evidence.
- Lead with the design and the clean estimate; keep the paper focused — REStat rewards a contained, well-argued contribution over a sprawling one.
- REStat uses an unstructured abstract and JEL codes; robustness and supplementary results belong in an online appendix.
- Exhibits should report magnitudes and let the central estimate be read from one table or figure.

## Official-submission checklist

- Search the live site for "Review of Economics and Statistics submission guidelines" / "information for authors" and follow the current MIT Press / editorial version.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, length expectations (including any short-paper format), and figure/table standards on the submission system.
- Re-check the current data and code availability / replication policy and any verification workflow — confirm it is enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the empirical question and why the identification or measurement is credible.
- [ ] The contribution is stated as identification / measurement / applied method, not as statistical significance.
- [ ] The introduction positions the paper against the recent applied frontier on this question.
- [ ] Identification threats are addressed by design; estimators and inference are state-of-the-art; the paper is focused.
- [ ] Data and code are ready for the current availability / replication policy.

## Common desk-reject triggers

- A correlational or weakly-identified design presented as causal.
- Naive TWFE on staggered adoption, weak IV, or RDD without density/covariate diagnostics.
- A sprawling, unfocused paper where the central empirical point is buried.
- "First to study X in context Y" with no design, measurement, or methodological advance.

## Re-routing decision

- General-interest empirical importance → `american-economic-review`, `quarterly-journal-of-economics`, or `journal-of-political-economy`; one crisp result → `aer-insights`.
- Applied-micro design as the headline → `aej-applied-economics`; policy-relevant magnitudes → `aej-economic-policy`.
- Empirical macro / quantitative macro → `aej-macroeconomics`; a genuine new estimator with full theory → `econometrica` or `journal-of-econometrics`.
- Field-leading specialist work → the relevant top field journal (`journal-of-labor-economics`, `journal-of-public-economics`, `journal-of-health-economics`).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Review of Economics and Statistics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / measurement clear the applied-econometrics bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / length format / data-code policy>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
