---
name: eer-submission
description: Use when running the final pre-submission preflight for the European Economic Review (EER) via Editorial Manager — submission fee, single-anonymized review, Elsevier format and house-style rules, declarations, and the data/replication policy. Final checks; it does not draft content.
---

# Submission Preflight (eer-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Unsure which files, fees, and declarations EER expects
- Confirming Elsevier format + EER house style are met
- Verifying the data/code availability statement and replication readiness

## Process facts (检索于 2026-06；以官网为准)

- EER is **Elsevier's** general-interest European economics journal (founded 1969), hosted on **ScienceDirect** (ISSN 0014-2921). Submission is via **Editorial Manager** at `https://www.editorialmanager.com/eerev`.
- **Editors-in-Chief (verified 2026-06-22):** Evi Pappa (Universidad Carlos III de Madrid), David K. Levine (Royal Holloway), Stefania Garetto (Boston University), Peter Rupert (UC Santa Barbara), and Robert Sauer (Royal Holloway). EER uses a multi-editor masthead; re-verify the current editor on the ScienceDirect editorial-board page before naming one in a cover letter.
- **Review model:** **single-anonymized** (single-blind) — referees see author identities; editors desk-screen for scope/novelty before sending to **≥2 referees**. First decision is typically fast.
- **Submission fee (verified 2026-06-22):** **non-refundable EUR 125** for new submissions (**EUR 100** if the contact author is a PhD student; **EUR 50** if from a Research4Life **Group B** country); **Research4Life Group A** countries eligible for a **full waiver via a voucher** requested before submission. Submissions are considered only after the fee is paid. Re-verify current amounts and waiver routes before filing.
- **Mandatory replication policy:** accepted papers with empirical/simulation/experimental content must provide data, programs, and computational details **before publication** (see `eer-replication-package`).
- **Open access:** optional Gold OA with an APC (**USD 3,760** excl. tax, verified 2026-06-22); the subscription route has **no APC**. Re-confirm the current APC on the journal page before quoting it.
- **Appeals:** one formal appeal per submission, per Elsevier's appeal policy; the appeal decision is final.

## Preflight checklist

### Format & house style (Elsevier economics)
- [ ] Manuscript in an **editable format** (LaTeX or Word) — editable source is required to typeset the final article
- [ ] **Abstract**, **JEL codes**, and **keywords** present (re-confirm any abstract word limit — 检索于 2026-06)
- [ ] **Research highlights** included (a few concise bullet findings)
- [ ] Figures/tables legible for review; **editable/vector source** ready for final files
- [ ] **Standard errors reported**; significance stars do not replace SEs/magnitudes
- [ ] References complete and consistent (Elsevier reference style; re-confirm exact style — 检索于 2026-06)
- [ ] Re-confirm any length/word guidance on the guide for authors (no single fixed cap verified — 待核实)

### Files & fees (Editorial Manager)
- [ ] Main manuscript (editable) + figures/tables + any supplementary appendix
- [ ] Submission fee ready (EUR 125 / EUR 100 PhD / EUR 50 R4L Group B), or **Research4Life Group A voucher obtained in advance**
- [ ] Cover letter (scope/contribution; suggested/excluded referees if invited)

### Declarations & policy
- [ ] **Declaration of interest** statement (Elsevier requirement) + funding sources
- [ ] **Data and code availability statement** consistent with the replication package
- [ ] Confirmed not under review elsewhere; **AI not listed as an author**; authorship/CRediT roles set
- [ ] Experimental papers: instructions/transcripts included; pre-registration noted where applicable

## Anti-patterns

- Submitting an out-of-scope/low-novelty paper and losing the **non-refundable fee** to a desk reject
- Forgetting the **Research4Life voucher must be requested before** submitting
- Uploading a non-editable PDF-only manuscript with no editable source
- Significance stars instead of SEs; missing research highlights or declaration of interest
- Treating the optional OA APC as a mandatory submission-time charge
- A data-availability statement that overclaims what is actually deposited
- Suggesting referees who are obvious conflicts, or omitting a needed exclusion list
- Submitting with declaration-of-interest or funding statements left blank

## Output format

```
【Format】editable source + abstract/JEL/keywords/highlights present? [Y/N]
【Exhibits】SEs reported, stars not load-bearing, editable figures? [Y/N]
【Fee】EUR 125 / EUR 100 PhD / EUR 50 R4L Group B ready, or Group A voucher obtained? [Y/N]
【Declarations】declaration of interest + data-availability + no-AI-author? [Y/N]
【Replication】deposit ready per mandatory policy? [Y/N]
【Next step】submit via Editorial Manager → eer-rebuttal after the decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Elsevier/ScienceDirect URLs behind every fact
