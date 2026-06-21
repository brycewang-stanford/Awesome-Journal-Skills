---
name: revedres-transparency-and-reproducibility
description: Use when settling coding reliability, open materials, PRISMA/MARS reporting, and a reproducible meta-analysis for a Review of Educational Research (RER) manuscript. Makes the review auditable and re-runnable; it does not run the substantive robustness analyses (revedres-comprehensiveness-and-balance) or design the exhibits (revedres-tables-figures).
---

# Transparency & Reproducibility (revedres-transparency-and-reproducibility)

## When to trigger

- The analysis is done and you must make the review auditable and re-runnable
- Coding reliability has not been quantified or reported
- You have not decided what search files, codebook, data, or scripts to share
- A reviewer is likely to ask "could someone reproduce this synthesis from what you report?"

## Why transparency IS the contribution at RER

Because RER reviews are **submitted and peer-reviewed** (not invited), a reader cannot take the synthesis on the author's authority — they must be able to **check it**. The credibility of a systematic review or meta-analysis is exactly the credibility of its **process documentation**: the search, the screening, the coding, and the analysis must be reported so completely that an independent reader could, in principle, re-run them and land in the same place. This is not an appendix afterthought; it is the spine of the review's claim to be *systematic*.

## Reporting standards RER points to

RER directs authors of systematic reviews and meta-analyses to specific reporting standards (检索于 2026-06；以官网为准):

- **PRISMA** — the systematic-review/meta-analysis reporting checklist and flow diagram. Report against every applicable item; include the flow diagram (see `revedres-tables-figures`).
- **APA "Reporting Standards for Research in Psychology"** (the JARS family, incl. **MARS** for meta-analyses) — RER's submission guidance cites the *American Psychologist* reporting-standards article. Use MARS to ensure the meta-analysis reports its eligibility, search, coding, effect-size metric, model, and heterogeneity/bias analyses completely.
- **PRISMA-P** for the protocol (see `revedres-proposal-and-commissioning`); **PROSPERO/OSF** registration cited.

## Coding reliability: report it, don't assert it

1. **Double-code a defined share** of studies (or all), independently.
2. **Quantify agreement** with the appropriate statistic — Cohen's/Fleiss' κ for categorical codes, ICC for continuous extractions — and **report the value**, not just "two coders agreed."
3. **State conflict resolution** (consensus, third coder) and re-check after disagreements.
4. Provide the **codebook** so a reader knows exactly what was coded and how.

## Open materials: make the synthesis re-runnable

- **Share the search artifacts**: full strings per database, dates, and the screening decisions/PRISMA counts.
- **Share the coding dataset and codebook** (de-identified as needed) on OSF or a repository, with a DOI.
- **Share the analysis code** (R `metafor`/`meta`, Stata `meta`, or Python) so the pooled estimates, moderators, and bias diagnostics are reproducible from the shared data.
- **Distinguish preregistered from exploratory** analyses, and flag/justify every deviation from the protocol.
- Note: RER publishes no original empirical data of *yours*; the open-materials obligation is on the **review's own** search, coding, and synthesis — your reproducible contribution.

## Checklist

- [ ] PRISMA checklist + flow diagram completed (systematic/meta)
- [ ] MARS / APA reporting standards walked for a meta-analysis
- [ ] Protocol registration (PROSPERO/OSF) cited; deviations flagged and justified
- [ ] Inter-coder reliability quantified (κ/ICC) and reported, not asserted
- [ ] Codebook included; conflict-resolution procedure stated
- [ ] Search strings, dates, and screening counts reported in full
- [ ] Coding dataset + analysis code shared (OSF/repository, with DOI) where possible
- [ ] Preregistered vs. exploratory analyses clearly distinguished

## Anti-patterns

- "Two coders agreed" with no κ/ICC value (unauditable reliability)
- A meta-analysis whose model, weights, or effect-size metric a reader cannot reconstruct
- Search strings paraphrased, not reported verbatim per database
- Silent deviations from the registered protocol
- Treating open materials as optional polish rather than the basis of the systematic claim
- Sharing nothing because "it's only a review" — the review's own process is the data

## Output format

```
【PRISMA】checklist + flow complete? Y/N
【MARS/JARS】meta-analysis reporting standards walked? Y/N
【Registration】PROSPERO/OSF cited; deviations flagged? Y/N
【Coder reliability】κ/ICC value reported = <value>; conflict resolution stated? Y/N
【Codebook】included? Y/N
【Search artifacts】strings + dates + screening counts reported in full? Y/N
【Open materials】dataset + code shared (DOI)? Y/N
【Preregistered vs exploratory】distinguished? Y/N
【Next step】→ revedres-editor-strategy (scope negotiation + reviewer expectations)
```
