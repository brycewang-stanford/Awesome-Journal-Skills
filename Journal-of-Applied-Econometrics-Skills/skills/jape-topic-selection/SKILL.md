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

## Output format

```
【Scope】applied on real data? [Y/N] | pure-theory risk? [Y/N]
【Replicable】data depositable or documentable? [Y/N]
【Track】Research Article / Replication Article
【Verdict】JAE fit / redirect → where
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JAE scope and Data Archive sources
