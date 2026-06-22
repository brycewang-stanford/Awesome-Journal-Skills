---
name: eursr-submission
description: Use when running the final pre-submission preflight for the European Sociological Review (ESR) via ScholarOne Manuscripts — anonymous-manuscript preparation, word/abstract caps, OUP author-date style, the Data Availability Statement, and replication-package readiness. Final checks; it does not draft content.
---

# Submission Preflight (eursr-submission)

The last check before submitting through **ScholarOne Manuscripts** (`mc.manuscriptcentral.com/esr`).
ESR is **double-blind**, so the most common avoidable failure is an under-anonymized manuscript; the
second is a missing or vague **Data Availability Statement**. Verify volatile specifics (caps, policy
dates, editors, any fees) on the official OUP/ESR page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure what ScholarOne expects (anonymous manuscript + DAS + replication readiness)
- Confirming the caps are met, the manuscript is anonymous, and the data statement is in place

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** **flagship journal of ECSR** (European Consortium for Sociological Research, a
  non-profit under German law hosted at the WZB Berlin), published by **Oxford University Press**. Scope:
  sociology with a **quantitative emphasis**.
- **Editor-in-Chief:** **Prof. Fabrizio Bernardi** (National University of Distance Education, UNED)
  (verified 2026-06-22 via ECSR, OUP, and Wikipedia; re-confirm the full team/term on the live
  Editorial Board page, as offices rotate).
- **Portal:** **ScholarOne Manuscripts**, `mc.manuscriptcentral.com/esr`.
- **Review model:** **double-blind** — the manuscript must be **completely anonymous**; you **may cite
  your own work** but not in identifying wording.
- **Length:** Articles **around 8,000 words including endnotes and references** (tables and figures
  excluded); longer papers are considered, but reviewers judge whether the contribution justifies the
  length. (Some renderings cite a stricter cap — confirm the current figure; 待核实.)
- **Abstract:** **≤200 words**, no identifying information; keywords as requested.
- **Format / style:** English; **author-date** citations (e.g., "(Gans, 1962)") per OUP/ESR conventions.
- **Data Availability Statement:** **required for every manuscript** (policy applies to submissions from
  5 Sep 2022).
- **Replication package:** for **statistical/computational** work, **submissions from 1 Jan 2025** must
  deposit a package as a condition of publication (assemble it now; typically required at conditional
  acceptance). **Qualitative work is exempt. Restricted/confidential data are accommodated** via
  shareable code plus a documented access path (no need to deposit the raw data itself).
- **Article types:** research **Articles**, **Comments/Replies**, and **Data Briefs**.
- **Fees:** no submission fee (verified 2026-06-22); an open-access APC applies only if OA is chosen.
  OUP sets the exact ESR APC on its live charges page and does not publish a stable figure — confirm the
  current amount and any read-and-publish/transformative-agreement waiver there. **Acceptance rate, time-to-first-decision, and reviewer count are not verified in
  the source map — check the live OUP/ESR page; do not quote a figure.**

## Preflight checklist

### Type & length
- [ ] Article (~8,000 words incl. text + endnotes + references) / Comment-Reply / Data Brief
- [ ] If over ~8,000, the contribution-justifies-length case is made
- [ ] Abstract ≤200 words, non-identifying; keywords included

### Anonymity (double-blind review)
- [ ] No author names, affiliations, or identifying acknowledgments anywhere in the manuscript
- [ ] Self-citations neutralized ("in a prior study," not "in our prior study")
- [ ] Identifying **file metadata stripped** (document properties)
- [ ] No identifying funding/grant numbers in the manuscript body (move to the system fields)

### Format & files
- [ ] English; author-date citations consistent (Zotero/BibTeX)
- [ ] Tables/figures self-contained and anonymous (see `eursr-tables-figures`)

### Transparency & ethics
- [ ] **Data Availability Statement** drafted (archive/provider + version + access condition)
- [ ] **Replication package** assembled (statistical/computational) or exemption noted (qualitative)
- [ ] Not under review elsewhere; prior appearances disclosed

## Avoidable returns at the ESR desk

| Trip-wire | Consequence | Fix before upload |
|-----------|-------------|-------------------|
| Author names / identifying acknowledgments in the file | anonymity broken | strip them; use system fields |
| "in our prior study" wording | de-anonymizes the author | neutralize to "in a prior study" |
| Endnotes/references left out of word count | over the target on recount | count text + endnotes + references |
| No / vague Data Availability Statement | desk return under policy | name archive, version, access condition |
| Statistical paper, no package plan | stalls at conditional acceptance | assemble the package now |

## Worked micro-example (illustrative)

An author preps a comparative panel paper for ScholarOne upload.

```
Body + endnotes + references: 8,140 words → near ~8,000; brief justification added for the extra
Abstract: 192 words, no institutions named → within ≤200
Anonymity sweep: 4 self-citations reworded; acknowledgments removed; document properties cleared
DAS: ESS open + register via DUA, code provided → drafted
Package: master.R + harmonization + README + seed=2026, deposited on Zenodo (statistical → not exempt)
```

Caps verified on a recount including endnotes and references, a clean anonymity sweep, and the data
statement plus package ready — the most common avoidable returns pre-empted before upload.

## Editor pushback → ESR-specific fix

- *"We could identify the authors."* → Re-run the anonymity sweep on wording, acknowledgments, funding
  lines, and metadata; identifiers belong only in the ScholarOne fields.
- *"Over length."* → Recount with endnotes and references; prune citation strings and endnotes, or argue
  the contribution justifies the length (hand to `eursr-writing-style`).
- *"Data statement insufficient."* → Name the archive/provider, data version, and exact access condition
  (hand to `eursr-transparency-and-data`).

## Calibration anchors

- **Anonymity is the highest-frequency failure.** At a double-blind journal, an under-anonymized file is
  the most common avoidable cause of a return.
- **Endnotes and references count.** ESR's target includes them — budget for them early.
- **The DAS and package are gating, not optional.** A required data statement and (for statistical work)
  a replication package are part of the submission posture; treat volatile dates/figures as provisional
  and verify live.

## Anti-patterns

- Leaving author names, affiliations, or identifying acknowledgments in the manuscript
- Treating endnotes/references as outside the word count — they count toward ~8,000
- Abstract over 200 words
- A missing or vague Data Availability Statement
- Submitting elsewhere while under ESR review

## Output format

```
【Type】Article (~8,000) / Comment-Reply / Data-Brief — cap met or length justified? [Y/N]
【Anonymous】no identifiers + self-refs neutralized + metadata clean? [Y/N]
【Abstract】word count (≤200), non-identifying?
【Style】English + author-date consistent? [Y/N]
【DAS + package】statement drafted + package ready (or exemption noted)? [Y/N]
【Next】await decision → eursr-rebuttal on R&R
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official ESR / OUP / ECSR URLs behind every fact in this pack
