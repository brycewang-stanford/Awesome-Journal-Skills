---
name: aeja-referee-strategy
description: Use when anticipating the objections a sophisticated American Economic Journal: Applied Economics (AEJ: Applied) referee will raise, so a manuscript pre-empts them before submission or addresses them in revision. Plans the defense; it does not draft the response letter (aeja-rebuttal) or run the submission preflight (aeja-submission).
---

# Referee Strategy (aeja-referee-strategy)

## When to trigger

- The paper is near submission and you want to stress-test it against the referees it will draw
- You need to decide which robustness checks to run *before* submitting vs. hold in reserve
- An R&R arrived and you must map referee concerns to concrete responses
- You want to understand how AEJ: Applied's single-blind peer-review process shapes strategy

## How AEJ: Applied review works (plan around it)

AEJ: Applied uses **single-blind review** through the AEA ScholarOne system: author identities are visible to referees, while referee identities remain anonymous to authors. An editor assigns the paper to a coeditor or handles it directly, and before a first R&R the handling coeditor consults a second coeditor. Referees here are **identification-literate applied microeconomists**; the modal report attacks the *credibility of the design* first, then magnitude/mechanism, then external validity. The editor weighs whether the contribution is novel *and* the design clears the bar. Plan to **pre-empt the predictable objections in the paper itself**, leaving the response letter for genuinely new asks.

## The objection map (pre-empt in the paper)

| Referee objection (by design) | Pre-emption to build in now |
|-------------------------------|-----------------------------|
| "TWFE is biased under staggered timing" | heterogeneity-robust estimator + Bacon decomposition already in the paper |
| "Parallel trends is not credible" | clean pre-trend leads + honest-DID sensitivity bound |
| "Instrument is not excludable" | institutional + theoretical exclusion argument + falsification tests |
| "RD jump is manipulation / bandwidth-driven" | density test + bandwidth sensitivity + donut |
| "Effect is just selection / confounding" | Oster δ / coefficient-stability bounds |
| "Local/ITT effect ≠ the policy-relevant effect" | explicit estimand + calibrated external-validity discussion |
| "Inference too narrow (few clusters)" | wild-cluster bootstrap / randomization inference |
| "Mechanism is a black box" | a test that distinguishes the proposed channel from rivals |
| "Not reproducible" | the openICPSR package built and referenced (`aeja-replication-package`) |

## Strategy craft

1. **War-game the design.** For each identifying assumption, write the sentence a hostile referee would use; if you cannot answer it in one paragraph + one exhibit, that is a hole to fix before submission.
2. **Pre-empt, do not hide.** Address the obvious weakness head-on in the text; referees punish papers that ignore the elephant.
3. **Sequence robustness.** Put decisive checks in the main paper; hold secondary ones for the appendix/online appendix so the paper stays readable.
4. **Anticipate the external-validity ask.** It is almost guaranteed for a local design — have the estimand and scope statement ready.
5. **Make reproducibility visible.** A referee who sees a clean package is less inclined to suspect specification search.

> The shared, venue-neutral objection catalog is in [`../../resources/README.md`](../../resources/README.md) (links to the empirical-methods hub) — walk it before drafting.

## Checklist

- [ ] Title/byline/front matter align with AEJ: Applied's single-blind process
- [ ] Each identifying assumption has a written hostile-referee sentence and a one-paragraph+one-exhibit answer
- [ ] The paper's biggest weakness is addressed in the text, not hidden
- [ ] Decisive robustness in the main paper; secondary checks in the appendix
- [ ] Estimand + external-validity scope stated to pre-empt the guaranteed ask
- [ ] Reproducibility package referenced so specification-search suspicion is defused
- [ ] Mechanism evidence distinguishes the proposed channel from rivals

## Anti-patterns

- Ignoring the obvious design weakness and hoping no referee notices
- Writing self-citations or acknowledgments as if the venue required anonymous review
- Dumping every robustness check into the main text so the paper becomes unreadable
- No estimand statement, guaranteeing an external-validity round-trip
- Treating the replication package as someone else's problem until acceptance

## Output format

```
【Front matter】single-blind title/byline and disclosures ready? [Y/N]
【Objection map】per assumption: [objection → pre-emption in paper]
【Biggest weakness】addressed in text? [Y/N] — how: ___
【Robustness placement】main vs appendix split: ___
【External validity】estimand + scope stated? [Y/N]
【Reproducibility visible】package referenced? [Y/N]
【Next step】aeja-submission
```
