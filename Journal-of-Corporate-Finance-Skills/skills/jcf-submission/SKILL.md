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

> ACCURACY NOTE (re-verified 2026-06-22 on ScienceDirect): the **US$340** submission fee, the **USD 4,520** hybrid-OA APC, and the **Co-Editors-in-Chief H. Almeida (Illinois) and K. Hankins (Kentucky)** are current. Re-verify before submission.

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

## Editorial Manager run-sheet

Work the EM screens in order; partially completed submissions stall silently:

1. Article type — full-length original manuscript versus shorter format paper; choose deliberately, it frames length expectations.
2. Title/abstract/keyword entry — paste the ≤250-word abstract; EM metadata must match the PDF exactly.
3. Author roster — every author with affiliation and email; the manuscript is non-anonymized, so consistency matters.
4. Declarations — competing interests, generative-AI disclosure, funding, and the Option C data-availability statement.
5. File upload — manuscript, exhibits per current guidelines, any internet appendix as supplementary material.
6. Fee payment — US$340, paid in-flow; the submission is not considered until it clears.
7. PDF approval — actually open the EM-built PDF; figure corruption and missing appendices are caught here or by the desk.

## Package inventory (calibration, hedged)

A typical complete JCF package — confirm against the journal's current author guidelines for required file types:

```text
main.pdf               # title page, abstract (≤250w), body, references, exhibits
declarations           # CoI + generative-AI disclosure via the EM declarations step
data_statement.txt     # Option C wording (see jcf-replication-and-data-policy)
internet_appendix.pdf  # IA tables/figures numbered IA.1, IA.2, …
cover_letter.pdf       # one-paragraph pitch + fit to the JCF remit
```

## Metadata snags that stall submissions

- Abstract in EM differs from the PDF — flagged at the desk; sync them last.
- Keywords outside the 1–7 band, or generic ("finance") — wastes the discoverability slot.
- A coauthor's email bouncing — EM verification halts until it is fixed.
- An internet appendix cited in the text but never uploaded — reviewers ask, a round is lost.
- Choosing "shorter format" then uploading a 60-page manuscript — the type/length mismatch invites a desk query.

## SSRN preprint call at submission

JCF offers free SSRN posting in-flow. Take it when priority matters (a crowded corporate-governance or ESG race) or when working-paper visibility helps recruit conference feedback before the first decision; skip it when the draft still carries claims you expect the desk screen or referees to force down, since the posted version circulates regardless of the outcome. Whatever you choose, keep the SSRN title identical to the EM title so citations consolidate.

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
