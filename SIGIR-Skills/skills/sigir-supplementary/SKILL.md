---
name: sigir-supplementary
description: Use when deciding what goes inside a SIGIR paper's page budget versus the cited repository — SIGIR counts appendices inside the 9-page (full) and 4-page (short) limits with only references free, so overflow material must be re-homed into run files, repository docs, or cut, without hiding review-critical evidence outside the paper.
---

# SIGIR Supplementary

SIGIR has no appendix escape hatch. The 2025 full-paper wording (the clearest recent
statement of the standing rule) caps papers at 9 pages **including figures, tables,
proofs, appendixes, and acknowledgments — everything except references**; the 2026
pages restate the budgets as 9/4 pages excluding references. There is no separate
supplementary upload in the NeurIPS sense on the verified track pages. Overflow
therefore has exactly three destinations: compression, the cited repository, or the
bin. This skill is the triage protocol.

## The three-container model

| Container | What belongs there | What must never be there |
|---|---|---|
| Paper body (9 or 4 pp) | Every claim a reviewer must verify to accept: method, main tables, significance results, tuning protocol summary, limitations | Filler related work, per-query dumps, prompt walls |
| References (free) | Complete citations — never trimmed for space | Content smuggled into bibnotes |
| Cited repository | Run files, full configs, per-query analyses, extra collections, prompts, proofs of secondary lemmas, negative results | Anything acceptance depends on |

The governing rule: **reviewers must be able to accept the paper without opening the
repository.** Track pages do not oblige reviewers to consult external material, so
evidence that lives only in the repo is evidence that may not exist for review.

## What earns its place in the budget

Rank candidate content by review-criticality, not by effort spent producing it:

1. The comparison table that carries the main claim, with significance markers.
2. The tuning-protocol paragraph (symmetric budgets, dev split) — its absence is a
   standing SIGIR objection.
3. One ablation table that isolates the mechanism.
4. The evaluation-setup block: collections, metrics with cutoffs, qrels versions.
5. Error/qualitative analysis — one distilled example pattern, not a gallery.
6. Efficiency numbers if the claim mentions cost, latency, or scale at all.

What loses its seat first: exhaustive metric grids (report the pre-registered ones;
put the grid in the repo), second and third qualitative examples, restated
definitions of standard metrics, and architecture recaps of well-known baselines.

## Compression before amputation

```latex
% Honest space wins that don't touch \vspace (which risks desk rejection):
% 1. Merge setup prose into the table caption.
\caption{nDCG@10 on \colA{} and \colB{}. Paired t-test vs BM25,
         Bonferroni-corrected; $\dagger$: $p<0.05$. 3 seeds, mean$\pm$sd.}
% 2. One combined results table with grouped columns beats three tables.
% 3. booktabs + \small in tables (allowed by class) before cutting content.
% 4. Inline enumerations for contribution lists; drop the roadmap paragraph.
```

Never buy space by deleting the significance-testing sentence, the seed count, or
the collection versions — those cuts convert a space problem into a soundness
objection, which is a worse trade at this venue than a missing extra ablation.

## Repository-as-appendix discipline

If the paper says "details in the repository," the repository must behave like an
appendix, not a junk drawer:

- A `PAPER_MAP.md` that mirrors the paper's section numbering: "§5.2 ablation →
  `eval/ablation_table.md` + `runs/ablate_*.trec`."
- Per-query result files for every table, so a skeptical reviewer can drill down.
- The full hyperparameter grid with the selected cell marked.
- Anonymized for double-blind tracks (fresh export, no usernames); the Resources
  track's single-anonymous regime is the exception, not the rule.

Cross-references must be one-directional: the paper points to the repo; the repo
never contains claims absent from the paper (reviewers cannot credit them, and
policy-wise unreviewed claims must not ride into the version of record later).

## Worked micro-triage

A full-paper draft sits at 10.5 pages against the 9-page budget. Candidate cuts:

1. A 0.6-page per-query case-study gallery (three annotated examples) → keep **one**
   example that names the diagnosed pattern; the other two move to the repo with
   their run-file coordinates. (-0.4 pp)
2. A 0.5-page secondary-metric grid (five metrics × four collections) → keep the two
   pre-committed metrics; grid to `eval/full_grid.md`. (-0.4 pp)
3. A 0.4-page derivation of a variant loss → state the result, cite the repo
   notebook. (-0.35 pp)
4. The tuning-protocol paragraph — **never**; it pre-answers the venue's most common
   fatal objection.
5. Caption-merge the setup prose and drop the roadmap paragraph. (-0.35 pp)

Net: on budget, with zero soundness loss — every cut demoted redundancy or depth,
not protocol.

## Short papers: the 4-page special case

A short paper has no room for a supplementary strategy — it *is* the strategy.
Standard shape that fits: one focused question, one main table, one analysis
figure, setup compressed into captions, everything else in the repo. If the triage
above still leaves review-critical content homeless, the work is a full paper
submitted to the wrong track; re-route rather than compress soundness away.

## Pre-submission checklist

- [ ] Page count within budget with acknowledgments space reserved (camera-ready
      restores them inside the same budget unless the track says otherwise — 待核实).
- [ ] No review-critical evidence lives only in the repository.
- [ ] Repository PAPER_MAP matches the submitted section numbering.
- [ ] References complete and untrimmed; no content in bibliography notes.
- [ ] No spacing/margin/font tampering; only class-sanctioned sizes used.

## Output format

```text
[Budget state] <pages>/<limit> with acks reserve y/n
[Cut list] <content demoted to repo, in order>
[Kept-by-criticality] main table / tuning protocol / ablation / setup / analysis
[Repo appendix] PAPER_MAP present y/n; per-query files y/n; anonymized y/n
[Soundness guard] significance sentence, seeds, versions all still in-paper y/n
[Re-route flag] none / "this is a full paper in short clothing"
```
