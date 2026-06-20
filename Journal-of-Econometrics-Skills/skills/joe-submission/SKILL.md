---
name: joe-submission
description: Use when running the final pre-submission preflight for the Journal of Econometrics (JoE) — live portal routing, the USD $75 fee, ScienceDirect source-file rules, Editorial Express resubmission norms, 250-word abstract, single-anonymized review, and track selection. Final checks; it does not draft content.
---

# Submission Preflight (joe-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit through the live official portal
- Unsure whether the current route is Editorial Manager or Editorial Express, or which track to pick
- Confirming format, abstract length, and fee/proof-of-payment requirements
- Checking declarations and the PDF is single-anonymized-ready

## Process facts (verified on 2026-06-20; re-confirm volatile portal routing on the official pages)

- JoE is published by **Elsevier** (founded 1973); Co-Editors-in-Chief **Michael Jansson (UC Berkeley)** and **Aureo de Paula (UCL)**.
- **Portal:** ScienceDirect's current **Submit your article** link points new submissions to **Editorial Manager**. JoE's own Google Sites Guidelines still says all submissions are made through **Editorial Express**, and the Editorial Express `dbase=je` page now says it is for **resubmissions only** and links new submissions to Editorial Manager. Start from the live ScienceDirect/JoE official link; use Editorial Express when the live route or resubmission flow directs you there.
- **Fee:** a **USD $75 nonrefundable submission fee** applies to new submissions and resubmissions over one year old. VAT is added for European authors; no student discounts or refunds.
- **Files/format:** the ScienceDirect Guide asks for editable source files (`.doc/.docx` or `.tex`) and says PDF is not an acceptable source file for that requirement. The Editorial Express resubmission flow instructs a **PDF-only** upload, with main text around **40 pages** at **≥1.5 spacing and 11pt font**.
- **Abstract:** **≤ 250 words**, concise and factual; avoid references unless essential, and cite author/year if included.
- **Review:** **single-anonymized** — referees know authors; authors do not know referees.
- **Tracks:** choose **Regular**, **Annals**, or **Themed** Issue (see `joe-review-process`).

## Preflight checklist

### Format & style
- [ ] Editable source files staged (`.doc/.docx` or `.tex`) for the ScienceDirect/Editorial Manager route
- [ ] If using the Editorial Express resubmission flow: one **single PDF** with manuscript, theorems/proofs, tables, figures, and appendices embedded
- [ ] Main text ~**40 pages**, **≥1.5 spacing, 11pt** when the Editorial Express resubmission form applies
- [ ] **Abstract ≤ 250 words**; any cited references spelled out in full
- [ ] **elsarticle** LaTeX class / Elsevier reference style; dataset citations tagged **`[dataset]`**
- [ ] Tables/figures numbered, called out in order, with self-contained notes (DGP, $n$, reps)
- [ ] PDF compiles cleanly; math and figures legible at print resolution

### Fee & proof of payment
- [ ] **$75 fee paid** if required (VAT added for EU authors); **proof of payment file ready** if the live route requests it
- [ ] Confirmed whether this is a new submission or a resubmission > 1 year (fee trigger)

### Single-anonymized readiness
- [ ] Manuscript may carry author identity (single-anonymized) — but confirm no confidential referee-only content is exposed
- [ ] Acknowledgments/funding handled per the guide

### Files for the live portal
- [ ] Main manuscript source files (`.doc/.docx` or `.tex`) and any portal-requested PDF
- [ ] **Proof-of-payment** document if requested by the live route
- [ ] Cover letter (problem, the methodological advance, fit; note the track and any Themed-Issue call)
- [ ] Suggested/excluded referees prepared (expert, fair, conflict-free)

### Declarations & content sanity
- [ ] Conflict-of-interest / funding disclosures prepared; paper not under review elsewhere
- [ ] Abstract states the contribution as a property (see `joe-writing-style`)
- [ ] Assumptions/asymptotics airtight (see `joe-identification-strategy`); Monte Carlo reports size + power (see `joe-data-analysis`)
- [ ] No over-claiming beyond what the theorems support

## Anti-patterns

- Forgetting the **$75 fee / proof-of-payment** step when the live portal requires it
- Assuming the old Editorial Express-only route still governs new submissions without checking the current official link
- A >250-word abstract or a non-PDF upload
- Picking a Themed Issue track the paper does not fit

## Output format

```
【Single PDF】manuscript + proofs + exhibits embedded? [Y/N]
【Abstract】≤250 words, references in full? [Y/N]
【Fee】$75 paid if required + proof-of-payment ready if requested? [Y/N]
【Portal】live official route checked: Editorial Manager new submission or Editorial Express resubmission? [route]
【Files staged】source files / PDF if requested / proof-of-payment if requested / cover letter / referees? [Y/N each]
【Declarations】COI / funding / not-under-review? [Y/N]
【Next step】await editor screen → joe-rebuttal on revision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — simulation/estimation tooling and the process/portal table
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JoE URLs behind every fact in this pack
