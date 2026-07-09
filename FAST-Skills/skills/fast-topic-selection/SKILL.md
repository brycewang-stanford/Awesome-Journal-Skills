---
name: fast-topic-selection
description: Use when deciding whether a storage project belongs at USENIX FAST or should be routed to OSDI, ATC, NSDI, EuroSys, HotStorage, MSST, SYSTOR, or a storage journal (ACM TOS), and when distinguishing FAST from general-systems siblings by storage-contribution shape, real-device evidence, and the two-deadline calendar.
---

# FAST Topic Selection

Decide the venue before drafting. FAST — the USENIX Conference on File and Storage Technologies — is
the **storage-specialized** flagship: its reviewers are file-system, SSD/NVM, key-value, caching,
and reliability people, and they read for a **storage contribution**, not a general systems result
that happens to touch disk. A technically strong paper whose real lesson is about scheduling,
networking, consensus, or an ML model is respected and then routed to OSDI, ATC, or NSDI.

## The routing question that matters most

The decisive question is rarely "is this systems work?" but **"is the core lesson a *storage*
lesson — about how data is laid out, written, cached, made durable, or kept consistent — that a
storage reviewer would recognize as theirs?"** If yes, FAST. If the storage angle is incidental to
a broader OS/distributed/networking result, a general-systems venue fits better.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| Core lesson is storage: file system, SSD/NVM, KV/object store, cache, dedup, reliability, crash consistency, and the next FAST deadline is reachable | **USENIX FAST** | The storage-specialized flagship; storage reviewer pool and evidence norms |
| Broad OS / kernel / VM / runtime result; storage is one component | **OSDI / SOSP** | General-systems flagships; storage is not the whole point |
| General systems, practical/deployment flavor, or a storage result also of broad systems interest | **USENIX ATC** | Broad systems scope; overlaps FAST but not storage-specialized |
| The heart is the network or distributed protocol (even for a storage service) | **NSDI** | Networked-systems focus |
| European-systems framing, or a systems result across the stack | **EuroSys** | General-systems venue with a different community and calendar |
| Early idea, position, or a provocative measurement not yet a full study | **HotStorage** | Storage workshop for work-in-progress and vision |
| Mass-storage / archival / HPC-storage engineering focus | **MSST** | Named storage-systems and technology scope |
| Study too long or too deep for the page limit; or a journal-length treatment | **ACM TOS (Transactions on Storage)** | Storage journal, no conference page ceiling |

## Storage-contribution shapes FAST rewards

- **New storage-system design** — a file system, KV/object store, cache, dedup or tiering system
  designed around a media or workload reality, embodied and evaluated on real devices (the F2FS
  lineage).
- **Media-conscious mechanism** — a data-layout, compaction, wear, or scheduling change that removes
  a *storage cost* (write amplification, tail latency, endurance) measured on real hardware (the
  WiscKey lineage).
- **Measurement / characterization methodology** — a way to observe or model a device or system
  property that was opaque, validated against ground truth (the Skylight / SHARDS lineage).
- **Large-scale reliability or field study** — what actually happens to storage hardware or software
  at scale, with data no lab experiment could produce (the flash-reliability lineage).
- **Storage correctness** — crash consistency, durability, or data-integrity techniques and the
  tools that test them — a distinctly prized FAST mode.

## The storage-lesson and re-label tests

Two quick tests sharpen a borderline verdict:

- **Storage-lesson test:** state your contribution in one sentence. If that sentence names a
  *storage* quantity or property (write amplification, endurance, crash consistency, miss ratio,
  layout, durability), FAST fits. If the storage word is removable without loss, route to a
  general-systems venue.
- **Re-label test:** could this paper go to OSDI or ATC unchanged and read as native there? If its
  heart is a scheduler, a runtime, or a protocol with storage as a case study, route accordingly;
  FAST rewards the paper whose *core* is storage.

## Evidence maturity, without the ladder cliché

Fit is necessary but not sufficient: the same idea sits at different doors depending on how far the
evidence has come. A provocative measurement with an argument but no system is a **HotStorage**
paper; a design evaluated only on a simulator or one fresh-out-of-box drive needs **real, aged
devices under real workloads** before the FAST bar; a study too deep for the page limit belongs in
**ACM TOS** first. Submitting one step early earns a polite "promising, but measure it for real,"
and — because FAST runs only twice a year — costs months.

## Cheap reconnaissance before committing

```text
[Scope]   scan the last two FAST programs (dblp conf/fast, usenix.org) for your subarea
          -> 3+ recent papers = a reviewer pool exists; 0 = opening or mismatch (or it's an OSDI/ATC topic)
[Citations] is your bibliography majority storage venues (FAST/OSDI/ATC/EuroSys/HotStorage/MSST/TOS)?
          -> majority non-storage => reviewers read you as a visitor; naturalize the framing first
[Calendar] which FAST deadline (Spring/Fall) is next, and does an OSDI/ATC/EuroSys date land sooner?
          -> route to the nearest honest fit; FAST's twice-a-year rhythm cuts both ways
```

## Decision procedure

```text
[Audience]   who acts differently if the claim holds? storage engineers/researchers/operators?
[Claim type] storage-system design / media-conscious mechanism / measurement / reliability / correctness
[FAST vs OSDI/ATC] is the CORE lesson storage? -> FAST; is storage incidental? -> general-systems venue
[Sibling check] network core -> NSDI; early/position -> HotStorage; too long -> ACM TOS
[Calendar]   choose the nearer of the two FAST deadlines, or a sibling if it lands sooner
[Verdict]    USENIX FAST / sibling venue / workshop / journal, with a one-line storage reason
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the verdict
is FAST, continue with `fast-workflow` for the two-deadline calendar and `fast-writing-style` for the
paper shape.
