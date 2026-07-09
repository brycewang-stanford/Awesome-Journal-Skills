# USENIX FAST Resources

Action-oriented resources for the FAST skill pack. The `skills/` give advice; this directory lets
an agent model a FAST-shaped storage paper, benchmark against verified exemplars, and prepare a
storage replication package for the double-blind USENIX process with its two deadlines and one-shot
revision.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before-to-after abstract/introduction rewrite for a storage-systems paper (a fictional SSD key-value study). Illustrative fictional paper; no policy invented. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against real, verified USENIX FAST papers across storage-contribution shapes, and avoid sibling-venue confusion with OSDI, ATC, EuroSys, and SOSP. |
| [`official-source-map.md`](official-source-map.md) | Confirm the current-cycle FAST deadlines (Spring/Fall), page limits, double-blind and one-shot-revision model, open-access publication, and artifact badges before giving submission-ready advice. |
| [`external_tools.md`](external_tools.md) | Open the official FAST, HotCRP, USENIX artifact, and template surfaces, plus the cross-check sources for when the gateway blocks a direct fetch. |
| [`code/README.md`](code/README.md) | Use the shared replication-package tooling: a claim-to-evidence matrix, a USENIX-badge checklist, and a dependency-free smoke checker adapted for storage artifacts. |

## Scope Note

This is a **storage-systems** conference pack whose papers publish **open access via USENIX**, not
an ML-conference, ACM-journal, or economics pack. Do not import the OpenReview/PMLR machinery, the
`acmart` journal metadata, or the Stata/DiD/IV/RDD econometrics kit. FAST evidence is storage
evidence: real devices and firmware, standard traces and workloads (SNIA IOTTA, YCSB, filebench,
fio, block traces), write amplification, tail latency, endurance and wear, crash-consistency
testing, and aging — carried through a double-blind review with an author response, shepherding,
and a possible one-shot revision.

## Suggested Workflow

1. Route and frame with
   [`../skills/fast-topic-selection`](../skills/fast-topic-selection/SKILL.md) and
   [`../skills/fast-writing-style`](../skills/fast-writing-style/SKILL.md) — deciding FAST vs.
   OSDI/ATC/EuroSys before writing, and against the nearer of the two deadlines, is the
   highest-leverage move.
2. Build evidence with [`../skills/fast-experiments`](../skills/fast-experiments/SKILL.md),
   [`../skills/fast-reproducibility`](../skills/fast-reproducibility/SKILL.md), and
   [`code/README.md`](code/README.md).
3. Benchmark against [`exemplars/library.md`](exemplars/library.md), then confirm the live cycle in
   [`official-source-map.md`](official-source-map.md) and [`external_tools.md`](external_tools.md)
   before the HotCRP audit in
   [`../skills/fast-submission`](../skills/fast-submission/SKILL.md).
