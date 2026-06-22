---
name: ectheory-submission
description: Use when running the final pre-submission preflight for Econometric Theory (ET) via ScholarOne / Manuscript Central — single embedded-font PDF, single-anonymous (no double-blind anonymization), APA author-date references, the 50-page ceiling, the optional cover letter, and the Supplementary Material file.
---

# Submission Preflight (ectheory-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on ScholarOne
- Unsure which files ET expects at submission and what goes in the Supplement
- Confirming the single-PDF format, APA author-date style, and ET prep specs are met
- Deciding Article vs Miscellanea and checking the length ceiling

## ET process facts (verified; re-confirm on the official page — 待核实 where noted)

- ET is published by **Cambridge University Press**, founded by **Peter C. B. Phillips** (Founding
  Editor 1985–2025); from **1 January 2026** edited by three joint Editors-in-Chief — **Patrik
  Guggenberger** (Penn State), **Liangjun Su** (Tsinghua), and **Yixiao Sun** (UC San Diego)
  (re-confirmed via the Cambridge Core editorial-board page 2026-06-22; re-verify before submission).
- Submission is via **ScholarOne / Manuscript Central** at `https://mc.manuscriptcentral.com/econ-theory`,
  effective **28 January 2026**, replacing the previous Editorial Express system.
- Manuscripts are submitted as a **single PDF** with all fonts, tables, and graphics embedded.
- **No submission fee or APC is stated** on the author-instructions pages (none mentioned; **待核实** —
  not a confirmed zero-fee policy). OA may be available via Cambridge read-and-publish agreements.
- **Single-anonymous** review — do **not** strip your identity as for a double-blind journal.
- **Cover letter required only** when you must convey review-relevant information (e.g., to share
  prior reviews from another journal); otherwise it is **optional**.
- Work must not be published or under review elsewhere.

## Preflight checklist

### Format & style
- [ ] One **single PDF** with manuscript, theorems/proofs, tables, figures, and appendices embedded; all fonts embedded
- [ ] References in **APA author-date**; reference list alphabetical by surname
- [ ] Abstract **<=200 words**; running head **<=40 characters**
- [ ] **11-point** min font, **>=1.5** line spacing, **>=1.25in** margins, pages numbered
- [ ] Title page: title, authors, affiliations, emails, footnotes as superscripts; p.2: running head, corresponding author, abstract
- [ ] Figures as TIFF/EPS/PDF, fonts embedded, legible at 50% reduction

### Length & article type
- [ ] Article type chosen: **Article** (<=50 pages incl. everything) or **Miscellanea** (<20pp, ~15)
- [ ] Regular Article within the **50-page ceiling**; overflow proofs/derivations moved to the Supplement
- [ ] Invited ET Interview NOT targeted (invited only)

### Single-anonymous (not double-blind)
- [ ] Manuscript shows author identity as normal — do NOT over-anonymize
- [ ] Self-citations in natural voice; contribution argued on merit

### Files for ScholarOne
- [ ] Main manuscript as a single embedded-font PDF
- [ ] Supplementary Material as a **separate clearly labeled file** (already-reviewed only; no new results)
- [ ] Cover letter only if conveying review-relevant info (otherwise optional)
- [ ] Confirmation the work is not under review/published elsewhere

### Final content sanity
- [ ] Main theorem stated early with its scope (see ectheory-contribution-framing)
- [ ] Assumptions complete and proofs gap-free (see ectheory-identification-strategy)
- [ ] Simulations probe the boundary cases (see ectheory-data-analysis)

## Anti-patterns

- Double-blind-style anonymization at a single-anonymous journal
- Padding the Article past 50 pages instead of using the online Supplement
- Numeric/Chicago references instead of APA author-date
- An over-200-word abstract or over-40-character running head
- A separate-figure-files upload when ET wants one embedded-font PDF
- Assuming a submission fee/APC exists (none stated; 待核实) and stalling on it

## Submission-blocker triage table

The fastest way to fail an ET submission is a format mismatch the editorial office catches before review —
each spec maps to its failure mode on this single-PDF, single-anonymous, APA-styled venue.

| Spec | If wrong | Fix before pressing submit |
| --- | --- | --- |
| File bundle | Separate figure files rejected | Merge into one embedded-font PDF (proofs, tables, figures) |
| Anonymization | Over-stripped identity | Restore identity — review is single-anonymous, not double-blind |
| Reference style | Numeric/Chicago bounced | Convert to APA author-date, alphabetized list |
| Length | Article over the page ceiling | Move overflow proofs to the labeled Supplement file |
| Abstract / running head | Over-length field | Trim abstract to ≤200 words, running head to ≤40 characters |

## Worked vignette and the office-pushback fixes

A nonstationary-estimator paper assembles into a single embedded-font PDF and gets under the page ceiling by
moving the auxiliary lemma's proof and extra tables into a labeled Supplement reusing the paper's numbering.
A cover letter is included only because prior reviews from another journal are shared; no APC question
stalls it, since none is stated (待核实). Submission goes through ScholarOne / Manuscript Central, in
effect since 28 January 2026 replacing Editorial Express. The fixes: incorrect anonymization → restore
identity, as ET is single-anonymous; over the ceiling → relocate overflow to the Supplement. Confirm the
ScholarOne URL and any fee policy against the live instructions.

## Output format

```
【Single PDF】all exhibits/proofs embedded, fonts embedded? [Y/N]
【Reference style】APA author-date, alphabetized? [Y/N]
【Specs】abstract<=200w / head<=40ch / 11pt / 1.5sp / 1.25in? [Y/N]
【Type & length】Article(<=50pp) or Miscellanea(~15pp); overflow → Supplement? [Y/N]
【Single-anonymous】identity visible (not over-anonymized)? [Y/N]
【Files staged】PDF / Supplement / cover letter (if needed)? [Y/N each]
【Next step】submit via ScholarOne → ectheory-rebuttal on a decision
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — LaTeX/theorem-proof tooling, asymptotic toolkit, Monte Carlo and reproducibility notes
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official ET URLs behind every fact in this pack
