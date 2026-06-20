---
name: jfm-topic-selection
description: Use when deciding whether a question belongs at the Journal of Financial Markets (JFM) — i.e., whether it is genuinely about market microstructure / how markets trade rather than broad asset pricing or corporate finance. Scopes and reroutes; it does not invent evidence or citations.
---

# Topic Selection (jfm-topic-selection)

## When to trigger

- The paper studies trading, liquidity, prices, or order flow, and you must decide JFM vs. JF / JFE / RFS / JFQA
- A coauthor says "we have liquidity in the regressions" but the mechanism is really a corporate-finance or macro story
- The dataset is microstructure-grade (TAQ, LOBSTER, proprietary order book) but the *question* may be too broad to interest microstructure referees
- A referee elsewhere wrote "this is not really a markets paper"
- You need to decide if a structural/macro asset-pricing result has a sharp microstructure cut worth carving out for JFM

## The JFM fit test

JFM publishes research on **how securities are traded and priced** — the design and analysis of trading mechanisms, optimal order placement, the role of information in markets, liquidity, and price discovery. The clean test is the **mechanism question**: *Does the paper's central economic force live inside the trading process?* If you can restate the contribution without referencing spreads, depth, order flow, market design, information asymmetry among traders, or price formation, it is probably not a JFM paper.

| The question is really about… | Microstructure cut that makes it JFM | If no such cut |
|-------------------------------|--------------------------------------|----------------|
| A firm event (M&A, earnings, issuance) | How information enters prices via trading (PIN/VPIN, price impact, adverse selection) | → corporate finance / JF / JFE |
| A cross-sectional return premium | Whether it is a *liquidity/illiquidity* premium with a trading mechanism | → broad asset pricing / RFS / JFQA |
| A regulation | Its effect on market quality (spreads, depth, fragmentation, price discovery) | → law-econ / banking |
| Institutional behavior | Their order-submission / execution / trading footprint | → institutions / JF |
| Crypto / new venues | The market microstructure of the venue (AMMs, latency, fragmentation) | → fintech generalist |

## Where JFM is the *better* home than its siblings

- The contribution is a **measurement or mechanism advance** in liquidity/price impact/discovery rather than a new risk factor or governance result.
- The paper exploits an **exogenous market-structure change** (tick-size pilot, decimalization, circuit breakers, venue entry/exit, MiFID/Reg NMS rules) as the identifying variation.
- It is **specialist-deep**: high institutional fidelity to one market's plumbing, where JF/RFS would want broader generality but JFM rewards the depth.
- A clean **microstructure theory** paper (Kyle, Glosten-Milgrom, Easley-O'Hara lineage) with testable implications, even if the empirics are modest.

## Worked triage (illustrative)

A draft studies how passive-fund ownership affects stock returns. Pitched as-is, it is a broad asset-pricing / institutions paper for JF or RFS, not JFM. The microstructure cut that *would* make it JFM: show that index-inclusion forced trading changes the stock's **price-impact function and quoted depth** around the rebalance, and that the return effect operates through this liquidity channel. Now the contribution lives in the trading process — measured in bps of impact and shares of depth — and the rebalance is an exogenous order-flow shock. Same data, repositioned around the mechanism, becomes a JFM paper. If no such trading-process channel can be isolated, route it back to a broad-finance venue rather than thinning it into a weak JFM fit.

## Scoping by asset class

JFM publishes across equities, options, fixed income (Treasuries, corporate bonds), FX, and increasingly crypto/AMMs — but the market-structure detail must be right for that asset. An equity-microstructure framing (continuous limit-order book, Lee-Ready) does not transfer unmodified to OTC corporate bonds (dealer-intermediated, TRACE) or to FX (decentralized, no consolidated tape). Name the actual market architecture; a referee who trades that market will spot a borrowed framing instantly.

## Theory vs. empirics: both have a JFM home, on different terms

JFM publishes microstructure *theory* (a model in the Kyle / Glosten-Milgrom / Easley-O'Hara lineage) as well as empirics, but the fit test differs. A theory paper must yield **testable predictions about observable market quantities** — spreads, depth, price impact, the speed of price discovery — not just an elegant equilibrium. An empirical paper must measure those quantities credibly and connect them to a mechanism. A paper that is pure theory with no market-observable implication, or pure data-mining with no mechanism, fails the fit test from opposite directions. When in doubt, ask: what would a trader or an exchange learn from this about how the market works?

## Quick desk-reject self-screen

Before committing to JFM, run the three fastest desk-reject filters: (1) **Mechanism** — strip the microstructure words; if the paper still stands, it is not JFM. (2) **Granularity** — does the data resolution match the claim (intraday/order-book for an impact or discovery claim, not daily aggregates)? (3) **Specialist depth** — would a microstructure referee learn something new about market plumbing, or only confirm a broad-finance prior? Failing any of the three means reframe-for-JFM or reroute — do not submit and hope.

## Checklist

- [ ] The one-sentence claim names a trading-process object (spread, depth, impact, order flow, discovery, venue, information asymmetry)
- [ ] The paper survives the mechanism test: it cannot be restated without microstructure vocabulary
- [ ] You can state in one line why this is JFM and not JF/JFE/RFS (specialist depth or microstructure mechanism, not broad generality)
- [ ] The market and instruments are named precisely (equities/options/Treasuries/FX/crypto; lit vs. dark; venue)
- [ ] The data granularity matches the claim (quote/trade-level for impact claims, not daily aggregates)
- [ ] Process facts cited are in `resources/official-source-map.md` or marked 待核实

## Sizing the contribution to JFM, not above or below it

JFM is a strong field journal, not a top-3 generalist, and the contribution should be sized accordingly. A result big and broad enough to reshape how all of finance thinks may belong at JF/RFS and would be under-placed at JFM; a result that merely re-confirms a known microstructure fact in one more sample is too thin. The JFM sweet spot is a genuine advance in understanding a trading-process mechanism — a new measure, a new identifying market-structure shock, a tested theoretical prediction, or the first careful study of a new venue/asset's microstructure — that a specialist audience will find both novel and credible. Calibrate the framing to that level: do not oversell a field contribution as a paradigm shift, and do not undersell a real mechanism advance as a minor robustness note.

## Common mis-targets and where they actually go

- Return-predictability with intraday data but no trading mechanism → broad asset pricing (RFS/JFQA).
- Bank or intermediary balance-sheet effects on lending → banking/corporate (JF/JFE).
- A pure econometric estimator with a finance illustration → an econometrics or quant-finance journal.
- Investor-behavior survey with no market-quality outcome → behavioral finance generalist.

If the paper keeps drifting toward one of these, that is the signal to reroute rather than force a thin JFM framing.

## Anti-patterns

- "Liquidity as a control variable" dressed up as a microstructure contribution
- Pitching a broad return-predictability result to JFM because it happens to use intraday data
- Claiming venue/market-design relevance without describing the actual matching/auction/priority rules
- Assuming a top-3-finance reject "steps down" cleanly to JFM — JFM wants microstructure depth the broad paper may lack
- Inventing an exemplar JFM paper instead of verifying it in the official archive

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-topic-selection
【Mechanism test】passes / fails — the trading-process object is: <…>
【Verdict】fit / reframe-for-JFM / reroute to JF·JFE·RFS·JFQA
【Why JFM not siblings】<specialist depth or microstructure mechanism>
【Data granularity】matches the claim? <quote/trade/order-book vs. daily>
【Source status】verified URL / 待核实 / not asserted
【Next skill】jfm-literature-positioning
```
