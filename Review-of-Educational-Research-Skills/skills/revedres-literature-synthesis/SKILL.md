---
name: revedres-literature-synthesis
description: Use when executing the systematic search, screening to a PRISMA flow, and extracting data for a Review of Educational Research (RER) review or meta-analysis. Builds the documented evidence corpus; it does not impose the conceptual spine (revedres-organizing-framework) or run robustness/risk-of-bias appraisal (revedres-comprehensiveness-and-balance).
---

# Systematic Search & Synthesis (revedres-literature-synthesis)

## When to trigger

- The protocol is fixed and it is time to search the literature exhaustively
- Searching feels ad hoc; you cannot yet report a reproducible PRISMA flow
- You have hundreds of records and need a defensible screening trail
- A reviewer at RER is likely to ask "why did you omit study X / database Y?"

## Search to a documented PRISMA flow, not to memory

An RER systematic review's credibility rests on a reader's belief that you found **everything that meets your criteria** — and can prove it. Execute the protocol, logging every number for the **PRISMA flow diagram** (identification → screening → eligibility → included).

1. **Run the registered search.** Search every database in the protocol (ERIC, PsycINFO, Education Source, Web of Science, Scopus, ProQuest Dissertations) with the recorded strings, plus grey-literature and hand-searches of key journals. Record hits per source and the search date.
2. **Deduplicate and log.** Report records identified, duplicates removed, and records screened — exact counts.
3. **Dual independent screening.** Two screeners at title/abstract, then full-text, against the eligibility criteria; record exclusions **with reasons** at full-text (required by PRISMA). Report inter-rater reliability (Cohen's κ or % agreement) and how conflicts were resolved.
4. **Supplement to saturation.** Backward (reference lists of included studies) and forward (who cites them) snowballing; ask whether new searches still surface eligible studies. Document where they stop.
5. **Extract into a structured dataset.** Apply the codebook to every included study — this is the raw material for the framework, the tables, and the meta-analysis.

## From extraction to synthesis (not summary)

Summarizing is restating each study; **synthesizing** is making the studies answer your question together. Maintain a coding dataset as you extract:

| Column | What to capture |
|--------|-----------------|
| Study | author–year; the included report (watch for multiple reports of one sample) |
| Sample/context | learners, setting, grade/level, country — for moderator analysis and scope claims |
| Design | RCT / quasi-experiment / correlational / qualitative — for risk-of-bias and weighting |
| Construct/measure | exactly what was measured (so non-commensurable outcomes are not pooled) |
| Effect / finding | effect size + variance (meta-analysis) or coded finding (narrative synthesis) |
| Risk of bias | your appraisal on the a-priori tool (you do not re-run the study; you judge it) |
| Dependencies | shared samples / multiple effects per study (drives the variance model) |

This dataset feeds the organizing framework, the forest plot and coding tables, and the even-handed treatment of conflicting evidence. You **appraise** the primary studies (you are the field's reviewer-of-record); you do **not** re-collect their data.

## Education-specific search hazards

The education literature is scattered across disciplines and document types, which creates predictable holes:

- **Cross-disciplinary indexing.** Relevant work hides in psychology (PsycINFO), economics (EconLit/NBER), sociology, and policy databases — searching only ERIC misses it. Map your constructs to each field's vocabulary.
- **Grey literature is large and consequential.** Dissertations (ProQuest), technical and foundation reports, and What Works Clearinghouse / IES products carry many null and small-sample results; omitting them biases pooled effects upward.
- **Terminology drift.** The same construct is named differently across eras and subfields (e.g. "self-regulation" vs. "metacognition" vs. "executive function") — build a thesaurus of synonyms into the search string.
- **Multiple reports of one study.** Program evaluations spawn several papers on the same sample; collapse them to one unit or model the dependency, or you double-count.

Document how you handled each, so a reviewer sees the gaps were anticipated, not missed.

## Checklist

- [ ] Every protocol database searched with recorded strings + search date
- [ ] Records identified / duplicates / screened / excluded-with-reasons / included all counted for PRISMA
- [ ] Dual independent screening; inter-rater reliability reported; conflict resolution stated
- [ ] Backward + forward snowballing run to saturation and documented
- [ ] Grey literature / dissertations handled per protocol (and publication-bias implications noted)
- [ ] Codebook applied uniformly; multiple-reports-of-one-sample and dependent effects flagged
- [ ] Non-commensurable outcomes flagged (not pooled into a false common effect)
- [ ] No eligible study or relevant database an informed reviewer could name as missing

## Anti-patterns

- Searching from memory or one database (predictable, fatal coverage gaps at RER)
- A PRISMA diagram whose numbers do not reconcile (a red flag reviewers check)
- Single-screener inclusion with no reliability statistic
- Excluding grey literature without acknowledging the publication-bias risk it creates
- Pooling outcomes that measure different constructs into one "effect of X"
- Re-analyzing or "correcting" a primary study's raw data — you appraise, you do not re-collect

## Output format

```
【Databases + date】<sources searched, search date>
【PRISMA counts】identified / dedup / screened / full-text / excluded-w-reasons / included
【Screening reliability】κ or % agreement; conflicts resolved by <method>
【Snowballing】backward + forward to saturation? Y/N
【Grey literature】included? Y/N — publication-bias implication noted? Y/N
【Coding dataset】codebook applied; dependent effects + shared samples flagged? Y/N
【Coverage risks】<any eligible study/database a reviewer could name as missing>
【Next step】→ revedres-organizing-framework (impose the conceptual spine on the corpus)
```
