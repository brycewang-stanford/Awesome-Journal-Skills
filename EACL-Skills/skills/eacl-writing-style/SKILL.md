---
name: eacl-writing-style
description: Use when revising an EACL paper's prose for a task-first first page, a concrete page-one example, scoped LLM-era claims, quantified error analysis, an anonymity-safe voice, honest Limitations, and compression into the 8-page long or 4-page short content budget without pushing the argument into appendices.
---

# EACL Writing Style

Use this to revise an EACL paper so its contribution is legible fast and its claims are scoped.
EACL reviewers read many papers in a short window; the ones that land put the **task and the
result on the first page**, quantify rather than assert, and name their limits. Pair this with
the worked example in `../../resources/worked-examples/01-introduction.md`.

## The EACL first-page arc

1. **Task** — the specific problem, in the first breath, not "great progress in NLP."
2. **Gap** — why current methods fall short, each reason nameable.
3. **What we do** — the contribution, stated plainly.
4. **Measured result** — a number tied to a table, with variance.
5. **Honest scope** — what the result does and does not cover.

## Habits to cut, habits to keep

| Cut | Keep |
|---|---|
| "Achieves strong performance" | "Improves F1 by X (95% CI ...) over baseline B" |
| Generic "prior work is limited" | A specific failure per cited approach |
| A concrete example only on page 5 | A worked example on page 1 |
| Unscoped "our method generalizes" | "On the six languages tested; see Limitations" |
| Roadmap standing in for an argument | A one-line roadmap after the argument |

## Scope the LLM-era claim

- If the paper uses or evaluates LLMs, **bound the claim to the models, prompts, and settings
  tested**, and disclose contamination risk. An unscoped "LLMs can/cannot do X" invites the
  reviewer to name the counterexample.
- Report prompts and decoding as part of the method, not as trivia (see `eacl-reproducibility`).

## Quantify the error analysis

- A page-one or early-section **error analysis with counts** ("40% of errors are agreement
  errors; examples in Table 3") is worth more than adjectives. EACL rewards papers that show
  *where* and *why* a system fails, especially across languages.

## Anonymity-safe voice

```text
Anonymity check before submission:
  - no author names, affiliations, or acknowledgements
  - no "as we showed in our EMNLP 2025 paper" -> use third-person citation
  - no links that identify authors (personal repos, named grant pages)
  - self-citations phrased neutrally
```

## Multilingual clarity

- Name languages and scripts explicitly; render diacritics correctly in the PDF and later in the
  Anthology metadata (`eacl-camera-ready`).
- Do not let an aggregate multilingual score stand in for per-language honesty — a table beats an
  average.

## Compression discipline

- The **content pages carry the argument**; appendices carry detail. If cutting for length pushes
  a core claim into an appendix, cut something else instead (see `eacl-supplementary`).
- The **Limitations** section is free space and read — use it to state scope, not to hide
  results.

## Output format

```text
[First-page arc] Present / Missing elements: <task/gap/what/result/scope>
[Overclaims] <phrases to scope, with fix>
[Evidence pairing] <claims lacking a table/number>
[Anonymity] <any leak>
[Multilingual honesty] <aggregate-hiding issues>
[Compression] <what to cut so the body carries the claim>
```
