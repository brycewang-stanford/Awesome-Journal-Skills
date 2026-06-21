---
name: cogpsych-workflow
description: Use when starting or navigating any Cognitive Psychology (Elsevier) manuscript and you are unsure which sub-skill applies. Use when choosing among manuscript types or returning with a decision letter. Routes by lifecycle stage and contribution type (multi-experiment empirical, experiment-plus-model, modeling-led, theoretical/review), and flags the journal's long-form, model-driven house style and code-transparency expectations. It dispatches; it does not draft content.
---

# Cognitive Psychology Workflow Router (cogpsych-workflow)

The orchestrator for a Cognitive Psychology (Elsevier) submission. The journal's two defining features
are that it rewards **longer, integrative, model-driven papers** — typically a **multi-experiment
program tied to a formal/computational model** — and that it expects **data, model code, and analysis
scripts** to be shareable. The router makes sure the contribution is theory-and-model-shaped from the
start, then sends the user to the matching skill.

## When to trigger

- Starting a new Cognitive Psychology paper and unsure where to begin
- Mid-project and unsure which skill applies next
- Choosing the contribution type (empirical-only vs. experiment-plus-model vs. modeling-led)
- Returning with a decision letter (route to `cogpsych-rebuttal`)

## First question: contribution type

| Situation | Type | Route note |
|-----------|------|-----------|
| Several controlled experiments that jointly constrain a theory | **Multi-experiment empirical** | main pipeline; make each experiment add inference, not repeat |
| Experiments **plus** a fitted formal model (the common shape here) | **Experiment + model** | pull `cogpsych-theory-and-hypotheses` (formalize) + `cogpsych-data-analysis` (fit/compare) forward |
| A new model / analysis tested against existing or new data | **Modeling-led** | `cogpsych-theory-and-hypotheses` → `cogpsych-data-analysis` (model recovery + comparison) |
| Integrative theoretical synthesis or review with a substantive advance | **Theoretical / review** | `cogpsych-literature-positioning` + `cogpsych-theory-and-hypotheses` |

> A single short experiment reporting one effect is usually the **wrong shape** for this venue — that
> is a Psychological Science / short-report contribution. Cognitive Psychology wants the longer arc.

## Routing map (stage → skill)

```text
Idea / fit?                          → cogpsych-topic-selection
Theory + model + predictions?        → cogpsych-theory-and-hypotheses
Where does it sit in the field?      → cogpsych-literature-positioning
Experiments / stimuli / power?       → cogpsych-study-design
Analysis + model fit/comparison?     → cogpsych-data-analysis
Exhibits (data + model fit)?         → cogpsych-tables-figures
Long-form prose clear?               → cogpsych-writing-style
Data + model code + materials open?  → cogpsych-open-science-and-transparency
How will it be judged?               → cogpsych-review-process
Ready to submit (Editorial Manager)? → cogpsych-submission
Got an R&R / decision?               → cogpsych-rebuttal
```

## Default order

`topic-selection → theory-and-hypotheses → literature-positioning → study-design → data-analysis →
tables-figures → writing-style → open-science-and-transparency → review-process → submission → rebuttal`

Theory comes **before** positioning here on purpose: the formal model *is* the contribution, so
formalize the account first, then position it against rival models. For experiment-plus-model papers,
the model is co-designed with the experiments — iterate `theory-and-hypotheses` ↔ `study-design`.

## Worked micro-example — routing a live project (illustrative)

A team has three preregistered recognition-memory experiments and a competing pair of models
(unequal-variance signal detection vs. a dual-process account) they want to fit and compare.

```
Type:    Experiment + model (multi-experiment program, model comparison).
Entry:   not idea-stage → skip topic-selection; they are at theory/design/analysis.
Route:   theory-and-hypotheses (formalize both models + the predictions that
            separate them)
         → study-design (stimuli, list construction, power for the critical
            contrast across all three experiments)
         → data-analysis (fit both models; compare with AIC/BIC + Bayes
            factors; report parameter recovery)
         → tables-figures (overlay model fit on data, not bars of means)
         → writing-style (integrate three experiments into one argument)
         → open-science-and-transparency (deposit data + model code + scripts)
         → submission (Editorial Manager) ; on R&R → rebuttal.
Flag:    the model comparison must be pre-committed where possible and the
         fits reproducible from the deposited code.
```

## Stage-triage table (symptom → skill)

| What the author says | Stage | Route to |
|----------------------|-------|----------|
| "Is one experiment enough for this journal?" | fit | `cogpsych-topic-selection` |
| "I have data but no formal model" | theory | `cogpsych-theory-and-hypotheses` |
| "Which model is better, AIC or BIC?" | analysis | `cogpsych-data-analysis` |
| "Reviewer says my experiments don't constrain the theory" | design | `cogpsych-study-design` |
| "How do I show model fit, not just means?" | exhibits | `cogpsych-tables-figures` |
| "Reviewer can't run my model code" | transparency | `cogpsych-open-science-and-transparency` |
| "I have an R&R" | revision | `cogpsych-rebuttal` |

## Routing pitfalls specific to this venue

- Sending an experiment-only project straight to `cogpsych-submission` without a formal model or an
  integrative theoretical payoff — the journal's identity is model-driven theory development.
- Treating the model as an afterthought bolted on at the end, instead of co-designing experiments to
  discriminate models from the start (iterate `theory-and-hypotheses` ↔ `study-design`).
- Deferring `cogpsych-open-science-and-transparency`: model code and fits should be reproducible from
  deposit, not promised at acceptance.

## Anti-patterns

- Pitching a single-experiment, single-effect paper (wrong length/ambition for this venue)
- Reporting experiments with no formal model and no integrative theoretical advance
- A model that is described in prose but never fit to data or compared to a rival
- Leaving data/model code/scripts unshareable until acceptance

## Output format

```
【Stage】idea / theory / positioning / design / analysis / exhibits / writing / transparency / review / submit / rebut
【Type】Multi-experiment empirical / Experiment + model / Modeling-led / Theoretical-review
【Route to】cogpsych-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — modeling, model-comparison, mixed-model and preregistration tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Cognitive Psychology / Elsevier URLs behind every fact in this pack
