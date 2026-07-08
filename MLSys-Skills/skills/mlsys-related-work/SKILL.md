---
name: mlsys-related-work
description: Use when positioning an MLSys submission against the fast-moving ML-systems literature scattered across OSDI, SOSP, NSDI, ASPLOS, and ML venues, handling arXiv-first and open-source-first prior work, comparing against production systems that have no paper, and writing the delta statement two reviewer cultures will both accept.
---

# MLSys Related Work

Use this to audit positioning and novelty. The core difficulty is that MLSys's literature
does not live at MLSys: the field's landmark systems are spread across OS, architecture,
networking, and ML conferences, plus arXiv reports and repositories that never became
papers. A related-work section here is judged on whether it maps that whole territory,
not one venue's proceedings.

## The five lanes to cover

| Lane | Where it publishes | What reviewers check |
|---|---|---|
| ML-systems venue work | MLSys proceedings (proceedings.mlsys.org) | Do you know this venue's own line on your topic? |
| Classical systems venues | OSDI, SOSP, NSDI, ASPLOS, ATC, EuroSys, SC | Is the nearest big-venue system compared or distinguished? |
| ML algorithm venues | NeurIPS, ICML, ICLR | Does the ML-side idea you accelerate/serve already have algorithmic competitors? |
| Industry systems | arXiv reports, engineering blogs, open-source repos | Are the systems practitioners actually use acknowledged? |
| Benchmarks/measurement | MLPerf/MLCommons line, characterization studies | Is your evaluation methodology situated, not invented? |

A bibliography drawing on only one or two lanes signals to half the reviewer pool that
their community's prior work is being rediscovered.

## The freshness problem

ML-systems moves on a months-scale clock: serving engines, compilers, and quantization
methods ship major improvements between your experiments and your reviews.

- Re-run a literature sweep in the final month before the deadline (in the 2026 cycle:
  October), specifically for new arXiv postings and release notes of your baselines.
- Pin the exact version/commit of every compared system in the paper; "we compare
  against X" without a version is unanswerable when X improves next month.
- Reviews arrive months after submission (January, for the 2026 cycle). Expect "why not
  compare against Y?" where Y postdates your submission — you cannot pre-cite it, but
  you can pre-empt the mechanism: if Y's approach is a known design point, place it in
  your taxonomy even before a specific system ships.

## Comparing against work without papers

Production and open-source systems are legitimate, expected comparison points here:

- Cite repositories and technical reports with version/commit and access date; treat a
  README's performance claims as claims, not results.
- If the practitioner-standard system is closed (a cloud provider's serving stack),
  say so and compare against the strongest open proxy, naming the gap honestly.
- Never dismiss an unpublished system as "not peer-reviewed" — to a systems reviewer
  who runs it daily, that reads as evasion.

```bibtex
@misc{vllm2025,
  title        = {vLLM (release v0.x.y)},
  howpublished = {\url{https://github.com/vllm-project/vllm}},
  note         = {Commit abc1234, accessed 2026-07-08; evaluated configuration in App.~B},
  year         = {2026}
}
```

## Writing the delta statement

Both reviewer cultures must find their contrast:

- **Against the nearest system**: what mechanism differs, and what measured behavior
  changes because of it — "unlike X's reactive swapping, we schedule migrations into
  predicted bubbles, which is why the p99 gap appears only under bursty load."
- **Against the nearest algorithm**: what your systems constraints add — "batching-aware
  variants of this idea exist [7]; none address multi-tenant memory pressure."
- Comparison tables (rows: systems; columns: capabilities) are venue-idiomatic and
  efficient, but every checkmark against a competitor must be defensible from their
  paper or code — reviewers include those systems' authors.

## Building the capability table honestly

The venue-idiomatic comparison table is powerful and dangerous. Rules that keep it
defensible when the compared systems' authors review you:

- Columns are *capabilities the paper evaluates*, not marketing attributes; a column
  never exercised in the evaluation does not belong in the table.
- Every negative cell (✗ for a competitor) carries a citation or footnote to where
  that limitation is documented — their paper, their docs, or your measured attempt.
- Version-stamp the table: a system's ✗ can become ✓ in next month's release, and a
  reviewer running the newer version will check.
- Include the row where a competitor beats you, if the evaluation shows one; a table
  where the proposed system sweeps every column is read as curated, and curation in
  the comparison table contaminates trust in the results tables.

Worked contrast sentence, fictional serving-scheduler paper: "Orca-style iteration-level
scheduling [4] and reactive expert swapping [9] both target utilization; the former
assumes dense models, the latter pays migration on the critical path. Our planner
addresses the MoE case the former excludes, using the bubble structure the latter
ignores — Section 6.3 measures both boundaries." Two named systems, two mechanism-level
gaps, one pointer to where the claims are tested.

## Misattribution traps

- Do not cite famous ML-systems work to the wrong venue (vLLM is SOSP, PipeDream is
  SOSP, FlashAttention is NeurIPS); this venue's reviewers notice. Verified MLSys-native
  exemplars live in `../../resources/exemplars/library.md`.
- Do not claim "first to X" in a field with a large gray literature; write "to our
  knowledge, the first published system that X" and let the evidence carry it.
- Concurrent work that appeared during your project deserves a neutral sentence and a
  mechanism-level contrast, not silence — silence looks like either ignorance or fear.

## Scoping the search itself

- Search the venue's own archive first (proceedings.mlsys.org is small enough to scan
  a topic exhaustively in an hour) — missing an MLSys-native predecessor is the least
  forgivable gap at MLSys.
- Then sweep the last two editions of each systems venue in your lane, then the
  ML-venue "efficient ML" tracks, then arXiv's recent months; breadth-first by
  community, not depth-first by citation chain, or one community's chain will crowd
  out the others.

## Double-blind interaction

Cite your own prior systems in third person, and be careful with self-identifying
version lineages ("we extend our earlier scheduler" → "we extend the scheduler of
[12]"). arXiv posting of the submission itself is permitted (2026 rule), but the
related-work text must not link the submission to that preprint.

## Output format

```text
[Lane coverage] <mlsys-native/systems-venues/ML-venues/industry/benchmarks: present?>
[Nearest neighbors] <top 3 with venue + version/commit where applicable>
[Delta statement] <mechanism contrast + measured-behavior contrast>
[Freshness] <last sweep date; baselines pinned?>
[Misattribution/overlap risks] <wrong-venue cites, "first" claims, concurrent work>
[Fixes] <ordered list>
```
