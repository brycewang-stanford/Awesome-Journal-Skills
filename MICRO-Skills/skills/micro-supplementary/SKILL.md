---
name: micro-supplementary
description: Use when deciding where a MICRO paper's supporting material lives, because MICRO allows no appendix at all — triaging content into the 11 reviewed pages, the unlimited references, an anonymized artifact repository, or the post-acceptance two-page artifact appendix, and cutting what fits nowhere.
---

# MICRO Supplementary Material

Most conference packs teach how to *organize* an appendix. MICRO needs the opposite
skill: the 2026 submission guidelines allow **11 content pages, unlimited
references, and no appendix whatsoever**. There is no supplementary PDF upload and
no "reviewers may optionally read" tier. Everything either earns a place in the 11
pages, moves to an artifact repository, or gets cut. This skill is the triage.

## The four legal destinations

| Destination | Review status | What belongs there |
|---|---|---|
| 11 content pages | Reviewed, binding | Anything a reviewer needs to judge correctness or significance |
| References (unlimited) | Reviewed | Full citation record — every entry with all authors named, no "et al." |
| Anonymized artifact repo (linked) | **Not** owed a read | Configs, raw stats, extra sweeps, trace recipes, proofs of side claims |
| Camera-ready artifact appendix (≤ 2 pages, post-AE, 2025 pattern) | Post-acceptance only | How to reproduce — hardware/software requirements, run steps |

Two consequences follow immediately:

1. **Nothing decision-critical may live outside the 11 pages.** Reviewers are not
   obligated to open the artifact link, and many will not while anonymous. If the
   security argument, the key ablation, or the storage accounting is only in the
   repo, the paper is incomplete as reviewed.
2. **The link itself is regulated.** Artifact links must be fully anonymized or
   removed (2026 guidelines). An anonymized repo (e.g., an anonymous hosting
   service) is legal; a lab GitHub URL is a desk-level anonymity violation.

## Triage procedure for over-length drafts

When the draft is at 13 pages and the venue gives you 11:

1. **Classify every subsection** as `judge` (reviewer needs it to score the paper),
   `trust` (supports a claim but a summary sentence + repo pointer suffices), or
   `nice` (context, extra results, alternate configs).
2. `judge` stays, compressed: convert prose methodology into the config table,
   merge redundant ablation figures, tighten the walkthrough.
3. `trust` becomes one sentence with a forward pointer: "the full 48-workload sweep
   (repo, `sweeps/`) matches the subset shown."
4. `nice` is deleted. Not moved — deleted. MICRO gives it nowhere to go, and
   "omitted for space" phrasing signals the cut poorly (see `micro-writing-style`).

```text
triage ledger (keep in the repo, not the paper)
------------------------------------------------
S4.3 replacement-policy interaction   judge   compress to half column
S5.6 per-benchmark IPC traces          trust   1 sentence + repo path stats/traces/
S5.7 alternate 14nm power results      nice    cut; keep runnable in repo
S6.2 sensitivity beyond 8 cores        trust   fold into Fig. 9 right panel
```

## What the artifact repo should contain at submission time

Even though nobody owes it a read, a well-stocked anonymous repo pays twice — some
reviewers do open it, and it becomes the AE package with zero rework in August:

- Run manifests + raw statistics for every figure (see `micro-reproducibility`).
- Simulator patches and full config files for baseline, mechanism, and ablations.
- Trace-generation recipes (not the traces themselves if licensing forbids —
  SPEC binaries cannot be redistributed; scripts and flags can).
- A top-level README with a figure-to-directory map, scrubbed of identity.

## Reviewer psychology around the link

Assume three reader types and satisfy all three:

1. **Never opens the repo** (the majority while anonymous). The 11 pages must
   carry the full argument — this reader is the reason nothing decision-critical
   leaves the body.
2. **Opens it to spot-check** one claim that bothered them. The figure-to-data
   map in the README decides whether this visit builds or burns trust; a maze of
   undocumented directories reads as concealment.
3. **Opens it forensically** — a methodology-minded reviewer diffing your configs
   against the paper's tables. Config files that contradict the methodology
   section are worse than no link at all; regenerate both from one source.

If institutional or licensing constraints forbid sharing anything at submission
time, say so in the paper in one neutral sentence and rest the case entirely on
the 11 pages — a missing link is survivable, a broken or identity-leaking one is
not.

## Camera-ready appendix (the one appendix MICRO permits)

After acceptance and successful artifact evaluation, MICRO's recent cycles (2025
verified; 2026 待核实) let authors add a **two-page artifact appendix, free of
charge**, describing requirements and reproduction steps. Draft it from the repo
README — it is the only place appendix-style material ever reaches the PDF, and it
arrives at camera-ready, not submission.

## Compression techniques that reclaim body space honestly

Before cutting `judge`-class content, reclaim space that formatting rules allow:

- Convert methodology prose into the config table — a half-page paragraph
  usually compresses to six table rows with zero information loss.
- Merge single-question figures: two ablation bar charts sharing an x-axis
  become one two-panel figure with one caption.
- Replace repeated config descriptions with a named-config shorthand defined
  once ("cfg-A = Table 2 plus 16 cores").
- Prune the intro's second background paragraph — at MICRO the audience arrives
  knowing what a cache is; the characterization data *is* the background.

What never gets compressed away: the storage-budget table, the overhead rows,
the sampling recipe, and the worst-case regression sentence — cutting any of
those to fit is trading a format problem for a review problem.

## Output format

```text
[Appendix check] draft contains appendix material: none / found (list — must be cleared)
[Triage] judge: <sections> · trust: <sections + pointer sentences drafted> · nice: <cut list>
[Page result] content pages after triage: N/11
[Repo] anonymized: yes / no · figure-to-data map complete: yes / no
[Link policy] every artifact link anonymized-or-removed: confirmed / violations
[AE seed] repo doubles as artifact package: ready / gaps listed
```
