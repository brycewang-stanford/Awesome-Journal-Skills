---
name: iclr-writing-style
description: Use when revising an ICLR manuscript for learning-representation framing, OpenReview readability, contribution clarity, limitations, ethics, and reviewer navigation.
---

# ICLR Writing Style

Use this to turn a technically correct draft into an ICLR-readable paper. The style should make the
learning-representation contribution easy to evaluate under public review.

## ICLR framing

- State the representation, learning problem, or model-behavior insight in the first page.
- Make clear whether the contribution is method, theory, benchmark, analysis, dataset, evaluation,
  systems support, or application-driven ML.
- Explain why the result changes how the community should train, evaluate, understand, or deploy
  learning systems.
- Avoid hiding the core idea behind implementation detail or benchmark trivia.
- Connect limitations to real deployment, robustness, safety, fairness, or data constraints when
  those issues are relevant.

## Reviewer navigation

- Give reviewers a short "what to verify" path: main theorem, key ablation, benchmark setting,
  reproducibility artifact, or appendix section.
- Use figure captions as mini-arguments, not labels.
- Keep notation local and consistent; ICLR reviewers span subfields.
- Use the appendix to answer predictable objections, but do not move decisive evidence out of the
  main narrative.
- Write the abstract and introduction so the paper still makes sense when read through OpenReview
  snippets and search.

## Output format

```text
[ICLR fit sentence] <one sentence>
[First-page problem] <what is hard or missing>
[Contribution type] method / theory / benchmark / analysis / data / systems / application
[Navigation fixes] <intro, figures, claims, appendix map>
[Risky prose] <overclaim, unclear novelty, unsupported generalization>
```

