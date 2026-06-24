---
name: jle-tables-figures
description: Use when building or revising the exhibits of a The Journal of Law and Economics (JLE) manuscript so the effect of the legal rule is legible in one table or figure and respects University of Chicago Press presentation norms. Formats exhibits; it does not establish the result (jle-identification / jle-robustness) or write the surrounding prose.
---

# Tables & Figures (jle-tables-figures)

## When to trigger

- The main effect of the legal rule is settled and must be made readable at a glance
- Tables are dense, over-decimaled, or bury the headline coefficient under controls
- An event-study around a law change, an RD at a regulatory cutoff, or a judge-leniency first stage needs to carry the identification visually
- You are preparing exhibits for submission and want them in University of Chicago Press house style

## The JLE exhibit bar

At JLE the **effect of the legal rule should be findable in seconds**, and every exhibit should earn its place. The signature visual is **the picture of the legal identification** — the event-study around the statute's effective date, the RD scatter at the regulatory threshold, the price path in treated vs. control markets after an enforcement action. Lead with it: at this journal, the figure that shows the rule "switching on" is half the persuasion. Report standard errors and the clustering level; describe the legal variation precisely in notes so an economist who does not know the statute can still read the table.

| Exhibit | What it must show | Common failure |
|---------|-------------------|----------------|
| Main results table | headline coefficient, SE in parentheses, N, clustering level, dependent-var mean | too many columns; SE/clustering buried; over-precision |
| Event-study around the law change | leads + lags, CIs, the rule's effective date marked, flat pre-trends visible | no CIs; treatment dated to signing; ambiguous reference period |
| RD at a regulatory cutoff | binned scatter + local-linear fit, bandwidth, density panel | overfit global polynomial; no density/manipulation panel |
| Judge/IV first stage | first-stage F, leniency leave-out construction, exclusion logic in notes | weak first stage hidden; leave-out not described |
| Treated-vs-control market plot (enforcement) | outcome paths around the action, control market defined | contaminated window; control market unjustified |
| Robustness exhibit | point-estimate stability across legal-design choices | a wall of columns with no map to threats |

## Exhibit craft

1. **One exhibit for the headline.** A reader should get the legal effect, its SE, and N without flipping pages.
2. **Make the identification visible as a figure.** Event-study leads around the effective date, RD continuity with a density panel, or treated/control market paths convince more than prose.
3. **Standard errors and clustering always.** Put SEs in parentheses and state the clustering level (usually the jurisdiction) in the note; if stars are used, define them — but the SE is the load-bearing object.
4. **Self-contained, institution-aware notes.** Each note states the sample, the legal variation, the treatment date used, the clustering level, and controls — a referee should read the table without the text.
5. **Right precision.** Two to three significant figures; do not report a litigation effect to five decimals.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JLE is empirical law-and-economics — DiD around legal/regulatory change is central.

- **Tables:** `etable` (multi-model) or `did_summary_to_latex` straight from the `result_id`.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering and states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Effect of the legal rule readable in one exhibit: coefficient, SE in parentheses, N, clustering, dep-var mean
- [ ] Identification figure present (event-study around the effective date with CIs / RD with density / treated-vs-control paths)
- [ ] Standard errors everywhere; clustering level stated; stars (if used) defined
- [ ] Notes name the legal variation and the treatment date used, and make each exhibit self-contained
- [ ] Figures are clean vector output, legible, no chartjunk, consistent scales
- [ ] Precision sensible (2–3 sig figs); no redundant exhibits

## Anti-patterns

- A main table with 12 columns where the legal-effect coefficient is hard to find
- An event-study plot with no confidence intervals, or one whose reference period dates treatment to the statute's signing rather than its effective date
- An RD figure with a high-order global polynomial that manufactures a jump and no density panel
- Reporting stars or t-stats but omitting standard errors or the clustering level
- Over-precision implying false accuracy in a noisy legal effect
- Exhibit notes that force the reader back to the text to learn what the rule or the control group is

## Worked vignette (illustrative)

A draft's Table 5 has 12 columns sweeping control sets for a tort-reform effect, and the headline coefficient sits in column 8 with only t-statistics shown. The JLE fix: promote the preferred specification to a two-panel Table 2 — Panel A the heterogeneity-robust ATT (−0.08, s.e. 0.03 in parentheses, N, clustering = state, dependent-var mean), Panel B the same with full controls — and move the sweep to the appendix. Add Figure 1, the event-study around the cap's effective date with confidence intervals and the effective date clearly marked, so the legal effect is visible before the reader reaches the table. The effect is now findable in seconds.

## The institutional/descriptive exhibit JLE expects

Beyond the causal exhibit, JLE referees who know the institution want to *see the legal setting* before the regression. Budget one early exhibit for it:

- **A timeline or map of the legal variation** — which jurisdictions adopted the rule and when (effective dates), or where the threshold/cutoff sits — so the reader sees the source of identification at a glance.
- **A descriptive table of the legal regime** — the rule's parameters across jurisdictions (cap amount, penalty schedule, eligibility cutoff), making the treatment concrete and the heterogeneity visible.
- **A first-look on the raw outcome** — the outcome path before any modeling, so the effect is not purely a regression artifact.

These earn their place because, at a law-and-economics journal, an exhibit that misrepresents or omits the institution is a faster route to rejection than a dense results table.

## Referee pushback mapped to the exhibit fix

- *"I cannot find your main legal effect."* → One headline exhibit with the coefficient, SE, N, clustering, and dep-var mean; everything else to the appendix.
- *"Your event-study reference period is ambiguous / mis-dated."* → Mark the rule's effective date, set a clear reference period, and show CIs on the leads.
- *"This RD jump looks like an artifact of the polynomial."* → Replace the global fit with a local-linear binned scatter plus a density/manipulation panel.
- *"I can't tell what the legal regime actually is."* → Add the timeline/map and a descriptive table of the rule's parameters across jurisdictions.

## Precision and reporting conventions

JLE follows University of Chicago Press house style, but a few reporting conventions carry across law-and-economics exhibits regardless of typesetting:

- **Report magnitudes the legal audience can interpret** — a percent change in litigation, a dollar price effect, a change in conviction probability — not just a raw coefficient on a transformed variable.
- **State the unit of legal variation in every note** (state-year, circuit, case, firm-quarter) so the reader knows what the SE is clustered on.
- **Translate the coefficient into the rule's terms** in the note or text: "a coefficient of −0.08 implies the cap reduced claims by about 8%."
- **Keep significance secondary to magnitude and SE**: a legally important effect with a wide interval is still informative; report the interval, not just the star.

## Output format

```
【Headline exhibit】one table/figure carrying the legal effect? [Y/N]
【Identification figure】event-study (effective date marked) / RD with density / treated-vs-control? [Y/N]
【Inference shown】SEs in parentheses + clustering level in notes? [Y/N]; stars defined if used
【Notes self-contained】legal variation + treatment date + sample + clustering? [Y/N]
【Figure quality】vector, legible, no chartjunk? [Y/N]
【Next step】jle-writing-style
```
