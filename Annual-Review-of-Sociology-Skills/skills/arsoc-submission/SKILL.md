---
name: arsoc-submission
description: Use when running the final delivery preflight for a commissioned Annual Review of Sociology (ARSoc) review via the Annual Reviews production system — disclosure statements, reference/format compliance, figure permissions, and the transparency of the coverage account or any meta-analysis the review contains. Final checks; it does not draft content or handle the response letter (arsoc-revision).
---

# Delivery Preflight (arsoc-submission)

## When to trigger

- "Delivering soon" — last check before handing the commissioned review to Annual Reviews
- Unsure which files, declarations, and permissions the production system expects
- Confirming reference style, format, and figure specs are Annual Reviews-compliant
- Verifying transparency obligations for the coverage account and any quantitative synthesis the review reports

## Process facts (检索于 2026-06；以官网为准 — re-confirm on the Annual Reviews author pages)

- **Publisher / venue.** ARSoc is published by **Annual Reviews** (nonprofit), founded **1975** (ISSN 0360-0572 print / 1545-2115 online), as an **annual volume**; it is a **review series**, distinct from ASR/AJS (sociology's primary-research flagships), *Sociological Theory* (theory development), and the sister Annual Reviews of Psychology/Economics. Articles are **invitation-led**: "experienced researchers are invited by journals' Editorial Committees to write Annual Reviews articles." There is **no cold-submission portal for unsolicited manuscripts** — delivery happens within the invited-article workflow (检索于 2026-06；以官网为准).
- **How a topic gets onto the list / suggesting one.** There is no public author-submission portal; the **Editorial Committee sets the topic list and issues invitations**. The source map records no formal author topic-proposal channel, so if you want to propose a topic or be considered, route it informally to the Editorial Committee (see the Editorial Committee page) — **待核实** whether a formal proposal mechanism exists; confirm on the author pages (检索于 2026-06；以官网为准).
- **Review/acceptance bar.** Annual Reviews states that review selections are assessed for **accuracy, rigor, and balance** (检索于 2026-06；以官网为准).
- **Editors.** Co-editors **Douglas S. Massey & Mary C. Waters** (co-editors since Aug 2023; verified 2026-06-22 — re-confirm on the Editorial Committee page, editors rotate).
- **Open access / fees.** Current volumes are published **open access under the Subscribe-to-Open (S2O) model**: Annual Reviews announced the S2O commitment in **2023** and reports that in **2024 all volumes were successfully published OA**. S2O is **library/subscriber-funded, not author-funded**, so it is not a pay-to-publish APC; treat any author-facing fee as **待核实** on the author pages (检索于 2026-06；以官网为准).
- **Disclosure (required).** Annual Reviews requires authors to **disclose potential sources of bias / conflicts of interest**; funding sources are stated. Prepare the disclosure as the author pages specify (检索于 2026-06；以官网为准).
- **Transparency of the review itself.** A pure review reports no new data. The transparency obligation bites on **your coverage account** (a documented, near-PRISMA-style search/selection record, from `arsoc-transparency-and-reproducibility`) and on **any meta-analysis/bibliometric analysis you contribute** — its data and code should be reproducible and depositable (检索于 2026-06；以官网为准).
- **Reference & format style.** Annual Reviews applies its **own house format and reference style** (distinct from ASA author-date) at production; the production editor copyedits to house style, so the delivered draft need not pre-conform, but reference data must be complete and accurate (检索于 2026-06；以官网为准).
- **Figures / permissions.** Confirm figure specs and secure permission for any reproduced exhibit (检索于 2026-06；以官网为准).
- **Length / abstract limits.** Exact word/abstract/keyword limits are **待核实** and are **not asserted from the source map** — they are article-specific delivery facts set by the current author resources and your editor correspondence; confirm there rather than assuming a number (检索于 2026-06；以官网为准).

## Preflight checklist

### Article & files
- [ ] This is a **commissioned/invited** article delivered in the invited-article workflow (not a cold submission)
- [ ] Manuscript complete; references complete and accurate (house style applied at production)
- [ ] Title page: title, complete author affiliations, keywords; abstract in review style
- [ ] Figures meet current specs; reproduced exhibits have permission and attribution

### Transparency
- [ ] Coverage account documented (search strategy, inclusion/exclusion, saturation) — near-PRISMA where applicable
- [ ] Any meta-analysis/bibliometrics the review reports: data + code reproducible and depositable (DOI)

### Declarations
- [ ] Conflict-of-interest / potential-bias disclosure prepared per Annual Reviews policy
- [ ] Funding sources stated
- [ ] AI not listed as an author

### Volatile re-confirms
- [ ] Exact length/abstract limits, current reference style, figure specs, disclosure format, S2O/OA status, current editors — re-checked on the Annual Reviews author pages (检索于 2026-06)

## Anti-patterns

- Treating ARSoc like a journal with a cold-submission portal — it is invited; deliver through the commissioned workflow
- Treating S2O open access as a pay-to-publish APC (it is not author-funded under S2O)
- Omitting the conflict-of-interest / bias disclosure Annual Reviews requires
- Asserting a length limit, fee, or editor name from memory rather than the live author pages
- Delivering a meta-analysis with no reproducible data/code, or a review with no documented coverage account

## Output format

```text
【Article type】commissioned/invited review (not cold submission)? Y/N
【References】complete + accurate (house style at production)? Y/N
【Abstract + front matter】review-style abstract, keywords, affiliations? Y/N
【Transparency】coverage account documented; meta-analysis (if any) reproducible? Y/N
【Disclosure】COI / bias disclosure + funding prepared? Y/N
【Figures】specs met; permissions secured? Y/N
【Volatile re-confirms】length / style / OA / disclosure / editors checked on Annual Reviews pages? Y/N
【Next step】deliver to Annual Reviews → arsoc-revision after the Committee letter
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight review scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Annual Reviews URLs and volatile facts
