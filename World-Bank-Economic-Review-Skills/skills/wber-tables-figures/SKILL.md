---
name: wber-tables-figures
description: Use when building the exhibits for a The World Bank Economic Review (WBER) manuscript so they read cleanly for a mixed economist + policymaker audience, fit the 40-page cap, and carry the policy magnitude. Designs and audits tables/figures; it does not run the analysis or write the prose.
---

# Tables and Figures (wber-tables-figures)

## When to trigger

- Tables are dense regression dumps a policymaker cannot read
- Significance is shown with asterisks instead of standard errors / confidence intervals
- Effect sizes are reported only in coefficient units, not policy-meaningful magnitudes
- Exhibits are pushing the paper over the 40-page total cap
- An event-study or treatment effect is buried in a table when a figure would carry it

## The WBER exhibit standard

WBER exhibits serve **two readers at once**: the applied economist who checks the design and the practitioner who wants the magnitude and its policy meaning. The best WBER tables and figures make the headline effect legible in *policy units* — percentage-point change in enrollment, dollars of consumption, cost per outcome — not just a coefficient. And remember the **40-page total cap includes tables, figures, references, and appendices**: every exhibit competes for scarce space, so each must earn its place. Lead with the design (balance, first stage, pre-trends) and then the effect; do not bury the main result in column 6 of a kitchen-sink table.

## Building exhibits that work

- **One question per exhibit.** A table that answers "is the design valid?" should not also try to answer "how big is the effect?" Split them.
- **Report SEs / CIs, never asterisks.** WBER, like serious applied journals, expects standard errors (and ideally confidence intervals) so readers judge magnitude and precision, not a star count. Note the clustering level in the table.
- **Translate to policy units in the table or note.** Beside the coefficient, give the effect as a share of the control mean, a percentage-point change, or a cost-effectiveness figure. State the units and the baseline.
- **Figures for designs and dynamics.** Event-study leads/lags, RD scatter with fitted lines and bins, and dose-response curves belong in figures — they show pre-trends, manipulation, and functional form at a glance.
- **Self-contained notes.** Each note states the sample, the data source (LSMS/DHS/admin), the estimator, the clustering, and the units. A practitioner skimming exhibits should understand the paper without the text.
- **Space discipline for the cap.** Move secondary specifications to the supplementary appendix; keep the main paper's exhibits to the load-bearing ones.

## Exhibit-by-purpose map

| Purpose | Best exhibit | Must show |
|---------|-------------|-----------|
| Design validity (RCT) | Balance table | covariate means by arm, normalized differences, attrition |
| Design validity (DiD) | Event-study figure | flat leads, dynamic effects, CI bands |
| Design validity (RD) | RD scatter + density plot | binned means, fitted lines, no density jump |
| Design validity (IV) | First-stage table | effective F, exclusion-falsification |
| Main effect | Compact results table | point estimate, SE/CI, clustering, control mean, policy-unit translation |
| Mechanism / heterogeneity | Coefficient/forest plot | subgroup effects with CIs, MHT-adjusted |
| Cost / policy magnitude | Small summary table or note | cost per outcome, benefit-cost, fiscal scale |

## Referee pushback mapped to the exhibit fix

- *"I can't tell how big this effect is."* → Add the control mean and a policy-unit translation (share of mean / pp / cost per outcome) beside the coefficient.
- *"Where's the evidence the design is valid?"* → Promote balance / pre-trends / density / first-stage from text to a dedicated exhibit.
- *"The asterisks tell me nothing about magnitude."* → Replace with standard errors and confidence intervals; state the clustering level.
- *"This table has too much in it."* → Split into a design exhibit and an effect exhibit; move nuisance columns to the appendix.
- *"The paper is over length."* → Audit every exhibit against the 40-page cap; keep only load-bearing ones in the main text.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). WBER is development economics — RCTs and observational designs in low/middle-income settings; randomization inference + DiD/IV, magnitude in policy units.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each exhibit answers exactly one question
- [ ] SEs / CIs reported; no significance asterisks; clustering level stated
- [ ] Headline effect translated into policy units (share of mean / pp / cost per outcome)
- [ ] Design diagnostics (balance / pre-trends / density / first stage) shown as exhibits
- [ ] Event-study, RD, and dose-response shown as figures, not buried in tables
- [ ] Notes are self-contained: sample, source, estimator, clustering, units
- [ ] Main-text exhibits trimmed to load-bearing ones; secondary ones in the appendix (40-page cap)

## Anti-patterns

- Significance asterisks instead of standard errors / confidence intervals
- A kitchen-sink table where the main effect hides among nuisance coefficients
- Coefficients reported with no baseline mean or policy-unit translation
- An event-study or RD presented as a table when the figure tells the story
- Notes that omit the data source, clustering, or units
- Pushing the paper over 40 pages with redundant exhibits that belong in the appendix

## Worked vignette (illustrative)

A draft reports a transfer program's effect in one wide table: 14 columns, asterisks everywhere, coefficient = 0.08 with no context. The WBER rebuild: Table 1 is balance (means by arm, normalized differences, 6% attrition, balanced). Table 2 is the main effect — one preferred specification, coefficient 0.08 (s.e. 0.02, clustered at village), control-mean consumption stated, with a note translating it to a 9% increase and a cost of about $34 per 10% consumption gain (illustrative). Figure 1 is the event study showing flat pre-trends. The kitchen-sink columns move to the appendix. The result is now legible to both an econometrician and a finance ministry.

## Reading exhibits for two audiences

A WBER exhibit is tested by a "two-reader skim": hand the tables and figures (without the text) to an econometrician and to a policy analyst.

- The **econometrician** should be able to verify the design from the exhibits alone — balance, pre-trends, first stage, clustering — and judge whether the estimate is credible.
- The **policy analyst** should be able to read off the magnitude in units they care about — how many more children enrolled, how many dollars, at what cost — without decoding a coefficient.

If either reader is lost, the exhibit set has failed. The note line is the bridge: it must state the data source (LSMS/DHS/admin), the estimator, the clustering level, the sample, and the units, so each reader can self-serve.

## Output format

```text
【Exhibit inventory】design / main / mechanism / cost — one question each
【Inference display】SE/CI shown, no asterisks, clustering noted? [Y/N]
【Policy-unit translation】effect as share of mean / pp / cost per outcome? [state]
【Figures】event-study / RD / dose-response as figures? [Y/N]
【Self-contained notes】source + estimator + clustering + units? [Y/N]
【Page-cap discipline】main exhibits trimmed; secondary in appendix? [Y/N]
【Next step】wber-writing-style
```
