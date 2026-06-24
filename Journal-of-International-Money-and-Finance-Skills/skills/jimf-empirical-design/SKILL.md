---
name: jimf-empirical-design
description: Use when the cross-country/time-series data construction, sample, frequency, or measurement of a Journal of International Money and Finance (JIMF) manuscript is the bottleneck. Builds the international dataset and measurement; it does not establish causality (jimf-identification) or run robustness (jimf-robustness).
---

# Empirical Design (jimf-empirical-design)

## When to trigger

- A cross-country panel is unbalanced, mixes incompatible series, or pools regimes that should be separated
- Frequency and alignment are unclear (daily FX vs. monthly flows vs. quarterly macro) and the design glosses the mismatch
- Key variables (exchange rate, capital flows, sovereign spread, pass-through) are measured in a way a referee will dispute
- Country coverage, the advanced-vs-emerging split, or sample period drives the result and is not justified
- Standard data quirks (USD vs. trade-weighted FX, gross vs. net flows, BoP vs. EPFR, nominal vs. real) are not pinned down

## The JIMF data-design bar

International-finance referees scrutinize **measurement and comparability** as hard as identification, because cross-country data are heterogeneous and easy to mis-align. Three recurring fault lines: (1) *which series* — there are several defensible measures of every JIMF object, and the choice matters; (2) *which countries and period* — advanced vs. emerging, pre- vs. post-GFC, in-vs-out of a crisis window; (3) *what frequency and alignment* — mixing frequencies without saying how. Make each explicit and defend it before the result.

| JIMF object | Measurement choices to declare | Common referee objection |
|-------------|-------------------------------|--------------------------|
| Exchange rate | bilateral USD vs. NEER/REER; nominal vs. real; end-of-period vs. average | "Your result is a dollar effect, not an exchange-rate effect" |
| Capital flows | gross vs. net; BoP (quarterly) vs. EPFR (high-frequency fund flows); by instrument (debt/equity/bank) | "EPFR is fund flows, not balance-of-payments flows" |
| Pass-through | import prices vs. CPI; aggregate vs. invoicing-currency level; horizon of pass-through | "Aggregate ERPT hides the dominant-currency margin" |
| Sovereign risk | CDS vs. EMBI/bond spread vs. rating; local- vs. foreign-currency debt | "LC and FC sovereign risk are different objects" |
| Global financial cycle | VIX vs. a factor (Miranda-Agrippino–Rey) vs. US shadow rate | "VIX is a proxy, not the GFCy" |
| Monetary stance | policy rate vs. shadow rate vs. surprise; domestic vs. foreign | "The ZLB period breaks your policy-rate measure" |

## Design moves that read as JIMF-competent

1. **Declare the country set and the split.** State advanced vs. emerging, why each country is in, and report results separately if the mechanism differs — pooling AE and EM without a test invites rejection.
2. **Anchor the sample period to the institutional history.** Bretton-Woods break, euro introduction, GFC, ZLB, taper tantrum, COVID — say which regimes your window spans and whether you split them.
3. **Resolve the frequency mismatch explicitly.** If the shock is daily and the outcome quarterly, state the aggregation; if you use mixed frequency, justify it (MIDAS / local projections at the native frequency).
4. **Defend the exchange-rate convention.** Distinguish a dollar effect from a general exchange-rate effect; report NEER/REER alongside USD when the claim is about the exchange rate per se.
5. **Document sources to the series level.** BIS, IMF IFS/BoP, IMF AREAER (capital-account openness), EPFR, Datastream/Bloomberg, Lane–Milesi-Ferretti external positions, Ilzetzki–Reinhart–Rogoff regime classification — name the exact vintage and any splicing.

## Execution bridge (StatsPAI / Stata MCP)

Run the asset-pricing battery, don't just specify it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JIMF is international macro-finance; cross-country panels + asset pricing — identification plus factor/Newey-West inference.

- **Factor regressions / time-series alphas:** `feols` with the right SEs (Newey–West /
  clustered) — read the alpha and t off the return.
- **Factor-zoo haircut:** after disclosing how many signals were screened, apply
  `romano_wolf` / `benjamini_hochberg` and report the alpha that survives.
- **Fama–MacBeth + Shanken EIV** are Stata-canonical — run via `mcp__stata-mcp__stata_do`
  with the vendored `resources/code/` (`asreg` / `xtfmb`).
- **Exhibits:** `etable`; hand formatting to the tables/figures skill.

