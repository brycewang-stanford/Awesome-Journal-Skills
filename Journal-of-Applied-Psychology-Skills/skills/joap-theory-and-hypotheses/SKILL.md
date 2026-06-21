---
name: joap-theory-and-hypotheses
description: Use when building the theoretical model and hypotheses for a Journal of Applied Psychology (JAP) manuscript. JAP demands a genuine I-O theoretical contribution with an explicit mechanism, directional hypotheses, and a clear confirmatory/exploratory split — theory stated before the data, not after. Structures the argument; it does not run analyses.
---

# Theory & Hypotheses (joap-theory-and-hypotheses)

JAP is theory-first. A paper lives or dies on whether it makes a **theoretical contribution to I-O
science** — a new **mechanism**, **boundary condition**, **integration of frameworks**, or **construct
clarification** — and whether the **hypotheses follow from that theory**. The cardinal honesty rule:
**state theory and confirmatory hypotheses before the data**, and label anything generated after seeing
data as exploratory.

## When to trigger

- Building the theoretical model and deriving hypotheses
- Writing a preregistration / pre-analysis plan
- Reconciling what you predicted with what you found
- A reviewer flagged the work as "atheoretical," "post hoc," "HARKed," or "no contribution"

## Build the argument

1. **Name the mechanism.** What process links X to Y, and why — grounded in I-O theory (e.g., social
   exchange, conservation of resources, self-determination, JD-R, affective events, justice). The
   mechanism is the contribution's core, not decoration.
2. **Specify the level(s).** State whether each construct and relationship is at the individual, dyad,
   team, or organization level, and whether effects are cross-level (e.g., 1-1-1, 2-1-1, 2-2-1). JAP
   reviewers read level-of-analysis sloppiness as a theory error.
3. **Derive directional hypotheses.** Translate the theory into specific, signed, testable predictions;
   state mediation and moderation as formal hypotheses, not afterthoughts.
4. **Mark hypothesis status.** Separate **confirmatory** (preregistered / predicted in advance) from
   **exploratory** (post hoc) analyses, clearly, in the text.
5. **Specify what would disconfirm.** Say which results count against the theory — this is what makes
   the test, and the contribution, credible.

## What counts as a JAP theoretical contribution

| Contribution type | What it must show |
|-------------------|-------------------|
| New mechanism | a process not previously specified linking established constructs |
| Boundary condition | when/for whom a known effect holds or reverses (a theorized moderator) |
| Integration | two frameworks reconciled to predict something neither does alone |
| Construct work | a clarified, differentiated, or newly measured construct with validity evidence |
| Cross-level model | how a higher-level factor shapes lower-level processes (or emergence upward) |

## Worked micro-example — theory to hypothesis status (illustrative)

A servant-leadership package, written so the mechanism, levels, and hypothesis status are legible.

```
Mechanism: Servant leadership signals safety and worth, building team
           psychological safety (social-exchange + safety climate), which
           frees members to voice and coordinate, raising team performance.
Levels:    Leadership (team, L2) → psychological safety (team, L2) →
           performance (team, L2); voice tested as L1 mediator (2-2-2 / 2-1-2).
H1 (confirmatory): Servant leadership relates positively to team performance.
H2 (confirmatory): Team psychological safety mediates H1.
H3 (confirmatory, preregistered in the lab study):
           The effect is stronger under high task interdependence (boundary).
Disconfirming: a near-zero indirect effect with a CI spanning zero, or a
           reversed safety path, counts against the account — stated up front.
```

## Theory-stage reviewer pushback and the venue fix

| Reviewer pushback | JAP fix |
|-------------------|---------|
| "No theoretical contribution" | name the new mechanism/boundary/integration in one sentence before H1 |
| "Level of analysis is muddled" | label every construct's level and the cross-level form (1-1-1, 2-1-1, …) |
| "This looks HARKed" | show the preregistration timestamp; relabel post hoc analyses exploratory |
| "Hypotheses don't follow from the theory" | rebuild each H as a signed deduction from the stated mechanism |
| "Mediation/moderation asserted, not theorized" | give the process reason the indirect/interaction effect should exist |

## Theory calibration anchors

- The contribution is the *mechanism and its boundary*, not the data context — "we tested it in
  hospitals" is a setting, not a theory advance.
- Level of analysis is theory, not bookkeeping: a cross-level claim needs a cross-level model and a
  cross-level hypothesis, stated as such.
- The honesty rule is temporal: anything specified *before* data is confirmatory; anything generated
  *after* seeing data is exploratory. Preregistration and the data-transparency appendix make the line
  visible to masked reviewers.
- Stating what would *disconfirm* the theory converts a story into a test; an unfalsifiable framing
  reads as a red flag at JAP.

## Anti-patterns

- A "contribution" that is only a new sample/industry for a known effect
- Muddled or unstated level of analysis
- Mediation/moderation hypotheses with no theorized process behind them
- Theory written to fit the result after the fact (HARKing)
- Blurring confirmatory and exploratory hypotheses

## Output format

```
【Mechanism】the I-O process linking the constructs, briefly
【Levels】each construct's level + cross-level form (1-1-1 / 2-1-1 / 2-2-2 …)
【Hypotheses】directional, signed (H1, H2 mediation, H3 moderation …)
【Status】which are confirmatory (preregistered) vs exploratory
【Disconfirming evidence】what would count against the theory
【Next】joap-literature-positioning
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — preregistration templates, theory-mapping and measurement tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope and contribution expectations
