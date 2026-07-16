---
name: jim-submission
description: Use when running the final preflight for a Journal of International Marketing (JIM) submission — the ScholarOne portal, the two-file anonymized package, formatting caps, and declarations. It clears the runway; post-decision strategy belongs to jim-rebuttal.
---

# Submission Preflight (jim-submission)

## When to trigger

- Submission is planned within days and the package needs a final audit
- Nobody is sure what ScholarOne will ask for or how the files must be split
- Anonymization, formatting caps, or declarations have not been verified against current rules
- An Insight paper or special-issue submission has extra constraints to confirm

> Facts below were checked **2026-07-16** against the AMA journal pages (ama.org) and the SAGE author instructions (journals.sagepub.com/author-instructions/jig). Limits, fees, and mastheads move — re-check the official pages the week you submit.

## Verified JIM specifications

- **Journal:** *Journal of International Marketing*, an American Marketing Association journal published by **SAGE**; quarterly; ISSN 1069-031X (print) / 1547-7215 (online); Editor-in-Chief **Ayşegül Özsomer** (Koç University), since 2024.
- **Portal:** ScholarOne at **mc.manuscriptcentral.com/ama_jim** (linked from the AMA JIM page). Online submission only.
- **Review model:** **double-anonymized.** The submission is split into at least two files: (1) a **title page** with authors, affiliations, contact details, acknowledgments, funding; (2) a **main document** with no identifying information anywhere — including the Web Appendix files.
- **Format:** 12-pt Times New Roman (or 12-pt LaTeX font), double-spaced text (tables/references may be single-spaced), 1-inch margins, **no page numbers, line numbers, headers, or footers** — ScholarOne stamps page/line numbers onto its PDF.
- **Length:** maximum **50 pages**, properly formatted, inclusive of title, abstract, keywords, text, footnotes, references, tables, figures, and print appendices.
- **Abstract:** **200 words**, unstructured, third person, placed between title and body.
- **Keywords:** minimum 3, specific to the topic; ScholarOne accepts up to 8 primary keywords.
- **Insight papers:** short manuscripts **under 4,000 words including all components**, designed for expedited review — confirm current scope on the AMA guidelines page.
- **Fees / OA:** no submission fee reported on the official pages; open-access options and any APC follow SAGE's current terms — re-check on the official site rather than assuming.

## Anonymization audit

- [ ] Main document and Web Appendix free of names, affiliations, acknowledgments, grant numbers
- [ ] Self-citations neutralized ("prior research shows (Author 2021)") — no "our earlier study"
- [ ] File metadata scrubbed (PDF/DOCX author properties, tracked-changes identities)
- [ ] Data/preregistration links routed through anonymized views (no personal OSF handles)
- [ ] Country-partner details that identify the team (a named university's panel in one country) generalized

## Package assembly

- [ ] Title page file: full author block, ORCIDs, correspondence, acknowledgments, funding, ethics/IRB note
- [ ] Main document: title, 200-word abstract, keywords, body, references, exhibits — inside 50 pages
- [ ] Web Appendix file(s): translations/items, extra analyses; anonymized; cited in text
- [ ] Cover letter: the JIM fit claim (international dimension as theoretical core), the sibling-boundary sentence, confirmation of no concurrent submission, special-issue name if applicable
- [ ] Keyword set chosen to route to the right associate editor (e.g., "export performance," "measurement invariance," "global branding")
- [ ] Declarations ready: conflicts of interest, funding, human-subjects approval, AI-use disclosure per current AMA/SAGE policy

## Portal walk-through notes

Create/verify the ScholarOne account with ORCID linked before submission day; the form asks for manuscript type (regular vs. Insight vs. special issue), keywords, and suggested/opposed reviewers. Paste the abstract as plain text and check that symbols survived. Build the proof PDF and read it once fully — exhibit rendering, no orphaned identity strings, reference list intact. Only then approve. Save the manuscript ID; `jim-review-process` tracks it from here.

## Anti-patterns

- One merged file with the author block on page 1 — instant administrative bounce
- "Fitting" 52 pages by shrinking margins or line spacing; the format spec is checked
- An abstract of 240 words because "it's close enough"
- Identity leakage through the Web Appendix, file properties, or a personal repository link
- A cover letter that summarizes the paper but never argues JIM fit
- Submitting the medical-AMA numeric reference style unconverted
- Trusting these specs next year without re-checking the official pages

## Output format

```text
【Files】title page / main doc / web appendix / cover letter: ready?
【Anonymization】text + metadata + links audit: pass/fix
【Caps】pages __ / 50; abstract __ / 200; keywords __ (3–8)
【Format】12-pt TNR, double-spaced, 1-inch margins, no page numbers: pass/fix
【Type】regular / Insight (<4,000 words) / special issue: [which]
【Declarations】COI / funding / ethics / AI use: complete?
【Fact status】portal + limits re-checked on ama.org & SAGE (date)
【Next step】submit at mc.manuscriptcentral.com/ama_jim → jim-review-process
```

## Templates

- [`templates/checklist.md`](templates/checklist.md) — printable preflight list
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JIM-shaped skeleton
