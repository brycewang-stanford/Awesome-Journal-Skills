---
name: colm-supplementary
description: Use when deciding what goes into a COLM paper's appendices and supplementary material versus the strict 9-page main text — verbatim prompts, full evaluation configurations, per-task result tables, contamination analyses, human-evaluation protocols, and anonymized code/data packages that survive double-blind review.
---

# COLM Supplementary Material

The 2026 format gives you a strict 9-page main text, unlimited citation pages, and
appendix space whose guaranteed audience is *nobody* — reviewers may read it, the
rebuttal may point into it, but no rule obliges anyone to open it. That asymmetry is
the whole design principle: the main text carries every load-bearing element, and
the supplement carries the *audit trail* that makes the main text checkable.

## The placement rule

Ask of each artifact: *is this needed to believe the claim, or to re-run it?*
Believe → main text. Re-run → appendix/supplement. Both → summarize in the main
text, deposit fully in the appendix, and cross-reference in both directions.

| Artifact | Placement | Note |
|---|---|---|
| Representative prompt (or skeleton) | Main text | Readers cannot judge an LM evaluation without seeing how the model was asked |
| Full prompt set, verbatim, incl. system prompts | Appendix | Paraphrased prompts are not reproducible; include exact strings |
| Decoding configs per experiment | Appendix table | One row per reported table cell group (`colm-experiments`) |
| Contamination analysis method + results | Summary in main text; full in appendix | The *conclusion* is load-bearing; the n-gram machinery is audit trail |
| Per-task / per-model full result grids | Appendix | Main text shows the aggregate + the interesting slice |
| Human-eval protocol: instructions, pay, demographics, agreement | Appendix | Screenshots of annotator UI earn trust |
| Failure cases and transcripts | Appendix, curated | A dozen *representative* transcripts beat 400 raw ones |
| Code + data package | Supplementary upload / anonymized repo | Must be anonymous at submission (see below) |
| Raw API responses archive | Release artifact (acceptance) | Often too large for review upload; describe it and commit to release |

## LM-specific supplement content reviewers actually use

Three appendix sections repeatedly decide borderline LM papers:

1. **The prompt appendix.** Exact strings, exemplar counts, formatting whitespace
   included. Prompt paraphrase is a known variance source, so approximation here
   undermines every number.
2. **The "what we tried" ledger.** Prompt variants and hyperparameters attempted
   per system — the fairness evidence for baseline comparisons.
3. **The contamination appendix.** Overlap statistics per evaluation set, or the
   documented reason none could be computed.

## Anonymization of the code/data package

COLM's instructions ban identity-revealing links, and supplements are the usual
leak. Before upload, scrub: repository remotes and commit author fields (`git log`
travels inside `.git/`), Hugging Face org names in `from_pretrained(...)` calls,
W&B entity names in configs, API org IDs in cached headers, absolute paths
(`/home/<username>/...`), and internal cluster hostnames.

```bash
# Build the review package from a clean export — never zip a working directory
git archive --format=tar HEAD | (mkdir -p /tmp/colm-pkg && tar -x -C /tmp/colm-pkg)
grep -rniE 'wandb|hf_[A-Za-z0-9]{20,}|api[_-]?key|/home/[a-z]|<lab-name>' /tmp/colm-pkg | head
grep -rlE 'from_pretrained\("[^"]*/' /tmp/colm-pkg --include='*.py' | head   # org-scoped model IDs
(cd /tmp && zip -rq colm-supplement.zip colm-pkg -x '*.git*')
```

`git archive` (not `cp -r`) is the load-bearing choice: it cannot smuggle `.git/`,
untracked scratch files, or environment files into the package.

## Referencing the supplement from the main text

- Point at specific anchors ("App. C.2, Table 9"), never "see appendix".
- In the rebuttal window (May 22 - June 8 in 2026), precise anchors let you answer a
  reviewer in one sentence plus a pointer — the highest-leverage use of everything
  you deposited.
- Do not promise supplement content that is not there; reviewers who follow a
  dangling pointer stop trusting the intact ones.

## Ordering the appendix for the reader you hope exists

Appendices get opened with a question in hand, not read linearly. Order sections by
the probability of the question:

1. **A. Experimental details** — models, revisions, decoding configs, harness
   commit: the reproduction question.
2. **B. Prompts** — verbatim, grouped by experiment: the "how did you ask" question.
3. **C. Contamination analysis** — the trust question.
4. **D. Full results** — per-task, per-model grids: the "does it hold on X" question.
5. **E. Baseline tuning ledger** — the fairness question.
6. **F. Human/judge evaluation protocol** — instructions, agreement, biases.
7. **G. Failure analysis** — curated transcripts.
8. **H. Compute** — the cost question.

Within each, lead with a two-line summary of what the section shows — the reviewer
deciding whether to trust an unread appendix trusts one with visible structure. And
keep appendix numbering frozen after submission: the rebuttal will cite "App. C.2"
and a renumbered revision breaks every pointer in the discussion thread.

## What not to include

- Anything load-bearing that appears *only* in the supplement — if the 9 pages
  cannot make the case alone, restructure (`colm-writing-style`).
- Un-curated dumps (every transcript, every checkpoint) — volume without curation
  reads as evasion.
- Data whose license or ToS forbids redistribution — describe it and state the
  restriction instead (`colm-artifact-evaluation`).
- 待核实: no supplementary size cap was verifiable for 2026; check the OpenReview
  form's actual limits rather than assuming.

## Timing note for the 2026-style calendar

In 2026 the supplement traveled with the paper at the March 31 deadline — no
separate later upload was posted (待核实 whether future cycles add one). Plan
accordingly: the anonymization sweep and package build belong in deadline week's
T-3 slot (`colm-submission`), not in an imagined grace period. And because the
May 22 - June 8 rebuttal leans on appendix anchors, whatever you deposit in March
is the ammunition you will fight with in June — deposit for your future self, who
will be tired and have eighteen days.

## Output format

```text
[Placement audit] load-bearing content in supplement? none / move up: <items>
[Prompt appendix] verbatim + system prompts ▢   [Tried-ledger] ▢   [Contamination appendix] ▢
[Anonymity scan] clean / hits: <files>
[Pointer integrity] all anchors resolve / dangling: <refs>
[Package] built via clean export ▢  size: <n> MB (cap 待核实)
```
