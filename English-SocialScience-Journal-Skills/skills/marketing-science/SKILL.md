---
name: marketing-science
description: Use when targeting Marketing Science or deciding whether a quantitative-marketing manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Marketing Science (marketing-science)

## Journal positioning

Marketing Science is the INFORMS flagship for quantitative marketing and an FT50 venue. It publishes analytical models and structural/empirical industrial-organization studies of markets, firms, and consumers — econometric and game-theoretic modeling at the marketing–economics interface. The defining taste is a rigorous formal contribution: a model that yields non-obvious, testable, or managerially relevant implications, or an empirical IO study with credible identification of demand, supply, or strategic interaction. Readership is the quantitative-marketing and marketing-economics community.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the INFORMS site and the submission system.

## When to trigger

- The author names Marketing Science (or the INFORMS / FT50 quantitative-marketing tier) as the venue.
- An analytical-modeling, structural-econometric, or empirical-IO marketing paper needs positioning for the quantitative wing of the field.
- An economics-flavored marketing paper (pricing, advertising, competition, platforms) needs framing as a marketing-science contribution.
- The author needs Marketing Science's desk-reject risks and a credible JMR / JM / management-science / economics alternative list.

## Scope & topic fit

- Analytical models of marketing strategy: pricing, advertising, channels, competition, product design, platforms, with game-theoretic structure.
- Structural and empirical IO of demand and supply: discrete-choice demand estimation, dynamic models, auctions, two-sided markets.
- Quantitative models of consumer behavior, customer dynamics, and digital/algorithmic marketing.
- Methodological contributions to marketing modeling and estimation with a clear substantive question.

## Method & evidence bar

- Analytical papers need a clean model, correct derivations/proofs, and results that are non-trivial and interpretable for marketing strategy — not modeling for its own sake.
- Structural/empirical papers need credible identification of structural parameters, attention to endogeneity (prices, advertising, selection), and model validation.
- Reduced-form empirics are held to current causal-inference standards but are most welcome when paired with or motivated by a model.
- Robustness, counterfactuals, and out-of-sample/policy experiments are expected for empirical IO work.

## Structure & house style

- The front end states the strategic/market question, the modeling approach, and the key insight or estimated mechanism early.
- Analytical contributions are framed around what the model teaches that intuition or prior models did not; empirical contributions around what identification delivers.
- Marketing Science uses an unstructured abstract and a technical/online appendix for proofs, estimation detail, and robustness.
- Exhibits and propositions carry the argument; managerial/strategic implications follow from the formal results.

## Official-submission checklist

- Search the live site for "Marketing Science submission guidelines / author instructions" and follow the current INFORMS version.
- Re-check formatting (often INFORMS LaTeX style), abstract conventions, anonymization, reference style, and the technical/online-appendix requirement.
- Re-check current data/code availability and replication policies and any disclosure/ethics requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the formal or empirical-IO contribution to quantitative marketing.
- [ ] Analytical results are non-obvious and interpretable; empirical results rest on credible identification.
- [ ] Endogeneity, model validation, and counterfactuals are handled to current standards.
- [ ] The introduction positions the paper against recent Marketing Science / quantitative-marketing work.
- [ ] Proofs/estimation detail, online appendix, and code/data are ready per the current guide.

## Common desk-reject triggers

- An analytical model whose results are mechanical or have no managerial/marketing payoff.
- A structural/empirical paper with unaddressed endogeneity or unidentified parameters.
- A reduced-form regression with no model and no credible source of variation, offered as quantitative marketing.
- A purely behavioral or substantive paper with no modeling content.

## Re-routing decision

- Behavioral experiments or measurement-led rigor → `journal-of-marketing-research`; broad substantive/managerial reach → `journal-of-marketing`.
- Consumer-behavior theory / psychological process → `journal-of-consumer-research` or `journal-of-consumer-psychology`.
- General OR/analytics or methods-broad modeling → `management-science`; pure economics of markets → `rand-journal-of-economics` or a field economics venue.
- Strong but narrower marketing-strategy / B2B work → `journal-of-the-academy-of-marketing-science`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Marketing Science
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the model / identification clear Marketing Science's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / LaTeX style / abstract / technical appendix / data-code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
