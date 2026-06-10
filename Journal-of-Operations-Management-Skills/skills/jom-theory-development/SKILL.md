---
name: jom-theory-development
description: Use when building the theoretical argument and hypotheses for a Journal of Operations Management (JOM) empirical study — deriving operations/behavioral mechanisms a priori, borrowing and adapting reference theory to an OM phenomenon, and specifying mediation/moderation so they are testable against observed operations data.
---

# Theory Development for Empirical OM (jom-theory-development)

## When to trigger

- Your hypotheses describe what happens but not *why*, operationally
- You are importing a reference theory (TCE, RBV, agency, institutional, behavioral decision theory, contingency, queueing/coordination logic) and must adapt it to an operations setting
- A reviewer says "this is a correlation, not a mechanism" or "the theory could apply to any context"
- You need to specify mediators/moderators that operations data can actually identify

## JOM's theory bar

JOM is empirical, but empirical strength without theory reads as a technical report. The argument must give an **operations mechanism** — a causal logic rooted in how work, capacity, inventory, information, incentives, or human behavior in operations actually function — not a generic management story bolted onto an OM dataset. Because JOM explicitly excludes purely analytical/optimization work, your theory is *verbal and falsifiable*, developed to be tested against **observation**, not derived as an optimization proof.

## Build the mechanism a priori

1. **Name the operations phenomenon and its level** (task, shift, line, plant, project, dyad, supply network). Operations theorizing is acutely level-sensitive.
2. **State the core mechanism** in operational terms — e.g., how variability propagates, how slack absorbs shocks, how a behavioral bias distorts ordering, how coordination cost rises with interdependence.
3. **Derive hypotheses before seeing results.** Post-hoc hypothesizing (HARKing) is a reject signal. For intervention-based and field work, state the theorized effect of the intervention up front.
4. **Adapt, don't import wholesale.** Show *why* the borrowed theory needs modification in the operations context; that modification is often the contribution.

## Behavioral vs. operational vs. organizational logic

JOM houses behavioral/empirical OM strongly. Be explicit about which engine drives the effect: a **behavioral** mechanism (heuristics, bias, fatigue, learning) needs human-decision evidence; an **operational** mechanism (flow, congestion, buffering) needs process/transaction evidence; an **organizational/economic** mechanism (governance, incentives, contracts) needs relational/firm evidence. Mismatched theory and evidence is a common rejection.

## Mediation / moderation

- **Mediation:** specify the operational process variable that transmits the effect; plan to measure it, not assume it.
- **Moderation:** contingency theory is native to OM — state the operational condition (e.g., demand uncertainty, automation level, supplier dependence) that strengthens/weakens the effect, with a directional rationale.

## Anti-patterns

- A generic management mechanism that ignores operational structure.
- Optimization-style "the firm chooses to minimize cost" framing instead of an empirically testable behavioral/operational claim.
- HARKing; hypotheses reverse-engineered from the output.
- Importing a theory verbatim with no OM-specific adaptation.

## Matching the mechanism engine to the evidence

JOM reviewers expect the theoretical engine and the evidence type to align; the map below is interpretive guidance, confirmed against current Department missions.

| Mechanism engine | Evidence it requires | Mismatch flagged |
|------------------|----------------------|-------------------|
| Behavioral (bias, fatigue, learning) | Human-decision data | Bias inferred from firm-level archival |
| Operational (flow, congestion, buffering) | Process/transaction data | A flow claim from survey perceptions |
| Organizational/economic (governance) | Relational/firm-level data | A governance claim as individual-level |
| Contingency (a condition moderates) | A measured operational moderator | A contingency asserted but unmeasured |

## Desk-reject and return triggers on theory

- A generic management mechanism bolted onto an OM dataset, no operational structure doing work.
- Optimization-style "the firm minimizes cost" framing instead of an empirically testable claim.
- HARKing — hypotheses reverse-engineered from the output, not derived a priori.

## Worked vignette: building an operations mechanism a priori

A team theorizes that automation reduces operator errors but the benefit reverses past a threshold because automation erodes situational awareness (illustrative). The phenomenon is operational and line-level; the mechanism is behavioral-operational: automation offloads routine cognition (lowering error) yet degrades the operator's mental model (raising error on exceptions). The reference theory is automation-complacency, adapted to a high-variability setting. Hypotheses precede estimation: H1, automation lowers routine error; H2, it raises exception error; H3, the net effect is non-monotonic, moderated by exception frequency. Because the prediction is verbal and falsifiable against observed error logs, it is JOM-shaped — not an optimization proof.

## Theory objections and the mechanism-grounded fix

- *"This is a correlation, not a mechanism."* State the operational logic that generates the effect and name the process variable that transmits it.
- *"The theory could apply to any context."* Show why the mechanism depends on operational structure (capacity, flow, interdependence) a generic setting lacks.
- *"The borrowed theory is used off the shelf."* Make the OM-specific adaptation explicit — that adaptation is often the contribution.

## Output format

```
【Phenomenon & level】...
【Core OM mechanism】(operational / behavioral / organizational) ...
【Reference theory + adaptation】...
【Hypotheses】H1 ... (a priori, directional)
【Mediator / moderator】operational variable to be measured ...
【Next step】jom-literature-positioning
```
