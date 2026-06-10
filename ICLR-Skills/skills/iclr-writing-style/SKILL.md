---
name: iclr-writing-style
description: Use when revising an ICLR manuscript for learning-representation framing, OpenReview readability, contribution clarity, limitations, ethics, and reviewer navigation. Use when the core representation insight is buried, when an abstract must read well as an OpenReview snippet, or when adding a "what to verify" path so reviewers can confirm the claim under permanent public review.
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

## Framing that survives public skimming

On OpenReview a reader meets your paper as a title, a TL;DR, and an abstract snippet before opening
the PDF, and the discussion thread is attached forever. The first page must carry the representation
insight unaided.

| Prose risk | ICLR-tuned rewrite | Why it matters under public review |
| --- | --- | --- |
| Insight hidden behind setup | Lead with what changes about representations | Snippet readers never reach page 3 |
| Vague contribution type | Name it: method/theory/analysis/benchmark | Reviewers route papers by type |
| Overclaimed generality | Scope to the tested regime | Public thread will surface the gap |
| Caption as label | Caption as a mini-argument | Reviewers read figures before text |

## Worked vignette

A draft on a new optimizer opens with three paragraphs of background before stating that the method
reduces gradient variance in deep nets. Rewritten, the first sentence names the phenomenon and the
fix, the introduction labels the contribution as "optimization analysis plus method," and a "what to
verify" line points reviewers to the variance-reduction ablation in Section 4. The abstract is
trimmed so its first 40 words stand alone as an OpenReview TL;DR.

## Reviewer-pushback patterns

- "I cannot find the contribution." Put the representation insight in sentence one of the abstract.
- "Claim is broader than the evidence." Scope the wording; the public thread punishes overclaims.
- "Notation is inconsistent." Keep it local; ICLR reviewers span subfields and will flag drift.

## Output format

```text
[ICLR fit sentence] <one sentence>
[First-page problem] <what is hard or missing>
[Contribution type] method / theory / benchmark / analysis / data / systems / application
[Navigation fixes] <intro, figures, claims, appendix map>
[Risky prose] <overclaim, unclear novelty, unsupported generalization>
```

