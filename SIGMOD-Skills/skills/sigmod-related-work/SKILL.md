---
name: sigmod-related-work
description: Use when positioning a SIGMOD submission against the data-management literature, covering coverage across SIGMOD/PACMMOD, PVLDB, ICDE, TODS, and PODS lines, decades-deep systems history, concurrent papers in rolling venues, industrial-system citations, and PACMMOD's substantial-overlap exclusivity rule.
---

# SIGMOD Related Work

Database research has unusually long memory and unusually fast turnover at
the same time: reviewers expect a submission to know both the 1980s ancestor
of its technique and the PVLDB paper from three months ago. Positioning at
SIGMOD is therefore a two-clock problem, and the related-work section is
where a PC of system builders first tests whether the authors know the field
they are claiming to advance.

## The five literature lines to cover

| Line | What it contributes | Cost of missing it |
|---|---|---|
| SIGMOD/PACMMOD + PVLDB | The current research frontier, updated quarterly/monthly | "Unaware of concurrent work" reviews |
| ICDE and sibling conferences | Adjacent engineering results | Novelty delta overstated |
| TODS and journal literature | Consolidated, definitive treatments | Comparing against superseded versions |
| PODS / theory venues | Lower bounds, complexity, formal semantics | Claiming possibility where impossibility is known |
| Industrial systems + docs | What deployed engines already do | "Postgres has done this since 9.5" comments |

The last line is venue-distinctive: at SIGMOD, a feature shipped in an
open-source or commercial engine counts as prior art in reviewers' minds even
when it was never formally published. Cite documentation, source code, or
system papers for deployed behavior, and position against it explicitly.

## Deep-history diligence

Many "new" ideas in data management are reinventions — adaptive indexing,
fractional cascading, semantic caching, and differential update propagation
have each been rediscovered more than once. Before claiming firstness:

- Walk the technique's lineage backwards at least to its earliest SIGMOD/
  VLDB/TODS appearance; the classics are findable via the ACM DL and dblp.
- Search under the field's older vocabulary (e.g., "materialized view
  maintenance," not only "incremental computation").
- If the ancestor exists, the honest and stronger claim is the delta:
  changed hardware assumptions, changed workload regime, new guarantee.

## Concurrency in a rolling world

Your round-based submission competes with PVLDB's monthly acceptances and
other rounds' PACMMOD issues appearing *during* your own review. Practical
protocol: sweep new PACMMOD/PVLDB issues at submission, again before the
feedback phase, and again when preparing a revision; cite genuinely
concurrent work as concurrent, with a factual one-line distinction. A
revision letter that quietly ignores a widely-seen concurrent paper invites
the reviewer to raise it for you, on their terms.

## Exclusivity interacts with positioning

PACMMOD's rule bars submitting work with substantial overlap in scientific
content elsewhere while under review. This binds related-work strategy for
your *own* pipeline: a companion paper from the same project must be
different enough in results — not just in prose — and when it is, cite the
anonymized companion and state the division of contributions plainly.
Reviewers who smell salami-slicing check overlap aggressively.

## Contrast-form writing

The section should read as a set of distinctions, not an annotated
bibliography:

```text
Weak:   "Smith et al. [12] proposed an LSM compaction scheduler.
         Jones et al. [17] studied write amplification."
Strong: "Prior schedulers [12, 17] choose compaction targets from
         size ratios alone; neither observes query access patterns,
         so both degrade under the skewed reads we target (Sec 2).
         Our scheduler is the first to condition on both, and Sec 6.3
         compares against tuned versions of each."
```

Every cited cluster gets: what they established, the precise dimension where
this paper departs, and — for the nearest neighbors — a pointer to the
experiment where the departure is measured. A nearest neighbor cited but not
benchmarked is the most predictable feedback-phase question at this venue.

## A repeatable search protocol

1. Enumerate the paper's techniques and, for each, its older names — ask
   a senior colleague or trace citation chains backwards for vocabulary.
2. Sweep the ACM DL for SIGMOD/PACMMOD and TODS hits, dblp for PVLDB and
   ICDE, and the PODS series for impossibility results touching the claim.
3. Check the documentation and changelogs of the three engines nearest
   your contribution for shipped equivalents.
4. Log every sweep with its date; the concurrency protocol above reuses
   this log at feedback and revision time.
5. File each hit as: ancestor / nearest neighbor / concurrent / deployed
   prior art — the four categories that demand different handling in text.

## Placement tactics

SIGMOD tolerates related work early (Section 2) or late (before the
conclusion). Choose early when the contribution is only legible against
prior designs; choose late when the running example teaches faster than
contrast does. Either way, the introduction still owes one paragraph of
sharp positioning — reviewers form the novelty judgment on page one.

## Output format

```text
[Line coverage] five-line audit with gaps named
[Lineage check] earliest ancestor found; firstness claim adjusted
[Concurrent sweep] last swept date; papers requiring mention
[Nearest neighbors] work -> distinction -> comparing experiment
[Self-overlap] companion submissions and division-of-contribution note
[Rewrite targets] bibliography-style passages to convert to contrast form
```
