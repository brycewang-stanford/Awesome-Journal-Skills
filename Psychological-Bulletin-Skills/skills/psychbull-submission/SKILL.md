---
name: psychbull-submission
description: Use when running the final pre-submission preflight for Psychological Bulletin via APA Editorial Manager — masking, the ≤ 250-word abstract, APA 7th style, MARS/PRISMA/JARS checklists, and the transparency package. Final checks; it does not draft content.
---

# Submission Preflight (psychbull-submission)

The last check before pressing submit on **APA Editorial Manager**. Psychological Bulletin uses
**masked review**, so the most common avoidable failure is an under-masked manuscript — and the second
is a synthesis whose MARS/PRISMA reporting is incomplete. Verify volatile specifics on the official APA
page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Manager expects
- Confirming masking, the abstract cap, and the MARS/PRISMA checklist are satisfied

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** American Psychological Association (APA).
- **Portal:** APA **Editorial Manager** (`editorialmanager.com/bul`).
- **Review model:** **masked** — author identity withheld from reviewers; no author clues in the file.
- **What it publishes:** research **syntheses** (systematic reviews, meta-analyses, meta-reviews,
  meta-synthesis, qualitative reviews) — **not** original primary studies; original theory →
  *Psychological Review*.
- **Abstract:** **≤ 250 words**, on a separate page.
- **Style:** APA Publication Manual, **7th edition**.
- **Reporting:** **MARS** (meta-analysis) · **PRISMA** (systematic review) · **JARS** (quant/mixed).
- **Transparency:** state preregistration + where; supply **database, codebook, scripts** (TOP, since
  Feb 1 2022 — 待核实 exact level).
- **Fee:** no submission fee stated (待核实; confirm any post-acceptance OA APC).

## Preflight checklist

### Fit & type
- [ ] It is a **synthesis**, not an original study or pure theory (else wrong journal)
- [ ] Synthesis type declared (meta-analysis / systematic / meta-review / qualitative)

### Masking
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] Self-references neutralized; easily identified self-citations removed from the reference list
- [ ] **File metadata stripped** (document properties)
- [ ] PROSPERO/OSF appendix anonymized (no registration number or author names)

### Reporting & format
- [ ] Abstract ≤ 250 words on a separate page
- [ ] APA 7th-edition formatting throughout
- [ ] **MARS / PRISMA / JARS** checklist completed for the synthesis type
- [ ] PRISMA flow diagram + forest/funnel exhibits present (see `psychbull-tables-figures`)

### Transparency & compliance
- [ ] Preregistration stated with access location
- [ ] Database + codebook + scripts deposited with a DOI; availability statement drafted
- [ ] Ethics/attribution compliant; original synthesis (no plagiarized text)

## Anti-patterns

- Author identifiers left in text, acknowledgments, or file metadata (breaks masking)
- A PROSPERO number visible in the masked appendix
- Abstract over 250 words
- Submitting an original empirical study or pure theory to the wrong venue
- Missing MARS/PRISMA checklist or an undeposited database

## Desk-reject patterns at the APA review flagship

Most avoidable failures at Psychological Bulletin are caught before peer review — at the editor's desk.
The recurring desk-reject patterns at the APA's flagship synthesis journal:

| Desk-reject pattern | Why it triggers | Pre-submission fix |
|---------------------|-----------------|--------------------|
| Wrong venue | A primary empirical study or pure theory was submitted | Confirm it is a synthesis; route theory to *Psychological Review* |
| Broken masking | Author names, affiliations, or file metadata remain | Strip identifiers from text and document properties |
| Visible registration | PROSPERO number/names left in the masked appendix | Anonymize the appendix before upload |
| Over-long abstract | Abstract exceeds 250 words | Trim to the cap on a separate page |
| Missing reporting | No MARS/PRISMA/JARS checklist or PRISMA diagram | Complete the checklist for the synthesis type |
| No deposited data | "Available on request" instead of a DOI'd package | Deposit database, codebook, scripts before submitting |

## Worked vignette — the final preflight pass

*Illustrative figures only.* The self-affirmation synthesis (k = 42, g = 0.34) clears preflight when:

- **Fit** is confirmed as a meta-analysis of existing trials, not new data.
- **Masking** is verified in the text, the neutralized self-citations, the stripped file metadata, and
  the anonymized OSF/PROSPERO appendix.
- **Abstract** is 218 words on its own page, stating k, the pooled g and CI, the moderator, and the
  robustness bottom line.
- **Reporting**: the MARS and PRISMA checklists are complete and the PRISMA diagram plus forest/funnel
  exhibits are attached.
- **Transparency**: the deposited database, codebook, and scripts carry a DOI and the availability
  statement is drafted. (Confirm the current TOP level and any APC on the official APA page.)

## Referee/editor pushback → venue-specific fix

- *"This appears to be a primary study."* → Reframe only if it genuinely synthesizes a literature;
  otherwise it is the wrong journal.
- *"Reviewer could infer the authors."* → Remove residual self-references and metadata; re-anonymize the
  registration appendix.
- *"MARS checklist is missing."* → Attach the completed checklist matched to the synthesis type before
  resubmitting.

## Output format

```
【Fit】synthesis, not primary study/theory? [Y/N]
【Type】meta-analysis / systematic / meta-review / qualitative
【Masked】text + self-refs + metadata + PROSPERO appendix clean? [Y/N]
【Abstract】word count (≤ 250)
【MARS/PRISMA/JARS】checklist complete? [Y/N]
【Transparency】database+codebook+scripts deposited + prereg stated? [Y/N]
【Next】await decision → psychbull-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, masking, repository/deposit tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Editorial Manager, masked review, abstract, MARS/PRISMA/JARS, TOP
