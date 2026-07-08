---
name: oopsla-writing-style
description: Use when revising a draft into OOPSLA's register — design insight stated before the artifact, claims written to be falsifiable, motivating examples that carry semantics, journal-article pacing inside the 23-page cap, and honest threats-to-validity prose that preempts the revision lever rather than triggering it.
---

# OOPSLA Writing Style

An OOPSLA paper is read twice by design: once by a committee choosing among
four outcomes, and again — possibly by the same people — if a revision comes
back. Style at this venue therefore optimizes for *checkability*: a paper
whose claims can be verified paragraph by paragraph collects bounded revision
demands (or none), while a paper that argues by adjective collects unbounded
ones. The published form is a journal article (PACMPL), and the prose should
carry that register: measured, self-contained, built to be cited.

## Voice calibration

| Draft habit | OOPSLA replacement |
| --- | --- |
| "We present NovelTool, a novel system for..." | Name the design question and your answer; the tool arrives as evidence (see `resources/worked-examples/01-introduction.md`) |
| "Our approach significantly outperforms..." | The number, the baseline, the workload, the dispersion — or nothing |
| "To the best of our knowledge, first..." | A positioning sentence naming the nearest prior work and the delta (`oopsla-related-work`) |
| "Due to space limitations, details are in the appendix" | A body-level statement of what the appendix establishes (`oopsla-supplementary`) |
| A wall of formalism before any example | A running example that motivates each definition as it appears |

## The running example as load-bearing structure

OOPSLA's classic papers — from type-system counterexamples to
language-experience reports (`resources/exemplars/library.md`) — are built
around concrete programs. Choose one small example early and make it do
three jobs: expose the problem, exercise the mechanism, and mark the
boundary (show the case the mechanism does *not* handle). If your example
cannot demonstrate the limitation honestly, the limitation section will read
as boilerplate — reviewers notice.

## Claims that survive two readings

Write each contribution as a sentence with a built-in test:

```text
Weak:   "We propose an efficient analysis for X."
Strong: "The analysis decides X for programs in fragment F in O(n log n);
         outside F it degrades to a sound approximation, evaluated in §6.3."

Weak:   "Our semantics is more expressive."
Strong: "Every program typable under [prior] remains typable (Thm 4.1);
         the converse fails on the example of §2.2."
```

The strong forms give a Minor-Revision reviewer something bounded to check —
which is exactly the outcome ladder you want to be standing on.

## Journal pacing inside 23 pages

- Spend the first two pages entirely on problem, insight, and claims; a
  reader stopping there should be able to state your thesis.
- Sections should alternate *mechanism* and *evidence*; ten pages of design
  followed by two of evaluation reads as unvalidated, the inverse as
  unmotivated.
- Threats-to-validity and limitations get their own subsection with specific
  content: which claims depend on which assumptions, and what was not
  measured. Generic threats paragraphs are revision bait.
- Prose must not lean on the appendix for coherence; the 23 pages are the
  paper (`oopsla-supplementary` for the layering rule).

## Revision-aware editing

When revising for a second round, mark the diff in prose quality too: the
change log tells reviewers *where* you changed; the writing must make each
change locally self-justifying, because continuity means your examiners
remember the old text. Never quietly weaken a claim a reviewer challenged —
weaken it visibly, with the reason.

## Output format

```text
[Register] design-insight-led: yes/no + first page diagnosis
[Adjective sweep] unquantified evaluatives found: <count + worst three>
[Claim audit] contributions rewritten in falsifiable form
[Example] running example present / missing / does not mark boundaries
[Pacing] mechanism-evidence alternation + limitations specificity
```
