---
name: jfm-empirical-design
description: Use when the market-data design and microstructure measurement are the bottleneck for a Journal of Financial Markets (JFM) manuscript — TAQ/order-book cleaning, liquidity and price-impact construction, sample filters. Hardens measurement; it does not invent evidence or citations.
---

# Empirical Design & Microstructure Measurement (jfm-empirical-design)

## When to trigger

- Liquidity, spread, depth, or price-impact measures are being constructed and the choices are not pinned down
- TAQ / order-book data needs cleaning (trade-quote matching, outlier filters, cancellations) and the rules are ad hoc
- The sample (universe, period, asset class, venue) is chosen without a documented inclusion/exclusion rule
- A daily-frequency liquidity proxy (Amihud, Roll, CRSP-based) is standing in for an intraday claim
- A referee will ask whether the result is an artifact of the measure or the filter, not a real market effect

## Microstructure measurement choices that JFM referees scrutinize

JFM is the journal where **measurement is the contribution as often as identification is**. Insiders know each liquidity construct embeds assumptions; the design must name them.

| Object | Common measures | The trap to disclose |
|--------|-----------------|----------------------|
| Spread | quoted, effective, realized; %/cents | effective vs. quoted matters when trades execute inside the quote |
| Depth / quantity | quoted depth, order-book imbalance, Kyle's lambda | depth at touch vs. deeper levels; venue-fragmented depth |
| Price impact | permanent vs. temporary; 5-min realized | horizon choice drives the adverse-selection share |
| Trade direction | Lee-Ready, tick rule, BVC | sign-classification error biases PIN/impact |
| Informed trading | PIN, VPIN, adverse-selection component | PIN estimation is numerically fragile; report it honestly |
| Daily proxies | Amihud illiquidity, Roll, Corwin-Schultz | proxies for high-frequency claims must be validated |

## Designing the sample and data pipeline

1. **State the universe and filters first.** Asset class, venue(s), period, price/volume screens, and exactly which records are dropped (errors, openings/closings, halts, locked/crossed quotes). Microstructure results are notoriously filter-sensitive.
2. **Match trades to quotes correctly.** State the timestamp alignment (no look-ahead), the quote-update convention, and the venue consolidation (single venue vs. consolidated tape; lit vs. dark).
3. **Handle the diurnal pattern.** Spreads, depth, and volume are U-shaped intraday; aggregate or control so time-of-day does not contaminate the measure.
4. **Validate the chosen measure.** Show the headline survives an alternative construct (effective↔realized spread, Amihud↔intraday impact) — this belongs partly here and partly in `jfm-robustness`.
5. **Lock the data lineage** for replication: raw feed → cleaning → analysis file, with a codebook (see `jfm-internet-appendix`).

## Worked pipeline (illustrative, equity TAQ)

A study of intraday adverse selection on consolidated TAQ: (1) restrict to common shares on primary listings, drop ADRs and ETFs; (2) keep regular-hours trades, drop the opening/closing auctions and the first/last few minutes; (3) remove trades with corrected/cancelled condition codes and crossed/locked quotes; (4) sign trades with Lee-Ready against the prevailing NBBO with a defensible quote-staleness rule; (5) compute effective spread = 2·|p − m| and the 5-minute permanent price impact as the adverse-selection component; (6) aggregate to stock-day, controlling for the intraday U-shape. Every dropped record class and every parameter (staleness, horizon) is logged in the codebook. The headline is then shown to survive switching the impact horizon and the sign-classification rule — the two choices a referee will challenge first.

## Asset-class measurement notes

- **Equities:** consolidated tape vs. single venue changes depth and fragmentation; state which. NBBO timing matters for effective-spread signing.
- **Corporate bonds:** TRACE is dealer-reported with reporting lags and caps on large-trade sizes; daily/transaction sparsity makes intraday measures impossible — use round-trip cost / imputed roundtrip (Feldhütter) instead of quoted spread.
- **Treasuries / FX:** decentralized; "the spread" depends on the platform (BrokerTec, EBS); name it.
- **Crypto / AMMs:** liquidity is the bonding-curve / pool depth, not a quoted spread; map the concept honestly rather than forcing an equity construct.

