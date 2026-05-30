---
name: journal-of-political-economy
description: Use when targeting Journal of Political Economy (JPE) or deciding whether an economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Political Economy (journal-of-political-economy)

## Journal positioning

JPE is the Chicago-edited general-interest journal and one of the economics "top-5" (with AER, QJE, Econometrica, REStud). It carries the price-theory tradition: papers that take economic logic, incentives, and equilibrium seriously, whether the contribution is rigorous theory or careful empirics. The editorial culture rewards a disciplined economic argument — a question framed in clean economic terms with a model or mechanism behind the result — for a discipline-wide readership.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the JPE / University of Chicago Press site and the editorial submission system.

## When to trigger

- The author names JPE (or JPE as a top-5 swing) as the target venue.
- A paper has tight economic logic — a model, a price/incentive mechanism, or theory-disciplined empirics — and the author is choosing among JPE / AER / QJE.
- An empirical paper needs re-framing so the economic mechanism, not just the reduced-form effect, becomes the contribution.
- The author needs JPE's desk-reject risks and a credible top-5 / top-field alternative list.

## Scope & topic fit

- First-order questions across economics with an explicit economic-theory backbone — price theory, incentives, equilibrium, market structure, human capital, growth, public economics.
- Rigorous theory papers whose results are general and economically consequential.
- Empirical papers disciplined by a model: structural work, or reduced-form designs whose interpretation rests on a clear mechanism.
- Work that bridges theory and evidence — testing a sharp theoretical prediction with credible data.

## Method & evidence bar

- The economic argument is the filter: a result without a coherent economic mechanism or model behind it is a poor fit, however clean the regression.
- Theory must deliver general, interpretable results — not a narrow parameterized extension — with assumptions stated and economically motivated.
- Empirical identification is held to top-5 standards (modern DiD, valid IV, credible RDD), but interpretation must connect to the underlying economics.
- Structural estimation should identify economically meaningful parameters and confront the data seriously; data and code transparency follows the AEA-style availability and verification norms.

## Structure & house style

- The introduction states the economic question, the mechanism or model, the approach, and the headline result, and motivates why the economics is interesting and general.
- Make the theoretical and empirical contributions distinct and mutually reinforcing; let the model discipline the interpretation of the evidence.
- JPE uses an unstructured abstract and JEL codes; proofs, derivations, and secondary results belong in an appendix or online supplement.
- Exhibits and propositions should be self-contained; the central result — theorem or estimate — should be legible on its own.

## Official-submission checklist

- Search the live site for "Journal of Political Economy submission guidelines" and the data and code availability policy, and follow the current UChicago Press / editorial versions.
- Re-check the submission fee, formatting, abstract/JEL requirements, anonymization expectations, and figure/table standards on the submission system.
- Re-check the current data/code deposit and verification workflow (replication package archive) — confirm it is enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the economic mechanism or model that makes this a JPE-style contribution.
- [ ] The contribution is stated as theory / mechanism / identification, not as statistical significance.
- [ ] The introduction positions the paper against the current top-5 frontier and the economic question it advances.
- [ ] Theory results are general and proven, or empirics are disciplined by a clear model; identification is state-of-the-art.
- [ ] Data and code are ready for the availability + verification workflow.

## Common desk-reject triggers

- A reduced-form empirical paper with no economic mechanism or model behind the result.
- A theory paper that is a narrow extension with no general or surprising implication.
- "First to study X in context Y" framing without a disciplined economic argument or conceptual advance.
- Identification the profession no longer accepts (naive TWFE on staggered adoption, weak IV, cosmetic RDD).

## Re-routing decision

- General-interest but a better fit elsewhere in the top-5 → `american-economic-review` (broad importance) or `quarterly-journal-of-economics` (big question + clean experiment).
- Pure theory / mechanism design → `econometrica` (theorem with proofs) or `aej-microeconomics` / `journal-of-economic-theory`.
- Excellent but narrower applied micro → `aej-applied-economics` or `review-of-economics-and-statistics`; macro/growth → `aej-macroeconomics`.
- Policy-facing applied economics → `aej-economic-policy` or `journal-of-public-economics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Political Economy
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the economic argument + identification/theory clear JPE's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
