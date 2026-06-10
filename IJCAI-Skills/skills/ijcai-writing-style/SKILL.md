---
name: ijcai-writing-style
description: Use when revising an IJCAI or IJCAI-ECAI paper for broad AI significance, 7-page-body compression, self-contained exposition, double-blind wording, optional ethics discussion, reproducibility clarity, and policy-safe use of LLM editing.
---

# IJCAI Writing Style

Use this when revising the main paper. IJCAI rewards clear, significant, original AI work
that a broad program committee can evaluate quickly.

## Revision rules

- Put the AI contribution in the first page: problem, gap, core idea, evidence, and why it
  matters beyond a narrow benchmark.
- Keep the submission self-contained; supplementary material should support, not rescue, the
  main argument.
- Spend the 7-page body on claims reviewers can verify: formal setup, method, theorem or
  algorithm, baselines, ablations, and limitations.
- Use third-person citation language for prior work by the authors and remove
  acknowledgements, contribution statements, and identity-revealing phrasing from the review
  version.
- Include an ethics or broader-impact statement when sensitive data, high-stakes deployment,
  safety, discrimination, privacy, consent, copyright, or societal harm is plausible.
- Treat LLM assistance conservatively. Style polishing may be acceptable in some cycles, but
  LLM-written manuscript text, fake citations, or unverified claims can trigger rejection.

## Writing for a cross-subfield committee

IJCAI's PC mixes symbolic AI, search, planning, KR, constraint reasoning, multi-agent, game
theory, ML, NLP, and vision. Write so a reviewer outside your niche reaches the contribution
fast, because the out-of-area reviewer often drives summary-reject risk.

| Reader risk | Symptom in the draft | Page-discipline fix |
| --- | --- | --- |
| Out-of-area reviewer lost early | Contribution buried after a long formal preamble | State problem, gap, and claim on page one |
| Notation overload | New symbols before motivation | Introduce notation only when the claim needs it |
| Niche jargon | Subfield acronyms undefined | Define on first use; assume a broad AI reader |
| Body overflow | Method spills toward the reference pages | Move proofs and grids to the appendix, keep claims in the body |

## Worked vignette: framing a KR paper for breadth

A knowledge-representation paper opens with three paragraphs of description-logic preliminaries
before naming its contribution. A planning or learning reviewer may summary-reject for unclear
significance. The fix: open with the reasoning task, why current encodings fall short, and the
new tractable fragment, then defer the heavy formalism. The technical depth stays; only the
ordering changes so a broad IJCAI reader sees the payoff within two reads.

## Reviewer pushback and the venue-specific fix

- "Could not find the contribution." Rewrite the first page as problem, gap, idea, evidence,
  significance; this is the single highest-leverage IJCAI edit.
- "Reads like a journal extension." Compress to the body limit and cite the longer work in
  third person rather than reproducing it.
- "Significance only within one benchmark." Add a sentence on why the result matters across AI,
  not just on the chosen suite.

## Output format

```text
[Writing diagnosis] clear / overloaded / underspecified / policy-risky
[First-page fix] <new framing>
[Compression cuts] <what to move or delete>
[Anonymity edits] <phrases to rewrite>
[Ethics/reproducibility edits] <specific additions>
```
