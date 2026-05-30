---
name: review-of-economic-studies
description: Use when targeting Review of Economic Studies (REStud) or deciding whether an economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Review of Economic Studies (review-of-economic-studies)

## Journal positioning

REStud is one of the economics "top-5" (with AER, QJE, JPE, Econometrica), European-leaning and run by an active scholarly board. It is strong in theory and frontier methods and is known for publishing ambitious, technically serious work — historically a natural home for outstanding junior-scholar papers. The editorial culture prizes novelty and rigor across fields: a paper that does something genuinely new, whether a new model, a new method, or a striking new result, for a discipline-wide readership.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the REStud / Oxford University Press site and the editorial submission system.

## When to trigger

- The author names REStud (or the top-5 with a novel theoretical/methodological angle) as the target venue.
- An ambitious paper — often by a junior scholar — pushes a frontier in theory, methods, or design and the author is choosing among the top-5.
- A technically serious paper needs re-framing so its novelty and rigor, not just its topic, lead the contribution.
- The author needs REStud's desk-reject risks and a credible top-5 / top-field alternative list.

## Scope & topic fit

- Frontier economic theory — micro theory, macro theory, dynamic models, mechanism and information economics — with general, novel results.
- Frontier empirical and structural work that introduces or pushes new methods or identification.
- Macro, labor, public, development, and IO papers when the contribution is methodologically or conceptually ambitious.
- Cross-field work that combines theory and evidence in a novel way and reads as broadly important.

## Method & evidence bar

- Novelty and rigor are the joint filter: the paper must do something new and do it correctly to a high formal standard.
- Theory needs general, well-proved results; empirical and structural work needs credible, state-of-the-art identification and, where the method is the contribution, the supporting theory.
- Ambition is rewarded but not at the expense of correctness — clean proofs, valid inference, and pre-empted threats are expected.
- Data and code transparency follows current top-journal availability and verification norms; replication packages are expected for empirical work.

## Structure & house style

- The introduction states the question, the novel contribution, the approach, and the result, and makes the case that the advance is new relative to the frontier.
- Lead with what is new — model, method, or result — and let the rest of the paper establish it rigorously.
- REStud uses an unstructured abstract and JEL codes; proofs, derivations, robustness, and secondary analyses move to appendices and online supplements.
- Exhibits and propositions should be self-contained; the central new result should be legible on its own.

## Official-submission checklist

- Search the live site for "Review of Economic Studies submission guidelines" / "information for authors" and the data and code availability policy, and follow the current OUP / editorial versions.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and figure/table standards on the submission system.
- Re-check the current data/code deposit and replication-verification workflow — confirm it is enforced before acceptance.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating what is genuinely new — the model, method, or result — relative to the frontier.
- [ ] The contribution is stated as novelty + rigor (theory / method / identification), not as statistical significance.
- [ ] The introduction positions the paper against the current top-5 / frontier work it advances.
- [ ] Theory results are general and proven, or empirics use state-of-the-art identification; the novel claim is fully established.
- [ ] Data and code are ready for the availability + verification workflow.

## Common desk-reject triggers

- A competent paper with no genuine novelty — a standard application or incremental extension.
- An ambitious idea executed without the formal rigor (incomplete proofs, weak identification) the venue demands.
- "First to study X in context Y" framing without a new method, model, or conceptual advance.
- Identification the profession no longer accepts (naive TWFE on staggered adoption, weak IV, cosmetic RDD).

## Re-routing decision

- More technical / formal than topical → `econometrica` (theorem or new estimator with full proofs); general theory → `journal-of-economic-theory`.
- General-interest empirical importance → `american-economic-review`, `quarterly-journal-of-economics`, or `journal-of-political-economy`.
- Excellent but narrower applied micro → `aej-applied-economics` or `review-of-economics-and-statistics`; micro theory → `aej-microeconomics`.
- Macro/growth/dynamics → `aej-macroeconomics`; one crisp single-result idea → `aer-insights`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Review of Economic Studies
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the novelty + rigor clear REStud's frontier bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
