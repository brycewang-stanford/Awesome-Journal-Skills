---
name: jpsp-submission
description: Use when running the final pre-submission preflight for the Journal of Personality and Social Psychology (JPSP) — section choice and correct Editorial Manager portal, masked-manuscript preparation, word/study caps, abstract, JARS, and TOP-Level-2 disclosures. Final checks; it does not draft content.
---

# Submission Preflight (jpsp-submission)

The last check before uploading to the **correct section's Editorial Manager portal**. The two most
common avoidable failures at JPSP are (1) submitting to the **wrong section** and (2) an
**under-masked** manuscript. Verify volatile per-section specifics on the live APA page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Confirming the section, its portal, and its caps
- Confirming the manuscript is properly masked and JARS/TOP disclosures are present

## Process facts (verify volatile items on the official page — 待核实)

- **Publisher:** American Psychological Association (APA).
- **Section + portal (pick one):** ASC → `editorialmanager.com/asc` · IRGP → `editorialmanager.com/irg`
  · PPID → `editorialmanager.com/pid`. Each section is edited independently.
- **Review model:** **masked review** for all submissions — mask the manuscript; provide a separate
  title page.
- **Abstract:** **≤ 250 words.** A limitations statement (≤ 200 words) may be required after the
  abstract (待核实).
- **Length / studies:** ASC intro + discussion **≤ 3,500 words**; IRGP intro + discussion **≤ 5,000
  words** and **≤ 5 studies** in the main text (extras → supplement); PPID "as succinctly as possible"
  (待核实). Tables/figures embedded; table content not counted toward the word limit.
- **Style:** **APA Publication Manual (7th edition)**; **JARS** required.
- **Transparency:** **TOP Level 2** — state data/code/materials repository + preregistration status.
- **Fee:** no submission fee stated (待核实; confirm any post-acceptance open-access APC).

## Preflight checklist

### Section & length
- [ ] Correct section chosen; uploading to that section's Editorial Manager portal
- [ ] Section word cap met (ASC ≤ 3,500 / IRGP ≤ 5,000 intro+discussion)
- [ ] Study count within the section cap (IRGP ≤ 5 in main text; extras in supplement)
- [ ] Abstract ≤ 250 words; limitations statement within cap if required (待核实)

### Masking (masked review)
- [ ] No author names, affiliations, or acknowledgments in the manuscript
- [ ] Self-citations neutralized; no "as we showed in…"
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Repository / OSF / preregistration links **masked** (no identifying URLs)
- [ ] Separate (non-masked) title page prepared as a distinct file

### Format, reporting & transparency
- [ ] APA 7th formatting; author–date citations; bias-free language
- [ ] Tables/figures **embedded** in the text; supplement has a table of contents
- [ ] JARS table for the design completed
- [ ] TOP Level 2 disclosures present (data/code/materials availability + preregistration status)

### Compliance & files
- [ ] Ethical treatment of human subjects stated; IRB as applicable
- [ ] Disclosure of any prior JPSP rejection (any section) and any published work using the same data
- [ ] File format per section (e.g., IRGP: .docx or .tex zip + PDF; ASC/PPID: .doc) — verify

## Anti-patterns

- Uploading to the wrong section's portal
- Author identifiers left in text, acknowledgments, file metadata, or a repository URL
- Abstract over 250 words; intro+discussion over the section cap
- More than the section's study cap in the main text
- Missing JARS or TOP Level 2 disclosures
- Budgeting for a submission fee that is not charged (verify)

## Avoidable desk-return triggers, ranked by frequency

The screen at JPSP catches the same failures repeatedly. This is illustrative ordering of risk, not an official list — confirm the current per-section requirements against the journal's submission guidelines (待核实).

| Trigger | Section editor's read | One-line fix |
|---------|------------------------|--------------|
| Wrong section's portal | Mis-fit before review begins | Route ASC→asc / IRGP→irg / PPID→pid deliberately |
| Author identity leaks | Masked review broken | Clean text, self-refs, file metadata, and repo URLs |
| Over the word cap | Long-format misread as no limit | Trim intro+discussion to the section cap; push detail to exhibits |
| Too many studies in main text | Study budget exceeded | Move extras to the supplement (IRGP ≤ 5 in main text) |
| Missing JARS / TOP L2 | Transparency floor unmet | Add the JARS table and data/code/materials + prereg statements |
| Single study | Not the multi-study standard | Reconsider fit before uploading (`jpsp-topic-selection`) |

A clean submission clears all six in one pass; any single miss can cost a review cycle.

## Output format

```
【Section + portal】ASC/IRGP/PPID → correct Editorial Manager URL? [Y/N]
【Caps met】intro+discussion words + study count within section limits? [Y/N]
【Abstract】word count (≤250) + limitations statement if required
【Masked】text + self-refs + metadata + repo links clean? [Y/N]
【APA 7th + JARS + TOP L2】all present? [Y/N]
【Files】per-section format + title page + supplement ToC? [Y/N]
【Next】await decision → jpsp-rebuttal on R&R / accept-with-revision
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — masking, JARS, repository, APA 7th tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — per-section portals, caps, masked-review, JARS/TOP policies
