---
name: aamas-topic-selection
description: Use when deciding whether a project is a strong AAMAS fit, comparing AAMAS with AAAI, IJCAI, NeurIPS, ICML, EC, and the JAAMAS journal, identifying whether the agents are truly the research object, naming the interaction primitive (solution concept, mechanism, coordination, negotiation), and sharpening the multiagent framing before writing begins.
---

# AAMAS Topic Selection

Use this before writing. AAMAS is strongest when the *agents* are the research object - when the
result exists because multiple self-interested or cooperating agents interact - not when a
single-agent method is dressed in multiagent vocabulary.

## Fit test

- Prefer AAMAS when the contribution advances game-theoretic reasoning, multiagent learning,
  mechanism design, auctions, negotiation, argumentation, coordination and teamwork, agent-based
  simulation, or social choice, with the interaction as the object.
- Route to NeurIPS or ICML if the core is a single-agent or general ML method and the
  multiagent setting is only a testbed.
- Route to AAAI or IJCAI if the contribution is broad AI - planning, knowledge representation,
  reasoning - without an interaction result at its center.
- Route to EC (Economics and Computation) if the contribution is primarily equilibrium
  computation, market design, or auction theory with the economics framing dominant.
- Route to the JAAMAS journal (or its AAMAS presentation track) when the work needs
  journal-length exposition and a full-length archival treatment.
- Check early whether the interaction result can be made convincing in an 8-page body.

## Fit signal table

| Signal in the project | AAMAS reading |
|---|---|
| A solution concept, mechanism, or coordination result paired with multiagent experiments | Core fit - the house genre |
| Emergent behavior that only appears because agents co-adapt | Core fit |
| Strong single-agent method benchmarked in a multiagent environment | Better served at NeurIPS or ICML |
| Pure market/auction theory with economics as the point | EC or an econ-CS journal |
| Broad AI reasoning with no interaction at its center | AAAI or IJCAI |

## Vignette: where a communication-learning project goes

A project trains agents to communicate and shows higher cooperation in a mixed-motive game.
AAMAS reading: strong fit if the analysis is about the *interaction* - what the emergent protocol
signals, whether it is incentive-compatible, how it changes the equilibrium. Strip the incentive
and coordination analysis and keep only a reward curve, and the same project reads as a general
MARL paper better suited to NeurIPS or ICML; grow it into a full theory of the signaling
equilibrium, and EC or JAAMAS becomes the better home.

## Sharpening moves before committing

- Name the interaction primitive: solution concept, mechanism, protocol, negotiation strategy,
  or coordination guarantee. If none exists, the AAMAS framing does not exist either.
- Apply the frozen-agent test: if the result survives with the other agents replaced by a static
  environment, it is single-agent and belongs elsewhere.
- Confirm the experiments can probe the interaction (deviation tests, held-out opponents), not
  merely accompany it.
- Topic emphasis and track structure drift between cycles; scan the current CFP and track list
  before final routing.

## Output format

```text
[Fit] strong AAMAS / possible AAMAS / better elsewhere
[Best venue] AAMAS / AAAI / IJCAI / NeurIPS / ICML / EC / JAAMAS / other
[Interaction primitive] <solution concept / mechanism / coordination / negotiation / none>
[Contribution sentence] <one sentence>
[Top rejection risk] <single-agent-in-disguise / concept-unnamed / thin-evaluation / scope>
[Next action] <theory, experiment, framing, or venue switch>
```
