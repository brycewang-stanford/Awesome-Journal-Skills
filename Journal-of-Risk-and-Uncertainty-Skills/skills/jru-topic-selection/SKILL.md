---
name: jru-topic-selection
description: Use when deciding whether a question belongs in the Journal of Risk and Uncertainty (JRU) and how to frame it as a risk/uncertainty primitive. Tests scope fit and sibling boundaries; it does not invent evidence or citations.
---

# Topic Selection (jru-topic-selection)

## When to trigger

- You have a behavioral or decision result and are unsure JRU is the right home rather than a method-general or broad-behavioral venue
- The question is phrased as "people do X" but does not yet name a **risk or uncertainty primitive** (a utility curvature, a probability-weighting parameter, an ambiguity attitude, a VSL, an insurance elasticity)
- A coauthor wants to "add a risk angle" to a paper whose core object is really a market, a game, or a generic nudge
- The draft could plausibly go to JRU, Experimental Economics, JEBO, or Theory and Decision and the team needs the boundary drawn

## What JRU actually rewards

JRU's center of gravity is the **economics of decision-making under risk and uncertainty**: expected utility *and its descendants* (prospect theory, rank-dependent / cumulative prospect theory, ambiguity and Knightian uncertainty), the **measurement** of risk and ambiguity preferences, the **value of a statistical life** and other risk-money tradeoffs, and **insurance, precaution, and intertemporal risk**. A JRU paper's contribution is a sharper *representation*, a cleaner *measurement*, or a more credible *estimate* of one of these primitives — not merely a new domain where a known anomaly appears.

Use this triage before committing the venue:

| Your core object | JRU fit | If weak, where it likely belongs |
|------------------|---------|----------------------------------|
| A utility / probability-weighting representation with behavioral content | Strong — `jru-theory-model` | Theory and Decision (if pure axiomatics, no measurement) |
| An incentive-compatible elicitation of risk or ambiguity attitudes | Strong — `jru-identification` | Experimental Economics (if the contribution is the **method**, not the risk primitive) |
| A VSL / mortality-risk valuation or insurance-demand estimate | Strong — JRU's signature empirical territory | health/labor field journal (if risk is incidental) |
| A general behavioral anomaly (default effects, social preferences) | Weak unless re-anchored on a risk primitive | JEBO, JEEA, a field journal |
| A market design or equilibrium where risk is a feature, not the object | Weak | GEB, a micro-theory journal |

## How to re-anchor a borderline paper

1. State the contribution in one sentence as a claim about a **primitive**: "We show probability weighting is [steeper / flatter] when [condition]," not "We find people are inconsistent."
2. Name which JRU readership would cite it — decision theorists, experimental risk researchers, or VSL/insurance empiricists — and which would desk-skip it.
3. Identify the *parameter or function* the paper moves. If you cannot name one, the paper is probably a sibling-journal paper wearing a risk costume.
4. Separate what the draft already shows from what still needs a model, an experiment, or an estimation pass.
5. Hand off to `jru-literature-positioning` if a primitive is named; otherwise return to `jru-workflow` to reconsider the venue.

## What gets desk-screened at JRU

The Editor-in-Chief (W. Kip Viscusi) reserves the right to return papers that do not fit, so the topic decision is also a desk-rejection-avoidance decision. Papers most at risk of a fast return:

- **Risk-incidental applications.** A labor or health study where uncertainty is background, not the object of measurement — better suited to a field journal.
- **Method demonstrations.** A clever new lab procedure whose payoff is the procedure, not a sharper risk primitive — Experimental Economics territory.
- **Broad behavioral grab-bags.** Several anomalies loosely themed around "irrationality" with no single decision-theoretic claim — JEBO territory.
- **Pure axiomatics with no behavioral or measurement hook.** Elegant but content-free for JRU's interface readership — Theory and Decision territory.
- **Underpowered one-off experiments** that cannot pin a parameter with usable precision.

## Worked vignette (illustrative)

A team has survey evidence that small firms under-insure against rare disasters and wants to send it to JRU. As written, the object is a market outcome (takeup), so it reads as a field-economics paper. The re-anchored version makes the *primitive* the target: it elicits the firms' subjective disaster probabilities and ambiguity attitudes, then shows under-insurance is driven by ambiguity aversion rather than by misperception — a claim about a risk primitive that JRU's readership owns. The application becomes the setting; the decision parameter becomes the contribution.

## Drawing the four sibling boundaries precisely

The boundary is not "is it about risk?" but "is the *contribution* a risk primitive?" Use these one-line tests:

- **vs. Experimental Economics:** if you could swap the risk task for any other well-incentivized task and the contribution would survive, it is a method paper, not a JRU paper.
- **vs. JEBO:** if the result is one of several loosely related behavioral findings with no single decision-theoretic claim, it is broad-behavioral, not JRU.
- **vs. Theory and Decision:** if the model has no behavioral or measurement implication anyone could test, it is pure axiomatics, not JRU.
- **vs. Management Science (decision analysis):** if the contribution is a managerial decision tool rather than a positive claim about how people value risk, it is applied decision analysis, not JRU.

When two venues genuinely both fit, JRU wins if the *primitive* is the headline and the application is the setting; the sibling wins if it is the reverse.

## Checklist

- [ ] The contribution names a specific risk/uncertainty primitive (curvature, weighting, ambiguity, VSL, insurance demand), not just a behavior
- [ ] A JRU reader can see *why decision theory or risk measurement, not the application domain*, is the point
- [ ] The boundary against Experimental Economics is drawn: the contribution is the risk object, not the experimental technique per se
- [ ] The boundary against JEBO / Theory and Decision is drawn (not broad-behavioral; not pure axiomatics without measurement)
- [ ] Process-fact claims trace to `resources/official-source-map.md` or are marked 待核实
- [ ] The handoff names the next decision, not a prose edit

## Anti-patterns

- "Risk-washing": bolting the word *risk* onto a paper whose real object is a nudge, a market, or a social preference
- Pitching a pure axiomatization with no behavioral or measurement implication (that is Theory and Decision's lane)
- Pitching a clean experiment whose only novelty is the procedure, not what it reveals about a risk primitive (Experimental Economics' lane)
- Claiming "general interest" breadth that JRU does not promise — its readership is specialized in risk and uncertainty
- Inventing editor names, fees, or scope quotes instead of marking them 待核实

## Output format

```text
【Journal】Journal of Risk and Uncertainty
【Skill】jru-topic-selection
【Verdict】fit / re-anchor / reroute to sibling
【Primitive named】curvature / weighting / ambiguity / VSL / insurance / intertemporal
【One-sentence contribution】<claim about the primitive>
【Sibling boundary】why not Experimental Economics / JEBO / Theory and Decision
【Source status】verified / 待核实 / not asserted
【Next skill】jru-literature-positioning
```
