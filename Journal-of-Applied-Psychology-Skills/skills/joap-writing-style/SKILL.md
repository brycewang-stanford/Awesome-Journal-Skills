---
name: joap-writing-style
description: Use when drafting or polishing a Journal of Applied Psychology (JAP) manuscript to fit APA 7th-edition style, the I-O contribution-forward narrative arc, and the article-type length norms (Feature Article commensurate with contribution; tighter Research Report). Tightens prose, structure, and style; it does not invent content.
---

# Writing Style (joap-writing-style)

JAP prose is **theory-forward, precise, and APA 7th-edition** throughout. The introduction must make
the **theoretical contribution unmistakable**, the method and results must be reported to a high
disclosure standard, and the discussion must interpret meaning and boundary conditions — not restate
results. Length is **commensurate with the contribution** (a Feature Article can be substantial; a
Research Report is tighter). This skill fits and polishes; it does not generate claims.

## When to trigger

- Drafting the Introduction/Discussion or doing final polish
- Writing the structured abstract
- Aligning the manuscript to APA 7th edition before submission
- A reviewer said the writing buries the contribution, over-claims, or wanders

## The JAP narrative arc

1. **Introduction: contribution by the third page.** Phenomenon and stakes → precise gap → the
   theoretical contribution (mechanism, level, boundary) stated against the closest prior work (see
   `joap-literature-positioning`). Do not make reviewers hunt for what is new.
2. **Theory & hypotheses: deductive.** Each hypothesis follows visibly from the stated mechanism; label
   level of analysis; keep the logic tight (see `joap-theory-and-hypotheses`).
3. **Method: full and replicable.** Sample, procedure, measures (with reliabilities and validity),
   design, and CMV remedies — enough that a reader could rerun the study.
4. **Results: estimation-first.** Report measurement model, then structural results with effect sizes
   and CIs; separate confirmatory from exploratory.
5. **Discussion: meaning, then boundaries.** Lead with the theoretical and practical implications and
   the boundary conditions; keep limitations honest and specific; end with concrete future directions.

## Abstract (APA 7th, structured)

Write a content-bearing abstract: the question, the theoretical contribution, the design and samples
(including levels and N), the key result (effect + direction + CI where it fits), and the implication.
Confirm the **current abstract word limit** on the official APA page (commonly ~250 words; 待核实).

## Worked micro-example — abstract clauses (illustrative)

For the servant-leadership package, every clause earns its place.

```
[Question] Do servant leaders raise team performance, and through what process?
[Contribution] We identify team psychological safety as a cross-level mechanism
  and task interdependence as its boundary.
[Design/samples] A two-wave multilevel field study (612 employees in 74 teams)
  and a lab experiment.
[Result] Servant leadership raised performance via team psychological safety
  (indirect = .13, 95% CI [.05, .23]); the experiment confirmed the safety path.
[Implication] Leadership develops performance by building safety, not by
  monitoring — with implications for leader development and team design.
[≈ confirm length against the official limit before submission.]
```

## APA 7th essentials (know them cold)

- Headings, bias-free language, author-date citations, and a complete reference list.
- Statistics reported with effect sizes and CIs; exact p-values; report fit indices for SEM.
- Tables and figures formatted to APA 7th; numbers, abbreviations, and statistical notation consistent.
- Manage references with a tool; an APA CSL style or `papaja` keeps formatting clean.

## Cutting / tightening playbook

- Move secondary analyses, full invariance tables, and alternative models to **online supplemental
  materials**; cite in one sentence.
- Convert background prose into anchor citations (handoff to `joap-literature-positioning`).
- Replace dichotomous "significant" sentences with estimation phrasing — often shorter and more
  venue-appropriate.
- If the Discussion restates Results, delete the restatement; lead with theoretical meaning and boundaries.

## Prose-stage reviewer pushback and the venue fix

- "I can't tell what the contribution is" → state the mechanism/boundary explicitly in the
  introduction; do not defer it to the discussion.
- "Over-claims causation" → scale the language to the design; reserve causal verbs for the experimental
  evidence.
- "Discussion just restates results" → lead with theoretical implications and boundary conditions.
- "Stats without effect sizes/CIs" → report estimates with CIs inline; this is non-negotiable here.

## Anti-patterns

- A long construct history that delays the contribution
- Causal language unsupported by the design
- A discussion that restates results instead of interpreting meaning and boundaries
- An abstract that omits the contribution, design, samples, or key result
- Stats reported without effect sizes / confidence intervals; inconsistent APA notation

## Output format

```
【Contribution legible by p.3?】[Y/N]
【Hypotheses deductive + levels labeled?】[Y/N]
【Method replicable + CMV remedies stated?】[Y/N]
【Results estimation-first (ES + CI) + confirmatory/exploratory split?】[Y/N]
【Discussion: meaning + boundaries, not restatement?】[Y/N]
【Abstract】structured + within current limit (待核实)?
【APA 7th consistent?】[Y/N]
【Next】joap-open-science-and-transparency
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `papaja`, reference managers, APA CSL styles, reproducible reporting
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — APA 7th edition, abstract limit, article-type length norms
