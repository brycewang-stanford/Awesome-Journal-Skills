---
name: colt-related-work
description: Use when positioning a COLT (Conference on Learning Theory) submission against prior bounds and models — building the known-versus-new comparison across COLT/ALT lineage, STOC/FOCS, NeurIPS-and-ICML theory tracks, statistics journals, and arXiv concurrency, while respecting anonymity and the parallel-submission rules.
---

# COLT Related Work

At COLT, related work is quantitative: the reviewer wants to know exactly which bound,
in exactly which model, your result improves, matches, generalizes, or separates.
Prose adjacency ("much work has studied bandits") is filler; a rates table is
evidence. Use this skill to build the comparison and to keep it eligible under the
current CFP's overlap rules.

## The known-vs-new ledger

For each of your main results, fill one row per nearest prior result:

| Prior result | Model / assumptions | Their bound | Your bound | Delta type |
|---|---|---|---|---|
| [Cite] Thm 4 | oblivious adversary, K arms | $O(\sqrt{TK\log K})$ | $O(\sqrt{TK})$ | log-factor removal |
| [Cite] Thm 1 | i.i.d., realizable | $O(d/\epsilon)$ | same rate, weaker assumption | assumption weakening |
| [Cite] | same model | lower bound $\Omega(\sqrt{TK})$ | upper matches | closes their gap |

Delta types COLT reviewers recognize as contributions: closing an upper/lower gap,
removing a log factor with a new technique, weakening assumptions at the same rate, a
new model with a separation from an old one, a simpler proof of a known result (yes —
if genuinely simpler, say so plainly), and resolving a posed open problem.

## Literature lanes to cover

| Lane | Where it lives | What the reviewer checks |
|---|---|---|
| COLT/ALT lineage | PMLR volumes (e.g., v247 = COLT 2024, v291 = COLT 2025), ALT proceedings | Whether you know the direct predecessors and cite the newest ones |
| CS theory | STOC, FOCS, SODA, ITCS | Whether complexity/lower-bound machinery is attributed correctly |
| ML theory tracks | NeurIPS, ICML, AISTATS theory papers | Whether a recent conference paper already claims your rate |
| Statistics and probability | Annals of Statistics, JMLR, Bernoulli, probability literature | Whether your "new" phenomenon is classical under another name |
| Open problems | COLT open-problem pieces (e.g., PMLR v65:4-7) | Whether you cite the problem you are solving — and claim credit for it |

A bibliography missing the statistics lane invites the deadliest COLT review sentence:
"this is a known result in the empirical-process literature." Search old names for
your objects (regret has cousins in sequential analysis; PAC bounds have cousins in
empirical processes) before claiming firsts.

## Open problems as positioning assets

COLT maintains a tradition of published open problems (short, citable pieces in the
proceedings — see the exemplars library for a verified instance). If your paper
resolves or dents one:

- cite the open-problem piece itself, state which part you resolve, and quote the
  posed question's parameters honestly — partial resolutions must say so;
- expect the problem's posers as likely reviewers, and write accordingly.

## Concurrency and arXiv norms

The theory community posts to arXiv aggressively, so collisions are routine:

- Concurrent arXiv work discovered before the deadline: cite it, mark it as
  concurrent and independent, and state the technical difference without priority
  litigation — reviewers verify tone here.
- Work appearing after submission: raise it in the rebuttal proactively if reviewers
  will find it anyway; silence looks worse.
- Your own prior arXiv version of this paper is not prior work; do not cite it in a
  way that de-anonymizes (see `colt-submission` for the anonymity sweep).
- The 2026 CFP barred parallel submission to journals and to proceedings venues of
  substantially similar work (verified 2026-07-08); the related-work section is where
  such overlap becomes visible, so audit your own citations for it.

## Citation mechanics

Cite PMLR-published COLT papers by volume; the canonical form:

```bibtex
@inproceedings{rakhlin11beyond,
  title     = {Online Learning: Beyond Regret},
  author    = {Rakhlin, Alexander and Sridharan, Karthik and Tewari, Ambuj},
  booktitle = {Proceedings of the 24th Annual Conference on Learning Theory},
  series    = {Proceedings of Machine Learning Research},
  volume    = {19},
  pages     = {559--594},
  year      = {2011},
  publisher = {PMLR}
}
```

(Entry verified against proceedings.mlr.press/v19/rakhlin11a.html on 2026-07-08.)
Cite theorem numbers, not just papers, when you invoke a specific bound — "[23,
Thm 3.2]" is house style and lets referees check your usage in seconds.

## A search protocol that catches the deadly citation

1. Enumerate your objects under alternate names: regret ↔ sequential prediction error
   in sequential analysis; sample complexity ↔ rates of convergence in nonparametric
   statistics; margin bounds ↔ empirical-process localization.
2. Sweep DBLP's COLT/ALT indices for the last five editions on your model keywords,
   then chase citations backward from the two nearest hits.
3. Search arXiv for the last twelve months on the model name and the bound form —
   this is the concurrency sweep, repeated once more in rebuttal week.
4. Check whether a COLT open-problem piece poses your question; solving one unknowingly
   wastes the single best positioning sentence available to you.
5. For every external theorem you invoke, cite the original source, not the survey
   you learned it from — theorists notice laundering through textbooks.

## Anti-patterns

- A paragraph-per-paper related-work section with no comparison table.
- Citing surveys where the reviewer expects the original theorem's source.
- "To the best of our knowledge, this is the first..." without a search story; scope
  the claim to a named model class instead.
- Comparing against a prior bound while quietly changing its model (their adaptive
  adversary, your oblivious one) — reviewers catch model-shifted comparisons and read
  them as either carelessness or spin.

## Cycle-volatility warnings

- Overlap and dual-submission wording is re-issued each cycle; the rules summarized
  here are the 2026 text (待核实 in later cycles).
- Whether an Open Problems track runs in the current cycle must be checked in the
  live CFP.

## Output format

```text
[Ledger status] complete / rows missing for <results>
[Nearest prior work] <paper, theorem, exact bound>
[Delta type] gap-closing / log-removal / assumption-weakening / separation / simpler proof / open-problem resolution
[Lane coverage] COLT-ALT / CS-theory / ML-tracks / statistics / open-problems
[Overlap risk] none / concurrent arXiv / eligibility issue to declare
```
