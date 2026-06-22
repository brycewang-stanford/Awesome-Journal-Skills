---
name: arpsych-submission
description: Use when running the final delivery preflight for a commissioned Annual Review of Psychology (ARPsych) review via the Annual Reviews production system — disclosures, reference/format compliance, figure permissions, length, and the transparency of any embedded meta-analysis. Final checks; it does not draft content or handle the post-review revision (arpsych-revision).
---

# Delivery Preflight (arpsych-submission)

## When to trigger

- "Delivering soon" — last check before handing the commissioned review to Annual Reviews
- Unsure which files, declarations, and permissions the production system expects
- Confirming length, reference completeness, and figure specs are Annual Reviews-ready
- Verifying transparency obligations for any quantitative synthesis the review reports

## Process facts (检索于 2026-06；以官网为准 — re-confirm on the Annual Reviews author pages)

- **Publisher / venue.** ARPsych is published by **Annual Reviews** (nonprofit), founded **1950**, as an **annual volume**, co-edited by **Susan T. Fiske** (since 2000) **and Daniel L. Schacter** (co-editors listed for Volume 77, 2026; web-verified 2026-06-22, re-verify before relying); it is a **review series**, distinct from *Psychological Bulletin* (submitted reviews/meta-analyses), *Annual Review of Clinical Psychology* (clinical sister), and *Perspectives on Psychological Science* (essays). Articles are **commissioned by the Editorial Committee**; there is **no cold-submission portal for unsolicited manuscripts** — delivery happens within the invited-article workflow (检索于 2026-06；以官网为准).
- **Open access.** Volumes are published **open access under the Subscribe-to-Open (S2O) model** (since 2023), under a Creative Commons license — there is **no author-facing APC** under S2O (检索于 2026-06；以官网为准). Do not treat S2O as a pay-to-publish APC.
- **Length.** Each article has a **length assigned in the invitation letter**, including figures and tables; keep to it (检索于 2026-06；以官网为准). There is no single journal-wide word limit — it is per-invitation.
- **Manuscript prep.** Annual Reviews asks for material **double spaced in 12-point type**; references must be complete and accurate (检索于 2026-06；以官网为准). House reference/format style is applied at production copyediting, so the delivered draft need not pre-conform — but reference data must be complete.
- **Disclosure (required).** Annual Reviews requires authors to **disclose potential sources of bias / conflicts of interest**; funding sources are stated. Prepare per the author pages (检索于 2026-06；以官网为准).
- **Transparency of the review itself.** A pure review reports no new data; the obligation bites on the **documented search** (from `arpsych-literature-synthesis`) and on **any meta-analysis** the review contributes — its data and code should be reproducible and depositable (检索于 2026-06；以官网为准).
- **Figures / permissions.** Confirm figure specs and secure permission for any reproduced/adapted exhibit (检索于 2026-06；以官网为准).

## Preflight checklist

### Article & files
- [ ] This is a **commissioned/invited** article delivered in the invited workflow (not a cold submission)
- [ ] Manuscript within the **assigned length** (figures and tables included)
- [ ] Double-spaced, 12-point; references complete and accurate (house style applied at production)
- [ ] Title page: title, complete author affiliations, keywords; review-style abstract
- [ ] Figures meet current specs; reproduced exhibits have permission and attribution

### Transparency
- [ ] Search account documented (databases, terms, dates, in/out) — near-PRISMA where applicable
- [ ] Any meta-analysis: effect data + code reproducible and depositable (OSF DOI)

### Declarations
- [ ] Conflict-of-interest / potential-bias disclosure prepared per Annual Reviews policy
- [ ] Funding sources stated
- [ ] AI not listed as an author

### Volatile re-confirms
- [ ] Assigned length, current reference style, figure specs, disclosure format, S2O/OA status — re-checked on the Annual Reviews author pages (检索于 2026-06)

## Anti-patterns

- Treating ARPsych like a journal with a cold-submission portal — it is invited; deliver through the commissioned workflow
- Treating S2O open access as a pay-to-publish APC (it is not author-funded under S2O)
- Over-running the assigned length or omitting figures/tables from the length count
- Omitting the conflict-of-interest / bias disclosure Annual Reviews requires
- Asserting a length limit, fee, or editor name from memory rather than the live author pages
- Delivering a meta-analysis with no reproducible data/code, or a review with no documented search

## Output format

```text
【Article type】commissioned/invited review (not cold submission)? Y/N
【Length】within the assigned length (figures/tables included)? Y/N
【Manuscript prep】double-spaced 12pt; references complete + accurate? Y/N
【Abstract + front matter】review-style abstract, keywords, affiliations? Y/N
【Transparency】search documented; meta-analysis (if any) reproducible? Y/N
【Disclosure】COI / bias disclosure + funding prepared? Y/N
【Figures】specs met; permissions secured? Y/N
【Volatile re-confirms】length / style / OA / disclosure checked on Annual Reviews pages? Y/N
【Next step】deliver to Annual Reviews → arpsych-revision when the editor/peer-review letter arrives
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Annual Reviews URLs and volatile facts
