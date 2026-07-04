---
name: anmath-workflow
description: Use when deciding which anmath-* sub-skill to invoke next, or when sequencing work on a pure-mathematics manuscript from scope check through major revision for an Annals of Mathematics submission. Routes — does not replace — the specialized skills.
---

# Annals of Mathematics Workflow (anmath-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which
anmath-* skill to use at your current stage** of a theorem-and-proof manuscript.

Default assumption: unless you say otherwise, the target is **Annals of Mathematics**,
where the bar is significance + originality + a complete, correct, rigorously verified
proof with clear exposition. The importance threshold is very high and acceptance is
highly competitive.

## When to trigger

- You ask "what should I do next?" with a math paper in progress
- You have a draft and need to find the current bottleneck (significance? a gap? exposition?)
- You are cycling between proof, writing, and referee response and have lost the thread
- You received a referee report from Annals and need to switch into revision mode

## Routing table

| Current symptom                                                  | Next skill                |
|------------------------------------------------------------------|---------------------------|
| Unsure the result clears the Annals importance bar / is in scope | `anmath-scope-fit`        |
| Main theorem stated vaguely; significance/positioning unclear    | `anmath-results-framing`  |
| Proof works but the argument's architecture is not laid out      | `anmath-methods`          |
| Exposition is hard to follow; sectioning/notation/diagrams weak  | `anmath-figures`          |
| Long computations / auxiliary lemmas clutter the main line       | `anmath-supplementary`    |
| Prose is sloppy; "clearly"/"it is easy to see" hide steps        | `anmath-writing-style`    |
| Paper feels bloated or padded; every section not yet justified   | `anmath-length-management`|
| Preparing the cover note to the editors                          | `anmath-cover-letter`     |
| Ready to submit; need the final preflight                        | `anmath-submission`       |
| Want to anticipate how an expert referee will probe the proof    | `anmath-referee-strategy` |
| Received a report; need to revise and reply                      | `anmath-revision`         |

## Default order

1. `anmath-scope-fit` — confirm the result is important and original enough for Annals
2. `anmath-results-framing` — state the main theorem(s) precisely and position them
3. `anmath-methods` — lay out the proof strategy, key lemmas, and where the difficulty lies
4. `anmath-figures` — exposition and structure: sectioning, notation, statements-before-proofs
5. `anmath-supplementary` — move auxiliary results / long computations to appendices
6. `anmath-writing-style` — eliminate gaps and "clearly"; tighten every claim
7. `anmath-length-management` — confirm every section is necessary; cut bloat
8. `anmath-cover-letter` — concise letter framing significance for the editors
9. `anmath-submission` — final preflight (format, TeX, MSC, references, arXiv)
10. `anmath-referee-strategy` — stress-test the proof against expert scrutiny before sending
11. `anmath-revision` — after the report arrives

> `anmath-writing-style` and `anmath-length-management` are **late-stage polish**; do not
> run them before the proof is actually complete and the architecture is fixed.

## Decision heuristics

- "I am not sure this is big enough for Annals" → `anmath-scope-fit`
- "My main theorem is a paragraph, not a precise statement" → `anmath-results-framing`
- "The proof is right but readers can't see the plan" → `anmath-methods`
- "A referee would get lost in Section 3" → `anmath-figures`
- "I have a 6-page computation in the middle of the proof" → `anmath-supplementary`
- "I wrote 'it is easy to see' and it is not" → `anmath-writing-style`
- "The paper is 90 pages and I can't justify all of them" → `anmath-length-management`
- "I'm clicking submit tomorrow" → `anmath-submission`
- "I got a referee report" → `anmath-revision`

## Difference vs. a generic math-writing toolbox

A generic LaTeX/writing helper optimizes for readability alone. This stack is tuned to
the Annals standard: **the importance bar is unusually high, and a single hidden gap is
fatal**. Significance and complete rigor dominate every routing decision here.

## Submission bundle layout

The final preflight (`anmath-submission`) checks a concrete file tree. A single hidden gap
is fatal at Annals, so the arXiv/journal package must let a referee verify the proof
end-to-end with nothing missing. Target layout:

```text
paper-submission/
├── main.tex              % single self-contained source; amsart or Annals class
├── main.pdf              % compiled, matches .tex exactly
├── refs.bib              % all cited works; MathSciNet-verified keys
├── figures/              % vector (.pdf/.eps); each referenced in text
│   └── fig-1.pdf
└── README.txt            % MSC 2020 primary+secondary, arXiv id, prior-submission note
CHECK before upload:
  [ ] main theorem stated precisely in the introduction, with hypotheses explicit
  [ ] every lemma either proved here or cited to a verifiable source
  [ ] no "clearly" / "it is easy to see" standing in for an unwritten step
  [ ] appendices hold long computations; the main line stays readable
  [ ] cover letter frames significance for the editors (anmath-cover-letter)
```

## Anti-patterns

- **Do not** skip `anmath-scope-fit` — Annals desk-screens on importance first
- **Do not** let `anmath-figures` polish exposition while a proof gap remains open
- **Do not** let `anmath-revision` draft a reply before you have actually fixed the text
- **Do not** treat `anmath-supplementary` as a dumping ground — essentials stay in main text
