---
name: jae-submission
description: Use when preparing to submit to the Journal of Accounting and Economics (JAE) — the Editorial Manager preflight, submission-fee live check, double-anonymized file separation (anonymized manuscript plus title page), mandatory Highlights, keywords and JEL codes, and Elsevier author-date formatting.
---

# Submission Preflight for JAE (jae-submission)

## When to trigger

- The manuscript is complete and you are about to upload
- You are unsure what files Editorial Manager requires or how anonymization works
- You need to budget for the submission fee or confirm formatting requirements

## Submission system and fee

JAE submits through Elsevier **Editorial Manager (EM)**, which converts your files into a single review PDF. Local source-map defaults use **USD 650** for unsolicited **new** manuscripts and no fee for resubmissions, but you must check the current ScienceDirect Guide for Authors before payment. The fee is paid during the submission process via Elsevier's Submission Start portal (submissionstart.elsevier.com); **EU authors add applicable VAT**. The paper is only considered after the fee is paid; proceeds fund journal activities and reviewer reimbursements.

## Double-anonymized file separation

JAE uses **double anonymized** review. Prepare:

- An **anonymized manuscript** with all author-identifying information removed (no names, no acknowledgments revealing identity, no self-citations that unmask authorship, scrubbed file metadata).
- A separate **title page** with author names, affiliations, contact details, and acknowledgments.
Check that headers, file properties, and "thank you" footnotes do not leak identity.

## Editorial Manager upload walkthrough

EM builds the review PDF from the files in the order you upload them, so sequence deliberately: (1) the anonymized manuscript (abstract, body, references, appendices, exhibits placed per Elsevier rules); (2) the separate title page carrying authors, affiliations, corresponding-author contact, acknowledgments, and declarations; (3) any online appendix meant for reviewers. After EM compiles, **open and read the generated review PDF end to end** — approving a garbled or identity-leaking build is the author's error. Verify that no author name survives in figure captions, appendix headers, tracked-changes remnants, or PDF bookmarks and document properties.

## Required packaging

- **Highlights**: 2-5 bullet points, **max 125 characters each**.
- **Keywords**: up to **6** (American spelling).
- **JEL classification codes**: up to **6** — required.
- **References**: Elsevier author-date (Harvard) style; numbered sections (1, 1.1, 1.1.1).
- **LaTeX** (optional): Elsevier `elsarticle.cls` with BibTeX; single-column native format.
- A concise, factual **abstract** (purpose, principal results, major conclusions; stands alone; no references or uncommon abbreviations). Do not import a numeric abstract cap from third-party templates unless the current JAE guide states it.

## Writing Highlights and choosing JEL codes

- Draft each Highlight as a **finding plus its economic mechanism**, not a topic label: "Disclosure rises where proprietary costs fall; liquidity gains concentrate in opaque firms" beats "We study disclosure and liquidity." Count characters including spaces against the 125-character cap; verbs, not nouns, carry the bullet.
- JEL codes tell the editor which economics conversation the paper joins: pair the accounting classification (M41) with the codes your mechanism actually lives in — contracting/capital-markets (G-family), information economics (D-family), or regulation (K/L-family) as the paper warrants. Three precise codes signal fit better than six generic ones.
- Budget the fee before upload day: payment clears through Submission Start, and a stalled department-card or VAT approval silently stalls consideration of the paper.

## Length and data policy

- **No explicit page or word limit** is stated in the Guide for Authors; the main text is divided into clearly numbered sections.
- **Data/code**: JAE follows Elsevier's **voluntary** research-data policy — it "encourages and enables" data sharing, data linking, a Data Statement, and the `[dataset]` citation tag, but does **not mandate** a replication archive (unlike JAR or JFE). Decide whether to share voluntarily.
- **Originality**: no simultaneous submission; Elsevier screens with Crossref Similarity Check (iThenticate). Editors may desk-reject or redirect unsuitable papers (Article Transfer Service).

## Checklist

- [ ] Editorial Manager account + ORCID linked
- [ ] Submission fee checked against the current JAE guide; VAT for EU authors
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
【System】Editorial Manager; current fee checked + VAT if EU
【Files】anonymized manuscript + title page; metadata scrubbed
【Packaging】Highlights ✓ keywords(≤6) ✓ JEL(≤6) ✓
【References】Elsevier author-date (Harvard) ✓
【Data policy】voluntary sharing decision: share / not
【Open items】... (verify live Guide for Authors)
【Next step】jae-review-process
```
