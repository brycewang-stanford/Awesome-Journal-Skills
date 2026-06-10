---
name: car-theory-development
description: Use when building the conceptual engine of a Contemporary Accounting Research (CAR) manuscript — the economic or behavioral mechanism, predictions/hypotheses, or the formal model — adapted to whether the paper is archival, experimental, analytical, or qualitative. Builds the argument; it does not run estimation (car-data-analysis) or frame the contribution (car-contribution-framing).
---

# Theory & Prediction Development (car-theory-development)

## When to trigger

- Predictions are descriptive ("X is associated with Y") with no mechanism
- An analytical paper has equations but no clear economic intuition
- An experiment lacks a theory that pins down the predicted direction and the process
- A reviewer says "this is atheoretical" or "the predictions don't follow from the framework"

## CAR develops theory differently by tradition

Because CAR is method-agnostic, "theory development" means different things across its traditions, and a reader should never be able to swap in a generic management-theory template:

- **Archival / capital-markets.** Ground predictions in economics-based frameworks (information asymmetry and disclosure, agency and contracting, market efficiency and the properties of accounting numbers). Derive *directional, falsifiable* predictions and, critically, predict **cross-sectional variation** — the moderators that make the effect stronger or weaker are where the theoretical content lives. State the maintained assumptions linking the accounting construct to the market outcome.
- **Experimental.** Specify the **psychological/economic process** (e.g., motivated reasoning, mental accounting, ambiguity, incentives) that produces the effect, then design predictions that *isolate* that process — including a predicted mediator and the conditions under which the effect reverses or vanishes. Theory must justify the manipulation, not just the dependent variable.
- **Analytical / modeling.** The model *is* the theory. State the setting, players, information structure, timing, and equilibrium concept; derive results as propositions with proofs; and translate each comparative static into an **empirical or institutional implication**. The contribution is the economic insight, not the algebra.
- **Field / qualitative.** Build theory inductively from the data; make the abductive logic from observations to constructs explicit and traceable.

## Predictions and hypotheses

- Write each prediction so the data could falsify it; state sign and, where possible, relative magnitude.
- For mediation/process claims, theorize the mechanism *before* testing it.
- Distinguish the maintained assumptions (untested) from the tested predictions.

## Checklist

- [ ] The mechanism is named and its logic is explicit, not assumed
- [ ] Predictions are directional and falsifiable; cross-sectional/conditional predictions stated
- [ ] (Analytical) assumptions, equilibrium concept, and the intuition behind each result are stated
- [ ] (Experimental) the predicted process/mediator and reversal conditions are specified
- [ ] Predictions map cleanly to constructs the chosen method can measure or manipulate

## Anti-patterns

- **Association dressed as theory**: "we expect X relates to Y" with no why.
- **Algebra without intuition** (analytical) or **DV-only theory** (experimental) that ignores the process.
- **Borrowed-template theory** that ignores accounting's information/contracting context.


## Operating pass for Contemporary Accounting Research

Use this as a second-pass capability check. First lock the accounting construct, setting, identification or theory, and disclosure/market/organizational implication; then test whether the manuscript addresses accounting reviewers who expect accounting-specific constructs, credible design, and contribution to reporting, auditing, tax, or governance debates.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against The Accounting Review for US flagship breadth, JAR for Chicago-style accounting research, JAE for economics/accounting interface; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Tradition】archival / experimental / analytical / qualitative
【Mechanism】the economic/behavioral logic ...
【Predictions/Hypotheses】H1..Hn, signs, conditional/cross-sectional ...
【Assumptions】maintained vs. tested (or model primitives) ...
【Process】predicted mediator / equilibrium intuition ...
【Next step】car-literature-positioning or car-methods
```
