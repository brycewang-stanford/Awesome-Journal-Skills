---
name: ppsych-literature-synthesis
description: Use when systematically gathering and synthesizing literature across psychology sub-areas for a Perspectives on Psychological Science (PoPS) integrative review, theoretical statement, or meta-science piece — coverage discipline, and for meta-science the systematic evidence about the field's practices. Builds the evidence corpus; it does not impose the analytical spine (ppsych-organizing-framework) or audit balance (ppsych-comprehensiveness-and-balance).
---

# Literature Synthesis (ppsych-literature-synthesis)

## When to trigger

- The topic/proposal is set and it is time to read across the relevant sub-areas thoroughly
- Reading feels unsystematic; you fear missing work a psychologist from an adjacent area would expect
- You have many papers but no way to weigh, compare, or reconcile their findings across paradigms
- For meta-science: you need systematic evidence *about the field's practices*, not just substantive findings

## Coverage discipline: read across areas, not one literature

A PoPS piece's credibility rests on the reader's belief that you read **across the relevant sub-areas**, not only your home paradigm — and PoPS reviewers are often drawn from the very areas being integrated, so siloing is noticed. Build coverage systematically:

1. **Seed set.** Start from the proposal's key references and each sub-area's canonical pieces.
2. **Forward + backward snowball.** Backward: every paper's reference list. Forward: who cites the seeds (Google Scholar / Scopus / Web of Science). Iterate until new searches stop turning up unseen important work (*saturation*).
3. **Database + keyword sweep.** Search **PsycINFO/APA PsycNet**, plus PubMed and discipline databases for adjacent fields (neuroscience, methods), by topic keywords **and** by the terms each sub-area uses for the same construct — different areas name the same phenomenon differently.
4. **Preprints + adjacent fields.** A current PoPS piece must include recent preprints (PsyArXiv) and the bordering literatures the argument draws on, or referees flag staleness and siloing.
5. **Saturation log.** Record when each sub-area's search stops yielding new must-cite work — your evidence of comprehensiveness for `ppsych-comprehensiveness-and-balance`.

## Meta-science: systematic evidence about the field's practices

If the piece is **meta-science** (about replication, reporting, power, bias, or methods *as practiced*), the "literature" includes the field's outputs as **data**: prevalence of a practice, distributions of statistics, registered-report rates, sharing rates. Treat the search as a **systematic protocol**:

- Pre-specify the sampling frame (journals, years, article filter) and inclusion/exclusion rules — ideally **preregistered** (see `ppsych-transparency-and-reproducibility`).
- Pilot and document the coding scheme (what counts as a preregistration, an open-data badge, an underpowered design).
- Report search dates, hit counts, and screening outcomes (a PRISMA-style flow) so a reader can audit the corpus.
- Plan double-coding and inter-rater reliability for any subjective extraction.

## From reading to synthesis (not summary)

Summarizing restates each paper; **synthesizing** makes papers from different areas *talk to each other*. Maintain an evidence matrix:

| Column | What to capture |
|--------|-----------------|
| Study | author–year, the result/claim you will cite it for |
| Sub-area / construct | which area + how it operationalizes the construct (so non-comparable work is not pooled) |
| Method/sample | design and sample (so you can weight credibility) |
| Finding | direction + magnitude (effect sizes/CIs where available) |
| Credibility | identification, power, replication status — your *appraisal* |
| Tension | which other studies/areas it agrees or conflicts with, and why |

This matrix feeds the organizing framework, the summary exhibits, and the even-handed treatment of controversies. You **appraise** the primary work; you do not re-run it (unless the piece *is* a meta-analysis with a superordinate message — then its data/code must be reproducible).

## Checklist

- [ ] Seed set drawn from each sub-area's canonical pieces + proposal references
- [ ] Forward and backward snowball iterated to saturation in every sub-area
- [ ] PsycINFO/PsycNet + adjacent databases swept by keyword **and** each area's construct terms
- [ ] Recent preprints (PsyArXiv) and bordering literatures included (no staleness, no silo)
- [ ] Saturation log records where each area's searches stopped yielding new must-cites
- [ ] Meta-science: sampling frame + coding scheme pre-specified (ideally preregistered); PRISMA-style flow
- [ ] Evidence matrix captures construct + method + finding + credibility + cross-area tension
- [ ] Non-comparable constructs flagged as such (not pooled into a false "the literature finds…")

## Anti-patterns

- Citing from one's home paradigm only (predictable cross-area gaps the integrated areas will spot)
- Summarizing paper-by-paper instead of synthesizing across areas
- Pooling studies that measure *different* constructs into one "the field finds…" claim
- Ignoring preprints (looks stale) or adjacent fields (looks siloed) in a *broad* journal
- Meta-science with an undocumented, unreplicable search — the reform critique applies to your own piece
- Re-running or "correcting" primary studies in a non-meta-analytic review — you appraise, you don't re-estimate

## Output format

```text
【Seed set】<canonical pieces per sub-area + proposal references>
【Snowball status】backward/forward iterated to saturation across areas? Y/N
【Databases swept】PsycINFO/PsycNet + adjacent — by keyword + construct terms? Y/N
【Preprints + adjacency】PsyArXiv + bordering literatures included? Y/N
【Meta-science protocol】sampling frame + coding scheme pre-specified; PRISMA flow? Y/N · N/A
【Saturation evidence】<where searches stopped yielding new must-cites>
【Evidence matrix】rows ready with construct / method / finding / appraisal / tension? Y/N
【Coverage risks】<any area/author an omission referee could name>
【Next step】→ ppsych-organizing-framework (impose the analytical spine on the matrix)
```
