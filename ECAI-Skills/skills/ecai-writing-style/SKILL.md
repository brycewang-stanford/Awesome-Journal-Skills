---
name: ecai-writing-style
description: Use when writing or tightening an ECAI paper body — leading with a general-AI contribution on the first page, matching evidence to claim (a theorem and construction, or a fair empirical comparison), and doing it inside a 7-page body where every paragraph must earn its space.
---

# ECAI Writing Style

ECAI reviews a **7-page body** across the full breadth of AI (symbolic reasoning, KR, planning,
search, multi-agent systems, ML, and applications). Two things follow, and they drive most of the
advice here: the contribution must be legible to a **general** AI audience, and the writing must be
**dense** — at 7 pages there is no room for a paragraph that does not carry the argument.

## The ECAI first-page arc

Land the whole contribution before the fold:

1. **A well-posed AI problem** — stated as a problem, not as "X has become popular."
2. **Why current methods are inadequate** — the specific gap, in one or two sentences.
3. **The contribution** — the mechanism, and where the claim is provable, the **guarantee**.
4. **Evidence proportional to the claim** — a theorem + construction, and/or a fair empirical
   comparison; named on the first page, delivered in the body.
5. **What it means for AI** — why a general AI audience should care.

The worked example ([`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md))
shows this arc rebuilt from a benchmark-first draft.

## Lead with the AI contribution, not the application of a model

The most common re-route signal is a paper that leads with "we apply <model> to <task>." ECAI
rewards a contribution that **generalizes** — a mechanism, a guarantee, a characterization, an
understanding — over a single benchmark delta. Apply the **model-swap test**: if you replaced the
underlying model/solver with another, would a lasting AI lesson remain? If not, the paper may belong
at a pure-ML venue (`ecai-topic-selection`).

## Match evidence to the claim shape

ECAI's breadth means the *right* evidence differs by contribution:

| Claim shape | Evidence ECAI expects |
|---|---|
| "This always holds / is complete / is optimal" | A **proof**, with all assumptions explicit |
| "This is more efficient / expands fewer nodes" | A **controlled comparison** vs a fair baseline, with spread |
| "This learns better / calibrates better" | A fair empirical comparison, seeds, and a reason *why* (not just a number) |
| "This works in deployment" | A credible real-world demonstration (route to **PAIS**) |

A provable claim asserted only empirically is a weakness a reviewer will name; a purely empirical
claim dressed as a theorem is worse.

## Density discipline (the 7-page reality)

- **Paragraph one carries the contribution.** Do not spend the opening on the importance of AI.
- **Cut the roadmap.** At 7 pages the paper cannot afford a "Section 2 does X, Section 3 does Y"
  preview; a single orienting sentence is enough.
- **Define once, precisely.** Symbolic-AI reviewers check every later lemma against your
  definitions; sloppy notation costs you the proof's credibility.
- **One figure doing three jobs** beats three figures. Merge panels; caption them to be
  self-contained.
- **Push detail, keep the idea.** Full proofs and extra tables go to the supplement; the *idea* and
  the *decision-critical* result stay in the body (`ecai-supplementary`).

## Threats / limitations as argument, not boilerplate

State the honest boundary of the claim where it lives — the assumption the theorem needs, the
regime where the method stops helping, the confound the experiment cannot rule out. In a
single-round, no-revision process (`ecai-review-process`), a limitation you name yourself is far
cheaper than one a reviewer discovers.

## Language and audience

- Write for a **broad** AI reader: define subfield jargon, motivate why a planning/KR/ML reader
  should care even if it is not their area.
- ECAI is an international European venue; keep the English clear and the claims measured — EurAI's
  reviewer pool spans many first languages and subfields.
- Avoid overclaiming ("revolutionizes," "solves"); ECAI rewards a precise, bounded contribution.

## Anti-patterns

- **Benchmark-first abstract** that never states an AI problem.
- **Model-as-contribution** with no lesson surviving a model swap.
- **Proof by assertion** — a completeness/optimality claim with no proof.
- **Roadmap padding** eating the 7-page budget.
- **Decision-critical content in the supplement** because the body ran long.

## Output format

```text
[First-page arc] problem / inadequacy / contribution+guarantee / proportional evidence / meaning — all present?
[Model-swap test] does an AI lesson survive swapping the model/solver? yes/no
[Evidence match] claim shape -> proof and/or fair comparison present? gaps: <list>
[Density] roadmap trimmed? paragraph one carries the contribution? figures merged?
[Limitations] stated as argument where the claim lives? yes/no
[Budget] decision-critical content inside 7 pages? yes/no
```
