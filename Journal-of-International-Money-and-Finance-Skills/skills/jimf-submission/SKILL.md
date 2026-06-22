---
name: jimf-submission
description: Use when running the final pre-submission preflight for a Journal of International Money and Finance (JIMF) manuscript via Elsevier Editorial Manager — file set, abstract/Highlights/JEL, declarations (competing interest, CRediT), data statement, and house style. Final checks; it does not draft content.
---

# Submission Preflight (jimf-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to Elsevier Editorial Manager
- Unsure which files and declarations the Elsevier submission expects
- Confirming the abstract, Highlights, keywords, JEL codes, and references are JIMF/Elsevier-compliant
- Confirming the Data Availability Statement, competing-interest declaration, and CRediT statement are ready

## Process facts (检索于 2026-06；以官网为准 — re-confirm on the live Guide for Authors)

- JIMF is an **Elsevier** journal (ISSN 0261-5606 print; 1873-0639 online; founded 1982), hosted on ScienceDirect. Submission is through **Elsevier Editorial Manager** (待核实 if the journal has moved to a newer Elsevier submission system).
- **No society membership and no submission fee** for a standard paper; an open-access APC applies only if the author chooses gold OA (exact fee 待核实).
- **Peer review:** single-anonymized is the Elsevier default; whether JIMF uses single- or double-anonymized review is 待核实 — confirm before deciding whether to anonymize the manuscript.
- **Abstract ≤250 words**; **Highlights** (3–5 bullets) and **keywords** required; **JEL codes** expected (F3x / E4x / G15 territory).
- **Declarations** required by Elsevier: **Declaration of Competing Interest**, **CRediT** author-contribution statement, funding sources, and a **Data Availability Statement**.
- **Editors (verified 2026-06-22): Joshua Aizenman, Menzie D. Chinn, John Beirne, and Donghyun Park.** Note that some aggregators (IDEAS-RePEc, older caches) still list the late James R. Lothian — that is stale; do not use it. The board is volatile, so re-verify the sitting editors on the live Elsevier board page before naming one in a cover letter.

## Preflight checklist

### Manuscript & front matter
- [ ] Title page with all affiliations and the corresponding author
- [ ] **Abstract ≤250 words**, factual, with the headline magnitude
- [ ] **Highlights** (3–5 bullets, each a finding); **keywords**; **JEL codes** present
- [ ] Figures and tables with self-contained notes; consistent reference style (Elsevier/author-date — 待核实 exact style)
- [ ] Acronyms defined on first use (UIP, ERPT, GFCy, FXI, NEER)
- [ ] Online/supplementary appendix prepared and indexed (see `jimf-internet-appendix`)
- [ ] Substantive checks done first (identification, robustness, positioning) — this is the mechanics pass, not a content review
- [ ] References complete and consistent; in-text citations all resolve in the list

### Files & declarations for Editorial Manager
- [ ] Main manuscript (and a blinded version if double-anonymized review is confirmed)
- [ ] Highlights file, and any supplementary appendix file(s)
- [ ] **Declaration of Competing Interest** statement
- [ ] **CRediT** author-contribution statement; funding/grant acknowledgments
- [ ] **Data Availability Statement**; data/code deposit (Mendeley Data or repository link) ready
- [ ] Suggested reviewers if the journal requests them; cover letter naming the international contribution
- [ ] Blinded manuscript prepared if double-anonymized review is confirmed (待核实)
- [ ] OA choice decided; APC not confused with a submission fee

### Cover letter
- [ ] One paragraph: the international question, the design, the headline finding, and why it is JIMF (not JIE/JME/JMCB/JFE)
- [ ] Confirms the paper is not under review elsewhere and is original
- [ ] Does NOT name a specific editor from memory (verify the board first)

## Deciding on the Econometrica/transfer and OA questions

- **No transfer route** like the society journals: JIMF is a standalone Elsevier journal; there is no fee-waived transfer of reports from a sibling. A paper rejected elsewhere is a fresh submission here.
- **Open access is a choice, not a requirement.** JIMF is a subscription journal with an optional gold-OA route at an APC (exact fee 待核实). Do not treat the APC as a submission fee; standard submission carries no fee.
- **Anonymization** depends on the review model: if double-anonymized is confirmed, prepare a blinded manuscript (no author names, scrubbed acknowledgments, neutral self-citations) and a separate title page; if single-anonymized, the author-visible manuscript is fine. Confirm before deciding (待核实).
- **Suggested/opposed reviewers**: if Editorial Manager requests them, suggest international-finance specialists in the paper's sub-program and avoid conflicts.

## Final-pass desk-reject screen

Before uploading, read the paper as an editor doing a 10-minute triage: Is the international contribution unmistakable on page 1? Is the abstract under 250 words with a number? Are Highlights, keywords, and JEL present? Is the cover letter saying why JIMF and not a sibling? Is the data/code deposit attached, not promised? A "no" on any of these is a common, avoidable desk-reject and should be fixed before submission, not after.

## What this preflight does not do

This is a mechanics-and-compliance check, not a content review. It confirms the file set, front matter, declarations, and house style are submission-ready; it does not judge whether the identification holds (`jimf-identification`), whether the result is robust (`jimf-robustness`), or whether the contribution is staked (`jimf-literature-positioning`). Run those substantive checks first; a perfectly formatted submission with a weak design wastes a review cycle. The preflight's value is catching the avoidable rejections — missing Highlights, an over-long abstract, an absent data statement, a cover letter that never says why JIMF.

## Anti-patterns

- Uploading without Highlights, keywords, or JEL codes — a visible Elsevier-compliance gap
- An abstract over 250 words or with undefined acronyms
- Missing the Declaration of Competing Interest, CRediT statement, or Data Availability Statement
- A cover letter that does not say why the paper is *international money and finance* specifically
- Naming a current editor from memory when the board page is the source of truth
- Treating the data/code deposit as a post-acceptance task instead of attaching it now

## Output format

```text
【Front matter】abstract ≤250w + Highlights + keywords + JEL? [Y/N]
【Declarations】competing interest + CRediT + funding + data statement? [Y/N]
【Files】manuscript (+ blinded if needed) + Highlights + appendix + deposit ready? [Y/N]
【Cover letter】states the international contribution; no editor named from memory? [Y/N]
【Review model】single/double-anonymized confirmed? [Y/N / 待核实]
【Source check】Elsevier process facts verified / 待核实 / 检索于 2026-06
【Next step】submit via Editorial Manager → jimf-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
