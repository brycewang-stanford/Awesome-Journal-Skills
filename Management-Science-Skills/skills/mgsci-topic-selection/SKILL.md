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
2. **Which Department?** Name it: Accounting; Behavioral Economics and Decision Analysis; Data Science; Entrepreneurship and Innovation; Finance; Healthcare Management; Information Systems; Market Design, Platform, and Demand Analytics; Marketing; Operations Management; Optimization and Decision Analytics; Organizations; Stochastic Models and Simulation; Strategy; Sustainability. The Department Editor owns your desk screen and standards.
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


## Borderline routing calls (illustrative)

| Project | Natural home | Why |
|---|---|---|
| New column-generation scheme for crew scheduling, runtime gains only | Operations Research | Method-first; managerial lever is thin |
| Field experiment on how delivery-time promises shift cart abandonment | Marketing Science | A marketing-mix decision owns it |
| Analytical model of how a platform sets commission to balance two sides | Management Science (Business Strategy/OM) | Cross-department decision model with managerial payoff |
| Inventory heuristic tested only in simulation, no decision insight | Re-scope or Operations Research | No empirical leverage and no managerial consequence |

The Management Science call is rarely "is it good?" — it is "does a generalizable decision insight travel across at least one Department boundary?" If the answer is no, a sister INFORMS journal usually owns the contribution more directly, and targeting Management Science only for prestige invites a desk reject.

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
