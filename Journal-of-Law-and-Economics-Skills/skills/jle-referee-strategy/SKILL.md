---
name: jle-referee-strategy
description: Use when anticipating the objections a law-and-economics referee at The Journal of Law and Economics (JLE) will raise, so a manuscript pre-empts them before submission or addresses them in revision. Plans the defense around JLE's single-blind process; it does not draft the response letter (jle-rebuttal) or run the submission preflight (jle-submission).
---

# Referee Strategy (jle-referee-strategy)

## When to trigger

- The paper is near submission and you want to stress-test it against the referees it will draw
- You need to decide which robustness/legal-design checks to run *before* submitting vs. hold in reserve
- An R&R arrived and you must map referee concerns to concrete responses
- You want to understand how JLE's single-blind process shapes strategy

## How JLE review works (plan around it)

JLE uses **single-blind review**: the **authors' identities are visible to referees** (the title page carries your name), while referees stay anonymous (检索于 2026-06；以官网为准). This changes strategy in two ways. First, **do not anonymize the manuscript** — that is the AEJ/JLEO reflex, not JLE; the title page should name you. Second, because referees know who you are, your **track record and your self-citations are visible**, so positioning honestly and not over-claiming matters more, not less. Referees here are **economists who also know the legal institution**; the modal report attacks (1) whether the institution is described correctly and the rule really binds, (2) the credibility of the legal identification, then (3) magnitude/mechanism and external validity across jurisdictions. Pre-empt the predictable objections in the paper itself.

## The objection map (pre-empt in the paper)

| Referee objection (by design / field) | Pre-emption to build in now |
|----------------------------------------|-----------------------------|
| "You misdescribe the rule / it didn't bind when you say" | precise institutional section: who is bound, effective date, exemptions, enforcement |
| "Staggered TWFE on the law change is biased" | heterogeneity-robust estimator + Bacon decomposition already in the paper |
| "Parallel trends across jurisdictions is not credible" | clean pre-trend leads + honest-DID sensitivity bound |
| "Your control jurisdictions had their own reforms" | documented legal landscape + dropped contaminated controls + placebo legal area |
| "Judge/case assignment isn't random / exclusion fails" | assignment balance + assignment-rule documentation + institutional exclusion argument |
| "RD jump is manipulation / bandwidth-driven" | density test + bandwidth sensitivity + donut; bunching addressed |
| "Effect is selection / confounding, not the rule" | Oster δ / coefficient-stability bounds |
| "Local/LATE legal effect ≠ the policy-relevant effect" | explicit estimand + calibrated cross-jurisdiction scope |
| "Inference too narrow (few states)" | wild-cluster bootstrap / randomization inference |
| "Mechanism is a black box (deterrence vs. incapacitation?)" | a test that distinguishes the channels |
| "Not replicable" | the data/code package built and referenced (`jle-replication-package`) |

## Strategy craft

1. **Get the institution right first.** A law-and-economics referee will dismiss a paper that misstates how the rule works before reaching the econometrics; have an economist-readable, accurate institutions section.
2. **War-game the legal identification.** For each identifying assumption, write the sentence a hostile referee would use; if you cannot answer it in one paragraph + one exhibit, fix it before submitting.
3. **Pre-empt, do not hide.** Address the obvious weakness (the contaminated control, the few-states inference) head-on in the text.
4. **Sequence robustness.** Decisive legal-design checks (re-dating, control-jurisdiction swaps) in the main paper; secondary ones in the appendix.
5. **Anticipate the cross-jurisdiction external-validity ask** — almost guaranteed for a single-state or local design; have the estimand and scope ready.
6. **Make replicability visible** so specification-search suspicion is defused.
7. **Signal institutional credibility.** Because the modal referee knows the law, a careful primary-source institutions section (or genuine institutional expertise on the author team) signals you will not be caught mis-stating the rule — the fastest way to lose a law-and-economics referee.

## What single-blind changes about strategy

Single-blind review is not a neutral detail — it shifts several decisions:

- **Your reputation enters the read.** A junior author cannot hide behind anonymity, and a senior author cannot coast on it; the paper must stand on its identification regardless. Do not assume name recognition substitutes for a clean design.
- **Self-citation is honest, not masked.** You can cite your own prior work normally (no "Author (2023)" contortions), which makes positioning cleaner — but it also means a referee sees exactly how this paper relates to your earlier ones, so the marginal contribution must be real.
- **Tone is visible and remembered.** Because the editor and (often) the field know who you are, a defensive or sloppy submission carries a reputational cost a blinded one does not.
- **Suggested/excluded reviewers.** If Editorial Manager invites reviewer suggestions, use them substantively — name people who know the institution, not just friendly economists.

## Checklist

- [ ] Manuscript **not anonymized** (single-blind; title page names authors)
- [ ] Institutions section accurate and economist-readable (who is bound, when, exemptions, enforcement)
- [ ] Each identifying assumption has a hostile-referee sentence and a one-paragraph+one-exhibit answer
- [ ] The biggest legal-design weakness addressed in the text, not hidden
- [ ] Decisive robustness in the main paper; secondary checks in the appendix
- [ ] Estimand + cross-jurisdiction scope stated to pre-empt the guaranteed ask
- [ ] Replication package referenced; mechanism evidence distinguishes channels

## The guaranteed asks to have ready

Three referee asks are near-certain at JLE; have the answer drafted before submission rather than discovering them in round one: (1) **"Is the rule correctly described and did it bind when you say?"** — answered by a primary-source institutions section; (2) **"With so few legal units, is your inference valid?"** — answered by a wild-cluster bootstrap or randomization inference; (3) **"Does this generalize beyond your jurisdiction/period?"** — answered by an explicit estimand and a calibrated scope statement, not by a sweeping claim.

## Anti-patterns

- **Anonymizing the paper** for a single-blind journal (wrong reflex; the title page should carry your name)
- Misdescribing the legal rule and losing the referee before the econometrics
- Ignoring the obvious design weakness and hoping no referee who knows the institution notices
- Dumping every robustness check into the main text so the paper becomes unreadable
- No estimand statement, guaranteeing a cross-jurisdiction external-validity round-trip
- Treating the replication package as someone else's problem until acceptance

## Worked vignette (illustrative)

A draft on occupational-licensing entry effects is near submission. War-gaming the referees (who know licensing law): the predictable attacks are "your treatment date is the statute's signing, but the board didn't issue rules for a year," "your control states reformed their own licensing," and "11 states is too few for asymptotic clustering." The author pre-empts all three in the paper: dates treatment to the board's effective rules, documents and drops the two contaminated control states, and reports a wild-cluster bootstrap alongside naive clustering. Because review is single-blind, the title page names the authors; nothing is anonymized. The response letter is now reserved for genuinely new asks.

## Output format

```
【Blinding】manuscript NOT anonymized (single-blind, title page named)? [Y/N]
【Institution】accurate, economist-readable section? [Y/N]
【Objection map】per assumption: [objection → pre-emption in paper]
【Biggest weakness】addressed in text? [Y/N] — how: ___
【Robustness placement】main vs appendix split: ___
【External validity】estimand + cross-jurisdiction scope stated? [Y/N]
【Replicability visible】package referenced? [Y/N]
【Next step】jle-submission
```
