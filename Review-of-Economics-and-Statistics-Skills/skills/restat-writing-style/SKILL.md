---
name: restat-writing-style
description: Use when revising the prose of a The Review of Economics and Statistics (REStat) manuscript — especially the abstract and introduction — so the applied question and the estimate land immediately in REStat house style. Polishes framing and prose; it does not change results or identification.
---

# Writing Style (restat-writing-style)

## When to trigger

- The introduction buries the question and the estimate under setup and machinery
- The abstract exceeds REStat's limit or does not state the finding
- A reader cannot say, after one paragraph, what was measured and what it matters for
- Prose is in passive throat-clearing mode ("has been studied extensively")

## The REStat prose bar

REStat is **empirical-first applied economics**, so the intro must put the **applied question, the design, and the headline estimate (with units and a standard error)** on page one. The abstract is **≤100 words** (source map refreshed 2026-06-20), in JEL-suitable form — so every word earns its place. The house style is plain, quantitative economics prose: state the number, state the design that earns it, state why an applied audience cares. REStat's measurement tradition means the writing should also make the **quality of the data/measurement** legible early when that is part of the contribution.

## The REStat introduction arc

1. **Question + headline quantity, first breath.** "When [X] changes, how much does [Y] move?" → "we find [estimate, with units and SE]."
2. **Why it is hard / why prior estimates are unreliable.** The identification or measurement obstacle, named.
3. **Approach.** Data + design (DID / RD / IV / shift-share) + what makes the measurement credible — in one paragraph.
4. **Result restated with mechanism / interpretation** and its uncertainty carried through.
5. **Contribution as a delta against named work** (from `restat-literature-positioning`), with scope honestly bounded.
6. **Brief roadmap** — no over-signposting.

## Abstract rules (REStat)

- **≤100 words**; live-check the current submission guidelines before upload.
- State the question, the design, and the **finding with a number**, not just "we study X."
- JEL-suitable: written so it can be classified; keywords/JEL codes accompany the title page.
- No undefined jargon; an applied economist outside your subfield should follow it.

## Checklist

- [ ] First paragraph states the applied question + the headline estimate (units + SE)
- [ ] Abstract ≤100 words and states the finding with a number
- [ ] Identification/measurement obstacle named before the machinery
- [ ] Approach (data + design + measurement credibility) in one paragraph
- [ ] Contribution framed as a delta against named work, scope bounded
- [ ] Roadmap brief; no over-signposting; active, plain quantitative prose
- [ ] Intro written/finalized AFTER identification and robustness settled

## Anti-patterns

- Leading the intro with the estimator or the data-cleaning, not the question (method-first reads like *J. Econometrics*)
- An abstract that says "we study X" with no number — wasting a ≤100-word budget
- Throat-clearing ("has been studied extensively") and vague stakes
- Burying the headline estimate on page 4
- Over-signposted roadmaps doing the argument's job
- Polishing the intro before the estimate and robustness are final

## Abstract micro-edit (illustrative)

- **Weak (over budget, no number):** "This paper studies the effect of broadband access on rural
  entrepreneurship. Using a difference-in-differences approach exploiting a staggered rollout, we examine how
  internet access shapes business formation and discuss policy implications." — says nothing, spends words.
- **REStat-shaped (≤100 words, states the finding):** "We estimate the effect of rural broadband access on
  small-business formation using a staggered subsidy rollout and a heterogeneity-robust difference-in-
  differences design, correcting for measurement error in rollout dates. Access raises new business
  registrations by 8.1 per 10,000 residents per year (s.e. 1.4), a 14% increase, concentrated where a
  supplier base already existed. The estimate is robust to alternative estimators and few-cluster inference.
  Both the estimator and the measurement correction matter, reconciling earlier near-zero estimates." (≈80 words)

## Worked example pointer

See `../../resources/worked-examples/01-introduction.md` for a before→after REStat-style introduction that executes this arc (fictional, illustrative).

## Output format

```
【Para-1 test】question + estimate (units + SE) present? [Y/N]
【Abstract】word count ≤100? states finding with a number? [Y/N]
【Obstacle named】identification/measurement obstacle before machinery? [Y/N]
【Approach】data + design + measurement credibility in one para? [Y/N]
【Contribution】delta vs named work + bounded scope? [Y/N]
【Prose】active, plain, no throat-clearing? [Y/N]
【Next step】restat-replication-package
```
