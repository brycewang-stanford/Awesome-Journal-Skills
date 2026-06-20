---
name: aejmic-writing-style
description: Use when prose buries the result or the abstract/intro do not land for an American Economic Journal: Microeconomics (AEJ: Micro) manuscript. Applies AEA house style and the theory-paper intro arc; it does not produce the result (see aejmic-theory-model) or build exhibits (see aejmic-tables-figures).
---

# Writing Style & the AEJ: Micro Intro Arc (aejmic-writing-style)

## When to trigger

- The introduction opens with machinery (the model's notation, an estimator) instead of the question
- A reader cannot state your main result after the first page
- The abstract describes activities ("we study…") rather than the result
- Late-stage polish before submission (do this **after** the model and proofs settle)

## The AEJ: Micro intro arc

A theory-first AEA journal rewards an introduction that makes a **broad micro audience** see the question and the result fast. The arc:

**question / puzzle → model + equilibrium concept (in words) → main result (a proposition, stated in words) → what drives it / which assumption is doing the work → contribution & scope → brief roadmap.**

- **Open with the economic question**, not the model. A non-specialist should grasp what is being asked in the first breath.
- **State the result in words on page one** — the proposition's content, not its proof. "We show that X, and this happens because Y."
- **Name the driving force** early (which assumption / mechanism delivers the result) — this is the AEJ: Micro reader's payoff and ties to `aejmic-identification`.
- **Frame the contribution as a result with scope**, including what it does *not* establish.
- The literature delta belongs here in one or two sentences (full treatment in `aejmic-literature-positioning`), not a survey.

## AEA house-style conventions

- **Abstract:** short and result-bearing; lead with the result, not the activity. (Confirm the current word limit on the AEA author page — volatile; 检索于 2026-06，以官网为准.)
- **JEL codes and keywords** required.
- **Statistical presentation:** for any empirical/experimental content, report **standard errors / confidence sets, not significance asterisks**.
- **Notation discipline:** define on first use; consistent throughout; avoid clutter.
- **Proofs:** key proofs self-contained in the paper (main text or appendix), not exiled to supplementary files.
- **Single-blind note:** AEJ: Micro review is single-blind (the referee sees the author), so the manuscript need **not** be anonymized — but acknowledgments and self-citations should still read professionally, not promotionally.

## Checklist

- [ ] Intro opens with the **economic question**, not the model/estimator
- [ ] Main result stated **in words on page one**, with its driving force named
- [ ] Contribution framed as a result with explicit scope ("we do not show…")
- [ ] Abstract leads with the result; JEL codes + keywords present
- [ ] No significance asterisks anywhere; SEs / coverage sets where relevant
- [ ] Notation defined at first use and consistent
- [ ] Self-citations and acknowledgments read professionally (single-blind: no anonymization needed)

## Anti-patterns

- Leading the introduction with the model's notation or the estimator (machinery-first)
- An abstract that lists activities ("we develop a model and run an experiment") with no result
- Burying the proposition's content until Section 4
- A literature *survey* in the introduction instead of a one-sentence delta
- Promotional self-citation ("our influential paper") rather than neutral phrasing
- Significance asterisks in tables

## Worked vignette (illustrative)

A draft opens: "We consider a Bayesian game with type space Θ and a sender who commits to a signal π." Rewrite to the arc: "**When can a better-informed seller credibly disclose product quality, and when does it pay to stay vague?** We model disclosure as a commitment to a signal and show the seller-optimal policy pools high types — vagueness is profitable precisely because…". The question leads, the result is on page one, the driving force (pooling preserves credibility) is named. See `../../resources/worked-examples/01-introduction.md`.

## Output format

```
【Intro opens with】question? [Y/N]
【Result on page one】stated in words + driving force named? [Y/N]
【Contribution】result + explicit scope limit? [Y/N]
【Abstract】leads with result; JEL + keywords? [Y/N]
【House style】no asterisks; notation consistent; self-cites professional? [Y/N]
【Next step】aejmic-replication-package (proofs + code) then aejmic-submission
```

## Supplementary resources

- [`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md) — before→after theory-paper intro in AEJ: Micro house style
