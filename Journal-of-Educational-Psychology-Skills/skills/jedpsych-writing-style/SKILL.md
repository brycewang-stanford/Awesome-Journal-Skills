---
name: jedpsych-writing-style
description: Use when drafting or polishing a Journal of Educational Psychology manuscript to fit its format — generally under 12,000 words (excluding references/tables/figures/appendices), a 250-word abstract, APA 7th-edition style, double-spaced, and fully masked for blind review. Tightens prose and format; it does not invent content.
---

# Writing Style (jedpsych-writing-style)

The Journal of Educational Psychology uses a full-length APA format with real room to develop theory,
method, and results — manuscripts generally **do not exceed 12,000 words** excluding references, tables,
figures, and appendices (检索于 2026-06；以官网为准), with a **250-word abstract**, **APA 7th edition**
style, double-spaced. Writing well here means a disciplined empirical arc that earns its length, stays
**masked**, and keeps the educational-psychology contribution legible throughout. This skill is about
fitting and polishing — not generating claims.

## When to trigger

- Drafting the manuscript or doing final polish
- Over the word budget and needing to cut without losing the argument
- Writing the **250-word** abstract
- Aligning to APA 7th edition and anonymizing for masked review

## The format (know it cold)

- **Length:** generally **≤ 12,000 words** (≈ 40 double-spaced pages, 12-pt Times New Roman),
  **excluding** references, tables, figures, and appendices.
- **Abstract:** **≤ 250 words** on a separate page.
- **Style:** **APA 7th edition**, double-spaced; statistics reported with effect sizes and CIs.
- **Masked review:** the first page omits author names/affiliations; avoid self-identifying grant numbers,
  IRB/institution names, and self-citations phrased in the first person ("our prior work" → third-person).
- **Verify volatile numbers** (word limit, abstract limit, page count) on the official submission page.

## Writing to the format

1. **Earn the length, don't fill it.** 12,000 words is room for a real Introduction, Method, Results, and
   Discussion — not a survey. Every section should advance the contribution (see
   `jedpsych-literature-positioning`).
2. **Front-load the contribution.** State the educational question, the gap, and what is new early; the
   reader should know the contribution before the Method.
3. **Method earns trust.** Report the design at the right level (nesting, randomization, power, measures,
   fidelity) in enough detail to replicate — this is where JEP rigor is judged.
4. **Results report estimates, not just stars.** Effect sizes with CIs and educational interpretation,
   multilevel/SEM detail; lead with the confirmatory tests, label exploratory ones.
5. **Discussion interprets, then bounds.** Lead with what the result means for learning theory and
   practice; state limitations and constraints-on-generality honestly; avoid restating Results.
6. **APA 7th + masked.** Headings, statistics, bias-free language, author-date citations; scrub every
   identity cue before submission.

## Worked micro-example — a 250-word abstract skeleton (illustrative)

For the cluster-randomized reading trial, the abstract states the question, design (with nesting), result
(effect + CI + meaning), and an implication. Confirm the current abstract limit on the official page.

```
[Question] Does teacher-delivered comprehension-strategy instruction improve
transfer to novel texts? [Design] A preregistered cluster-randomized trial
(48 classrooms, 1,089 upper-elementary students) compared strategy
instruction with business-as-usual, using a two-level model with a pretest
covariate. [Result] Strategy instruction raised transfer comprehension
(g = 0.23, 95% CI [0.06, 0.40]; ~2 months of progress); gains in
metacognitive monitoring mediated about 40% of the effect. [Implication]
Explicit strategy instruction produces educationally meaningful, mechanism-
consistent transfer in authentic classrooms. [≈ 110 words; expand to ≤ 250.]
```

## Word-budget allocation (illustrative, full-length)

| Section | Suggested share of body | Note |
|---------|-------------------------|------|
| Introduction | ~20–25% | question, gap, contribution, theory — engage closest priors |
| Method | ~25–30% | design at the right level: nesting, power, measures, fidelity |
| Results | ~20–25% | confirmatory first; effect sizes + CIs; mechanism test |
| Discussion | ~20–25% | meaning + practice, then limitations/constraints |
| (excluded) | references, tables, figures, appendices | do not count toward the limit |

## Cutting-to-format playbook

- Move full measurement models, every robustness specification, and item-level detail to **online
  supplemental material**; cite in one sentence.
- Replace dichotomous "significant" sentences with estimation phrasing — often shorter *and* more
  venue-appropriate.
- If the Discussion restates Results, delete the restatement; lead with interpretation and practice.
- Compress chronological background into engagement with the contrast class (handoff to
  `jedpsych-literature-positioning`).

## Prose-stage reviewer pushback and the venue fix

- "Reads like a review article" → cut survey background; deepen the contrast class and the contribution.
- "Stats without effect sizes" → report effect sizes and CIs inline, with educational interpretation.
- "I can infer who the authors are" → scrub self-citations, grant numbers, site/IRB names for masked review.
- "Over the word limit" → push secondary material to the supplement; confirm the current limit.

## Anti-patterns

- Filling 12,000 words with survey background instead of advancing the contribution
- An abstract over 250 words or missing design/effect/implication
- Results reported as stars without effect sizes, CIs, or educational meaning
- Self-identifying cues (first-person prior work, grant numbers, institution/IRB names) breaking masking
- A Discussion that restates Results instead of interpreting and bounding them

## Output format

```
【Length】body ≤ 12,000 words (excl. refs/tables/figures/appendices)?
【Abstract】≤ 250 words; question + design + effect + implication?
【APA 7th】headings, stats (ES+CI), citations, double-spaced? [Y/N]
【Masked】no names/affiliations/grant#/site/IRB/first-person self-cites? [Y/N]
【Cuts】what moved to online supplemental material
【Next】jedpsych-open-science-and-transparency
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `papaja`, reference managers, reproducible reporting
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — word format, abstract limit, masked review, APA 7th edition
