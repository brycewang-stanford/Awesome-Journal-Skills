---
name: revacc-submission
description: Use when a Review of Accounting Studies (RAST) manuscript is close to submission and needs the Editorial Manager preflight — anonymization for double-blind review, the submission fee and its deadline, file completeness, and format compliance. Runs the preflight; it does not polish prose (revacc-writing-style) or plan the review cycle (revacc-review-process).
---

# Submission Preflight (revacc-submission)

## When to trigger

- The manuscript is finished and you are about to upload to Editorial Manager
- You need to confirm the double-blind anonymization is complete
- You must budget for and schedule the submission fee within its deadline
- You are deciding between the regular journal and the **RAST Conference** submission path
- You need a final completeness check on files, abstract, and formatting

## RAST submission mechanics (verify before relying)

| Item | What to do | Status |
|------|------------|--------|
| Portal | Submit through **Editorial Manager** (Springer) | 待核实; 检索于 2026-06 |
| Submission fee | **USD $500**, payable **within 7 days** or the manuscript is removed (desk rejection refunds the fee minus a **US$75** admin charge) | verified on the Springer submission guidelines, 核查于 2026-06-22; re-verify before submitting |
| Managing Editor | **Lakshmanan (Shiva) Shivakumar** (London Business School) | verified 2026-06-22 (Springer editorial-board page via snippets + LBS pages); re-verify masthead |
| Review model | **Double-blind** — anonymize the manuscript fully | 待核实 |
| Abstract limit | ~**150–250 words** | 待核实 |
| Length | Confirm any page/word limit on the official guidelines page | 待核实 |
| Conference path | RAST Conference submissions feed a **conference issue**; all are also considered for the regular journal | verified via Wharton page, 检索于 2026-06 |

Always re-check fee, abstract limit, length, and editor on the official Springer page (link.springer.com/journal/11142) at submission time.

## Anonymize for double-blind review

Because RAST is double-blind, scrub author identity thoroughly — referees should not be able to infer the authors:

- Remove author names, affiliations, acknowledgements, and funding/grant identifiers from the manuscript file.
- Strip identifying metadata from the document and from any data/code file names.
- Neutralize self-citations ("Smith (2022) shows" not "in our prior work (Smith 2022)"); cite your own working papers without revealing authorship where possible.
- Remove conference/seminar acknowledgements and presentation footnotes that fingerprint the authors.

## File and format completeness

- **Title page** (separate, with author details) vs. **anonymized manuscript** — keep them distinct.
- **Abstract** within the limit, **keywords**, and **JEL codes** if requested.
- **Tables and figures** placed per the guidelines, self-contained, anonymized (see `revacc-tables-figures`).
- **Online appendix / proofs** for analytical papers; **data provenance** notes for empirical work.
- **ORCID**, **cover letter** (state the contribution and confirm no concurrent submission), and any **AI-use disclosure** the publisher requires (待核实).
- A reconstructable **data-and-code** trail ready if requested in review (RAST does not headline a posted package the way JAR does, but be ready — 待核实).

## Fee logistics

Budget the **$500 fee** before you submit and pay **within the 7-day window** — a missed payment withdraws the paper regardless of quality (待核实; confirm the current amount and window). Confirm waiver/discount eligibility on the official page if relevant.

## Checklist

- [ ] Manuscript fully anonymized (names, affiliations, acknowledgements, metadata, self-cites)
- [ ] Separate title page with author details prepared
- [ ] Abstract within the limit; keywords / JEL codes as required
- [ ] Tables/figures self-contained and anonymized
- [ ] Analytical proofs / online appendix or empirical provenance trail included
- [ ] Cover letter states the contribution and confirms exclusivity
- [ ] Submission fee budgeted and payable within the deadline
- [ ] Conference vs. regular path chosen deliberately
- [ ] Fee, abstract limit, length, and editor re-verified on the official page

## Anti-patterns

- **Leaky anonymization:** self-citations or acknowledgements that reveal the authors.
- **Identifying metadata** left in the document or file names.
- **Missing the 7-day fee window**, auto-withdrawing an otherwise strong paper.
- **Trusting cached facts:** quoting last year's fee/limit without re-checking the official page.
- **Wrong path:** submitting to the conference issue when the regular track was intended (or vice versa).

## Output format

```text
【Portal】Editorial Manager (Springer) — verified? (待核实)
【Anonymization】names/affil/ack/metadata/self-cites scrubbed? yes/no
【Files】title page / anon manuscript / abstract / keywords / proofs or provenance
【Fee】USD $500 within 7 days budgeted? (待核实)
【Path】regular journal / RAST Conference issue
【Re-verify】fee + abstract limit + length + editor on official page
【Next skill】revacc-review-process
```
