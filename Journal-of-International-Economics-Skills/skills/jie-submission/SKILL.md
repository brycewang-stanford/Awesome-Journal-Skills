---
name: jie-submission
description: Use when running the final pre-submission preflight for the Journal of International Economics (JIE) via Elsevier's Editorial Manager — the non-refundable submission fee, the regular/short/PRP Article Type choice, the 150-word abstract, 1-7 keywords, suggesting a fitting (Co-)Editor, and reference completeness. Final checks; it does not draft content.
---

# Submission Preflight (jie-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on Editorial Manager
- Deciding between a regular, short, or Prior Review Process (PRP) submission
- Confirming the abstract, keywords, and reference completeness are JIE-compliant
- Making sure the submission fee and editor-suggestion steps are handled

## Process facts (verified 2026-06-20; editors + fee re-verified 2026-06-22; re-confirm on the official guide)

- JIE is published by **Elsevier**; submission is through **Editorial Manager**. The official board lists **Editors Martin Uribe (Columbia)** and **Costas Arkolakis (Yale)** (re-verified 2026-06-22), with Co-Editors spanning trade and international macro/finance; re-confirm the masthead before naming an editor.
- There is a **non-refundable submission fee of USD 190 / EUR 169.20 / JPY 20,660**, reduced to **USD 95 when every author is a PhD student**; VAT is added for authors in relevant European countries. Fee revenue funds JIE summer schools and the biennial **Jagdish Bhagwati Award** for the best paper in the journal.
- **Submission types**: regular, **Short Paper**, or **PRP**. Short Papers are capped at **6,000 words** and **5 exhibits**, must be self-contained, and require a separate word-count PDF. For PRP, attach the editorial decision letter and all referee reports from a rejection at **AER, Econometrica, JPE, QJE, or Review of Economic Studies** and select **'PRP' from the Article Type menu**; there is no extra fee versus a regular submission.
- **Abstract ≤ 150 words**, concise/factual, single paragraph, references avoided (cite author(s)/year(s) only if essential). Provide **1-7 keywords**.
- Authors are advised to **suggest an Editor or Co-Editor whose profile fits** the paper (trade vs international macro/finance).
- Reference style is applied by Elsevier **at the proof stage**; submit in any consistent style as long as required elements are present (DOIs encouraged).
- JIE follows a **single anonymized** review process; suitable submissions are typically sent to a minimum of two reviewers. Do not assert a regular-paper word cap from the Short Paper rule.

## Preflight checklist

### Article Type & fit
- [ ] Type chosen: **regular / Short Paper / PRP** (PRP only if you hold a qualifying AER/Econometrica/JPE/QJE/REStud letter + reports)
- [ ] If PRP: decision letter and referee reports attached; 'PRP' selected as Article Type
- [ ] If Short Paper: ≤6,000 words, ≤5 exhibits, self-contained, word-count PDF prepared
- [ ] Suggested **Editor or Co-Editor** whose profile matches the paper's trade or macro/finance focus

### Format & style
- [ ] Abstract is a single factual paragraph, **≤ 150 words**, references avoided
- [ ] **1-7 keywords** provided; field-discoverable
- [ ] References complete (author names, title, year, volume, article number/pages); **DOIs** added where available
- [ ] Tables and figures numbered, called out in order, with self-contained notes
- [ ] JEL codes prepared only if requested by the live submission system

### Files & declarations
- [ ] Manuscript file plus any online appendix staged for Editorial Manager
- [ ] Cover letter (concise: question, method, headline result, trade-vs-macro fit, suggested editor)
- [ ] Replication code + data staged for the JIE secure repository (see jie-replication-and-data-policy)
- [ ] Conflict-of-interest / funding disclosures prepared; confirmed not under review elsewhere

### Fee
- [ ] Submission fee budgeted: **USD 190 / EUR 169.20 / JPY 20,660** (USD 95 if all authors are PhD students); VAT noted for European authors

## Last-mile sanity pass before you press submit

Three errors cause the most avoidable bounces, all fixable in minutes: editor mismatch (a trade paper with no suggested trade editor risks routing to a macro editor, and vice versa — set the suggestion to your scope half); a PRP misfire (selecting PRP without a qualifying AER/Econometrica/JPE/QJE/REStud letter plus the full reports, favorable and critical); and an over-long or citation-laden abstract (the cap is 150 words, references avoided). Re-confirm the fee amount, editor roster, and upload flow against the live author guide before relying on them.

## Anti-patterns

- Treating the fee as refundable or skipping it (submission will not proceed)
- Selecting PRP without a qualifying letter from one of the five named journals
- A 250-word, citation-laden abstract (cap is 150 words, references avoided)
- Not suggesting an editor, so trade work lands with a macro editor or vice versa
- Applying the Short Paper cap to a regular submission, or selecting Short Paper without the word-count PDF

## Output format

```
【Article Type】regular / Short Paper / PRP (PRP letter held? Y/N)
【Editor suggested】Editor or Co-Editor matched to trade / macro-finance? [Y/N]
【Abstract】≤150 words, factual, no references? [Y/N]
【Keywords】1-7 provided? [Y/N]
【References】required elements + DOIs present? [Y/N]
【Fee】USD 190 / 95 (all-PhD) budgeted; VAT noted? [Y/N]
【Replication】code+data staged for JIE secure repo? [Y/N]
【Next step】jie-review-process → on R&R, jie-rebuttal
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — trade & international macro/finance data and Stata/R/Python/Dynare toolkits
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JIE / Elsevier URLs behind every fact in this pack
