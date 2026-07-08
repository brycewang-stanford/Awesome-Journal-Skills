# VLDB Exemplars Library (award-anchored)

> **Verified via web search, access date 2026-07-08.** Every entry below is anchored to a
> VLDB Endowment award citation or a PVLDB bibliographic record, cross-checked against at
> least two independent sources (the vldb.org awards page plus an institutional award
> announcement, or dblp plus the vldb.org proceedings PDF). Anything that could not be
> pinned cleanly to a VLDB or PVLDB publication was left out and documented at the bottom.
> Four verified entries beat a dozen plausible ones.
>
> **Zero-hallucination rule:** the notes give positioning guidance only. No result
> numbers, speedups, or table values are restated here — read the paper on
> `vldb.org/pvldb/` before citing anything quantitative.
>
> **Sibling-venue guard:** the database world publishes across SIGMOD/PACMMOD, PVLDB,
> ICDE, CIDR, EDBT, and the systems conferences, and famous "database" papers are
> routinely misplaced. A paper is a VLDB exemplar only if it appeared in the VLDB
> conference proceedings or in PVLDB — check the actual venue string, not folklore.

---

## How to read this library

Each entry answers two questions: *why the community still cites it* (the design move
worth imitating) and *what to ask of your own draft* before claiming it plays in the same
genre. Pair the entries with
[`../../skills/vldb-writing-style/SKILL.md`](../../skills/vldb-writing-style/SKILL.md)
for the page-one expectations,
[`../../skills/vldb-experiments/SKILL.md`](../../skills/vldb-experiments/SKILL.md) for
the evaluation bar, and
[`../../skills/vldb-topic-selection/SKILL.md`](../../skills/vldb-topic-selection/SKILL.md)
for category routing.

---

## Verified entries

### The evaluation paper that changed practice — EA&B genre

**Leis, Gubichev, Mirchev, Kemper, Neumann & Boncz, "How Good Are Query Optimizers,
Really?", PVLDB 2015.** VLDB Test of Time Award 2025, presented at VLDB 2025 in London.
Verified via `vldb.org/awards_10year.html` and the CWI award announcement.

- **The move to imitate:** it measured a component everyone assumed was solved —
  cardinality estimation inside query optimizers — with a benchmark built to expose it,
  and let the measurements indict the field. No new system, no new algorithm: the
  contribution is disciplined measurement plus an honest diagnosis.
- **Ask of your draft:** if you are writing an EA&B paper, does your study change what a
  builder would do on Monday, or does it only rank systems? The award citation values
  practical impact.

### The architecture bet — classic systems genre

**Stonebraker et al., "C-Store: A Column-oriented DBMS," VLDB 2005.** Honored with the
VLDB ten-year award at VLDB 2015. Verified via the VLDB 2015 awards page and the
"C-Store: Looking Back" retrospective hosted on vldb.org.

- **The move to imitate:** a full-stack architectural position — store columns, not
  rows, for read-optimized workloads — argued end to end through a working prototype,
  a decade before the commercial column-store wave validated it.
- **Ask of your draft:** does your system paper commit to a defensible architectural
  thesis, or does it hedge across designs? VLDB's most durable papers picked a side.

### The scale-out data-management paper — big-data genre

**Aji, Wang, Vo, Lee, Liu, Zhang & Saltz, "Hadoop-GIS: A High-Performance Spatial Data
Warehousing System Over MapReduce," 2013.** VLDB Endowment Test of Time Award 2024.
Verified via the OSU CSE and Stony Brook award announcements cross-checked against the
vldb.org awards lineage.

- **The move to imitate:** it carried a domain workload (spatial analytics at medical-
  imaging scale) onto commodity scale-out infrastructure and released the result as
  open source, seeding an ecosystem — impact through availability, not just novelty.
- **Ask of your draft:** is the artifact something others can actually adopt? The 2024
  citation explicitly credits ecosystem creation.

### The industrial systems paper — production genre

**Huang et al., "TiDB: A Raft-based HTAP Database," PVLDB 13(12): 3072-3084, 2020.**
Verified via dblp record `journals/pvldb/HuangLCFMXSTZHW20` and the proceedings PDF at
`vldb.org/pvldb/vol13/p3072-huang.pdf`.

- **The move to imitate:** a deployed production system described with enough internal
  mechanism (consensus-replicated row store plus a columnar replica) to teach, not just
  advertise — the bar that separates PVLDB industrial papers from white papers.
- **Ask of your draft:** would a reader learn a reusable design decision, complete with
  the constraint that forced it, from every section?

---

## Genre coverage map

| Genre | Exemplar | Venue record | Award anchor |
| --- | --- | --- | --- |
| EA&B / measurement | "How Good Are Query Optimizers, Really?" | PVLDB 2015 | Test of Time 2025 |
| Architecture thesis | C-Store | VLDB 2005 | Ten-year award, VLDB 2015 |
| Scale-out platform | Hadoop-GIS | 2013 (ToT lineage) | Test of Time 2024 |
| Industrial deployment | TiDB | PVLDB 13(12), 2020 | dblp + proceedings PDF |

---

## Excluded after checking (common misattributions — do not cite as VLDB)

- **"Access Path Selection in a Relational Database Management System" (Selinger et
  al., 1979)** — SIGMOD, not VLDB. The foundational optimizer paper belongs to the
  sibling venue's lineage.
- **"The Snowflake Elastic Data Warehouse" (2016)** and **"Amazon Aurora" (2017)** —
  both SIGMOD industrial papers. Frequently misremembered as VLDB because of their
  cloud-database subject matter.
- **"Spanner," "Bigtable," "MapReduce"** — OSDI papers. Data-heavy does not mean
  database-venue.
- **MonetDB/X100 vectorized execution** — CIDR 2005, not VLDB, despite its deep
  influence on later PVLDB work.

Before adding a new entry, require either an award citation on `vldb.org` or a dblp
`journals/pvldb` / `conf/vldb` record, plus one independent confirmation, and record
both. If the two sources disagree on venue or year, leave the paper out or mark it
待核实 with no attribution.
