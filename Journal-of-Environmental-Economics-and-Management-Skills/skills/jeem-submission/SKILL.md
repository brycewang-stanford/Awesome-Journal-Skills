---
name: jeem-submission
description: Use when running the final pre-submission preflight for a Journal of Environmental Economics and Management (JEEM) manuscript via Elsevier Editorial Manager — the scope/style desk-screen, submission fee, abstract/length limits, data-availability statement, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (jeem-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to Elsevier Editorial Manager
- Unsure which files, statements, and fees JEEM's submission expects
- Confirming scope/style compliance so the paper is not desk-rejected before review
- Deciding between the regular-paper and short-paper/note route
- Preparing the data-availability statement and declarations Elsevier requires at submission

## Process facts (检索于 2026-06；以官网为准 — re-confirm on the official ScienceDirect guide for authors)

- JEEM is published by **Elsevier** (ScienceDirect, ISSN 0095-0696); submission is through **Elsevier Editorial Manager**. The journal appears six times a year.
- **Submission fee:** a fee is charged at submission — approximately **US$100** regular / **US$50** full-time student (待核实 exact current amounts and waivers). Manuscripts are considered only after the fee is paid, and a paper may be **rejected without review** for scope or style non-compliance — the fee is generally **not refunded** on a desk reject.
- **Short papers / notes:** JEEM accepts short submissions that make a contribution comparable to full papers, with expedited review and minimal revision; the exact word ceiling for the short-paper route is volatile (sources cite figures from ~3,000 up to ~6,000 words) — 待核实.
- **Data-availability / replication:** data must be documented and made available for replication, computational methods explained in enough detail to reproduce, and the **Editor notified at submission if these conditions cannot be met**. Elsevier's data-statement and code-sharing requirements apply (待核实 current form).
- **Co-Editors-in-Chief:** Roger H. von Haefen (NC State) and Andreas Lange (Hamburg) — re-verified 2026-06-22 (Elsevier editorial board / IDEAS-RePEc); re-confirm on the live masthead before submission. Review model (single vs. double anonymized) — confirm the current setting in the guide for authors (待核实).
- **Sibling caution:** do not submit to JEEM a paper better suited to **JAERE**, **Resource and Energy Economics**, or **Ecological Economics**; the environmental mechanism must be load-bearing.

## Why the fee changes the calculus

The submission fee makes JEEM unusual among the venues a paper might target, and it sharpens the preflight's stakes: a desk reject costs money, not just time, and the fee is generally non-refundable on a scope/style return (待核实 current refund policy). The practical consequence is that the scope and style screens deserve more pre-submission attention here than at a fee-free journal — it is worth an extra read against the guide for authors and an honest self-check that the environmental mechanism is load-bearing before paying. Confirm the current fee amount, student discount, and any low-income-country waiver (待核实) at the Editorial Manager submission step rather than assuming a figure.

## Preflight checklist

### Scope & style desk-screen (the desk-reject gate)
- [ ] Environmental/resource mechanism is unmistakably load-bearing (not decoration)
- [ ] The paper clears the field-journal bar (welfare-relevant number, credible economics)
- [ ] Format and reference style conform to the current guide for authors (待核实 — Elsevier style)
- [ ] Abstract within the journal's word limit (待核实); keywords and JEL codes as required
- [ ] Regular vs. short-paper route chosen; word count within the relevant ceiling (待核实)

### Files & fee for Editorial Manager
- [ ] Main manuscript (Elsevier format); exhibits per artwork specs; appendices as required
- [ ] Submission fee ready (regular/student) — paid at submission, non-refundable on desk reject
- [ ] Data and code deposit / availability statement prepared (see `jeem-replication-package`)
- [ ] Cover letter stating the contribution and JEEM fit; suggested/excluded reviewers if requested

### Final read against the live guide
- [ ] Re-checked the current guide for authors today (limits/style/fee/policy are volatile — 待核实)
- [ ] Confirmed the journal is still the right field venue vs. JAERE / Resource and Energy Economics

### Declarations
- [ ] Declaration of interest / funding statement (Elsevier policy)
- [ ] CRediT author-contribution statement if required (待核实)
- [ ] Data-availability statement; Editor notified if data cannot be fully shared
- [ ] Confirmed not under review elsewhere; AI/LLM use disclosed per Elsevier policy; AI not listed as author

## The desk-reject gate, in practice

JEEM's editors screen before review, and the fee is generally lost on a desk reject — so the preflight's highest-value job is to avoid one. Two failure modes dominate. First, **scope:** a paper whose environmental mechanism is decoration (a generic applied-micro result on a green dataset) is the classic JEEM desk reject — confirm the externality/resource/valuation content is load-bearing (`jeem-topic-selection`). Second, **style:** non-conformance to Elsevier/JEEM format, reference style, abstract length, or artwork specs can trigger a return without review. Run the manuscript against the current guide for authors immediately before upload; treat every length, abstract, and format number as 待核实 and re-check it, because Elsevier specs change.

## Cover letter that earns a review

The cover letter is read at the scope screen. State, in three or four sentences: the environmental problem and its policy stake, the design and the welfare-relevant number it delivers, why this is a JEEM (not JAERE / JPubE / Ecological Economics) contribution, and any data-availability constraint the Editor must know about at submission. A cover letter that does this gives the editor the load-bearing-mechanism evidence needed to send the paper out rather than screen it.

## Anti-patterns

- Submitting a paper whose environmental angle is decoration — the fastest desk reject
- Paying the fee, then losing it to a scope/style desk reject that a preflight would have caught
- Treating the data-availability statement as a post-acceptance formality
- Misformatting references/artwork against current Elsevier specs
- Choosing the short-paper route for a paper that needs full-length treatment (or vice versa)

## Choosing the route: regular vs. short paper

Before upload, confirm the route. The **short-paper / note** route suits a single decisive contribution — one new parameter estimate, a robustness correction to a published result, a focused valuation-method note — and offers expedited review with minimal revision (检索于 2026-06；以官网为准; word ceiling 待核实). The **regular** route suits a multi-part argument with theory, identification, and welfare analysis. Padding a short contribution to full length wastes referee patience; cramming a full argument into the short format invites "underdeveloped." Pick the route that matches the contribution's natural size, and verify the current word ceiling for each in the guide for authors before counting.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-submission
【Scope screen】mechanism load-bearing + field-bar cleared? [Y/N]
【Style】Elsevier format/refs + abstract limit + JEL/keywords? [Y/N] (待核实 limits)
【Route】regular / short-paper — word count within ceiling? [Y/N]
【Fee】submission fee ready (non-refundable on desk reject)? [Y/N]
【Data statement】availability statement + Editor notice if restricted? [Y/N]
【Declarations】DoI / funding / CRediT / AI disclosure ready? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next step】submit via Editorial Manager → jeem-rebuttal after the decision
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
