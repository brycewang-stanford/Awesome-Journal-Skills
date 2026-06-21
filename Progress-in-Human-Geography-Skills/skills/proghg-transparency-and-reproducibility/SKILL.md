---
name: proghg-transparency-and-reproducibility
description: Use when documenting the scholarly apparatus, positionality, and coverage/search account of a Progress in Human Geography (PiHG) review under qualitative and critical-geography norms (not PRISMA tallies). Builds the transparency and reflexivity record; it does not gather the literature (proghg-literature-synthesis) or appraise individual works (proghg-comprehensiveness-and-balance).
---

# Transparency & Reflexivity for a Review (proghg-transparency-and-reproducibility)

## When to trigger

- The synthesis is settled and you must show *how* the literature was read and selected, and *from where*
- A referee is likely to ask "how did you decide what to include?" or "from what standpoint do you read this?"
- You want the apparatus and positionality to pre-empt the predictable "you omit literature X" or "this is partisan" pushback
- You are unsure what "transparency" means for a critical review that runs no empirical analysis

## What "transparency" means in a critical review with no primary data

A PiHG review reports **no new empirical data of its own**, so the usual replication-package machinery (raw data, estimation code, a reproducibility README of *your* analysis) does not apply to the review's claims. PiHG sits in a **qualitative / critical-geography tradition**, so transparency is **scholarly apparatus and reflexivity**, *not* a PRISMA flow tally. It bites on three things you *do* produce:

1. **Scholarly apparatus** — accurate, complete citation and attribution so a reader can trace every claim about the literature to its source.
2. **Positionality / reflexivity** — a brief, honest account of the standpoint from which you read the field, where your theoretical and political commitments shape the appraisal. This is *expected* in critical human geography, not optional.
3. **A coverage account** — a short narrative of how you gathered and selected the literature (the saturation log from `proghg-literature-synthesis`), so "comprehensive" is a defensible claim rather than a boast.

Distinguish this from primary-research reproducibility: you are not defending an identification strategy of your own (there is none); you are making your *reading* of others' work traceable and your *standpoint* explicit.

## The coverage account (narrative, not PRISMA-by-default)

Carry forward the saturation log into a brief, sharable record. A *formal PRISMA flow is usually inappropriate* for a critical review — PiHG is not a systematic-review tally journal — but a transparent narrative of the search is increasingly expected:

| Element | What to document |
|---------|------------------|
| Databases & dates | Web of Science, Scopus, GeoBase, Google Scholar — with search dates |
| Search terms & traditions | keyword strings *and* the theoretical-tradition names swept |
| Selection logic | how you decided what to engage vs. cite-in-cluster vs. set aside, and why |
| Tradition coverage | how political-economic, feminist, poststructural, postcolonial, more-than-human, and quantitative work were captured |
| Prior reports | how the standing PiHG progress reports on the area were accounted for |
| Saturation | where forward/backward snowballing stopped yielding new must-cites |

Use a formal PRISMA flow **only** if the piece is explicitly a systematic review of a tractable evidence base; confirm whether the topic warrants it on the author pages (检索于 2026-06；以官网为准). For most PiHG reviews the narrative account is the right form.

## Positionality and ethics

- **State your standpoint briefly** where it shapes the appraisal — theoretical commitments, disciplinary location, and (where relevant) political stance. Reflexivity is a strength a referee expects, not a confession.
- **Attribute scrupulously.** Credit originators of concepts and turns; mis-attribution in a state-of-the-art review is a serious fault (and the reviewed authors may be your referees).
- **Follow publication ethics.** PiHG/SAGE follow **COPE** standards and expect adherence to **ICMJE**-style authorship and disclosure norms; declare funding, conflicts, and any AI-tool use, and ensure all listed authors meet authorship criteria (检索于 2026-06；以官网为准).

## Checklist

- [ ] Every claim about the literature traces to an accurate, complete citation
- [ ] Concept/turn attribution credits originators (reviewed authors may referee)
- [ ] Coverage account documented (databases, dates, terms/traditions, selection logic, saturation)
- [ ] Tradition coverage and prior PiHG reports accounted for in the search record
- [ ] Positionality / reflexivity stated briefly where the standpoint shapes the appraisal
- [ ] PRISMA used only if a genuine systematic review warrants it; otherwise a transparent narrative (format 待核实)
- [ ] COPE/ICMJE ethics met: funding, conflicts, AI-tool use disclosed; authorship criteria met
- [ ] Coverage account ready to pre-empt "why did you omit X?" and "is this partisan?" at review

## Anti-patterns

- Claiming "comprehensive coverage" with no documented search to back it
- Importing primary-research replication machinery for claims the review does not itself estimate
- Forcing a PRISMA tally onto a critical/theoretical review where it does not fit (PiHG is not a systematic-review journal)
- Hiding the author's standpoint where it plainly shapes the reading (reflexivity is expected here)
- Mis-attributing a concept or turn to a popularizer over its originator
- Skipping COPE/ICMJE disclosures (funding, conflicts, AI use)

## Output format

```text
【Apparatus】every literature claim traces to a complete, accurate citation? Y/N
【Attribution】concepts/turns credited to originators? Y/N
【Coverage account】databases + dates + terms/traditions + selection logic + saturation documented? Y/N
【Tradition + prior reports】tradition coverage and prior PiHG reports recorded? Y/N
【Positionality】standpoint stated where it shapes the appraisal? Y/N
【PRISMA】formal flow only if a systematic review warrants it; else narrative? Y/N · 待核实
【Ethics】COPE/ICMJE — funding, conflicts, AI use disclosed; authorship met? Y/N
【Next step】→ proghg-editor-strategy (commissioned report vs. submitted review) → proghg-submission
```
