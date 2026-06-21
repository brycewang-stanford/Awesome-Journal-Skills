---
name: cogpsych-writing-style
description: Use when drafting or polishing a Cognitive Psychology (Elsevier) manuscript — a long-form, integrative article that must weave multiple experiments and a formal model into one continuous theoretical argument. Tightens structure, the experiment-to-model narrative, and APA-style reporting; it does not invent content. Verify the journal's current length and format guidance on the official page.
---

# Writing Style (cogpsych-writing-style)

Cognitive Psychology publishes **longer, integrative articles**, so the challenge is the opposite of a
short-report journal: the danger is not the word limit but **losing the argument across many
experiments and a model**. Writing well here means making a multi-experiment program plus a formal
model read as **one cumulative theoretical argument**, in clear scientific prose with rigorous
(APA-style) statistical reporting.

## When to trigger

- Drafting the Introduction/General Discussion or doing a structural pass
- A series of experiments reads as a list rather than a single argument
- Integrating the model exposition with the empirical sections
- Aligning statistical reporting and references to the journal's style before submission

## Writing the long-form, model-driven paper

1. **Front-load the theoretical claim.** State the question, the rival accounts, and the contribution in
   the Introduction (see `cogpsych-literature-positioning`). The reader should know what is at stake
   before Experiment 1.
2. **Make each experiment a step in the argument.** Open each experiment with the specific question it
   answers and what it adds (rules out a confound, tests a divergent prediction); close with a brief
   bridge to the next. Avoid a flat "Experiment N: Method/Results" list.
3. **Integrate the model, don't append it.** Introduce the model where it does explanatory work — often
   alongside the experiments it explains — not as a detached final section the empirical reader skips.
4. **General Discussion earns its length.** Synthesize across experiments and the model fit; state the
   theoretical advance and its scope; keep limitations honest. This is where the integrative payoff is
   delivered, not a restatement of each Results section.
5. **Report statistics rigorously.** Effect sizes with intervals for behavior, model-comparison criteria
   for fits, exact test statistics; APA-style author-date citations and reference formatting. Confirm
   the current style requirements on the official guide for authors.

## Structure that keeps a multi-experiment paper coherent

| Section | Job | Failure mode to avoid |
|---------|-----|-----------------------|
| Introduction | question + rival accounts + contribution | chronological phenomenon history |
| Model (where introduced) | formalization + what each parameter means | a detached "the model" section nobody reads |
| Experiments 1..k | each adds inference, with a bridge | a flat list of independent studies |
| General Discussion | synthesis + theoretical advance + scope | restating each Results section |

## Worked micro-example — making experiments cohere (illustrative)

For the recognition-memory program, the General Discussion turns three experiments into one claim:

```
Weak: "Experiment 1 found a linear z-ROC. Experiment 2 also found a linear
       z-ROC. Experiment 3 found a linear z-ROC."
Strong: "Across three experiments engineered to make z-ROC shape diagnostic -
       and after ruling out a list-composition confound (Exp 2) and testing a
       further divergent prediction (Exp 3) - the z-ROC was reliably linear,
       the qualitative signature UVSD predicts and DPSD forbids. The single
       continuous-strength account is thus favored not by a fit index alone
       but by a pattern the rival cannot produce."
```

## Cohesion playbook

- Replace "Experiment N also showed X" with "having established X, we next asked whether..." — make the
  series a chain of questions, not a pile of studies.
- Put procedural detail in Method and lengthy derivations/recovery in an appendix/supplement so the main
  narrative stays about the theory.
- Replace dichotomous "significant" sentences with estimation/model-comparison phrasing — more precise
  and more venue-appropriate.
- If the General Discussion restates Results, cut it; lead with the cross-experiment synthesis and the
  theoretical advance.

## Prose-stage reviewer pushback and the venue fix

- "Reads as a list of experiments" → add the question-and-bridge structure; synthesize in the General
  Discussion.
- "The model feels bolted on" → introduce it where it explains the data; connect each experiment to a
  model prediction.
- "Stats without effect sizes / model comparison" → report intervals and comparison criteria, not stars.
- "Too long for what it says" → length must buy integration; cut redundant per-experiment recaps.

## Anti-patterns

- A multi-experiment paper written as independent, disconnected studies
- A formal model quarantined in a section detached from the experiments
- A General Discussion that restates each Results section instead of synthesizing
- Statistics reported without effect sizes/intervals or without model comparison
- Length used to pad rather than to integrate the program

## Output format

```
【Theoretical claim front-loaded】question + rivals + contribution? [Y/N]
【Experiments cohere】each adds inference, with bridges? [Y/N]
【Model integrated】introduced where it explains, not appended? [Y/N]
【General Discussion】synthesis + advance + scope, not restatement? [Y/N]
【Reporting】effect sizes/intervals + model comparison + APA style? [Y/N]
【Next】cogpsych-open-science-and-transparency
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, reproducible reporting (Quarto/R Markdown), `papaja`
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — article length, style, and reference format
