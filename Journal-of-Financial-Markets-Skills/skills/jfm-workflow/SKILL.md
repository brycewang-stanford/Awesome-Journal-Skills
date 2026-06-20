---
name: jfm-workflow
description: Use when deciding which jfm-* sub-skill to invoke next, or when sequencing work on a Journal of Financial Markets (JFM) manuscript from topic selection through rebuttal. Routes — it does not replace — the specialized microstructure-focused skills.
---

# JFM Workflow Router (jfm-workflow)

## Overview

This is the router for a manuscript aimed at the **Journal of Financial Markets (JFM)** — Elsevier's specialized field journal for **market microstructure and the functioning of financial markets**: liquidity, price formation and discovery, order flow, trading-mechanism and venue design, high-frequency dynamics, market-based asset pricing, and market regulation. JFM rewards papers built on **deep institutional knowledge of how markets actually trade** plus a **careful empirical design on market data** (TAQ/order-book/proprietary feeds) or **microstructure theory**. It is small, fast, and specialist — not a broad-finance generalist.

The single most useful thing this router does is keep you from mis-targeting. The fatal JFM error is submitting a paper whose mechanism is corporate finance, broad asset pricing, or banking with a thin "and we look at liquidity" wrapper. JFM referees are microstructure insiders; the mechanism, not the dataset, must be about market trading.

Verify volatile process facts before relying on them: publisher **Elsevier**; submission via **Editorial Manager** (检索于 2026-06；以官网为准); review model double-blind 待核实; ISSN 1386-4181 (print) / 1878-576X (online). Editor names, abstract/length limits, APC: 待核实.

## When to trigger

- A user asks "what should I do next?" on a markets/microstructure paper
- A draft is ping-ponging between mechanism framing, data design, exhibits, and the response letter
- The team is weighing JFM against JF / JFE / RFS (broad top-3) or JFQA
- A JFM decision letter arrived and revision mode must start
- A reviewer says the paper "is not really microstructure" and fit is in doubt

## Routing table

| Current symptom | Next skill |
|-----------------|-----------|
| Is this even a microstructure/markets question, or broad finance? | `jfm-topic-selection` |
| Contribution vs. the microstructure frontier is fuzzy or oversold | `jfm-literature-positioning` |
| Causal claim rests on OLS+controls or a fragile event window | `jfm-identification` |
| Liquidity/price-impact measures, sample filters, or TAQ cleaning are shaky | `jfm-empirical-design` |
| Results may be spec-, sample-, microstructure-noise-, or inference-sensitive | `jfm-robustness` |
| Spread/depth/impact exhibits are dense or do not answer the question | `jfm-tables-figures` |
| Supporting material is too thin or sprawling for the Internet Appendix | `jfm-internet-appendix` |
| Intro/abstract bury the mechanism; prose misses the JFM voice | `jfm-writing-style` |
| Close to submission; need an Editorial Manager preflight | `jfm-submission` |
| Want to anticipate the microstructure referee's objections | `jfm-referee-strategy` |
| A decision letter / report needs a response plan | `jfm-rebuttal` |

## Default order

`jfm-topic-selection → jfm-literature-positioning → jfm-identification → jfm-empirical-design → jfm-robustness → jfm-tables-figures → jfm-internet-appendix → jfm-writing-style → jfm-submission → jfm-referee-strategy → jfm-rebuttal`

> `jfm-writing-style` is late polish: do not rewrite the intro before the mechanism, measurement, and identification settle. `jfm-referee-strategy` is best run *before* submission as a pre-mortem, then again to plan the `jfm-rebuttal`.

## Routing by paper archetype

The binding constraint differs sharply by the kind of microstructure paper. Read the archetype, enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Empirical microstructure (TAQ/order book) | liquidity/impact measurement + sample filters | `jfm-empirical-design` |
| Market-structure event (tick-size, reg change, venue entry) | identification off the exogenous shock | `jfm-identification` |
| Microstructure theory (Kyle/Glosten-Milgrom lineage) | mapping model objects to testable market predictions | `jfm-literature-positioning` → `jfm-writing-style` |
| Market-based asset pricing (liquidity premia, limits-to-arbitrage) | distinguishing from a broad-AP story for JF/RFS | `jfm-topic-selection` |
| HFT / fast-trading / latency | data granularity + venue/clock alignment | `jfm-empirical-design` → `jfm-robustness` |

## Worked routing example (illustrative)

A user says: "My paper shows a new order type tightens spreads, but a referee called the result a measurement artifact and said liquidity is endogenous to the venue's launch." That is two distinct JFM pushbacks owned by different skills. The endogeneity charge is an *identification* problem — route first to `jfm-identification` to exploit the staggered venue rollout as the identifying variation and cluster correctly. The artifact charge is a *measurement* problem — route to `jfm-empirical-design` to construct alternative spread measures, then `jfm-robustness` to show the effect (say it settles at 9-14 bps across constructs, illustrative) survives. Only once both are solid do you return to `jfm-tables-figures` to present the event study and `jfm-rebuttal` to write the response. Prose polish (`jfm-writing-style`) waits until last.

## Minimal decision snippet

```
if decision_letter_arrived:          -> jfm-rebuttal (plan via jfm-referee-strategy)
elif ready_to_submit:                -> jfm-submission
elif exhibits_unclear:               -> jfm-tables-figures
elif appendix_or_replication:        -> jfm-internet-appendix
elif results_fragile:                -> jfm-robustness
elif measurement_shaky:              -> jfm-empirical-design
elif endogeneity_or_causal:          -> jfm-identification
elif contribution_fuzzy:             -> jfm-literature-positioning
elif fit_in_doubt:                   -> jfm-topic-selection
else:                                -> jfm-topic-selection
```

## Anti-patterns

- Treating JFM as interchangeable with JF, JFE, or RFS — those are broad top-3; JFM is the microstructure specialist
- Listing a general asset-pricing or corporate-finance paper as a JFM exemplar
- Polishing prose before the trading mechanism and measurement are stable
- Letting the Internet Appendix carry a claim the main text must establish
- Quoting an editor name, fee, or word limit not in `resources/official-source-map.md` and not marked 待核实

## Output format

```text
【Target】Journal of Financial Markets (JFM) — microstructure specialist
【Archetype】empirical micro / market-structure event / theory / market-AP / HFT
【Current bottleneck】fit / contribution / identification / measurement / robustness / exhibits / appendix / style / submission / revision
【Next skill】<one jfm-* skill>
【Reason】why this is the binding constraint at this stage
【Source check】official facts verified or marked 待核实
```
