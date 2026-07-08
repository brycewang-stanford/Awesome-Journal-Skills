---
name: webconf-related-work
description: Use when positioning a Web Conference (WWW) submission against prior literature — tracing lineage through three decades of WWW proceedings, contrasting with the WSDM/CIKM/SIGIR/KDD sibling circuit, handling the venue's preprint-non-citation rule, and budgeting references against the shared 12-page PDF tail.
---

# Web Conference Related Work

Related work at this venue does two jobs the generic version skips: it proves the
paper knows its **WWW lineage** (the series runs to 1994, and many web problems
have decade-old ancestors reviewers personally remember), and it draws the line
against the **sibling circuit** — WSDM, CIKM, SIGIR, KDD, ICWSM, WebSci — whose
reviewer pools overlap heavily with the track panels judging you.

## Lineage first, novelty second

Web research recycles its problems as the platform layer changes: link spam →
social spam → LLM-generated content; PageRank-era graph analysis → network
embeddings → graph neural networks; forum mining → microblog mining → short-video
mining. A strong related-work section names the lineage explicitly and locates the
contribution at the *newest turn*:

```text
Weak:   "Graph embedding has been widely studied [3,7,12,19]."
Strong: "Web-graph representation moved from link-analysis scores through
         embedding objectives (LINE, WWW 2015) to message-passing models
         (HAN, WWW 2019); all assume a static snapshot. Our setting -- edges
         arriving from a live crawl -- breaks that assumption because ..."
```

The pattern: two or three named waypoints with venues and years, then the
assumption every waypoint shares, then why your setting breaks it. One paragraph of
this outperforms twenty grouped citations.

## The sibling-circuit contrast table

Reviewers here habitually ask "why is this not a WSDM/SIGIR/KDD paper?" Answer
inside related work by contrasting *evidence norms*, not prestige:

| Neighbor | Its center of gravity | Your contrast sentence should say |
|---|---|---|
| WSDM | Web search & mining methods, offline rigor | what your paper adds beyond the method: platform mechanism, measurement, or system |
| SIGIR | Retrieval effectiveness & evaluation | why the web setting (adversaries, freshness, heterogeneity) changes the retrieval problem |
| KDD | Mining methods & deployed data science | what is web-structural rather than generic-tabular/graph |
| CIKM | Broad IR/DB/KM methods | the sharper web claim that the broad venue wouldn't demand |
| ICWSM | Social-media measurement | your computational/methodological delta beyond measurement |
| WebSci | Interdisciplinary web studies | your technical contribution beyond the socio-technical finding |

Cite the nearest paper from each relevant neighbor when one exists; its authors may
well be your reviewers, and omitting them reads as either ignorance or evasion.

## Venue-attribution hygiene

Misattributing a classic to the wrong venue is a credibility wound with expert
panels. Traps specific to this literature: the PageRank *algorithm* report is a
Stanford technical report while the search-engine paper (Brin & Page) appeared at
WWW7 1998 in a journal-published proceedings; several "web" classics actually live
at KDD or SIGIR; and the series' own name changed (WWW → The Web Conference, 2018;
ACM Web Conference era from 2022) so citation styles vary across decades. Verify
every load-bearing citation against dblp or the ACM DL — this pack's
`resources/exemplars/library.md` records five verified WWW papers safe to cite as
lineage waypoints.

## The preprint rule shapes citation practice

Two verified 2026 rules interact here: submissions must be original (nothing under
review or published elsewhere), and your *own* anonymized preprint may exist on
arXiv/SSRN **but the submission must not cite it**. For third-party preprints,
cite them when they are the real prior art — with arXiv IDs and honest framing as
non-archival — but do not treat an uncited arXiv posting as license to claim
novelty over it; track reviewers in fast-moving areas (retrieval-augmented AI
especially) read arXiv daily. Concurrent work merits a labeled paragraph:
"Concurrent and independent: [X] (arXiv, Sep 2025) addresses ...; we differ in ..."

## Budgeting against the shared tail

References and appendix split the same 4-page PDF tail (12 total minus 8 main).
Reference-list discipline is therefore a *space* decision: cite the survey plus the
directly-contrasted papers rather than every member of a lineage; drop redundant
multi-citations ("[3,7,12,19]" where only [12] is discussed); prefer one recent
strong baseline citation over three historical weak ones. A typical healthy budget
here is 1.5-2 pages of references, preserving 2+ pages of appendix.

## A two-pass drafting workflow

Pass 1, **coverage** (weeks before the deadline): harvest candidates from the last
two proceedings of WWW plus the relevant sibling venue, the track's likely
reviewer bibliographies, and the citation graphs of your three closest papers.
Verify each candidate's venue on dblp *at harvest time* — batching verification
for later is how misattributions survive into the submission. Pass 2,
**argument** (with the draft stable): delete every citation the text does not
discuss, write the lineage paragraph and the sibling-contrast sentences, and
re-run a final search two weeks before the deadline for the fast-moving tracks —
a September arXiv posting in retrieval-augmented AI can become the rebuttal's
central objection if the October submission ignores it.

Ordering heuristic inside the section: lineage first (establishes you belong),
nearest neighbors second (establishes the delta), adjacent-discipline anchors
last (establishes construct credibility for the mixed panel). The common inverse
— starting with a broad sociology-of-the-web sweep — spends the section's best
real estate before reaching the papers reviewers will actually compare you to.

## Pre-submission checklist

- [ ] Lineage paragraph with named, venue-attributed waypoints and the shared
      assumption your setting breaks.
- [ ] One contrast sentence per relevant sibling venue; nearest-neighbor papers
      from the current and previous cycle cited.
- [ ] Every classic verified against dblp/ACM DL; no venue misattributions.
- [ ] Own preprint uncited; concurrent work labeled; no novelty claims over
      papers the section pretends not to know.
- [ ] Reference pages counted against the appendix budget.

A final self-test: hand the section to a co-author and ask which two papers a
reviewer would demand comparison against. If their answer names a paper the
section does not cite, the coverage pass failed regardless of how many
references it holds.

## Output format

```text
[Lineage] <waypoints named> -> <shared assumption broken>
[Sibling contrasts] WSDM/SIGIR/KDD/CIKM/ICWSM/WebSci: <which drafted, which N/A>
[Attribution audit] <misattributions found and fixed>
[Preprint handling] own-preprint uncited: yes/no; concurrent-work paragraph: yes/no
[Tail cost] references=<pages>, appendix room left=<pages>
```
