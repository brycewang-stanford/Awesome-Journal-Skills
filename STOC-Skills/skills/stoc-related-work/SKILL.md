---
name: stoc-related-work
description: Use when positioning a STOC (ACM Symposium on Theory of Computing) paper against the theory literature — tracing bound-improvement lineages, citing conference/journal/preprint version pairs correctly, handling concurrent arXiv and ECCC work, and keeping self-citation double-blind-safe.
---

# STOC Related Work

Theory positioning is quantitative: reviewers expect the paper to place its
bounds in an explicit lineage ("[A] gave $O(n^2)$; [B] improved to
$O(n \log n)$ under assumption X; we remove X and reach $O(n)$"), and they
check the lineage against their own memory of it. Errors here — a missed
improvement, a misquoted exponent, a result attributed to the journal version's
year instead of the conference announcement — are among the fastest credibility
losses available at this venue.

## The lanes a STOC reviewer checks

| Lane | What must be covered | Typical miss |
|---|---|---|
| The direct lineage | Every prior bound on your exact problem, with its model | Quoting the weakest prior bound to inflate the delta |
| The barrier literature | Known obstructions your result confronts (relativization, natural proofs, hardness reductions, integrality gaps) | Claiming a breakthrough while silent on why the barrier does not apply |
| Neighboring models | The same question in weaker/stronger models (randomized vs. deterministic, static vs. dynamic, classical vs. quantum) | "First" claims that are only first in one cell of the model grid |
| Technique ancestry | Where your machinery comes from, even from other subfields | Reviewers who invented the machinery are plausibly your reviewers |
| Concurrent work | Recent arXiv/ECCC preprints on the problem | The subreviewer knows about last month's preprint; your draft predates it |

## Version-aware citation, a theory-specific craft

Most important theory results exist as a conference extended abstract, a later
journal version, and a preprint — and they can differ mathematically (bounds
improve; bugs get fixed in the journal version). House rules:

- Cite the version whose *statement you actually use*. If you invoke the
  strengthened journal bound, cite the journal paper, possibly alongside the
  conference announcement.
- Date claims by first announcement (conference or preprint), attribute proofs
  by where the complete proof appears.
- Keep both versions in the entry when the community habitually does:

```bibtex
@inproceedings{ST01-smoothed,
  author    = {Spielman, Daniel A. and Teng, Shang-Hua},
  title     = {Smoothed Analysis of Algorithms: Why the Simplex Algorithm
               Usually Takes Polynomial Time},
  booktitle = {Proc. 33rd ACM Symposium on Theory of Computing (STOC)},
  pages     = {296--305},
  year      = {2001},
  note      = {Journal version: J. ACM 51(3), 2004}
}
```

- dblp is the community's canonical metadata source; export entries from it
  rather than hand-typing venues, and prefer its conference/journal splitting
  over publisher aggregator records.

## Concurrent and independent work

The arXiv/ECCC-first culture means collisions are visible within days, not
years. Norms as practiced:

- A concurrent preprint (posted around your submission, obtained independently)
  gets a clearly flagged paragraph — "Independently and concurrently, [Z]
  obtained..." — with an honest comparison of strength, generality, and
  technique. Committees routinely accept both papers when the note is fair.
- A *prior* preprint you missed is not concurrent work; the delta must be
  recomputed against it, sometimes fatally. Run a fresh arXiv/ECCC sweep the
  week before the deadline, and again before camera-ready.
- If a collision surfaces mid-review, current practice varies on whether and
  how to notify the chair; check the cycle's instructions (待核实) rather than
  improvising contact with the PC.

## Double-blind self-positioning

STOC 2026 was double-blind (checked 2026-07-08). Your prior work is often the
nearest related work, so:

- Cite yourself in third person, with no ownership markers ("building on the
  framework of [7]" — not "our framework [7]").
- Do not cite an unpublished manuscript of yours that only the authors could
  possess; if the submission genuinely depends on it, it must be publicly
  posted (anonymity-compatibly) or its content inlined.
- Acknowledgement-style thanks to collaborators on adjacent work wait for
  camera-ready.

## Building the comparison honestly

- State comparisons in the prior work's own parameterization before yours;
  translating everything into the units most flattering to your bound is
  spotted immediately by the lane-one reviewer.
- When your result is incomparable to a prior one (better dependence on $n$,
  worse on $\varepsilon$), say "incomparable" and give the crossover point —
  that sentence pre-empts the review question (`stoc-author-response`'s
  objection ledger).
- A small comparison table in the introduction (result, model, bound, source)
  is house-standard for crowded problems and often becomes the most-read
  object in the paper.

## The deadline-week sweep, as a procedure

1. Search arXiv (`cs.DS`, `cs.CC`, and your problem's other categories) and
   ECCC for the problem's standard names and their variants; theory titles are
   conventional enough that keyword search works.
2. Check the most recent STOC/FOCS/SODA accepted-paper lists — results
   announced there may not have preprints yet.
3. Walk the dblp pages of the five authors most active on the problem; new
   preprints appear there within days.
4. For each hit, classify: prior (delta must be recomputed), concurrent
   (comparison paragraph), or unrelated-despite-title (note why, for your own
   future reference).
5. Re-run the same sweep before camera-ready; the February-to-March window
   regularly produces new lineage entries that the full version should cite.

## Cycle-volatility warnings

- Anonymity rules for citing your own preprints follow the live CFP's
  double-blind wording (待核实 per cycle; the policy is new at STOC and may be
  refined).
- Deadline-week literature sweeps must include ECCC and the current FOCS/SODA
  accepted-paper lists, which shift the frontier between CFPs.

## Output format

```text
[Lineage table] complete / gaps: <missing bounds or models>
[Barrier account] addressed / silent <- fix before review
[Version hygiene] statements matched to cited versions? dblp-verified?
[Concurrency] <preprints found in final sweep; comparison note drafted?>
[Self-citation] double-blind-safe / leaks: <list>
```
