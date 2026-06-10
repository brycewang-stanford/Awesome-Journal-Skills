---
name: psci-theory-and-hypotheses
description: Use when stating the theory and hypotheses for a Psychological Science manuscript. The journal's credibility norms require a clear separation of confirmatory (preregistered) from exploratory analyses and theory stated before results. Structures the argument; it does not run analyses.
---

# Theory & Hypotheses (psci-theory-and-hypotheses)

Psychological Science rewards a **clear theoretical claim** and **honest hypothesis status**. Because
preregistration quality is weighed and a Research Transparency Statement is required, the cardinal
rule is: **state theory and confirmatory hypotheses before the data**, and label exploratory results
as exploratory.

## When to trigger

- Writing the theoretical framing and hypotheses
- Preparing a preregistration / pre-analysis plan (Registered Report or OSF)
- Reconciling what you predicted with what you found
- A reviewer flagged the work as "post hoc," "atheoretical," or "HARKed"

## Build the argument

1. **State the theory.** What mechanism or principle predicts the effect, and why. Keep it crisp —
   the format does not allow a long theoretical treatise.
2. **Derive directional hypotheses.** Translate the theory into specific, testable predictions
   (direction and, where possible, magnitude/effect-size expectations).
3. **Mark hypothesis status.** Separate **confirmatory** (preregistered, predicted in advance) from
   **exploratory** (generated after seeing data) analyses — clearly, in the text.
4. **Specify what would disconfirm.** Say which results would count against the theory; this is what
   makes a test credible.
5. **Match to the right format.** If the theory is best tested prospectively and confirmatorily, a
   **Registered Report** makes the claim far stronger (route via `psci-review-process`).

## Avoiding HARKing (Hypothesizing After Results are Known)

- Do not present an exploratory finding as if it were predicted.
- If you discovered something post hoc, **say so** and frame it as a hypothesis for future
  confirmation — Psychological Science values this honesty and the Transparency Statement surfaces it.

## Worked micro-example — theory to hypothesis status (illustrative)

The two-study attention package, written so hypothesis status is legible at a glance.

```
Theory:  Brief mindfulness induction transiently broadens attentional
         control, reducing automatic capture by emotional distractors.
H1 (confirmatory, preregistered, S1+S2):
         Induction reduces capture cost vs. control (directional; d ≥ 0.30 SESOI).
H2 (exploratory in S1 → confirmatory in S2):
         Effect is larger for high trait-anxiety participants
         (interaction; preregistered only for Study 2).
Disconfirming: a CI for H1 centered near zero, or a reversed sign, counts
         against the broadening account — stated up front.
```

## Constraints-on-generality (a venue expectation)

Post-credibility-revolution, name the boundary of the claim explicitly rather than implying universal
scope. Confirm current wording against the journal's submission guidelines, but include the substance:

```
Constraints on generality: We expect H1 to hold for healthy adults under
brief laboratory inductions and screen-based capture tasks. We do not claim
it generalizes to clinical anxiety, sustained meditation training, or
real-world attentional demands without further test.
```

## Theory-stage reviewer pushback and the venue fix

| Reviewer pushback | Psychological Science fix |
|-------------------|---------------------------|
| "Atheoretical / mechanism unclear" | state the broadening mechanism in one crisp sentence before the hypotheses |
| "This looks HARKed" | show the preregistration timestamp; relabel post hoc analyses exploratory |
| "Claims outrun the manipulation" | scale H1's scope to what the induction plausibly does; add a constraints-on-generality clause |
| "Non-directional hypothesis" | commit to a sign and, where possible, a SESOI magnitude |

## Theory calibration anchors

- Theory here is crisp, not encyclopedic: one mechanism sentence and a derived, directional prediction
  beat a multi-page treatise that the 2,000-word budget cannot hold.
- The cardinal honesty rule is temporal: anything specified *before* data is confirmatory; anything
  generated *after* seeing data is exploratory, full stop. The Research Transparency Statement and a
  graded preregistration make the distinction visible to editors and reviewers.
- Stating what would *disconfirm* the theory is what converts a story into a test; reviewers steeped in
  the credibility revolution read an unfalsifiable framing as a red flag.
- When the theory is best tested prospectively and confirmatorily, a Registered Report makes the claim
  materially stronger — confirm current Registered Report availability against the journal's submission
  guidelines, then route via `psci-review-process`.

## Anti-patterns

- Theory written to fit the result after the fact (HARKing)
- Vague, non-directional "we expect a relationship" hypotheses
- No statement of what would disconfirm the theory
- Blurring confirmatory and exploratory analyses
- A theory section so long it breaks the 2,000-word budget

## Output format

```
【Theory】the mechanism/principle, briefly
【Hypotheses】directional, testable (H1, H2, …)
【Status】which are confirmatory (preregistered) vs exploratory
【Disconfirming evidence】what would count against the theory
【Format fit】Research Article vs Registered Report (if confirmatory + prospective)
【Next】psci-study-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — preregistration templates and tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — preregistration and transparency policy
