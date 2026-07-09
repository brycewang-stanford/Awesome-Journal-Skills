# USENIX FAST Exemplars Library (storage-contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** (`db/conf/fast`) and the **USENIX FAST proceedings** to confirm it appeared at the
> **USENIX Conference on File and Storage Technologies (FAST)** — matching title, author list,
> year, and venue string. Papers that could not be cleanly confirmed as FAST (as opposed to OSDI,
> ATC, SOSP, EuroSys, or a journal) were **omitted and documented below**. It is deliberately a
> short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** FAST is **not** OSDI, **not** ATC, **not** SOSP, **not** EuroSys.
> Several canonical storage systems were introduced at those venues instead; a famous author or a
> familiar storage tool name does **not** prove FAST. Each row was checked to be a FAST edition
> specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, throughput numbers, or table values — read the original on the
> USENIX site before citing anything. For FAST-specific policy, scope, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **storage-contribution shape × method** is closest to yours, then study how that
paper states a **storage problem practitioners recognize**, backs it with **evidence proportional
to the claim on real devices and workloads**, and reasons about the storage-specific costs (write
amplification, tail latency, endurance, crash consistency) — the FAST bar (see
[`../../skills/fast-writing-style/SKILL.md`](../../skills/fast-writing-style/SKILL.md),
[`../../skills/fast-topic-selection/SKILL.md`](../../skills/fast-topic-selection/SKILL.md), and
[`../../skills/fast-experiments/SKILL.md`](../../skills/fast-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "FAST-shaped."

Several rows are USENIX **Test of Time** or FAST **Best Paper** honorees, so they also model what
"influence a decade later" looks like at this venue.

---

## By storage-contribution shape

### New file-system design — flash-aware file system

- **Lee, Shin, Hwang & Cho, "F2FS: A New File System for Flash Storage," FAST 2015.**
  Verified: dblp `db/conf/fast/fast2015.html`; USENIX FAST '15 proceedings. **USENIX Test of Time**
  honoree (recognized at FAST '26). A log-structured file system designed from the ground up for the
  characteristics of flash/SSD storage.
  - **Why it is an exemplar:** it takes a hardware reality (flash's out-of-place update and FTL
    behavior) and redesigns a **whole file system** around it, then evaluates on real devices and
    workloads. The contribution is a storage-native design, not a general OS result that happens to
    touch disk.
  - **Self-check:** is your design motivated by a concrete device or media property, and evaluated
    on real hardware under workloads a storage reviewer accepts?

### SSD-conscious key-value store — I/O amplification

- **Lu, Pillai, Arpaci-Dusseau & Arpaci-Dusseau, "WiscKey: Separating Keys from Values in
  SSD-conscious Storage," FAST 2016.** Verified: dblp `rec/conf/fast/LuPAA16`; USENIX FAST '16.
  **FAST Best Paper.** An LSM-tree key-value store that separates keys from values to cut read/write
  amplification on SSDs.
  - **Why it is an exemplar:** it names a measurable storage pathology (**amplification** in
    LSM-trees on flash) and removes it with a data-layout change, quantifying the win on real SSDs.
    A mechanism others adopt, evaluated in storage terms.
  - **Self-check:** does your design target a storage cost you can measure (amplification, latency,
    endurance) rather than a generic "faster" claim, and is the comparison against a tuned real
    baseline?

### Cache-modeling algorithm — miss-ratio curves

- **Waldspurger, Park, Garthwaite & Ahmad, "Efficient MRC Construction with SHARDS," FAST 2015.**
  Verified: dblp `db/conf/fast/fast2015.html`; USENIX FAST '15. **USENIX Test of Time** honoree. A
  sampling technique that builds miss-ratio curves at drastically lower cost.
  - **Why it is an exemplar:** it makes a previously expensive storage-modeling instrument (the
    miss-ratio curve) **cheap enough to use online**, with an algorithm whose accuracy/cost
    trade-off is characterized carefully. A measurement/algorithm contribution the whole caching
    community reuses.
  - **Self-check:** does your method improve an instrument storage researchers rely on, with a
    stated accuracy-vs-cost trade-off rather than a single point claim?

### Device-behavior measurement methodology — shingled disks

- **Aghayev & Desnoyers, "Skylight—A Window on Shingled Disk Operation," FAST 2015.**
  Verified: dblp `db/conf/fast/fast2015.html`; USENIX FAST '15. **FAST Best Paper.** A combined
  software-and-physical (high-speed camera) method to reverse-engineer SMR drive behavior.
  - **Why it is an exemplar:** it invents a **measurement methodology** to see inside an opaque
    storage device, turning black-box hardware into characterized behavior others can design
    against. The contribution is *how to measure*, a distinctly prized FAST mode.
  - **Self-check:** does your paper give the community a way to observe or characterize a device or
    system property that was previously hidden, validated against ground truth?

### Large-scale reliability field study — flash in production

- **Schroeder, Lagisetty & Merchant, "Flash Reliability in Production: The Expected and the
  Unexpected," FAST 2016.** Verified: dblp `db/conf/fast/fast2016.html`; USENIX FAST '16. A
  multi-million-drive-day field study of SSD reliability across models and flash technologies in
  Google's fleet.
  - **Why it is an exemplar:** it reports what **actually happens to storage hardware at scale** —
    replacement and error behavior across MLC/eMLC/SLC over years — reshaping community beliefs with
    data no lab experiment could produce. Pure empirical storage insight.
  - **Self-check:** does your study change what the community believes about real storage behavior,
    with a dataset, population, and methodology a reviewer could scrutinize?

---

## Storage-shape ↔ exemplar (verified rows)

| Contribution shape | Verified FAST exemplar | Edition | Method |
| --- | --- | --- | --- |
| New file-system design | Lee et al., "F2FS" | FAST 2015 | Flash-aware file system |
| SSD-conscious KV store | Lu et al., "WiscKey" | FAST 2016 | Key/value separation |
| Cache-modeling algorithm | Waldspurger et al., "SHARDS" | FAST 2015 | Sampled MRC construction |
| Device-measurement methodology | Aghayev & Desnoyers, "Skylight" | FAST 2015 | Physical + software probing |
| Reliability field study | Schroeder et al., "Flash Reliability in Production" | FAST 2016 | Large-scale field data |

> Five verified papers across five storage shapes. The two FAST '15 Test-of-Time rows (F2FS,
> SHARDS) and the two Best-Paper rows (Skylight FAST '15, WiscKey FAST '16) also model what
> "influence a decade later" looks like at this venue.

---

## Omitted for lack of clean FAST verification (do not attribute to FAST without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"All File Systems Are Not Created Equal: On the Complexity of Crafting Crash-Consistent
  Applications" (Pillai et al.)** — verified to be **OSDI 2014**, *not* FAST, despite being a
  canonical crash-consistency paper by overlapping authors. A direct sibling-venue trap; listed
  only as a guardrail.
- **"The Google File System" (Ghemawat, Gobioff & Leung)** — **SOSP 2003**, not FAST. Omitted.
- **RocksDB / LevelDB origin write-ups** — engineering/blog and non-FAST venues; do not attribute an
  LSM-store's origin to FAST without checking the exact proceedings.
- **Log-structured file system founding paper (Rosenblum & Ousterhout)** — **SOSP 1991 / ACM TOCS**,
  a predecessor to flash-aware designs like F2FS but *not* a FAST placement; cite it to its real
  venue.

Before adding any paper, confirm it on **dblp** (`db/conf/fast`) and the **USENIX proceedings** by
matching the venue string to a FAST edition (not OSDI, ATC, SOSP, EuroSys, or a journal), then
record authors, year, and DOI/pages, and update the access-date header. When in doubt, omit. If web
search is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
