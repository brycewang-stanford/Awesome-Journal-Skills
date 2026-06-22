---
name: respol-submission
description: Use when running the final pre-submission preflight for Research Policy (RP) via Elsevier's online submission system — article-type choice, length/abstract limits, double-blind anonymization, data & code statement, and the out-of-scope desk-screen. Final checks; it does not draft content.
---

# Submission Preflight (respol-submission)

## When to trigger

- "Submitting tomorrow" — last check before uploading to the Elsevier submission system
- Choosing between a full article and a Research Note, and what each requires
- Confirming length, abstract, anonymization, and declaration rules are RP-compliant
- Making sure the paper will not trip the out-of-scope desk screen

## Process facts (source map refreshed 2026-06，editor/fee 项再核实于 2026-06-22；以官网为准)

- RP is **Elsevier's** flagship innovation-studies journal (Print ISSN 0048-7333); manuscripts go through the **Elsevier online submission system** (Editorial Manager), which assembles a single PDF for review; editable source files (Word/LaTeX) are required at acceptance for typesetting.
- **Review model: double-blind** — the manuscript must be anonymized; author identities are concealed from referees and vice versa (检索于 2026-06；以官网为准).
- **Article types & length:** full articles ~**8,000–10,000 words** including footnotes, references, and text in tables; **Research Notes** ~**3,000–5,000 words** (not a faster, lighter article — a Note requires a cover letter explaining its rationale, contribution, and why the Note format) (检索于 2026-06；以官网为准).
- **Scope desk-screen:** a paper whose literature is "almost entirely economics or management journals" is likely desk-rejected as out of scope; the cover letter and references must show innovation-studies (SPRU-tradition) grounding (检索于 2026-06；以官网为准).
- **Data & code:** include a data (and, where relevant, code) availability statement; verify the exact policy and any mandatory statement wording on the guide for authors (待核实).
- **Editorial routing:** RP runs a **distributed editorial team (no single Editor-in-Chief)**; **Maria Savona** (SPRU / Luiss) is the **Coordinating Editor** (verified 2026-06-22). Address the cover letter to the journal and name the *innovation-studies area* so it routes to the right handling editor, rather than to one person by name.
- **Fees:** publishing via the **subscription route carries no APC and no submission fee**; the optional gold **open-access APC is reported around USD 3,700 for 2026** (verified 2026-06-22; Elsevier shows a personalized APC by country/affiliation, so confirm the exact figure live). There is no society-style per-submission fee.
- Exact current abstract word limit and keyword/JEL requirements: 待核实 — confirm on the live guide for authors before submitting.

## Preflight checklist

### Scope & article type
- [ ] References and cover letter visibly anchor the paper in innovation studies (not econ/management-only)
- [ ] Article type chosen deliberately: full article vs. Research Note (with the Note rationale cover letter if applicable)
- [ ] The cover letter names the innovation-studies contribution and the suggested handling-editor area

### Format & anonymization
- [ ] Length within the article-type limit (full ~8–10k incl. notes/refs/tables; Note ~3–5k) — 待核实 exact figure on the guide
- [ ] Manuscript fully **anonymized** for double-blind review (no author names, acknowledgements, self-citations that reveal identity, or identifying file metadata)
- [ ] Abstract within the journal's limit; keywords (and JEL if requested) present — 待核实
- [ ] Tables and figures legible, numbered, with self-contained notes; reference style per the Elsevier guide
- [ ] Editable source files (Word/LaTeX) ready for the acceptance stage

### Declarations
- [ ] Data (and code) availability statement included and consistent with the analysis
- [ ] Funding, competing-interest, and authorship statements prepared per Elsevier policy
- [ ] Confirmed the paper is not under review elsewhere; AI not listed as an author

## Full article vs. Research Note (decide before you format)

| | Full article | Research Note |
|---|---|---|
| Length (待核实 exact) | ~8,000–10,000 words incl. notes/refs/tables | ~3,000–5,000 words |
| Best for | a developed mechanism + full evidence and robustness | a focused, complete contribution (a finding, a measurement, a replication-with-twist) |
| Cover letter | states the innovation-studies contribution | **must additionally justify the Note format** — RP stresses a Note is *not* a faster/lighter article |
| Common mistake | padding a Note-sized idea into a thin full article | submitting an underdeveloped full article as a "Note" to dodge rigor |

## Anti-patterns

- Submitting a paper whose lit base is "all econ/management" — the canonical out-of-scope desk reject
- Treating a Research Note as a quick, lighter article (it needs its own justifying cover letter)
- Leaving author-identifying traces in a double-blind submission (acknowledgements, file metadata, "as we showed in [own work]")
- Omitting or mismatching the data/code availability statement
- Asserting an exact word/abstract limit or fee as fixed when it is volatile — mark 待核实 and check live

## Output format

```text
【Journal】Research Policy
【Skill】respol-submission
【Scope】lit base + cover letter anchored in innovation studies? [Y/N]
【Article type】full / Research Note (+ Note rationale letter if Note)
【Length & abstract】within limits (or 待核实)? [Y/N]
【Anonymization】double-blind clean (text + metadata)? [Y/N]
【Data/code statement】included and consistent? [Y/N]
【Declarations】funding / competing interest / authorship ready? [Y/N]
【Next step】submit via Elsevier system → respol-review-process for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
