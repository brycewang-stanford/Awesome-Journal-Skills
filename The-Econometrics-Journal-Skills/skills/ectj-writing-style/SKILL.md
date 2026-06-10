---
name: ectj-writing-style
description: Use when revising a The Econometrics Journal (EctJ) manuscript for compact RES/OUP style covering the 150-word summary, the roughly 20-page printed-paper discipline, theorem readability, one-page simulation summaries, applied-value clarity, and template-conformant prose that survives the desk screen.
---

# EctJ Writing Style

Use this when the paper is correct but too diffuse for EctJ.

## Style rules

- Write the summary in no more than the current word limit; RES guidance states a 150-word
  summary.
- Keep the paper near the current printed-paper cap; RES guidance says manuscripts should not
  normally exceed 20 pages including the printed appendix.
- Use the RES/EctJ LaTeX template and the separate online-appendix template when applicable.
- Put assumptions close to the theorem or estimator they support.
- Prefer short theorem interpretation paragraphs over long verbal restatements of algebra.
- Cut general econometrics motivation that does not help the leading case.
- Summarize simulation results compactly in the main text, normally within about one page,
  pushing full grids to the appendix.
- Treat conformance as part of the science: EctJ instructions state that submissions not
  conforming to the guidelines are rejected routinely, so style and format are a screen,
  not cosmetics.

## Compression moves

- Replace broad motivation with the econometric failure mode in the first paragraph.
- Replace a long literature survey with a closest-paper contrast table or two compact paragraphs.
- Convert repeated theorem intuition into one theorem interpretation paragraph after the statement.
- Move full simulation grids to the supplement and keep only the table that identifies the boundary case.
- Put empirical application details after the method has earned them; the application proves value, not
  venue fit by itself.

## EctJ page-budget pass

Before line editing, build a one-page ledger:

- **Opening claim**: one paragraph that names the econometric object, the failure of existing tools, and
  the leading-case result.
- **Theory core**: every assumption, theorem, proof sketch, and interpretation paragraph must have a
  visible job. If a proof step is essential to credibility, keep it in the printed paper or printed
  appendix rather than hiding it behind supplementary detail.
- **Simulation core**: keep the design that tests the sharpest assumption or approximation. Push
  alternative grids, tuning sweeps, and robustness tables to the online appendix.
- **Application core**: state why the empirical illustration is diagnostic for the method; remove
  institutional background that does not change interpretation of the estimator, test, or procedure.
- **Related work**: keep citations near the claim they discipline. A citation that does not define the
  incumbent method, the relaxed assumption, or the applied use case is a cut candidate.

After the ledger, revise in this order: summary, introduction, theorem statements, simulation captions,
application paragraph, then appendix cross-references. This catches the highest-friction EctJ style
problems before sentence polishing.

## Theorem-prose conventions for RES/OUP print

- State assumptions as numbered, referenced objects ("Assumption 3 fails when...") so the
  interpretation paragraphs can point at them; unnamed inline conditions cannot be audited within
  a compact paper.
- After each theorem, write one paragraph answering three questions: what the result lets an
  applied user do, which assumption does the real work, and where the simulation confirms the
  finite-sample counterpart.
- Notation is a budget item: a symbol introduced for one equation is a cut candidate; the EctJ
  page discipline rewards reusing standard notation from the closest published treatment.
- Write simulation prose as findings, not procedure ("coverage stays near nominal until the rate
  condition fails at n=250" — illustrative phrasing), since design details belong to notes and
  the supplement under the one-page summary norm.

## Page-leak patterns

Three sentence-level habits consume EctJ pages fastest: restating the theorem in words directly
after its formal statement; defending each assumption against every conceivable objection rather
than the one a referee will actually raise; and narrating the application's institutional history.
Each deleted instance typically buys back a paragraph; across a draft this is often the difference
between 22 printed pages and a conforming 19.

## Output format

```text
[Style diagnosis] compact / too long / too abstract / under-applied
[Summary fix] <150-word target or revision notes>
[Page compression] <move, cut, or merge>
[Template risk] <style, appendix, proof placement>
[Clarity edit] <specific paragraph fix>
```
