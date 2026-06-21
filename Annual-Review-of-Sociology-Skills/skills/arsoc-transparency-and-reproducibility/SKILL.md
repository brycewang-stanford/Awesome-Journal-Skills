---
name: arsoc-transparency-and-reproducibility
description: Use when documenting the coverage account of an Annual Review of Sociology (ARSoc) review and the transparency obligations of any systematic-review search or meta-analysis the review itself contains. Builds the search/selection record and the reproducibility plan; it does not gather the literature (arsoc-literature-synthesis) or appraise individual studies' designs (arsoc-comprehensiveness-and-balance).
---

# Transparency & Reproducibility for a Review (arsoc-transparency-and-reproducibility)

## When to trigger

- The synthesis is settled and you must show *how* the literature was searched and selected
- The review reports a quantitative synthesis (meta-analysis, meta-regression, citation analysis) of its own
- A Committee member or referee is likely to ask "how did you decide what to include?"
- You want the coverage account to pre-empt the predictable "you omit literature X" pushback

## What "transparency" means in a review with no primary data

An ARSoc review reports **no new data of its own**, so the usual replication-package machinery (raw data, estimation code, a reproducibility README of *your* analysis) does not apply to the review's claims about the world. Transparency instead bites on two things you *do* produce:

1. **The coverage account** — a documented, near-PRISMA-style record of how the literature was searched, screened, and selected. This is what makes "comprehensive" a verifiable claim rather than a boast.
2. **Any analysis the review itself runs** — if the review contributes a meta-analysis, a citation/bibliometric analysis, or a re-coded dataset of studies, *that* artefact must be reproducible and depositable like any quantitative work.

Distinguish the two clearly: you are not defending an identification strategy of your own (there is none); you are documenting how you found and weighed others' work, and reproducing any synthesis you actually computed.

## The coverage account (near-PRISMA, adapted for sociology)

Carry forward the saturation log from `arsoc-literature-synthesis` into a brief, sharable record:

| Element | What to document |
|---------|------------------|
| Databases & dates | Sociological Abstracts, Web of Science, Scopus, JSTOR, Google Scholar — with search dates |
| Search terms & traditions | keyword strings *and* the theoretical-tradition names swept |
| Inclusion / exclusion | what counted (years, methods/modes, languages, publication types) and what was excluded and why |
| Mode coverage | how qualitative, computational, demographic, and theoretical work were captured (not just quant) |
| Saturation | where forward/backward snowballing stopped yielding new must-cites |
| Counts | rough numbers screened vs. discussed, so "comprehensive" is auditable |

Sociology reviews are rarely strict PRISMA systematic reviews, but a *near*-PRISMA narrative of the search makes the coverage defensible and is increasingly expected. Confirm whether the topic warrants a formal PRISMA flow on the author pages (检索于 2026-06；以官网为准).

## When the review runs its own analysis

If the review contributes a meta-analysis or bibliometric study:

- **Deposit data + code** in a public repository (OSF, Dataverse, Zenodo) so the synthesis is reproducible; cite the DOI.
- **State the protocol:** inclusion criteria, effect-size extraction, coding rules, weighting, heterogeneity and publication-bias diagnostics.
- **Pool only commensurable studies** — never reduce qualitative or theoretical work to a spurious effect size (see `arsoc-tables-figures`).
- **Make the coding reproducible:** a second coder could re-derive your study-level codes from your codebook.

## Checklist

- [ ] Coverage account documented (databases, dates, terms, inclusion/exclusion, saturation, counts)
- [ ] Search captured qualitative, computational, demographic, and theoretical modes, not only quant
- [ ] Near-PRISMA narrative (or formal flow if warranted) prepared; format confirmed on author pages (volatile)
- [ ] Any meta-analysis/bibliometric analysis: data + code deposited with a citable DOI
- [ ] Synthesis protocol stated (inclusion, extraction, coding rules, weighting, bias diagnostics)
- [ ] Study-level coding reproducible from a documented codebook
- [ ] Only commensurable studies pooled into any quantitative synthesis
- [ ] Coverage account ready to pre-empt "why did you omit X?" at review

## Anti-patterns

- Claiming "comprehensive coverage" with no documented search to back it
- Importing primary-research replication machinery for claims the review does not itself estimate
- Treating a narrative review as exempt from any coverage account (the gap referees probe)
- Running a meta-analysis with no deposited data/code or no stated protocol
- Pooling incommensurable findings (qualitative, theoretical) into a single effect size
- Documenting only the quantitative search and silently dropping the qualitative/theoretical sweep

## Output format

```text
【Coverage account】databases + dates + terms + inclusion/exclusion + saturation + counts documented? Y/N
【Mode coverage】qual / computational / demographic / theoretical search documented? Y/N
【PRISMA】near-PRISMA narrative (or formal flow) prepared; format confirmed? Y/N · 待核实
【Own analysis】meta-analysis/bibliometrics deposited with DOI + protocol? Y/N · n/a
【Coding reproducibility】codebook lets a second coder re-derive codes? Y/N · n/a
【Pre-empt】coverage account answers "why omit X?" before review? Y/N
【Next step】→ arsoc-editor-strategy (scope + volume timeline) → arsoc-submission
```
