---
name: jmcb-empirical-design
description: Use when bank/central-bank data construction, measurement, or sample design is the bottleneck for a Journal of Money, Credit and Banking (JMCB) manuscript. Hardens how the dataset is built and measured so the identification can do its job; it does not re-argue the causal strategy or write prose.
---

# Empirical Design (jmcb-empirical-design)

## When to trigger

- The dataset is assembled from Call Reports, Y-9C, supervisory, credit-register, or central-bank sources and the construction is under-documented
- The key variable (a "monetary shock," a "bank capital ratio," a "credit-supply" measure) is a constructed object whose definition matters for the result
- Sample period, window, or frequency choices are not motivated and could be driving the finding
- Restricted-access bank/central-bank data are involved and the access path is unstated
- A referee questioned whether the measurement, not the mechanism, produces the result

## The JMCB measurement bar

JMCB carries a deep replication heritage — the journal's own 1980s–2000s Data Archive episodes (Dewald–Thursby–Anderson; the 2006 "Got Replicability?" audit) made it acutely aware that monetary/banking results often hinge on how series are spliced, deflated, and aligned. So referees scrutinize **construction and timing**: how a series is seasonally adjusted, how regulatory definitions changed mid-sample, how a bank merger reshapes a panel, and whether the announcement window for a monetary surprise is defensible. The standard is that a reader could rebuild the central variables from the description.

## Construction craft by data type

### Bank micro-data (Call Reports / Y-9C / credit registers)
- **Identifier hygiene:** track RSSD/entity IDs through mergers and acquisitions; state how you treat acquirers vs. targets so a merger does not masquerade as growth.
- **Balance-sheet ratios:** define capital, liquidity, and lending consistently across the sample; note Basel/regulatory regime changes that redefine the numerator or denominator mid-panel.
- **Winsorize/trim** extreme ratios and state the rule; report how many bank-quarters are dropped and why.

### Monetary / macro series
- **Real-time vs. revised data:** for policy questions use the vintage the policymaker saw (ALFRED / real-time databases); say which and why.
- **Frequency and alignment:** state how high-frequency surprises are aggregated to the estimation frequency and how announcement timestamps map to observations.
- **Splicing and deflation:** document base years, deflators, and any series breaks (e.g., reserve-regime or reference-rate transitions).

### Central-bank / supervisory / restricted data
- **Access path:** name the RDC / central-bank data room / register and the disclosure constraints; this scopes what the replication package can contain.
- **Confidentiality:** state aggregation/masking rules and how they affect inference.

## Sample and specification hygiene

- Motivate the **sample window** from the institution/policy, not from where significance appears.
- Pre-specify the **frequency** (the local-projection horizon, the panel frequency) and show the headline survives nearby choices.
- Document **missing-data and entry/exit** handling so survivorship does not drive results.

## The construction decisions referees probe most

A JMCB referee will mentally re-run your data build and ask where it could have gone wrong. The recurring pressure points:

- **Seasonal adjustment and deflation.** State the SA method and base year; an unstated SA choice can manufacture or erase a cyclical pattern.
- **Reference-rate and regime transitions.** LIBOR→SOFR, reserve-regime changes, and the move to ample reserves all break series; splice them explicitly and note the break date.
- **Treatment timing.** For a policy/regulation study, the *exact* effective date and any anticipation window matter; misdated treatment biases event studies.
- **Aggregation level.** Holding-company (Y-9C) vs. bank (Call Report) reporting answers different questions; pick the level that matches the mechanism and say why.
- **Survivorship.** Failed and acquired banks leaving the panel during a crisis is not random; show the result is not an artifact of who exits.

## From measurement to a credible replication path

Measurement and reproducibility are the same discipline at JMCB. As you finalize the data build, write the construction in enough detail that the eventual replication package — or, for restricted data, the documented access path — lets someone rebuild the central variables. Note which inputs are public (Call Reports, Y-9C, FRED, ALFRED real-time vintages) and which require restricted access (supervisory panels, credit registers, RDC), since this determines what `jmcb-internet-appendix` can include. A measurement section that doubles as a reproduction recipe pre-empts the journal's signature replication concern.

## Execution bridge (StatsPAI / Stata MCP)

Run the asset-pricing battery, don't just specify it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JMCB is monetary/banking — macro time series + bank panels; local projections for the macro lane, DiD/IV for the bank lane.

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

- [ ] Every constructed key variable has a definition a reader could rebuild
- [ ] Bank IDs tracked through M&A; merger treatment stated
- [ ] Regulatory/definitional regime changes within the sample flagged and handled
- [ ] Real-time vs. revised data choice stated and justified for policy questions
- [ ] Window/frequency motivated by institutions, not by significance; headline survives nearby choices
- [ ] Restricted-data access path and disclosure constraints documented
- [ ] Winsorizing/trimming and missing-data rules stated with counts

## Anti-patterns

- A constructed "shock" or ratio whose definition is buried, so the result cannot be reproduced
- Bank mergers silently inflating growth because acquirer/target handling is unspecified
- Using revised data for a real-time policy question (or vice versa) without saying so
- A sample window or estimation horizon that quietly maximizes significance
- Restricted-data results with no statement of what the replication package can and cannot include
- Splicing series across a regime break (reserve regime, reference-rate transition) without noting it

## Public-data first, restricted-data when the mechanism demands it

Not every JMCB question needs supervisory access. Call Reports and Y-9C (bank balance sheets and income), FRED and ALFRED (macro series and real-time vintages), and disclosed monetary-surprise datasets carry a large share of publishable transmission and banking work, and they make the replication path trivial. Reserve restricted data (credit registers, supervisory loan-level panels, RDC products) for mechanisms that genuinely require within-firm-across-bank or loan-level variation. Choosing the lightest data that identifies the mechanism is both a feasibility win and a reproducibility win.

## Worked vignette (illustrative)

A paper measures the deposits channel using bank-level deposit betas. A referee notes the panel grows 30% over the sample and asks whether mergers drive it. The fix: build a merger-adjusted panel that aggregates acquirer+target pre-merger, recompute betas, and show the deposit-beta gradient is unchanged (e.g., high-branch-density banks pass through 40% of rate hikes vs. 70% for low-density, illustrative). Documenting the RSSD crosswalk and the winsorization rule turns a fragile measurement into a defensible one.

## Output format

```text
【Journal】Journal of Money, Credit and Banking
【Skill】jmcb-empirical-design
【Data sources】Call Report / Y-9C / register / central-bank / macro series
【Key constructed variable】definition a reader could rebuild
【Timing/measurement risk】real-time vs revised / window / regime change handled
【Sample hygiene】M&A, entry/exit, winsorizing, counts
【Access constraints】restricted-data path + disclosure limits (if any)
【Next skill】jmcb-robustness
```
