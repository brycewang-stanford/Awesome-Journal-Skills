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

## Output format

```text
[Writing diagnosis] clear / overloaded / underspecified / policy-risky
[First-page fix] <new framing>
[Compression cuts] <what to move or delete>
[Anonymity edits] <phrases to rewrite>
[Ethics/reproducibility edits] <specific additions>
```
