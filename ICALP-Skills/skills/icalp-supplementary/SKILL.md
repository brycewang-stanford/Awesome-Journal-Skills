---
name: icalp-supplementary
description: Use when splitting an ICALP (EATCS) theory paper between the 15-page main body and the clearly labelled appendix / full version — deciding what a referee must see in the body versus what may be deferred, ensuring every deferred proof is actually present and findable, and keeping the split consistent with lightweight double-blind review.
---

# ICALP Supplementary (the body / appendix / full-version split)

ICALP gives you a **15-page body** (excluding references and a clearly labelled appendix) plus an
appendix that may hold omitted proofs or a **full version**, read **at the program committee's
discretion**. The whole game is deciding **what goes where**: the body must let a referee *judge and
follow* the paper; the appendix must let them *verify* it. Getting this split wrong — either cramming
proofs into the body or hiding the substance in an unread appendix — is a common, avoidable weakness.

## The governing principle

> The body earns the referee's belief; the appendix earns their verification.

- The **body** contains the model, the theorem statements, the main ideas, the key lemmas, and enough
  of the central proof that a referee can see **why it is true** and **that it is nontrivial**.
- The **appendix / full version** contains the **complete proofs**, routine cases, and technical
  details a referee consults to confirm correctness.
- "At the PC's discretion" means the appendix is **not guaranteed** to be read — so nothing whose
  *significance* the referee must weigh may live only there.

## What must be in the body

- The **model and definitions** needed to state the results.
- **All headline theorem statements**, positioned against prior bounds.
- The **main technical idea** — the new lemma or technique that makes the result work — at least in
  proof-sketch form with the key step shown.
- Enough structure that every deferred proof has a **clear pointer** ("full proof in Appendix B.2").

## What may be deferred to the appendix / full version

- **Complete proofs** whose ideas are sketched in the body.
- **Routine or standard** arguments, long case analyses, and calculations.
- **Auxiliary lemmas** whose statements the body can cite.
- Supporting **computation / certificates** (see `icalp-experiments`, `icalp-reproducibility`).

## The two failure modes

| Failure | Symptom | Fix |
|---|---|---|
| **Over-stuffed body** | Every proof crammed into 15 pages; unreadable, over-budget | Move complete proofs to the appendix, keep sketches + key lemmas in the body |
| **Hollow body** | Body states theorems, all proofs (incl. the key idea) dumped in an unread appendix | Bring the central technique and the main lemma's proof idea into the body |

The hollow body is the more dangerous: referees judge on the body, and a paper whose substance they
cannot see reads as either thin or evasive, even if the appendix is perfect.

## Completeness and findability

- **Every deferred proof must actually exist** in the appendix / full version. "Proof omitted" with no
  full version is a soundness failure, not a space saving (`icalp-reproducibility`).
- Deferred proofs must be **findable**: label appendix sections to match the body's pointers so a
  referee spends seconds, not minutes, locating a step.
- Keep the **submission appendix and any public full version consistent** in content.

## Double-blind consistency

- The appendix / full version is part of the **anonymous** submission: no author names,
  acknowledgements, grant numbers, or de-anonymizing links there either.
- If you host a full version on arXiv, refer to it as "the full version" without the identifying handle
  during review (`icalp-submission`).

## Worked split: a two-theorem paper

An algorithm (Thm 1) and a matching conditional lower bound (Thm 2). Body: the model; both theorem
statements with the prior-bound comparison; the algorithm's design and the **one key invariant**
proved; the reduction's **construction and its intuition**. Appendix / full version: the full
correctness proof and complexity analysis of the algorithm; the complete case analysis of the
reduction; a computer-checked verification of the gadget. Result: a referee can judge significance and
follow both ideas from the body, then verify every detail in the appendix.

## Output format

```text
[Body budget] <=15pp excl. refs + appendix; over/under
[In body] model / theorem statements / key technique / main-lemma idea: all present? gaps
[Deferred] complete proofs, routine cases, computation — each with a body pointer? yes/no
[Hollow-body check] is the central idea visible in the body (not only the appendix)? yes/no
[Completeness] every deferred proof actually present and findable? yes/no
[Anonymity] appendix/full version scrubbed and referenced without de-anonymizing? yes/no
[Fix queue] <ordered moves between body and appendix>
```
