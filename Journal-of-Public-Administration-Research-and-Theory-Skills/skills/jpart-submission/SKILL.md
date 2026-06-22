---
name: jpart-submission
description: Use when running the final pre-submission preflight for the Journal of Public Administration Research and Theory (JPART) via Editorial Express — word/format limits, double-blind anonymization, OUP author-date style, keywords, Data Availability Statement, and declarations. Final checks; it does not draft content.
---

# Submission Preflight (jpart-submission)

The last check before pressing submit on **Editorial Express**. JPART is **double-blind**, so the most
common avoidable failure is an under-anonymized manuscript; the second is forgetting that the word cap
*includes the abstract, tables, and references*. Verify volatile specifics on the official page first.

## When to trigger

- "Submitting tomorrow" — last pass before upload
- Unsure which files/metadata Editorial Express expects
- Confirming the word cap is met and the manuscript is properly anonymized

## Process facts (verify volatile items on the official page)

- **Owner / publisher:** Public Management Research Association (PMRA) / Oxford University Press (OUP).
- **Editors (re-verified 2026-06-22):** Editor-in-Chief **Ole Helby Petersen** and Co-Editor **Kim Sass
  Mikkelsen** (both Roskilde University), serving a four-year term; re-verify the masthead on the live
  Editorial Board page before relying on it.
- **Portal:** **Editorial Express** (`editorialexpress.com/jpart`). Submit one PDF containing title,
  abstract, text, references, all tables/figures, plus any appendices.
- **Review model:** **double-blind** — anonymize the manuscript; identifying info (name, funding,
  acknowledgments) goes on the **cover sheet** only.
- **Length:** **no longer than ~12,000 words, *including* abstract, tables, and references** (检索于
  2026-06-22；以官网为准).
- **Abstract:** state **theoretical approach, method and data, results, and implications for theory**
  (no fixed word limit stated — 待核实).
- **Keywords:** **3–5**; the first three should indicate **theory, research theme, and method**.
- **Style:** OUP **author-date**; alphabetical reference list **with DOIs**.
- **Data policy:** authors must, where ethically possible, **publicly release data and code** as a
  condition of publication, with a mandatory **Data Availability Statement** (see
  `jpart-transparency-and-data`).
- **Fee:** **no submission fee** (re-verified 2026-06-22); open-access publication requires an OUP-handled
  APC after acceptance (current figure 待核实 — confirm on the OUP page if choosing open access).
- **ORCID:** not confirmed as required on the guidelines page (待核实).

## Preflight checklist

### Length & format
- [ ] Manuscript ≤ ~12,000 words *including abstract, tables, and references*
- [ ] Abstract states theory → method/data → results → implications for theory
- [ ] 3–5 keywords; first three signal theory / research theme / method
- [ ] OUP author-date citations; reference list alphabetical with DOIs

### Anonymity (double-blind)
- [ ] No author names, affiliations, funding, or acknowledgments in the manuscript
- [ ] Self-citations phrased in the third person; no "as we showed in…"
- [ ] Identifying **file metadata stripped** (document properties, comments)
- [ ] Separate **cover sheet** prepared with name/funding/acknowledgments
- [ ] Pre-registration report blinded (hyperlinks anonymized) or placed on the cover sheet

### Transparency & compliance
- [ ] **Data Availability Statement** drafted; data + code staged for public release
- [ ] Ethics / IRB / human-subjects compliance addressed
- [ ] Original work; not under review elsewhere
- [ ] Online supplement/appendix uploaded if used

## Anti-patterns

- Leaving author identifiers in the text, funding lines, or file metadata (breaks double-blind)
- Forgetting the word cap counts the abstract, tables, *and* references (a common overrun)
- An abstract that omits the theoretical approach or implications for theory
- Submitting without a Data Availability Statement / public data-and-code plan
- Budgeting a submission fee that is not charged (verify; the APC applies only to open access)

## Output format

```
【Length】≤ ~12,000 words incl. abstract/tables/references? [Y/N]
【Anonymized】text + self-refs + file metadata clean; cover sheet separate? [Y/N]
【Abstract】theory → method/data → results → implications for theory? [Y/N]
【Keywords】3-5, theory/theme/method first? [Y/N]
【OUP author-date + DOIs】[Y/N]
【Data Availability Statement + public package】[Y/N]
【Next】await decision → jpart-rebuttal on R&R
```

## Supplementary resources

- [`./templates/checklist.md`](templates/checklist.md) — full pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reference managers, anonymization, repro tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JPART URLs behind every fact in this pack
