---
name: uai-related-work
description: Use when positioning a UAI submission within the probabilistic reasoning, graphical-model, causality, and Bayesian ML literature, covering PMLR archival status of recent UAI volumes, double-blind self-citation discipline, concurrent arXiv and workshop versions, and the cross-community citation coverage UAI reviewers check first.
---

# UAI Related Work

Use this to audit positioning before submission. UAI sits at a junction of communities —
ML conferences, statistics, causal inference, and the older probabilistic-AI tradition —
and its reviewers typically belong to at least two of them. Related-work failures here
are usually coverage failures: the paper positions against one community and gets
reviewed by another.

## The lanes a UAI reviewer expects covered

| Lane | Where that literature lives | The question the reviewer asks |
|---|---|---|
| Prior UAI work | PMLR volumes (v161 2021, v180 2022, v216 2023, v244 2024, v286 2025) and earlier AUAI-era proceedings | "Do they know this venue already treated this problem?" |
| Sibling ML conferences | AISTATS, NeurIPS, ICML, ICLR | "Is the nearest recent method compared or distinguished?" |
| Statistics literature | JASA, Biometrika, Annals of Statistics, JMLR | "Is there a classical estimator or test that already does this?" |
| Causality community | UAI itself, CLeaR, epidemiology and econometrics journals | "Which identification tradition does this extend — Pearl's graphical or the potential-outcomes one?" |
| Foundations | Decision theory, belief functions, imprecise probability | "If the paper generalizes Bayes, is the relevant non-Bayesian line acknowledged?" |

A causal-discovery submission citing only deep-learning-era papers, or a Bayesian-deep-
learning submission ignoring the statistics literature on calibration, triggers the
"backing" and "novelty" criteria simultaneously.

## Establish the delta, not the bibliography

- For the three closest works, state the technical difference in one sentence each:
  different assumption set, different identification regime, different complexity,
  different guarantee type. "Unlike [7], we do not require faithfulness" beats a
  paragraph of summary.
- If the closest work appeared in the last two UAI or AISTATS cycles, compare
  empirically or explain concretely why comparison is impossible — silence on a
  same-venue neighbor is the most predictable review objection.
- When your contribution weakens an assumption, show what the prior method does when
  that assumption fails; that experiment converts a related-work sentence into evidence.

## Verifying venue attribution

Misattributed citations are common in this corner of ML because UAI, AISTATS, and ICML
all publish through PMLR. Before submission, verify each PMLR citation against its
volume page — the volume, not the paper title, determines the venue. Example of a
correctly attributed UAI entry (metadata verified on the PMLR v161 sources):

```bibtex
@inproceedings{ruiz21a,
  title     = {Unbiased gradient estimation for variational auto-encoders
               using coupled {M}arkov chains},
  author    = {Ruiz, Francisco J. R. and Titsias, Michalis K. and
               Cemgil, Taylan and Doucet, Arnaud},
  booktitle = {Proceedings of the Thirty-Seventh Conference on Uncertainty
               in Artificial Intelligence},
  series    = {Proceedings of Machine Learning Research},
  volume    = {161},
  pages     = {707--717},
  year      = {2021},
  publisher = {PMLR}
}
```

Older UAI papers (pre-PMLR era) live in AUAI Press proceedings; cite them as such rather
than inventing PMLR volumes for them.

## Anonymity mechanics for prior versions

- Cite your own published prior work in the third person, exactly as you would cite a
  stranger's; omitting it entirely is worse, since reviewers who find it will suspect
  concealment.
- The 2026 instructions forbade links that could reveal identity — so no linking your own
  arXiv page or repository from the related-work section.
- Workshop versions and arXiv preprints: UAI's dual-submission concern is other
  archival venues; non-archival workshop exposure and preprints are traditionally
  tolerated at ML conferences, but the current CFP's own wording controls (2026 fine
  print: 待核实 before relying on it).
- Concurrent submissions of the same work to another archival conference violate the
  standard rule; overlapping-but-distinct papers should be disclosed to chairs if the
  form asks.

## A search protocol that finds the embarrassing neighbor

The reviewer most likely to sink a UAI submission is the one who wrote the adjacent
paper you missed. Search deliberately:

1. Sweep the last three UAI volumes' tables of contents (v216, v244, v286 as of this
   pack's check) for your problem's keywords — titles at this venue are unusually
   literal, which makes the sweep fast.
2. Repeat on the last two AISTATS volumes and, for causal work, CLeaR; these pools
   share reviewers with UAI.
3. For each candidate neighbor, read the assumption section before the method
   section; adjacency at UAI is measured in assumptions, not architectures.
4. Trace forward citations of your three closest works for the concurrent-preprint
   layer; note preprints separately since their claims are unrefereed.
5. Log every neighbor with a one-line delta at collection time. Deltas written during
   the deadline sprint degenerate into "differs in setting".

## Deltas that count here, deltas that do not

Positioning language calibrated to this reviewer pool:

- Counts: weaker assumption set, broader graph class, finite-sample instead of
  asymptotic, exact instead of approximate (or a quantified approximation), lower
  complexity with the same guarantee, a guarantee where none existed.
- Counts conditionally: better empirical calibration/coverage — if measured on the
  ladder of regimes, not one benchmark.
- Does not count: "more scalable" without a complexity or wall-clock statement,
  "more flexible" without a named class the prior work excludes, "first deep-learning
  approach to X" when the classical approach is unbeaten.

## Related work as a routing signal

If honest positioning shows the contribution is really about representation learning
with incidental uncertainty, or pure learning theory with no probabilistic-reasoning
core, the related-work audit has just made a venue recommendation — hand off to
`uai-topic-selection` before polishing citations.

## Output format

```text
[Lane coverage] <covered lanes / missing lanes from the table>
[Closest three] <work → one-sentence technical delta>
[Same-venue neighbors] <recent UAI/AISTATS papers compared or explained>
[Attribution check] PMLR volumes verified? AUAI-era citations correct?
[Anonymity] self-citations third-person? no identifying links?
```
