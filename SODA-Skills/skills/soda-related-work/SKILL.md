---
name: soda-related-work
description: Use when positioning a SODA (ACM-SIAM Symposium on Discrete Algorithms) paper in the algorithms literature — tracing bound lineages across SODA/STOC/FOCS/ESA/ICALP and journals, handling arXiv-first priority culture, citing conference versus journal versions correctly, and self-citation under lightweight double-blind rules.
---

# SODA Related Work

Positioning at SODA is quantitative: the related-work section's job is to
establish, bound by bound, exactly where your result sits in a lineage the
referees already know. The most common positioning failure is not a missing
citation but a *mis-stated bound* — quoting a superseded conference version,
missing a stronger journal version, or comparing against the randomized bound
when a better deterministic one exists.

## The five lanes to sweep

| Lane | Where it lives | What referees check |
|---|---|---|
| Direct predecessors | SODA/STOC/FOCS/ESA/ICALP proceedings, arXiv | Is the displaced bound the true state of the art? |
| Journal consolidations | SICOMP, JACM, ACM ToA, Algorithmica | Did the journal version strengthen the bound you quote? |
| Lower bounds / hardness | Same venues + ITCS, CCC | Does a conditional lower bound cap your claimed improvement's meaning? |
| Concurrent arXiv postings | arXiv (last ~18 months) | Anything simultaneous that changes the delta |
| Adjacent-model results | Distributed (PODC/DISC), parallel (SPAA), geometry (SoCG), dynamic/streaming lines | Incomparable-but-related results a subreviewer will ask about |

The concurrent lane is the one that changes late: re-sweep arXiv in the final
week before the July deadline and again before the September rebuttal — a
concurrent improvement discovered by the referee but unacknowledged by you turns
a coexistence story into a credibility problem.

## Bound-lineage verification recipe

For every row of your comparison table (`soda-writing-style`):

```text
1. Find the paper's dblp entry (dblp.org) — canonical venue + year.
2. Check for a journal version listed alongside the conference version;
   if one exists, read ITS abstract for the strongest stated bound.
3. Check the arXiv page for post-publication revisions or errata.
4. Quote: strongest bound, both versions cited ("[SODA 2019; SICOMP 2021]"),
   with the model/caveat column filled from the actual theorem statement.
5. If two papers claim the same bound, cite both and let dblp dates
   order them — do not adjudicate priority disputes in your paper.
```

## arXiv-first culture and priority

The algorithms community treats arXiv posting as the priority event and the
conference as certification. Consequences for positioning:

- Cite arXiv preprints of results you use or displace — refusing to engage with
  a well-known preprint because it is "unpublished" reads as gamesmanship.
  Distinguish status in the bibliography (`arXiv:2401.xxxxx, preprint`).
- If your result was scooped between writing and deadline, the honest structure
  is a "concurrent and independent work" paragraph stating both results'
  deltas — PCs routinely accept parallel discoveries when the relationship is
  cleanly disclosed.
- Your own posting strategy: SODA permits arXiv dissemination before and during
  review (2027 CFP, checked 2026-07-08), so establishing priority early is free.

## Self-citation under lightweight double-blind

SODA's double-blind rules explicitly require that important references *not* be
omitted or anonymized (`soda-submission`). So:

- Cite your prior work in third person, fully: "extending the decomposition of
  [14]" — never "our decomposition [14]," and never a blanked "[anonymized]."
- A direct predecessor paper of yours belongs in the comparison table like
  anyone else's; suppressing it to "look more novel" is the actual violation.
- Do not cite an in-submission companion manuscript that referees cannot read;
  if the companion is load-bearing, post it to arXiv first.

## Bibliography mechanics for dual-version results

The conference/journal duality has a concrete BibTeX answer — cite both, quote
the strongest:

```bibtex
% Conference announcement:
@inproceedings{HLRW24soda, ... booktitle = {SODA}, year = {2024}, ... }
% If a journal version exists, add and PREFER its bound:
@article{HLRW26sicomp, ... journal = {SIAM J. Comput.}, ... }
% In text: "achieves O(m log^2 n) [HLRW24soda; journal version HLRW26sicomp]"
```

Hygiene rules that referees notice when violated:

- Never cite an arXiv identifier for a result that has a published version —
  it suggests the sweep stopped at the preprint.
- Never quote a bound from a paper's abstract; abstracts round. Quote the
  theorem, with its number if your comparison is load-bearing.
- Keep dblp keys or DOIs in comments next to each entry so the September
  rebuttal and the October camera-ready don't re-litigate attribution.
- Alphabetic-initial citation labels ([HLRW24]) are house convention in theory
  bibliographies; numeric labels work, but author-initial labels make your
  comparison table readable without flipping to the references.

## Positioning prose patterns

- **Lineage sentence:** "For dynamic connectivity, worst-case bounds improved
  from `O(sqrt n)` [F] through `n^{o(1)}` [NSW] to the current `polylog`
  amortized bounds [HdLT; journal version]." Three citations, one sentence, and
  the referee knows you know the field.
- **Incomparability paragraph:** for results that trade parameters ("faster but
  randomized," "deterministic but amortized"), state the trade explicitly
  instead of claiming dominance.
- **Technique genealogy:** name where your tools come from ("our charging
  argument adapts [X]'s token scheme") — theory culture rewards disclosed
  intellectual debts and punishes discovered ones.

## Output format

```text
[Lineage verdict] Sound / Gaps / Mis-stated bounds found
[Lane sweep] <per-lane findings, incl. concurrent arXiv window>
[Version errors] <rows quoting superseded or weaker versions>
[Self-citation audit] <third-person compliance; nothing omitted or anonymized>
[Table repairs] <rows to add, bounds to correct, caveats to co-locate>
```
