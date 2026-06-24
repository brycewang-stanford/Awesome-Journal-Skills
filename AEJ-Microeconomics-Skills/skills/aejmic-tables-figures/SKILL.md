---
name: aejmic-tables-figures
description: Use when presenting results for an American Economic Journal: Microeconomics (AEJ: Micro) manuscript — propositions, numerical examples, schematic theory figures, and empirical/experimental tables. Builds exhibits to AEA house norms; it does not derive the results (see aejmic-theory-model).
---

# Result Presentation: Propositions, Examples & Exhibits (aejmic-tables-figures)

## When to trigger

- Propositions are buried in prose or stated imprecisely
- A numerical example would make an abstract result concrete but is missing or cluttered
- A schematic figure (timeline, type space, equilibrium region) would help but is not drawn
- (Applied/experimental) tables are dense or carry significance asterisks

## Presenting a theory-first result

AEJ: Micro results are mostly **propositions, characterizations, and numerical examples**, not regression tables. The exhibit job is to make a formal result **legible and concrete**.

### Propositions and theorems
- State each as a **numbered, self-contained** Proposition/Theorem/Lemma: a reader should grasp it without re-reading the model.
- Put the **economic content first** in surrounding prose ("Higher search costs *raise* equilibrium prices because…"), then the formal statement.
- Define every symbol at first use; keep notation consistent across statements; minimize ad-hoc subscripts.

### Numerical examples (the AEJ: Micro workhorse)
- Use a small, transparent parameterization to **illustrate the mechanism**, not to "test" it — say which proposition it instantiates.
- Show the moving part: a table or plot of the key object (optimal mechanism, equilibrium strategy, welfare) as a primitive varies.
- Report enough to reproduce (parameter values, grid) — these go in the replication package.

### Schematic theory figures
- Timelines for extensive-form games; **type-space / signal partitions** for information design; **equilibrium-region** plots in parameter space; best-response diagrams.
- Vector output; readable labels; no chartjunk. A figure should carry one idea.

### Applied / experimental tables
- Three-line tables; **report standard errors and confidence sets, not significance asterisks** (AEA house norm for inference presentation).
- Place exhibits near their discussion; self-contained notes (sample, units, what each column is).

### Choosing the right exhibit for the result

| What you want to convey | Best exhibit |
|---|---|
| A characterization holds | A numbered Proposition + an intuition sentence; rarely a table |
| How an optimum moves with a primitive | A numerical-example plot (object vs. primitive) |
| The structure of an equilibrium | A schematic (timeline, partition, region plot) |
| A magnitude from estimation/experiment | A three-line table with SEs / coverage sets |
| Model fit (structural) | Data vs. model overlay, not a fit statistic alone |

Pick one exhibit per idea. If a sentence does the job, do not add a figure; an AEJ: Micro theory paper can be exhibit-light without penalty.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id` — one variable definition, one set of numbers, body and appendix in sync.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering (from the result's diagnostics) and
  states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every formal result is a numbered, self-contained Proposition/Theorem/Lemma
- [ ] Economic content precedes the formal statement in prose
- [ ] Notation defined at first use and consistent across exhibits
- [ ] Numerical example states which proposition it illustrates and is reproducible
- [ ] Schematic figures carry one idea each; vector output; clean labels
- [ ] (Applied) tables report SEs / coverage sets, no significance asterisks
- [ ] Exhibits placed near discussion; notes self-contained

## Anti-patterns

- A proposition stated only inside a paragraph, un-numbered and un-restated
- A numerical example with a dozen parameters and no statement of what it shows
- Overloaded figures (multiple unrelated panels, dense legends, chartjunk)
- Inconsistent or ad-hoc notation across statements
- Significance asterisks in an empirical/experimental table

## Worked vignette (illustrative)

An information-design paper proves the sender-optimal signal is a two-message partition. The presentation: state **Proposition 2** cleanly ("The sender-optimal signal partitions the state into {low, high} with cutoff x*"), precede it with the intuition (pooling above x* maximizes the receiver's action while preserving credibility), then a **schematic figure** of the state line with the cutoff and a **small numerical example** showing how x* moves with the sender's bias. No regression table, no asterisks — the exhibits make the mechanism visible.

## Output format

```
【Formal results】numbered propositions/theorems, each self-contained? [Y/N]
【Economic-content-first prose】present for each? [Y/N]
【Numerical example】illustrates which proposition; reproducible? [Y/N]
【Schematic figures】one idea each; vector; clean labels? [Y/N]
【Applied tables】SEs/coverage, no asterisks? [Y/N or N/A]
【Next step】aejmic-writing-style
```
