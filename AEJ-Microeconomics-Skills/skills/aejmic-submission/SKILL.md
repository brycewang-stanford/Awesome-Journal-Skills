---
name: aejmic-submission
description: Use when running the final pre-submission preflight for the American Economic Journal: Microeconomics (AEJ: Micro) via the AEA submission system — single-blind review, the 100-word abstract, JEL classification, the submission fee, format, and the AEA Data and Code Availability Policy. Final checks; it does not draft content.
---

# Submission Preflight (aejmic-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA system
- Unsure which files, codes, and fees the AEA submission expects
- Confirming the abstract, format, and data/code requirements are met
- Verifying the data/code availability requirements before submission

## Process facts (检索于 2026-06；editor + fees re-verified 2026-06-22；以官网为准)

- AEJ: Micro is one of the AEA's four field journals (founded 2009 — 待核实, quarterly); submission is through the **AEA submission/editorial system**. Editor (re-verified 2026-06-22): **Navin Kartik** (Yale, since Fall 2025); coeditors Ali, Bonatti, Rozen, Xu — re-verify the masthead before submission.
- **Single-blind review:** the author's name is revealed to referees, while referees remain anonymous to authors. There is **no anonymization requirement** — but state author info, acknowledgments, and funding professionally.
- **Abstract:** **100 words or fewer** (required). JEL classification per AEA practice; keywords expected.
- **Submission fee:** AEA members **$200** (high-income) / **$100** (middle-income) / **$0** (low-income); nonmembers **$300 / $200 / $0**; scaled by membership and country income classification. Papers rejected without review are refunded **50%**. (Amounts **volatile** — confirm on the AEA submissions page.)
- **Publication fee:** **$15 per typeset page** assessed at page proofs (papers submitted after Feb 1, 2024) — distinct from the submission fee.
- **Data & code:** the **AEA Data and Code Availability Policy** (administered by the **AEA Data Editor**, Lars Vilhuber) applies to papers with **empirical work, simulations, or experimental work**; deposit to the **AEA Data and Code Repository (openICPSR)**; verified before acceptance. Pure-theory papers still deposit numerical/simulation code.
- **House style:** AEA style; proofs in appendix where long; numerical examples to illustrate; report **standard errors (not asterisks)** for empirical/experimental work.
- **What to expect after submit:** a co-editor screens for fit and may **desk-reject** without referees; otherwise expert referees verify the proofs. Choose JEL codes that route the paper to a co-editor in the right subfield (see `aejmic-referee-strategy`).

## Preflight checklist

### Front matter & format
- [ ] **Abstract ≤100 words** (hard limit)
- [ ] **JEL codes** and keywords present
- [ ] Numbered propositions/theorems; proofs self-contained (main text or appendix)
- [ ] Figures/tables legible; **no significance asterisks** for inference — report SEs / coverage sets
- [ ] AEA/LaTeX formatting per the current author guidelines
- [ ] Author info, acknowledgments, and funding stated professionally (single-blind: no anonymization)

### Files, fees & data
- [ ] Manuscript PDF + any separate files the system requires
- [ ] Submission fee ready (member $200/$100/$0 by income; nonmember higher) — confirm current amount
- [ ] Aware of the $15/typeset-page publication fee at proofs (not now)
- [ ] Data/code deposit prepared if the paper has empirical/simulation/experimental work; theory-only numerics code prepared too
- [ ] Experiment materials (instructions, code, pre-registration) ready

### Declarations
- [ ] Disclosure statement per AEA policy (financial interests, funding)
- [ ] Confirmed not under review elsewhere; AI not listed as an author
- [ ] Verified the venue (AEJ: Micro, not AEJ: Applied or a specialist theory journal)

## Anti-patterns

- Abstract over 100 words, or missing JEL codes
- Significance asterisks, or a load-bearing proof exiled to supplementary files
- Treating the data/code deposit as a post-acceptance afterthought (the Data Editor checks before acceptance)
- Confusing the submission fee with the later $15/page publication charge
- Assuming single-blind anonymity is required — it is not; rigor, not anonymity, carries the paper

## Output format

```
【Front matter】abstract ≤100 words + JEL + keywords? [Y/N]
【Format/style】numbered results; proofs self-contained; no asterisks? [Y/N]
【Fee】AEA submission fee ready (amount confirmed)? [Y/N]
【Data/code】deposit prepared (incl. theory-only numerics)? [Y/N]
【Declarations】disclosure; not under review; AI not an author? [Y/N]
【Next step】submit via AEA system → aejmic-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA/AEJ: Micro URLs behind every fact
