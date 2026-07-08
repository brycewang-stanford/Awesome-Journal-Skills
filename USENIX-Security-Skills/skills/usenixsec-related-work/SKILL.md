---
name: usenixsec-related-work
description: Use when positioning a USENIX Security Symposium paper against prior work — covering the Big-Four security venues plus specialty conferences, handling concurrent submissions across the multi-cycle calendar, citing your own work double-blind, and using USENIX's open-access proceedings for verification.
---

# USENIX Security Related Work

Related work at USENIX Security is an adversarial exercise: the committee contains
people who wrote the nearest prior papers, and the multi-cycle Big-Four calendar
means the nearest prior paper may be four months old. This skill covers coverage,
differentiation, and the venue's citation mechanics.

## The coverage map reviewers apply

| Lane | Where it lives | The question your text must answer |
|---|---|---|
| Big-Four security | USENIX Security, IEEE S&P, ACM CCS, NDSS | Same problem, same class of technique — what's new here? |
| Specialty security | PETS, SOUPS, RAID, ACSAC, WOOT, DIMVA, ESORICS | Did the niche community already do this at smaller scale? |
| Adjacent systems/ML | OSDI/SOSP, SIGCOMM/IMC, NeurIPS/ICML | Is the "security" contribution a re-badged systems or ML result? |
| Industry/offense track record | Black Hat/DEF CON talks, vendor blogs, CVE history | Do practitioners already know this? (Reviewers here often do) |
| Preprints and the cycle pipeline | arXiv, prior cycles' accepted-paper lists | What landed in the last 6–12 months that you must acknowledge? |

The fourth lane is distinctive: at this venue, an attack "known in the community"
via a conference talk or advisory — even without an academic paper — weakens a
novelty claim, and reviewers will cite the talk. Search offensive-industry sources,
not just DBLP.

## Freshness under a two-cycle regime

With USENIX Security itself, CCS, NDSS, and S&P all running multiple deadlines,
the relevant literature refreshes roughly every quarter. Concretely:

- Sweep the **accepted-papers pages of every Big-Four cycle that concluded after
  your last literature pass** (e.g., a Sec '27 Cycle-1 submission in Aug 2026
  should have digested Sec '26 Cycle-2 acceptances announced May 2026).
- USENIX helps you here: its proceedings are open access on usenix.org, so
  verification against the actual PDF costs nothing. Do the same via each venue's
  accepted-paper listings.
- Genuinely concurrent work (public after your submission, or within the same
  cycle window) merits acknowledgment, not differentiation-by-contortion.
  Reviewers know the calendar; say "concurrently and independently" and state the
  factual differences.

## Differentiation that survives expert readers

Comparison tables of checkmarks read as advertising. The pattern that works here
is mechanism-level: state what the prior system assumed or measured, then the
delta. Three useful framings:

1. **Threat-model delta** — "X defends against a network adversary; we handle a
   co-resident one, which breaks X's core assumption (shared cache is trusted)."
2. **Scale/vantage delta** — "prior measurements covered one ccTLD from a single
   vantage; we cover 214 TLDs from 14 vantage points, and Section 6 shows the
   single-vantage view misestimates prevalence by 3×."
3. **Evidence delta** — "Y's evaluation is simulation-only; we demonstrate the
   attack end-to-end on production hardware."

If the honest delta is "same idea, better engineering," consider whether the
contribution framing should change before the related-work section does (see
`usenixsec-topic-selection`).

## Double-blind citation mechanics

Cite your own prior work in the third person as if written by strangers; the '26
CFP names first-person self-reference as an anonymity violation. When a paper
builds so directly on your unpublished or just-published system that third person
fails, the mitigation hierarchy is: cite an anonymized tech report in the artifact
mirror; failing that, consult the chairs — never silently omit a paper reviewers
will know exists, since a missing obvious citation both distorts positioning and
fingerprints the authors.

```bibtex
@inproceedings{example-sec24,
  author    = {Doe, Jane and Roe, Riley},
  title     = {Sample: What a USENIX Security Reference Looks Like},
  booktitle = {33rd USENIX Security Symposium (USENIX Security 24)},
  year      = {2024},
  publisher = {USENIX Association},
  url       = {https://www.usenix.org/conference/usenixsecurity24/presentation/...}
}
```

Verify metadata against the usenix.org presentation page or DBLP's `conf/uss`
stream; both were consistent sources historically (DBLP direct fetch 403'd in this
environment on 2026-07-08 — cross-check via search rendering if needed).

## Placement and length

Related work usually closes the body (≈1 page of the 13). Two exceptions worth
making: an attack paper whose novelty hinges on a subtle difference from a known
technique should differentiate **early**, in the introduction; SoK-style framing
(if pursued at all — check the current CFP for whether the venue solicits it,
待核实) makes the literature the paper's subject rather than its perimeter.

## Reverify each cycle

- Accepted-paper lists of all Big-Four cycles concluded since the last sweep.
- Whether the current CFP says anything about citing concurrent work or preprints.
- Anonymity wording around self-citation.

## Output format

```text
[Coverage] five lanes swept, with dates of the last sweep per lane
[Nearest neighbors] top 3–5 with mechanism-level deltas drafted
[Concurrent] same-window items + acknowledgment wording
[Self-citations] third-person rewrite check: pass / violations listed
```
