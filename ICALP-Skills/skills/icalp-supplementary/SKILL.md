---
name: icalp-supplementary
description: Use when splitting an ICALP (EATCS) theory paper between the first ten pages after the title page (which every referee reads) and the rest of the full-version submission (read at the committee's discretion; there is no page limit) — deciding what a referee must see early versus what may be deferred, ensuring every deferred proof is actually present and findable, and keeping the split consistent with lightweight double-blind review.
---

# ICALP Supplementary (the body / appendix / full-version split)

Since ICALP 2026 there is **no page limit**: authors are encouraged to submit the **full version**,
but the **first ten pages after the title page** must clearly present the merits, main contributions,
and key concepts and technical ideas, and material beyond the abstract, references and those ten
pages is read **at the committee's discretion** (ICALP 2027 Track B call, verified 2026-11-24; the
15-page extended-abstract-plus-appendix rule was ICALP 2025's). In this skill, the "body" means those
first ten pages and the "appendix / full version" means everything after them. The whole game is
deciding **what goes where**: the first ten pages must let a referee *judge and follow* the paper; the
rest must let them *verify* it. Getting this split wrong — either cramming every proof into the first
ten pages or hiding the substance after them — is a common, avoidable weakness.

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
| **Over-stuffed body** | Every proof crammed into the first ten pages; unreadable, the merits buried | Move complete proofs after page ten, keep sketches + key lemmas up front |
| **Hollow body** | The first ten pages state theorems, all proofs (incl. the key idea) come later and may go unread | Bring the central technique and the main lemma's proof idea into the body |

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
[First ten pages] merits + contributions + key ideas all within ten pages after the title page? yes/no
[In body] model / theorem statements / key technique / main-lemma idea: all present? gaps
[Deferred] complete proofs, routine cases, computation — each with a body pointer? yes/no
[Hollow-body check] is the central idea visible in the body (not only the appendix)? yes/no
[Completeness] every deferred proof actually present and findable? yes/no
[Anonymity] appendix/full version scrubbed and referenced without de-anonymizing? yes/no
[Fix queue] <ordered moves between body and appendix>
```
