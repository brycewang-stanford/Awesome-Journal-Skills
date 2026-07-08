---
name: kdd-writing-style
description: Use when revising a KDD paper into the venue's register, where the first page names a data regime, a mechanism, and scale evidence, efficiency adjectives trace to design decisions, and two-column sigconf pages punish sprawl. Covers Research vs ADS voice, dataset-size discipline, assertive contribution bullets, and 8-page compression.
---

# KDD Writing Style

Use this during revision passes. KDD prose has a recognizable register: it talks about
**data regimes** (scale, drift, sparsity, heterogeneity, label scarcity) rather than
model families, it attaches every performance adjective to a mechanism, and it treats
dataset cardinalities as part of grammar — a dataset without a size reads as
unfinished. The `resources/worked-examples/01-introduction.md` file shows a full
before/after; this skill is the rule set behind it.

## First-page contract

Within page one, a KDD reviewer expects to find, in some order:

1. The **data regime** that makes the problem hard (not "X is important").
2. Why existing method families fail **in that regime**, each for a mechanism-level
   reason.
3. The **named mechanism** this paper adds (a primitive someone could re-implement).
4. Evidence scoped with numbers: dataset scale, throughput or memory if claimed,
   headline quality delta.
5. For ADS: where this is deployed and the post-launch headline number.

If the introduction could open an ICML or a database paper unchanged, the framing is
not yet KDD's.

## Register rules

| Draft habit | KDD-register rewrite | Why it matters here |
|---|---|---|
| "novel framework" | Name the mechanism: "drift-weighted sketch family" | Frameworks are unreviewable; mechanisms are ablatable |
| "large-scale experiments" | "3 graphs, 10M-2.1B edges" | Scale is the venue's currency; unquantified scale reads as small |
| "efficient" | "O(1) update; 1.4M events/s on one core" | Efficiency claims must be attributable and checkable |
| "significantly outperforms" | "+3.3 AUPRC, median of 5 seeds, IQR ±0.4" | Practitioner reviewers distrust unquantified superlatives |
| "real-world data" | Name the datasets and their provenance | "Real-world" without provenance signals toy benchmarks |
| "can be applied to many domains" | One demonstrated transfer, or silence | Unpaid generality checks are a known reject pattern |

## Contribution bullets that survive review

Circular bullets ("we propose X, we evaluate X") waste the most-read lines of the
paper. Each bullet should assert a falsifiable fact:

```text
Weak:   - We propose StreamHive, a novel framework for stream anomaly detection.
Strong: - We show bounded-memory detection under drift reduces to online decay-rate
          selection, and give a mixture-of-sketches scheme with O(1) update cost.

Weak:   - Extensive experiments demonstrate the effectiveness of our approach.
Strong: - Across three streams up to 2.1B events, the scheme matches window-retrained
          deep baselines on AUPRC at fixed 512MB memory; ablations attribute the gain
          to the drift weighting rather than the ensemble.
```

## ADS voice

The Applied Data Science register differs deliberately from the Research register:

- Lead with the business/operational problem and the deployment context, then the
  technical path — reviewers of ADS papers score problem realism before novelty.
- **Lessons learned are content, not filler**: what failed before the shipped design,
  which offline metrics mispredicted online behavior, what broke at rollout. The
  classic KDD applied papers are remembered for exactly these sections.
- Post-launch numbers must be flagged as such and separated from offline evaluation —
  the track's desk-reject rule is about quantified post-launch performance, so make
  those numbers typographically impossible to miss.

## Two-column compression tactics

The ACM sigconf format is tight, and submission is 8 content pages:

- Write display math sparingly; inline the one-off definitions and reserve display
  lines for objects the paper reuses.
- Every figure earns its column-width: delete any plot whose caption cannot state
  what decision it supports. Wide tables go `table*` (full width) early, since late
  layout flips cascade page breaks.
- Algorithm environments are expensive; one algorithm block for the core mechanism,
  prose for variants, full pseudocode in the appendix.
- Kill roadmap paragraphs ("Section 2 discusses...") — in an 8-page paper the
  structure is visible without a tour guide.
- The camera-ready adds exactly one content page; do not defer required content to it
  (reviewers score the submission, and refs+appendix get capped at 3 pages later).

## Anonymity phrasing

- Research Track: "our production system at a large e-commerce platform" is fine;
  naming the company usually is not — and internal system codenames are as
  identifying as the company name.
- Cite your own prior work in third person, and check the referenced repository's
  README carries no author trace (`kdd-artifact-evaluation`).

## Title and abstract mechanics

- KDD titles favor **named-system-plus-claim** ("<Name>: <what it does> <in what
  regime>") or a direct claim; question titles and pun-only titles underperform with
  this reviewer pool.
- The abstract is bid-bait: reviewers choose papers from it, so the regime vocabulary
  (graph, stream, drift, recommendation, fraud, spatio-temporal) must appear
  honestly — the wrong vocabulary buys the wrong experts.
- One quantitative claim in the abstract, minimum: an abstract with no number is a
  style violation at a venue whose currency is measured evidence.

## Revision pass order

A concrete sequence for turning a complete draft into a KDD submission, one pass per
day in the final week:

1. **Regime pass**: rewrite page one until the data regime leads; fix the abstract's
   vocabulary and number.
2. **Adjective audit**: grep the draft for "novel", "significantly", "efficient",
   "large-scale", "real-world"; each occurrence either gains a mechanism/number or
   dies.

```bash
grep -n -iE "novel|significant|efficient|large-scale|real-world|extensive" \
  sections/*.tex | wc -l   # target: near zero unattached occurrences
```

3. **Claim-evidence pass**: every contribution bullet cross-referenced to its table,
   figure, or section; circular bullets rewritten as assertions.
4. **Compression pass**: apply the two-column tactics until the body sits at 8 pages
   without spacing hacks (`kdd-submission` treats those as desk-level).
5. **Anonymity pass**: self-citations, system codenames, acknowledgements, repo
   traces — last, so later edits cannot reintroduce leaks.

## Output format

```text
[Register diagnosis] regime-first / model-first (needs reframe) / journal-paced
[First-page contract] items present: <1-5 checklist>
[Adjective audit] <unattached efficiency/scale adjectives found>
[Bullet quality] assertive / circular -> <rewrites>
[ADS voice] lessons-learned present / post-launch numbers flagged / N-A
[Compression cuts] <move/delete/merge list to reach 8 pages>
```
