---
name: ors-submission
description: Use when running the final pre-submission preflight for an Operations Research (OR) manuscript — INFORMS Author Portal/ScholarOne, area selection, recommending Associate Editors and reviewers, soft double-anonymous anonymization, the mandatory contribution statement, page-tier limits, and the code/data deposit plan. Checks readiness to submit; it does not handle the post-decision response (ors-rebuttal).
---

# Pre-Submission Preflight (ors-submission)

## When to trigger

- "We're submitting this week" — the last check before hitting submit.
- Unsure what the INFORMS Author Portal / ScholarOne requires for *Operations Research*.
- Verifying area routing, anonymization, the contribution statement, and page limits.

> Always re-verify current limits and required files on the official OR
> submission-guidelines page and the Code and Data Disclosure Policy before submitting —
> specifics change. As of 2026-06-20 the key specs below were corroborated; items marked
> 待核实 / re-confirm should be checked on the live page.

## Verified OR specs (confirm current values)

- **Submission system:** ScholarOne Manuscripts via the **INFORMS Author Portal**.
- **Review model:** **soft double-anonymous** — omit author names from the submission;
  reviewers cannot see authors; the Area Editor and Associate Editor can; authors **can**
  see the handling **Area Editor's** name but not the AE or reviewers.
- **Area routing:** select the correct **editorial area** so it reaches the right Area
  Editor (confirm the current area list and Area Editors' Statements — 待核实 names).
- **Nominations:** recommend **3 Associate Editors** from the chosen area and suggest
  **5 reviewers**.
- **Contribution statement (since 1 June 2023):** cover letter must include a statement
  in **fewer than 500 words** on the novel, innovative, and rigorous original
  contribution to operations research.
- **Abstract:** **≤ 200 words**, text-only; **up to 3 keywords**.
- **Introduction:** must be **equation-free** (no equations or notation).
- **Length tiers (excl. references):** Focused Technical = **20 pages**;
  Context-and-Challenge = **20 pages**; regular = **30 pages**; lengthy generally
  **~40 pages**. E-companion (regular/lengthy) must **not be longer than the
  manuscript**; Context-and-Challenge papers have **no e-companion**.
- **Formatting:** 1.5-spaced, **11-point** font, **1-inch** margins; **PDF** at
  submission (source LaTeX/Word on acceptance); **LaTeX style files** provided;
  **author-year** citations.
- **Fees:** no submission/processing fee is *stated* in the official guidelines;
  the only fee is the optional **INFORMS Open Option** open-access fee (US$3,000,
  after acceptance). Re-verify on the live page before relying on it.

## Pre-submission checklist

### Anonymization (soft double-anonymous)

- [ ] Manuscript omits author names, affiliations, and acknowledgments
- [ ] Self-citations worded neutrally ("Norman (1977) shows ..."), not "our prior work"
- [ ] Prior conference version cited **anonymously**; disclosed in the cover letter
- [ ] File metadata/properties scrubbed of identity; file names carry no identifiers

### Article type, area & nominations

- [ ] Correct **manuscript type** chosen (Focused Technical / Context-and-Challenge / regular / lengthy)
- [ ] Correct **editorial area** selected (matches the contribution)
- [ ] **3 Associate Editors** recommended and **5 reviewers** suggested (non-conflicted)

### Format & files

- [ ] Abstract ≤ 200 words (text-only); **up to 3** keywords
- [ ] Introduction **equation-free**
- [ ] Within the **page tier** for the chosen type (excl. references); e-companion ≤ manuscript
- [ ] 1.5-spaced, 11-pt, 1-inch margins; PDF built and previewed; LaTeX style files used
- [ ] Author-year citations; reference list complete and consistent

### Cover letter & policies

- [ ] **Contribution statement < 500 words** included
- [ ] Prior conference version disclosed/linked; incremental contribution justified
- [ ] Code/data deposit prepared for the **ORJournal GitHub** workflow, **or** an
      **exemption requested with rationale** (confidential/licensed/non-public data or
      purely methodological paper)
- [ ] INFORMS **Generative AI Guidelines** followed and disclosed as required

## Anti-patterns

- Submitting to the wrong area, forcing a re-route and delay.
- Self-identifying language or a non-anonymized conference citation left in.
- Missing or over-length (≥500-word) contribution statement.
- Introduction with equations; abstract over 200 words.
- Exceeding the page tier by forgetting the e-companion length rule.
- No code/data deposit and no exemption requested where the policy applies.

## Output format

```
【Anonymization】pass / fix: [...]
【Type & area】type ...; area ...; 3 AEs + 5 reviewers listed?
【Format】abstract ≤200 / 3 keywords / equation-free intro / page tier: pass?
【Cover letter】contribution statement <500 words; conference disclosure: yes/no
【Reproducibility】ORJournal deposit ready or exemption requested?
【Next step】await decision → ors-review-process; on revision → ors-rebuttal
```

## Resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — OR/MS modeling languages, solvers, simulation/stochastic tools, and the ORJournal reproducibility workflow
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official INFORMS/OR URLs behind every verified fact in this pack (accessed 2026-06-20)
