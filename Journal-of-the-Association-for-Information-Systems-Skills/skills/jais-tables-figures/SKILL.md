---
name: jais-tables-figures
description: Use when building the exhibits of a Journal of the Association for Information Systems (JAIS) manuscript — tables, figures, the required SEM correlation/covariance matrix, and theory diagrams — so the body remains a self-contained, APA-styled document. Makes exhibits answer the question; it does not write surrounding prose (jais-writing-style) or run the analysis (jais-data-analysis).
---

# Tables & Figures (jais-tables-figures)

## When to trigger

- Exhibits are cluttered, off APA style, or do not answer the question a reader brings to them
- You are relying on multimedia, links, or external files to carry evidence the body should hold
- Your SEM paper has no correlation/covariance matrix exhibit yet
- A theory/framework paper has no diagram, or a diagram that does not match the prose
- A reviewer says a table "buries the result" or a figure "is unreadable in print"

## The JAIS-specific constraint: the body must stand alone

JAIS instructs that the article body may include **"text, tables, and figures only"** and that **"the body should function as a standalone document"**; complex materials go in separate files, and **links and multimedia belong in appendices** (检索于 2026-06；以官网为准). This is a real design constraint: every claim a reviewer needs to evaluate must be readable inside the body, on paper, without clicking out. Design exhibits that work in static, printed form.

## The theory figure earns its place at JAIS

Because JAIS foregrounds theory, the framework or research-model figure is often the most-read exhibit in the paper — sometimes more than the results table. Make it carry real meaning: show the constructs, the directional relationships, the moderators/mediators, and the boundary, and ensure it matches the propositions in the text exactly. A diagram that adds a path the prose never theorizes, or omits one the prose argues, reads as a drafting error and undermines the theoretical contribution. For Theory and Foundational papers especially, invest in a figure that a reader could reconstruct the argument from.

## Make each exhibit answer one question

A JAIS exhibit should have a single job a reader can state in a sentence. A results table answers "what is the estimated relationship and how precise is it?"; a measurement table answers "are the constructs reliable and distinct?"; a theory figure answers "what is the mechanism?" Title and note each exhibit so it is self-contained — readable without hunting through the text.

## Exhibit kit by tradition

| Tradition | Core exhibits | Watch for |
|-----------|---------------|-----------|
| **Behavioral / SEM** | measurement model (loadings, AVE, CR), discriminant-validity table, structural path diagram with effect sizes, **correlation/covariance matrix + descriptives** | the matrix is *required* in an appendix — do not omit it |
| **Economics of IS** | main estimates with clustered SEs, event-study/pre-trends plot, robustness table | report magnitudes; avoid stars-only tables |
| **Design science** | architecture/artifact figure, evaluation-vs-baseline table, ablation table | tie each row back to a design proposition |
| **Theory / conceptual** | the framework diagram, a propositions table | the diagram and the prose must say the same thing |
| **Qualitative** | data-structure figure (codes → themes → dimensions), representative-quotation table | show the path from data to constructs |

## Keep exhibits anonymized for double-blind review

Tables and figures are a common place double-blind anonymity leaks: a screenshot showing an institutional logo or URL, a dataset name that identifies the field site, a figure caption thanking a named funder, or file metadata carrying the author's name. Before submission, scrub every exhibit and its source file — mask identifying screenshots, neutralize site/dataset names, and strip embedded metadata. An exhibit that de-anonymizes the authors triggers the same administrative return as a self-identifying citation, regardless of how strong the evidence is.

## Style and reporting norms

- **APA 6th edition** governs table/figure formatting and notes (JAIS's required reference style) (检索于 2026-06；以官网为准).
- Report **effect sizes / magnitudes**, not significance stars alone; precision (SEs, CIs) belongs in the exhibit.
- Keep figures legible in grayscale print; do not rely on color or interactivity to convey meaning.
- Number and reference every exhibit in the text; an exhibit the prose never points to is noise.

## The required SEM matrix is an exhibit, not an afterthought

For SEM studies JAIS requires "a full correlation matrix or covariation matrix as a part of articles (appendix)," plus descriptives (检索于 2026-06；以官网为准). Treat this as a first-class exhibit you design now: label the constructs clearly, report means, standard deviations, and the inter-construct correlations (with reliabilities on the diagonal where conventional), and place it in the appendix the body points to. Reviewers and Senior Editors use it to re-check discriminant validity and to spot multicollinearity the path diagram hides; an SEM paper that omits it invites an administrative or first-round return.

## Mind the length budget through exhibits

Bloated exhibits push the manuscript toward the **~15,000-word extra-scrutiny zone and the 65-page hard ceiling**. Consolidate redundant tables, move secondary robustness exhibits to an appendix file (while keeping the body self-contained for the main claims), and prefer one clear figure over three partial ones.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JAIS spans empirical and design-science IS; apply the chain below to its causal / econometric papers and note when work is design-science or conceptual.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The body is self-contained: all main-claim evidence is in text/tables/figures, not behind links
- [ ] Each exhibit answers one stated question and is readable standalone (title + note)
- [ ] SEM paper includes the required correlation/covariance matrix + descriptives (appendix)
- [ ] Theory figure and propositions table agree with the prose
- [ ] Magnitudes/effect sizes reported with precision, not stars alone
- [ ] APA 6th formatting; legible in grayscale; every exhibit referenced in text
- [ ] Exhibits trimmed so the manuscript stays within the length budget

## Worked vignette: the figure that breaks the standalone rule (illustrative)

A design-science team showcases its artifact with an interactive dashboard hosted on a personal site and a video walkthrough, and the results "figure" in the body is a screenshot pointing readers to the live demo for the real evidence. At JAIS this fails the standalone-body requirement: a reviewer reading the printed manuscript cannot evaluate the artifact's utility without clicking out, and the live link risks de-anonymizing the authors. The fix is to bring the load-bearing evidence into the body as static, grayscale-legible exhibits — an architecture figure, an evaluation-vs-baseline table tied to each design proposition, and an ablation table — while the interactive demo and video move to clearly labeled appendix files. The body must carry the argument on paper; the multimedia is supplementary, not primary.

## Anti-patterns

- Putting load-bearing evidence in a clickable link or multimedia file, breaking the standalone body.
- Omitting the correlation/covariance matrix from an SEM submission.
- A framework diagram that contradicts or outruns the prose.
- Significance-stars tables with no effect sizes or confidence intervals.
- Figures that only work in color, illegible once printed in grayscale.

## Output format

```text
【Journal】Journal of the Association for Information Systems (JAIS)
【Body standalone?】all main evidence in text/tables/figures: yes/fix
【Exhibit inventory】measurement / results / event-study / artifact / framework / data-structure
【SEM matrix】correlation/covariance + descriptives present: yes/fix
【Reporting】effect sizes + precision (not stars only): yes/fix
【Style】APA 6th; grayscale-legible; all referenced: pass/fix
【Length impact】within ~15k words / 65pp: yes/trim
【Next skill】jais-writing-style
```
