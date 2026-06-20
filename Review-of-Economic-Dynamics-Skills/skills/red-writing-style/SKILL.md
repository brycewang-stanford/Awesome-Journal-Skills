---
name: red-writing-style
description: Use when applying Review of Economic Dynamics (RED) house style — the stand-alone abstract not exceeding 250 words, author-year (Harvard-style) references, 1 to 6 keywords, LaTeX via Elsevier's elsarticle class under "your paper your way", and the generative-AI declaration. Drafting conventions for a quantitative dynamic paper; it does not invent results.
---

# Writing Style for RED (red-writing-style)

## When to trigger

- Drafting or tightening the abstract, introduction, and front matter for a RED submission
- Setting up references and keywords to RED specifications
- Formatting the manuscript for initial submission

## RED conventions (verified; re-confirm on the official Guide for Authors)

- **Abstract**: concise and factual, **not exceeding 250 words**, and **able to stand alone** —
  references inside the abstract are discouraged. Lead with the question, the model, and the headline
  quantitative result.
- **References**: **author-year (Harvard-style)** citation system; reference list alphabetical and consistent.
- **Keywords**: **1 to 6** required.
- **Formatting**: Elsevier's general Guide for Authors applies; **LaTeX accepted via the `elsarticle`
  class**; initial submission is flexible ("your paper your way"), so you need not fully typeset to
  Elsevier style for the first round.
- **Generative AI**: any use of generative-AI tools must be **declared at submission**.
- **Length**: this pack does not encode a RED-specific manuscript word/page cap. Use the current Guide and
  Editorial Manager prompts for live file constraints; keep the paper as long as the contribution warrants
  and no longer.

## Abstract shape

Use this order:

```text
Dynamic question -> model/mechanism -> discipline/evidence -> headline quantitative result -> implication.
```

Do not begin with data or policy motivation alone. RED readers need to see the dynamic mechanism before
they decide whether the paper belongs in the journal.

## Style notes for dynamic papers

- Make the **mechanism legible before the math** — a reader should grasp the dynamic force from the intro.
- Define the model cleanly; relegate long derivations and proofs to an appendix.
- State magnitudes (the calibrated/estimated number that matters) early and precisely.

## Introduction paragraph order

Use this sequence for RED introductions:

1. Dynamic fact or puzzle.
2. Mechanism and state variable that make the problem dynamic.
3. Model discipline: data moments, calibration, estimation, or theoretical restriction.
4. Headline quantitative result or theorem.
5. Why the result changes how the SED/dynamic-economics audience thinks about the mechanism.

Avoid opening with institutional background that could fit a static paper. The first page should prove
that time, state dependence, expectations, accumulation, adjustment costs, search, or equilibrium dynamics
are essential to the contribution.

## Notation conventions for dynamic-model prose

- Write recursive problems in standard Bellman form — V(a, z) = max over (c, a') of u(c) + βE[V(a', z')|z] —
  defining every state, choice, and shock at first use, and keep symbols stable across the model section,
  the calibration table, and the computational appendix.
- Time variables explicitly (beginning- vs end-of-period assets): timing mismatches between the equations
  and the archived code are a referee-visible error class at a code-first journal.
- Keep the body for the model, the calibration logic, and the experiments; equilibrium-condition
  derivations and algorithm detail go to appendices the body cites by number.
- Give experiment units in-line ("a one-standard-deviation TFP shock", "a transfer of 1% of GDP") rather
  than relying on a figure caption to carry them.

## Abstract rewrite example (illustrative)

```text
WEAK:  "We study inequality and monetary policy in a rich model with many
realistic features and find interesting effects."

RED-SHAPED:  "How does household debt shape monetary transmission? In a
heterogeneous-agent New Keynesian model calibrated to U.S. wealth and MPC
distributions, a 25bp rate cut raises aggregate consumption by 0.4% — twice
the representative-agent benchmark — because constrained borrowers' interest
burdens fall."  (numbers illustrative)
```

The rewrite names the model class, the discipline (wealth and MPC distributions), and the headline
magnitude in three sentences — the pattern a RED desk screen rewards.

## Checklist

- [ ] Abstract ≤250 words, stand-alone, no internal references, headline result stated
- [ ] References clean author-year; list alphabetical and consistent
- [ ] 1–6 keywords supplied
- [ ] AI-use declaration prepared; LaTeX builds under elsarticle

## Anti-patterns

- A 250+-word abstract or one that cannot be read without the paper
- Mixed citation styles instead of clean author-year
- Asserting a manuscript length cap that the current RED Guide does not publish

## Output format

```text
[Style diagnosis] dynamic mechanism clear / static opening / too long / format risk
[Abstract fix] <250-word stand-alone target>
[Intro repair] <paragraph or sequence to rewrite>
[Front matter] keywords / references / AI declaration / LaTeX
[Next step] red-submission or red-tables-figures
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Guide-for-Authors facts and fee/source-precedence notes
