---
name: revedres-submission
description: Use when running the final pre-submission preflight for a Review of Educational Research (RER) manuscript via Manuscript Central — masking, APA 7, the 150-word abstract, file set, and reporting-standard attachments. Checks readiness to submit; it does not negotiate scope (revedres-editor-strategy) or handle the decision letter (revedres-revision).
---

# Submission Preflight (revedres-submission)

## When to trigger

- The review is complete and you are about to upload to Manuscript Central
- You need a last pass on masking, APA 7, the abstract limit, and the file set
- You are unsure which files RER expects (blinded vs. unblinded title page, bios)
- You want to confirm reporting-standard attachments before the portal flags an incomplete submission

## RER intake at a glance (检索于 2026-06；以官网为准)

| Item | What RER expects |
|------|------------------|
| Portal | **Manuscript Central / ScholarOne**: `mc.manuscriptcentral.com/rer` |
| Artefact | A **comprehensive, critical, integrative review of literature related to education** — RER **does not publish original empirical research** unless it is incorporated in a broader integrative review. **Interdisciplinary** submissions (psychology, sociology, history, economics) are welcome **provided they address educational issues**. RER also occasionally runs **solicited but refereed** analytic reviews of special topics |
| Review process | **Masked (anonymized) review** — manuscript anonymized so reviewers do not see author identity |
| Style | **APA 7th edition** throughout |
| Abstract | **≤ 150 words**, with keywords (separately and on page 2 after the blinded title page) |
| File format | **Microsoft Word** (not PDF) — the system converts it |
| Files | (a) separate **unblinded title page** with APA-7 Author Note; (b) **main manuscript** with a **BLINDED title page**, abstract + keywords, and the body incl. tables/figures; (c) **Author Bios** |
| Masking | Manuscript anonymized for masked review; anonymize **only limited-circulation** self-citations (forthcoming/in press/unpublished), not ordinary published self-cites |
| Reporting standards | Systematic reviews/meta-analyses: consult **PRISMA** and the APA **Reporting Standards for Research in Psychology** (MARS/JARS); authors should also consult RER's **Guidelines for Reviewers** |
| Publication | RER is an **AERA** journal published by **SAGE**, **established 1931**, issued **bimonthly (six issues/year)**; DOI stem `10.3102/` |
| Volatile | **Fee/APC** (none stated in the captured guidance — do not assert one), **exact length/word maximum**, current **editors/contact**, and **decision timelines / reviewer counts** — **re-confirm on the SAGE/AERA RER pages** (待核实) |

## Preflight (work top to bottom)

1. **Venue fit.** It is a comprehensive, critical, integrative review (systematic / meta-analytic / critical-integrative) of literature bearing on education — **not** original empirical research (unless folded into a broader integrative review), else route per `revedres-editor-strategy`. Interdisciplinary angles are fine if they address educational issues. Review is **masked/anonymized**, so masking must hold.
2. **Masking is correct.** Body de-identified; blinded title page in the main file; **only** limited-circulation self-citations anonymized; a separate unblinded title page + Author Note + Author Bios prepared.
3. **APA 7 conformance.** Citations, references, headings, tables, figures, and bias-free language all APA 7th.
4. **Abstract ≤ 150 words**, review-style, with keywords, in both required locations.
5. **Exhibits attached and reconciling.** PRISMA flow (counts reconcile), study table with risk-of-bias, forest/funnel for meta-analyses — embedded in the Word file.
6. **Reporting-standard checklists** completed (PRISMA, MARS) and registration (PROSPERO/OSF) cited; open-materials links ready; **Guidelines for Reviewers** consulted.
7. **File set + format.** Word (not PDF); the three-file set (unblinded title page / blinded main manuscript / Author Bios) assembled.
8. **Volatile re-confirms.** Fee, length, current editors/contact, and any policy specifics checked on the official RER pages today.

See `templates/checklist.md` for the full last-pass list.

## Checklist

- [ ] Artefact is a review, not original empirical research
- [ ] Body masked; blinded title page in main file; only limited-circulation self-cites anonymized
- [ ] Separate unblinded title page + APA-7 Author Note + Author Bios prepared
- [ ] APA 7 throughout (citations, references, headings, bias-free language)
- [ ] Abstract ≤ 150 words, review-style, with keywords, in both locations
- [ ] PRISMA flow / study table / forest / funnel embedded and reconciling
- [ ] PRISMA + MARS checklists done; PROSPERO/OSF registration cited; open materials ready
- [ ] Files in **Word** (not PDF); three-file set assembled for Manuscript Central
- [ ] Volatile facts (fee, length, editors/contact) re-confirmed on the RER pages today

## Anti-patterns

- Uploading a **PDF** when RER asks for Word
- Leaving author names in the body or blinding ordinary *published* self-citations (over-anonymizing)
- A 200+-word abstract, or one written like a single-study report
- Missing the unblinded title page or Author Bios → an **incomplete** submission
- No PRISMA/MARS checklist attached for a systematic review/meta-analysis
- Asserting fee/length/editor facts from memory instead of re-checking the official pages

## Output format

```
【Venue fit】review (not original empirical)? Y/N
【Masking】body blinded; blinded title page in main file; only ltd-circ self-cites anonymized? Y/N
【File set】unblinded title page + blinded manuscript + Author Bios, all Word? Y/N
【APA 7】citations/refs/headings/bias-free language conform? Y/N
【Abstract】≤150 words, review-style, keywords, both locations? Y/N
【Exhibits】PRISMA + study table + forest/funnel embedded and reconciling? Y/N
【Reporting standards】PRISMA + MARS done; PROSPERO/OSF cited; open materials ready? Y/N
【Volatile re-confirmed】fee / length / editors / portal checked today? Y/N
【Next step】→ revedres-revision (after the decision letter)
```
