---
name: jfi-writing-style
description: Use when revising a Journal of Financial Intermediation (JFI) manuscript for the journal's house conventions — numbered sections, author–date Elsevier referencing, a concise stand-alone abstract, specialist intermediation vocabulary, and prose that explains the mechanism before the specifications. It edits for style; it does not invent content.
---

# Writing Style (jfi-writing-style)

## When to trigger

- Polishing a JFI draft before submission or revision
- Aligning references, sections, and abstract with JFI/Elsevier conventions

## JFI house conventions (verified 2026-06-20; re-confirm on the official page)

- **Numbered sections** (1, 1.1, 1.1.1) structure the manuscript.
- **References:** "your-paper-your-way" at submission — any **internally consistent** style is accepted;
  the journal applies an **author–date (name–year) Elsevier** style at proof. In-text citations give
  surname(s) and year, with "et al." for three or more authors; the list is alphabetical then
  chronological, with a/b/c disambiguation for same-author/same-year items. Keep author–year fields clean.
- **Abstract:** concise, factual, and able to stand alone, with references avoided; keep it at **250 words
  or fewer**.
- **Keywords:** provide **1-7 English keywords** for indexing.
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

## Mechanism-first rewrite, worked (illustrative)

- **Before:** "We regress loan growth on the capital shortfall interacted with bank size, controlling for
  firm fixed effects. The coefficient is −2.1 and significant at the 1% level."
- **After:** "Banks that must rebuild capital face a choice between costly equity and shrinking assets.
  If lending relationships embody information rivals cannot replicate, constrained banks can cut
  relationship credit without losing the borrower — so recapitalization's burden falls on locked-in
  firms. Consistent with this, a 1pp shortfall reduces credit to the same firm by 2.1pp, and twice that
  for single-bank borrowers."
- The rewrite names friction → channel → prediction **before** the number, which is how this journal's
  specialist readership parses a result; the regression mechanics move to the design section.

## An intermediation lexicon check

Loose vocabulary signals a non-specialist to a single-blind referee who knows your name:

- **liquidity creation** (the Diamond–Dybvig transformation function) vs. **liquidity provision**
  (supplying funds) — not interchangeable;
- **capital requirement** (the rule) vs. **capital ratio** (the outcome) vs. **capital shock** (the
  change you exploit);
- say **credit supply** only after demand is absorbed — until then it is "lending growth";
- **relationship lending** implies repeated interaction and private information, not merely an existing
  loan;
- a **run** is strategic withdrawal, not any deposit outflow;
- **shadow bank** denotes intermediation outside the regulated perimeter, not any nonbank financial firm.

## Style pushbacks at this venue, and fixes

- "The introduction is a results list" → restructure as friction, mechanism, design, finding, lesson.
- "Notation drifts between model and empirics" → one symbol table; the model's friction parameter should
  be the object the regression coefficient estimates or proxies.
- "Reads like a policy report" → replace recommendation language with the equilibrium or identified
  margin the analysis actually delivers.
- "The abstract could describe ten papers" → one abstract sentence each for friction, design or model,
  headline magnitude or proposition, and the intermediation lesson; cut everything else.

## Anti-patterns

- A numbered/footnote citation style left in at submission with no internal consistency
- An abstract stuffed with references or with no stated finding
- Specifications introduced before the mechanism is explained
- Forgetting the AI-disclosure section when such tools were used

## Output format

```
【Sections】numbered (1, 1.1)? [Y/N]
【References】internally consistent, author–year-ready? [Y/N]
【Abstract】concise, stand-alone, no refs, <=250 words? [Y/N]
【Mechanism-first】explained before specs? [Y/N]
【AI disclosure】present-if-used? [Y/N]
【Next skill】jfi-replication-and-data-policy
```
