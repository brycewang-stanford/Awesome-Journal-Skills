---
name: soctheory-argument-development
description: Use when stress-testing the reasoning of a Sociological Theory (ST) manuscript — turning stated propositions into a valid, warranted argument that survives rival theories and counter-cases. Develops and audits the argument; it does NOT define the concepts (soctheory-theory-construction) or bound the theory's domain (soctheory-boundary-conditions).
---

# Argument Development: Warrants, Rivals, Validity (soctheory-argument-development)

## When to trigger

- Concepts and propositions exist, but the reasoning that connects them is thin
- A reviewer would say "the propositions don't follow from the premises"
- You have not engaged the obvious rival explanation
- The argument has not been tested against a counter-case or a hard case

> At ST, logical soundness plays the role statistics play at empirical journals. The argument
> *is* the evidence. This skill makes it valid before reviewers find the gaps.

## The argument audit

Walk the manuscript's spine — premises → mechanism → propositions → conclusion — and check
each link. Reed's "Justifying Sociological Knowledge" (ST 2008, 26(2):101–129) frames the
central demand: every theoretical claim carries an implicit *warrant*, and you owe the reader
the warrant, not just the claim.

1. **Premise check.** Are the starting premises stated, defensible, and consistent with the
   assumptions from `soctheory-theory-construction`? An unstated premise is a hidden bet.
2. **Inference check.** Does each proposition actually *follow* from the premises + mechanism?
   Name the inference type — deductive derivation, **abduction** (the "best explanation" move
   central to ST theorizing; cf. Timmermans & Tavory, ST 2012, 30(3):167–186), or analogy —
   and check it is doing legitimate work.
3. **Warrant check.** For each major claim, state the warrant: *why is this a good reason to
   believe the claim?* If the warrant is "it seems plausible," it is not yet an argument.
4. **Rival-theory check.** Name the strongest rival explanation and show, on theoretical
   grounds, why yours is better (more parsimonious, more general, dissolves an anomaly the rival
   cannot). Defeating a strawman convinces no one.
5. **Counter-case / hard-case check.** Construct the case where your theory would seem to fail.
   Either the argument handles it, or you have found a boundary condition (hand to
   `soctheory-boundary-conditions`).

## Toulmin per proposition

A compact discipline for each load-bearing proposition:

- **Claim** — the proposition.
- **Grounds** — the concepts/premises it rests on.
- **Warrant** — why the grounds support the claim (the mechanism does most of this work).
- **Backing** — the tradition or prior reasoning that licenses the warrant.
- **Rebuttal** — the condition under which the claim would not hold (a candidate boundary condition).

A proposition that cannot fill *warrant* and *rebuttal* is an assertion, not a theoretical claim.

## Handling rivals without data

Because ST does not test, you adjudicate rivals **theoretically**:

| Rival situation | Theoretical move |
|-----------------|------------------|
| Rival explains the same cases | Show your account is more parsimonious or unifies more |
| Rival rests on a shakier premise | Expose and challenge that premise |
| Rival and yours seem observationally equivalent | Specify a *conceptual* difference that matters, even if untested |
| Rival is a special case of yours | Subsume it and show the added range |

## Checklist

- [ ] The premises are stated and consistent with the theory's assumptions
- [ ] Each proposition demonstrably follows from premises + mechanism (inference type named)
- [ ] Each load-bearing claim states its warrant (not "it seems plausible")
- [ ] The strongest rival theory is named and answered on theoretical grounds
- [ ] At least one counter-case / hard case is constructed and handled (or yields a boundary condition)
- [ ] No empirical "test" stands in for an argument; data, if any, only illustrates

## Anti-patterns

- A chain of plausible-sounding claims with no stated warrants
- Engaging a strawman rival instead of the strongest one
- "Future research could test this" used to dodge a current logical gap
- Abduction invoked as a license to assert rather than to reason toward the best explanation
- Inconsistency: a later proposition silently violating an earlier premise
- Smuggling an empirical result in as if it settled a theoretical dispute

## Output format

```
【Spine】premises → mechanism → propositions → conclusion: valid? [Y/N + gaps]
【Warrants stated】per load-bearing claim: yes / missing [...]
【Strongest rival】[named] → why yours wins (theoretically)
【Counter-case】[case] → handled / becomes a boundary condition
【Inference types】deductive / abductive / analogical — each legitimate?
【Next step】soctheory-boundary-conditions
```
