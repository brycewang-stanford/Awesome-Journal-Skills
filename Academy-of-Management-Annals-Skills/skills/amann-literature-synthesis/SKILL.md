---
name: amann-literature-synthesis
description: Use when systematically gathering, coding, and synthesizing a management/organization literature for an Academy of Management Annals (Annals) review — the search-and-coverage methodology and the choice of narrative vs. systematic vs. bibliometric integration. Builds the corpus and synthesis notes; it does not impose the organizing spine (amann-organizing-framework) or write prose.
---

# Literature Synthesis Methodology (amann-literature-synthesis)

## When to trigger

- The proposal was invited and it is time to read the field thoroughly and transparently
- Reading feels unsystematic; you fear missing streams a referee could name
- You have many papers but no way to code, compare, or reconcile them
- You must decide whether this review is narrative, systematic, or bibliometric in method

## At Annals you synthesize — you do not run primary research

The folder name says "data analysis," but an Annals review reports **no data of its own**. Your "analysis" is the **systematic appraisal and integration of a literature**. The credibility of the whole review rests on the reader's belief that you read **everything that matters** and coded it consistently. Build coverage as a transparent process, not from memory.

## Choose the integration method first

| Method | What it does | Best when |
|--------|--------------|-----------|
| **Narrative / integrative review** | reads, interprets, and reorganizes the literature into a new framework | the contribution is conceptual integration (Annals' core mode) |
| **Systematic review** | a pre-specified, reproducible search-and-screen protocol; transparent inclusion | the field is large and you must prove comprehensive, unbiased coverage |
| **Bibliometric / meta-analytic** | co-citation, co-word, or quantitative effect-size synthesis | the contribution is structural (intellectual map) or a cumulative magnitude estimate |

Most Annals reviews are **integrative narrative** with a **systematic backbone**: a transparent search establishes coverage, and the narrative does the reorganizing. Bibliometrics can *support* the framework but rarely replaces the interpretive contribution.

## Building coverage to saturation

1. **Seed set.** Start from the proposal's key references and the field's canonical pieces.
2. **Transparent search.** Search the major databases (Web of Science, Scopus, EBSCO/Business Source, Google Scholar) by topic keywords; record terms, databases, dates, and counts so the "Review scope and process" claims are auditable.
3. **Forward + backward snowball.** Backward: each paper's reference list. Forward: who cites the seeds. Iterate until new searches stop turning up unseen important work (*saturation*).
4. **Inclusion / exclusion logic, stated.** Define what is in and out (time window, journal tier, theoretical vs. empirical, allied fields) and apply it consistently — referees ask "why did you omit X?"
5. **Working papers + adjacent literatures.** A current review must reach recent work and the bordering fields (organizational psychology, sociology) the literature draws on, or it reads stale or siloed.
6. **Saturation log.** Record when each search stopped yielding new must-cite work — this is your evidence of comprehensiveness for `amann-evidence-standards` and the referees.

## From reading to synthesis (a coding matrix, not a summary)

Summarizing restates each paper; **synthesizing** makes papers *talk to each other*. Code the corpus as you read:

| Column | What to capture |
|--------|-----------------|
| Study | author–year; the contribution you cite it for |
| Construct / question | exactly what it theorizes or measures (so incommensurable work is not pooled) |
| Theory base | the lens it uses (so you can map streams and detect silos) |
| Method / context | design, sample, setting (so you can weight credibility) |
| Finding / claim | direction + magnitude or the conceptual move |
| Tension | which work it agrees/conflicts with, and *why* |

This matrix feeds the organizing framework, the synthesis tables, and the even-handed treatment of debates. You **appraise** the studies (you are the field's reviewer-of-record); you do **not** re-run or "correct" them.

## Checklist

- [ ] Integration method chosen and justified (narrative-integrative / systematic / bibliometric)
- [ ] Seed set drawn from canonical pieces + proposal references
- [ ] Search terms, databases, dates, and counts recorded for the "scope and process" account
- [ ] Forward and backward snowball iterated to saturation
- [ ] Inclusion/exclusion logic stated and applied consistently
- [ ] Recent working papers and adjacent literatures included (no staleness, no silo)
- [ ] Saturation log records where searches stopped yielding new must-cites
- [ ] Coding matrix captures construct + theory base + method + finding + tensions
- [ ] Incommensurable constructs flagged (not pooled into a false "the literature finds…")
- [ ] No major author/stream whose omission a referee could name

## Anti-patterns

- Reviewing from a personal reading list (predictable coverage gaps a referee will spot)
- Summarizing paper-by-paper instead of synthesizing across the corpus
- Pooling studies that theorize *different* constructs into one "the field shows…" claim
- An undocumented search with no terms, databases, or counts — coverage claims become unfalsifiable
- Ignoring working papers (stale) or adjacent literatures (siloed)
- Re-estimating or "fixing" primary studies — an Annals review appraises, it does not re-run

## Output format

```text
【Method】narrative-integrative / systematic / bibliometric — and why
【Seed set】<canonical + proposal references>
【Search record】terms / databases / dates / counts logged? Y/N
【Snowball】backward+forward iterated to saturation? Y/N
【Inclusion logic】stated and consistently applied? Y/N
【Frontier + adjacency】recent WPs + bordering fields included? Y/N
【Saturation evidence】<where searches stopped yielding new must-cites>
【Coding matrix】construct/theory/method/finding/tension rows ready? Y/N
【Coverage risks】<any author/stream an omission referee could name>
【Next skill】→ amann-organizing-framework (impose the integrative spine on the matrix)
```
