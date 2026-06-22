---
name: bjps-submission
description: Use when running the final pre-submission preflight for the British Journal of Political Science (BJPS) — format selection, double-blind anonymization, word/abstract caps, Cambridge (Harvard author-date) house style, ORCID, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (bjps-submission)

The last check before pressing submit. BJPS is **double-blind**, so the single most common avoidable
failure is an under-anonymized manuscript. Verify volatile specifics on the official Cambridge/BJPS
page before relying on them.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata the portal expects
- Confirming the chosen format's caps are met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** **Cambridge University Press** (BJPS / BJPolS). Associated with the British
  Academy; awards the Brian Barry Prize.
- **Portal:** the journal's online submission system (Editorial Manager, `editorialmanager.com/bjpols`;
  the seed flagged ScholarOne vs Editorial Manager — 检索于 2026-06；以官网为准).
- **Review model:** **double-blind** — anonymize the manuscript; provide a separate title page.
- **Formats:** **Research Articles** (~10,000 words), **Letters** (short articles, ~4,000 words),
  **Comments**. (Word caps 待核实 — confirm current figures and what they include.)
- **Abstract:** **≤ 150 words** (required for all article types).
- **Style:** **Cambridge house style** — **Harvard author-date** citations and reference list.
- **Manuscript prep:** double spacing, ≥ 12-point type, margins per the style guide; accepted in
  **MS Word or LaTeX**.
- **ORCID:** encouraged/required per Cambridge policy (待核实 current requirement).
- **Fee:** no submission fee. BJPS is now **wholly Gold Open Access** (verified 2026-06-22): accepted
  Articles and Letters are published Gold OA with Cambridge's standard 2026 APC of **£2,610 / US $3,655**
  (plus tax), commonly covered by institutional read-and-publish agreements, the Cambridge Open Equity
  Initiative, or a waiver. Re-verify the current APC and waiver routes before submission.

## Preflight checklist

### Format & length
- [ ] Format chosen and its word cap met (Article ~10,000 / Letter ~4,000; 待核实)
- [ ] Abstract ≤ 150 words, states question + approach + finding

### Anonymity (double-blind)
- [ ] No author names, affiliations, acknowledgments, or **funding notes** in the manuscript
- [ ] No links to personal/university websites; no obvious self-references ("as we showed in…")
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Anonymized pre-analysis plan / OSF link if preregistration is referenced
- [ ] Separate (non-anonymous) title page prepared as a distinct file

### Format & metadata
- [ ] Cambridge **Harvard author-date** formatting; consistent reference list
- [ ] MS Word or LaTeX file; double-spaced, ≥ 12-point, correct margins
- [ ] Corresponding-author **ORCID** ready (待核实)
- [ ] Figures/tables self-contained, sized to Cambridge's box at ≥ 300 dpi (see `bjps-tables-figures`)

### Compliance & files
- [ ] Ethics / consent / human-subjects compliance addressed
- [ ] Original work; preprint status checked against Cambridge preprint policy
- [ ] Replication data + code staged for the **BJPolS Dataverse** at acceptance
      (see `bjps-transparency-and-data`)

## Anti-patterns

- Leaving author identifiers, funding notes, or website links that break anonymity
- Abstract over 150 words
- Sending a long paper to the Letter format (or vice versa)
- Using a non-Harvard citation style or mixing styles
- Budgeting for a submission fee that is not charged (none as of 2026-06-22); note BJPS is now wholly Gold OA, so accepted Articles/Letters carry an APC unless covered by an agreement or waiver

## Output format

```
【Format】Research Article / Letter / Comment (caps met? Y/N)
【Anonymized】text + self-refs + funding + file metadata clean? [Y/N]
【Abstract】word count (≤150)
【Harvard author-date + MS Word/LaTeX + ORCID】[Y/N]
【Repro package】staged for BJPolS Dataverse? [Y/N]
【Next】await decision → bjps-rebuttal on R&R
```

## Supplementary resources

- [`./templates/checklist.md`](./templates/checklist.md) — copy-paste submission preflight checklist
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official BJPS URLs behind every fact in this pack
