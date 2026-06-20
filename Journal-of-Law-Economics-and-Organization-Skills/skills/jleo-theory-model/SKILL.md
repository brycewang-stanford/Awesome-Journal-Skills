---
name: jleo-theory-model
description: Use when building or sharpening the formal model for a Journal of Law, Economics, and Organization (JLEO) manuscript — transaction-cost, incomplete-contracts / property-rights, principal-agent, or political-agency models of institutions and organizations. Right-sizes and disciplines the model; it does not run the empirics (jleo-identification, jleo-robustness).
---

# Theory & Model Craft (jleo-theory-model)

## When to trigger

- A verbal institutional argument needs to be formalized into testable predictions
- A formal model exists but its assumptions or comparative statics are not tied to the institution it describes
- A referee asks "what is the model actually adding beyond the intuition?"
- The paper is a pure-theory JLEO submission and must deliver a sharp, novel institutional mechanism
- An empirical paper needs a minimal model to define the estimand and generate the sign predictions it tests

## The JLEO modeling tradition

JLEO is unusual in welcoming both **standalone formal theory** and **empirical work disciplined by a model**, but in both cases the model must be a *model of an institution or organization*, in one of the house lineages:

- **Transaction-cost economics (Williamson):** asset specificity, uncertainty, frequency → governance choice (market / hybrid / hierarchy). The model's job is to predict which governance form economizes on transaction costs.
- **Incomplete contracts / property rights (Grossman–Hart–Moore):** residual control rights, non-contractible investment, ownership allocation. The model predicts who should own what.
- **Principal–agent / mechanism design:** incentive provision under moral hazard or adverse selection inside organizations and contracts.
- **Positive political economy / political agency:** legislators, courts, bureaucrats, voters as strategic actors; separation of powers, delegation, credible commitment, agenda control.

Pick the lightest model that delivers the institutional prediction; a model that adds notation but no new comparative static is decorative and JLEO referees say so.

## Right-sizing the model

| The model's job | Right amount | Where it goes |
|-----------------|--------------|---------------|
| Name and discipline a mechanism | a few equations / a 2-type or 2-period setup | short framework section |
| Generate sign predictions to test empirically | a tractable comparative-statics model | framework before results; tested in data |
| Adjudicate a governance/ownership comparison | a TCE or GHM model with a clear cutoff | dedicated theory section |
| Deliver a full institutional result (theory paper) | a complete model with proofs | the paper's core, proofs in appendix |

## Craft moves JLEO referees reward

1. **Tie every assumption to the institution.** An assumption that is mathematically convenient but institutionally implausible (e.g., fully contractible quality in a hold-up story) draws fire. Justify the non-contractibility, the timing, the information structure from the institution.
2. **Make the comparative statics the deliverable.** State the testable predictions *before* the data appear (no HARKing the theory). For a theory paper, state which prediction is the surprising one.
3. **Earn the equilibrium concept.** If you use a refinement (e.g., a particular off-path belief, a specific bargaining protocol), say why that protocol fits the institution and what changes under alternatives.
4. **Show robustness of the mechanism.** Demonstrate the key result is not an artifact of a knife-edge assumption; relegate the general case to an appendix if it clutters.
5. **Connect to the empirics (if mixed).** The model should define the estimand the empirical section recovers, and the parameters should map to measurable institutional features.

## Checklist

- [ ] The model is a model of a specific institution/organization in a JLEO lineage (TCE / GHM / agency / PPE)
- [ ] Every substantive assumption is justified from the institutional setting, not just tractability
- [ ] The testable comparative statics are stated before the empirics; the surprising prediction is flagged
- [ ] The equilibrium concept / bargaining protocol fits the institution and alternatives are discussed
- [ ] For theory papers: proofs complete and in the appendix; the main text carries intuition
- [ ] For mixed papers: the model defines the estimand and maps parameters to measurable features

## Anti-patterns

- A "model" section that adds notation but no new prediction or governance comparison
- Assuming away the non-contractibility / specificity that the institution actually exhibits, to gain tractability
- Comparative statics derived after seeing the empirical results (HARKing the theory)
- Borrowing an off-the-shelf principal-agent setup with no institutional content specific to the paper
- A knife-edge result presented as the headline with no robustness of the mechanism

## Worked vignette (illustrative)

A paper asks why public agencies use long-term sole-source contracts despite the apparent loss of competition. A bare auction model says competition is always better. A JLEO model adds non-contractible quality and relationship-specific investment: under high specificity, the long-term relationship sustains quality that competitive re-bidding would destroy, so sole-sourcing economizes on transaction costs above a specificity threshold. The comparative static — sole-sourcing rises with specificity and with the cost of quality verification — is then taken to procurement data, where the model defines exactly what to measure.

## Output format

```text
【Lineage】TCE / incomplete-contracts-GHM / principal-agent / political-agency
【Institutional object modeled】the firm boundary / ownership / incentive scheme / political institution
【Key assumptions (institutionally justified)】[...]
【Testable comparative statics】[stated pre-data]; surprising prediction: ___
【Equilibrium concept + why it fits】[...]
【Role in paper】standalone theory / disciplines the empirics (defines estimand: ___)
【Next skill】jleo-robustness
```
