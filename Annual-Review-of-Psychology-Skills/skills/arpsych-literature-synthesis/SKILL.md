---
name: arpsych-literature-synthesis
description: Use when systematically gathering, reading, and structuring the literature for an Annual Review of Psychology (ARPsych) review so coverage is comprehensive and current. Builds the evidence base; it does not design the analytical spine (arpsych-organizing-framework) or judge balance (arpsych-comprehensiveness-and-balance).
---

# Literature Synthesis — Reading the Whole Field (arpsych-literature-synthesis)

## When to trigger

- An invitation is in hand and the reading must start in earnest
- The user has "read a lot" but has no system for tracking what is covered
- Coverage gaps are likely (one paradigm, one lab, or one decade dominates the notes)
- An embedded meta-analysis is planned and the search must be documentable

## Coverage is the price of admission, not the contribution

ARPsych readers trust a review to be **comprehensive within its frame and current to the frontier**. A reviewer caught missing a major line of work loses authority instantly. But coverage is the floor: the *contribution* is the framework you impose later (`arpsych-organizing-framework`). This skill builds an evidence base broad and well-recorded enough that (a) nothing important is missed and (b) you can later be *selective in prose* without being *incomplete in coverage*.

## A systematic, documentable search

Even a narrative review benefits from a near-systematic search you can describe:

1. **Seed set** — the canonical and recent agenda-setting papers you already know.
2. **Forward + backward citation chasing** — who cites the seeds; whom the seeds cite.
3. **Database sweep** — PsycINFO/APA PsycNet, Web of Science, Scopus, Google Scholar with explicit terms.
4. **Specialty + adjacent venues** — the relevant primary journals AND adjacent fields (neuro, economics, linguistics) the topic touches.
5. **Stopping rule** — saturation: new searches surface only papers already in the matrix.
6. **Record the protocol** — terms, databases, dates, inclusion/exclusion — even for a narrative review; mandatory if you report a meta-analysis (→ `arpsych-transparency-and-reproducibility`).

> Document the search *as you go*, not from memory afterward. ARPsych's transparency expectations and any meta-analytic component both depend on a search log you can reproduce (检索于 2026-06；以官网为准).

## The evidence matrix (one row per study/finding)

Build a structured table — not a pile of PDFs. Useful columns:

| Column | Why |
|--------|-----|
| Construct / question | lets you later sort papers into framework cells |
| Population / paradigm | surfaces over-reliance on one method or sample (WEIRD bias) |
| Design + strength | feeds credibility weighting in `arpsych-comprehensiveness-and-balance` |
| Effect / finding (+ direction, size if available) | enables quantitative synthesis |
| Replication status | flags shaky vs. robust effects (post-replication-crisis hygiene) |
| Lab / camp | exposes citation concentration and balance risks |

The matrix is the bridge: its rows become framework cells, its columns become balance and credibility checks.

## Checklist

- [ ] Seed set, citation chasing, database sweep, and adjacent venues all run
- [ ] Search terms, databases, and dates recorded (protocol, not memory)
- [ ] Saturation reached (new searches return only known papers)
- [ ] Evidence matrix built: one row per study/finding with the columns above
- [ ] Replication status noted for contested effects
- [ ] Lab/camp column reveals whether coverage concentrates on a few groups
- [ ] Non-English / non-WEIRD and cross-disciplinary work checked for, not assumed away
- [ ] Coverage is current to the frontier AND anchored to foundational work

## Anti-patterns

- Reading by familiarity (only your own subfield's journals) — guarantees coverage gaps
- No search protocol — cannot satisfy ARPsych transparency or support a meta-analysis
- A pile of summaries instead of a structured matrix — no path to a framework
- Ignoring replication status, so debunked effects are reviewed as established
- Stopping when tired rather than at saturation
- Treating coverage as the contribution (it is the floor, not the spine)

## Output format

```text
【Search protocol】seeds + databases + terms + dates + stopping rule (recorded?)
【Coverage】subfields/paradigms/adjacent fields swept; saturation reached? Y/N
【Evidence matrix】#rows; columns include design, replication status, lab/camp? Y/N
【Gaps / concentration】where coverage thins or over-concentrates
【Meta-analysis planned?】Y/N → if Y, route to transparency skill
【Next step】→ arpsych-organizing-framework (turn the matrix into a spine)
```
