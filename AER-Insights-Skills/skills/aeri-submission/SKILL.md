---
name: aeri-submission
description: Use when running the final pre-submission preflight for American Economic Review: Insights (AER: Insights) via the AEA online submission system — the word-count and exhibit-count gates, abstract limit, fees, JEL codes, blinding, and the AEA Data and Code Availability Policy. Final checks; it does not draft content.
---

# Submission Preflight (aeri-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the AEA portal
- Verifying the word count and exhibit count clear the **auto-return** gates
- Unsure which files, fees, and declarations the AEA system expects
- Confirming double-blind anonymization and the data/code statement

## Process facts (检索于 2026-06；以官网为准)

- AER: Insights is an **AEA** journal (founded 2019) for **short, single-idea** general-interest papers. Submission is through the **AEA online submission system**.
- **Hard length gate:** main text **≤7,000 words with no exhibits; each exhibit subtracts 200 words; maximum five exhibits** (figures + tables combined), **each ≤1 page**. The word count includes body, footnotes, endnotes, and in-paper appendices; it **excludes** title, authors, abstract, acknowledgement footnote, references, exhibits, and the Supplemental Appendix. **Papers over the word or exhibit limit are returned unreviewed.**
- **Abstract: ≤100 words.**
- **Submission fee (volatile):** AEA members — high-income US$200 / middle-income US$100 / low-income US$0; nonmembers — US$300 / US$200 / US$0; re-confirm current amounts. **Publication fee** (volatile): about **US$15 per typeset page** at acceptance.
- **JEL codes** required; **double-blind** review, so the submitted manuscript must be **anonymized** (no author names, no identifying acknowledgements/self-citations that unmask).
- **Data and code:** submission must comply with the **AEA Data and Code Availability Policy**; data, code, and documentation sufficient for replication are required before acceptance, verified by the **AEA Data Editor** (deposit to the AEA Data and Code Repository / openICPSR). See [`aeri-replication-package`](../aeri-replication-package/SKILL.md).

## Preflight checklist

### Length & format (the auto-return gates)
- [ ] Main text **≤ 7,000 − 200 × (#exhibits)** words, counted per the AEA scope rules above
- [ ] **≤5 exhibits** (figures + tables), **each ≤1 page**
- [ ] **Abstract ≤100 words**
- [ ] **No asterisks/boldface for significance**; SEs / confidence sets reported
- [ ] Supplemental Appendix carries everything pushed out of the main text

### Anonymization & metadata
- [ ] Manuscript **anonymized** for double-blind review (names, acknowledgements, identifying self-cites)
- [ ] **JEL codes** and keywords provided
- [ ] Title page / metadata entered as the portal requires

### Files, fees & declarations
- [ ] Main manuscript PDF + Supplemental Appendix uploaded as the system expects
- [ ] **Submission fee** ready (correct member/income band); current amount re-confirmed
- [ ] **AEA Data and Code Availability Policy** acknowledged; data/code plan ready
- [ ] Disclosure statement; AI **not** listed as an author; not under review elsewhere

## Counting words the way the AEA counts them

The auto-return gate is enforced on a specific scope, so count it correctly:

- **Include:** the main body, footnotes, endnotes, and **in-paper appendices**.
- **Exclude:** title, author names, abstract, the acknowledgement footnote, the reference list, the
  exhibits themselves, and the Supplemental Appendix.
- **Then subtract 200 words per exhibit** from the 7,000 ceiling: a paper with five exhibits has a 6,000-word
  main-text budget. A common mistake is counting only the body and forgetting footnotes/in-paper appendices,
  then discovering the true count is over at the portal.

Reconcile this with [`aeri-writing-style`](../aeri-writing-style/SKILL.md) (cutting to the cap) and
[`aeri-tables-figures`](../aeri-tables-figures/SKILL.md) (the exhibit budget) before you reach the portal.

## Anti-patterns

- Submitting over the **word or exhibit cap** (auto-return without review)
- Abstract over 100 words; exhibits over one page
- Forgetting to anonymize for the double-blind process
- Significance asterisks/boldface in exhibits
- Treating the data/code policy as a post-acceptance afterthought

## Output format

```
【Word count】main text = __ ; cap = 7000 − 200×__ = __ ; under? [Y/N]
【Exhibits】__ / 5, each ≤1 page? [Y/N]
【Abstract】__ words (≤100?) [Y/N]
【Anonymized】double-blind ready? [Y/N]
【JEL + keywords】provided? [Y/N]
【Fee + data/code】fee ready; AEA data policy acknowledged? [Y/N]
【Next step】submit via AEA portal → aeri-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA / AER: Insights URLs behind every fact
