---
name: psychrev-theory-construction
description: Use when building the actual theory or formal/computational model for a Psychological Review manuscript — turning a framed problem into explicit assumptions, mechanisms, formal structure, and derivations. Constructs the model; it does NOT derive and test predictions against data (that is psychrev-argument-development) or set scope and identifiability limits (psychrev-boundary-conditions).
---

# Theory & Model Construction (psychrev-theory-construction)

## When to trigger

- The problem and the rivals are set; now you must build the theory
- You have intuitions but no explicit assumptions or mechanism
- Your "model" is a diagram with no specified dynamics or equations
- Verbal claims need to be made formal enough to derive predictions

## The build order

A Psychological Review theory is assembled in a disciplined sequence. Skipping a step is the
most common reason a draft reads as "a story, not a theory."

1. **State the assumptions (primitives).** What entities, representations, and processes does
   the theory posit, and what is taken as given? Separate **core commitments** (the theory
   lives or dies by these) from **auxiliary/implementational assumptions** (convenient,
   replaceable). Reviewers attack hidden or load-bearing-but-unstated assumptions hardest.
2. **Specify the mechanism — the *why*.** The mechanism is the engine: the causal/dynamic
   story by which the primitives produce the phenomena. A model without a mechanism is a
   curve-fit. State it in prose before you formalize it.
3. **Formalize.** Render the mechanism as math, a computational process, or a precise
   conceptual structure. For a **formal/computational model**: give the equations or
   algorithm, define every **parameter** (psychological meaning, range, units), and state the
   functional forms and why those forms. A free parameter with no interpretation is a liability.
4. **Derive the model's behavior.** Show what the model *does*: closed-form results where
   possible, otherwise simulation. The behavior, not the equations alone, is the theory's
   content. (Confront that behavior with data in `psychrev-argument-development`.)
5. **Connect to the explanandum.** Map each posited mechanism to the phenomena it is meant to
   explain — and flag phenomena it leaves to other processes.
6. **Distinguish theory from implementation.** Be explicit about which results follow from the
   core commitments versus from implementational choices, so a reviewer cannot dismiss the
   theory by attacking a replaceable detail.

## Formal-model discipline (for computational/mathematical theories)

- Every parameter has a **psychological interpretation**, not just a fitted value.
- State **functional forms** and justify them theoretically, not by fit alone.
- Distinguish **structural** assumptions (architecture) from **parametric** ones (settings).
- If the model is fit to data, say so plainly and treat fit as *illustration/constraint*, not
  as the empirical contribution — the contribution is the theory.
- Plan for `psychrev-boundary-conditions`: note where identifiability or scope may be at risk.

## Conceptual-model discipline (for non-formal frameworks)

- Each construct: a precise definition, what it includes and excludes, and how it differs
  from the nearest existing construct (no relabels).
- Each relationship: named form (causal, recursive, constitutive, inhibitory) and a mechanism.
- The framework must yield **derivable predictions**, even if stated verbally — generality
  without testable consequences is not a Review contribution.

## Checklist

- [ ] Core commitments separated from auxiliary/implementational assumptions
- [ ] The mechanism (the why) is stated in prose before formalization
- [ ] Every parameter / construct has a psychological interpretation and stated range or domain
- [ ] Functional forms / relationship forms are justified theoretically
- [ ] The model's behavior is derived (closed-form or simulated), not just its equations listed
- [ ] Each mechanism is mapped to the phenomena it explains
- [ ] Theory-level results are distinguished from implementation-level choices

## Anti-patterns

- A model that is a redescription of the data with enough free parameters to fit anything
- Parameters introduced with no psychological meaning ("a scaling constant" doing real work)
- Listing equations without ever showing what the model *does*
- Hidden core assumptions exposed later by a reviewer
- A "framework" of boxes and arrows with no mechanism and no derivable prediction
- Smuggling in a new experiment as the contribution — data only motivate or constrain here

## Output format

```
【Assumptions】core commitments | auxiliary/implementational
【Mechanism】[the why, in prose]
【Formal structure】equations / algorithm / conceptual structure; parameters with meaning + range
【Model behavior】[derived results: closed-form or simulation summary]
【Explanandum map】mechanism → phenomena explained (and phenomena left to others)
【Next step】psychrev-argument-development (derive predictions, confront data + rivals)
```
