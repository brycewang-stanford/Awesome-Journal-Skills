---
name: sigir-writing-style
description: Use when drafting or revising prose for a SIGIR paper — the IR register that leads with task, collection, and metric; claim sentences calibrated to significance results; first-page architecture for retrieval contributions; table-centric argumentation; and compressing into the 9-page budget without cutting soundness.
---

# SIGIR Writing Style

SIGIR prose has a recognizable register: it names the retrieval task before the
model, quantifies on named collections with named metrics, and calibrates every
adjective to a statistical test. Papers written in general-ML register ("we achieve
state-of-the-art performance across diverse benchmarks") read as tourists. This
skill converts drafts into the native register.

## The first-page arc for a retrieval paper

Reviewers form the accept/reject prior on page one. The arc that works:

1. **Task + regime**: which retrieval problem, under which constraints (first-stage
   vs re-ranking, latency budget, corpus scale, low-resource language, ...).
2. **The specific failure of current practice**: not "existing methods have
   limitations" but "late-interaction models pay a storage cost that grows with
   document length" — a mechanism, not a mood.
3. **The move**: your method/finding in one sentence, mechanism visible.
4. **Calibrated evidence preview**: collections, headline metric deltas, and the
   significance qualifier, all in one breath.
5. **Contribution bullets** that are checkable promises ("a re-ranking model that
   ...; an analysis showing ...; run files and code at ..."), not virtues.

```text
Register conversion (before -> after)
-------------------------------------
"Our novel framework significantly outperforms strong baselines."
->
"On MS MARCO dev and TREC DL 2019/2020, OURS improves nDCG@10 over a
 tuned BM25+monoT5 pipeline by 2.1-3.4 points (paired t-test, p<0.05,
 Bonferroni-corrected across collections), at equal re-ranking depth."

"Experiments demonstrate the effectiveness and efficiency of our approach."
->
"OURS matches ColBERT-style quality within 0.4 nDCG@10 while storing
 12x fewer vectors per document (Table 4); §5.3 isolates the pruning
 step as the source of the storage saving."
```

## Vocabulary calibration

| Say | Only if | Otherwise say |
|---|---|---|
| "significantly better" | A named test with correction passed | "better" / "numerically higher" |
| "state of the art" | Verified against the current published best on that collection + setup | "competitive with recent systems" |
| "generalizes" | ≥2 materially different collections/tasks tested | "transfers to <named setting>" |
| "efficient" | A cost table exists (latency/memory/index size) | Drop the word |
| "robust" | A stress condition was varied and reported | "stable across <the thing varied>" |

"Significant" is a reserved word in IR writing. Using it decoratively — while the
community's own methodology papers police exactly this — is the fastest credibility
leak available.

## Tables carry the argument

SIGIR argumentation is table-centric; prose narrates tables rather than replacing
them. Conventions reviewers expect:

- Metrics with explicit cutoffs (nDCG@10, R@1000, RR@10), collections as columns or
  blocks, systems as rows grouped by family (sparse / dense / hybrid / ours).
- Significance markers defined in the caption (†/‡ vs which baseline, which test,
  which correction) — an unmarked table triggers the standing objection.
- Bold for best only if best is statistically distinguishable; otherwise bold the
  statistically-tied set or none.
- Every table answers one named question; the narrating paragraph states the answer
  in its first sentence, then points at the supporting cells.

## Sectioning that survives the 9-page budget

A load-bearing skeleton for a full paper (adjust, don't worship): intro (1),
related work (0.75), method (2), experimental setup (1.25), results + ablations
(2.5), analysis (1), limitations + conclusion (0.5). Appendices count inside the
budget at SIGIR, so this skeleton has no "we'll appendix it" release valve — the
repository is the release valve (see `sigir-supplementary`).

Short papers invert the proportions: setup and the single result table dominate;
related work compresses to positioning sentences with dense citations.

## Sentence-level habits of accepted IR papers

- Present tense for the method, past tense for what was run.
- One idea per sentence in §Method; retrieval pipelines have too many moving parts
  for nested clauses.
- Name systems consistently — the review alias, table row label, and repo config
  name should be the same string.
- Limitations stated with scope, not apology: "results are offline; click-based
  validation is future work" beats a defensive paragraph.
- No roadmap paragraph ("Section 2 discusses...") in a 9-page paper; headers do that.

## Abstract length and shape

SIGIR abstracts run dense and factual: task, failure, move, lineup, deltas,
qualifier — typically 150-220 words with at least one number. If your abstract has
no collection name and no metric by word 100, it is still in ML register. The
final sentence belongs to availability ("code and run files at ...") or to the
scope qualifier, not to a vision statement.

## Revision protocol

1. Pass 1 — claims: highlight every evaluative adjective; check each against the
   vocabulary table; fix or delete.
2. Pass 2 — tables: caption completeness (test, correction, seeds), marker
   definitions, bold policy.
3. Pass 3 — first page: does the arc above survive a 60-second read by a tired AC?
4. Pass 4 — register: excise ML-venue boilerplate ("remarkable", "paradigm",
   "extensive experiments demonstrate").
5. Pass 5 — budget: compress by demotion to the repository, never by deleting
   protocol details.

## Output format

```text
[Register diagnosis] native-IR / mixed / ML-tourist
[First-page arc] task-regime / failure / move / calibrated-evidence / bullets: present-missing each
[Reserved-word violations] "significant(ly)" uses without a test: <n>, lines <...>
[Table conventions] cutoffs / markers / bold-policy / caption-tests: pass-fail each
[Compression debt] <pages over budget> and the demotion plan
[Three worst sentences] <quoted, with rewrites>
```
