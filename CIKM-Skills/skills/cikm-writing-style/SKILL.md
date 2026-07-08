---
name: cikm-writing-style
description: Use when revising a CIKM manuscript for the tri-community readership — writing an opening that lands with IR, data-mining, and knowledge-management reviewers simultaneously, compressing into appendix-inclusive page budgets, keeping claims inside the evidence, and maintaining double-blind and disclosure-compliant prose.
---

# CIKM Writing Style

A CIKM paper is read in three accents at once. The IR reviewer scans for the task
and the evaluation; the mining reviewer scans for the mechanism and its delta; the
KM/database reviewer scans for the data reality — schemas, scale, heterogeneity,
noise. Style at this venue means making all three scans succeed in the first page,
inside a budget where appendices offer no escape (10 pages including them for 2026
full papers).

## The first page, three scans deep

Order the opening so each lane hits its anchor early:

1. **The information problem** in domain terms — what is being retrieved, mined,
   linked, or integrated, and for whom.
2. **Why the boundary is the hard part.** CIKM contributions usually live where
   lanes meet; say which interaction breaks existing single-lane methods ("KG
   completion models assume static graphs; enterprise search feeds them a stream").
3. **The mechanism, named.** One clause a mining reviewer can repeat in their
   review.
4. **The evidence preview, calibrated.** Datasets, baselines, and the honest size
   of the win — with the deployment or resource evidence up front if the track
   demands it.

If the paper cannot state point 2, it is a single-lane paper and
`cikm-topic-selection` should re-run before more polishing.

## Vocabulary discipline across lanes

Cross-community words are where CIKM drafts leak credibility. Terms with lane-
specific meanings — *entity*, *knowledge*, *relevance*, *scalable*, *online* — must
be pinned at first use. A table of rewrites that recur in CIKM drafts:

| Draft habit | Lane it annoys | Repair |
|---|---|---|
| "our knowledge-aware model" (never defined) | KM-DB | Name the structure: "a model conditioned on a curated product KG (2.1M triples)" |
| "significantly better" without a test | IR | Reserve the word for tested significance; else give the margin |
| "scales to large graphs" | mining | Give the size, hardware, and growth curve actually measured |
| "real-world dataset" | all three | Name the source, size, license, and collection window |
| "state-of-the-art baseline" | mining + IR | Cite venue + year; stale SOTA claims are checked at review |

## Budget compression, appendix-inclusive

Because appendices count inside the 2026 budgets, the compression question is not
"what moves to the appendix" but "what leaves the PDF." Priority order for cuts:
redundant pipeline diagrams; per-dataset tables that repeat one pattern (keep the
pattern statement plus the fullest table); hyperparameter grids (→ the cited
artifact); derivations of standard results (→ cite). What must stay: everything a
reviewer needs to *not* trust you — evaluation protocol, baseline tuning parity,
and the one ablation that isolates the mechanism.

## Anonymity and disclosure in prose

Double-blind style at CIKM includes third-person self-citation ("Cao et al.
proposed", even when Cao is an author) and de-identified system prose for applied
papers — the deployment must stay describable without becoming attributable. The
GenAI Usage Disclosure section is also prose: write it in the same factual register
as the experiments ("evaluation scripts drafted with a code assistant, reviewed and
tested by the authors; manuscript text human-written"), not as legal boilerplate.

## Section skeleton for a 10-page full paper

A load-bearing default under the appendix-inclusive budget (adjust, don't worship):

```text
1.0 pp  Introduction — the four-step tri-lane opening
0.75 pp Related work — three fronts + the boundary-work paragraph
2.5 pp  Method — problem formulation, mechanism, complexity note
3.0 pp  Experiments — protocol ¶, main results, decisive ablation, robustness
0.5 pp  Deployment/resource specifics (track-dependent)
0.5 pp  Limitations + conclusion
1.75 pp Appendix (counts!) — only review-critical overflow
—       GenAI Usage Disclosure + references (uncounted)
```

The commonest imbalance in CIKM drafts is a method section eating four-plus pages
while the evaluation protocol gets one paragraph; the blended panel reads the
protocol paragraph first.

## Title and abstract as routing devices

Title and abstract are consumed twice before any human reads page 2: by EasyChair
bidding (which lane's reviewers self-select) and later by ACM DL search. A CIKM
title should carry the task, the data structure, and — when honest — the setting:
"Freshness-Aware Entity Linking for Enterprise Search" routes correctly;
"Towards Better Knowledge Utilization" routes randomly. In the abstract, spend
one sentence per lane anchor, and put the one number you want remembered in the
final sentence — that sentence is what shows in search snippets.

## Micro-rewrite exercise

> Draft: "With the explosion of information, knowledge graphs have attracted much
> attention. We propose a novel framework, XYZ, which significantly outperforms
> state-of-the-art methods."

Rewritten for the tri-lane scan: "Product search at catalog scale fails on queries
whose intent lives in relations the index never sees — compatibility, succession,
bundling. We link the query to a 2.1M-triple product KG at retrieval time and
propagate relevance along typed edges; on two public benchmarks and one industrial
log this lifts nDCG@10 by 4-6 points over the strongest KG-free ranker, with the
gain concentrated exactly on relation-dependent queries." Problem, boundary,
mechanism, calibrated evidence — one breath each.

## Limitations without self-sabotage

A limitations paragraph that works at CIKM scopes rather than confesses: state the
regime the evidence covers (data types, scale, languages, graph density), name the
adjacent regime it does not, and say what would be needed to extend — three
sentences, no adjectives of apology. The blended panel treats a well-scoped
limitation as expertise and an unscoped one ("may not generalize") as either
evasion or, worse, an invitation to imagine failures the authors never tested.

## Output format

```text
[Three-scan check] IR anchor / mining anchor / KM-DB anchor — found on page 1?
[Pinned terms] <cross-lane words defined at first use>
[Claim-evidence gaps] <sentences promising more than the tables hold>
[Cut list] <what leaves the PDF to make the appendix-inclusive budget>
[Compliance prose] <self-citation person, deployment de-identification, GenAI section tone>
```
