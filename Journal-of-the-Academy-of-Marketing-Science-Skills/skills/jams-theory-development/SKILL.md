---
name: jams-theory-development
description: Use when building the conceptual framework and mechanism for a Journal of the Academy of Marketing Science (JAMS) manuscript — deriving hypotheses from marketing theory, specifying mediators and boundary conditions, and carrying the logic through to a managerial implication. Builds the argument; it does not select the question (jams-topic-selection) or run the analysis (jams-data-analysis).
---

# Theory Development (jams-theory-development)

## When to trigger

- The question is set but the conceptual framework that generates the hypotheses is thin
- Reviewers will ask "what is the mechanism?" and "why these moderators?"
- You have a strong empirical pattern but no organizing marketing theory
- You are tempted to bolt a generic psychological or economic theory onto a marketing finding

## JAMS's theory bar: a framework that does work

JAMS papers are expected to **develop theory**, not merely apply it. The house archetype is the **conceptual framework with a nomological network** — antecedents → focal construct(s) → consequences, with mediators that name the process and moderators that name the contingencies. Marketing reviewers want to see the framework *drawn* (a conceptual model figure) and *defended* construct by construct, each path justified by a stated theoretical logic, not by a citation alone.

JAMS draws on the field's standard theoretical lenses — resource-based view and dynamic capabilities (strategy), relationship-marketing / commitment–trust and transaction-cost / governance (B2B and channels), service-dominant logic and SERVQUAL-tradition gaps models (services), signaling and brand-equity theory (branding), diffusion and the marketing–finance interface (innovation, firm value), and consumer information-processing and self-construal theories (behavior). Pick the lens the phenomenon actually demands and use it to derive predictions, not to decorate them.

## Build the conceptual logic

- **Define every focal construct** conceptually before it is operationalized — JAMS reviewers police construct definitions and conceptual/operational alignment hard.
- **Draw the nomological net**: antecedents, focal construct(s), consequences. Each arrow is a hypothesis with a *theoretical reason*, not just a sign.
- **Specify the mechanism (mediation)**: name the process variable that carries the effect, so the story is "X → M → Y," not "X → Y, somehow."
- **Specify boundary conditions (moderation)**: when does the effect strengthen, weaken, or reverse? Contingency theory is JAMS's bread and butter; a contingency makes the framework generalizable and the managerial advice conditional.
- **Carry the logic to the manager**: if the mechanism holds, what should a decision maker do, and when? The managerial implication must be *derivable from the theory*, not appended.

## Two legitimate routes

1. **Theory-first**: lens → framework → hypotheses → test. The standard JAMS structure.
2. **Empirics-first / abductive**: a robust, surprising marketing pattern leads, and a conceptual account is built to explain it. Acceptable at JAMS if declared honestly — do not present a post-hoc account as a priori theory (HARKing).

## Hypothesis craft

JAMS reviewers read hypotheses closely, so write them to do real theoretical work:

- **One claim per hypothesis.** A hypothesis bundling a main effect and an interaction is two hypotheses; split them so each can be supported or rejected cleanly.
- **State the direction and the reason.** "H2: Because [mechanism], the effect of X on Y is *stronger* when [moderator] is high." The clause after "because" is what separates a JAMS hypothesis from a hunch.
- **Mediation as a stated path.** Hypothesize the indirect effect (X → M → Y) explicitly so the analysis can test it directly, rather than inferring process from a significant total effect.
- **Boundary conditions that are theoretically motivated**, not data-mined — name the moderator before you see the interaction, and tie it to the lens.
- **Keep the wording identical** to the conceptual model figure and the results section; drift between them is a classic reviewer catch.

## Conceptual papers (the framework genre)

JAMS also publishes purely conceptual / framework articles, and the bar is higher than a literature review:

- Deliver a **genuinely new organizing structure** — a typology, a process model, a set of propositions, or an integrative framework that reconciles competing streams — not a summary of what is known.
- State **propositions** (not testable hypotheses) with the logic that generates each, and specify the conditions under which the framework applies.
- Make the **research agenda** concrete: what the framework lets future empirical work test that it could not test before.
- Carry the framework to a **managerial reading** — even a conceptual JAMS paper should tell a decision maker how the framework changes how they think about a marketing problem.

## Avoid the construct-validity traps at the theory stage

Many measurement problems are really theory problems, so catch them now: a construct that cannot be defined distinctly from a neighbor will fail discriminant validity later; a construct defined so broadly that it absorbs its own antecedents creates tautology; and a mediator that is conceptually the same as the outcome cannot carry a mechanism. Before handing off to `jams-methods`, confirm each construct has a single, bounded definition, that no two constructs overlap conceptually, and that mediator, predictor, and outcome are genuinely distinct ideas — not three labels for the same thing.

## Checklist

- [ ] Every focal construct conceptually defined and distinct from its neighbors
- [ ] Conceptual model figure drawn; each path is a reasoned hypothesis
- [ ] Mechanism named via at least one mediator (process, not black box)
- [ ] Boundary conditions / moderators specified, with the theoretical reason they matter
- [ ] Theoretical lens fits the marketing phenomenon (not a generic borrowed theory)
- [ ] Managerial implication is derived from the mechanism, not bolted on
- [ ] Route (theory-first vs. empirics-first) declared honestly
- [ ] Constructs are conceptually distinct (no tautology, no predictor/outcome overlap)

## Anti-patterns

- **Hypothesis-by-citation**: "Prior work finds X→Y (Cite); thus H1" with no mechanism
- **Theory theater**: an elaborate framework that adds no new substantive insight
- **Main-effect-only logic**: no mediator, no moderator, no contingency
- **Borrowed-theory veneer**: a psychology/economics theory pasted on without marketing fit
- **Construct sprawl**: many overlapping constructs with no discriminant logic
- **A mechanism with no managerial consequence** anyone could act on

## Anti-patterns (continued)

- **Borrowing a lens you do not use:** naming a theory in the front end that never constrains a hypothesis or interpretation.
- **A model figure that overpromises:** boxes and arrows the empirics will not actually test.
- **Propositions with no logic** in a conceptual paper — assertions are not theory.

## Output format

```text
【Theoretical lens】RBV / commitment-trust / S-D logic / signaling / diffusion / consumer IP / ...
【Focal constructs (defined)】[...]
【Conceptual model】antecedents → focal → consequences; figure drawn? yes/no
【Mechanism (mediator)】X → M → Y: [...]
【Boundary conditions (moderators)】[...] + why they matter theoretically
【Route】theory-first / empirics-first (declared)
【Managerial implication derived】if mechanism holds → manager should [...]
【Next skill】jams-literature-positioning
```