Report the economic magnitude (bps/month alpha, Sharpe gain); full factor grid → appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Country set justified; AE/EM split reported or its absence defended
- [ ] Sample period mapped to international monetary history; regime breaks handled (split or controlled)
- [ ] Each JIMF object measured with a declared, defended choice (USD vs. NEER, gross vs. net, CDS vs. spread)
- [ ] Frequency alignment stated; mixed-frequency method named if used
- [ ] Data sources named to the series and vintage; splicing/cleaning documented for audit
- [ ] A dollar effect is not mislabeled as an exchange-rate effect (and vice versa)
- [ ] Sample-construction steps reproducible enough for the online appendix and Mendeley Data deposit

## Anti-patterns

- Pooling advanced and emerging economies with no test for whether the mechanism is common
- Using EPFR fund flows and calling them balance-of-payments capital flows (or vice versa) without flagging the difference
- A "global financial cycle" measured only by VIX with no acknowledgment it is a proxy
- An unbalanced panel where entry/exit of countries correlates with the outcome (crisis countries dropping out)
- Spanning the GFC and ZLB with a single policy-rate measure and no regime control
- Hiding the exchange-rate convention so a dollar-specific result reads as a general exchange-rate result

## Worked vignette (illustrative)

A draft regresses quarterly EM "capital flows" on a daily US surprise and finds a strong effect, but the flows are EPFR weekly fund flows aggregated to quarters and the panel drops three countries during their crises. The JIMF fix: state that EPFR captures benchmarked-fund flows (a leading indicator), not BoP flows, and either align the analysis at the native weekly frequency via local projections or report both; keep the crisis countries in with a balanced-panel robustness; and report whether the effect is a dollar phenomenon (USD bilateral) or survives in NEER terms.

## Referee pushback mapped to the design fix

- *"That's a dollar effect, not an exchange-rate effect."* → Report NEER/REER alongside the USD bilateral; show whether the result is dollar-specific or holds for the effective rate.
- *"EPFR is not balance-of-payments capital flows."* → State what EPFR measures (benchmarked-fund flows, a high-frequency leading indicator) and either align at its native frequency or triangulate with BoP data.
- *"Your panel is unbalanced in a way that correlates with the outcome."* → Show a balanced-panel robustness; report whether crisis-driven entry/exit moves the estimate.
- *"You pooled advanced and emerging economies."* → Split AE/EM and test whether the mechanism is common before pooling.
- *"The ZLB breaks your policy-rate measure."* → Use a shadow rate or a monetary surprise over the affected window; show the result is not an artifact of the policy-rate floor.

## A note on sources international-finance referees trust

Name the canonical datasets and their roles so the design reads as field-literate: IMF IFS/BoP for macro and flows; BIS for cross-border banking and FX statistics; IMF AREAER and the Chinn–Ito index for capital-account openness; the Ilzetzki–Reinhart–Rogoff classification for de facto exchange-rate regimes; Lane–Milesi-Ferretti for external positions; EPFR for high-frequency fund flows; Datastream/Bloomberg for prices, CDS, and yields. Using the wrong dataset for an object (e.g. a de jure regime classification when the question is de facto behavior) is a credibility tell referees catch quickly.

## Pre-analysis design questions to settle first

Before estimating, lock five decisions and write the one-line justification for each — they are the questions a referee asks before reading Table 1:

1. **Outcome and treatment frequency** — at what frequency is each measured, and how are they aligned (aggregation, MIDAS, native-frequency local projections)?
2. **Country set and entry/exit rule** — which countries, why, and what happens to crisis-driven gaps in the panel.
3. **Regime/period partition** — which exchange-rate or policy regimes the window spans, and whether you split or control for the breaks.
4. **The exchange-rate convention** — USD bilateral, NEER, or REER, nominal or real, and whether the claim is about the dollar or the effective rate.
5. **The flow/risk object** — gross vs. net, BoP vs. fund flows, CDS vs. spread, and which the mechanism actually predicts.

Settling these up front prevents the most common revision loop, where a measurement choice the authors never justified turns out to drive the headline result.

## Output format

```text
【Journal】Journal of International Money and Finance
【Skill】jimf-empirical-design
【Country set / split】AE / EM / both → justified? [Y/N]
【Sample period / regimes】window + breaks handled
【Key measures declared】FX convention / flows type / risk measure / GFCy proxy
【Frequency】native / aggregated / mixed-frequency method
【Data sources】named to series + vintage; splicing documented? [Y/N]
【Next skill】jimf-robustness
```
