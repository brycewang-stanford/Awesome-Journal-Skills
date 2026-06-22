---
name: humrel-submission
description: Use when running the final pre-submission preflight for Human Relations (HR) via ScholarOne — anonymization, the 13k word cap, SAGE Harvard style, abstract/keywords, AI and data-transparency declarations. Final checks; it does not draft content.
---

# Submission Preflight (humrel-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on ScholarOne
- Unsure which files, declarations, and format the HR submission expects
- Confirming the manuscript is fully anonymized for double-anonymous review
- Checking length, abstract, keywords, and SAGE Harvard compliance

## Process facts (source map refreshed 2026-06; re-confirm on the official pages)

- HR is published by **SAGE for the Tavistock Institute of Human Relations** (founded 1947, monthly). Submission is through **ScholarOne / ManuscriptCentral** (mc.manuscriptcentral.com/hr).
- **Review model: double-anonymous.** The manuscript must contain no author names or identifying details and no links to external websites that could reveal authorship.
- **Length: 13,000 words total**, including references and appendices (检索于 2026-06；以官网为准).
- **Abstract: 100–200 words**, jargon-free, stating the topic/question, approach, and theoretical contribution; **keywords** as searchable key phrases.
- **Referencing: SAGE Harvard** (author-date) (检索于 2026-06；以官网为准).
- **Editorial scoping screen before full review:** "suitable data are a necessary but not sufficient feature to get to full peer review" — the theoretical contribution and HR fit must be legible up front. Article types: original empirical, theory-development, and intervention pieces; **critical/analytical reviews are accepted only through the annual special-issue call**.
- **AI policy:** any AI use must be **declared at submission and detailed in the cover letter**; AI is permitted only for copy-editing/proofing — using it otherwise, or undisclosed, is grounds for rejection/retraction.
- **Data transparency matrix:** if multiple papers draw on the same dataset, declare them and supply a matrix of which variables/quotations each uses; violation is grounds for rejection.
- Manuscripts are checked with **iThenticate/CrossCheck** for prior publication; HR follows **COPE** standards.
- Co-Editors-in-Chief: **Smriti Anand and Penny Dick** (verified 2026-06-22 via the journal editorial-team page; re-verify before submission) — address the cover letter to the editors, not a named individual unless verified.

## Preflight checklist

### Anonymization (double-anonymous)
- [ ] No author names, affiliations, or identifying acknowledgements anywhere in the manuscript
- [ ] Self-citations phrased neutrally (no "in our earlier work")
- [ ] No live URLs, no identifying field-site/organization names, no grant numbers that reveal authorship
- [ ] A separate (non-anonymized) title page uploaded as its own file, per portal fields

### Format & style
- [ ] Total length **≤13,000 words** including references and appendices
- [ ] **Abstract 100–200 words**, jargon-free, naming the theoretical contribution; key-phrase keywords supplied
- [ ] References in **SAGE Harvard** (author-date), consistent in-text and in the list
- [ ] Exhibits legible, anonymized, and within the word budget

### Declarations & files (ScholarOne)
- [ ] Cover letter to the editors: the contribution, HR fit, and **AI-use declaration** (if any)
- [ ] Data transparency matrix attached if the dataset spans multiple papers
- [ ] Article type selected correctly (do not submit a stand-alone review outside the special-issue call)
- [ ] Ethics/COPE compliance confirmed; not under review elsewhere; AI not listed as an author

## Anti-patterns

- Leaving author-identifying traces in a double-anonymous submission (the most common desk return)
- Exceeding 13k words and assuming an appendix is "free"
- A cover letter that describes the topic but not the *theoretical contribution* — a scoping-screen risk
- Submitting a stand-alone critical review outside the annual special-issue call
- Undisclosed AI use, or AI use beyond copy-editing
- Inconsistent or non-SAGE-Harvard references

## Output format

```text
【Journal】Human Relations
【Skill】humrel-submission
【Anonymization】no author/site/grant tells; separate title page? [Y/N]
【Length】≤13,000 words incl. refs + appendices? [Y/N]
【Abstract】100–200 words + key-phrase keywords? [Y/N]
【Style】SAGE Harvard references consistent? [Y/N]
【Declarations】AI use declared; data matrix if needed; correct article type? [Y/N]
【Next step】submit via ScholarOne → humrel-review-process for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — submission self-check
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — lightweight manuscript scaffold
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official URLs and volatile facts
