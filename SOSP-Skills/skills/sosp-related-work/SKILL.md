---
name: sosp-related-work
description: Use when positioning a SOSP submission against the systems literature — the SOSP/OSDI lineage a PC expects you to know, structural comparison instead of citation listing, third-person self-citation under double-blind rules, and handling concurrent work across the now-annual systems deadline circuit.
---

# SOSP Related Work

Use this when writing or auditing the related-work section of a SOSP paper. At this
venue the section is a load-bearing wall: the PC contains authors of the systems you
must compare against, the meeting will replay any positioning gap out loud, and the
"how does this differ from X" review is the most common avoidable negative. Rules
below reflect the 2026-cycle CFP's double-blind policy (checked 2026-07-08).

## Know the lineage or be corrected in public

A SOSP reviewer expects the paper to place itself in the SOSP/OSDI line of work on
its problem — often decades deep — plus the adjacent venues where the problem also
lives (EuroSys, USENIX ATC, NSDI for networked systems, FAST for storage, ASPLOS at
the architecture boundary). Two search passes are mandatory before the freeze:

1. **Ancestry pass**: walk the problem back through prior SOSP/OSDI editions via
   `dl.acm.org/conference/sosp`, dblp, and the SIGOPS Hall of Fame list
   (`sigops.org/awards/hof/`) — a HoF paper on your problem uncited is a credibility
   wound out of proportion to its citation value.
2. **Recency pass**: both SOSP and OSDI have run annually since 2024, so the "last
   edition" is now at most a year old, and the paper most likely to sink yours
   appeared months ago. Sweep the two most recent programs of each sibling venue.

## Compare structures, not abstracts

Listing citations with one-line summaries is a survey; SOSP wants **positioning** —
for each nearest neighbor, the axis on which your design differs and why that axis
matters for the paper's claims:

| Comparison axis | Positioning sentence shape | Weak version it replaces |
|---|---|---|
| Assumption | "X assumes a trusted hypervisor; Foo removes that trust and pays for it in §5.3" | "X is a related virtualization system" |
| Mechanism | "Both log; X logs operations, Foo logs allocation intents, which is what makes recovery size-independent" | "Unlike X, we use a different log format" |
| Guarantee | "X provides per-object linearizability; Foo's per-session guarantee is weaker and §2 argues sufficient" | "Foo has better consistency" |
| Evidence | "X evaluates on synthetic skew; the trace-driven results in §6 cover the regime X excludes" | "X's evaluation is limited" |

Comparisons that end in a section pointer are meeting-proof: an advocate can answer
"how is this different from X" by reading your sentence aloud.

## Double-blind mechanics in the citations

- Cite your own prior work in **third person**, normally, as if written by others.
  Omitting a needed self-citation is worse anonymization than citing it neutrally.
- The unpublishable case — the submission directly extends your identifiable
  tech report or workshop paper — is the one place to consult the current CFP's
  precise language rather than improvise (待核实 per cycle whether anonymized
  citation or chair consultation is prescribed).
- Acknowledgment-style credits ("thanks to the Bar team for traces") leak identity;
  hold them for the camera-ready.

## Concurrent work across an annual circuit

With SOSP and OSDI both annual and EuroSys/ATC/NSDI in between, "concurrent" now
means a sliding window of months:

- Work published after your submission freeze is genuinely concurrent; note it
  gracefully in the response if reviewers raise it, and integrate it at
  camera-ready with the shepherd's blessing (see `sosp-camera-ready`).
- An arXiv preprint of a competing system is citable context; treat it as
  unrefereed and compare against its claims cautiously and visibly.
- Do not silently ignore a known concurrent system hoping reviewers missed it —
  at this PC, someone reviewed it.

```text
Related-work matrix (build before writing the section)

               assumption      mechanism        guarantee       evidence regime
Foo (ours)     <...>           <...>            <...>           <...>
X  [SOSP'24]   same            op logging       stronger        synthetic only
Y  [OSDI'25]   weaker: <..>    similar: <..>    same            no failure runs
Z  [arXiv'26]  unclear (unrefereed) ...
-> nearest neighbor: X; the axis that matters: recovery cost vs log size (§6.2)
```

## Placement and length

Three-quarters of a page is typical (see `sosp-writing-style`'s budget). Early
placement (after the intro) suits papers whose contribution is best seen against a
specific prior design; end placement suits papers whose design needs absorbing
first. Either way, the *intro* must already name the nearest neighbor — burying the
closest competitor until page 11 reads as evasion.

## Output format

```text
[Lineage audit] HoF / SOSP / OSDI ancestors cited? gaps: <list>
[Recency sweep] last two editions of SOSP, OSDI, EuroSys, ATC checked? finds: <list>
[Matrix] nearest neighbor + decisive axis + section pointer
[Blind check] self-citations third person? credits deferred?
[Concurrent] known unpublished competitors + handling plan
```
