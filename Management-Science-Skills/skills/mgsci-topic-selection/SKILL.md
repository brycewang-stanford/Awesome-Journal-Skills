---
name: mgsci-topic-selection
description: Use when shaping or stress-testing a research question for Management Science (INFORMS) — confirming the decision-relevance bar, choosing the right Department lane (analytical vs empirical), and testing fit against sister INFORMS journals (Operations Research, M&SOM, Marketing Science) so the paper is not desk-rejected as "better suited elsewhere".
---

# Topic Selection & Fit (mgsci-topic-selection)

## When to trigger

- The idea is interesting but you cannot name the **Department** it belongs to
- You are unsure whether it fits **Management Science** or a sister INFORMS journal
- A reviewer or Department Editor said "off fit" or "better suited elsewhere"
- You have a method looking for a question, or a result with no decision implication

## The Management Science bar

Management Science publishes work whose unifying test is **methodological rigor plus a demonstrated contribution to management/business decision-making that travels across departments**. It is deliberately **bimethodological**: a clean **analytical model** (OR/optimization, stochastic processes, game/economic theory) and a sharp **empirical study** (econometrics, experiments, behavioral, data science) are *equally* at home — but each must deliver a generalizable managerial insight, not just a technical result.

Ask three questions before investing:

1. **Decision relevance.** What management decision changes if the result holds? A model with no managerial reading, or an empirical fact with no decision lever, is off-mission.
2. **Which Department?** Name it: Accounting; Behavioral Economics and Decision Analysis; Business Strategy; Data Science; Entrepreneurship & Innovation; Finance; Information Systems; Operations Management; Optimization and Decision Analytics; Revenue Management & Market Analytics; Stochastic Models and Simulation (Marketing/Organizations as applicable; exact 2026 set 待核实). The Department Editor owns your desk screen and standards.
3. **Cross-department travel.** Does the insight matter beyond a single niche? Management Science prizes results that a reader in another Department still finds informative.

## The sister-journal fit test (this is where papers die)

A large share of submissions are desk-rejected as better suited elsewhere. Before committing, distinguish:

| If the core contribution is...                                  | Likely better venue                     |
|-----------------------------------------------------------------|-----------------------------------------|
| A new OR algorithm / methodology with limited managerial reading | **Operations Research**                 |
| Supply-chain / service-operations / manufacturing focus          | **M&SOM**                               |
| Quantitative-marketing models of consumer/firm behavior          | **Marketing Science**                   |
| Broad, decision-relevant insight that travels across departments | **Management Science**                  |

Management Science wants the **managerial-science** angle: rigor in service of a decision insight that is not confined to one application area. Ambiguous-fit papers spanning departments are discussed across the editorial team — make the intended Department and the cross-department payoff explicit in the cover letter.

## Anti-patterns

- A polished algorithm with no managerial interpretation (aim at Operations Research).
- An empirical regularity with no decision lever or theory.
- "It touches operations and finance" with no clear home Department and no cross-department insight.
- Picking Management Science only for prestige when a sister INFORMS journal is the natural home.


## Fit pass for Management Science

Run this as a concrete capability pass. First lock the decision problem, formal or empirical engine, managerial lever, and generality claim; then test whether the manuscript addresses OR/MS reviewers who expect a generalizable decision model, credible empirical leverage, or algorithmic insight with managerial consequence.

- **Primary move:** Score fit, novelty, evidence readiness, and audience ownership; reject prestige-only targeting when a sibling venue owns the contribution more directly.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Operations Research for method-first optimization, Marketing Science for marketing models, Organization Science for organization-theory mechanisms; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Decision relevance】what decision changes ...
【Department】[named lane] — analytical or empirical
【Cross-department travel】who else cares ...
【Fit vs sister journals】Mgmt Sci vs OR / M&SOM / Marketing Science: keep/redirect
【Next step】mgsci-theory-development or mgsci-methods
```
