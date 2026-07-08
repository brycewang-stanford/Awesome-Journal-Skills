---
name: osdi-related-work
description: Use when positioning an OSDI submission against prior systems literature — covering the OSDI/SOSP/NSDI/FAST/EuroSys/ATC lanes, verifying venues through USENIX's free open-access proceedings and dblp, and citing your own precursors without breaking the renamed-system anonymity rule.
---

# OSDI Related Work

Position the paper the way a systems PC checks it. The anonymity mechanics referenced
here are OSDI '26 rules (verified 2026-07-08); the literature lanes are structural and
change slowly, but the nearest-neighbor papers change every cycle.

## What related work does at OSDI

An OSDI related-work section is not a survey; it is a **difference ledger**. For each
neighboring system: what it does, what it cannot do that yours can, and *why* — at the
mechanism level. Systems reviewers usually know the neighbors personally; they are not
reading to learn the area but to test whether you know exactly where you sit.

The strongest form is one sentence of grouping plus one sentence of mechanism-level
difference per group, with the difference tied to your design's named idea (see
`osdi-writing-style`). "Unlike X, we are faster" is not a difference; "X orders its log
cluster-wide, so its recovery scope is the cluster; ours is the tenant" is.

## The six lanes to sweep

| Lane | Where it lives | What reviewers check |
|---|---|---|
| Direct competitors | Recent OSDI/SOSP programs | Is the nearest published system compared head-on, in the evaluation and not only in prose? |
| The same problem, different layer | NSDI (network object), FAST (storage stack), EuroSys | Did you claim novelty for something solved one layer away? |
| The mechanism's ancestry | Classic OSDI/SOSP/ATC papers, possibly decades old | Is the lineage acknowledged? Systems memory is long — leases, logs, and schedulers all have ancestors |
| Production/industry reports | Operational-track papers, company engineering literature | Does deployed practice already do this quietly? |
| Concurrent work | arXiv, the venue cycle immediately before yours | Handled generously — parallel invention is normal in a two-flagship annual cadence |
| Your own precursors | Your arXiv/tech reports/talks | Cited without deanonymizing (rules below) |

## USENIX open access is a verification tool

Every OSDI paper — and every NSDI, FAST, and (historical) ATC paper — is a **free PDF
on `usenix.org`**, available to everyone from the day its event began. Consequences:

- There is no excuse for citing a systems paper from its abstract. Download and check
  the claim you attribute; misdescribing a neighbor's mechanism is the fastest way to
  lose a reviewer who built it.
- Venue attribution is checkable in seconds and must be exact. The systems canon
  scatters confusingly (GFS is SOSP, Raft is ATC, Firecracker is NSDI — see the trap
  list in [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md));
  verify on `dblp.org/db/conf/osdi/` before writing "at OSDI."
- SOSP-side papers live in the ACM DL rather than usenix.org; verify those through
  dblp plus the SIGOPS pages.

```bash
# Venue sanity pass over the bibliography (run before the anonymity sweep)
grep -nEi 'booktitle.*(OSDI|SOSP|NSDI|FAST|EuroSys|ATC|Annual Technical)' refs.bib |
  sort | uniq -c | sort -rn
# For each OSDI-attributed entry: confirm a conf/osdi/ dblp key exists.
# For each ATC entry dated 2026+: USENIX ATC ended after ATC '25 — recheck the
# actual venue (successor is stewarded by ACM SIGOPS).
```

## Citing yourself under OSDI '26 anonymity

OSDI '26 allowed prior non-peer-reviewed exposure — arXiv, tech reports, talks, social
media — but with a sharp condition: the **submission must use an anonymized system name
different from any used in those contexts**. Operational rules:

- Cite your precursor in the **third person**, as if it were someone else's system,
  under its public name; your submission's system carries its new name.
- Never write "we extend our earlier work"; the sentence itself is the leak.
- Sweep for indirect leaks: repository URLs in footnotes, trace names that appear only
  in your group's papers, acknowledgment stubs, `\cite` keys visible in comments.
- Do not omit the precursor entirely if it is publicly findable — omission plus a
  renamed system reads worse in shepherding than a clean third-person citation.

## Difference-ledger template

Draft the section as a ledger before writing prose; prose written first hides the
gaps the ledger exposes:

```text
related-work-ledger.md (one row per neighbor; groups become paragraphs)
neighbor        | venue+yr   | its mechanism        | why ours differs (mechanism level)   | in eval?
ReplayFS        | OSDI 'xx   | cluster-wide log     | recovery scope = cluster, ours = tenant | yes (fig 7)
CkptStore       | SOSP 'xx   | boundary checkpoints | moves the stall, doesn't bound it       | yes (fig 7)
LeaseKV         | NSDI 'xx   | per-key leases       | network object, no crash-adoption path  | prose only
<1990s ancestor>| SOSP '9x   | leases (original)    | we inherit; delta = epoch-bump adoption | n/a
```

Rules the ledger enforces: every row's difference is a mechanism, not an adjective;
any row marked "prose only" whose mechanism competes head-on is an evaluation gap to
fix or explicitly justify; and the ancestry row is mandatory — writing it is how
era-blindness gets caught before a PC member catches it for you.

## Failure patterns PCs flag

- **The missing obvious neighbor** — the one paper everyone on the PC thinks of within
  ten seconds, absent from the ledger. Fatal in a no-rebuttal cycle: nobody can ask
  "did you know about X?", they just score.
- **Citation without comparison** — the nearest system cited in Section 2 but absent
  from the evaluation table (`osdi-experiments` owns the fix).
- **Era-blindness** — treating a 2020s reinvention as novel over a 1990s mechanism;
  OSDI PCs contain people who wrote the 1990s paper.
- **Wrong-venue attributions** — individually small, collectively a credibility tax.

## Neighbors that exist only on arXiv

Systems work increasingly surfaces as arXiv-only preprints months before any PC sees
it. Handle by class: a preprint clearly targeting the same cycle is **concurrent
work** — cite it, note the concurrency, and do not let reviewers discover it for
you; an older unreviewed preprint with real adoption is engaged on its technical
content (reviewers will know it); and an abandoned preprint may still claim the
idea's name, in which case position by mechanism, not by name. In all three cases
the citation is dated — arXiv versions move, and "vN, month year" pins what you
actually compared against.

## Output format

```text
[Ledger status] complete / gaps in lanes: <list of the six lanes>
[Nearest neighbor] <system, venue, year> — compared in eval? yes/no
[Mechanism differences] <top 3, each one sentence, tied to the named idea>
[Self-citation audit] precursors renamed + third-person? leaks found: <list>
[Venue attributions] verified via dblp/usenix.org? unverified count: <n>
```
