---
name: geb-submission
description: Use when running the final pre-submission preflight for Games and Economic Behavior (GEB) via Elsevier Editorial Manager — Word/LaTeX (elsarticle) source, 250-word abstract, the mandatory conference-version disclosure in the cover letter, and the generative-AI declaration. Final checks; it does not draft content.
---

# Submission Preflight (geb-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Unsure what Editorial Manager expects, or how to handle a prior conference version
- Confirming the 250-word abstract, elsarticle format, and AI declaration are GEB-compliant
- Preparing the cover letter

## Process facts (verify volatile items on the official Guide for Authors; some are 待核实)

- GEB is published by **Elsevier** and is an **official journal of the Game Theory Society**; founded 1989 by Ehud Kalai; Editor-in-Chief **Hervé Moulin** (University of Glasgow) since 2021 — re-confirmed current 2026-06-22 via ScienceDirect, the Game Theory Society page, and the Elsevier editorial-board listing (re-verify the full masthead before submission, as the seven-Editor roster is volatile).
- Submission is via **Elsevier Editorial Manager** (linked from ScienceDirect). **Editable source files (Word or LaTeX) are required for final typesetting**; LaTeX uses the **elsarticle** template; the published citation style is **elsarticle-num**. At initial submission, format is flexible (any consistent style; LaTeX or Word both accepted) — strict formatting is deferred until acceptance.
- **No upfront submission fee** is identified (待核实 — inferred from standard Elsevier practice, not an official quote). Optional **gold open access** carries an **Article Publishing Charge last verified at USD 2,860 excluding tax** (ScienceDirect GEB listing, 2026-06-22; a 2026-06-23 independent re-audit could not re-confirm the exact figure from a second authoritative source because Elsevier now serves APCs through its personalized submission flow rather than a static public number), only for accepted papers whose authors choose OA — confirm the live amount in the submission system before relying on it, as APCs change.
- **Abstract must not exceed 250 words.** No fixed manuscript length/word/page limit is specified (treat as "not specified," not "confirmed absent").
- The **cover letter must explain how the submission differs from any conference version** — GEB receives substantial CS/EC-conference-adjacent work, so prior conference publication is common and must be disclosed and distinguished.
- Any use of generative AI/AI-assisted tools must be declared in a section titled **"Declaration of generative AI and AI-assisted technologies..."** (待核实 — Elsevier uses both "...in the writing process" and "...in the manuscript preparation process"; copy the exact heading from the live Guide for Authors), placed **before the reference list** (basic grammar/spell tools exempt).
- Review is the **Editor-in-Charge model**: the chief editor assigns your paper to one of **seven Editors** (publicly known, final authority) over **anonymous** Advisory Editors and referees; **~one-third desk-rejected**, **~15% published** (see geb-review-process).

## Preflight checklist

### Format & files
- [ ] Manuscript in **LaTeX (elsarticle)** or **Word**, internally consistent
- [ ] **Abstract ≤ 250 words**, stating the contribution and main result
- [ ] References in a **single consistent style** (elsarticle-num is the published target)
- [ ] Theorems/lemmas numbered; proofs complete; appendix for long derivations
- [ ] Figures/tables (game trees, payoff matrices) self-contained and print-legible
- [ ] **Generative-AI declaration** present before the reference list, if AI tools were used

### Cover letter (GEB-specific)
- [ ] States the contribution to **game theory** in one or two sentences
- [ ] **Explicitly explains how the paper differs from any conference version** (or states there is none)
- [ ] Notes the most relevant sub-field to aid routing to an Editor in Charge
- [ ] Confirms the paper is not under review elsewhere

### Declarations & data
- [ ] Conflict-of-interest / funding disclosures prepared
- [ ] Data/code sharing plan ready — **encouraged, not required** at GEB (see geb-replication-and-data-policy)
- [ ] Suggested/excluded referees prepared if requested (expert, fair, conflict-free)

### Final content sanity
- [ ] Page-one contribution legible to a specialist Editor (see geb-contribution-framing)
- [ ] Assumptions/results/proofs audited (see geb-identification-strategy)
- [ ] No over-claiming beyond what the proofs/experiment support

## Anti-patterns

- Omitting the conference-version explanation in the cover letter (a GEB-specific must)
- An abstract over 250 words
- Mixed/inconsistent reference styles at submission
- Forgetting the generative-AI declaration when AI tools were used
- Budgeting for a mandatory data archive that GEB does not require, or for a submission fee not confirmed to exist

## Output format

```
【Format】elsarticle/Word, consistent; abstract ≤250 words? [Y/N each]
【Cover letter】contribution + conference-version statement? [Y/N each]
【AI declaration】present before references (if used)? [Y/N / NA]
【Data plan】prepared (encouraged, not required)? [Y/N]
【Declarations】COI / funding / not-under-review? [Y/N each]
【Next step】submit on Editorial Manager → await Editor-in-Charge desk decision → geb-rebuttal on R&R
```

## Supplementary resources

- [`templates/cover_letter_template.md`](templates/cover_letter_template.md) — GEB cover letter with the mandatory conference-version paragraph
- [`templates/checklist.md`](templates/checklist.md) — pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — solvers, experiment platforms, and typesetting tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official GEB URLs behind every fact (with 待核实 flags)
