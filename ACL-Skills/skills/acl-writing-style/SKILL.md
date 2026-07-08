---
name: acl-writing-style
description: Use when revising an ACL paper for computational-linguistics house style, covering task-first framing, linguistic examples tied to quantitative error analysis, scoping language claims to tested languages, LLM-era claim discipline, anonymous self-reference, Limitations prose, and compressing into the 8-page or 4-page ACL format.
---

# ACL Writing Style

Use this on the manuscript itself. ACL reviewers are NLP specialists who read
for whether the paper understands *language* as well as *models*; the style
that survives them is concrete, example-grounded, and precisely scoped.

## First-page contract

- Open with the task or linguistic phenomenon, not the model family: what
  goes in, what comes out, why it is hard, and for whom.
- State the contribution as a typed claim by paragraph two: new method, new
  resource, new analysis, or new finding — ACL reviews are calibrated per type.
- Give one real example (input, desired output, failure of the status quo)
  on page one; abstract problem statements without an example read as vague
  at this venue.
- Say what languages the paper covers in the abstract if the answer is not
  "English only" — and if it is, say that too.

## Claim scoping in the LLM era

| Reflex phrasing | ACL-safe phrasing |
|---|---|
| "LLMs cannot do X" | "The five models tested fail X under these prompts" |
| "Our method understands Y" | "Improves the Y benchmark by n points; error classes A, B shrink" |
| "Works across languages" | "Evaluated on de/hi/sw/zh/ar; typological coverage discussed in §7" |
| "Significantly better" | Reserve for tested significance; give the test and p-value or interval |
| "State-of-the-art" | Scope to the exact setting, model scale, and date checked |

Reviewers increasingly ask whether a result is a property of the task, the
model snapshot, or the prompt; write so each claim names which.

## Examples and error analysis as prose

- Every qualitative example must be attached to a number: how often the
  illustrated behavior occurs, in which slice, under which condition.
  Cherry-picked generations presented as evidence is a named reject pattern.
- Use interlinear glosses or transliteration conventions correctly for
  non-English examples; sloppy linguistics costs credibility with exactly the
  reviewers who like the paper's topic.
- Name error categories functionally ("negation-scope errors") rather than
  narratively ("the model gets confused").

## Anonymity-compatible voice

- Write self-reference in third person: "Smith (2024) introduced X," never
  "In our previous work." Keep it in place until camera-ready.
- Do not cite "anonymous (under review)" material that reviewers cannot read;
  ARR bars relying on documents unavailable to them.
- Acknowledgements, funding, and AI-assistance credits are omitted at
  submission and added at camera-ready.

## Compression into 8 (or 4) pages

- The short-paper form is a single sharp point with one strong experiment —
  do not shrink a long paper into four pages; re-argue it.
- Push prompt dumps, per-language tables, and hyperparameter grids to the
  appendix; keep one summary row of each in the body (see `acl-supplementary`).
- Kill the related-work-as-inventory section; two paragraphs of positioned
  contrast beat a page of citations (see `acl-related-work`).
- Figures earn their space only when they carry an argument — pipeline
  diagrams restating the text are the first cut.

## Limitations and ethics prose

- Write Limitations as the referee brief against yourself: scope, data
  coverage, model dependence, evaluation validity. Specificity here is
  protected — ACL instructs reviewers not to penalize honest limitations.
- The optional ethics statement is for real stakes: human data, dual use,
  representational harm. A boilerplate ethics paragraph is worse than none.

## Micro-edit pass

```text
weak:   "We leverage powerful LLMs to achieve impressive gains."
strong: "Reranking with a 7B model cuts negation-scope errors from
         31% to 12% of sampled failures (Table 4)."

weak:   "Performance is good across all settings."
strong: "Gains hold on 4 of 5 languages; Swahili degrades (-1.2 F1),
         which §7 traces to tokenizer fragmentation."
```

## Terminology and notation discipline

- Pick one name per concept and hold it: a system called "our reranker,"
  "the verifier," and "the LLM judge" in three sections reads as three
  systems to a tired reviewer.
- Define task-specific terms at first use, even standard-seeming ones —
  "hallucination," "faithfulness," and "robustness" each have three
  incompatible literatures behind them.
- Dataset names get their citation at first mention and exact split names
  thereafter ("XNLI dev-matched," not "the dev set").
- Numbers in prose match tables to the decimal; reviewers diff them.
- Language codes: introduce once (ISO 639), then use consistently in
  tables, figures, and prose alike.

## Section-level failure smells

- An introduction with no example → underspecified task (fix first).
- A method section narrating engineering chronology ("we first tried...")
  → rewrite as design with rationale.
- A results section that re-reads the table aloud → replace with claims the
  table supports plus pointers into it.
- A conclusion introducing new claims → move them into results or delete;
  ACL reviewers treat conclusions as summaries under oath.

## Output format

```text
[Style diagnosis] task-first / model-first / survey-ish / underspecified
[First-page fix] <one concrete rewrite>
[Overclaim list] <claim -> scoped version>
[Example-evidence gaps] <anecdotes lacking counts>
[Compression plan] <cut / move / merge>
```
