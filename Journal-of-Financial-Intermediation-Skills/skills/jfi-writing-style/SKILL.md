---
name: jfi-writing-style
description: Use to revise a Journal of Financial Intermediation manuscript for the journal's house conventions — numbered sections, author–date Elsevier referencing, a concise stand-alone abstract, and prose that explains the intermediation mechanism before the specifications. It edits for style; it does not invent content.
---

# Writing Style (jfi-writing-style)

## When to trigger

- Polishing a JFI draft before submission or revision
- Aligning references, sections, and abstract with JFI/Elsevier conventions

## JFI house conventions (verified 2026-06-01; re-confirm on the official page)

- **Numbered sections** (1, 1.1, 1.1.1) structure the manuscript.
- **References:** "your-paper-your-way" at submission — any **internally consistent** style is accepted;
  the journal applies an **author–date (name–year) Elsevier** style at proof. In-text citations give
  surname(s) and year, with "et al." for three or more authors; the list is alphabetical then
  chronological, with a/b/c disambiguation for same-author/same-year items. Keep author–year fields clean.
- **Abstract:** concise, factual, and able to stand alone, with references avoided; there is **no stated
  numeric word cap** (待核实).
- **Optional Highlights:** 3–5 bullets, max 85 characters each, strongly encouraged.
- **Generative-AI disclosure:** if AI writing tools were used, declare them in a dedicated section
  **before the References** (see jfi-submission).

## Make the mechanism land

JFI is read by intermediation specialists who reward a clearly motivated **economic mechanism**:

- Explain the intermediary friction and channel **before** the econometric specification or the formal
  model — the reader should know *why* before *how*.
- Tie every result back to the intermediation contribution (see jfi-contribution-framing); avoid
  coefficient-by-coefficient narration with no economic interpretation.
- Define institutional terms on first use; precision about banks, loans, and regulation signals fluency.

## Anti-patterns

- A numbered/footnote citation style left in at submission with no internal consistency
- An abstract stuffed with references or with no stated finding
- Specifications introduced before the mechanism is explained
- Forgetting the AI-disclosure section when such tools were used

## Output format

```
【Sections】numbered (1, 1.1)? [Y/N]
【References】internally consistent, author–year-ready? [Y/N]
【Abstract】concise, stand-alone, no refs? [Y/N]  (word cap 待核实)
【Mechanism-first】explained before specs? [Y/N]
【AI disclosure】present-if-used? [Y/N]
【Next skill】jfi-replication-and-data-policy
```
