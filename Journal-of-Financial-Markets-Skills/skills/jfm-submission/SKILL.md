---
name: jfm-submission
description: Use when running the final pre-submission preflight for a Journal of Financial Markets (JFM) manuscript via Elsevier Editorial Manager — file set, blinding, declarations, data statement, and house formatting. Final checks; it does not draft content.
---

# Submission Preflight (jfm-submission)

## When to trigger

- "Submitting this week" — last check before uploading to Editorial Manager
- Unsure which files and declarations the Elsevier submission form expects
- Confirming the manuscript is correctly blinded for the review model
- Verifying competing-interest, data, and AI-use statements are in place

## Process facts (检索于 2026-06，费用项再核实于 2026-06-22；以官网为准; re-confirm on the JFM guide for authors before submitting)

- JFM is an **Elsevier** journal (ISSN 1386-4181 print / 1878-576X online); submission is via **Elsevier Editorial Manager** (待核实 the exact portal link on the journal's guide-for-authors page).
- **Review model:** double-blind reported by secondary sources (待核实 against the official guide). If double-blind, the manuscript file must be **fully anonymized** — no author names, no acknowledgments, no self-citation tells like "in our earlier work," no identifying file metadata; author details go on a separate title page.
- **Reference style, abstract word limit, and any structured-abstract / JEL requirements:** 待核实 on the guide for authors. Elsevier finance journals typically use an author-date style; confirm the exact format.
- **Declarations (Elsevier-standard):** Declaration of Competing Interest; funding sources; CRediT author-contribution statement; data-availability statement; statement on generative-AI use (AI may not be listed as an author). Verify the current required set.
- **Submission fee:** JFM charges a **US$170 submission fee** for original *and* revised submissions; the manuscript is only considered once the fee is paid (verified 2026-06-22 via the Elsevier guide for authors; re-confirm live, and check the developing-country/limited-means waiver if relevant). Do **not** assume JFM is fee-free.
- **APC / open access:** JFM offers subscription (no APC) and open-access routes; the OA **APC is USD 3,040 excluding taxes** (verified 2026-06-22, single source — treat as indicative and re-confirm the exact figure live before opting into open access).

## Preflight checklist

### Blinding & files
- [ ] If double-blind: manuscript fully anonymized (text, acknowledgments, self-citations, file metadata)
- [ ] Separate title page with all authors, affiliations, and corresponding-author contact
- [ ] Main manuscript (PDF/Word per portal), exhibits embedded or per Elsevier convention
- [ ] Internet Appendix / supplementary file uploaded as a separate item
- [ ] Cover letter naming the microstructure contribution and why JFM (not JF/JFE/RFS)

### Content & style
- [ ] Abstract within the stated limit (待核实); keywords / JEL as required
- [ ] Reference style matches the guide for authors (待核实)
- [ ] Every liquidity measure defined; units consistent across exhibits; SE/clustering in table notes
- [ ] Suggested reviewers prepared if the portal requests them (avoid conflicts/coauthors)

### Declarations
- [ ] Declaration of Competing Interest + funding statement
- [ ] CRediT contribution statement
- [ ] Data-availability statement (consistent with the proprietary-feed access path in the Internet Appendix)
- [ ] Generative-AI use statement; AI not listed as author
- [ ] Confirmed the paper is not under review elsewhere

## Matching the data statement to reality

Elsevier requires a data-availability statement, and for microstructure papers this is where proprietary feeds create a trap. The statement must be **truthful and consistent with the Internet Appendix access path**: if the order-book data come from a licensed vendor that prohibits redistribution, say so and point to the access path, rather than checking "data available on request." An inconsistency between a permissive data statement and a paper that visibly uses a restricted feed is a credibility flag the editor can see at desk screen. Confirm the journal's current data-and-code policy and whether any deposit is required at submission vs. acceptance (待核实).

## The blinding pass (if double-blind — 待核实)

Anonymization fails most often on subtle tells, so do an explicit pass: (1) strip author names, affiliations, emails, and acknowledgments (including grant-number thanks that name an author's institution); (2) neutralize self-citations — "we show in Smith (2022)" becomes "as shown in prior work (citation withheld for review)"; (3) clear document metadata (author field, file path, track-changes history) from the PDF/Word file; (4) remove links to a named personal/SSRN page that identifies the authors; (5) check figure source files and embedded code comments for names. A separate, fully attributed title page carries all the author information the editor needs.

## Cover letter craft

The cover letter is read by the handling editor as a triage signal. In a tight paragraph: state the **microstructure contribution** in one sentence with the headline magnitude; say **why JFM specifically** (the trading-process mechanism / specialist depth, not "we were rejected by JF"); name the **data and identifying variation**; and confirm the paper is not under review elsewhere. If suggesting reviewers, propose microstructure specialists with no coauthorship/advising conflict. A letter that pitches the paper as broad finance undercuts the desk-screen for a microstructure journal.

## Suggested reviewers and conflicts

If the portal requests suggested reviewers, treat it as a real lever. Propose three to five **microstructure specialists** whose own work your paper engages, excluding recent coauthors, advisors/advisees, and same-institution colleagues — a conflicted suggestion is worse than none. The point is to signal which sub-field expertise the paper needs (information-based, market design, HFT), helping the editor route it well. If there are scholars who should be excluded for a genuine conflict, the portal usually allows that too; use it sparingly and only for real conflicts, since over-exclusion reads as gaming the process. None of this substitutes for the paper standing on its own at desk screen.

## Anti-patterns

- Uploading a non-anonymized manuscript when the model is double-blind (self-citation/metadata tells)
- A data-availability statement that contradicts the replication package's access path
- Forgetting the US$170 submission fee (due on original *and* revised submissions), or assuming a fixed word limit, without checking the live guide
- A cover letter that pitches the paper as broad finance instead of microstructure
- Treating any volatile fact above as settled when it is marked 待核实

## Last-mile consistency checks

The cheapest rejections come from internal inconsistencies a careful pass would catch. Confirm: the title, abstract, and intro state the **same headline magnitude**; every liquidity measure is **defined on first use** and labeled identically across tables; **units** (bps/cents/shares/horizon) are consistent everywhere; table notes **all** name the clustering scheme; the **data-availability statement** matches the proprietary-feed access path documented in the Internet Appendix; and the reference list format matches the guide for authors (待核实). Run a final figure check that every event study shows pre-event leads. These take an hour and remove the most common avoidable desk-screen failures for a microstructure submission.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-submission
【Blinding】anonymized for double-blind + separate title page? [Y/N]
【Files】manuscript + title page + Internet Appendix + cover letter ready? [Y/N]
【Style】abstract limit / reference style verified or 待核实
【Declarations】COI / funding / CRediT / data / AI all present? [Y/N]
【Cover letter】names microstructure contribution + why JFM? [Y/N]
【Source status】portal & policy verified or 待核实
【Next step】submit via Editorial Manager → jfm-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
