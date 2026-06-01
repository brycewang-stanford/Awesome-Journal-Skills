---
name: jcf-submission
description: Use when running the final pre-submission preflight for the Journal of Corporate Finance (JCF) via Editorial Manager — the US$340 non-refundable fee, single-anonymized (non-anonymized) manuscript, ≤250-word abstract, author-date "your paper, your way" references, Option C data statement, declarations, and the optional free SSRN preprint. Final checks; it does not draft content.
---

# Submission Preflight (jcf-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Confirming the fee, abstract cap, references, declarations, and data statement are JCF-compliant
- Deciding on the optional free SSRN preprint at submission

## Process facts (verified; re-confirm on the official guide)

- Published by **Elsevier**; submission via **Editorial Manager**, reached from the ScienceDirect **"Submit your article"** link.
- A **US$340.00 non-refundable submission fee** is paid during submission; the paper is **considered only after payment**, and **desk-rejected articles are not refunded** (a handling fee, separate from any open-access APC).
- Review is **single anonymized (single-blind)** — submit a **non-anonymized** manuscript with author names and affiliations.
- **Abstract ≤ 250 words**; **1–7 keywords**; in-text **author-date** citations; **"your paper, your way"** references (consistent style, DOIs encouraged) at first submission.
- **Research data = Elsevier Option C**: include a **data-availability statement** at submission.
- A **competing-interest declaration** and a **generative-AI disclosure** are required; **free SSRN preprint posting** is offered.

## Preflight checklist

- [ ] US$340 fee ready (budgeted as **non-refundable**, no refund on desk reject), via Editorial Manager
- [ ] Author names/affiliations **included** (do not anonymize)
- [ ] Abstract ≤ 250 words, no references, abbreviations defined; 1–7 keywords
- [ ] In-text author-date citations; reference list consistent; DOIs added
- [ ] Tables/figures self-contained (FE, clustering, notes)
- [ ] Competing-interest declaration + generative-AI disclosure completed
- [ ] Elsevier Option C data-availability statement included (see jcf-replication-and-data-policy)
- [ ] Decide on the free SSRN preprint posting

## Anti-patterns

- Anonymizing the manuscript (JCF is single-blind, not double-blind).
- Forgetting the US$340 fee is **not refunded** even if desk-rejected.
- An abstract over 250 words; asserting a hard page limit (none stated, 待核实).

## Output

```
【Fee】US$340 ready, non-refundable understood? [Y/N]
【Manuscript】non-anonymized; abstract ≤250w; keywords 1–7? [Y/N]
【Refs】author-date, consistent, DOIs? [Y/N]
【Declarations】CoI + AI + Option C DAS? [Y/N each]
【Next】await desk screen → jcf-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data sources and Stata/R/Python packages for empirical corporate finance
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JCF URLs behind every fact in this pack
