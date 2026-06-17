---
name: car-writing-style
description: Use when polishing the prose of a Contemporary Accounting Research (CAR) manuscript — a front-loaded research question, disciplined accounting terminology, the ≤300-word abstract that states question/predictions/method/findings/implications, and CAR Style Guide conventions (footnotes not endnotes, author-date references on a new page). Polishes prose; it does not run the submission preflight (car-submission).
---

# Writing Style (car-writing-style)

## When to trigger

- The introduction buries the question and the finding under setup
- The abstract is over 300 words or omits a required element
- Prose is jargon-heavy, passive, or inconsistent in terminology
- References or notes do not follow CAR Style Guide conventions

## Write the CAR abstract to spec

CAR caps the abstract at **300 words** on an abstract page that begins the manuscript and carries the paper's title. The abstract should state, in order: the **research question and why it is important**, the **predictions** (if applicable), the **research method(s)**, the **principal findings**, and their **key implications** — followed by **up to six keywords** for indexing. Note that the CAAA translates every accepted abstract into **French** for publication, so write an abstract that is clear and self-contained, with minimal idiom, so it translates cleanly.

## Front-load the argument

- Open the introduction with the accounting question and why it matters; state the finding early rather than withholding it.
- Use active voice and precise accounting terminology (e.g., distinguish disclosure from recognition; earnings management from earnings quality; discretionary accruals construct vs. its proxy).
- State predictions before results; keep construct names, hypothesis labels, and variable names identical across text, tables, and the code repository.
- Keep the main text within the **30-page** guideline (50-page overall limit); move detail to the online appendix rather than expanding prose.

## CAR Style Guide conventions

- **Footnotes, not endnotes**, for in-text notes.
- **References begin on a new page** after the manuscript text, in the author-date style typical of accounting journals (the CAR Style Guide governs the exact format — set your reference manager to an author-date style and reconcile against it).
- 12-point, double-spaced; pages numbered sequentially after the abstract page.
- Keep the manuscript **blind**: no author names, affiliations, or "our prior work" phrasing — self-cite neutrally.
- Declare any **generative-AI** use and describe it in the Methods section (grammar/reference tools are exempt).

## Accounting-term consistency pass

Create a short terminology ledger before final polish:

| Term | Definition in manuscript | Table / code label | Risk if inconsistent |
| --- | --- | --- | --- |
| Construct | Economic/accounting concept, not just proxy name | Variable family | Reviewer thinks the proxy is the theory |
| Proxy | Exact measurement and data source | Column name / script variable | Replication fails or results are misread |
| Treatment / event | Institutional trigger and timing | Event-window variable | Identification and interpretation drift |
| Outcome | Financial reporting, audit, disclosure, tax, or governance outcome | Dependent variable | Implications overreach the measure |

Use the ledger to align abstract, hypotheses, tables, and code. CAR reviewers are sensitive to construct/proxy slippage; polish should remove ambiguity rather than merely improve style.

## Checklist

- [ ] Abstract ≤ 300 words with question/importance, predictions, method, findings, implications; ≤ 6 keywords
- [ ] Abstract written to translate cleanly into French
- [ ] Introduction front-loads the question and the finding
- [ ] Active voice; precise, consistent accounting terminology and labels
- [ ] Footnotes (not endnotes); references on a new page in author-date style
- [ ] Manuscript blind; self-citations neutral; AI use declared in Methods if applicable
- [ ] Main text within the 30/50-page budget
- [ ] Terminology ledger aligns constructs, proxies, tables, and code labels

## Anti-patterns

- **Mystery-novel intros** that hide the finding until the results.
- **Endnotes** or a non-author-date reference style straight from the manager.
- **Idiomatic abstract prose** that resists French translation.
- **Inconsistent construct/variable names** between text, tables, and code.
- **Proxy drift**: changing from a measurement claim to a theory claim without saying so.

## Output format

```
【Abstract】≤300 words; all elements present; ≤6 keywords; translation-friendly?
【Intro】question and finding front-loaded?
【Terminology】accounting terms precise; labels consistent?
【Construct/proxy ledger】text, tables, and code aligned?
【Style】footnotes, author-date refs on a new page, double-spaced, blind?
【AI disclosure】declared in Methods if used?
【Next step】car-submission
```
