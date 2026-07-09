---
name: itcs-writing-style
description: Use when drafting or revising an ITCS paper's abstract, introduction, and technical presentation so the conceptual innovation lands before any theorem, the model is motivated as a lens rather than a tweak, scope and limitations are owned up front, and complete proofs are deferred cleanly — matching the ITCS emphasis on new ideas over technical depth.
---

# ITCS Writing Style

At ITCS the reader must feel the **innovation before the theorem**. Reviewers are briefed to
reward a new model, question, or connection over a deeper result on an old one, so a paper that
opens like a STOC depth paper — leading with a bound and a technique — reads as if it mistook the
venue. The whole job of the first pages is to make a skeptical expert think *"I hadn't thought to
ask that, and I want to"* before they reach a single lemma. Because ITCS has **no rebuttal**
(see [`itcs-review-process`](../itcs-review-process/SKILL.md)), the writing must also *pre-empt*
objections there is no later chance to answer.

## The ITCS first-page arc

Structure the abstract and introduction as:

1. **The new question or model** — the first breath. Name the object or ask the question the
   standard setting cannot phrase. Not "we study X with parameter Y," but "here is a thing worth
   thinking about that we did not have a way to talk about."
2. **Why the field lacked it** — isolate the silent assumption or missing seam that hid the
   question. This is the honest delta (see [`itcs-related-work`](../itcs-related-work/SKILL.md)).
3. **The conceptual payoff** — what the new lens *lets us see or do*: a connection, a
   reorganization of known questions, a new axis of measurement.
4. **A result that shows the model is alive** — at least one crisp theorem (a separation, a
   surprising possibility, an impossibility) proving the model is neither empty nor everything.
   ITCS PCs probe every new model for exactly this.
5. **Scope and directions** — own what is unresolved and frame the open problems as the
   deliverable. At ITCS a candid "first map" beats a polished increment.

See the before/after in
[`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md).

## Lead with the idea, not the machinery

- **State the contribution as a new noun.** "We introduce *forgetful certificates*" beats "we
  analyze memory-bounded provers." A named object the community can adopt is the ITCS currency.
- **Motivate the model as a lens, not a tweak.** Do not write "we add a bound"; write what the
  bound *reveals*. The move that earns ITCS acceptance is showing the new setting makes an old
  thing look different.
- **Spend the abstract's real estate on why-it-matters, not on constants.** "Improving the
  constant" or "tightening the bound" is a depth-venue virtue; at ITCS it can actively signal the
  wrong fit. Report the result, then immediately its conceptual consequence.
- **Do not over-claim finality.** ITCS respects a bold, incomplete direction. Overselling a
  first foray as the last word invites the reviewer to test it as one and find the gaps.

## The first-10-pages merits window

ITCS submissions have **no hard page limit**, but the community norm (stated in the call) is that
the **first ~10 pages** give a clear, self-contained presentation of the paper's **merits,
significance, innovations, and place in the literature**, with complete proofs following (in an
appendix if needed). Treat those ten pages as the document a busy PC member actually reads to
decide:

- The model, the motivation, the main results, and the *why-new* must all fit and cohere there.
- Proof *ideas* (a paragraph of intuition per main theorem) belong here; full proofs can defer.
- Do not bury the innovation on page 14 behind preliminaries — if the merits are not legible by
  page 10, the paper is effectively judged as if they are absent.

## Pre-empting objections (because there is no rebuttal)

Write the three reviewer objections *into* the paper:

- **"Is the model trivial or all-powerful?"** -> the anchoring result in the intro, and a
  remark placing your model between two known extremes.
- **"Is this actually new?"** -> a delta-first related-work paragraph that names the closest
  prior model and says exactly what it did not ask (not a citation dump).
- **"Why should the community care?"** -> a concrete payoff: a connection drawn, a question
  reframed, an application sketched — even if informal.

## Technical presentation

- **Definitions before use, self-contained.** A reviewer should parse every theorem statement
  without your prior papers open — which lightweight double-blind would expose anyway.
- **One idea per definition.** Resist bundling three parameters into a mega-definition; ITCS
  readers value a clean object they can carry away.
- **Proof intuition in the body, full proofs deferred cleanly.** Each main theorem gets a "proof
  sketch / idea" paragraph in the merits window; the complete proof lives later or in an
  appendix, clearly cross-referenced. Never write "the proof is standard" for a central claim.
- **Keep the open problems as a real section.** At ITCS they are part of the contribution — a good
  open-problems section is an invitation the community accepts by working on your model.

## Common failure modes at ITCS

| Symptom | Why it fails here | Fix |
|---|---|---|
| Abstract leads with a bound/technique | Reads as a STOC depth paper; the idea is hidden | Lead with the new question/model |
| New model with no result | "Definition in search of a theorem" | Add an anchoring result showing it is alive |
| "New" question is a known one relabeled | Novelty is the selection axis; a rename fails it | Do the honest delta; find the truly new seam |
| Merits not legible by page 10 | The window the PC reads shows nothing | Restructure so model+motivation+results fit early |
| Over-claimed finality on a first foray | Invites the reviewer to find the gaps | Own the scope; frame open problems as the point |
| Central proof marked "omitted"/"standard" | Violates the full-proof requirement | Include the complete proof (appendix if needed) |

## Output format

```text
[ITCS framing status] innovation-first / buried / mis-venued
[First breath] does p.1 pose a NEW question/model before any theorem? yes/no
[Alive] anchoring result present (not empty / not everything)? yes/no
[Merits window] model+motivation+results legible within ~10 pages? yes/no
[Objections pre-empted] trivial? / new? / why-care? all answered in-text? yes/no
[Proofs] every central claim fully proved (appendix ok)? yes/no
[Fix queue] <ordered edits>
```