## Execution bridge (StatsPAI / Stata MCP)

Run the asset-pricing battery, don't just specify it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFM is market microstructure and asset pricing — liquidity, price discovery, and cross-sectional return tests where the factor-zoo multiple-testing haircut is salient.

- **Factor regressions / time-series alphas:** `feols` with the right SEs (Newey–West /
  clustered) — read the alpha and t off the return, not off a memory of the spec.
- **Factor-zoo haircut:** after disclosing how many signals were screened, apply
  `romano_wolf` / `benjamini_hochberg` and report the alpha that survives the threshold.
- **Fama–MacBeth + Shanken EIV correction** are Stata-canonical: run them via
  `mcp__stata-mcp__stata_do` with the vendored `resources/code/` (`asreg` / `xtfmb`).
- **Emit exhibits** with `etable`; hand formatting to the tables/figures skill.

Report the economic magnitude (bps/month alpha, Sharpe gain); the full factor grid and
all screened signals go to the appendix. [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Universe, period, venue, asset class, and every inclusion/exclusion filter are documented
- [ ] Trade-quote matching, timestamp alignment, and venue consolidation are stated (no look-ahead)
- [ ] Each liquidity/impact measure is named with its construction and its embedded assumption
- [ ] The data granularity matches the claim (intraday for impact; not a daily proxy for a high-frequency story)
- [ ] The intraday diurnal pattern is handled
- [ ] The headline measure is shown robust to at least one alternative construct
- [ ] Data sources and any proprietary-feed access path are named for replication

## The diurnal pattern is not optional

Intraday spreads, depth, and volume follow a pronounced U-shape — wide and active at the open, tightest midday, widening into the close — and this pattern is strong enough to swamp many effects if ignored. Any design comparing periods, events, or stocks at different times of day must neutralize it: include time-of-bin fixed effects, compare within the same intraday interval across treatment/control, or normalize each observation by its time-of-day average. The classic failure is an event that happens to cluster at the open or close, whose "effect" is really the diurnal level. State explicitly how the U-shape is handled; a microstructure referee will assume it contaminates the result until shown otherwise.

## Documenting the sample-construction funnel

Report the sample as a funnel a referee can audit: start from the raw universe, then show each screen and the count it removes (e.g., 9,800 stocks → drop ADRs/ETFs → 6,200 → require ≥250 trading days → 5,400 → drop penny stocks → 5,100). This single table answers the perennial "are the results driven by sample selection?" before it is asked. Pair it with the period, venue, and frequency. Hidden or undocumented filters are the most common silent driver of a fragile microstructure result and the easiest reject to avoid.

## Anti-patterns

- Reporting a spread or impact number without saying quoted vs. effective vs. realized, or the horizon
- Undocumented filters that quietly drive the result (the classic JFM reject)
- A daily Amihud/Roll proxy used to make a claim that requires order-book resolution
- Lee-Ready sign classification applied without acknowledging its error rate
- Ignoring venue fragmentation / dark trading when the claim is about market-wide liquidity
- PIN/VPIN reported as if numerically clean when estimation is fragile

## Where measurement becomes the contribution

In many JFM papers the contribution *is* a better measure: a sharper decomposition of the spread into adverse-selection vs. inventory vs. order-processing components, a price-impact estimator robust to microstructure noise, an order-book-based liquidity index, or a way to sign trades when the NBBO is stale. If that is your paper, hold the new measure to a higher standard: show it recovers the right answer in a setting with a known benchmark, show it correlates sensibly with established measures while capturing something they miss, and show the downstream result is not mechanically induced by the construction. A new measure that is only validated by "it gives the result we wanted" will not survive review.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-empirical-design
【Sample】universe / period / venue / asset class / key filters
【Liquidity measure】<spread/depth/impact + construction + assumption>
【Granularity check】matches the claim? <quote/trade/order-book vs. daily>
【Pipeline】trade-quote match + diurnal handling + lineage documented? [Y/N]
【Measure validation】alternative construct agrees? [Y/N → jfm-robustness]
【Source status】verified URL / 待核实 / not asserted
【Next skill】jfm-robustness
```
