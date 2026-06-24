---
name: ier-tables-figures
description: Use when exhibits in an International Economic Review (IER) manuscript are dense, do not carry the argument, or do not present structural/theory results well. Makes each exhibit answer one question; it does not generate the data.
---

# Tables and Figures (ier-tables-figures)

## When to trigger

- A reader cannot tell from a table alone what claim it supports
- A structural paper's parameter table lists estimates but not what identifies them or their precision
- A theory paper has no figure making the mechanism or comparative static visible
- Regression tables are wall-to-wall coefficients with significance stars and no economic magnitudes
- Exhibits must fit the ≤50-page IER ceiling and are crowding out the argument

## What IER exhibits must do

IER exhibits serve a **rigor-leaning, broad audience**, so each one must answer a single question and make the *economics* — not just the statistics — legible. For a theory/structural-tilted journal, the most valuable exhibits are often the ones that make a mechanism or a comparative static visible, and the parameter table that shows the model is disciplined by data. Sort your exhibits by their job:

| Exhibit type | Its one job | The IER craft |
|--------------|-------------|----------------|
| Structural parameter table | Show estimates ARE pinned, not just reported | Pair each parameter with its identifying moment and a standard error / sensitivity entry |
| Model-fit table | Show targeted moments fit AND untargeted moments match | Two panels: targeted vs. untargeted; data column next to model column |
| Comparative-statics figure | Make the mechanism visible | Plot the key outcome against the key parameter; annotate where the sign flips |
| Counterfactual table | Show the policy result and its uncertainty | Report the headline as a range over the uncertain parameter, not a lone point |
| Regression table (applied) | Show the design's answer | Report economic magnitudes and CIs, not just coefficients; group by threat, not by control |
| Event-study figure | Show pre-trends are flat | Leads and lags with CIs; reference line at treatment |

### House-style discipline

- **Report standard errors and confidence/coverage sets, not significance asterisks.** A rigor journal wants the precision shown, not thresholded — strip `***/**/*` and report SEs in parentheses and economic magnitudes in the text.
- **Self-contained notes.** Every table/figure note states the sample, the estimator, the unit of observation, the inference method, and what each column varies — a referee should not need the text to read the exhibit.
- **One question per exhibit.** If a table answers two questions, split it. Dense omnibus tables are where IER referees lose the thread.
- **Magnitudes in the text.** The table holds the numbers; the prose says what they mean ("a one-SD increase raises X by 8%, roughly a third of the cross-country gap").
- **Mind the page budget.** With a ≤50-page ceiling (检索于 2026-06；以官网为准), move secondary exhibits to the online/proof appendix (`ier-replication-package`) and keep the main text exhibits that carry the contribution.

### The structural paper's signature exhibit

For the structural/quantitative papers that are IER's bread and butter, the single most important exhibit is usually the **parameter table read together with the sensitivity/identification panel**. A referee scanning a new structural paper goes straight to it to answer one question: are these parameters pinned by the data, or assumed? Make that table do the work — estimate, standard error, the identifying moment, and (ideally) the sensitivity entry showing which moment moves it. A parameter table that is just a list of numbers tells the referee the model was calibrated, not estimated, and that perception is hard to reverse.

### Worked example (illustrative)

A draft presents a 12-column regression table with three sets of controls and stars on everything. It answers no single question and the reader cannot find the result. The fix splits it: one main-text table reporting the headline coefficient as an economic magnitude with its confidence interval, columns ordered by *threat retired* (baseline → drop influential subsample → alternative inference), and the control-set permutations moved to an online appendix. The note states sample, estimator, unit, and clustering. Now the table answers exactly one question — "is the effect there and how big" — and the reader sees it in five seconds.

### Why no asterisks at a rigor journal

The case against significance stars is not stylistic at IER — it is methodological. A rigor-leaning readership wants the *precision* of an estimate (its standard error or confidence set) shown directly, so the reader judges economic and statistical significance themselves, rather than having a coarse three-level threshold imposed by the author. Stars also encourage the very specification search the robustness section is meant to rule out. Report the SE in parentheses, state the economic magnitude in the text, and let the confidence interval do the work the stars used to do. This aligns with the broader econometric-society house norm and is the safer default even where the exact style guideline is 待核实.

### Figures earn their place by showing what a table cannot

A figure that merely re-plots a table's numbers wastes a page against the ≤50-page ceiling. The figures that earn space show something a table cannot: a *shape* (a non-monotonic comparative static), a *flip* (where a sign changes), a *distribution* (heterogeneity a mean hides), or a *fit* (model vs. data across the support). For theory and structural papers especially, the comparative-statics figure that makes the mechanism visible is often the most-cited exhibit in the paper — it is where the broad reader grasps the economics without following the algebra.

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

- [ ] Each exhibit answers exactly one question, stated in its title or note
- [ ] Structural parameter table pairs each estimate with its identifying moment and SE/sensitivity
- [ ] Model-fit shown for targeted AND untargeted moments (data vs. model columns)
- [ ] A figure makes the mechanism or comparative static visible
- [ ] No significance asterisks; SEs/confidence sets reported; economic magnitudes in the text
- [ ] Notes are self-contained (sample, estimator, unit, inference, what varies)
- [ ] Secondary exhibits moved to the appendix to respect the ≤50-page ceiling

## Anti-patterns

- An omnibus table answering three questions that the reader must disentangle
- A parameter table with no identifying moment and no precision — estimates with no provenance
- Significance stars substituting for standard errors / confidence sets
- Coefficients reported with no economic magnitude anywhere in the text
- A figure that repeats a table instead of showing something the table cannot (a shape, a flip, a non-monotonicity)
- Notes that force the reader back to the body to learn the sample or estimator

## Referee pushback mapped to the exhibit fix

- *"I can't tell what this table shows."* → Split it so each exhibit answers one question; put that question in the title or note.
- *"Are these parameters estimated or assumed?"* → Add the identifying moment and SE/sensitivity beside each structural parameter; separate estimated from external parameters.
- *"Drop the stars."* → Replace asterisks with standard errors / confidence sets; move economic magnitudes into the text.
- *"The figure just repeats the table."* → Replace it with one showing a shape, flip, distribution, or model-vs-data fit the table cannot convey.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-tables-figures
【Exhibit inventory】each exhibit → the one question it answers
【Parameter table】identifying moment + SE/sensitivity per estimate? [Y/N]
【Mechanism figure】comparative static / mechanism made visible? [Y/N]
【House style】no asterisks; SEs/CIs shown; magnitudes in text? [Y/N]
【Notes】self-contained (sample/estimator/unit/inference)? [Y/N]
【Page budget】main-text exhibits within the ≤50pp ceiling? [Y/N]
【Verdict】carries-the-argument / needs-work
【Next skill】ier-writing-style
```
