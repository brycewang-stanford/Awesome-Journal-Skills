---
name: jape-topic-selection
description: Use when deciding whether a project fits the Journal of Applied Econometrics (JAE) — an applied (not pure-theory) journal publishing empirical, replicable work that applies or develops econometric techniques on real data. Tests scope fit, the replicability requirement, and the Research vs. Replication Article tracks before you commit.
---

# Topic Selection for JAE (jape-topic-selection)

## When to trigger

- Choosing where to send an empirical or method-application paper and weighing JAE
- Unsure whether your idea is "applied enough" or "too theoretical" for JAE
- Deciding between a standard Research Article and JAE's Replication Article track

## JAE's scope test

JAE publishes **applied** econometrics: papers that **apply and develop econometric techniques on real data**, with the focus on the *application* rather than pure econometric theory. A purely theoretical contribution (a new estimator with asymptotics but no real-data application) is off-fit — route it to a methods/theory outlet. A good JAE topic does one of:

- Applies an established or newly adapted method to a substantive economic question on real data, with credible inference;
- Develops a technique but **anchors it in a real-data application** that demonstrates and tests it; or
- **Replicates** previously published empirical results (the dedicated **Replication Article** category), reporting successes *and* failures.

## The non-negotiable filter: replicability

Because accepted papers must deposit data and code in the **JAE Data Archive** (since 1994, now at ZBW, unless confidential), ask *before* you start: can the data behind every result be deposited as plain ASCII/CSV with a readme, or at minimum documented enough that others can apply for access? If the data can be neither shared *nor described* for access, the project is a poor JAE fit.

## Fit matrix

Score the candidate on five gates before drafting:

- **Economic question**: the paper answers a substantive question, not only demonstrates an estimator.
- **Econometric lesson**: readers learn when or why a method changes an applied conclusion.
- **Real-data anchor**: the central evidence uses actual data, not only simulation or asymptotics.
- **Replication path**: every result can be regenerated from depositable or clearly documentable inputs.
- **Article track**: the paper is either a standard applied contribution or a Replication Article; do not
  mix the two without saying which promise is primary.

If any gate fails, redirect early. JAE fit is strongest when the data, method, and applied question are
mutually necessary; it is weakest when one of the three can be removed without changing the paper.

## Scope verdict table

Pattern-match the project against recurring candidate shapes:

| Project shape | JAE verdict | Why |
| --- | --- | --- |
| New estimator + asymptotics + small empirical illustration | Borderline | Fit hinges on whether the application carries the paper; if the illustration is decorative, reroute to a theory/methods outlet |
| Established method, new real-data finding with credible inference | Strong fit | The venue's bread and butter — provided the deposit is feasible |
| Pure Monte Carlo comparison of estimators | Off-fit alone | Anchor the simulations to a real empirical problem or send to a methods journal |
| Re-examination of a prominent published result using its archived data | Strong fit (Replication Article) | The dedicated track exists exactly for this |
| Policy evaluation on administrative data that can never be shared or described | Poor fit | The mandatory archive deposit cannot be satisfied even via the confidential-data readme route |

## Choosing a Replication Article target

The track rewards replications of *prominent* papers — results people teach, cite, or build policy on. Screen a target on four points: (i) the original's data are archived (ideally in the JAE Data Archive) or otherwise reconstructible; (ii) the claim is sharp enough that confirm/qualify/overturn is decidable; (iii) you can separate data-revision effects from coding differences from genuine fragility; (iv) a negative result would still be informative — JAE's track publishes failures as well as successes, which is rare and worth exploiting. Replicating an obscure paper, or one whose data are gone, fails the screen however careful the execution.

## Worked fit assessment: two candidates (illustrative)

Candidate A: a new shrinkage estimator with proofs, demonstrated on one well-worn growth dataset where it barely changes the estimates. The real-data anchor is decorative — redirect to a methods venue, or find an application where shrinkage flips a conclusion. Candidate B: quarterly energy-demand elasticities for 14 countries, where switching from textbook HAC to a few-cluster-appropriate bootstrap moves the headline elasticity from "significant at 5%" to marginal — an applied question, an econometric lesson, public data exportable to CSV. B is the JAE paper despite A being technically deeper.

## Output format

```
【Scope】applied on real data? [Y/N] | pure-theory risk? [Y/N]
【Replicable】data depositable or documentable? [Y/N]
【Lesson】method choice changes an applied conclusion? [Y/N]
【Track】Research Article / Replication Article
【Verdict】JAE fit / redirect → where
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JAE scope and Data Archive sources
