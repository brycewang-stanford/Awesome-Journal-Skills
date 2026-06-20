---
name: jcp-theory-development
description: Use when building the psychological theory and hypotheses for a Journal of Consumer Psychology (JCP) manuscript — naming the mechanism (mediator), deriving theory-predicted moderators, and ruling out rival processes. Builds the mechanism that IS the contribution; it does not run the studies (jcp-methods).
---

# Theory Development (jcp-theory-development)

## When to trigger

- You have a consumer effect but no explanatory **psychological process**
- Hypotheses read as "A increases B" with no account of *why* it happens in the mind
- A reviewer wrote "the theory is thin" or "this is an effect in search of a process"
- Your moderators feel like a robustness dump rather than tests of the mechanism
- You cannot name, in one clause, the mediator that produces the effect

## At JCP the mechanism IS the contribution

JCP does not reward effects; it rewards **explanations of effects**. The theory section must specify a **psychological process** — a shift in inference, construal, attention, affect, motivation, goal activation, identity, or processing fluency — that *generates* the consumer outcome, and then derive hypotheses that test that process a priori. The standard frame is a causal chain: **antecedent → psychological process (mediator) → consumer outcome**, with **moderators** that the process predicts. A paper whose contribution is "X affects Y" will be desk-rejected or sent back; a paper whose contribution is "X affects Y *because* it changes mental state M, and only when condition C holds" is a JCP paper.

## Build the process, not the prediction

- **Name the mediator concretely.** "Increased motivation" is too vague; "an inflated sense of personal control that lowers perceived risk" is a process. The mediator should be a known or definable psychological construct with established measurement.
- **Derive moderation from the mechanism.** The most persuasive JCP moderators are ones that **switch the process on or off**: if the effect runs through M, then blocking M (cognitive load, an alternative goal, a manipulation that satisfies the need M serves) should attenuate or reverse it. That is a theoretical claim, not a sensitivity check.
- **State hypotheses a priori; avoid HARKing.** Each study should test a distinct link in the chain (effect → mediation → moderation → boundary). Post-hoc explanations dressed as predictions are the rigor-era's cardinal sin and reviewers look for it.
- **Pre-empt rival processes.** A JCP reviewer will propose a competing mechanism (demand, mood, a confounded construal). Name the leading rivals and design the theory so a study can adjudicate — ideally a moderator that *your* process predicts but the rival does not.

## Theory archetypes JCP rewards

| Archetype | What the contribution looks like |
|-----------|----------------------------------|
| Novel mediator | A familiar effect is shown to run through an unexpected mental process |
| Process adjudication | Two rival mechanisms are pitted against each other; data favor one |
| Moderation-as-theory-test | A theory-predicted moderator turns the effect off, proving the process |
| Boundary / when-not | Specifying conditions under which a "known" effect reverses, via the mechanism |
| New construct | A new consumer-psychological construct, defined, measured, and shown to do work |

## Checklist

- [ ] The mediator is named as a concrete psychological construct, not a vague "motivation/感觉"
- [ ] The causal chain antecedent → process → outcome is explicit
- [ ] At least one moderator is derived *from* the mechanism (switches the process on/off)
- [ ] Hypotheses are a priori and map onto a planned study chain
- [ ] The leading rival process(es) are named and there is a plan to rule them out
- [ ] The theory engages and changes an existing account, not just labels an effect

## Anti-patterns

- **Effect in search of a process**: a robust result with no mechanism — the classic JCP reject
- **Mediator-as-restatement**: a "mediator" that is just the dependent variable measured earlier
- **Moderator dump**: boundary conditions with no theoretical rationale tied to the process
- **HARKing**: presenting post-hoc accounts as a priori hypotheses
- **Borrowed-label theory**: invoking a construct's name (e.g., "construal level") without using its logic or measuring it
- **Single rival blindness**: ruling out one alternative while ignoring the one the reviewer will actually raise

## Output format

```text
【Effect】antecedent → consumer outcome
【Process (mediator)】the named psychological mechanism = the contribution
【Moderators】theory-predicted, with which switch the process on/off
【Rival processes】named + how a study adjudicates
【Study chain】effect → mediation → moderation → boundary (study-by-study)
【What changes in the literature】advance / deepen / overturn which account
【Next skill】jcp-literature-positioning
```
