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
