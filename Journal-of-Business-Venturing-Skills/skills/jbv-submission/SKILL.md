---
name: jbv-submission
description: Use when preparing to submit a Journal of Business Venturing (JBV) manuscript through Elsevier Editorial Manager — double-anonymized preparation, required declarations (competing interest, CRediT, generative-AI when used), flexible first-submission references, the Option C data availability statement, open-access/APC choice, and optional Data in Brief / MethodsX co-submission. Handles the submission preflight; it does not write the paper (jbv-writing-style) or manage the review (jbv-review-process).
---

# Submission Preflight (jbv-submission)

## When to trigger

- The manuscript is final and you are about to upload
- You need the Editorial Manager checklist for JBV
- You are unsure how to anonymize, what to declare, or whether to pay the APC
- You want to co-submit a data/methods artifact

## Where and how

- **Portal**: Elsevier **Editorial Manager** (editorialmanager.com/jbvi). Submission is fully online, with stepwise file upload from the ScienceDirect submission link.
- **First submission format**: provide editable source files; submit a separate title page and a fully anonymized manuscript for double-anonymized review. Strict reference formatting is not required at initial submission if every reference is complete and the style is consistent.
- **Current masthead**: ScienceDirect lists **Sophie Bacq** and **Simon Parker** as Co-Editors-in-Chief; manuscripts route through the current area-editor / handling-editor structure.

## Double-anonymized preparation (required)

Review is **double-anonymized**, so prepare an anonymized manuscript:

- Remove author names, affiliations, and acknowledgements from the manuscript file.
- Cite your own prior work in the third person; remove identifying funding/thanks.
- Keep author identifiers in the Editorial Manager metadata only, not in the file.

## Required declarations

- **Declaration of competing interest** (state "Declarations of interest: none" if applicable).
- **CRediT author-contribution statement** for corresponding authors.
- **Generative-AI disclosure** statement describing any AI use in preparation; no statement is needed for basic grammar, spelling, or reference tools.
- **Data availability statement**: JBV uses Elsevier's Option C research-data policy, so deposit/cite/link research data where possible or explain why data cannot be shared (e.g., proprietary VC data, confidential founder information). The statement is published with the article.

## Abstract & metadata

- Abstract concise and factual, **≤ 250 words**.
- **1 to 7 keywords** reflecting the entrepreneurial phenomenon and disciplinary lens.
- **Article highlights**: 3 to 5 bullet points, each no more than 85 characters including spaces.
- **Graphical abstract**: encouraged, submitted as a separate file if used.
- ORCID linked to the corresponding author's account.

## Fees / open access

- The subscription publication route lists **no publication fee charged to authors**.
- Optional open access carries an **APC of USD 4,280 (excluding taxes)**; the open-access choice **does not affect peer review or acceptance**.

## Co-submission (optional)

- On the "Attach files" page you can co-submit a **Data in Brief** descriptor or a **MethodsX** protocol article alongside the main manuscript — useful for novel hand-coded datasets or experimental protocols.

## Checklist

- [ ] Separate title page and anonymized manuscript prepared as editable source files
- [ ] Manuscript fully anonymized (no names/affiliations/acknowledgements; third-person self-cites)
- [ ] Competing-interest declaration included
- [ ] CRediT author-contribution statement included
- [ ] Generative-AI disclosure included if AI tools were used
- [ ] Option C data availability statement included
- [ ] Abstract ≤ 250 words; 1-7 keywords; highlights; ORCID linked
- [ ] Open-access/APC choice decided (USD 4,280 if OA; live-check current)
- [ ] Data in Brief / MethodsX co-submission decided

## Anti-patterns

- **Identifiers left in the file** (author names, "our prior work," thanks) breaking anonymity.
- **Missing competing-interest, CRediT, or required AI declaration.**
- **No Option C data availability statement.**
- **Abstract over 250 words.**
- **Missing article highlights.**

## Submission-stage failure modes and the fix

| Failure caught at upload                                  | The fix before resubmitting                                                         |
|-----------------------------------------------------------|-------------------------------------------------------------------------------------|
| Self-citations in first person ("in our earlier study").  | Convert to third person; check no in-press personal item de-anonymizes the list.    |
| Proprietary VC/founder data, no statement.                | Write a data availability statement explaining the restriction and what *can* be shared.|
| Generative-AI used but undisclosed.                       | Add the AI disclosure (tool and scope); separate from the competing-interest line.  |
| Abstract over 250 words, method-heavy.                    | Cut to ≤250 and lead with the entrepreneurial phenomenon and contribution.          |

## Worked micro-example: a one-pass preflight (illustrative)

A founder-team study of accelerator effects is ready to upload. The preflight catches, in order:

- Abstract is 268 words → trimmed to 240, reordered so the opportunity-team mechanism leads (illustrative).
- Self-citations read "we previously showed" → rewritten in third person; an in-press item cited as "Author, in press."
- Data are part Crunchbase (licensed), part hand-coded survey → statement notes the licensed portion cannot be redistributed; the coded instrument is available on request.
- Competing-interest line present, AI line missing → AI disclosure added ("language editing only," illustrative).
- References complete though not yet in journal style → acceptable at first submission; numbered style cleanup deferred to revision or proof.

## Calibration anchors (hedged)

- The declarations editors most often bounce a paper for are the **competing-interest declaration**, **CRediT statement**, **generative-AI disclosure when applicable**, and **data availability statement**.
- Flexible first-submission references do **not** relax anonymization, title-page separation, declarations, or highlights; treat those as hard gates.
- Fee figures, contacts, and portal URLs change; confirm against the journal's current author guidelines.

## Output format

```
【Portal】Editorial Manager (jbvi) ...
【Anonymization】clean? remaining identifiers ...
【Declarations】competing-interest / AI / data-statement present? ...
【Abstract/metadata】≤250 words; 1-7 keywords; highlights; ORCID ...
【OA/APC】subscription | OA (USD 4,280) ...
【Co-submission】Data in Brief / MethodsX? ...
【Next step】jbv-review-process
```
