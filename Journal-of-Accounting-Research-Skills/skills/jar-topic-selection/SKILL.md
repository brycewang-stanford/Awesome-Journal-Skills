---
name: jar-topic-selection
description: Use when choosing or sharpening a research question for a Journal of Accounting Research (JAR) manuscript — testing whether it is a real accounting question with a credible setting, JAR fit, and identification potential before any data work begins. Locks the question; it does not build the mechanism (jar-theory-development) or design the test (jar-methods).
---

# Topic Selection & JAR Fit (jar-topic-selection)

## When to trigger

- You have a dataset or a setting but not yet a question that matters for accounting
- You are unsure whether the idea fits JAR versus TAR, JAE, RAST, or CAR
- The question is "is X correlated with Y?" with no clear stakes for accounting
- You are deciding whether to target the **Ray Ball JAR Annual Conference** or the **Registered Reports** track

## What JAR is looking for

JAR publishes original research in all areas of accounting and accounting-related topics, drawing on finance, economics, statistics, psychology, and sociology. The journal's gravitational center is **empirical-archival capital-markets** research in the **Ball-Brown** tradition: how accounting information is produced, disclosed, audited, and used by investors, analysts, creditors, regulators, and managers. A JAR-fit question almost always (a) concerns an accounting/disclosure/auditing/standard-setting phenomenon, (b) lives in a setting with a **credible source of identifying variation** (a standard change, a regulation, a discontinuity, a shock), and (c) has clear **economic stakes** — it changes how we think information flows into prices, contracts, or decisions.

## The fit test (run before collecting data)

- **Accounting question?** Is the dependent or independent variable genuinely about accounting information (earnings, disclosure, audit quality, comparability, recognition vs. disclosure, enforcement)? A pure finance or pure economics question belongs elsewhere.
- **Setting with leverage?** Is there a shock, rule change, threshold, or staggered adoption you can exploit? "We run a panel regression of Y on X" with no identifying variation is a weak JAR start.
- **Economic magnitude?** Would a referee see the estimate as economically (not just statistically) meaningful?
- **Marginal contribution?** Does it move beyond a known result, an out-of-sample replication, or a mechanical mediator?
- **Data/code feasibility?** Because JAR **requires** posted data and code, confirm you can build a reproducible package from licensed sources (you usually cannot redistribute raw WRDS data).

## Sourcing strong JAR questions

- Regulatory and standard-setting shocks (FASB/IASB adoptions, SEC rules, PCAOB inspections) as natural experiments.
- New or under-used disclosure/text data (EDGAR filings, comment letters, conference calls).
- Tensions in theory (e.g., recognition vs. disclosure, transparency vs. proprietary cost) that a clean setting can adjudicate.
- For **higher-outcome-risk** questions needing **new data collection** (surveys, field experiments), consider Registered Reports — in-principle acceptance protects a well-designed null.

## Checklist

- [ ] The question is genuinely about accounting information, not just finance/economics
- [ ] A credible identifying setting (shock/rule/threshold/staggered adoption) is in sight
- [ ] The expected estimate is economically meaningful, not only significant
- [ ] The marginal contribution over existing accounting work is articulable in one sentence
- [ ] A reproducible data-and-code package is feasible from accessible sources
- [ ] Venue fit confirmed: JAR vs. TAR/JAE/RAST/CAR
- [ ] If new-data/high-risk: Registered Reports considered; if conference-relevant: Ray Ball eligibility checked

## Anti-patterns

- **Data-dredging**: starting from "what's in WRDS" rather than a question.
- **Finance in disguise**: a returns paper with no accounting-information content.
- **No identification**: a cross-sectional correlation framed as an effect.
- **Mechanical relations**: regressing a variable on its own construction.
- **Replication-only**: re-confirming a settled result with newer data and no new economics.

## Output format

```
【Question】one sentence (about accounting information)
【Setting & identifying variation】shock / rule / threshold / staggered adoption / none-yet
【Economic stakes】why the magnitude matters
【JAR fit vs. TAR/JAE/RAST/CAR】fit / redirect because ...
【Track】Regular Manuscript / Registered Report / Ray Ball Conference candidate
【Data-and-code feasibility】reproducible package possible? sources ...
【Next step】jar-theory-development
```
