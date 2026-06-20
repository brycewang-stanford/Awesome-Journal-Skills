---
name: jfm-internet-appendix
description: Use when assembling the Internet Appendix, data codebook, and replication materials for a Journal of Financial Markets (JFM) manuscript — what stays in the main text vs. the appendix, and the TAQ/proprietary-data access path. Organizes supporting material; it does not invent evidence or citations.
---

# Internet Appendix & Replication (jfm-internet-appendix)

## When to trigger

- The main text is overflowing with secondary robustness tables that should move to an appendix
- A referee asked for a check that does not deserve main-text space but must be available
- The liquidity-measure construction and sample filters are described too thinly to be reproduced
- You are preparing the replication package and must document a proprietary or restricted data feed
- It is unclear which results are load-bearing (main text) vs. supporting (appendix)

## What belongs where

The discipline is **the main paper must be self-contained**: every claim a referee must accept to believe the headline lives in the main text. The Internet Appendix carries depth, not load-bearing claims.

| Material | Main text | Internet Appendix |
|----------|-----------|-------------------|
| Headline result + its identifying design | ✓ | |
| The one or two load-bearing robustness checks | ✓ | |
| Alternative liquidity-measure replications | summary line | full tables |
| Sample-filter / period / subsample variations | mention | full grid |
| Full microstructure-measure construction & formulas | brief | complete derivation |
| Data cleaning rules (trade-quote match, filters) | summary | exhaustive codebook |
| Placebo / falsification batteries | result stated | full set |
| Proofs / model details (if theory) | key steps | complete |

## Building the replication package (Elsevier / JFM context)

JFM is an Elsevier journal; confirm the current data-and-code policy and whether a deposit is required at submission vs. acceptance (检索于 2026-06；以官网为准 — 待核实). Regardless of the minimum, prepare:

1. **Data lineage**: raw feed (TAQ / LOBSTER / proprietary) → cleaning scripts → analysis files, with a README mapping each table/figure to the script that builds it.
2. **Codebook**: every variable, its construction (effective spread formula, impact horizon, sign-classification rule), and every filter with its rationale.
3. **Proprietary-data path**: if the feed cannot be redistributed (e.g., a vendor or exchange feed), document the *access path* — vendor, license, query/sample definition — so a replicator can obtain equivalent data. Never imply data can be shared that cannot.
4. **Environment**: software versions and a lockfile so estimates reproduce (PIN/lambda estimation is sensitive to solver settings).
5. **Map from appendix to claim**: each appendix table states which main-text sentence it supports.

## Worked self-containment test (illustrative)

Read only the main text and ask: could a referee accept the headline without ever opening the appendix? If the only evidence that the result is not a measurement artifact sits in Internet Appendix Table IA.7, the paper fails — move at least one alternative-measure column into the main text and leave the full battery in the appendix. Conversely, if the main text reproduces every sub-period split and influential-name drop, it is bloated — push those down and keep a one-line summary ("results are stable across sub-periods and to dropping the most-traded names; see IA.2-IA.4"). The main text carries the *claims*; the appendix carries the *exhaustiveness*.

## Proprietary-data documentation patterns

Microstructure papers routinely use feeds that cannot be redistributed (exchange order-book feeds, a broker's order data, Nasdaq ITCH, a vendor's TAQ license). The honest pattern is to document the **access path** precisely: the vendor/exchange, the product name, the license type, the exact query or universe/period filter used, and the cost tier if relevant. A replicator with their own license can then reconstruct the sample. State plainly what is shareable (code, derived non-proprietary aggregates) and what is not. Do not write "data available on request" for data you have no right to share — that is a common and easily caught evasion.

## Checklist

- [ ] Main text is self-contained: no headline-supporting claim lives only in the appendix
- [ ] Each appendix exhibit names the main-text claim it backs
- [ ] Full liquidity-measure construction and filter rules are in the codebook
- [ ] README maps every table/figure to its build script
- [ ] Proprietary/restricted data has a documented access path, not a false promise of sharing
- [ ] Software versions / lockfile recorded so numerically sensitive estimates reproduce
- [ ] Data-and-code policy specifics verified or marked 待核实

## A working appendix table of contents

A curated Internet Appendix for a typical empirical microstructure paper reads as a deliberate outline, not a dumping ground: **IA.1** full variable definitions and construction formulas (every liquidity/impact measure); **IA.2** the complete sample-filter grid and how many records each screen removes; **IA.3** alternative liquidity-measure replications of the headline; **IA.4** sub-period and asset-subset robustness; **IA.5** placebo/falsification tests; **IA.6** computational details (solver, starting values, tolerances, software versions); **IA.7** additional figures (intraday patterns, alternative event windows). Each section opens with one line stating which main-text claim it supports. This structure lets a referee find the check they want in seconds and signals that the authors know exactly which results are load-bearing.

## The appendix-to-text feedback loop

Use the appendix build as a check on the main text. If, while curating the appendix, you find a robustness check that is essential to believing the headline, that check belongs in the main text — promote it. If you find a main-text table that no reader needs to accept the claim, demote it. Done well, this pass leaves a main text where every exhibit is load-bearing and an appendix where every exhibit is genuinely supplementary, each labeled with the claim it backs. The relabeling alone often surfaces a buried fragility the authors had not noticed.

## Anti-patterns

- The appendix carrying a result the main argument depends on
- A sprawling appendix of orphan tables with no link to any claim
- "Data available on request" used to dodge documenting a real access path
- Omitting the construction formula for a non-standard liquidity measure
- No record of solver/version settings for PIN/structural estimates
- Treating the appendix as a dumping ground instead of curating it

## Reproducibility for numerically fragile estimates

Microstructure papers often rely on estimates that are sensitive to implementation: PIN/VPIN (likelihood with many local optima), Kyle's lambda (regression specification and sampling frequency), realized-volatility and impact measures (sampling-frequency and noise corrections), and structural model solvers. For these, the appendix and replication package must record the **exact solver, starting values, multistart strategy, convergence tolerance, and software versions** — otherwise a replicator gets different numbers and reads it as a failure. A short "computational details" subsection that states these, plus a lockfile pinning package versions, pre-empts the most common reproducibility dispute. Where a derived aggregate can be shared even though the raw feed cannot, ship that aggregate so the final tables at least reproduce from an intermediate file.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-internet-appendix
【Self-containment】main text stands alone? [Y/N]
【Appendix map】each exhibit ↔ main-text claim? [Y/N]
【Codebook】measures + filters fully documented? [Y/N]
【Data access path】proprietary feed access documented (not false sharing)? [Y/N]
【Reproducibility】versions/lockfile recorded? [Y/N]
【Policy status】data-and-code policy verified or 待核实
【Next skill】jfm-writing-style
```
