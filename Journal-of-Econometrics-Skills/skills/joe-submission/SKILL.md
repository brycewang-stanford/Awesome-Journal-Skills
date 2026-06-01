---
name: joe-submission
description: Use when running the final pre-submission preflight for the Journal of Econometrics (JoE) via Editorial Express — the USD $75 fee with proof-of-payment upload, PDF-only single-file format (~40 pages), 250-word abstract, single-anonymized review, and track selection. Final checks; it does not draft content.
---

# Submission Preflight (joe-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Express
- Unsure which files Editorial Express expects, or which track to pick
- Confirming format, abstract length, and fee/proof-of-payment requirements
- Checking declarations and the PDF is single-anonymized-ready

## Process facts (verified where noted; re-confirm on the official pages — several Elsevier pages 403)

- JoE is published by **Elsevier** (founded 1973); Co-Editors-in-Chief **Michael Jansson (UC Berkeley)** and **Aureo de Paula (UCL)**.
- Author submission is through the journal's **self-hosted Editorial Express portal** (database `je`) — **not** Elsevier's Editorial Manager. (The ScienceDirect guide references Editorial Manager, which appears to be residual boilerplate and/or the optional Data in Brief / MethodsX route — 待核实.)
- **Fee:** a **USD $75 nonrefundable submission fee** applies to new submissions and resubmissions over one year old; **proof of payment must be uploaded before the manuscript can be submitted**. VAT is added for European authors; no student discounts or refunds. (待核实: exact amount/wording surfaced via search snippets; the live Elsevier page 403'd.)
- **Format:** manuscripts must be uploaded in **PDF only**; the submission system instructs that the main text be **around 40 pages at ≥1.5 line spacing and 11pt font** (a norm, not a verified hard cap — 待核实). Six-step submission process.
- **Abstract:** **≤ 250 words**, concise and factual; cited references given in full (待核实).
- **Review:** **single-anonymized** — referees know authors; authors do not know referees (待核实).
- **Tracks:** choose **Regular**, **Annals**, or **Themed** Issue (see `joe-review-process`).

## Preflight checklist

### Format & style
- [ ] One **single PDF** with manuscript, theorems/proofs, tables, figures, and appendices embedded
- [ ] Main text ~**40 pages**, **≥1.5 spacing, 11pt** (norm — 待核实)
- [ ] **Abstract ≤ 250 words**; any cited references spelled out in full
- [ ] **elsarticle** LaTeX class / Elsevier reference style; dataset citations tagged **`[dataset]`**
- [ ] Tables/figures numbered, called out in order, with self-contained notes (DGP, $n$, reps)
- [ ] PDF compiles cleanly; math and figures legible at print resolution

### Fee & proof of payment
- [ ] **$75 fee paid** (VAT added for EU authors); **proof of payment file ready to upload** (待核实)
- [ ] Confirmed whether this is a new submission or a resubmission > 1 year (fee trigger)

### Single-anonymized readiness
- [ ] Manuscript may carry author identity (single-anonymized) — but confirm no confidential referee-only content is exposed (待核实 the current policy)
- [ ] Acknowledgments/funding handled per the guide

### Files for Editorial Express
- [ ] Main manuscript as a single **PDF**
- [ ] **Proof-of-payment** document
- [ ] Cover letter (problem, the methodological advance, fit; note the track and any Themed-Issue call)
- [ ] Suggested/excluded referees prepared (expert, fair, conflict-free)

### Declarations & content sanity
- [ ] Conflict-of-interest / funding disclosures prepared; paper not under review elsewhere
- [ ] Abstract states the contribution as a property (see `joe-writing-style`)
- [ ] Assumptions/asymptotics airtight (see `joe-identification-strategy`); Monte Carlo reports size + power (see `joe-data-analysis`)
- [ ] No over-claiming beyond what the theorems support

## Anti-patterns

- Forgetting the **$75 fee / proof-of-payment** upload — the paper cannot be submitted without it (待核实)
- Submitting via Editorial Manager when the journal's own route is **Editorial Express** (待核实)
- A >250-word abstract or a non-PDF upload
- Picking a Themed Issue track the paper does not fit

## Output format

```
【Single PDF】manuscript + proofs + exhibits embedded? [Y/N]
【Abstract】≤250 words, references in full? [Y/N]
【Fee】$75 paid + proof-of-payment ready? [Y/N] (待核实)
【Portal】Editorial Express (db je), correct track? [Regular/Annals/Themed]
【Files staged】PDF / proof-of-payment / cover letter / referees? [Y/N each]
【Declarations】COI / funding / not-under-review? [Y/N]
【Next step】await editor screen → joe-rebuttal on revision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — simulation/estimation tooling and the process/portal table
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JoE URLs behind every fact in this pack
