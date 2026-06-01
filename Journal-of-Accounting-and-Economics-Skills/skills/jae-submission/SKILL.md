---
name: jae-submission
description: Use when preparing to submit to the Journal of Accounting and Economics (JAE) — the Editorial Manager preflight, the USD 650 submission fee, double-anonymized file separation (anonymized manuscript plus title page), mandatory Highlights, keywords and JEL codes, and Elsevier author-date formatting.
---

# Submission Preflight for JAE (jae-submission)

## When to trigger

- The manuscript is complete and you are about to upload
- You are unsure what files Editorial Manager requires or how anonymization works
- You need to budget for the submission fee or confirm formatting requirements

## Submission system and fee

JAE submits through Elsevier **Editorial Manager (EM)**, which converts your files into a single review PDF. A **USD 650 submission fee** is charged for unsolicited **new** manuscripts; there is **no fee for resubmissions** (revisions). The fee is paid during the submission process via Elsevier's Submission Start portal (submissionstart.elsevier.com); **EU authors add applicable VAT**. The paper is only considered after the fee is paid; proceeds fund journal activities and reviewer reimbursements. (The fee amount is **待核实** against the live Guide for Authors — the current guide and the 2025 JAE Conference state USD 650, while an older Wharton mirror shows USD 500.)

## Double-anonymized file separation

JAE uses **double anonymized** review. Prepare:

- An **anonymized manuscript** with all author-identifying information removed (no names, no acknowledgments revealing identity, no self-citations that unmask authorship, scrubbed file metadata).
- A separate **title page** with author names, affiliations, contact details, and acknowledgments.
Check that headers, file properties, and "thank you" footnotes do not leak identity.

## Required packaging

- **Highlights**: 2-5 bullet points, **max 125 characters each**.
- **Keywords**: up to **6** (American spelling).
- **JEL classification codes**: up to **6** — required.
- **References**: Elsevier author-date (Harvard) style; numbered sections (1, 1.1, 1.1.1).
- **LaTeX** (optional): Elsevier `elsarticle.cls` with BibTeX; single-column native format.
- A concise, factual **abstract** (purpose, principal results, major conclusions; stands alone; no references or uncommon abbreviations). No numeric word cap is stated in JAE's own guide (待核实 — third-party sites cite ~250 words, unconfirmed).

## Length and data policy

- **No explicit page or word limit** is stated in the Guide for Authors; the main text is divided into clearly numbered sections.
- **Data/code**: JAE follows Elsevier's **voluntary** research-data policy — it "encourages and enables" data sharing, data linking, a Data Statement, and the `[dataset]` citation tag, but does **not mandate** a replication archive (unlike JAR or JFE). Decide whether to share voluntarily.
- **Originality**: no simultaneous submission; Elsevier screens with Crossref Similarity Check (iThenticate). Editors may desk-reject or redirect unsuitable papers (Article Transfer Service).

## Checklist

- [ ] Editorial Manager account + ORCID linked
- [ ] Submission fee (USD 650, 待核实) budgeted; VAT for EU authors
- [ ] Anonymized manuscript + separate title page; metadata scrubbed
- [ ] Self-citations and acknowledgments do not unmask authorship
- [ ] Highlights (2-5, ≤125 chars), ≤6 keywords, ≤6 JEL codes
- [ ] Elsevier author-date references; numbered sections
- [ ] Concise factual abstract; data-sharing decision made
- [ ] No concurrent submission; originality screen anticipated

## Anti-patterns

- **Uploading a non-anonymized manuscript** for double-anonymized review.
- **Forgetting the fee** and stalling the submission.
- **Missing Highlights or JEL codes.**
- **Numbered/Vancouver references** instead of Elsevier author-date.
- **Assuming a mandatory replication archive** is required (it is not, but document code anyway).

## Output format

```
【System】Editorial Manager; fee USD 650 (待核实) + VAT if EU
【Files】anonymized manuscript + title page; metadata scrubbed
【Packaging】Highlights ✓ keywords(≤6) ✓ JEL(≤6) ✓
【References】Elsevier author-date (Harvard) ✓
【Data policy】voluntary sharing decision: share / not
【Open items】... (verify live Guide for Authors)
【Next step】jae-review-process
```
