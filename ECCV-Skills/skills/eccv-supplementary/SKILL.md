---
name: eccv-supplementary
description: Use when assembling ECCV supplementary material under its own deadline one week after the paper (March 12 in 2026) — deciding what belongs in the extra week's upload, video and qualitative-result packaging, anonymity scrubbing of archives, and keeping the 14-page LNCS body self-contained.
---

# ECCV Supplementary

Use this when planning the ECCV supplement. ECCV 2026 kept the classic
vision-conference structure the CVF siblings have moved away from: the
supplement had **its own deadline a week after the paper** (paper March 5,
supplement March 12). That week is a gift with sharp edges — the paper is
already frozen, so the supplement can only *support* claims, never *add*
them.

## What the extra week is actually for

Legitimate uses of March 5 → March 12:

- Rendering the qualitative-results PDF and video reels at full quality.
- Finishing the code archive scrub (`eccv-artifact-evaluation`).
- Formatting extended tables and per-category breakdowns already summarized
  in the body.

Illegitimate uses that reviewers punish:

- Landing a result the body cites as "see supplement" but never summarizes —
  the 14 pages must stand alone.
- Squeezing overflow *method* description out of the body; a reader of only
  the main PDF must be able to reimplement the core.
- Adding experiments the frozen body never mentions, hoping reviewers credit
  them anyway.

## Supplement inventory for a vision paper

| Component | Why it earns its place | Packaging rule |
|---|---|---|
| Qualitative grids (success + failure) | Vision reviewers trust pixels over deltas | Same scenes across all baselines; no cherry-pick without a random-sample page |
| Video results | Temporal methods are unjudgeable from stills | Short, compressed, playable without exotic codecs |
| Per-dataset / per-category tables | Backs the body's averaged claims | Every table cross-referenced from the body |
| Full training recipes + configs | Reproducibility ledger overflow | Mirror the code archive; no contradictions with body numbers |
| Extra ablations | Answers the predictable "what about X?" review | One line each in the body's ablation discussion |
| Proof/derivation details | Rare at ECCV but present in geometry papers | Notation identical to the body |

## Anonymity scrub for supplement archives

Supplement uploads leak identity through channels the paper PDF does not:

```text
□ Video files: no institutional watermarks, no title slides with names
□ MP4/PDF metadata: author, tool, and GPS fields wiped
□ Code: paths (/home/<user>/, /cluster/<lab>/), git config, W&B entities
□ Screenshots: browser profiles, OS usernames, bookmark bars cropped out
□ Filenames: no lab acronyms or grant codes in archive member names
□ Prior-work assets: reused figures that only your group could possess
```

## Reviewer-attention model

Plan around discretionary reading: the qualitative PDF gets skimmed by most
reviewers, videos get opened when the paper is temporal, tables get opened
when a body claim looks suspicious, and code gets opened by at most one
reviewer. Therefore: put the persuasion (visual evidence) where skimming
lands, and the protection (recipes, breakdowns) where suspicion lands.

## Size and format constraints

Upload caps and allowed formats are set per cycle in OpenReview and were
not re-verified for 2026 (待核实) — check the submission form early, because
video compression to meet a cap takes an evening you do not want to
discover on March 11. Keep one master script that rebuilds the whole
supplement archive from sources so a size cut does not require manual
re-assembly.

## Output format

```text
[Supplement verdict] ready / thin / overloaded / body-dependent
[Inventory] <component -> present, cross-referenced from body?>
[Self-containment check] <body claims that lean on supplement-only material>
[Anonymity scrub] <leaks found -> fix>
[Deadline plan] <what lands March 5 vs the supplement week>
```
