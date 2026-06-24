---
name: isr-tables-figures
description: Use when designing the exhibits for an Information Systems Research (ISR) manuscript — correlation/measurement tables, estimation results, model/equilibrium figures, design-science evaluation tables, and the split between main text and the electronic companion under ISR's 32-page text / 38-page total cap. Finalizes exhibits; it does not run the analysis (isr-data-analysis) or polish prose (isr-writing-style).
---

# Tables, Figures & the Electronic Companion (isr-tables-figures)

## When to trigger

- The main text is over the page budget and you must decide what moves to the companion
- Exhibits are cluttered, not self-contained, or off INFORMS house style
- You have proofs, lemmas, or full measurement items competing for space in the body
- A reviewer says "Table X is unreadable" or "the model is hard to follow"

## Budget exhibits against ISR's hard page cap

ISR caps manuscripts at **32 pages of text** and **no more than 38 pages including all material** (references, appendixes, tables, figures). This discipline is tighter than many peer journals, so exhibits must earn their place. Treat the **electronic companion / online appendix** (published if accepted) as the home for everything that supports but does not carry the argument: full proofs and lemmas, complete measurement items and scale sources, additional robustness, and large auxiliary tables. Keep in the body only the exhibits a reader needs to follow the core claim.

## Genre-specific exhibits

- **Behavioral/empirical.** A descriptives/correlation table with reliabilities on the diagonal; a measurement table (loadings, AVE, discriminant validity); a results table with effect sizes; interaction plots with simple slopes; the theoretical model as a path diagram.
- **Analytical/economic.** A clean **timeline/game-tree** figure of the model; a notation/assumptions table; comparative-statics figures or tables showing how the equilibrium shifts with key parameters. Push full proofs to the companion; keep only the load-bearing result and its intuition in the body.
- **Design science.** An artifact architecture figure; a design-objectives-to-features mapping table; an evaluation table benchmarking the artifact against baselines on objective-linked metrics.

## House style and self-containment

Follow INFORMS exhibit conventions; every table and figure must be **self-contained** (title, units, N, significance notes, and what the reader should conclude) so it reads without the prose. Number consistently and ensure every exhibit is referenced and interpreted in the text — no orphan tables.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). ISR is empirical IS with strong econometric and experimental work; identification (DiD / IV) for observational claims, randomization inference for experiments.

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the effect size in
  interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Body exhibits limited to those that carry the core claim
- [ ] Proofs, full items, extra robustness routed to the electronic companion
- [ ] Page budget (32 text / 38 total) verified after exhibit placement
- [ ] Each exhibit self-contained and INFORMS-styled
- [ ] Model/equilibrium or path diagram present and legible
- [ ] Every exhibit referenced and interpreted in text

## Anti-patterns

- **Kitchen-sink tables** dumping every coefficient into the body.
- **Proofs in the main text** crowding out the argument.
- **Orphan exhibits** never discussed in prose.
- **Non-self-contained** tables that require the text to be intelligible.


## Exhibit pass for Information Systems Research

Run this as a concrete capability pass. First lock the digital artifact or system, user/firm behavior, identification or design evidence, and IS-theory contribution; then test whether the manuscript addresses IS reviewers who expect digital-technology theory, empirical or design leverage, and implications for organizations or markets.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against MIS Quarterly for broader IS theory, Management Science for OR/MS generality, Journal of Management Information Systems for applied IS systems; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Genre exhibits】[...]
【Body vs companion split】[...]
【Page budget】32 text / 38 total: ok? [...]
【Self-containment】[...]
【House style】INFORMS conventions: pass/fix
【Next step】isr-writing-style
```
