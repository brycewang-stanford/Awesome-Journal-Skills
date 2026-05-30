---
name: journal-of-financial-markets
description: Use when targeting Journal of Financial Markets (JFM) or deciding whether a market-microstructure / trading manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Financial Markets (journal-of-financial-markets)

## Journal positioning

The Journal of Financial Markets is an Elsevier journal specializing in market microstructure and trading: liquidity, price discovery, market design, order flow, and high-frequency dynamics. It is the natural specialist home for work on how prices form and how markets are organized, judged on whether it advances microstructure understanding. The readership is microstructure and trading-focused financial economists.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Elsevier / JFM site and the editorial submission system.

## When to trigger

- The author names JFM (or microstructure field venues) as the target venue.
- A paper studies liquidity, price discovery, trading, order flow, market design, or high-frequency dynamics and the author wants a specialist home.
- A general asset-pricing or empirical paper needs re-framing around a microstructure mechanism.
- The author needs JFM's desk-reject risks and a credible microstructure / top-finance alternative list.

## Scope & topic fit

- Market microstructure theory and empirics: liquidity, bid-ask spreads, price impact, adverse selection.
- Price discovery, information aggregation, and the speed and quality of information incorporation.
- Market design and regulation: tick size, fragmentation, dark pools, market structure, circuit breakers.
- High-frequency trading, order-flow and limit-order-book dynamics, and microstructure of specific asset classes.

## Method & evidence bar

- A microstructure mechanism must be central: how information, inventory, or market design shapes prices and liquidity.
- Empirical claims need credible identification — natural experiments in market rules, exogenous shocks to trading, discontinuities — and careful high-frequency data handling.
- Theory must deliver testable implications about trading, liquidity, or price formation.
- Inference meets current standards, including the microstructure-specific care that high-frequency data demand (microstructure noise, clock conventions, clustering).

## Structure & house style

- The introduction states the microstructure question, the mechanism, the identification or model, and the headline magnitude early.
- Distinguish the contribution from the nearest microstructure papers explicitly; "no one has looked at this market" is not a contribution.
- JFM uses an unstructured abstract and JEL codes; an online appendix carries robustness, derivations, and secondary results.
- Exhibits report economic magnitudes (not only t-stats); the central result should be readable from one table or figure.

## Official-submission checklist

- Search the live site for "Journal of Financial Markets guide for authors" and follow the current Elsevier version.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and the disclosure policy (data sources, conflicts, prior circulation).
- Re-check the current data/code and online-appendix requirements and any replication expectations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters for market microstructure.
- [ ] The contribution is stated as a microstructure mechanism / identification / model, not as a significant coefficient.
- [ ] The introduction positions the paper against the most recent microstructure work on this question.
- [ ] High-frequency data handling and inference meet current standards.
- [ ] Disclosure, data sources, and the online appendix are ready.

## Common desk-reject triggers

- A paper that uses trade or quote data but makes no microstructure contribution.
- A high-frequency analysis that mishandles microstructure noise or timing conventions.
- A descriptive study of one market with no mechanism or design question.
- A paper that is really general asset pricing (`journal-of-financial-economics`) framed as microstructure.

## Re-routing decision

- Top-3 microstructure work → `journal-of-finance`, `journal-of-financial-economics`, `review-of-financial-studies`.
- Peer elite-field venues → `review-of-finance`, `journal-of-financial-and-quantitative-analysis`.
- Liquidity in intermediaries → `journal-of-financial-intermediation`; broad applied markets, large volume → `journal-of-banking-and-finance`.
- Volatility / return-predictability econometrics → `journal-of-empirical-finance`; quantitative/derivatives theory → `mathematical-finance`; international markets → `journal-of-international-money-and-finance`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Financial Markets
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the microstructure mechanism / identification clear the field bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / disclosure / online appendix / data>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
