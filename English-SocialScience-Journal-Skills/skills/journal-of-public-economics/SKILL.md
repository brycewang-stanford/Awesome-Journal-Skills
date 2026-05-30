---
name: journal-of-public-economics
description: Use when targeting Journal of Public Economics (JPubE) or deciding whether a public-economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Public Economics (journal-of-public-economics)

## Journal positioning

The Journal of Public Economics (JPubE) is the field flagship for public economics, publishing the most consequential work on taxation, public goods, social insurance, redistribution, and political economy. The paper that wins here links a credibly identified effect or a public-finance model to a question about government policy and welfare — the contribution is a mechanism plus a welfare-relevant takeaway, not just a clean estimate. The readership is public economists who care about the design and consequences of public policy.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the publisher's own site or submission system.

## When to trigger

- The author names JPubE (or a top public-economics outlet) as the target venue.
- A paper studies taxes, transfers, public goods, or government behavior and the author is choosing among public and applied-micro venues.
- An applied-micro paper needs re-framing so the public-finance mechanism and welfare relevance, not the dataset, is the contribution.
- The author needs JPubE's desk-reject risks and a credible public / applied-micro alternative list before submitting.

## Scope & topic fit

- Taxation: incidence, behavioral responses, optimal tax, evasion, and tax-policy design.
- Social insurance and transfers: unemployment, disability, health, pensions, and means-tested programs.
- Public goods, externalities, local public finance, and the economics of government provision.
- Political economy, public choice, and the determinants and effects of policy when framed around public-sector questions.

## Method & evidence bar

- Credible identification is the desk filter: quasi-experiments, policy variation, RDD at policy thresholds, bunching, IV with a defensible exclusion, or modern DiD estimators.
- Naive TWFE on staggered policy adoption, weak instruments, and unaddressed selection are treated as fatal; inference must match current standards.
- Public-finance theory and sufficient-statistics / welfare analysis must state assumptions clearly and connect estimates to welfare or optimal-policy conclusions.
- Robustness, mechanism evidence, and explicit welfare or policy relevance are expected beyond a single headline coefficient.

## Structure & house style

- The introduction states the policy question, the identification, the mechanism, the headline magnitude, and the welfare/policy implication, and says why it matters for public economics.
- Make the contribution explicit against the closest public-finance work; tie the empirical estimate to a welfare or optimal-policy framework where relevant.
- The journal uses an unstructured abstract and JEL codes; an online appendix carries robustness, derivations, and data construction.
- Exhibits report economic magnitudes, elasticities, and welfare-relevant quantities; the central result should be legible from one table or figure.

## Official-submission checklist

- Search the live site for "Journal of Public Economics guide for authors / submission guidelines" and follow the current Elsevier version, not a third-party broker's copy.
- Re-check formatting, abstract/JEL codes, reference style, the online-appendix policy, and the data & code / replication availability requirements.
- Re-check the current code-and-replication-package expectation and any structured-submission or pre-registration routes on the editorial system.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this changes how we think about a public policy and its welfare consequences.
- [ ] The contribution is stated as identification / mechanism / welfare relevance, not as a significant coefficient.
- [ ] The introduction positions the paper against the current public-economics frontier on this question.
- [ ] Identification is credible; DiD/IV/RDD/bunching choices are state-of-the-art and inference is correct.
- [ ] The estimate connects to a welfare or optimal-policy reading and the replication package is ready.

## Common desk-reject triggers

- A clean estimate with no public-finance mechanism or welfare relevance.
- Identification the field no longer accepts (naive TWFE on staggered policy, weak IV, unaddressed selection).
- A tax/transfer correlation with no source of exogenous variation and no welfare reading.
- A paper that is really labor, health, or development economics with no public-sector core framed as public.

## Re-routing decision

- General-interest public at top-5 ambition → `american-economic-review` or `aej-economic-policy`.
- Labor outcomes without a public-finance core → `journal-of-labor-economics`; health policy → `journal-of-health-economics`.
- Public policy in low/middle-income settings → `journal-of-development-economics`; broad applied micro → `aej-applied-economics` or `review-of-economics-and-statistics`.
- Optimal-tax or mechanism theory → `journal-of-economic-theory`; political-economy with a macro/growth core → `journal-of-economic-growth`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Public Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification + welfare relevance clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / online appendix / replication / pre-registration>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
