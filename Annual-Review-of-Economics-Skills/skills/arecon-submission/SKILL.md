---
name: arecon-submission
description: Use when running the final delivery preflight for a commissioned Annual Review of Economics (ARE) review via the Annual Reviews production system — disclosure statements, reference/format compliance, figure permissions, and the transparency/reproducibility of any meta-analysis the review itself contains. Final checks; it does not draft content.
---

# Delivery Preflight (arecon-submission)

## When to trigger

- "Delivering soon" — last check before handing the commissioned review to Annual Reviews
- Unsure which files, declarations, and permissions the production system expects
- Confirming reference style, format, and figure specs are Annual Reviews-compliant
- Verifying transparency obligations for any quantitative synthesis (meta-analysis) the review itself reports

## Process facts (检索于 2026-06；以官网为准 — re-confirm on the Annual Reviews author pages)

- **Publisher / venue.** ARE is published by **Annual Reviews** (nonprofit), founded **2009**, as an **annual volume**; it is a **review series**, distinct from JEL (AEA survey of record), JEP (non-technical), and Handbook chapters. Articles are **commissioned by the Editorial Committee**; there is **no cold-submission portal for unsolicited manuscripts** — delivery happens within the invited-article workflow (检索于 2026-06；以官网为准).
- **Open access.** Volumes are published **open access under the Subscribe-to-Open (S2O) model** (2023–2025 converted; 2026 in production), under a Creative Commons license — there is **no author-facing APC** under S2O (检索于 2026-06；以官网为准). Do not treat S2O as a pay-to-publish APC.
- **Disclosure (required).** Annual Reviews requires authors to **disclose potential sources of bias / conflicts of interest**; funding sources are stated. Prepare the disclosure as the author pages specify (检索于 2026-06；以官网为准).
- **Reproducibility of the review itself.** A pure review reports no new data. The transparency obligation bites on **your systematic coverage** (a documented, near-PRISMA-style account of how the literature was searched and selected, from `arecon-literature-synthesis`) and on **any meta-analysis you contribute** — its data and code should be reproducible and depositable (检索于 2026-06；以官网为准).
- **Reference & format style.** Annual Reviews applies its **own house format and reference style** (numbered/name style distinct from AEA author-year) at production; the production editor copyedits to house style, so the delivered draft need not pre-conform, but reference data must be complete and accurate (检索于 2026-06；以官网为准).
- **Figures / permissions.** Confirm figure specs and secure permission for any reproduced exhibit (检索于 2026-06；以官网为准).
- **Length / abstract limits.** Exact word/abstract limits are **待核实** — confirm on the author pages; typical published reviews run ~25–40 pages (检索于 2026-06；以官网为准).

## Preflight checklist

### Article & files
- [ ] This is a **commissioned/invited** article delivered in the invited-article workflow (not a cold submission)
- [ ] Manuscript complete; references complete and accurate (house style applied at production)
- [ ] Title page: title, complete author affiliations, keywords; abstract in review style
- [ ] Figures meet current specs; reproduced exhibits have permission and attribution

### Transparency
- [ ] Systematic-coverage account documented (search strategy, inclusion/exclusion) — near-PRISMA where applicable
- [ ] Any meta-analysis the review reports: data + code reproducible and depositable

### Declarations
- [ ] Conflict-of-interest / potential-bias disclosure prepared per Annual Reviews policy
- [ ] Funding sources stated
- [ ] AI not listed as an author

### Volatile re-confirms
- [ ] Exact length/abstract limits, current reference style, figure specs, disclosure format, S2O/OA status — re-checked on the Annual Reviews author pages (检索于 2026-06)

## Anti-patterns

- Treating ARE like a journal with a cold-submission portal — it is invited; deliver through the commissioned workflow
- Treating S2O open access as a pay-to-publish APC (it is not author-funded under S2O)
- Omitting the conflict-of-interest / bias disclosure Annual Reviews requires
- Asserting a length limit, fee, or editor name from memory rather than the live author pages
- Delivering a meta-analysis with no reproducible data/code, or a systematic review with no documented search

## Output format

```text
【Article type】commissioned/invited review (not cold submission)? Y/N
【References】complete + accurate (house style at production)? Y/N
【Abstract + front matter】review-style abstract, keywords, affiliations? Y/N
【Transparency】coverage account documented; meta-analysis (if any) reproducible? Y/N
【Disclosure】COI / bias disclosure + funding prepared? Y/N
【Figures】specs met; permissions secured? Y/N
【Volatile re-confirms】length / style / OA / disclosure checked on Annual Reviews pages? Y/N
【Next step】deliver to Annual Reviews → arecon-review-process for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Annual Reviews URLs and volatile facts
