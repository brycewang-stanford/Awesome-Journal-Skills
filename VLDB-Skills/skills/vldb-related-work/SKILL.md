---
name: vldb-related-work
description: Use when positioning a PVLDB submission against prior literature, covering the deep database canon back to the 1980s VLDB proceedings, the SIGMOD/ICDE/CIDR neighborhood, concurrent work under rolling monthly deadlines, industrial and open-source systems as citable prior art, and overlap declarations for extended versions.
---

# VLDB Related Work

Use this to pressure-test novelty before writing the contribution list. The
database field has forty-plus years of proceedings and a reviewer pool with
long memories; the classic VLDB rejection is not "compared badly" but
"reinvented, without knowing it."

## The reinvention audit

Before claiming a technique is new, sweep three strata:

1. **The deep canon (1975-2000)** — partitioning, replication, buffering,
   adaptive query processing, and materialization ideas recur under new
   hardware. Search old VLDB/SIGMOD proceedings and TODS for the *mechanism*,
   not today's terminology for it.
2. **The modern venue ring** — PVLDB itself, SIGMOD/PACMMOD, ICDE, EDBT,
   CIDR, plus the systems conferences (SOSP/OSDI, NSDI, EuroSys) where storage
   and dataflow work also lands.
3. **Running code** — features shipped in PostgreSQL, RocksDB, DuckDB, Spark,
   or the cloud warehouses count as prior art whether or not a paper exists.
   Citing a system's documentation is normal here; pretending an implemented
   idea is unpublished is a rejection with a hyperlink.

If the mechanism existed, the honest contribution is the delta: new hardware
assumptions, new scale, new workload class, or the first measured comparison.

## Lane coverage check

| Literature lane | The reviewer question it answers |
|---|---|
| Classic DB canon | Did they know this was tried in 1994? |
| Current PVLDB/SIGMOD/ICDE | Is the nearest recent method compared or distinguished? |
| Systems venues | Is the OS/distributed-systems version of this idea acknowledged? |
| Industrial systems & open source | Does a shipping engine already do it? |
| Theory (PODS/ICDT) | Are known bounds or hardness results respected? |

A related-work section drawing on only one lane signals a half-searched field.

## Concurrency on a rolling calendar

Monthly deadlines mean near-neighbors surface *during* your review window.

- Sweep arXiv and the latest PVLDB issues in the week before your abstract
  registration; issues appear monthly, not annually.
- Work published after your submission date is concurrent: acknowledge it in
  the revision or camera-ready neutrally, without priority anxiety.
- If a concurrent paper lands mid-revision, address it in the change document
  factually — the same board is likely reviewing both.

## Extended versions and overlap

- Prior *workshop or demo* versions: declare them and state the delta; a PVLDB
  research paper must carry substantial new content over them (exact overlap
  thresholds: 待核实 on the live volume guidelines).
- Do not hold the same work under review at PVLDB and another venue
  simultaneously; rolling cadence makes "just try both" tempting and
  detectable — the communities share a review pool.
- The later journal expansion (The VLDB Journal, TODS) is the sanctioned lane
  for outgrowing the 12 pages.

## Writing the positioning paragraphs

```text
Per nearest neighbor (3-5 of them):
  [Name + venue + year] does <mechanism> under <assumption>.
  We differ in <assumption/scale/workload>, which matters because <consequence>.
  Compared in §<eval section> / not comparable because <honest reason>.
```

Group remaining citations by problem, one clause of contrast each. A citation
without a contrast is bibliography, not positioning.

## Output format

```text
[Reinvention audit] clean / hits found (mechanism, source, year)
[Lane coverage] <lanes with gaps>
[Nearest neighbors] <3-5, each with the distinguishing assumption>
[Concurrent-work watch] <items surfaced this month>
[Overlap declarations] <prior versions and their deltas>
[Novelty sentence] <one sentence a skeptical builder would accept>
```
