---
name: jebo-submission
description: Use when running the final pre-submission preflight for the Journal of Economic Behavior & Organization (JEBO) via Elsevier Editorial Manager — abstract/keyword/JEL limits, author-date references, single-anonymized formatting, declarations, and the experimental-materials attachments. Final checks; it does not draft content.
---

# Submission Preflight (jebo-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to Editorial Manager
- Unsure which files, declarations, and limits JEBO/Elsevier expects
- Confirming the abstract, keywords, JEL, and reference style are compliant
- Packaging experiment instructions/code as supplementary material

## Process facts (检索于 2026-06；以官网为准)

- JEBO is published by **Elsevier** on ScienceDirect (ISSN 0167-2681); submission is through **Elsevier Editorial Manager**.
- Review is **single-anonymized** (referees anonymous, authors named) — so there is **no need to anonymize the manuscript**; include author names and affiliations.
- **Abstract ≤250 words**; **1–7 keywords**; **JEL classification codes** required.
- **References: author-date (Elsevier Harvard)** — in-text "(Author, year)"; reference list "Author, Year. Title. Journal vol, pages."
- **Declaration of competing interest** and **declaration of generative-AI use** required (Elsevier policy); AI may not be listed as an author.
- **Data/code**: Elsevier Research Data policy — sharing encouraged via Mendeley Data or a linked repository; a **data-availability statement** is expected (not a hard pre-acceptance gate — 待核实).
- **No submission fee** for standard submission; **open-access (gold) APC** applies only if the OA option is chosen (exact amount 待核实 — confirm on the journal page).
- Article types: research articles; check current calls for special issues (待核实).

## Preflight checklist

### Format & front matter
- [ ] Manuscript is **not** anonymized (single-anonymized review): author names + affiliations present
- [ ] **Abstract ≤250 words**, no undefined abbreviations, no references in the abstract
- [ ] **1–7 keywords** + **JEL codes** included
- [ ] References in **author-date Elsevier Harvard**; every in-text cite has a list entry and vice versa
- [ ] Tables/figures numbered, near first mention, legible in grayscale, self-contained captions
- [ ] Confidence intervals shown (asterisks not the sole evidence)

### Files for Editorial Manager
- [ ] Main manuscript (with embedded or separately-uploaded exhibits per the Elsevier flow)
- [ ] **Cover letter** stating the behavioral contribution and why JEBO (not a sibling)
- [ ] Supplementary: **experiment instructions + z-Tree/oTree code + protocol** (the JEBO-distinctive attachment)
- [ ] Data-availability statement / Mendeley Data link prepared
- [ ] Suggested/opposed reviewers entered (conflicts considered)

### Declarations
- [ ] Declaration of competing interest
- [ ] Declaration of generative-AI use (if any); AI not an author
- [ ] Funding sources stated
- [ ] Ethics/IRB approval and consent referenced for human-subjects work
- [ ] Pre-registration link + deviations (if applicable)
- [ ] Confirmed not under review elsewhere

## Anti-patterns

- Anonymizing the manuscript (unnecessary — review is single-anonymized) or, conversely, forgetting names
- Abstract over 250 words or stuffed with abbreviations/references
- Missing JEL codes or fewer/more than 1–7 keywords
- Numbered/Vancouver references instead of author-date Elsevier Harvard
- Submitting an experiment paper without instructions and experiment code attached
- Treating the gold-OA APC as a mandatory submission fee
- Omitting the competing-interest or generative-AI declaration

## Output format

```text
【Portal】Elsevier Editorial Manager; single-anonymized (names included)
【Front matter】abstract ≤250w / 1–7 keywords / JEL / author-date refs? [Y/N]
【Exhibits】numbered, grayscale-safe, CIs shown? [Y/N]
【Experiment materials】instructions + z-Tree/oTree code + protocol attached? [Y/N]
【Declarations】COI + generative-AI + funding + ethics? [Y/N]
【Data statement】Mendeley/repository link or justified restriction? [Y/N]
【Cover letter】states behavioral contribution + why-JEBO? [Y/N]
【Next step】submit → jebo-rebuttal when the decision arrives
```
